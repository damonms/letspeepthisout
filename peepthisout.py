from youtube_transcript_api import YouTubeTranscriptApi
import requests
import json 
import os
API_KEY=os.environ['API_KEY_PEEP']
CHANNEL_ID='UC8MbwfzshpM4T4miBkhqx5A'
PAGE_TOKEN='CDIQAA'

def get_next_page_token(response):
    return response['nextPageToken']

def get_next_page_response(page):
    url_page = f'https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID}&part=id&order=date&maxResults=50&pageToken={page}'
    print(url_page)
    return json.loads(requests.get(url_page).content)

if __name__ == '__main__':
    # srt = YouTubeTranscriptApi.get_transcript("9Om_a7Hr_8E")
    # for line in srt:    
    #     print(line['text'].replace('\n',' '))
        
    url_base = f'https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID}&part=id&order=date&maxResults=50'
    
    r = requests.get(url_base)
    
    # Print the results

    j = json.loads(r.content)
    
    while len(j['items']) ==50:
        for item in j['items']:
            print(item['id']['videoId'])
            print(item)
        next_token = get_next_page_token(j)
        j = get_next_page_response(next_token)
    