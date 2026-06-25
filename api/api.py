from fastapi import FastAPI,Request,HTTPException

app = FastAPI()

@app.post("/wati/webhook")
async def wati_webhook(request:Request):
    try:
        payload = await request.json()
        print(payload)
    
        return {"message":"You have successfully entered CRM"}
    except Exception as e:
        raise HTTPException(status_code=400,detail=e)

@app.get("/status")
async def server_status():
    return {
        "statusCode":200,
        "message":"The server is live"}