from errbot import botflow, FlowRoot, BotFlow, FLOW_END

class AtendimentoFlow(BotFlow):
    """
    Flow para suporte técnico.
    """

    @botflow
    def passoapasso(self, flow: FlowRoot):
        first_step = flow.connect('começar', auto_trigger=True)
        second_step = first_step.connect('nomear')
        third_step = second_step.connect('modelocam')
        fourth_step = third_step.connect('problemas')
