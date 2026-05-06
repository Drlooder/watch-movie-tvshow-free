import requests
import json
import random
from temp_mail import TempMail
import re
import pyfiglet
import os
import webbrowser

# website to get movie informations: https://www.omdbapi.com/
# webiste to load the movie, tvShow: https://vidapi.ru/
# temp mail lib: https://github.com/cardisnotvalid/10MinuteMail.net by https://github.com/cardisnotvalid

API_KEY = ""


def HTML_Create_and_Stream(ID, type, season=1, episod=1):
    HTML_TEXT_MOVIE = f"""
    <html>
    <body style="margin:0">
        <iframe
            src="https://vaplayer.ru/embed/movie/{ID}"
            width="100%" height="100%"
            frameborder="0" allowfullscreen>
        </iframe>
    </body>
    </html>
    """

    HTML_TEXT_TV = f"""
    <html>
    <body style="margin:0">
        <iframe
            src="https://vaplayer.ru/embed/tv/{ID}/{season}/{episod}"
            width="100%" height="100%"
            frameborder="0" allowfullscreen>
        </iframe>
    </body>
    </html>
    """

    filename = "index.html"

    with open(filename, "w", encoding="utf-8") as file:
        if type == "series":
            file.write(HTML_TEXT_TV)
        elif type == "movie":
            file.write(HTML_TEXT_MOVIE)

    webbrowser.open(filename)

def generateDiffNames():
    fname = ''
    lname = ''
    text = ''

    charest = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".capitalize()

    limit = [5, 9, 8, 10, 12, 4, 6]
    count = 0
    for _ in charest:
        maxCount = random.choice(limit)
        fname = fname + random.choice(charest)
        lname = lname + random.choice(charest)
        if fname and lname:
            count += 1

        if maxCount == count:
            break
        
    limit = [12, 15, 16, 19, 20]
    count = 0
    for _ in charest:
        maxCount = random.choice(limit)
        text = text + random.choice(charest)

        if text and lname:
            count += 1

        if maxCount == count:
            break

    return fname, lname, text

def createEmail():
    print("[+] - start creating temp mail ")
    tm = TempMail()
    email = tm.get_email_address()
    print("[+] - email created " + email)

    return email, tm

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_logo()


def GetNewAPI():
    print("[+] - start generating new api key.")
    url = "https://www.omdbapi.com/apikey.aspx"
    invaildMSG = "A key has already been assigned to that email address."
    
    
    fname, lname, text = generateDiffNames()
    email, tm = createEmail()

    payload = {
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__LASTFOCUS": "",
        "__VIEWSTATE": "/wEPDwUKLTIwNDY4MTIzNQ9kFgYCAQ9kFggCAQ8QDxYCHgdDaGVja2VkaGRkZGQCAw8QDxYCHwBnZGRkZAIFDxYCHgdWaXNpYmxlaGQCBw8WAh8BZ2QCAg8WAh8BZxYCAgEPDxYCHgRUZXh0BUxBIHZlcmlmaWNhdGlvbiBsaW5rIHRvIGFjdGl2YXRlIHlvdXIga2V5IHdhcyBzZW50IHRvOiBkNDgxNTM4NmJjQGVtYWlsYXgucHJvZGQCAw8WAh8BZxYCAgEPDxYCHwIFNkEga2V5IGhhcyBhbHJlYWR5IGJlZW4gYXNzaWduZWQgdG8gdGhhdCBlbWFpbCBhZGRyZXNzLmRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQtwYXRyZW9uQWNjdAULcGF0cmVvbkFjY3QFCGZyZWVBY2N0X6StVZ26p1cctMa7N3cdZyghynNCfQ46dqFyIhECv+w=",
        "__VIEWSTATEGENERATOR": "5E550F58",
        "__EVENTVALIDATION": "/wEdAAgRI5UZ9GYIuD7SpqTDMQlNmSzhXfnlWWVdWIamVouVTzfZJuQDpLVS6HZFWq5fYphdL1XrNEjnC/KjNya+mqh8hRPnM5dWgso2y7bj7kVNLSFbtYIt24Lw6ktxrd5Z67/4LFSTzFfbXTFN5VgQX9Nbzfg78Z8BXhXifTCAVkevd/Qady6OV/MMzi0IXaZwY8QSWK1ZUGL9KK3euQYMcAZq",
        "at": "",
        "freeAcct": "on",
        "Email2": email,
        "FirstName": fname,
        "LastName": lname,
        "TextArea1": text,
        "Button1": "Submit"
    }

    response = requests.get(url=url, params=payload)

    if invaildMSG in response.text:
        print("[+] - error cann`t create new key try do it manully")
    else:
        try:
            global API_KEY
            print("[+] - waiting for message")
            message = tm.wait_for_message()

            print("[+] - Updating the new key")

            key_match = re.search(r"key:\s*([a-fA-F0-9]+)", message)
            token = key_match.group(1) if key_match else "Not found"

            url_match = re.search(r"(http[s]?://www\.omdbapi\.com/apikey\.aspx\?VERIFYKEY=[a-fA-F0-9-]+)", message)
            activation_url = url_match.group(1) if url_match else "Not found"

            print(f"[+] - Token: {token}")
            print(f"[+] - Activation URL: {activation_url}")

            print("[+] - trying activate token ")

            try:
                url = activation_url
                response = requests.post(url=url)
            except Exception as e:
                print(e)

            if response.text == "Your key is now activated!":
                print("[+] - key activated.")
            else:
                print(f"[!] - visit {activation_url} to active: ", token)
            
            return token
        
        except Exception as e:
            print("[-] - error while creating API key. try do it manualy")
            print(e)

