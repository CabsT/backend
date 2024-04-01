from psycopg2.pool import SimpleConnectionPool



conn_pool = SimpleConnectionPool(
    1, 80, 
    database = "datatex",
    user = "postgres",
    password = "Girlcode@123",
    host ="localhost",
    port = "5432",
    
    )


class Database:
    def __init__(self, table):
        self.table = table
        self.pool = conn_pool

    def insert(self, login_data):
       conn = self.pool.getconn()
       cursor = conn.cursor() 
       insert_query =  f"INSERT INTO {self.table} (login, password) VALUES (%s, %s)"
       
       cursor.execute(insert_query, (login_data['login'], login_data['password']))
           
       conn.commit()
    
       self.pool.putconn(conn)
    