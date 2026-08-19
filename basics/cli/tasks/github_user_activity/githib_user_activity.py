import argparse
import requests
from pprint import pprint

parser = argparse.ArgumentParser(description="Script that can track users github activity.")
parser.add_argument("-un", "--username", help="Users github username.", required=True)
args = parser.parse_args()

try:
    response = requests.get(f"https://api.github.com/usedrs/{args.username}/events", timeout=5)
    response.raise_for_status()
    data = response.json()
    print("Success!", data)
except requests.exceptions.RequestException as e:
    print(f"Something went wrong: {e}")