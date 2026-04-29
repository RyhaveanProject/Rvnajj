import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Məlumatların
API_ID = 22928256
API_HASH = '9273844f91fb501b034627078133f966'
# 1-ci addımda aldığın o uzun kodu bura yapışdır
STRING_SESSION = "1ApWapzMBu41rbpP-ZQz4968m7v1v-TCCtkFwPYuLEuJhzMoQXvkMziJH7fWypXIV-925MYvwOZWAJSJb0tEOcG6ExlKeSyeJn-gGfniEXUdv9iEIFkT6hKSqlZYYPoRTx5HwRxBjqUUA5xT9hUXVLe8KClYmNuW42GPjwgtlVZQ5bSRnNbnEdN1CMeFtKjJoRjsxsAphKXc9E_sCBW59kyJCIp0sd5SHqvefT_28GHpM-zxO9h6fdMAYxbm0gw4CMhaInaWeWEiAP5R3iWlENUce0t_Yy8Z5NRA8k-UpanyCl7x-lNRTu_Z6o1M-dzTSwf2CaRwJcX2QYG-l9YSRiz_oFyhvg8o="
TARGET_CHANNEL = 'Ayano_Gifts'

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

@client.on(events.NewMessage(pattern=r'\.alive', outgoing=True))
async def alive(event):
    await event.edit("**Ryhavean UserBOT! Koyeb üzərində 7/24 Aktiv!**")

@client.on(events.NewMessage(chats=TARGET_CHANNEL))
async def fast_reply(event):
    try:
        # Ən sürətli cavab: \\
        await event.reply("\\\\")
        print("Hədiyyə mesajına reaksiya verildi!")
    except Exception as e:
        print(f"Xəta: {e}")

print("Bot Koyeb serverində uğurla başladı...")
client.start()
client.run_until_disconnected()
