from ai.services.whisper_service import WhisperService

transcript = WhisperService.transcribe_audio("media/audio/dQw4w9WgXcQ.webm")

print(transcript)
