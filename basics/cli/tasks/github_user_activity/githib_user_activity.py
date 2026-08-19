import argparse

parser = argparse.ArgumentParser(description="Script that can track users github activity.")
parser.add_argument("-un", "--username", help="Users github username.", required=True)
args = parser.parse_args()
