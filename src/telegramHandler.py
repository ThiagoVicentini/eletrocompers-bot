import requests, os, json
from steamHandler import printOnlineFriends
from redditHandler import subreddit
from dotenv import load_dotenv

load_dotenv()

class telegramBot:
    def __init__(self):
        TELEGRAM_KEY = None
        try:
            TELEGRAM_KEY = os.environ["TELEGRAM_KEY"]
        except:
            raise Exception("Erro ao ler o conteudo do .env")
        self.token = TELEGRAM_KEY
        self.url_base = f'https://api.telegram.org/bot{self.token}/'
        self.channel = ""

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
                help = "/play => Checa se os jogadores informados estão em jogo na Steam.\n\n/r@nome_subreddit => Seleciona um post aleatorio do 'nome_subreddit'\n"
                return help
            if cmd == '/play':
                return printOnlineFriends()    
            if cmd == f'/r':
                try:
                    self.channel = terminal[1]
                    return subreddit(self.channel)
                except Exception:
                    return 'Subreddit não encontrado!'
        else:
            return None

    # Responder 
    def responder(self, resposta, chat_id):
        link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio)