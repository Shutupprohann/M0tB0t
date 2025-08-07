import random
import praw 
import dotenv 
import os 
from twilio.rest import Client
import schedule,pytz

dotenv.load_dotenv()

### Configuring reddit account 

reddit = praw.Reddit(
	client_id = os.getenv('REDDIT_CLIENTID'),
	client_secret = os.getenv('REDDIT_SECRET'),
	user_agent = os.getenv('REDDIT_USERAGT'),
    password = os.getenv('REDDIT_PASSWD'),
    username = os.getenv('REDDIT_USER'),
    )

posts = []
emojis = ["🌞", "✨", "🌟", "💫", "🌈", "☀️", "🔆", "🧠", "💡", "🎯", "🚀", "🌸", "🦋", "🌼", "💥", "🙌", "🪄", "🎉", "🔥", "🍀", "📈"]

## Scraping post 

subreddit = reddit.subreddit('GetMotivated').hot(limit=500)
for post in subreddit:
	if post.url.lower().endswith(('.jpg','.png','.jpeg')):
		posts.append(post.url)
	else:	
		pass 

## Twilio configs
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('auth_token')
sender = os.getenv('TWILIO_FROM')
receiver = os.getenv('TWILIO_TO')	

client = Client(account_sid,auth_token)

def send_message(text):
	message=client.messages.create(
	from_=sender,
	to = receiver,
	body = text,
	media_url = posts[random.randint(0,50)],
	)

schedule.every().day.at("15:15","Asia/Kolkata").do(send_message,text=f'You will make yourself proud today {emojis[random.randint(0,21)]*2} ')
schedule.every().day.at("23:00","Asia/Kolkata").do(send_message,text=f'You did well Today {emojis[random.randint(0,21)]*2}')

while True:
	try:
		schedule.run_pending()

	except Exception as e:
		print(e)
		exit()
		
	
