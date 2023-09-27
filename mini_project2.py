### Utility Functions
import pandas as pd
import sqlite3
from sqlite3 import Error
import datetime

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


def create_table(conn, create_table_sql, drop_table_name=None):
    
    if drop_table_name: # You can optionally pass drop_table_name to drop the table. 
        try:
            c = conn.cursor()
            c.execute("""DROP TABLE IF EXISTS %s""" % (drop_table_name))
        except Error as e:
            print(e)
    
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

def insert_data(conn, sql_statement, values):
    cur = conn.cursor()
    with conn:
        cur.execute(sql_statement,values)



def step1_create_region_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None
    
    ### BEGIN SOLUTION
    conn = create_connection(normalized_database_filename, delete_db=False)
    create_table_sql = """CREATE TABLE Region(
                        RegionID Integer not null primary key,
                        Region Text not null)"""
    create_table(conn, create_table_sql, drop_table_name='Region')
    df = pd.read_csv(data_filename,delimiter='\t')
    data = [(i,) for i in df['Region'].drop_duplicates().to_list()]
    data.sort()
    sql_statement = """INSERT INTO Region(Region) VALUES(?)"""
    for i in data:
        insert_data(conn,sql_statement,i)
    ### END SOLUTION

def step2_create_region_to_regionid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    dict = {}
    conn = create_connection(normalized_database_filename, delete_db=False)
    data_fetch_sql = "SELECT RegionID, Region from Region"
    rows= execute_sql_statement(data_fetch_sql, conn)
    for i in rows:
        dict[i[1]] = i[0]
    return dict
    ### END SOLUTION


def step3_create_country_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None
    
    ### BEGIN SOLUTION
    conn = create_connection(normalized_database_filename, delete_db=False)
    create_table_sql = """CREATE TABLE Country(
                        CountryID Integer not null primary key,
                        Country Text not null,
                        RegionID integer not null,
                        FOREIGN KEY(RegionID) REFERENCES Region(RegionID))"""
    create_table(conn, create_table_sql, drop_table_name='Country')
    df = pd.read_csv(data_filename,delimiter='\t')
    region_dict = step2_create_region_to_regionid_dictionary(normalized_database_filename)
    region_id_func = lambda x: region_dict[x]
    df['RegionID'] = df['Region'].apply(region_id_func)
    df.sort_values('Country',inplace=True)
    df = df[['RegionID','Country']]
    df.drop_duplicates(inplace=True)
    print(df)
    sql_statement = """INSERT INTO Country(Country,RegionID) VALUES(?,?)"""
    for i in df[['Country', 'RegionID']].values:
        insert_data(conn, sql_statement, (i[0],i[1]))
    ### END SOLUTION


def step4_create_country_to_countryid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    dict = {}
    conn = create_connection(normalized_database_filename, delete_db=False)
    data_fetch_sql = "SELECT CountryID, Country from Country"
    rows= execute_sql_statement(data_fetch_sql, conn)
    for i in rows:
        dict[i[1]] = i[0]
    return dict
    ### END SOLUTION
        
        
def step5_create_customer_table(data_filename, normalized_database_filename):

    ### BEGIN SOLUTION
    conn = create_connection(normalized_database_filename, delete_db=False)
    create_table_sql = """CREATE TABLE Customer(
                        CustomerID Integer not null primary key,
                        FirstName Text not null,
                        LastName Text not null,
                        Address Text not null,
                        City Text not null,
                        CountryID integer not null,
                        FOREIGN KEY(CountryID) REFERENCES Country(CountryID))"""
    create_table(conn, create_table_sql, drop_table_name='Customer')
    df = pd.read_csv(data_filename,delimiter='\t')
    country_dict = step4_create_country_to_countryid_dictionary(normalized_database_filename)
    country_id_func = lambda x: country_dict[x]
    df['CountryID'] = df['Country'].apply(country_id_func)
    df.sort_values('Country',inplace=True)
    fname_split = lambda x: x.split(' ',1)[0]
    lname_split = lambda x: x.split(' ',1)[1]
    df['FirstName'] = df['Name'].apply(fname_split)
    df['LastName'] = df['Name'].apply(lname_split)
    df = df[['FirstName', 'LastName', 'Address', 'City', 'CountryID']]
    df.sort_values(['FirstName','LastName'],ascending=[True,True],inplace=True)
    df.drop_duplicates(inplace=True)
    sql_statement = """INSERT INTO Customer(FirstName, LastName, Address, City, CountryID) VALUES(?, ?, ?, ?, ?)"""
    for i in df.values:
        insert_data(conn, sql_statement, (i))
    ### END SOLUTION


def step6_create_customer_to_customerid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    dict = {}
    conn = create_connection(normalized_database_filename, delete_db=False)
    data_fetch_sql = "SELECT FirstName, LastName, CustomerID from Customer"
    rows= execute_sql_statement(data_fetch_sql, conn)
    for i in rows:
        dict[i[0] + ' ' + i[1]] = i[2]
    return dict
    ### END SOLUTION
        
