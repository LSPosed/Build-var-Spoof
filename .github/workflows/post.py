import os, asyncio, sys
from pathlib import Path
from telethon import TelegramClient, utils
from telethon.tl.functions.help import GetConfigRequest


API_ID = 611335
API_HASH = "d524b414d21f4d37f08684c1df41ac9c"
bot_token = os.environ["BOT_TOKEN"]
channel_id = int(os.environ["CHANNEL_ID"])
event_name = os.environ["EVENT_NAME"]
if event_name == "push":
    msg = f'**Push:** [{os.environ["SHA"][:7]}]({os.environ["COMMIT_URL"]})\n{os.environ["COMMIT_MESSAGE"]}'
elif event_name == "pull_request":
    msg = f'**Pull request:** [{os.environ["PULL_REQUEST_TITLE"]}]({os.environ["PULL_REQUEST_URL"]})\n{os.environ["PULL_REQUEST_BODY"]}'
elif event_name == "workflow_dispatch":
    msg = f'**Workflow dispatch** on `{os.environ["REF"]}`'


async def main():
    if len(sys.argv) < 2:
        raise ValueError("No files to upload")
    files = []
    for file in list(Path(sys.argv[1]).glob("*.zip")):
        files.append(open(file, "rb"))
    caption = [""] * len(files)
    caption[-1] = msg[:1024]
    async with await TelegramClient(
            session="/tmp/znbot", api_id=API_ID, api_hash=API_HASH
    ).start(bot_token=bot_token) as bot:
        await bot.send_file(entity=channel_id, file=files, caption=caption)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error: {e}")
