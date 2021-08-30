from errbot import BotPlugin, botcmd, botmatch

nome = None
modelo = None
problema = None

class Atendimento(BotPlugin):

    @botcmd
    def ajudacamera(self, msg, args):
        """
        Começa o atendimento perguntando o nome do cliente.
        """
        yield "Olá! Seja bem-vindo ao canal de suporte técnico da Intelbras no Discord!"
        yield "Eu me chamo Smart, o robô de suporte das câmeras Mibo."
        yield "Para começar, comece dizendo o seu nome para começar o nosso atendimento:"

    @botmatch
    def nomear(self, msg, match):
        """
        Agora que tem o nome, começa o atendimento.
        """
        global nome
        nome = match.string.capitalize()
        yield "Olá, " + nome + "! Vamos começar o nosso atendimento."

    @botmatch
    def modelocam(self, msg, match):
        global modelo
        modelo = match.string.capitalize()
        yield "Para começar, comece dizendo o modelo da sua câmera:"
        yield "iM3 | iM4 | iM5 S"
    
