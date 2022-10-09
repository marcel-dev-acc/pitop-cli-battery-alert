import os
import time
import http.client
import json
from env import SLACK_URL

def slack(message: str) -> None:
    """Send a message to slack endpoint"""
    conn = http.client.HTTPSConnection("hooks.slack.com")
    payload = json.dumps({
        "text": "---------\nPi-top BATTERY:\n".format(message)
    })
    headers = {
        "Content-Type": "application/json"
    }
    conn.request("POST", SLACK_URL, payload, headers)
    res = conn.getresponse()

def main():
    """Main function to check battery status"""
    os.system("pi-top battery > battery.txt")
    # Read in the contents of the text file
    contents = None
    with open(os.path.join(os.getcwd(), "battery.txt"), "r") as f:
        # Send contents in a slack message
        slack(f.read())

if __name__ == "__main__":
    main()
