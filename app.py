import os
import time

def main():
    """Main function to check battery status"""
    os.system("pi-top battery > battery.txt")
    # Read in the contents of the text file
    contents = None
    with open(os.path.join(os.getcwd(), "battery.txt"), "r") as f:
        contents = f.read()
    if contents is None:
        return None
    # Send contents in a slack message
    time.sleep(10 * 60)



if __name__ == "__main__":
    main()

