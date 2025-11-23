import asyncio
from telethon import TelegramClient

# --- TUS CREDENCIALES ---
api_id = 35150197
api_hash = '2ced9d56993f07f4ce2ccb13e2258b81'

# --- TU NÚMERO ---
phone_number = '+50582269592' 

# --- EL GRUPO DESTINO ---
target_group = 'https://t.me/cardingkicks'

# --- EL MENSAJE DE VENTA ---
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
• Scrapper premium✅"""

async def main():
    print(f"Conectando con el número {phone_number}...")
    client = TelegramClient('anon_session', api_id, api_hash)
    
    # Iniciar sesión
    await client.start(phone_number)
    print("✅ ¡Conectado exitosamente!")

    while True:
        try:
            print(f"Enviando mensaje a: {target_group}")
            await client.send_message(target_group, MENSAJE)
            print("✅ Mensaje enviado.")
            
            # --- PAUSA DE SEGURIDAD ---
            # Se mantiene en 300 segundos (5 min) para evitar el ban inmediato
            # en grupos públicos con protección anti-spam.
            await asyncio.sleep(300) 
            
        except Exception as e:
            print(f"❌ Error: {e}")
            # Si ocurre un error (ej: flood wait), esperar 1 minuto antes de reintentar
            await asyncio.sleep(60)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
