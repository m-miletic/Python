import argparse
import requests
from pprint import pprint

parser = argparse.ArgumentParser(description="Script that can track users github activity.")
parser.add_argument("-un", "--username", help="Users github username.", required=True)
args = parser.parse_args()

response = requests.get(f"https://api.github.com/users/{args.username}/events")
print(response.status_code)
pprint(response.json())