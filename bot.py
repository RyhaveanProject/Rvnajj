import os
import asyncio
import sys
from telethon import TelegramClient, events, functions, types
from telethon.sessions import StringSession

# Məlumatların
API_ID = 22928256
API_HASH = '9273844f91fb501b034627078133f966'
STRING_SESSION = "1ApWapzMBu41rbpP-ZQz4968m7v1v-TCCtkFwPYuLEuJhzMoQXvkMziJH7fWypXIV-925MYvwOZWAJSJb0tEOcG6ExlKeSyeJn-gGfniEXUdv9iEIFkT6hKSqlZYYPoRTx5HwRxBjqUUA5xT9hUXVLe8KClYmNuW42GPjwgtlVZQ5bSRnNbnEdN1CMeFtKjJoRjsxsAphKXc9E_sCBW59kyJCIp0sd5SHqvefT_28GHpM-zxO9h6fdMAYxbm0gw4CMhaInaWeWEiAP5R3iWlENUce0t_Yy8Z5NRA8k-UpanyCl7x-lNRTu_Z6o1M-dzTSwf2CaRwJcX2QYG-l9YSRiz_oFyhvg8o="
TARGET_CHANNEL = 'Ayano_Gifts'

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

# PLUGINLƏR ÜÇÜN QOVLUQ
if not os.path.exists("plugins"):
    os.makedirs("plugins")

# .alive komandası
@client.on(events.NewMessage(pattern=r'\.alive', outgoing=True))
async def alive(event):
    await event.edit("**Ryhavean UserBOT!🥷**")

# HƏDİYYƏ KANALI ÜÇÜN SÜRRƏTLİ REAKSİYA
@client.on(events.NewMessage(chats=TARGET_CHANNEL))
async def fast_reply(event):
    try:
        await event.reply("\\\\")
    except:
        pass

# .blockall @istifadeci_adi - Qrupdakı bütün üzvləri bloklayır
@client.on(events.NewMessage(pattern=r'\.blockall (.*)', outgoing=True))
async def block_all(event):
    chat_name = event.pattern_match.group(1).replace('@', '')
    await event.edit(f"**@{chat_name} sizi atıram bluqa😏...**")
    
    count = 0
    try:
        async for user in client.iter_participants(chat_name):
            if not user.bot and not user.is_self:
                try:
                    await client(functions.contacts.BlockRequest(id=user.id))
                    count += 1
                    # Spam filterinə düşməmək üçün hər 3 blokdan bir 1 saniyə gözləyir
                    if count % 3 == 0:
                        await asyncio.sleep(2)
                except Exception:
                    continue
        await event.edit(f"**Uğurlu! {count}-nəfər siz getdiz bluqa😏.**")
    except Exception as e:
        await event.edit(f"**Xəta:** {e}")

# .add - Mesaja reply atdıqda həmin kodu plugin kimi yükləyir
@client.on(events.NewMessage(pattern=r'\.add', outgoing=True))
async def add_plugin(event):
    if not event.is_reply:
        return await event.edit("**Ayqa plugin olan mesaja replay at!🤬**")
    
    reply_msg = await event.get_reply_message()
    plugin_name = f"plugin_{reply_msg.id}.py"
    with open(f"plugins/{plugin_name}", "w") as f:
        f.write(reply_msg.text)
    
    await event.edit(f"**Plugin yükləndi cigər: {plugin_name}. Aktivləşdirməy üçün .restart et**")

# .restart - Botu yenidən başladır
@client.on(events.NewMessage(pattern=r'\.restart', outgoing=True))
async def restart(event):
    await event.edit("**Bot yenidən başladılır 🫦**")
    os.execl(sys.executable, sys.executable, *sys.argv)

print("Bot başladıldı...")
client.start()
client.run_until_disconnected()
