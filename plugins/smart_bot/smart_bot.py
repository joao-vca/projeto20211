from errbot import BotPlugin, botcmd, botmatch

nome = None
modelocam = None
problemas = None

class Atendimento(BotPlugin):
    @botcmd
    def começar(self, msg, args):
        """
        Começa o atendimento perguntando o nome do cliente.
        """
        yield "Olá! Seja bem-vindo ao canal de suporte técnico da Intelbras no Discord!"
        yield "Eu me chamo Smart, o robô de suporte das câmeras Mibo."
        yield "Para começar, comece dizendo o seu nome para começar o nosso atendimento:"

    @botmatch(r'.*$', flow_only=True)
    def nomear(self, msg, match):
        """
        Começa o atendimento perguntando o nome do cliente e salva.
        """
        global nome
        nome = match.string.capitalize()
        yield "Olá, " + nome + "! Vamos começar o nosso atendimento."

    @botmatch(r'.*$', flow_Only=True)
    def modelocam(self, msg, match):
        """
        Pergunta o modelo da câmera e salva.
        """
        global modelo
        modelo = match.string.capitalize()
        yield "Para começar, comece dizendo o modelo da sua câmera:"
        yield "iM3"
        yield "iM4"
        yield "iM5 S"
    
        if modelo == "iM3":
            yield "OK, sua câmera é uma iM3, iM3 Duo, iM3 Black ou iM3 c/micro-SD."
        
        if modelo == "iM4":
            yield "OK, sua câmera é uma iM4 ou iM4 c/micro-SD."

        if modelo == "iM5 S":
            yield "OK, sua câmera é uma iM5 S ou iM5 S c/micro-SD."
    
    @botmatch(r'.*$', flow_Only=True)
    def problemas(self, msg, match):
        """
        Qual problema o cliente está enfrentando?
        """
        global problema
        problema = match.string.capitalize()
        yield "Certo. Qual problema você está enfrentando?"
        yield "(1) Não conecta"
        yield "(2) Desvincular câmera"
        yield "(3) Ajuda com compartilhamento"

        if problema == "(1) Não conecta":
            yield "OK"
        
        if problema == "(2) Desvincular câmera":
            yield "OK"

        if problema == "(3) Ajuda com compartilhamento":
            yield "OK"
