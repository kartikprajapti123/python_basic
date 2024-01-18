import psycopg2


try:
    connection=psycopg2.connect(
        host="localhost",  
        port="5432",
        user="postgres", 
        password="kartik1234", 
        database="postgres_db"
    
    )
    cursor=connection.cursor()
    
    query="""CREATE TABLE STUDENTS(
            ID INT PRIMARY KEY NOT NULL,
            NAME VARCHAR NOT NULL,
            ROLLNO INT NOT NULL,
            ADDRESS VARCHAR NOT NULL
        );""" 
    cursor.execute(query)
    connection.commit()
    
    
    query="""INSERT INTO STUDENTS (ID,NAME,ROLLNO,ADDRESS) VALUES(2,'kartik',29,'xyz')"""
    cursor.execute(query)
    connection.commit()
    
    query="""SELECT name FROM STUDENTS where name='kartik'"""
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print(i)
    connection.commit()
    
    
    query="""SELECT * FROM STUDENTS where name='kartik'"""
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print(i)
    connection.commit()
    
    query="""UPDATE STUDENTS SET ID=10 WHERE ID=1"""
    cursor.execute(query)
    connection.commit()
    
    query="""DELETE FROM STUDENTS WHERE ID=10"""
    cursor.execute(query)
    connection.commit()
    
    data=[(112,"kaeti",12,"sd"),(12,"smdms",12,"df"),(25,"smdms",12,"df")]
    query="""INSERT INTO STUDENTS (id,name,rollno,address) values(%s,%s,%s,%s)"""
    cursor.executemany(query,data)
    connection.commit()
    
    data=[(101,"kartik101",10),(102,"kartik102",12)]
    query="""UPDATE STUDENTS SET ID=%s,NAME=%s where id=%s"""
    cursor.executemany(query,data)
    connection.commit()
    
    
    data=[(101,),(102,)]
    query="""DELETE FROM STUDENTS WHERE ID=%s"""
    cursor.executemany(query,data)
    connection.commit()
    
    
except Exception as e:
    print(e)

finally:
    if connection:
        connection.close()
        
    if cursor:
        cursor.close()