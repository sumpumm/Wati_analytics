from fastapi import FastAPI,Request,HTTPException
from utils import extract_operatorDetail,extract_senderDetails,extract_conversationDetails,extract_eventDetails

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
        
        extract_senderDetails(payload)
        extract_operatorDetail(payload)
        extract_conversationDetails(payload)
        extract_eventDetails(payload)
        
        # with open('messageReceived.txt','a',encoding="utf-8") as f:
        #     f.write(f"{payload}\n\n")
            
        # with open('messageSent.txt','a',encoding="utf-8") as f:
        #     f.write(f"{payload}\n\n")   
                 
        return {"message":"Data received"}
    except Exception as e:
        raise HTTPException(status_code=400,detail=e)

@app.post("/wati/webhook/messageSent")
async def message_sent(request:Request):
    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=400,detail=e)