def GetSavedAPIkeys(key=None):
    try:
        with open("api.json", "r") as file:
            data = json.load(file)
            if key:
                for id, table in data.items():
                    if table.get("key") == key:
                        return data[id]
                return None
            
            else:
                return data
    except:
        print("[!] Can not open or get saved api keys.")

def editAPIKeyUsing(key, using):
    try:
        with open("api.json", "r") as file:
            data = json.load(file)


        for entry_id, table in data.items():
            if table.get('key') == key:

                data[entry_id]['used'] = table.get('used', 0) - using
                

        with open("api.json", "w") as file:
            json.dump(data, file, indent=4)

    except:
        print("[!] - cannot edit the key usses")

def SaveAPIKey(key=None):
    data = {}
    try:
        with open("api.json", "r") as file:
            data = json.load(file)
    except:
        print("[!] - error can`t find save file.")
        CreateAPIkeySaveFile()
        SaveAPIKey(key)

    if key:
        print("[+] - start registering a new key")
        data[str(len(data) + 1)] = {"key": key, "used": 1000}

        with open("api.json", "w") as file:
            json.dump(data, file, indent=4)

        print(f"[+] - new key: {key} saved.")

    return data

def CreateAPIkeySaveFile():
    print("[+] - creating save file")
    with open("api.json", "w") as file:
        file.write("{}")
    
    print("[+] - File created successfully.")

def setApiKey(key):
    global API_KEY
    API_KEY = key
    print(f"[+] - new api key applied key {key}")


def handle_tv(key, data):
    print("\n[+] - Handling tv shows")

    SELECTED_SEASON = 0
    SELECTED_EPISOD = 0

    seasons = data["totalSeasons"]
    seasons = int(seasons)

    for i in range(seasons + 1):
        if i == 0: 
            continue
        print(f"[+] - season {i}")

    while True:
        try:
            selection = int(input(f"Select Season (1-{str(seasons)}) .>  "))
            
            if selection < 0:
                continue

            if selection > seasons:
                continue

            if selection > 0 and selection <= seasons:
                SELECTED_SEASON = selection
                break
        except:
            print("invaild input")


    try:
        url = f"http://www.omdbapi.com/?apikey={key}&t=you&Season={selection}"
        editAPIKeyUsing(key, 1)
        response = requests.post(url=url, timeout=10)
        seasonsData = json.loads(response.text)
        
        choices = {}
        for k, v in seasonsData.items():
            if k == "Episodes":
                episods = len(v)
                for i in range(len(v)):
                    print(f"[+] - [{i+1}] " + v[i]["Title"])
                    choices[i+1] = v[i]["Title"]
                break

        while True:
            try:
                selection = int(input(f"Select Episod (1-{str(episods)}) .>  "))
                
                if selection < 0:
                    continue

                if selection > episods:
                    continue

                if selection > 0 and selection <= episods:
                    print("[+] - Selected: " + choices[selection])
                    SELECTED_EPISOD = selection
                    break
            except:
                print("invaild input")

    except Exception as e:
        print("[+] - faild.", e)

    if SELECTED_EPISOD == 0 or SELECTED_SEASON == 0:
        print("[!] - can`t get the selected season or episod")
        return

    print("Injoy your watching")
    HTML_Create_and_Stream(data["imdbID"], data["Type"], SELECTED_SEASON, SELECTED_EPISOD)

