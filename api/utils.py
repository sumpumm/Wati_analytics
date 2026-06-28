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
        
payload={'id': '6a3cceaa02162ec653a74f20', 'created': '2026-06-25T06:46:02.6749436Z', 'whatsappMessageId': 'wamid.HBgNOTc3OTgwOTQ4OTc2NBUCABIYIEFDQ0ZBQjY5RENDREYxREFFQzczRkE4QTVCQzEzNkFGAA==', 'conversationId': '69757a762c89b921e674d5ff', 'ticketId': '6a3ccdbeae03fbc07875b7b6', 'text': 'Veterinarian ko class hunx ki nai', 'type': 'text', 'data': None, 'sourceId': None, 'sourceUrl': None, 'timestamp': '1782369960', 'owner': False, 'eventType': 'message', 'statusString': 'SENT', 'avatarUrl': None, 'assignedId': '67cfc3b23b21b9d3e767595e', 'operatorName': 'indira  batala', 'operatorEmail': 'ibatala161@gmail.com', 'waId': '9779809489764', 'messageContact': None, 'senderName': 'pari☺️😘', 'listReply': None, 'interactiveButtonReply': None, 'buttonReply': None, 'replyContextId': '', 'sourceType': 7, 'frequentlyForwarded': False, 'forwarded': False, 'bsuid': 'NP.1016949897961236'}

extract_senderDetails(payload)
extract_operatorDetail(payload)

    