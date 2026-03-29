import ffmpeg
from pathlib import Path

video_formats = {".mov", ".mp4", ".mkv", ".webm", ".avi", ".m4v", ".flv", ".wmv", ".mts", ".m2ts"}
image_formats = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff", ".heic", "heif"}
subtitle_formats = {".srt", ".ass", ".ssa", ".vtt", ".webvtt"}

out_video_