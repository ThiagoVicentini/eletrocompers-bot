import requests, os
from dotenv import load_dotenv

# Carrega o conteudo do arquivo .env
load_dotenv()

friends = []
with open("friends.txt") as file:
    friend = file.readline()
    while friend != '':
        friends.append(friend)
        friend = file.readline()

STEAM_KEY = None
STEAM_ID = None
try:
    STEAM_KEY = os.environ["STEAM_KEY"]
    STEAM_ID = os.environ["STEAM_ID"]
except:
    raise Exception("Erro ao ler o conteudo do .env")


def printOnlineFriends():

    friend_list_uri = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=' + STEAM_KEY + '&steamid=' + STEAM_ID + '&relationship=friend'
    friend_list = requests.get(friend_list_uri).json()['friendslist']['friends']

    STEAM_ID_list = []
    STEAM_ID_list.append(STEAM_ID)
    for i in range(len(friend_list)):
        STEAM_ID_list.append(friend_list[i]['steamid'])
    ids_join = ','.join(STEAM_ID_list)

    profiles_uri = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + STEAM_KEY + '&steamids=' + ids_join
    profiles = requests.get(profiles_uri).json()['response']
    
    players_online_dict = {}
    global max_namelen
    max_namelen = 0

    for i in range(len(profiles['players'])):
        status_profile = profiles['players'][i]['personastate']
        if status_profile != 0:
            if 'gameextrainfo' in profiles['players'][i]:
                player_name = profiles['players'][i]['personaname']
                player_game = profiles['players'][i]['gameextrainfo']
                players_online_dict.update( {player_name : player_game} )
                if len(player_name) > max_namelen:
                    max_namelen = int(len(player_name))
        else:
            continue

    textoDiscord = ''
    friends_count = 0
    for i in sorted(players_online_dict.keys()):
        if friends.__contains__(i):
            friends_count += 1
            tspaces = ''
            len_name_diff = ((max_namelen - len(i)) + 2)*2 + 1
            for x in range(len_name_diff):
                tspaces += ' '
            textoDiscord += i + tspaces + "[" + players_online_dict[i] + "]" + '\n'
    if friends_count == 0:
        textoDiscord = 'Ninguem jogando :c'
        
    return textoDiscord