from connection import db_connection

def create_student():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE student(id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, senderName VARCHAR(255), senderContact VARCHAR(20));')
    conn.commit()
    cursor.close()
    conn.close()
    
def create_operator():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE operatorDetails (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    operatorName VARCHAR(255),
    operatorEmail VARCHAR(255),
    assignedId VARCHAR(100)
);''')
    conn.commit()
    cursor.close()
    conn.close()
    
def create_messageReceived():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE messageReceived (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    conversationId VARCHAR(100),
    timestamp DOUBLE PRECISION,
    assignedId VARCHAR(100),
    sourceId VARCHAR(100),
    sourceUrl TEXT
);''')
    conn.commit()
    cursor.close()
    conn.close()
    
def create_messageSent():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE messageSent (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    conversationId VARCHAR(100),
    timestamp DOUBLE PRECISION,
    assigneeId VARCHAR(100)
    );''')
    conn.commit()
    cursor.close()
    conn.close()
    
def create_eventDetails():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE eventDetails (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    eventType VARCHAR(100),
    created DOUBLE PRECISION
    );''')
    conn.commit()
    cursor.close()
    conn.close()