def step7_create_productcategory_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None

    
    ### BEGIN SOLUTION
    conn = create_connection(normalized_database_filename, delete_db=False)
    create_table_sql = """CREATE TABLE ProductCategory(
                        ProductCategoryID Integer not null primary key,
                        ProductCategory Text not null,
                        ProductCategoryDescription Text not null)"""
    create_table(conn, create_table_sql, drop_table_name='ProductCategory')
    df = pd.read_csv(data_filename,delimiter='\t')
    df = df[['ProductCategory', 'ProductCategoryDescription']]
    df.drop_duplicates(inplace=True)
    df.sort_values('ProductCategory', inplace=True)
    sql_statement = """INSERT INTO ProductCategory(ProductCategory, ProductCategoryDescription) VALUES (?,?)"""
    data = []
    for i in df.values:
        x = i[0].split(';')
        y = i[1].split(';')
        for k in range(len(x)):
            tup = (x[k],y[k])
            if tup not in data:
                data.append(tup)
    data.sort(key=lambda x:x[0])                
    for i in data:
        insert_data(conn, sql_statement, (i))
        
    ### END SOLUTION

def step8_create_productcategory_to_productcategoryid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    dict = {}
    conn = create_connection(normalized_database_filename, delete_db=False)
    data_fetch_sql = "SELECT ProductCategory,ProductCategoryID from ProductCategory"
    rows= execute_sql_statement(data_fetch_sql, conn)
    for i in rows:
        dict[i[0]] = i[1]
    return dict
    ### END SOLUTION
        

def step9_create_product_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None

    ### BEGIN SOLUTION
    conn = create_connection(normalized_database_filename, delete_db=False)
    create_table_sql = """CREATE TABLE Product(
                        ProductID Integer not null primary key,
                        ProductName Text not null,
                        ProductUnitPrice Decimal not null,
                        ProductCategoryID integer not null,
                        FOREIGN KEY(ProductCategoryID) REFERENCES ProductCategory(ProductCategoryID))"""
    create_table(conn, create_table_sql, drop_table_name='Product')
    df = pd.read_csv(data_filename,delimiter='\t')
    productcategory_dict = step8_create_productcategory_to_productcategoryid_dictionary(normalized_database_filename)
    df = df[['ProductName', 'ProductUnitPrice', 'ProductCategory']]
    df.drop_duplicates(inplace=True)
    sql_statement = """INSERT INTO Product(ProductName, ProductUnitPrice, ProductCategoryID) VALUES (?,?,?)"""
    data = []
    for i in df.values:
        x = i[0].split(';')
        y = i[1].split(';')
        z = i[2].split(';')
        for k in range(len(x)):
            tup = (x[k],float(y[k]),productcategory_dict[z[k]])
            if tup not in data:
                data.append(tup)
    data.sort(key=lambda x:x[0])
    for i in data:
        insert_data(conn, sql_statement, (i))
    ### END SOLUTION


def step10_create_product_to_productid_dictionary(normalized_database_filename):
    
    ### BEGIN SOLUTION
    dict = {}
    conn = create_connection(normalized_database_filename, delete_db=False)
    data_fetch_sql = "SELECT ProductID,ProductName from Product"
    rows= execute_sql_statement(data_fetch_sql, conn)
    for i in rows:
        dict[i[1]] = i[0]
    return dict
    ### END SOLUTION
        

def step11_create_orderdetail_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None

    
    ### BEGIN SOLUTION
    conn = create_connection(normalized_database_filename, delete_db=False)
    create_table_sql = """CREATE TABLE OrderDetail(
                        OrderID Integer not null primary key,
                        CustomerID Integer not null,
                        ProductID Integer not null,
                        OrderDate Date not null,
                        QuantityOrdered integer not null,
                        FOREIGN KEY(CustomerID) REFERENCES Customer(CustomerID),
                        FOREIGN KEY(ProductID) REFERENCES Product(ProductID))"""
    create_table(conn, create_table_sql, drop_table_name='OrderDetail')
    df = pd.read_csv(data_filename,delimiter='\t')
    product_dict = step10_create_product_to_productid_dictionary(normalized_database_filename)
    customer_dict = step6_create_customer_to_customerid_dictionary(normalized_database_filename)
    df = df[['Name','ProductName', 'OrderDate', 'QuantityOrderded']]
    sql_statement = """INSERT INTO OrderDetail(CustomerID, ProductID, OrderDate, QuantityOrdered) VALUES (?,?,?,?)"""
    data = []
    for i in df.values:
        x = i[1].split(';')
        y = i[2].split(';')
        z = i[3].split(';')
        for k in range(len(x)):
            tup = (customer_dict[i[0]],product_dict[x[k]],datetime.datetime.strptime(y[k],'%Y%m%d').date(),int(z[k]))
            # if tup not in data:
            data.append(tup)
    data.sort(key=lambda x:x[0])
    cur = conn.cursor()
    with conn:
        cur.executemany(sql_statement,data)
    ### END SOLUTION


