from os import getenv
from dotenv import load_dotenv

load_dotenv()


TREASURES_AND_KEEPERS_DB = getenv("DATA_BASE")
HOST_URL = getenv("URL")
