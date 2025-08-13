import os
from pathlib import Path
from dotenv import load_dotenv
import httpx  

dotenv_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path)

def send_message(whatsAppNumber: str, contactName: str) -> bool:
    instanceId = os.getenv("Z_API_INSTANCE_ID")
    instanceToken = os.getenv("Z_API_INSTANCE_TOKEN")
    clientToken = os.getenv("Z_API_CLIENT_TOKEN")
    url = f"https://api.z-api.io/instances/{instanceId}/token/{instanceToken}/send-text"

    headers = {
      "Client-Token":f"{clientToken}",
      "Content-Type": "application/json"
    }

    payload = {   
        "phone": whatsAppNumber,
        "message": f"Olá {contactName}, tudo bem com você?"
    }

    try:
        response = httpx.post(url, json=payload,headers=headers,)
        if response.status_code == 200:
            print(f"Mensagem enviada para {contactName} ({whatsAppNumber})")
            return True
        else:
            print(f"Erro ao enviar para {contactName}")
            return False
    except Exception as e:
        print("Erro na requisição:", e)
        return False


