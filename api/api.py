from fastapi import FastAPI,Request,HTTPException
from api.utils import extract_operatorDetail,extract_senderDetails,extract_messageReceieved,extract_messageSent,extract_eventDetails
from db.create import *

app = FastAPI()

@app.get("/status")
async def server_status():
    return {
        "statusCode":200,
        "message":"The server is live"}

@app.post("/wati/webhook/messageReceived")
async def message_received(request:Request):
    try:
        payload = await request.json()
        print(payload)
        
        #extract information
        a = extract_senderDetails(payload)
        b = extract_operatorDetail(payload)
        c = extract_messageReceieved(payload)
        d = extract_messageSent(payload)
        e = extract_eventDetails(payload)
        
        #save to database
        insert_student(a["studentName"],a["studentContact"])
        insert_operator(b["operatorName"],b["operatorEmail"],b["assignedId"])
        insert_message_received(c["conversationId"],c["timestamp"],c["assignedId"],c["sourceId"],c["sourceUrl"])
        insert_message_sent(d["conversationId"],d["timestamp"],d["assigneeId"])
        insert_event(e["eventType"],e["timestamp"])
        
        # with open('messageReceived.txt','a',encoding="utf-8") as f:
        #     f.write(f"{payload}\n\n")
            
        # with open('messageSent.txt','a',encoding="utf-8") as f:
        #     f.write(f"{payload}\n\n")   
                 
        return {"message":"Data received"}
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))

@app.post("/wati/webhook/messageSent")
async def message_sent(request:Request):
    try:
        payload = await request.json()
        print(payload)
        
        d = extract_messageSent(payload)
        insert_message_sent(d["conversationId"],d["timestamp"],d["assigneeId"])
        
        return {"message":"Data received"}
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))