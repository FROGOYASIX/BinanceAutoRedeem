import json
import re
from telethon import TelegramClient, events
from reedem import redeem_red_packet, create_driver


with open("config.json", "r") as config_file:
    config = json.load(config_file)


api_id = config["api_id"]
api_hash = config["api_hash"]
session_name = config["session_name"]
channel_link = config["channel_link"]
config_file.close()


pattern = re.compile(r"[A-Z]`[A-Z0-9]+`[A-Z]")

async def main():
    # Create the Telegram client
    client = TelegramClient(session_name, api_id, api_hash)
    driver = create_driver()
    

    @client.on(events.NewMessage(chats=channel_link))
    async def handler(event):
        # Get the message text
        message_text = event.message.text

        # Check if the message matches the pattern
        if message_text and pattern.search(message_text):
            result = message_text[2:-2]
            redeem_red_packet(result, driver)
            print(result)

    # Start the client and keep it running
    await client.start()
    print("Listening for messages matching the pattern...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())