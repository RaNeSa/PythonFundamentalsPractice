# **************************************************
# print()
# print("=" * 50)

# first_name = input("What is your first name: ").strip().title()
# last_name = input("What is your last name: ").strip().title()
# age = input("How old are you? ")
# age = int(age)

# print("-" * 50)

# if age < 20:
#     print("You are teenager!")
# else:
#     print("You are not teenager!")

# print("-" * 50)

# message = f"You are {first_name} {last_name} and {age} years old."
# print(message)

# print("=" * 50)
# print()
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# # دستور ذیل خطا می‌دهد
# os.system("cls")

# print("Hello, World!")
# **************************************************


# **************************************************
# import os

# os.system("cls")

# print("Hello, World!")
# **************************************************


# **************************************************
# import os

# os.system(command="dir")  # Best Practice

# print("Hello, World!")
# **************************************************


# **************************************************
# The below code is not Cross Platform (Windows / Linux / MacOS)!
# **************************************************
# import subprocess

# subprocess.run(args="cls", shell=True)

# print("Hello, World!")
# **************************************************


# **************************************************
# import os
# import subprocess

# if os.name == "nt":
#     subprocess.run(args="cls", shell=True)
# else:
#     subprocess.run(args="clear", shell=True)

# print("Hello, World!")
# **************************************************


# **************************************************
# # Bad Practice
# # import os, subprocess

# # Best Practice
# import os
# import subprocess
# **************************************************
# **************************************************
# **************************************************


# **************************************************
# # NEW
# import os
# import subprocess

# # NEW
# if os.name == "nt":
#     subprocess.run(args="cls", shell=True)
# else:
#     subprocess.run(args="clear", shell=True)

# # NEW
# # print()

# print("=" * 50)

# first_name = input("What is your first name: ").strip().title()
# last_name = input("What is your last name: ").strip().title()
# age = input("How old are you? ")
# age = int(age)

# print("-" * 50)

# if age < 20:
#     print("You are teenager!")
# else:
#     print("You are not teenager!")

# print("-" * 50)

# message = f"You are {first_name} {last_name} and {age} years old."
# print(message)

# print("=" * 50)
# print()
# **************************************************


# **************************************************
# if 1 == 1:
#     print("Hello, World!")

# print("Finished!")
# **************************************************


# **************************************************
# Infinitive
# **************************************************
# while 1 == 1:
#     print("Hello, World!")

# print("Finished!")
# **************************************************


# **************************************************
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# print("Hello, World!")
# **************************************************


# **************************************************
# count = 3
# counter = 1

# while counter <= count:
#     print("Hello, World!")
# **************************************************


# **************************************************
# count = 3
# counter = 1

# while counter <= count:
#     print("Hello, World!")

# counter = counter + 1
# **************************************************


# **************************************************
# count = 3
# counter = 1

# while counter <= count:
#     print("Hello, World!")

#     counter = counter + 1
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# Expression
# **************************************************
# a = 10
# b = 20

# c = a * 2 + b - 12
# **************************************************


# **************************************************
# + - * / ...
# **************************************************
# a = 10
# # a = a * 2
# a *= 2
# print(a)
# **************************************************
# **************************************************
# **************************************************


# **************************************************
# c = 3
# i = 1

# while i <= c:
#     print("Hello, World!")
#     i = i + 1
# **************************************************


# **************************************************
# count = 3
# counter = 1

# while counter <= count:
#     print("Hello, World!")

#     # یک واحد به متغیر ذیل اضافه می‌کنیم
#     counter += 1
# **************************************************


# **************************************************
# ذهن استقرایی
# **************************************************
# count = 3
# counter = 1

# while counter <= count:
#     print("Hello, World!")

#     counter += 1
# **************************************************


# **************************************************
# # NEW
# count = 10

# counter = 1

# while counter <= count:
#     print("Hello, World!")

#     counter += 1
# **************************************************


# **************************************************
# count = 10
# counter = 1

# while counter <= count:
#     # NEW
#     print(counter)
#     # print("Hello, World!")

#     counter += 1
# **************************************************


# **************************************************
# count = 10
# counter = 1

