import yt_dlp
import os
import subprocess
base_output_dir="D:/tools/basic-utility-tools/nse_option_chain/yt_dwnlod"
def download_video(urls, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'ignoreerrors': True,  
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                # First extract info (without downloading)
                info = ydl.extract_info(url, download=False, process=False)
                if "entries" in info:
                    print(f"📜 Playlist found: {url} — {len(info['entries'])} items")

                    for entry in info['entries']:
                        if not entry:
                            print("⚠️  Skipping broken or unavailable video entry")
                            continue
                        try:
                            print(f"⬇️  Downloading: {entry['title']}")
                            ydl.download([entry['webpage_url']])
                        except Exception as e:
                            print(f"⚠️  Failed to download: {entry['webpage_url']}\nReason: {e}")
                else:
                    print(f"⬇️  Downloading: {info['title']}")
                    ydl.download([url])
            except Exception as e:
                print(f"❌  Failed to process URL: {url}\nReason: {e}")

def convert_to_mp3(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".webm") or filename.endswith(".mp4"):
            input_path = os.path.join(directory, filename)
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(directory, base_name + ".mp3")

            if os.path.exists(output_path):
                print(f"⏩ Skipping (already converted): {base_name}.mp3")
                os.remove(input_path)  # Optional: clean up leftover .webm/.mp4
                continue

            print(f"🎵 Converting: {filename} → {base_name}.mp3")

            # Run ffmpeg conversion
            subprocess.run([
                "ffmpeg",
                "-i", input_path,
                "-vn",  # no video
                "-ab", "192k",
                "-ar", "44100",
                "-y",  # overwrite
                output_path
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            os.remove(input_path)
            print(f"🗑️ Deleted original: {filename}")

if __name__ == "__main__":
    # Read URLs from yt_dwnlod/urls.txt
    folder_name = input("Enter folder name (optional): ").strip()
    
    output_dir = os.path.join(base_output_dir, folder_name) if folder_name else base_output_dir

    # with open("yt_dwnlod/urls.txt", "r") as f:
    #     urls = [line.strip() for line in f if line.strip()]

    urls = [
        "https://www.youtube.com/watch?v=HTeP7ja9UFY&list=RDHTeP7ja9UFY&index=1&ab_channel=seventyskye",
        # "https://www.youtube.com/watch?v=yMiIrAxQhFA&list=PL5jD2fLvy_Gpb4kh1hSg5gKS5qFndSsyP&ab_channel=SidewalksandSkeletons-Topic",
        # "https://www.youtube.com/watch?v=q2u6Hr52Lno&ab_channel=medicomkvlog1206",
        # "https://www.youtube.com/watch?v=j7TM2ccOGbU&list=PLUOEf-vLOCSkxWY5z9cjS4OT3oZ9D8suk&ab_channel=SuperHitGaane",
        # "https://www.youtube.com/watch?v=ls5l5uNDfnU&list=PL5jD2fLvy_Gqx5jY9L1Q1n7GgCWyr8YpQ&ab_channel=MusicAcapellaForAll",
    ]

    download_video(urls, output_dir)
    convert_to_mp3(output_dir)

