class Machine_Run_State:
    def __init__(self, tape,head_position ,state):
        self.tape=tape   ## type is list<string>
        self.head_position = head_position  ## type is int
        self.state = state  ## type is State




    def try_me(self,function):

        return function(1)




    def execute_config(self, config):
        self.tape[self.head_position] = config.symbol
        self.state=config.state
        if config.action == 'R':
            self.head_position += 1
            if self.head_position == len(self.tape):
                self.tape.append("B")  # Blank symbol for extending the tape to the right
        elif config.action == 'L':
            self.head_position -= 1
            if self.head_position < 0:
                self.head_position = 0
               # self.tape.insert(0, "B")  # Blank symbol for extending the tape to the left



    def put_word_on_tape(self, input_string):
        if(input_string == ''):
            self.tape = ['B']
        else:
            self.tape=list(input_string)



