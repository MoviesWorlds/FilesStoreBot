# (c) @senuinfinity

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID","15554181"))
	API_HASH = os.environ.get("API_HASH","c5524df816d0b2d6a137ea6066c7096f")
	BOT_TOKEN = os.environ.get("BOT_TOKEN","5269745681:AAFLMhp6sU7kf7Zx4WadzqVed0NMM0Jxxmw")
	BOT_USERNAME = os.environ.get("BOT_USERNAME","ESMFILE_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL","-1001298652572"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER","1319079143"))
	DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://filesesm:filesesm@cluster0.r6b2pn7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","-1002038756910")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot 🤖!
The files are Stored In Mydatabase. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Platform:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 ** Heroku server:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Editing:** @EverseenMoviesofficial

👥 **Any Doubt Support group:** [EverseenMovies Group](https://t.me/Everseen_Movies)

📢 **Join My update channel:** [EverseenMovies Channel](http://t.me/+LFS3S9RT-_4zNWFl)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @EverseenMoviesofficial

💲**Donate Now:** @EverseenMoviesofficial

📌Create Any Bot Contact Admin @EverseenMoviesofficial

"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
