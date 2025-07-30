import requests,sys 
import discord
from discord.ext import commands
import asyncio
import multiprocessing
import time
import random
import threading
from colorama import Fore,Style
import fade
import os
import aiohttp
import subprocess
import psutil
import json
from datetime import datetime
import time
import aiohttp
import requests,sys
import os
import base64
import tqdm
import pyfiglet
import string

import sys
import os
import shutil
import configparser
import re
import requests
SCRIPT_URL = "https://github.com/7xta/silent-menu"
LOCAL_SCRIPT = os.path.join(os.path.dirname(__file__), "silentmenu.py")

def check_update_and_run():
    print("checking for script updates...")
    try:
        response = requests.get(SCRIPT_URL)
        if response.status_code != 200:
            print(f"failed to fetch update: status code {response.status_code}")
            return

        remote_data = response.text
        local_data = ""

        if os.path.exists(LOCAL_SCRIPT):
            with open(LOCAL_SCRIPT, "r", encoding="utf-8") as f:
                local_data = f.read()
            print("local script loaded.")
        else:
            print("local script not found, will create new.")

        if local_data != remote_data:
            print("update found, updating local script...")
            with open(LOCAL_SCRIPT, "w", encoding="utf-8") as f:
                f.write(remote_data)
            print("update done, restarting index.js...")
            subprocess.Popen([sys.executable, LOCAL_SCRIPT], stdout=sys.stdout, stderr=sys.stderr)
            sys.exit(0)
        else:
            print("no update found.")

    except Exception as e:
        print("error while checking update:", str(e))

if __name__ == "__main__":
    check_update_and_run()
