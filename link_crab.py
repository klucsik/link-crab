import session_manager
import reporting
import exercise_url
import gather_links

from urllib.request import urlparse
import yaml
from datetime import datetime
import colorama

# Colorama init https://pypi.org/project/colorama/
colorama.init()
GREEN = colorama.Fore.GREEN
RED = colorama.Fore.RED
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET


#for development tests
import time
from tests.test_app import generate_mock_app
generate_mock_app()

# setup:
print('----------------setup---------------------')
starting_time = datetime.now()
config={}
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
user = None
try:
    user=config['user']
except:
    pass    
session = session_manager.make_session(user)

starting_url = config['starting_url']

links = set()
link_db = []
links.add(starting_url)

# gathering:
print('----------------gather links---------------------')
checked_domain = urlparse(starting_url).netloc
links.add(starting_url)
links = gather_links.gather_links(session, links,checked_domain)

# excresizing:
print('----------------Excercise links---------------------')
session = session_manager.make_session(user) #remake the session, because crawling through the log-out link logs us out :D
for link in links:
    link_db.append(exercise_url.exercise_url(session, link)) #TODO: error handling


# reporting:
print('----------------Report---------------------')

for link in link_db:
    print(f"[*] {link[0]} - {GREEN if link[1]==200 else RED} {link[1]} {RESET}- {link[2]} ms - {link[3]}")

reporting.save_linkdb_to_csv(link_db,checked_domain)


