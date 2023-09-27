import pandas as pd
import sqlite3
from sqlite3 import Error

conn_orders = sqlite3.connect("orders.db")
cur = conn_orders.cursor()

# sql_statement = "select * from customers;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from orders;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from vendors;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from products;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from orderitems;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from productnotes;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)


def ex1():
    # Write an SQL statement that SELECTs all rows from the `customers` table
    # output columns: cust_name, cust_email

    ### BEGIN SOLUTION
    sql_statement = "SELECT cust_name, cust_email from customers"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex2():
    # Write an SQL statement that SELECTs all rows from the `products` table
    # output columns: vend_id

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id from products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex3():
    # Write an SQL statement that SELECTs distinct rows for vend_id from the `products` table
    # output columns: vend_id

    ### BEGIN SOLUTION
    sql_statement = "SELECT distinct vend_id from products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex4():
    # Write an SQL statement that SELECTs the first five rows from the `products` table
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name from products limit 5"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex5():
    # Write an SQL statement that SELECTs 4 rows starting from row 3 from `products` table
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "select prod_name from products where ROWID BETWEEN 4 and 7"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex6():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_name
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name from products order by prod_name"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex7():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_price and then prod_name 
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products order by prod_price,prod_name"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex8():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_price (descending order)
    # and then prod_name 
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products ORDER By prod_price desc,prod_name"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex9():
    # Write an SQL statement that SELECTs all rows from `products` table where the price of product is 2.50
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name from products where prod_price=2.50"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex10():
    # Write an SQL statement that SELECTs all rows from `products` table where the name of product is Oil can
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products where prod_name='Oil can'"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex11():
    # Write an SQL statement that SELECTs all rows from `products` table where the price of product is 
    # less than or equal to 10
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products where prod_price<=10" 
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex12():
    # Write an SQL statement that SELECTs all rows from `products` table where the vendor id is not equal to 1003
    # output columns: vend_id, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_name FROM products where vend_id<>1003"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex13():
    # Write an SQL statement that SELECTs all rows from `products` table where the product prices are between 5 and 10
    # output columns: prod_name, prod_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_name, prod_price FROM products where prod_price between 5 and 10"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex14():
    # Write an SQL statement that SELECTs all rows from the `customers` table where the customer email is empty
    # output columns: cust_id, cust_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT cust_id, cust_name from customers where cust_email is null "
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex15():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1003 and
    # the price is less than or equal to 10. 
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name from products where vend_id=1003 and prod_price<=10"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex16():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1002 or 1003 and
    # the price is greater than or equal to 5. 
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name from products where vend_id in (1002,1003) and prod_price>=5"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex17():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1002 or 1003 or 1005.
    # Use the IN operator for this!
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name from products where vend_id in (1002,1003,1005)"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex18():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is NOT 1002 or 1003.
    # Use the NOT IN operator for this!
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT vend_id, prod_id, prod_price, prod_name from products where vend_id not in (1002,1003)"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex19():
    # Write an SQL statement that SELECTs all rows from the `products` table where the product name starts with 'jet'
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name from products where prod_name like 'jet%'"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex20():
    # Write an SQL statement that SELECTs all rows from the `products` table where the product name ends with 'anvil'
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, prod_price, prod_name FROM products where prod_name like '%anvil'"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex21():
    # Write an SQL statement that SELECTs all rows from the `vendors` table. Concatenate vendor name and vendor country
    # as vend_title. Order by vend_title. Leave space in between -- example `ACME (USA)`
    # output columns: vend_title

    ### BEGIN SOLUTION
    sql_statement = "select vend_name || ' (' || vend_country || ')' vend_title from vendors order by vend_title"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex22():
    # Write an SQL statement that SELECTs all rows from the `orderitems` table where order number is 20005. 
    # Display an extra calculated column called `expanded_price` that is the result of quantity multiplied by item_price.
    # Round the value to two decimal places. 
    # output columns: prod_id, quantity, item_price, expanded_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT prod_id, quantity, item_price, round(quantity*item_price,2) as expanded_price FROM orderitems where order_num=20005"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex23():
    # Write an SQL statement that SELECTs all rows from the `orders` table where the order date is between 
    # 2005-09-13 and 2005-10-04
    # output columns: order_num, order_date
    # https://www.sqlitetutorial.net/sqlite-date-functions/sqlite-date-function/
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT order_num, order_date from orders where order_date between '2005-09-13' and '2005-10-04'"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex24():
    # Write an SQL statement that calculates the average price of all rows in the `products` table. 
    # Call the average column avg_price
    # output columns: avg_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT avg(prod_price) avg_price from products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex25():
    # Write an SQL statement that calculates the average price of all rows in the `products` table 
    # where the vendor id is 1003 . Call the average column avg_price
    # output columns: avg_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT avg(prod_price) avg_price from products where vend_id=1003"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement



