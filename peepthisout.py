from youtube_transcript_api import YouTubeTranscriptApi

srt = YouTubeTranscriptApi.get_transcript("9Om_a7Hr_8E")

for line in srt:
    print(line['text'].replace('\n',' '))