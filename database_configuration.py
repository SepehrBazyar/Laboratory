from psycopg2 import connect
from psycopg2._psycopg import connection, cursor
import dbconfig

create_table_queries = []


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
            password CHAR(50) NOT NULL,
            type_id INT NOT NULL,
            id SERIAL PRIMARY KEY,
            CONSTRAINT fk_type
               FOREIGN KEY(type_id) 
               REFERENCES user_type(id)
               ON DELETE RESTRICT 
               ON UPDATE RESTRICT);""")

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
               ON DELETE RESTRICT 
               ON UPDATE RESTRICT,
            CONSTRAINT fk_test_info
               FOREIGN KEY(test_info_id) 
               REFERENCES test_info(id)
               ON DELETE RESTRICT 
               ON UPDATE RESTRICT);""")

# creating tables
with access_database() as database_cursor:
    for query in create_table_queries:
        database_cursor.execute(query)
