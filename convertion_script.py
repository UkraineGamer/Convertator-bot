import ffmpeg
import subprocess
from pathlib import Path

video_formats = {".mov", ".mp4", ".mkv", ".webm", ".avi", ".m4v", ".flv", ".wmv", ".mts", ".m2ts"}
image_formats = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff", ".heic", ".heif"}

out_video_formats = {".mp4", ".mkv", ".webm", ".mov", ".avi", ".giv"}
out_image_formats = {".jpg", ".png", ".webp", ".bmp", ".tiff"}
out_audio_formats = {".mp3", ".m4a", ".aac", ".wav", ".flac", ".opus"}

