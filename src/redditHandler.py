import praw, os
from dotenv import load_dotenv

load_dotenv()

REDDIT_CLIENT_ID = None
REDDIT_CLIENT_SECRET = None
REDDIT_PASSWORD = None
REDDIT_USER = None
try:
    REDDIT_CLIENT_ID = os.environ["REDDIT_CLIENT_ID"]
    REDDIT_CLIENT_SECRET = os.environ["REDDIT_CLIENT_SECRET"]
    REDDIT_PASSWORD = os.environ["REDDIT_PASSWORD"]
    REDDIT_USER = os.environ["REDDIT_USER"]
    if(REDDIT_CLIENT_ID == None or REDDIT_CLIENT_SECRET == None or REDDIT_PASSWORD == None or REDDIT_USER == None):
        raise Exception("Erro ao ler o conteudo do .env")
except:
    raise Exception("Erro ao ler o conteudo do .env")


reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET, 
                     password=REDDIT_PASSWORD,
                     user_agent='eletrocompers',
                     username=REDDIT_USER)

def subreddit(channel):
    submission = reddit.subreddit(channel).random()
    return submission.url