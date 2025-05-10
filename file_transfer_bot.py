from pyrogram import Client, filters
from pyrogram.types import Message
import logging
import asyncio

api_id = 17178604
api_hash = "0185d63ff2147519b544026e03a2bbcc"
bot_token = "7768032133:AAEc4fBlWMWt6_s6AX5cRNdPS-1P08guidY"

source_channel = -1002113097087
destination_channel = -1002031226550  # Change if needed

# Set up logging
logging.basicConfig(level=logging.INFO, filename='transfer.log', format='%(asctime)s - %(message)s')

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

ALLOWED_TYPES = ["video", "document", "photo", "audio"]  # Customize if needed

@app.on_message(filters.chat(source_channel))
async def copy_selected_files(client, message: Message):
    try:
        if (
            (message.video and "video" in ALLOWED_TYPES) or
            (message.document and "document" in ALLOWED_TYPES) or
            (message.photo and "photo" in ALLOWED_TYPES) or
            (message.audio and "audio" in ALLOWED_TYPES)
        ):
            await asyncio.sleep(3)  # Delay in seconds
            await message.copy(destination_channel)
            logging.info("Copied message ID %s", message.id)
            print("Copied:", message.id)
        else:
            print("Skipped:", message.id)
    except Exception as e:
        logging.error("Error: %s", e)
        print(f"Error: {e}")

app.run()
