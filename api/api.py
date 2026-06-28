from fastapi import FastAPI,Request,HTTPException
from utils import extract_operatorDetail,extract_senderDetails,extract_conversationDetails

app = FastAPI()

@app.post("/wati/webhook")
async def wati_webhook(request:Request):
    try:
        payload = await request.json()
        print(payload)
        
        extract_senderDetails(payload)
        extract_operatorDetail(payload)
        extract_conversationDetails(payload)
        
        return {"message":"Data received"}
    except Exception as e:
        raise HTTPException(status_code=400,detail=e)

@app.get("/status")
async def server_status():
    return {
        "statusCode":200,
        "message":"The server is live"}