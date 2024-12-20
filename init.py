import logging
import os
from dotenv import load_dotenv


#Logger setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#environment
load_dotenv(dotenv_path='.env')
TOKEN = os.getenv('TOKENA')
MAX_CACHE = os.getenv('MAX_CACHE')
DISCORD_CLIENT_ID = os.getenv('DISCORD_CLIENT_IDA')
BOT_INVITE_URL = f"https://discord.com/oauth2/authorize?client_id={DISCORD_CLIENT_ID}&permissions=1126967810710593&integration_type=0&scope=applications.commands+bot"