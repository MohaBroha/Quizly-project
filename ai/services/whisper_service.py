from ai.services.youtube_service import YouTubeService


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
        Transcribes an audio file.
        """

        return "Temporary transcript."
