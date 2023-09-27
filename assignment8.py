import pandas as pd
from datetime import *
import math

def ex1():
    """
    Reproduce ex1.tsv from 'AdmissionsCorePopulatedTable.txt'
    https://mkzia.github.io/eas503-notes/sql/sql_6_conditionals.html#conditionals
    Separate the columns by a tab
    """

    # BEGIN SOLUTION
    df = pd.read_csv('AdmissionsCorePopulatedTable.txt',delimiter='\t')
    month_func = lambda x: datetime.strftime(datetime.strptime(x,"%Y-%m-%d %H:%M:%S.%f"),"%B")
    df['AdmissionMonth'] = df['AdmissionStartDate'].apply(month_func)
    df_f = df.groupby(['AdmissionMonth'])['PatientID'].count()
    df_f = df_f.to_frame()
    df_f.reset_index(inplace=True)
    df_f.columns=['AdmissionMonth',	'AdmissionCount']
    df_f.sort_values(['AdmissionCount'],ascending=False,inplace=True)
    df_f.reset_index(drop=True,inplace=True)
    df_f.to_csv('ex1.tsv',sep='\t',index=False)
    # END SOLUTION


def ex2():
    """
    Repeat ex1 but add the Quarter column 
    This is the last SQL query on https://mkzia.github.io/eas503-notes/sql/sql_6_conditionals.html#conditionals
    Hint: https://stackoverflow.com/questions/60624571/sort-list-of-month-name-strings-in-ascending-order
    """

    # BEGIN SOLUTION
    def func(mon):
        if mon in ['January', 'February', 'March']:
            return 'Q1'
        elif mon in ['April', 'May', 'June']:
            return 'Q2'
        elif mon in ['July', 'August', 'September']:
            return 'Q3'
        return 'Q4'
    df = pd.read_csv('AdmissionsCorePopulatedTable.txt',delimiter='\t')
    month_func = lambda x: datetime.strftime(datetime.strptime(x,"%Y-%m-%d %H:%M:%S.%f"),"%B")
    month1_func = lambda x: datetime.strftime(datetime.strptime(x,"%B"),"%m")
    df['AdmissionMonth'] = df['AdmissionStartDate'].apply(month_func)
    df_f = df.groupby(['AdmissionMonth'])['PatientID'].count()
    df_f = df_f.to_frame()
    df_f.reset_index(inplace=True)
    df_f.columns=['AdmissionMonth',	'AdmissionCount']
    df_f.reset_index(drop=True,inplace=True)
    quarter_lambda = lambda x: func(x)
    df_f['Quarter'] = df_f['AdmissionMonth'].apply(quarter_lambda)
    df_f['month_num'] = df_f['AdmissionMonth'].apply(month1_func).astype('int32')
    # print(df_f)
    df_f.sort_values(['month_num'],inplace=True)
    df_f.reset_index(drop=True,inplace=True)
    df_f = df_f[['Quarter','AdmissionMonth','AdmissionCount']]    
    df_f.to_csv('ex2.tsv',sep='\t',index=False)
    # END SOLUTION


