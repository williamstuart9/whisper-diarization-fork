import os
import subprocess

root_dir = r"recordings"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        base, ext = os.path.splitext(file)
        if ext == ".mp3":
            full_file_path = os.path.join(dirpath, file)
            output_file_path = os.path.join(dirpath, f"{base}.wav")
            print(output_file_path)
            subprocess.run(
                [
                    r"ffmpeg.exe",
                    "-i",
                    full_file_path,
                    "-acodec",
                    "pcm_u8",
                    "-ar",
                    "22050",
                    output_file_path,
                ]
            )
            subprocess.run(
                [
                    "py",
                    "diarize.py",
                    "-a",
                    output_file_path,
                    "--no-stem",
                    "--whisper-model",
                    "large-v3",
                    "--language",
                    "en",
                    "--device",
                    "cuda",
                ]
            )
