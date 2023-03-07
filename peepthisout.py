from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import requests
import json 
import os
import re

# TODO
# get a random 5 second clip and extract the audio for channel alerts 

API_KEY=os.environ['API_KEY_PEEP']
CHANNEL_ID='UC8MbwfzshpM4T4miBkhqx5A'
PAGE_TOKEN='CDIQAA'

def get_next_page_token(response):
    """
    Extracts and returns the `nextPagetoken` from the reponse so we can paginate
    """
    return response['nextPageToken']

def get_next_page_response(page):
    """
    Run a request on the nextPageTokena and send back the response in json 
    """
    url_page = f'https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=50&pageToken={page}'
    print(url_page)
    return json.loads(requests.get(url_page).content)

def get_transcription(video_id):
    """
    Calls the youtube transcript api and returns the transcript as strings. If it's fucked, send back empty
    """
    try:
        srt = YouTubeTranscriptApi.get_transcript(video_id)
    except TranscriptsDisabled as fuckme:
        return ""
    except NoTranscriptFound as fuckemeharder:
        return""
    s = ""
    for line in srt:    
        s+= " "+ line['text'].replace('\n',' ')
    return s


if __name__ == '__main__':
    #This is just for the first request, we need to use the nextPageToken from this 200 assuming the number of items > maxResults
    url_base = f'https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=50'
    r = requests.get(url_base)
    j = json.loads(r.content)
    
    # for debug in case you get 403'd
    print(j)
    
    count = 0
    
    # iterate bish 
    while len(j['items']) ==50:
        print(j)
        for item in j['items']:
            vid_name = re.sub(r'[^a-zA-Z0-9]', '', (item['snippet']['title']))+'.txt'
            # This is a shitty check to see if the file exits, if it does we assume it hasn't changed and skip it
            if not os.path.exists(re.sub(r'[^a-zA-Z0-9]', '', (item['snippet']['title']))+'.txt'):
                s = get_transcription(item['id']['videoId'])
                with open(re.sub(r'[^a-zA-Z0-9]', '', (item['snippet']['title']))+'.txt', 'w') as f:
                    f.write(s)

        print('DONE WITH PAGE %d' % count)
        count+=1

        next_token = get_next_page_token(j)
        j = get_next_page_response(next_token)
    