def ex26():
    # Write an SQL statement that counts the number of customers in the `customers` table 
    # Call the count column num_cust
    # output columns: num_cust

    ### BEGIN SOLUTION
    sql_statement = "select count(*) num_cust from customers"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex27():
    # Write an SQL statement that calculates the max price in the `products` table 
    # Call the max column max_price. Round the value to two decimal places. 
    # output columns: max_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT round(max(prod_price),2) as max_price from products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex28():
    # Write an SQL statement that calculates the min price in the `products` table 
    # Call the min column min_price. Round the value to two decimal places. 
    # output columns: min_price

    ### BEGIN SOLUTION
    sql_statement = "SELECT round(min(prod_price),2) as min_price from products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex29():
    # Write an SQL statement that sums the quantity in the `orderitems` table where order number is 20005. 
    # Call the sum column items_ordered
    # output columns: items_ordered

    ### BEGIN SOLUTION
    sql_statement = "SELECT sum(quantity) items_ordered from orderitems where order_num=20005"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


#---------------------------------------------------------------------------------------------------------------------------------------------#

# You cannot use Pandas! I will deduct points after manual check if you use Pandas. You CANNOT use the 'csv' module to read the file

# Hint: Ensure to strip all strings so there is no space in them

# DO NOT use StudentID from the non_normalized table. Let the normalized table automatically handle StudentID. 


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


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def execute_sql_statement(sql_statement, conn):
    cur = conn.cursor()
    cur.execute(sql_statement)
    rows = cur.fetchall()
    return rows

# conn_non_normalized = create_connection('non_normalized.db')
# sql_statement = "select * from Students;"
# df = pd.read_sql_query(sql_statement, conn_non_normalized)
# display(df)

def insert_data(sql_statement,values,conn):
    cur = conn.cursor()
    cur.execute(sql_statement,values)
    # print("data_inserted")
    return cur.lastrowid

def normalize_database(non_normalized_db_filename):
#     Normalize 'non_normalized.db'
#     Call the normalized database 'normalized.db'
#     Function Output: No outputs
#     Requirements:
#     Create four tables
#     Degrees table has one column:
#         [Degree] column is the primary key
    
#     Exams table has two columns:
#         [Exam] column is the primary key column
#         [Year] column stores the exam year
    
#     Students table has four columns:
#         [StudentID] primary key column 
#         [First_Name] stores first name
#         [Last_Name] stores last name
#         [Degree] foreign key to Degrees table
        
