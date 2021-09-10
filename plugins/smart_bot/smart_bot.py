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
        
        yield "nomear"

        global nome
        nome = match.string.capitalize()

        yield "Olá, " + nome + "! Vamos começar o nosso atendimento."
        yield "Primeira coisa: qual é o modelo da sua câmera? (digite a letra inicial para cada opção)"
        yield "A iM3"
        yield "B iM4"
        yield "C iM5 S"

    @botmatch(r'^(A|B|C)$', flow_only=True)
    def modelocam(self, msg, match):
        """
        Pergunta o modelo da câmera e salva.
        """
        
        global modelo
        modelo = match.string.capitalize()
        
        if modelo == "A":
            yield "OK, sua câmera é uma iM3, iM3 Duo, iM3 Black ou iM3 c/micro-SD."
            modelo = "iM3"

        if modelo == "B":
            yield "OK, sua câmera é uma iM4 ou iM4 c/micro-SD."
            modelo = "iM4"

        if modelo == "C":
            yield "OK, sua câmera é uma iM5 S ou iM5 S c/micro-SD."
            modelo = "iM5 S"
        
        yield "Certo. Qual problema você está enfrentando? (digite a letra inicial para cada opção)"
        yield "A Não conecta"
        yield "B Desvincular câmera"
        yield "C Ajuda com compartilhamento"

    """
    @botmatch(r'^[D-Z|0-9|a-z]$', flow_only=True)
    def modelocam_alt(self, msg, match):
        
        Pergunta o modelo da câmera e salva.
        

        yield "Desculpa, não entendi. Por favor, utilize uma das letras iniciais para continuar o atendimento."
    """

    @botmatch(r'^(A|B|C)$', flow_only=True)
    def problemas(self, msg, match):
        """
        Qual problema o cliente está enfrentando?
        """
        
        global problema
        problema = match.string.capitalize()

        if problema == "A":
            yield "Ok, sua câmera não está conectando."
            problema = "Não conecta"
        
        if problema == "B":
            yield "Ok, você está com problemas para desvincular a sua câmera."
            problema = "Desvincular câmera"

        if problema == "C":
            yield "Ok, você está com problemas para compartilhar sua câmera."
            problema = "Ajuda com compartilhamento"

        yield "Ok, esses são os dados que nós temos:"
        yield "Seu nome:" + nome
        yield "Sua câmera:" + modelo
        yield "O problema que você está enfrentando:" + problema
        yield "Por favor, aguarde um pouco. Em breve um dos nossos atendentes vai te responder."
        yield "Foi um prazer atender você! ;)"
        
    """
    @botmatch(r'^[D-Z|0-9|a-z]$', flow_only=True)
    def problemas_alt(self, msg, match):
        
        Pergunta o modelo da câmera e salva.
        
        
        yield "Desculpa, não entendi. Por favor, utilize uma das letras iniciais para continuar o atendimento."
    """