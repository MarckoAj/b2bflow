from src.services.supabase_service import supabase_get_contact
from src.services.zapi_service import send_message
from src.utils.logger import log

if __name__=="__main__":
 log("Iniciando envio de mensagens")
 contatos = supabase_get_contact()

if not contatos:
 log("contato encontrado no Supabase")
else:
  for contato in contatos :
   numero = contato.get("numero_whathsapp")
   nome = contato.get("nome_contato")
   if numero and nome:
    send_message(numero,nome)
   else:
    log(f"contato invalido {contato}")
log("mensagens enviadas")