# while counter <= count:
#     print(counter)

#     # NEW
#     counter += 2
# **************************************************


# **************************************************
# count = 10

# # NEW
# # counter = 1
# counter = 2

# while counter <= count:
#     print(counter)

#     counter += 2
# **************************************************


# **************************************************
# # NEW
# count = 100
# counter = 1

# while counter <= count:
#     # NEW
#     if counter % 7 == 0:
#         print(counter)

#     # NEW
#     counter += 1
# **************************************************


# **************************************************
# count = 100
# counter = 1

# # NEW
# while counter * 7 <= count:
#     # NEW
#     print(counter * 7)

#     counter += 1
# **************************************************


# **************************************************
# count = 100

# # NEW
# counter = 7

# while counter <= count:
#     print(counter)

#     # NEW
#     counter += 7
# **************************************************


# **************************************************
# هرگاه برنامه، به دستور
# break
# برخورد نماید، از آخرین (درونی‌ترین) حلقه‌ای که در داخل آن قرار دارد، خارج می‌شود
# **************************************************
# هرگاه برنامه به دستور
# Continue
# برخورد نماید، به ابتدای آخرین (درونی‌ترین) حلقه‌ای که در داخل آن قرار دارد
# وارد شده و شرط آن‌را تست می‌کند
# **************************************************
# index = 1

# while index <= 10:
#     if index == 3:
#         index = 6
#         continue

#     if index == 8:
#         break

#     print(index)
#     index += 1
# **************************************************


# **************************************************
# import os
# import subprocess

# if os.name == "nt":
#     subprocess.run(args="cls", shell=True)
# else:
#     subprocess.run(args="clear", shell=True)

# print("=" * 50)
# print("Dariush Tasdighi Simple Chatbot!")

# # while 1 == 1:
# while True:
#     print("-" * 50)
#     user_prompt = input("User: ").strip()

#     if user_prompt == "":  # Null String
#         print("-" * 50)
#         print()
#         continue

#     # if user_prompt == "bye":
#     #     break

#     # if user_prompt == "bye" or user_prompt == "Bye":
#     #     break

#     # if user_prompt.lower() == "bye":
#     #     break

#     # if user_prompt.lower() == "bye" or user_prompt.lower() == "exit":
#     #     break

#     # if user_prompt.lower() == "bye" or user_prompt.lower() == "exit" or user_prompt.lower() == "quit":
#     #     break

#     if user_prompt.lower() in ["bye", "exit", "quit"]:
#         break

#     assistant_answer = f"Your question is: {user_prompt}"  # Echo
#     print(f"AI: {assistant_answer}")
#     print("-" * 50)
#     print()

# print("=" * 50)
# print()
# **************************************************


# **************************************************
# - Browser -> pip install rich
# - https://pypi.org/project/rich
# - pip install rich
# **************************************************
import os
import subprocess

# NEW
# import rich
from rich import print

if os.name == "nt":
    subprocess.run(args="cls", shell=True)
else:
    subprocess.run(args="clear", shell=True)

print("=" * 50)

# NEW
# print("Dariush Tasdighi Simple Chatbot!")
# print("[blue]Dariush Tasdighi Simple Chatbot![/blue]")
# print("[bold]Dariush Tasdighi Simple Chatbot![/bold]")
# print("[bold][blue]Dariush Tasdighi Simple Chatbot![/blue][/bold]")
# print("[blue][bold]Dariush Tasdighi Simple Chatbot![/bold][/blue]")
# print("[blue bold]Dariush Tasdighi Simple Chatbot![/blue bold]")
print("[blue bold]Dariush Tasdighi[/blue bold] [yellow]Simple Chatbot![/yellow]")

while True:
    print("-" * 50)
    user_prompt = input("User: ").strip()

    if user_prompt == "":
        print("-" * 50)
        print()
        continue

    if user_prompt.lower() in ["bye", "exit", "quit"]:
        break

    assistant_answer = f"Your question is: {user_prompt}"  # Echo
    print(f"AI: {assistant_answer}")
    print("-" * 50)
    print()

print("=" * 50)
print()
# **************************************************
