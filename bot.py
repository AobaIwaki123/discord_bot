import os

import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

# 環境変数からトークンとチャンネルIDをロード
load_dotenv()
TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

# Intentsを設定
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# スケジューラーを初期化
scheduler = AsyncIOScheduler()


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # スケジューラー開始
    scheduler.start()
    print("Scheduler started!")


@client.event
async def on_message(message):
    # コマンドで手動リマインダーを送る
    if message.content.lower() == "!remind":
        await remind()


# リマインドメッセージを送る関数
async def remind():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("リマインド: EC2を停止しましたか?")
    else:
        print(f"Channel with ID {CHANNEL_ID} not found.")


# 毎日0:00にリマインダーを送信
scheduler.add_job(remind, "cron", hour=0, minute=0)

# ボットを実行
client.run(TOKEN)
