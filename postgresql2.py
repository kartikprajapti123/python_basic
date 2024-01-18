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
    
    query="""CREATE TABLE NEW(
        ID INT PRIMARY KEY NOT NULL,
        NAME CHAR NOT NULL,
        STD INT NULL
    );"""
    cursor.execute(query)
    connection.commit()
    query="""INSERT INTO new (id,name,std) values (%s,%s,%s)"""
    values=(4,"kartik",2)
    cursor.execute(query,values)
    connection.commit()   
     
    
    query="""SELECT * FROM new """
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)
    for i in data:
        print(i)
        
        
        
    data=[(10,"Gautam",12),(20,"kartik",10)]
    query=f"""INSERT INTO NEW (id,name,std) VALUES (%s,%s,%s)"""
    
    query=cursor.executemany(query,data)
    connection.commit()
    
    
    query=""" UPDATE new SET id=10 where id=1 """
    cursor.execute(query)
    connection.commit()
    
    
    update=[("kartik1234","k")]
    query="""UPDATE NEW SET name=%s WHERE name=%s"""
    cursor.executemany(query,update)
    connection.commit()
    
    
    query="""DELETE FROM new WHERE id=10"""
    cursor.execute(query)
    connection.commit()
    
    
    data_to_delete=[(10,),(2,),(3,)]
    query="""DELETE FROM new where id = %s"""
    cursor.executemany(query,data_to_delete)
    connection.commit()
    
    
except Exception as e:
    print(e)
    
    
finally:
    if connection:
        connection.close()
        
    if cursor:
        cursor.close()