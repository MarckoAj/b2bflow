import os
from dotenv import load_dotenv;
from supabase import create_client,Client
from pathlib import Path

dotenv_patch = Path(__file__).parent.parent/ ".env"
load_dotenv()

def supabase_create_client()-> Client:
    url= os.getenv("SUPABASE_URL")
    key= os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise ValueError("SUPABASE_URL ou SUPABASE_KEY não configurados no .env")
    return create_client(url,key)
    


def supabase_get_contact(limit:int = 3) ->list :
    client = supabase_create_client()
    response = client.table("contatos").select("*").limit(limit).execute()
    if hasattr(response,'data'):
        return response.data
    else:
        return[]