def GetInfo(name, key):
    url = f"http://www.omdbapi.com/?apikey={key}&t={name}"
    editAPIKeyUsing(key, 1)
    response = requests.post(url=url)
    if response.status_code == 200:
        data = json.loads(response.text)

        if data["Response"] == "False":
            print("Unactivated api")
            return

        if data["Response"]:
            print("ID: " + data["imdbID"])
            print("Title: " + data["Title"])
            print("Desc: " + data["Plot"] + "\n")

            imdb_id = data["imdbID"]
            if data["Type"] == "movie":
                HTML_Create_and_Stream(imdb_id, data["Type"])
            elif data["Type"] == "series":
                handle_tv(key, data)


def print_logo():
    print(pyfiglet.figlet_format("Drlooder", "big"))

    print("""
    [+] Made by Drlooder
    [+] For more tools Github: https://github.com/Drlooder
    [+] Thanks for: 
            [+] - website to get movie informations and api: https://www.omdbapi.com/
            [+] -  webiste to load the movie, tvShow: https://vidapi.ru/
            [+] - temp mail lib: https://github.com/cardisnotvalid/10MinuteMail.net by https://github.com/cardisnotvalid
    """)

def selectAPIKey():
    print("\n[+] - choose key to use.")
    data = GetSavedAPIkeys()
    choices = {}
    while True:
    
        for id, table in data.items():
            print(f"[{id}] - {table['key']} ({table['used']})")
            choices[id] = table['key']

        try:
            selection = int(input(".> "))
            if selection < 0:
                print("[!] - what a nerd.")
                continue
            if selection > len(choices):
                print("[!] - wtf ru doing bro.")
                continue
            
            setApiKey(choices[str(selection)])
            break
        except:
            print("invaild input.")
            pass

def checkAPIKeys():
    try:
        with open("api.json", "r") as file:
            data = json.load(file)

        filtered_data = {}

        for k, v in data.items():
            if v.get('used', 0) >= 5:
                filtered_data[k] = v

        with open("api.json", "w") as file:
            json.dump(filtered_data, file, indent=4)
            
    except (FileNotFoundError, json.JSONDecodeError):
        print("[!] - File missing or corrupted!")
    except Exception as e:
        print(f"[!] - Error verifying tokens: {e}")

def start():
    clear_console()

    if GetSavedAPIkeys() == None:
        CreateAPIkeySaveFile()
        new_key = GetNewAPI()
        SaveAPIKey(new_key)
        setApiKey(new_key)
    else:
        print("[+] - save file found")

    if len(GetSavedAPIkeys()) == 0:
        new_key = GetNewAPI()
        SaveAPIKey(new_key)
        setApiKey(new_key)
    else:
        selectAPIKey()

    clear_console()

    choices = {
        "1": "Watch",
        "2": "Generate new API key",
        "3": "Select API key",
        '4': "Exit"
    }

    global API_KEY
    while True:
        for id in choices:
            print(f"[{id}] {choices[id]}")

        try:
            selection = int(input(".> "))

            if selection < 0:
                print("[!] - what a nerd.")
                continue

            if selection > len(choices):
                print("[!] - wtf ru doing bro.")
                continue
            
            if selection == 1:
                clear_console()
                Stream(API_KEY)
                break

            if selection == 2:
                new_key = GetNewAPI()
                SaveAPIKey(new_key)
                setApiKey(new_key)

            if selection == 3:
                checkAPIKeys()
                selectAPIKey()

            if selection == 4:
                print("cya.")
                break

        except:
            print("[!] - insert a vaild input.")

def Stream(key):
    print("[+] - Type !Exit to close.")
    try:
        while True:
            name = input("Enter Name.> ")
            
            if name == "!Exit":
                break
            if name:
                clear_console()
                name.replace(" ", "+")
                break
        GetInfo(name, key)
    except:
        pass

start()