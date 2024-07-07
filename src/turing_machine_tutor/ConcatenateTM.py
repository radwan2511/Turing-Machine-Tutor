import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.CombinedTuringMachine import CombinedTuringMachine

class ConcatenateTM(CombinedTuringMachine):
    def __init__(self, tm1name: str, TMObj1:TuringMachine, *additionalTMs):
        # if not isinstance(tm1name,str):
        #     raise Exception("tm name cannot be not str")
        # if len(ls) == 0:
        #     raise Exception("constructor parameter should be list of minimum len of 1!")
        index = 0
        for l in additionalTMs:
            if index % 2 == 0:
                if not isinstance(l, str):
                    raise Exception("parameter should be str of tm name!")
            else:
                if not isinstance(l, TuringMachine):
                    raise Exception("parameter should be TuringMachine Object!")
            index += 1
        
        if index%2 != 0:
            raise Exception("parameters number of TM name and TuringMachine should be equal!")
        super().__init__(TMObj1.input_alphabet)
        #self = CombinedTuringMachine(ls[0][1].input_alphabet)

        index = 0
        names = [tm1name]
        objs = [TMObj1]
        for l in additionalTMs:
            if index % 2 == 0:
                names.append(l)
            else:
                objs.append(l)
            index += 1
        
        for l in range(len(names)):
            self.add(names[l], objs[l])
        
    # def run(self, input_str,head_position=0):
    #     self.run(input_str,head_position)
    
    # def given_state_is_in_acceptance(self,state):
    #     return self.given_state_is_in_acceptance(state)
    
    # def get_input_alphabet(self):
    #     return self.get_input_alphabet()
    
    def __str__(self):
            #__init__(self, tm1name: str, TMObj1:TuringMachine, *additionalTMs):
            st = ""
            for t in self.turing_machines:
                st += ",'"+t.name +"',"+t.__str__()
            st = st[1:]

            st_res = f"ConcatenateTM({st})"
            return st_res 