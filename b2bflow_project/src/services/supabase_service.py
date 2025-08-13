import os
from utils.logger import log
from dotenv import load_dotenv;
from supabase import create_client,Client
from pathlib import Path

dotenv_patch = Path(__file__).parent.parent/ ".env"
load_dotenv()

def supabase_create_client()-> Client:
    """Cria e retorna o cliente Supabase"""
    url= os.getenv("SUPABASE_URL")
    key= os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise ValueError(log("SUPABASE_URL ou SUPABASE_KEY não configurado no .env"))
    return create_client(url,key)
    


def supabase_get_contact(limit:int = 3) ->list :
    """Busca lista de contatos no Supabase"""
    client = supabase_create_client()
    response = client.table("contatos").select("*").limit(limit).execute()
    if hasattr(response,'data'):
        return response.data
    else:
        return[]



