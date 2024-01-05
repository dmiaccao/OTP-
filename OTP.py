from telethon.sessions import StringSession
from telethon.sync import TelegramClient, events
import re

api_id = 13469730
api_hash = 'f2bb2d8a1d1f9f235bcf742b2d04f93e'
your_session = 'AQDNiCIAtLv7YY1WgtBa_UUYmGkKiG_v0SEr_AyYVSL4FM9bMCymQHR1ir3b5EDHUAvx-x01e4NJpdQbyMtGGLTgFwG95rcfLl6pXIUkyIwOaGKeZp6JiISTcPZ5jbqzEe29t9LamhUNcJyGgnoEuoNOXzWM_WHWEuQP5IZKHVlpKDNGRqCJShFnOnLA4qIyNA9yRLhLFtL30rwREkDu5Rwt7Czwcmm4Mo8nSa8cVIHFTv4dABQjQ6UlQ0TMfN5hFiw9s28CnNtpEcK-z1-S_43yH2jIYuhsnaks4vtkUNqbwiLOKTlvlGcQUXgw0SsyH5neNZIDvDgrFp7ARmzvgfOXI_Yv0gAAAABX6uJNAA'

#client = TelegramClient(your_session, api_id, api_hash)

# Use this if you want to use session string
client = TelegramClient(StringSession(your_session), api_id, api_hash)

@client.on(events.NewMessage(from_users=777000))
async def handle_incoming_message(event):
    # Extract OTP from the message using regular expression
    otp = re.search(r'\b(\d{5})\b', event.raw_text)
    if otp:
        print("Your login code:", otp.group(0))

print("Listening for messages...")

with client:
    client.run_until_disconnected()