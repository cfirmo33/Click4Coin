import os
import asyncio
from time import sleep
from sys import argv
from telethon import TelegramClient, errors

# API variables
api_id = 12345 		             # add your api_id here
api_hash = "19f30c5a1c..."       # add your api_hash here

user_names = ["Zcash_click_bot", "Dogecoin_click_bot", "Litecoin_click_bot", "BCH_clickbot", "BitcoinClick_bot"]
message = "/visit"

# Client Object
client = TelegramClient("session_C4C", api_id, api_hash)
client.start()

# Then we need a loop to work with
loop = asyncio.get_event_loop()


async def visiting_link(messages):
    """
    get message, find link and execute with curl
    :param messages: get bot message as param
    :return: nothing, just print url
    """
    start = str(messages).find("url=")
    link = str(messages)[start + 5:start + 36]
    if "'" in link:
        link = link[:-1]
    print(link)
    command = "curl --silent " + link + " > /dev/null"
    os.system(command)
    sleep(1)


async def get_balance(username):
    """
    get username, send balance command, get and filter message, print balance
    :param username: bot username
    :return: nothing just print balance
    """
    balance = "/balance"
    await client.send_message(username, balance)
    sleep(1)
    messages = await client.get_messages(username, limit=1)
    messages_list = str(messages[0])[8:-1].split(", ")
    print(str(messages_list[9])[9:-1])


async def main():
    if argv[1] == "logout":
        print("logging out...")
        await client.log_out()
        exit(0)

    while True:
        if len(user_names) <= 0:
            print("all ads finished, try again later...")
            exit(0)
        for username in user_names:
            try:
                await client.send_message(username, message)
                print("sending message to {}".format(username))
                sleep(1)
                messages = await client.get_messages(username, limit=1)
                if "Sorry," not in str(messages[0]):
                    await visiting_link(messages)
                    messages = await client.get_messages(username, limit=1)
                    if "10 seconds..." not in str(messages[0]):
                        print("skipping task...")
                        await messages[0].click(1, 1)
                    else:
                        print("site visited!")
                else:
                    print("no more ads in {}, removing bot from list.".format(username))
                    await get_balance(username)
                    user_names.remove(username)

            except errors.FloodWaitError as e:
                print('Have to sleep', e.seconds, 'seconds')
                print("this limit is set by telegram!\n Nobody knows the exact limits for all requests since they "
                      "depend on a lot of factors.\n don't worry about it.")
                sleep(e.seconds)
        print("wait 9 seconds...")
        sleep(9)


# Then, we need to run the loop with a task
loop.run_until_complete(main())
