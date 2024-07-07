class Call_Turing_Machine:
    def __init__(self, TM_name, tm, list_of_tapes_indexes, return_state_acc, return_state_rej):
        self.TM_name = TM_name  ## type is State
        self.tm = tm
        self.list_of_tapes_indexes=list_of_tapes_indexes ## symbol is string - one char
        #self.call_state=call_state ## Action is string - one char L,R,S
        self.return_state_acc = return_state_acc
        self.return_state_rej = return_state_rej

    def __str__(self):
        return f"Call_Turing_Machine('{self.TM_name}', {self.tm}, {self.list_of_tapes_indexes}, '{self.return_state_acc}', '{self.return_state_rej}')"