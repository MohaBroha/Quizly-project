import logging
import os

import whisper

from ai.services.youtube_service import YouTubeService

logger = logging.getLogger(__name__)

MODEL = whisper.load_model(os.getenv("WHISPER_MODEL", "base"))


class WhisperService:
    """
    Handles transcript generation.
    """

    @staticmethod
    def generate_transcript(url):
        """
        Generates a transcript from a YouTube URL.
        """

        try:
            audio_file = YouTubeService.download_audio(url)
            return WhisperService.transcribe_audio(audio_file)
        except Exception:
            logger.exception("Whisper transcription failed")
            raise

    @staticmethod
    def transcribe_audio(audio_file):
        """
        Transcribes an audio file using Whisper.
        """

        result = MODEL.transcribe(
            audio_file,
            beam_size=1,
            best_of=1,
            condition_on_previous_text=False,
            fp16=False,
        )

        return result["text"]
