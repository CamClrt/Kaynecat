import os

from dotenv import load_dotenv


# Init dotenv
load_dotenv()

# Flask
SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
