from errbot import BotPlugin, botcmd


class Example(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd  # flags a command
    def bomdia(self, msg, args):
        """
        Responde educadamente ao solicitante.
        """
        return "fala aí rapaziada"  # This string format is markdown.
