import os
from datetime import datetime

import discord
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

# 環境変数からトークンをロード
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  # 通知を送るチャンネルIDを設定

# Intentsを設定
intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

# スケジューラーを初期化
scheduler = BackgroundScheduler()


# 通知メッセージを送る関数
async def send_notification():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(
            f'定期通知: 現在の時刻は {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} です！'
        )


# スケジュール設定 (毎日10:00に通知を送信)
@scheduler.scheduled_job("cron", hour=10, minute=0)
def scheduled_job():
    client.loop.create_task(send_notification())


@client.event
async def on_ready():
    print(f"{client.user} がログインしました")
    scheduler.start()  # スケジューラーを開始


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!time"):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await message.channel.send(f"現在の時刻は {current_time} です")


# ボットを実行
client.run(TOKEN)
