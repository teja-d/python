import sqlite3

import numpy as np
import pandas as pd
from faker import Faker


def create_connection(db_file, delete_db=False):
    import os
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except Error as e:
        print(e)

    return conn


conn = create_connection('non_normalized.db')
sql_statement = "select * from Students;"
df = pd.read_sql_query(sql_statement, conn)
# print(df)


def create_df_degrees(non_normalized_db_filename):
    """
    Open connection to the non-normalized database and generate a 'df_degrees' dataframe that contains only
    the degrees. See screenshot below. 
    """

    # BEGIN SOLUTION
    conn = create_connection(non_normalized_db_filename)
    sql_statement = "SELECT DISTINCT Degree FROM Students;"
    df_degrees = pd.read_sql_query(sql_statement, conn)
    return df_degrees
    # END SOLUTION


def create_df_exams(non_normalized_db_filename):
    """
    Open connection to the non-normalized database and generate a 'df_exams' dataframe that contains only
    the exams. See screenshot below. Sort by exam!
    hints:
    # https://stackoverflow.com/a/16476974
    # https://stackoverflow.com/a/36108422
    """

    # BEGIN SOLUTION
    conn = create_connection(non_normalized_db_filename)
    sql_statement = "SELECT DISTINCT Exams FROM Students;"
    df_exams = pd.read_sql_query(sql_statement, conn)
    split_func = lambda x: [[i.strip().split(' ')[0].strip(),int(i.strip().split(' ')[1].replace('(','').replace(')','').strip())] for i in x['Exams'].strip().split(', ')]
    data = []
    for i in df_exams.apply(split_func,axis=1):
        for val in i:
            if val not in data:
                data.append(val)
        
    # print(data)
    df_exams2 = pd.DataFrame(data,columns=['Exam','Year'])
    df_exams2.sort_values(['Exam'],inplace=True)
    df_exams2.reset_index(drop=True,inplace=True)
    return df_exams2
    # return df_exams
    # END SOLUTION


def create_df_students(non_normalized_db_filename):
    """
    Open connection to the non-normalized database and generate a 'df_students' dataframe that contains the student
    first name, last name, and degree. You will need to add another StudentID column to do pandas merge.
    See screenshot below. 
    You can use the original StudentID from the table. 
    hint: use .split on the column name!
    """

    # BEGIN SOLUTION
    conn = create_connection(non_normalized_db_filename)
    sql_statement = "SELECT DISTINCT Name,Degree FROM Students;"
    df_students = pd.read_sql_query(sql_statement, conn)
    split_func1 = lambda x:x.strip().split(', ')[0]
    split_func2 = lambda x:x.strip().split(', ')[1]
    df_students['Last_Name'] = df_students['Name'].apply(split_func1)
    df_students['First_Name'] = df_students['Name'].apply(split_func2)
    df_students['StudentID'] = df.index + 1
    df_students = df_students[['StudentID','First_Name','Last_Name','Degree']]
    return df_students
    # END SOLUTION


def create_df_studentexamscores(non_normalized_db_filename, df_students):
    """
    Open connection to the non-normalized database and generate a 'df_studentexamscores' dataframe that 
    contains StudentID, exam and score
    See screenshot below. 
    """

    # BEGIN SOLUTION
    conn = create_connection(non_normalized_db_filename)
    sql_statement = "SELECT DISTINCT Name,Exams,Scores FROM Students;"
    df_ses = pd.read_sql_query(sql_statement, conn)
    df_final = pd.merge(df_students,df_ses,left_on=df_students.Last_Name+", "+df_students.First_Name, right_on=df_ses.Name)
    df_final = df_final[['StudentID','Exams','Scores']]
    exams_split = lambda x: [i.strip().split(' ')[0].strip() for i in x]
    df_final['Exams1'] = df_final['Exams'].str.split(', ')
    df_final['Exams1'] = df_final['Exams1'].apply(exams_split)
    df_final['Scores1'] = df_final['Scores'].str.split(', ')
    lambda_func = lambda x: [[x['Exams1'][i],int(x['Scores1'][i])]for i in range(len(x['Exams1']))]
    df_final['Exam_scores'] = df_final.apply(lambda_func,axis=1)
    df_final.reset_index(inplace=True,drop='index')
    df_final = df_final[['StudentID','Exam_scores']]
    df_f = df_final.explode(['Exam_scores'])
    df_f[['Exam','Score']] = pd.DataFrame(df_f.Exam_scores.to_list(),index=df_f.index)
    df_f.drop('Exam_scores',inplace=True,axis=1)
    df_f.reset_index(inplace=True,drop='index')
    return df_f
    # END SOLUTION


