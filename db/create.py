from db.connection import db_connection

def insert_student(studentName, studentContact):
    conn=db_connection()
    cursor=conn.cursor()
    query = """
    INSERT INTO student(
        studentName,
        studentContact
    )
    VALUES (%s, %s)
    """

    cursor.execute(query, (studentName, studentContact))
    conn.commit()
    
def insert_operator(operatorName, operatorEmail, assignedId):
    conn=db_connection()
    cursor=conn.cursor()
    query = """
    INSERT INTO operator (
        operatorName,
        operatorEmail,
        assignedId
    )
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (operatorName, operatorEmail, assignedId)
    )
    conn.commit()
    
def insert_message_received(conversationId,timestamp,assignedId,sourceId,sourceUrl):
    conn=db_connection()
    cursor=conn.cursor()
    query = """
    INSERT INTO messageReceived (
        conversationId,
        timestamp,
        assignedId,
        sourceId,
        sourceUrl
    )
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            conversationId,
            timestamp,
            assignedId,
            sourceId,
            sourceUrl
        )
    )

    conn.commit()
    
def insert_message_sent(conversationId,timestamp,assigneeId):
    conn=db_connection()
    cursor=conn.cursor()
    query = """
    INSERT INTO messageSent (
        conversationId,
        timestamp,
        assigneeId
    )
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (
            conversationId,
            timestamp,
            assigneeId
        )
    )

    conn.commit()
    
def insert_event(eventType,created):
    conn=db_connection()
    cursor=conn.cursor()
    query = """
    INSERT INTO eventDetails (
        eventType,
        created
    )
    VALUES (%s, %s)
    """

    cursor.execute(
        query,
        (
            eventType,
            created
        )
    )

    conn.commit()