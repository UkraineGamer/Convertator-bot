import subprocess

video_formats = {".mov", ".mp4", ".mkv", ".webm", ".avi", ".m4v", ".flv", ".wmv", ".mts", ".m2ts"}
image_formats = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff", ".heic", "heif"}


class Conversion:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert_video_extension(self):
        subprocess.run([
            "ffmpeg", 
            "-i", self.input_file,
            "-c:v", "libx264",
            "-c:a", "aac",
            f"{self.output_file}",
        ], check=True)

    def convert_image_extension(self):
        subprocess.run([
            "ffmpeg",
            "-i", self.input_file,
            f"{self.output_file}",
        ], check=True)

    def convert_audio_extension(self):
        subprocess.run([
            "ffmpeg",
            "-i", self.input_file,
            "-c:a", "libmp3lame",
            f"{self.output_file}",
        ], check=True)