def ex3():
    """
    Reproduce 
    SELECT
        LabsCorePopulatedTable.PatientID,
        PatientCorePopulatedTable.PatientGender,
        LabName,
        LabValue,
        LabUnits,
        CASE
            WHEN PatientCorePopulatedTable.PatientGender = 'Male'
            AND LabValue BETWEEN 0.7
            AND 1.3 THEN 'Normal'
            WHEN PatientCorePopulatedTable.PatientGender = 'Female'
            AND LabValue BETWEEN 0.6
            AND 1.1 THEN 'Normal'
            ELSE 'Out of Range'
        END Interpretation
    FROM
        LabsCorePopulatedTable
        JOIN PatientCorePopulatedTable ON PatientCorePopulatedTable.PatientID = LabsCorePopulatedTable.PatientID
    WHERE
        LabName = 'METABOLIC: CREATININE'
    ORDER BY
        - LabValue

    using PatientCorePopulatedTable.txt and LabsCorePopulatedTable

    **** ADD  LabDateTime
    **** SORT BY Patient ID and then LabDateTime in ascending order 
    """
    # BEGIN SOLUTION
    def func(x,y):
        if x=='Male' and 0.7 <= y <= 1.3:
            return 'Normal'
        elif x=='Female' and 0.6 <= y <= 1.1:
            return 'Normal'
        return 'Out of Range'
    df_labs = pd.read_csv('LabsCorePopulatedTable.txt',delimiter='\t')
    df_patient = pd.read_csv('PatientCorePopulatedTable.txt',delimiter='\t')
    df_join = df_labs.merge(df_patient,on='PatientID')
    df_f = df_join[df_join.LabName=='METABOLIC: CREATININE']
    df_f['Interpretation'] = [func(x,y) for x,y in zip(df_f['PatientGender'],df_f['LabValue'])]
    df_f = df_f[['PatientID', 'PatientGender', 'LabName', 'LabValue', 'LabUnits','LabDateTime','Interpretation']]
    temp_list = df_f['LabValue'].values.tolist()
    for i in range(len(temp_list)):
        if temp_list[i]==1.0:
            print(temp_list[i])
            temp_list[i]=str(1)

    df_f['LabValue'] = temp_list
    df_f.sort_values(['PatientID','LabDateTime'],inplace=True)
    df_f.to_csv('ex3.tsv',sep='\t',index=False)
    # print(df_f)
    # END SOLUTION


def ex4():
    """
    Reproduce this
    WITH AGE AS (
        SELECT 
            PATIENTID,
            ROUND((JULIANDAY('NOW') - JULIANDAY(PATIENTDATEOFBIRTH))/365.25) AGE
        FROM 
            PATIENTCOREPOPULATEDTABLE
    )
    SELECT 
        CASE 
            WHEN AGE < 18 THEN 'YOUTH'
            WHEN AGE BETWEEN 18 AND 35 THEN 'YOUNG ADULT'
            WHEN AGE BETWEEN 36 AND 55 THEN 'ADULT'
            WHEN AGE >= 56 THEN 'SENIOR'
        END AGE_RANGE,
        COUNT(*) AGE_RANGE_COUNT
    FROM 
        AGE
    GROUP BY AGE_RANGE
    ORDER BY AGE

    ****** VERY IMPORTANT: Use the Date: 2022-12-11 as today's date!!!! VERY IMPORTANT otherwise your result will change everyday!
    ****** VERY IMPORTANT divide the number of days by 365.25; to get age do math.floor(delta.days/365.25), where delta days is now-dob

    """
    # BEGIN SOLUTION
    def gen_calc(x):
        if x<18:
            return 'YOUTH'
        elif x<=35:
            return 'YOUNG ADULT'
        elif x<=55:
            return 'ADULT'
        return 'SENIOR'
    df_patient = pd.read_csv('PatientCorePopulatedTable.txt',delimiter='\t')
    date_func = lambda x: math.floor((datetime.strptime('2022-12-11',"%Y-%m-%d") - datetime.strptime(x,"%Y-%m-%d %H:%M:%S.%f")).days/365.25)
    df_patient['AGE'] = df_patient['PatientDateOfBirth'].apply(date_func)
    df_patient['AGE_RANGE'] = df_patient['AGE'].apply(gen_calc)
    df_f = df_patient.groupby(['AGE_RANGE'])['AGE'].count()
    df_f = df_f.reset_index()
    df_f.columns = ['AGE_RANGE', 'AGE_RANGE_COUNT']
    df_f.sort_values(['AGE_RANGE_COUNT'],inplace=True)
    df_f.to_csv('ex4.tsv',sep='\t',index=False)
    # END SOLUTION
