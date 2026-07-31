from ai.services.youtube_service import YouTubeService
import whisper


class WhisperService:
    """
    Handles transcript generation.
    """

    @staticmethod
    def generate_transcript(url):
        """
        Generates a transcript from a YouTube URL.
        """

        audio_file = YouTubeService.download_audio(url)

        return WhisperService.transcribe_audio(audio_file)

    @staticmethod
    def transcribe_audio(audio_file):
        """
        Transcribes an audio file using Whisper.
        """

        model = whisper.load_model("base")

        result = model.transcribe(audio_file)

        return result["text"]
