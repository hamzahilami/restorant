import psycopg2


DB_NAME = "restaurant"
USER = "postgres" 
PASSWORD = "2002" 
HOST = "localhost"
PORT = "5432"

try:
    connection = psycopg2.connect(
        dbname = DB_NAME,
        user = USER,
        password = PASSWORD,
        host = HOST,
        port = PORT
    )
except Exception as e:
    print(f"Error: {e}")
cursor=connection.cursor()

class MenuItem:
    def __init__(self, name, price):
        self.name=name
        self.price=price
        
    def save(self):
        query=f'''insert into Menu_Items(item_name,item_price) 
        values ('{self.name}',{self.price})'''
        cursor.execute(query)
        connection.commit()
        
    def delete(self):
        query=f'''delete from Menu_Items where item_name=%s'''
        cursor.execute(query,(self.name,))
        connection.commit()
        
    def update(self ,new_name,new_price):
        query=f"update Menu_Items set item_name='{new_name}',item_price={new_price} where item_name='{self.name}'"
        cursor.execute(query)
        connection.commit()
        self.name=new_name
        self.price=new_price


    