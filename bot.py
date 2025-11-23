import asyncio
import telegram # Librería: python-telegram-bot

# --- TUS DATOS ---
# Token del bot (asegúrate de que este es el Token de SENTINEL CHK)
TOKEN = '8563684051:AAEAtt8RlQ3fi13UDxmzqPId2b3AEQpy-I' 

# ID del chat usando el handle del grupo que has confirmado
CHAT_ID = '@AnubisCHK'

# --- MENSAJE DE VENTA ---
# (El contenido se mantuvo igual que en el código anterior)
MENSAJE = """@SentinelChksBot
Precios planes.

- $5.00 USD - 15 Dias + 300 creditos.
- $9.00 USD - 30 Dias + 750 Creditos.
- $15.00 USD - 40 Dias + 1150 Creditos.
- $20.00 USD - 45 Dias + Creditos ilimitados.

• CREDITOS
- $7.00 USD - 700 Creditos.
- $12.00 USD - 1600 Creditos.
- $16.00 USD - 2500 Creditos.

• Plan de por vida: 
- $200 USD - Posibilidad de pedir 2 Keys de 3 dias por mes.

• Grupo privado incluido en todos los planes! ✅
• Asistencia 24/7 incluido en todos los planes! ✅
• Scrapper premium✅
° seller : @Shadow09_05"""

async def enviar_mensaje():
    print("Iniciando Bot API para @AnubisCHK...")
    bot = telegram.Bot(token=TOKEN)
    
    while True:
        try:
            # Enviar el mensaje al handle del grupo
            await bot.send_message(chat_id=CHAT_ID, text=MENSAJE)
            print(f"Mensaje enviado a {CHAT_ID} con éxito.")
            
            # Pausa de 60 segundos (ajusta esto si quieres más tiempo)
            await asyncio.sleep(60) 
            
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            # Esperar 5s si hay un error antes de reintentar
            await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(enviar_mensaje())
