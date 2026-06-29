from pathlib import Path
import csv,os,ast

BASE_DIR = Path(__file__).resolve().parent.parent

def convert_dict(file_path):
    payload=[]
    with open(BASE_DIR/file_path,'r',encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            
            if not line:
                continue
            
            payload.append(ast.literal_eval(line))
            
    return payload
        
def extract_senderDetails(payload:dict):
    sender_name = payload.get("senderName")
    sender_contact = payload.get("waId")
    
    file_path = BASE_DIR/'data/studentDetails.csv'
    file_exists = os.path.exists(file_path)
       
    with open(file_path,'a',encoding="utf-8",newline="") as f:
        writer=csv.writer(f,delimiter='|')
        
        if not file_exists:
            writer.writerow(['senderName','senderContact'])
        
        writer.writerows([[sender_name,sender_contact]])
    
    return {"studentName":sender_name, "studentContact":sender_contact}
        
def extract_operatorDetail(payload:dict):
    operatorName = payload.get("operatorName")
    operatorEmail = payload.get("operatorEmail")
    assignedId = payload.get("assignedId")
    
    file_path = BASE_DIR/'data/operatorDetails.csv'
    file_exists = os.path.exists(file_path)   
    
    with open(file_path,'a',encoding="utf-8",newline="") as f:
        writer=csv.writer(f,delimiter='|')
        
        if not file_exists:
            writer.writerow(['operatorName','operatorEmail','assignedId'])
        
        writer.writerows([[operatorName,operatorEmail,assignedId]]) 
    return {"operatorName":operatorName,"operatorEmail":operatorEmail,"assignedId":assignedId}
        
def extract_messageReceieved(payload:dict):
    conversationId = payload.get("conversationId")
    timestamp = payload.get("timestamp")
    assignedId = payload.get("assignedId")
    sourceId = payload.get("sourceId")
    sourceUrl = payload.get("sourceUrl")    
    
    file_path = BASE_DIR/'data/messageReceieved.csv'
    file_exists = os.path.exists(file_path)  
    
    with open(file_path,'a',encoding="utf-8",newline="") as f:
        writer=csv.writer(f,delimiter='|')
        
        if not file_exists:
            writer.writerow(['conversationId','timestamp','assignedId','sourceId','sourceUrl'])
        
        writer.writerows([[conversationId,timestamp,assignedId,sourceId,sourceUrl]])
    return {"conversationId":conversationId, "timestamp":timestamp, "assignedId":assignedId, "sourceId":sourceId, "sourceUrl":sourceUrl}

def extract_messageSent(payload:dict):
    conversationId = payload.get("conversationId")
    timestamp = payload.get("timestamp")
    assigneeId = payload.get("assigneeId")
    
    file_path = BASE_DIR/'data/messageSent.csv'
    file_exists = os.path.exists(file_path)
    
    with open(file_path,'a',encoding="utf-8",newline="") as f:
        writer=csv.writer(f,delimiter='|')
        
        if not file_exists:
            writer.writerow(['conversationId','timestamp','assigneeId'])
        
        writer.writerows([[conversationId,timestamp,assigneeId]])
    return {"conversationId":conversationId, "timestamp":timestamp, "assigneeId":assigneeId}
    
def extract_eventDetails(payload:dict):
    eventType = payload.get("eventType")
    timestamp = payload.get("timestamp")
    
    file_path = BASE_DIR/'data/eventDetails.csv'
    file_exists = os.path.exists(file_path)
    
    with open(file_path,'a',encoding="utf-8",newline="") as f:
        writer=csv.writer(f,delimiter='|')
        
        if not file_exists:
            writer.writerow(['eventType','timestamp'])
        
        writer.writerows([[eventType,timestamp]])
    return {"eventType":eventType,"timestamp":timestamp}
        
file_path = 'data/messageReceived.txt'

payload = convert_dict(file_path)

for x in payload:
    extract_senderDetails(x)
    extract_operatorDetail(x)
    extract_messageReceieved(x)
    extract_eventDetails(x)

file_path = 'data/messageSent.txt'

payload = convert_dict(file_path)
    
for x in payload:
    extract_messageSent(x)
