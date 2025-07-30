\import os
import sys
import requests
import subprocess

SCRIPT_NAME = "silentmenu.py"
SCRIPT_URL = "https://raw.githubusercontent.com/7xta/silent-menu/main/silentmenu.py"
CURRENT_PATH = os.path.abspath(__file__)
SCRIPT_DIR = os.path.dirname(CURRENT_PATH)
LOCAL_SCRIPT = os.path.join(SCRIPT_DIR, SCRIPT_NAME)

def rename_if_needed():
    if not CURRENT_PATH.endswith(SCRIPT_NAME):
        print(f"Script name is incorrect. Renaming to {SCRIPT_NAME}...")
        try:
            new_path = os.path.join(SCRIPT_DIR, SCRIPT_NAME)
            with open(CURRENT_PATH, "r", encoding="utf-8") as current_file:
                content = current_file.read()
            with open(new_path, "w", encoding="utf-8") as new_file:
                new_file.write(content)
            print(f"Rename complete. Launching {SCRIPT_NAME}...")
            subprocess.Popen([sys.executable, new_path], stdout=sys.stdout, stderr=sys.stderr)
            sys.exit(0)
        except Exception as e:
            print("Error during rename:", str(e))
            sys.exit(1)

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
            print("update done, restarting silentmenu.py...")
            subprocess.Popen([sys.executable, LOCAL_SCRIPT], stdout=sys.stdout, stderr=sys.stderr)
            sys.exit(0)
        else:
            print("no update found.")

    except Exception as e:
        print("error while checking update:", str(e))

if __name__ == "__main__":
    rename_if_needed()
    check_update_and_run()
