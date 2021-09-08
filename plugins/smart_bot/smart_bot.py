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
        yield "Primeira coisa: qual é o modelo da sua câmera? (digite a letra inicial para cada opção)"
        yield "A iM3"
        yield "B iM4"
        yield "C iM5 S"

    @botmatch(r'A|B|C', flow_only=True)
    def modelocam(self, msg, match):
        """
        Pergunta o modelo da câmera e salva.
        """
        global modelo
        modelo = match.string.capitalize()

        respostas_aceitaveis = ["A", "B", "C"]
        respostas_aceitaveis == True

        if respostas_aceitaveis == False:
            yield "Desculpa, não entendi. Por favor, utilize uma das letras iniciais para continuar o atendimento."

        else:
            respa = "OK, sua câmera é uma iM3, iM3 Duo, iM3 Black ou iM3 c/micro-SD."
            respb = "OK, sua câmera é uma iM4 ou iM4 c/micro-SD."
            respc = "OK, sua câmera é uma iM5 S ou iM5 S c/micro-SD."
            if modelo == "A":
                yield respa
 
            if modelo == "B":
                yield respb

            if modelo == "C":
                yield respc

    @botmatch(r'.*$', flow_only=True)
    def problemas(self, msg, match):
        """
        Qual problema o cliente está enfrentando?
        """
        yield "Certo. Qual problema você está enfrentando? (digite a letra inicial para cada opção)"
        yield "A Não conecta"
        yield "B Desvincular câmera"
        yield "C Ajuda com compartilhamento"
        global problema
        problema = match.string.capitalize()

        if problema == "A":
            yield "OK"
        
        if problema == "B":
            yield "OK"

        if problema == "C":
            yield "OK"
