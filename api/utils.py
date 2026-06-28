from pathlib import Path
import csv,os

BASE_DIR = Path(__file__).resolve().parent.parent

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
        
def extract_conversationDetails(payload:dict):
    conversationId = payload.get("conversationId")
    assignedId = payload.get("assignedId")
    sourceId = payload.get("sourceId")
    sourceUrl = payload.get("sourceUrl")    
    
    file_path = BASE_DIR/'data/conversationDetails.csv'
    file_exists = os.path.exists(file_path)  
    
    with open(file_path,'a',encoding="utf-8",newline="") as f:
        writer=csv.writer(f,delimiter='|')
        
        if not file_exists:
            writer.writerow(['conversationId','assignedId','sourceId','sourceUrl'])
        
        writer.writerows([[conversationId,assignedId,sourceId,sourceUrl]])
      

    