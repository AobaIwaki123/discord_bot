import os
import discord
from dotenv import load_dotenv

# .envファイルからトークンをロード
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")  # Discord Botのトークン
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  # 特定のチャンネルID

# Intentsを設定
intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # 特定のチャンネルにメッセージを送信
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Hello! This is a message from your bot.")
    else:
        print(f"Channel with ID {CHANNEL_ID} not found.")


client.run(TOKEN)
