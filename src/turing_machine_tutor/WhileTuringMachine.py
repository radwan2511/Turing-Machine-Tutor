import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.IFTuringMachine import IFTuringMachine

class WhileTuringMachine(IFTuringMachine):
    def __init__(self, condTMName:str,condTM : TuringMachine, doTMName:str, doTM : TuringMachine):
        super().__init__(condTMName,condTM, doTMName, doTM, "", None)
    
    # def run(self, input_str,head_position=0):
    #     self.run(input_str,head_position)
    
    # def given_state_is_in_acceptance(self,state):
    #     return self.given_state_is_in_acceptance(state)
    # def get_input_alphabet(self):
    #     return self.get_input_alphabet()
    
    # def __str__(self):
    #     return self.__str__()
    
    def run(self, input_str,head_position=0): ##if it is not given then it is 0, this what means the '=0'
        self.resultTM = self.thenTm
        machine_run_state = None
        while 1:
            if(self.ifTm == None or (not isinstance(self.ifTm, TuringMachine))):
                raise Exception("Cannot run, Missing IF TM. Please Use SetIFtm to set the turing machine")
            if(self.thenTm == None or (not isinstance(self.thenTm, TuringMachine))):
                raise Exception("Cannot run, Missing Then TM. Please Use SetThentm to set the turing machine")
            # first run ifTm
            machine_run_state2 = self.ifTm.run(input_str)
            if (machine_run_state2.state in self.ifTm.accept_states):
                # then run thenTm
                machine_run_state = self.thenTm.run(input_str)
                input_str = ''.join(machine_run_state.tape.copy())
                self.resultTM = self.thenTm
                #return machine_run_state
            else:
                print("TM Cond rejected the input: "+input_str)
                break
        return machine_run_state
    

    def __str__(self):
            st = f"WhileTuringMachine('{self.ifTm.name}', {self.ifTm}, '{self.thenTm.name}', {self.thenTm})"
            return st