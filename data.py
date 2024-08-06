from configparser import ConfigParser

__config = ConfigParser()
__config.read("config.ini")
__data = __config["data"]

TOKEN = __data["token"]
OWNER_ID = __data["owner_id"]
OWNER_HANDLE = __data["owner_handle"]