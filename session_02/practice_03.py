# ================================================
# pip install rich

import os
import subprocess
import sys

from rich import print

# ================================================
if os.name == "nt":
    subprocess.run(args="cls", shell=True, check=False)
else:
    subprocess.run(args="clear", shell=True, check=False)

# ================================================
print("=" * 50)
print("My Chatbot")
print("[blue]My Chatbot[/blue]")
print("[blue]My[/blue] [red][bold]first[/bold][/red] [yellow]Chatbot[/yellow]")

# ================================================
while True:
    print("=" * 50)
    user_prompt = input("User: ").strip()

    if user_prompt == "":
        print("-" * 50)
        print()
        continue
    if user_prompt.lower() in ["bye", "quit", "exit"]:
        print("-" * 50)
        print("Exit")
        # break
        print("Have a nice day!")
        sys.exit(0)

    print(f"[yellow]AI: You've asked: [/yellow]{user_prompt}")

# print("The program is terminated")
