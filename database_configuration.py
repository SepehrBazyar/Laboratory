import json

from psycopg2 import connect
from psycopg2._psycopg import connection, cursor
import dbconfig

create_table_queries = []
insert_table_queries = []


# context manager for accessing database
class access_database:

    def __enter__(self):
        self.conn: connection = connect(dbconfig.config)
        self.curs: cursor = self.conn.cursor()
        return self.curs

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.curs.close()
        self.conn.close()


# creating test_info table query
create_table_queries.append("""CREATE TABLE test_info ( 
            test_name CHAR(50) NOT NULL,
            price INT,
            extra_data JSON NOT NULL,
            id SERIAL PRIMARY KEY);""")

# creating user_type table query
create_table_queries.append("""CREATE TABLE user_type (
            type char(20) NOT NULL, 
            extra_data JSON NULL,
            id SERIAL PRIMARY KEY);""")

# creating users table query
create_table_queries.append("""CREATE TABLE users (
            first_name CHAR(50) NOT NULL,
            last_name CHAR(50) NOT NULL,
            national_code char(10) UNIQUE NOT NULL , 
            phone CHAR(11) NOT NULL,
            email CHAR(100),
            password CHAR(100) NOT NULL,
            type_id INT NOT NULL,
            extra_data JSON NOT NULL,
            id SERIAL PRIMARY KEY,
            CONSTRAINT fk_type
               FOREIGN KEY(type_id) 
               REFERENCES user_type(id)
               ON DELETE SET NULL 
               ON UPDATE SET NULL);""")

# creating person tests query
create_table_queries.append("""CREATE TABLE tests (
            request_date DATE NOT NULL ,
            result_date DATE NOT NULL ,
            result JSON NOT NULL , 
            user_id INT NOT NULL , 
            test_info_id INT NOT NULL , 
            id serial PRIMARY KEY, 
            CONSTRAINT fk_user
               FOREIGN KEY(user_id) 
               REFERENCES users(id)
               ON DELETE SET NULL 
               ON UPDATE SET NULL,
            CONSTRAINT fk_test_info
               FOREIGN KEY(test_info_id) 
               REFERENCES test_info(id)
               ON DELETE SET NULL 
               ON UPDATE SET NULL);""")

patient_extra_data = json.dumps({"gender": "", "age": "", "blood_type": ""})
doctor_extra_data = json.dumps({"expertise": ""})
operator_extra_data = json.dumps({"licence": ""})

corona_extra_data = json.dumps({"rest_time": ""})
cbc_extra_data = json.dumps({"WBC": ""})
blood_extra_data = json.dumps({"HDL": ""})

# insert patient in user_type
insert_table_queries.append(
    [
        "INSERT INTO user_type (type, extra_data) VALUES (%s, %s);",
        ('patient', patient_extra_data)
    ]
)
# insert doctor in user_type
insert_table_queries.append(
    [
        "INSERT INTO user_type (type, extra_data) VALUES (%s, %s);",
        ('doctor', doctor_extra_data)
    ]
)
# insert operator in user_type
insert_table_queries.append(
    [
        "INSERT INTO user_type (type, extra_data) VALUES (%s, %s);",
        ('operator', operator_extra_data)
    ]
)

# insert corona in test_info
insert_table_queries.append(
    [
        "INSERT INTO test_info (test_name,price, extra_data) VALUES (%s, %s, %s);",
        ('corona', '500', corona_extra_data)
    ]
)

# insert cbc in test_info
insert_table_queries.append(
    [
        "INSERT INTO test_info (test_name,price, extra_data) VALUES (%s, %s, %s);",
        ('cbc', '200', cbc_extra_data)
    ]
)

# insert blood in test_info
insert_table_queries.append(
    [
        "INSERT INTO test_info (test_name,price, extra_data) VALUES (%s, %s, %s);",
        ('blood', '200', blood_extra_data)
    ]
)

# creating tables
with access_database() as database_cursor:
    for query in create_table_queries:
        database_cursor.execute(query)

# inserting data
with access_database() as database_cursor:
    for query in insert_table_queries:
        database_cursor.execute(query[0], query[1])