def ex1(df_exams):
    """
    return df_exams sorted by year
    """
    # BEGIN SOLUTION
    df_exams.sort_values('Year',inplace=True)
    # END SOLUTION
    return df_exams


def ex2(df_students):
    """
    return a df frame with the degree count
    # NOTE -- rename name the degree column to Count!!!
    """
    # BEGIN SOLUTION
    df = df_students['Degree'].value_counts().to_frame()
    df.columns = [['Count']]
    # END SOLUTION
    return df


def ex3(df_studentexamscores, df_exams):
    """
    return a datafram that merges df_studentexamscores and df_exams and finds the average of the exams. Sort
    the average in descending order. See screenshot below of the output. You have to fix up the column/index names.
    Hints:
    # https://stackoverflow.com/a/45451905
    # https://stackoverflow.com/a/11346337
    # round to two decimal places
    """

    # BEGIN SOLUTION
    df = pd.merge(df_studentexamscores,df_exams,left_on='Exam',right_on='Exam')
    df = df[['Exam','Year','Score']]
    df = df.groupby(['Exam','Year']).mean(['Score']).round(2)
    df = df.reset_index()
    df.columns = ['Exam','Year','average']
    df.sort_values('average',ascending=False,kind='mergesort',inplace=True)
    df = df.set_index(['Exam'])
    # END SOLUTION
    return df


def ex4(df_studentexamscores, df_students):
    """
    return a datafram that merges df_studentexamscores and df_exams and finds the average of the degrees. Sort
    the average in descending order. See screenshot below of the output. You have to fix up the column/index names.
    Hints:
    # https://stackoverflow.com/a/45451905
    # https://stackoverflow.com/a/11346337
    # round to two decimal places
    """

    # BEGIN SOLUTION
    df = pd.merge(df_studentexamscores,df_students,left_on='StudentID',right_on='StudentID')
    df = df[['Degree','Score']]
    df = df.groupby(['Degree']).mean(['Score']).round(2)
    df = df.reset_index()
    df.columns = ['Degree','Average']
    df.sort_values('Average',ascending=False,kind='mergesort',inplace=True)
    df = df.set_index(['Degree'])
    # END SOLUTION
    return df


def ex5(df_studentexamscores, df_students):
    """
    merge df_studentexamscores and df_students to produce the output below. The output shows the average of the top 
    10 students in descending order. 
    Hint: https://stackoverflow.com/a/20491748
    round to two decimal places

    """

    # BEGIN SOLUTION
    cols = ['First_Name','Last_Name','Degree']
    df = pd.merge(df_studentexamscores,df_students,left_on='StudentID',right_on='StudentID')
    df = df[['First_Name','Last_Name','Degree','Score']]
    df = df.groupby(cols).mean(['Score']).round(2)
    df = df.reset_index()
    df.columns = ['First_Name', 'Last_Name', 'Degree', 'average']
    df.sort_values(['average','Degree'],ascending=False,inplace=True)
    df = df.head(10)
    # END SOLUTION
    return df


# DO NOT MODIFY THIS CELL OR THE SEED

# THIS CELL IMPORTS ALL THE LIBRARIES YOU NEED!!!


np.random.seed(0)
fake = Faker()
Faker.seed(0)


def part2_step1():

    # ---- DO NOT CHANGE
    np.random.seed(0)
    fake = Faker()
    Faker.seed(0)
    # ---- DO NOT CHANGE

    # BEGIN SOLUTION
    data = [[f"{j[0][:2].lower()}{np.random.randint(1000,9999)}",j[0],j[1]] for j in [fake.name().split(' ',1) for i in range(100)]]
    df = pd.DataFrame(data,columns=['username','first_name','last_name'])
    return df
    # END SOLUTION
    


def part2_step2():

    # ---- DO NOT CHANGE
    np.random.seed(0)
    # ---- DO NOT CHANGE

    # BEGIN SOLUTION
    data = np.clip(np.round(np.random.normal(loc=[35,75,25,45,45,75,25,45,35],scale=[9,15,7,10,5,20,8,9,10],size=(100,9))),a_min=[0,0,0,0,0,0,0,0,0],a_max=[50,100,40,60,50,100,50,60,50])
    df = pd.DataFrame(data,columns=['Hw1','Hw2','Hw3','Hw4','Hw5','Exam1','Exam2','Exam3','Exam4'])
    return df
    # END SOLUTION


