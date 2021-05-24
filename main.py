try:
	import requests
	import json
	import random
	import string
	from time import sleep
except:
	print("You need to install the packages!")

print("""

  ___ ___   _______   ___       ___ ___      ___ ___   _______   _______    ___ ___   _______   _______   ___ ___  
 |   Y   | |   _   | |   |     |   Y   |    |   Y   | |   _   | |   _   \  |   Y   | |   _   | |   _   | |   Y   ) 
 |.  1   | |.  |   | |.  |     |   1   |    |.  |   | |.  1___| |.  1   /  |.  1   | |.  |   | |.  |   | |.  1  /  
 |.  _   | |.  |   | |.  |___   \_   _/     |. / \  | |.  __)_  |.  _   \  |.  _   | |.  |   | |.  |   | |.  _  \  
 |:  |   | |:  1   | |:  1   |   |:  |      |:      | |:  1   | |:  1    \ |:  |   | |:  1   | |:  1   | |:  |   \ 
 |::.|:. | |::.. . | |::.. . |   |::.|      |::.|:. | |::.. . | |::.. .  / |::.|:. | |::.. . | |::.. . | |::.| .  )
 `--- ---' `-------' `-------'   `---'      `--- ---' `-------' `-------'  `--- ---' `-------' `-------' `--- ---' 

""")

print("Welcome to The Holy Webhook Spammer\nMade by TTheHolyOne#1642")

messageinput = input("What is the message you want to send?\n")
usernameinput = input("What is the username you want?")

print("Get ready for hell..")

def random_number(digits):
    range_start = 10**(digits-1)
    range_end = (10**digits)-1
    return random.randint(range_start, range_end)


def send_message(webhook_url):
    username = usernameinput
    message = f"@everyone {messageinput}"
    avatar = "https://picsum.photos/id/{}/200".format(random.randint(1, 500))
    data = json.dumps({
        "content": message,
        "username": username,
        "avatar_url": avatar,
        "tts": True
    })

    header = {
        "content-type": "application/json"
    }

    response = requests.post(webhook_url, data, headers=header)

    if not response.ok:
        if response.status_code == 429:
            print("Too many requests.. - waiting before retying..")
        else:
            print("Failed to send message!")
            print(response.status_code)
            print(response.reason)
            print(response.text)
        return False
    else:
        print("Send message!")
        return True

webhook = input("Webhook URL you want to spam: \n")
attempt_count = 0
sent_count = 0

print("Spamming that skids webhook! Press CTRL+C to stop!")


failed_previous = False

try:
    while True:
        if (send_message(webhook)):
            sent_count += 1
            failed_previous = False
        else:
            if failed_previous:
                print("Waiting 30 seconds! - didn't work second time!")
                sleep(30)
            else:
                sleep(1)
            failed_previous = True
        attempt_count += 1
except KeyboardInterrupt:
    print("Stopped! Send {} messages and did {} attempts. We made the skid cry today :D".format(sent_count, attempt_count))
    pass


print("Goodbye...")