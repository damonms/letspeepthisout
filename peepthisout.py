from youtube_transcript_api import YouTubeTranscriptApi

if __name__ == '__main__':
    srt = YouTubeTranscriptApi.get_transcript("9Om_a7Hr_8E")
    for line in srt:    
        print(line['text'].replace('\n',' '))