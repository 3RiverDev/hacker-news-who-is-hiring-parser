import sys
from urllib.request import urlopen
import json
import time
import html

if len(sys.argv) != 2:
    print('Error: Provide the Hacker News "Item ID" for the "Who is hiring?" feed.')
    print('Find the ID in the URL: https://news.ycombinator.com/item?id=[ID].')
    sys.exit()

item_id = sys.argv[1]

hn_response = urlopen('https://hacker-news.firebaseio.com/v0/item/' + item_id + '.json')
hn_json = json.load(hn_response)

post_ids = hn_json['kids']

# Sort in reverse chronological order.
post_ids.sort(reverse=True)

for post_id in post_ids:
    hn_post_response = urlopen('https://hacker-news.firebaseio.com/v0/item/' + str(post_id) + '.json')
    hn_post_json = json.load(hn_post_response)

    # Posts can be deleted.  If so, deleted=True is included.  But the field is omitted entirely if False.
    if not ('deleted' in hn_post_json and hn_post_json['deleted']):
        post = hn_post_json['text']
        post = html.unescape(post)

        # Replace the newlines with a space.  Sure, it crams things together, but it makes this script easier
        # to use with grep.
        post = post.replace('\n', ' ')

        # Prefix with the datetime.
        post = time.ctime(hn_post_json['time']) + ': ' + post

        print(post + '\n')
