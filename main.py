import requests
import time

site = "https://www.roblox.com/users/7733466/profile"

def send(text: str):
    token = "YOUR TOKEN"
    url = "https://api.telegram.org/bot"
    channel_id = "@YOUR CHANNEL"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

while True:
    send("🕒 Wait 15 seconds for update...")
    time.sleep(15)
    send("💡 Checking...")
    result = requests.get(site)
    result = result.text
    if "Online" or "In Game" in result:
        send(f"🟢 InceptionTime is Online! Here is a link for you: {site}. Join him! 🤗")
        break
    else:
	    send("🔴 Offline! Wait...")