#     StudentExamScores table has four columns:
#         [PK] primary key column,
#         [StudentID] foreign key to Students table,
#         [Exam] foreign key to Exams table ,
#         [Score] exam score

    
    ### BEGIN SOLUTION
    db_file = 'normalized.db'
    conn = create_connection(db_file, delete_db=False)
    conn_old = create_connection(non_normalized_db_filename, delete_db=False)

    drop_query = lambda x:execute_sql_statement(f"DROP TABLE IF EXISTS {x}", conn)
    create_query = lambda x:create_table(conn, x)

    # Drop tables
    drop_query('StudentExamScores')
    drop_query('Students')
    drop_query('Exams')
    drop_query('Degree')

    # Create Tables
    # Degree Table
    degree_ddl = """CREATE TABLE Degree(Degree VARCHAR PRIMARY KEY)"""
    create_query(degree_ddl)
    
    # Exams table
    exams_ddl = """CREATE TABLE Exams
                        (Exam VARCHAR PRIMARY KEY,
                        Year BIGINT)"""
    create_query(exams_ddl)
    
    # Students table
    students_ddl = """CREATE TABLE Students
                        (StudentID INTEGER NOT NULL PRIMARY KEY,
                            First_Name VARCHAR,
                            Last_Name VARCHAR,
                            Degree VARCHAR,
                            FOREIGN KEY(Degree) REFERENCES Degree(Degree))"""
    create_query(students_ddl)

    # StudentExamScores table
    ses_ddl = """CREATE TABLE StudentExamScores
                        (PK INTEGER NOT NULL PRIMARY KEY,
                            StudentID INTEGER,
                            Exam VARCHAR,
                            Score DECIMAL,
                            FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
                            FOREIGN KEY(Exam) REFERENCES Exams(Exam)
                        )"""
    create_query(ses_ddl)

    # Load data
    # Degree
    fetch_degrees = "SELECT distinct Degree FROM Students"
    degree_data = execute_sql_statement(fetch_degrees, conn_old)
    insert_degrees = "INSERT INTO Degree(Degree) Values(?)"
    with conn:
        for i in degree_data:
            insert_data(insert_degrees,i,conn)
    
    # Exams data
    fetch_exams = "SELECT distinct Exams FROM Students"
    exams_data = execute_sql_statement(fetch_exams, conn_old)
    exams = []
    for i in exams_data:
        for val in i[0].split(','):
            val = val.strip()
            exam = (val.split(' ')[0].strip(),int(val.split(' ')[1].replace('(','').replace(')','').strip()))
            if exam not in exams:
                exams.append(exam)
    insert_exams = "INSERT INTO Exams(Exam,Year) Values(?,?)"
    with conn:
        for i in exams:
            insert_data(insert_exams,i,conn)

    # Students data
    fetch_students = """SELECT Name, Degree FROM Students"""
    students_data = execute_sql_statement(fetch_students, conn_old)
    students = []
    for i in students_data:
        lname,fname = i[0].strip().split(', ')
        students.append((fname.strip(),lname.strip(),i[1].strip()))
    print(students)
    insert_students = "INSERT INTO Students(First_Name,Last_Name,Degree) Values(?,?,?)"
    with conn:
        for i in students:
            insert_data(insert_students,i,conn)

    # Creating fk dict for students table
    fk_dict_query = """SELECT StudentId, First_Name || '_' || Last_Name from Students"""
    fk_dict_data = execute_sql_statement(fk_dict_query, conn)
    fk_students = {}
    for i in fk_dict_data:
        fk_students[i[1]] = i[0]
    # print(fk_students)

    # Ses data
    ses_fetch_query = """SELECT Name, Exams, Scores from Students"""
    ses_old_data = execute_sql_statement(ses_fetch_query, conn_old)
    ses_data = []
    for i in ses_old_data:
        sid = fk_students["_".join(reversed([name.strip() for name in (i[0].strip().split(', '))]))]
        exam_scores = zip([exam.strip().split(' ')[0].strip() for exam in (i[1].strip().split(', '))],[float(score.strip()) for score in (i[2].strip().split(', '))])
        for exam_score in exam_scores:
            ses_data.append((sid,exam_score[0],exam_score[1]))
    # print(ses_data[:3])
    insert_ses = "INSERT INTO StudentExamScores(StudentID, Exam, Score) Values(?,?,?)"
    with conn:
        for i in ses_data:
            insert_data(insert_ses,i,conn)
    ### END SOLUTION
        
    
# normalize_database('non_normalized.db')
# conn_normalized = create_connection('normalized.db')

def ex30(conn):
    # Write an SQL statement that SELECTs all rows from the `Exams` table and sort the exams by Year
    # output columns: exam, year
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT exam, year FROM Exams order by Year,Exam"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex31(conn):
    # Write an SQL statement that SELECTs all rows from the `Degrees` table and sort the degrees by name
    # output columns: degree
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT degree from Degree order by degree"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex32(conn):
    # Write an SQL statement that counts the numbers of gradate and undergraduate students
    # output columns: degree, count_degree
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT degree,count(*) count_degree from Students group by 1 order by 1;"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex33(conn):
    # Write an SQL statement that calculates the exam averages for exams; sort by average in descending order.
    # output columns: exam, year, average
    # round to two decimal places
    
    
    ### BEGIN SOLUTION
    sql_statement = """SELECT e.exam, year, round(avg(score),2) average
                        FROM Exams e
                        INNER JOIN StudentExamScores ses
                            ON e.Exam=ses.Exam
                        GROUP BY e.exam,year
                        ORDER BY average desc"""
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex34(conn):
    # Write an SQL statement that calculates the exam averages for degrees; sort by average in descending order.
    # output columns: degree, average 
    # round to two decimal places
    
    ### BEGIN SOLUTION
    sql_statement = """SELECT degree, round(avg(score),2) average 
                        FROM Students s
                        INNER JOIN StudentExamScores ses
                            ON s.StudentId = ses.StudentId
                        GROUP BY degree
                        ORDER BY average DESC"""
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement

def ex35(conn):
    # Write an SQL statement that calculates the exam averages for students; sort by average in descending order. Show only top 10 students
    # output columns: first_name, last_name, degree, average
    # round to two decimal places
    # Order by average in descending order
    # Warning two of the students have the same average!!!
    
    ### BEGIN SOLUTION
    sql_statement = """SELECT first_name, last_name, degree, round(avg(score),2) average
                            FROM Students s
                            INNER JOIN StudentExamScores ses
                                ON s.StudentId=ses.StudentId
                            GROUP BY first_name, last_name, degree
                            ORDER BY average DESC
                            LIMIT 10"""
    ### END SOLUTION 
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement
