import json
import praw
from mySteam import printOnlineFriends as friends
import requests
from secrets import tokenTelegram, tokenReddit, password



reddit = praw.Reddit(client_id='ZKgYtHVPcSTGzQ',
                     client_secret=tokenReddit, 
                     password=password,
                     user_agent='eletrocompers',
                     username='selectko')

class telegramBot:
    def __init__(self):
        token = tokenTelegram
        self.url_base = f'https://api.telegram.org/bot{token}/'
        self.channel = "dataisbeautiful"

    # Iniciar o bot
    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_mensagens(update_id)
            mensagens = atualizacao['result']
            if mensagens:
                for mensagem in mensagens:
                    if 'message' in mensagem:
                        update_id = mensagem['update_id']
                        chat_id = mensagem['message']['chat']['id']
                        eh_primeira_mensagem = mensagem['message']['message_id'] == 1
                        resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
                        if resposta is not None:
                            self.responder(resposta, chat_id)
                        else:
                            self.responder("Comando não reconhecido, digite /help para acessar a cental de comandos", chat_id)

    # Obter mensagens
    def obter_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeou=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if 'text' in mensagem['message']:
            terminal = mensagem['message']['text']
            terminal = terminal.split("@")
            cmd = terminal[0]
            if cmd == '/help':
                help = "/play => Ver amiguinhos que estão jogando\n/waifu => Uma waifu só sua\n/r@nome_subreddit => Seleciona um post aleatorio do 'nome_subreddit'\n"
                return help
            if cmd == '/play':
                return friends()    
            if cmd == '/waifu':
                submission = reddit.subreddit("CuteAnimeGirls").random()
                return submission.url
            if cmd == f'/r':
                try:
                    self.channel = terminal[1]
                    submission = reddit.subreddit(self.channel).random()
                    return submission.url
                except Exception:
                    return 'Não existe essa poha seu corno!'
        else:
            return None

    # Responder 
    def responder(self, resposta, chat_id):
        link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio)