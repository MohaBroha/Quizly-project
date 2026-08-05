import os
import yt_dlp


class YouTubeService:
    """
    Handles YouTube video processing.
    """

    BASE_YDL_OPTS = {
        "remote_components": ["ejs:github"],
        "js_runtimes": {"node": {}},
    }

    @staticmethod
    def get_ydl_options():
        """
        Returns yt-dlp options and uses cookies if a cookie file exists.
        """

        ydl_opts = dict(YouTubeService.BASE_YDL_OPTS)

        cookie_path = os.getenv("YTDLP_COOKIEFILE")

        if cookie_path and os.path.exists(cookie_path):
            ydl_opts["cookiefile"] = cookie_path

        return ydl_opts

    @staticmethod
    def download_audio(url):
        """
        Downloads the audio of a YouTube video.
        """

        YouTubeService.get_video_info(url)
        return YouTubeService.extract_audio(url)

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

        output_path = "media/audio"
        os.makedirs(output_path, exist_ok=True)

        ydl_opts = {
            **YouTubeService.get_ydl_options(),
            "format": "bestaudio/best",
            "outtmpl": f"{output_path}/%(id)s.%(ext)s",
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)

        return ydl.prepare_filename(info)
