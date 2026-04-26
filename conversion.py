import subprocess
import os
import shutil

video_formats = {".mov", ".mp4", ".mkv", ".webm", ".avi", ".m4v", ".flv", ".wmv", ".mts", ".m2ts"}
image_formats = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff", ".heic", "heif"}


class Conversion:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def _ffmpeg_cmd(self):
        configured_path = os.getenv("FFMPEG_PATH")
        if configured_path and os.path.exists(configured_path):
            return configured_path

        binary_name = "ffmpeg.exe" if os.name == "nt" else "ffmpeg"
        local_binary = os.path.join(os.path.dirname(__file__), binary_name)
        if os.path.exists(local_binary):
            return local_binary

        discovered_binary = shutil.which("ffmpeg")
        if discovered_binary:
            return discovered_binary

        raise FileNotFoundError(
            "ffmpeg not found. Install ffmpeg, add it to PATH, set FFMPEG_PATH, or place ffmpeg.exe next to conversion.py"
        )

    def convert_video_extension(self):
        subprocess.run([
            self._ffmpeg_cmd(),
            "-y",
            "-i", self.input_file,
            "-c:v", "libx264",
            "-c:a", "aac",
            f"{self.output_file}",
        ], check=True)

    def convert_image_extension(self):
        subprocess.run([
            self._ffmpeg_cmd(),
            "-y",
            "-i", self.input_file,
            f"{self.output_file}",
        ], check=True)

    def convert_audio_extension(self):
        output_ext = self.output_file.rsplit(".", maxsplit=1)[-1].lower()
        codec_for_extension = {
            "mp3": "libmp3lame",
            "aac": "aac",
            "ogg": "libvorbis",
        }
        audio_codec = codec_for_extension.get(output_ext, "libmp3lame")

        subprocess.run([
            self._ffmpeg_cmd(),
            "-y",
            "-i", self.input_file,
            "-c:a", audio_codec,
            f"{self.output_file}",
        ], check=True)

