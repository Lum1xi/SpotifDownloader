import os
import subprocess
import logging

# Disable spotdl logging
logging.getLogger("spotdl").setLevel(logging.ERROR)
logging.getLogger("root").setLevel(logging.ERROR)

folder = "Downloads"
if not os.path.exists(folder):
    os.makedirs(folder)

def download(url,):
    if not url:
        print("No URL provided")
        return None

    print("Starting download...")
    command = ["spotdl", url, "--output", folder]

    try:
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return "Download completed successfully"
    except Exception as e:
        print(f"Error: {e}")
        return None
