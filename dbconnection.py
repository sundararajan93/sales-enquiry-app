import pymysql

def db_connect(dbhost, username, password, dbname):
    global cursor
    global connect

    try:
        connect = pymysql.connect(host=dbhost, user=username, password=password, database=dbname)
        cursor = connect.cursor()
        print("DB Connected Succesfully!!!")        
    except Exception as e:
        print(f"Something went wrong! Unable to connect to {dbhost}", e)
        

def create_table(table_name):
    try:
        create_table_query = """CREATE TABLE IF NOT EXISTS %s(
        _id INT AUTO_INCREMENT PRIMARY KEY, 
        agentName VARCHAR(40),
        customerName VARCHAR(40),
        companyName VARCHAR(50),
        address VARCHAR(250),
        contactNumber VARCHAR(15),
        emailId VARCHAR(50),
        requirement VARCHAR(500)
        )"""%(table_name)
        cursor.execute(create_table_query)
        print(f"{table_name} table is ready to use!!!")
    except Exception as e:
        print("Unable to create Table" ,e)

def delete_table(table_name, data_only):
    if data_only:
        try:
            delete_table_query = "TRUNCATE TABLE %s"%(table_name)
            cursor.execute(delete_table_query)
            print(f"{table_name} Table Data Deleted")
        except Exception as e:
            print("Unable to delete table data", e)
    else:
        try:
            delete_table_query = "DROP TABLE %s"%(table_name)
            cursor.execute(delete_table_query)
            print(f"{table_name} Table deleted")
        except Exception as e:
            print("Unable to delete the Table", e)

def insert_enquiry_data(table_name, values):
    try:
        insert_data_query = """INSERT INTO {}(agentName, customerName, companyName, address, 
        contactNumber, emailId, requirement) 
        values(%s, %s, %s, %s, %s, %s, %s)""".format(table_name)
        cursor.execute(insert_data_query, values)
        connect.commit()
        print("Data inserted successfully to the tablename")
    except Exception as e:
        connect.rollback()
        print("Unable to Insert Data", e)

def read_table_data(table_name):
    try:
        query = """select * from %s"""%(table_name)
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print("Unable to fetch records!!!", e)

DBHOST = "localhost"
DBUSER = "root"
DBPASS = "password@321"
DBNAME = "sales"

# To connect to the DB
# db_connect(DBHOST, DBUSER, DBPASS, DBNAME)

# To create table
# create_table("enquiry1")

# To delete table Data only
# delete_table("enquiry", True)

# To delete table completely
# delete_table("enquiry", False)

# Reading Values in table
# for i in read_table_data("enquiry"):
#     print(i)
