import requests
from secrets import tokenSteam

eletrocompers = ["Marconauta",
                "KKDuShi",
                "Ottselatto",
                "Zayes",
                "Montanari",
                "Matheusuz",
                "BRCOLT",
                "SH4K3 P31D40",
                "Selectko"]

key_api = tokenSteam
steam_id = '76561198169109577'
    

def printOnlineFriends():

    friend_list_uri = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=' + key_api + '&steamid=' + steam_id + '&relationship=friend'
    friend_list = requests.get(friend_list_uri).json()['friendslist']['friends']

    steam_id_list = []
    steam_id_list.append(steam_id)
    for i in range(len(friend_list)):
        steam_id_list.append(friend_list[i]['steamid'])
    ids_join = ','.join(steam_id_list)

    profiles_uri = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + key_api + '&steamids=' + ids_join
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
    eletrocompers_count = 0
    for i in sorted(players_online_dict.keys()):
        if eletrocompers.__contains__(i):
            eletrocompers_count += 1
            tspaces = ''
            len_name_diff = ((max_namelen - len(i)) + 2)*2 + 1
            for x in range(len_name_diff):
                tspaces += ' '
            textoDiscord += i + tspaces + "[" + players_online_dict[i] + "]" + '\n'
    if eletrocompers_count == 0:
        textoDiscord = 'Nenhum eletrocomper jogando :c'
        
    return textoDiscord