def part2_step3(df2_scores):
    # BEGIN SOLUTION
    df2_pivot = df2_scores.describe().transpose()
    standard_data = [['Hw1', 35, 9],['Hw2', 75, 15],['Hw3', 25, 7],['Hw4', 45, 10],['Hw5', 45, 5],['Exam1',75, 20],['Exam2',25, 8],['Exam3',45, 9],['Exam4',35, 10]]
    df_std = pd.DataFrame(standard_data,columns=['Name','mean_theoretical','std_theoretical'])
    # print(df_std)
    df2_pivot = df2_pivot.reset_index()
    df2_pivot = df2_pivot[['index','mean','std']]
    # print(type(df2_pivot))
    # print(type(df_std))
    # print(df2_pivot.columns)
    # print(df_std.columns)
    df_merged = pd.merge(df_std,df2_pivot,left_on='Name',right_on='index')
    df_merged.drop(['index'],inplace=True,axis=1)
    df_merged['abs_mean_diff'] = (df_merged['mean_theoretical'] - df_merged['mean']).abs()
    df_merged['abs_std_diff'] = (df_merged['std_theoretical'] - df_merged['std']).abs()
    df_merged = df_merged.round(2)
    df_merged = df_merged[['Name','mean','std','mean_theoretical','std_theoretical','abs_mean_diff','abs_std_diff']]
    df_merged = df_merged.set_index(['Name'])
    return df_merged
    # print(df2_scores.pivot_table())
    # END SOLUTION


def part2_step4(df2_students, df2_scores, ):
    # BEGIN SOLUTION
    max_scores = {'Hw1':50,'Hw2':100,'Hw3':40,'Hw4':60,'Hw5':50,'Exam1':100,'Exam2':50,'Exam3':60,'Exam4':50}
    df2_students = df2_students.reset_index()
    df2_scores = df2_scores.reset_index()
    df_final = pd.merge(df2_students,df2_scores,on='index')
    df_final.drop(['index'],inplace=True,axis=1)
    cols = df_final.columns
    for i in cols:
        if i in max_scores.keys():
            df_final[i] = df_final[i].divide(max_scores[i]).multiply(100).round(0)
    
    df_final.reset_index(drop=True,inplace=True)
    return df_final
    pass
    # END SOLUTION


def part2_step5():
    # BEGIN SOLUTION
    df = pd.read_csv('part2_step5-input.csv')
    cols = ['Hw1','Hw2','Hw3','Hw4','Hw5','Exam1','Exam2','Exam3','Exam4']
    # df['AI_Count'] = 0
    count_func = lambda x: 1 if x == 'AI_ISSUE' else 0
    for i in cols:
        df[i] = df[i].apply(count_func)
    df['AI_Count'] = df[cols[0]] + df[cols[1]] + df[cols[2]] + df[cols[3]] + df[cols[4]] + df[cols[5]] + df[cols[6]] + df[cols[7]] + df[cols[8]]
    df = df[df['AI_Count']!=0]
    df = df.reset_index(drop=True)
    df = df[['username','first_name','last_name','AI_Count']]
    # print(df)
    return df
    # END SOLUTION


def part2_step6():
    def letter(num):
        if num>=80:
            return 'A'
        elif num>=70:
            return 'B'
        elif num>=50:
            return 'C'
        elif num>=40:
            return 'D'
        return 'F'
    # BEGIN SOLUTION
    df = pd.read_csv('part2_step5-input.csv')
    df =  df.replace('AI_ISSUE',0) 
    hw_cols = ['Hw1', 'Hw2', 'Hw3', 'Hw4','Hw5']
    exam_cols = ['Exam1', 'Exam2', 'Exam3', 'Exam4']
    df[hw_cols] = df[hw_cols].astype('float')
    df[exam_cols ] = df[exam_cols ].astype('float')
    df['mean1'] = df[['Hw1', 'Hw2', 'Hw3', 'Hw4','Hw5']].mean(numeric_only=True,axis=1).round(0)
    df['mean2'] = df[['Exam1', 'Exam2', 'Exam3', 'Exam4']].mean(numeric_only=True,axis=1).round(0)
    for i in hw_cols:
        df[i] = df[i].fillna(df['mean1'])
    for i in exam_cols:
        df[i] = df[i].fillna(df['mean2'])
    df.drop(['mean1','mean2'],inplace=True,axis=1)
    df['Grade'] = round(df['Hw1'] * 0.05 + df['Hw2'] * 0.05 + df['Hw3'] * 0.05 + df['Hw4'] * 0.05 + df['Hw5'] * 0.05 + df['Exam1']*0.2 + df['Exam2']*0.2 + df['Exam3']*0.2 + df['Exam4'] * 0.15)
    letter_func = lambda x: letter(x)
    df['LetterGrade'] = df['Grade'].apply(letter_func)
    # df.drop()
    df_desc =df.describe().round().iloc[1:3]
    df_f = pd.concat([df,df_desc])
    return df_f
    # END SOLUTION
