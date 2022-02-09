from pyrogram.types import Message

Message.input = property(
    lambda m: m.text[m.text.find(m.command[0]) + len(m.command[0]) + 1:] 
    if len(m.command) > 1 else None
)
