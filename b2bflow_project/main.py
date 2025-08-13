from src.services.supabase_service import supabase_get_contact
from src.services.zapi_service import send_message

if __name__=="__main__":
 print("Iniciando envio de mensagens")
 contatos = supabase_get_contact()

if not contatos:
 print("contato encontrado no Supabase")
else:
  for contato in contatos :
   numero = contato.get("numero_whathsapp")
   nome = contato.get("nome_contato")
   if numero and nome:
    send_message(numero,nome)
   else:
    print(f"contato invalido {contato}")
print("mensagens enviadas")
