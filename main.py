import requests

payload={'id': '6a3cceaa02162ec653a74f20', 'created': '2026-06-25T06:46:02.6749436Z', 'whatsappMessageId': 'wamid.HBgNOTc3OTgwOTQ4OTc2NBUCABIYIEFDQ0ZBQjY5RENDREYxREFFQzczRkE4QTVCQzEzNkFGAA==', 'conversationId': '69757a762c89b921e674d5ff', 'ticketId': '6a3ccdbeae03fbc07875b7b6', 'text': 'Veterinarian ko class hunx ki nai', 'type': 'text', 'data': None, 'sourceId': None, 'sourceUrl': None, 'timestamp': '1782369960', 'owner': False, 'eventType': 'message', 'statusString': 'SENT', 'avatarUrl': None, 'assignedId': '67cfc3b23b21b9d3e767595e', 'operatorName': 'indira  batala', 'operatorEmail': 'ibatala161@gmail.com', 'waId': '9779809489764', 'messageContact': None, 'senderName': 'pari☺️😘', 'listReply': None, 'interactiveButtonReply': None, 'buttonReply': None, 'replyContextId': '', 'sourceType': 7, 'frequentlyForwarded': False, 'forwarded': False, 'bsuid': 'NP.1016949897961236'}


response = requests.post("http://127.0.0.1:8000/wati/webhook",json=payload)

print(response.status_code)
print(response.json())