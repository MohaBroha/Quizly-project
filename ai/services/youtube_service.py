import logging
import os
import re

import yt_dlp
from django.conf import settings

logger = logging.getLogger(__name__)


class YouTubeService:
    """
    Handles YouTube video processing.
    """

    BASE_YDL_OPTS = {
        "remote_components": ["ejs:github"],
    }

    @staticmethod
    def get_ydl_options():
        """
        Returns yt-dlp options and uses proxy and cookies if configured.
        """

        ydl_opts = dict(YouTubeService.BASE_YDL_OPTS)

        cookie_path = os.getenv("YTDLP_COOKIEFILE")
        proxy_url = os.getenv("YTDLP_PROXY")
        deno_path = os.getenv("YTDLP_DENO_PATH")

        if cookie_path and os.path.exists(cookie_path):
            ydl_opts["cookiefile"] = cookie_path
        elif cookie_path:
            logger.warning("Configured YouTube cookie file does not exist")

        if proxy_url:
            ydl_opts["proxy"] = proxy_url

        if deno_path and os.path.exists(deno_path):
            ydl_opts["js_runtimes"] = {"deno": {"path": deno_path}}

        return ydl_opts

    @staticmethod
    def download_audio(url):
        """
        Downloads the audio of a YouTube video.
        """

        try:
            return YouTubeService.extract_audio(url)
        except yt_dlp.utils.DownloadError as error:
            message = re.sub(
                r"(https?://)[^\s/@:]+:[^\s/@]+@",
                r"\1<redacted>@",
                str(error),
            )
            logger.warning("YouTube download failed: %s", message)
            raise

    @staticmethod
    def get_video_info(url):
        """
        Retrieves information about a YouTube video.
        """

        with yt_dlp.YoutubeDL(YouTubeService.get_ydl_options()) as ydl:
            return ydl.extract_info(url, download=False)

    @staticmethod
    def extract_audio(video_url):
        """
        Downloads the audio track of a YouTube video.
        """

        output_path = os.path.join(settings.BASE_DIR, "media", "audio")
        os.makedirs(output_path, exist_ok=True)

        ydl_opts = {
            **YouTubeService.get_ydl_options(),
            "format": "bestaudio/best",
            "outtmpl": f"{output_path}/%(id)s.%(ext)s",
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)

        return ydl.prepare_filename(info)
