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
        """
        third_step = second_step.connect('modelocam_alt')
        third_step = third_step.connect(third_step)
        fourth_step = third_step.connect('problemas')
        fourth_step = third_step.connect('problemas_alt')
        fourth_step = fourth_step.connect(fourth_step)
        fifth_step = fourth_step.connect('solução')
        fifth_step.connect(FLOW_END)
        """
