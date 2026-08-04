import os
import yt_dlp


class YouTubeService:
    """
    Handles YouTube video processing.
    """

    BASE_YDL_OPTS = {
        "remote_components": ["ejs:github"],
        "js_runtimes": {"node": {}},
        "cookiefile": "/home/moha/youtube_cookies.txt",
    }

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

        with yt_dlp.YoutubeDL(YouTubeService.BASE_YDL_OPTS) as ydl:
            return ydl.extract_info(url, download=False)

    @staticmethod
    def extract_audio(video_url):
        """
        Downloads the audio track of a YouTube video.
        """

        output_path = "media/audio"
        os.makedirs(output_path, exist_ok=True)

        ydl_opts = {
            **YouTubeService.BASE_YDL_OPTS,
            "format": "bestaudio/best",
            "outtmpl": f"{output_path}/%(id)s.%(ext)s",
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)

        return ydl.prepare_filename(info)
