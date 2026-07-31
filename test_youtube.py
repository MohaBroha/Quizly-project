from ai.services.youtube_service import YouTubeService

audio_file = YouTubeService.download_audio(
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
)

print(audio_file)
