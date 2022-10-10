import os
import time
import http.client
import json
from env import SLACK_URL, ROOT


def slack(message: str) -> None:
    """Send a message to slack endpoint"""
    # print(message)
    conn = http.client.HTTPSConnection("hooks.slack.com")
    payload = json.dumps({
        "text": "---------\nPi-top BATTERY:\n{}".format(message)
    })
    headers = {
        "Content-Type": "application/json"
    }
    conn.request("POST", SLACK_URL, payload, headers)
    res = conn.getresponse()
    # data = res.read()
    # print(data.decode("utf-8"))

def main():
    """Main function to check battery status"""
    os.system("pi-top battery > battery.txt")
    # Read in the contents of the text file
    contents = None
    with open(os.path.join(ROOT, "battery.txt"), "r") as f:
        contents = f.read()
    if contents is None:
        return None
    message = ""
    for line in contents.split("\n"):
        if line.strip() == "Charging State: 0":
            message += "Pitop unplugged\n"
        elif line.find("Capacity:") > -1:
            message += "{}{}\n".format(line, "%")
        elif line.find("Time Remaining:") > -1:
            _hours = int(int(line.replace("Time Remaining: ", "")) / 60)
            _minutes = (round(int(line.replace("Time Remaining: ", "")) / 60, 2) - _hours) * 60
            message += "Time Remaining: {} hours and {} minutes\n".format(
                _hours,
                int(_minutes)
            )
        else:
            message += line
    # Send contents in a slack message
    slack(message)

if __name__ == "__main__":
    main()