def ex1(conn, CustomerName):
    
    # Simply, you are fetching all the rows for a given CustomerName. 
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer and Product table.
    # Pull out the following columns. 
    # Name -- concatenation of FirstName and LastName
    # ProductName
    # OrderDate
    # ProductUnitPrice
    # QuantityOrdered
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- round to two decimal places
    # HINT: USE customer_to_customerid_dict to map customer name to customer id and then use where clause with CustomerID
    
    ### BEGIN SOLUTION
    sql_statement = f"""SELECT FirstName ||' ' ||LastName as Name
	, ProductName
	, OrderDate
	, ProductUnitPrice
	, QuantityOrdered
	, round(ProductUnitPrice * QuantityOrdered,2) as Total
FROM OrderDetail OD
INNER JOIN Customer C
ON OD.CustomerID = C.CustomerID
INNER JOIN Product P
ON OD.ProductID = P.ProductID WHERE Name = '{CustomerName}'"""
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex2(conn, CustomerName):
    
    # Simply, you are summing the total for a given CustomerName. 
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer and Product table.
    # Pull out the following columns. 
    # Name -- concatenation of FirstName and LastName
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round to two decimal places
    # HINT: USE customer_to_customerid_dict to map customer name to customer id and then use where clause with CustomerID
    
    ### BEGIN SOLUTION
    sql_statement = """    
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex3(conn):
    
    # Simply, find the total for all the customers
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer and Product table.
    # Pull out the following columns. 
    # Name -- concatenation of FirstName and LastName
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round to two decimal places
    # ORDER BY Total Descending 
    ### BEGIN SOLUTION
    sql_statement = """
    
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex4(conn):
    
    # Simply, find the total for all the region
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer, Product, Country, and 
    # Region tables.
    # Pull out the following columns. 
    # Region
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round to two decimal places
    # ORDER BY Total Descending 
    ### BEGIN SOLUTION

    sql_statement = """
    
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex5(conn):
    
     # Simply, find the total for all the countries
    # Write an SQL statement that SELECTs From the OrderDetail table and joins with the Customer, Product, and Country table.
    # Pull out the following columns. 
    # Country
    # CountryTotal -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round
    # ORDER BY Total Descending 
    ### BEGIN SOLUTION

    sql_statement = """

    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement


def ex6(conn):
    
    # Rank the countries within a region based on order total
    # Output Columns: Region, Country, CountryTotal, CountryRegionalRank
    # Hint: Round the the total
    # Hint: Sort ASC by Region
    ### BEGIN SOLUTION

    sql_statement = """
     
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement



def ex7(conn):
    
   # Rank the countries within a region based on order total, BUT only select the TOP country, meaning rank = 1!
    # Output Columns: Region, Country, CountryTotal, CountryRegionalRank
    # Hint: Round the the total
    # Hint: Sort ASC by Region
    # HINT: Use "WITH"
    ### BEGIN SOLUTION

    sql_statement = """
      
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex8(conn):
    
    # Sum customer sales by Quarter and year
    # Output Columns: Quarter,Year,CustomerID,Total
    # HINT: Use "WITH"
    # Hint: Round the the total
    # HINT: YOU MUST CAST YEAR TO TYPE INTEGER!!!!
    ### BEGIN SOLUTION

    sql_statement = """
       
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex9(conn):
    
    # Rank the customer sales by Quarter and year, but only select the top 5 customers!
    # Output Columns: Quarter, Year, CustomerID, Total
    # HINT: Use "WITH"
    # Hint: Round the the total
    # HINT: YOU MUST CAST YEAR TO TYPE INTEGER!!!!
    # HINT: You can have multiple CTE tables;
    # WITH table1 AS (), table2 AS ()
    ### BEGIN SOLUTION

    sql_statement = """
    
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex10(conn):
    
    # Rank the monthly sales
    # Output Columns: Quarter, Year, CustomerID, Total
    # HINT: Use "WITH"
    # Hint: Round the the total
    ### BEGIN SOLUTION

    sql_statement = """
      
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex11(conn):
    
    # Find the MaxDaysWithoutOrder for each customer 
    # Output Columns: 
    # CustomerID,
    # FirstName,
    # LastName,
    # Country,
    # OrderDate, 
    # PreviousOrderDate,
    # MaxDaysWithoutOrder
    # order by MaxDaysWithoutOrder desc
    # HINT: Use "WITH"; I created two CTE tables
    # HINT: Use Lag

    ### BEGIN SOLUTION

    sql_statement = """
     
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement