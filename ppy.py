# This code may not work all the time
# You must provide your own ChatGPT API key as I cannot provide you with one for security reasons
# Created by ph0neh1 on 2024-01-30
# This only supports openai>=1.0.0:

import os
import time

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

os.system('cls||clear')
os.system("title Installing")
print("Downloading and installing required files... (This can take awhile)")
os.system("pip3 install openai==0.28") # Alternative to migration, uninstalls current OpenAI version
os.system('cls||clear')

import openai

openai.api_key = open_file('ChatGPTAPIKey.txt')

def ChatGPT(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None
    )
    return response['choices'][0]['text'].strip()

class TextColor:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"

os.system("title PythonGPT 1.0")
print(TextColor.GREEN + "<PythonGPT>" + TextColor.RESET + " " + "Currently running on" + " " + TextColor.RED + "Version 1.0")
print(TextColor.GREEN + "<PythonGPT>" + TextColor.RESET + " " + "Project designed and scripted by" + " " + TextColor.CYAN + "Ph0neh1" + TextColor.RESET)
time.sleep(5)
print(TextColor.GREEN + "<PythonGPT>" + TextColor.RESET + " " + "Type (exit) to quit PythonGPT")
while True:
    user_input= input(TextColor.YELLOW + "<User>" + TextColor.RESET + " " + ":" + " ")
    if user_input.lower() in ['exit']:
        print(TextColor.GREEN + "<PythonGPT>" + TextColor.RESET + " " + TextColor.RED + "Terminated PythonGPT" + TextColor.RESET)
        break

    prompt = f"{TextColor.YELLOW}<User>{TextColor.RESET} : {user_input}\n{TextColor.GREEN}<PythonGPT>{TextColor.RESET} :"
    chatgpt_response = ChatGPT(prompt)
    print(chatgpt_response)