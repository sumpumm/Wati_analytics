from db.connection import db_connection

def insert_student(studentName, studentContact):
    conn = db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO student (
        studentName,
        studentContact
    )
    SELECT %s, %s
    WHERE NOT EXISTS (
        SELECT 1
        FROM student
        WHERE studentContact = %s
    )
    """

    cursor.execute(query, (studentName, studentContact, studentContact))
    conn.commit()
    cursor.close()
    conn.close()
    
def insert_operator(operatorName, operatorEmail, assignedId):
    conn = db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO operator (
        operatorName,
        operatorEmail,
        assignedId
    )
    SELECT %s, %s, %s
    WHERE NOT EXISTS (
        SELECT 1
        FROM operator
        WHERE assignedId = %s
    )
    """

    cursor.execute(
        query,
        (
            operatorName,
            operatorEmail,
            assignedId,
            assignedId
        )
    )

    conn.commit()
    cursor.close()
    conn.close()

    
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
    cursor.close()
    conn.close()
    
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
    cursor.close()
    conn.close()
    
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
    cursor.close()
    conn.close()