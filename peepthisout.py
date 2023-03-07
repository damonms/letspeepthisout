from youtube_transcript_api import YouTubeTranscriptApi
import requests
import json 
import os
API_KEY=os.environ['API_KEY_PEEP']
CHANNEL_ID='UC8MbwfzshpM4T4miBkhqx5A'


if __name__ == '__main__':
    # srt = YouTubeTranscriptApi.get_transcript("9Om_a7Hr_8E")
    # for line in srt:    
    #     print(line['text'].replace('\n',' '))
        
    url = f'https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=2000'

    r = requests.get(url)
    
    # Print the results
    j = json.loads(r.content)
    for item in j['items']:
        print(item['id']['videoId'])