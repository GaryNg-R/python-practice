import os
import time
import wakeonlan
import requests
import json

# Set your TV details
TV_MAC_ADDRESS = "1"  # Replace with your TV's MAC
TV_IP = "10.0.0.97"  # Replace with your TV's IP address
TV_PORT = 8001  # Samsung's remote API port

def turn_on_tv():
    """Send a Wake-on-LAN magic packet to turn on the TV."""
    print("Sending Wake-on-LAN packet...")
    wakeonlan.send_magic_packet(TV_MAC_ADDRESS)
    time.sleep(2)
    print("TV should be turning on!")

def turn_off_tv():
    """Send power off command to Samsung TV."""
    url = f"http://{TV_IP}:{TV_PORT}/api/v2/channels/samsung.remote.control"
    headers = {'Content-Type': 'application/json'}
    
    payload = {
        "method": "ms.remote.control",
        "params": {
            "Cmd": "Click",
            "DataOfCmd": "KEY_POWER",
            "Option": "false",
            "TypeOfRemote": "SendRemoteKey"
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        print("TV is turning off...")
    else:
        print(f"Failed to send power-off command: {response.status_code}")

if __name__ == "__main__":
    action = input("Enter 'on' to turn on or 'off' to turn off the TV: ").strip().lower()
    if action == "on":
        turn_on_tv()
    elif action == "off":
        turn_off_tv()
    else:
        print("Invalid input. Please enter 'on' or 'off'.")
