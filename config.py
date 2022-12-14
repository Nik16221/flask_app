import os

DATA_PATH_POST = os.path.join("data", "posts.json")
DATA_PATH_COMMENTS = os.path.join("data", "comments.json")
DATA_PATH_BOOKMARKS = os.path.join("data", "bookmarks.json")

LOGGER_API_PATH = os.path.join(".", "logs", "api.logs")
LOGGER_FORMAT = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
JSON_AS_ASCII = False


