import psycopg2

try:
    connection=psycopg2.connect(
        user="postgres",
        password="kartik1234",
        host="localhost",
        port="5432",
        database="postgres_db"
        
    )
    cursor=connection.cursor()
    
    insert="""INSERT INTO mobile (kartik) VALUES ('Iphone12')"""
    
                      
    cursor.execute(insert)
    connection.commit()
    
except Exception as e:
    print(e)
    
finally:
    if connection:
        connection.close()
    
    