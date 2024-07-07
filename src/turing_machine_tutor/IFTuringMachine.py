import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.TuringMachine import TuringMachine

class IFTuringMachine:
    def __init__(self, ifname,ifTM,thenName, ThenTM, elsename, elseTM):
        self.name = ""
        self.setIfTM(ifTM, ifname)
        #self.ifName = ""
        self.setThenTM(ThenTM, thenName)
        #self.thenName = ""
        try:
            self.setElseTM(elseTM, elsename)
        except:
            pass
        #self.elseName = ""
        self.resultTM = None

    def given_state_is_in_acceptance(self,state):
        return self.resultTM.given_state_is_in_acceptance(state)

    def setIfTM(self, tm, name):
        if(tm == None):
            raise Exception("ifTM cannot be None")
        if(not isinstance(tm, TuringMachine)):
            raise Exception("ifTM cannot be Not Turing Machine Object")
        if(name == None or name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        self.ifTm = tm
        self.ifTm.name = name
        #self.ifName = name
    def setThenTM(self, tm, name):
        if(tm == None):
            raise Exception("thenTM cannot be None")
        if(not isinstance(tm, TuringMachine)):
            raise Exception("thenTM cannot be Not Turing Machine Object")
        if(name == None or name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        self.thenTm = tm
        self.thenTm.name = name
        #self.thenName = name
    def setElseTM(self, tm, name):
        if(tm == None):
            raise Exception("elseTM cannot be None")
        if(not isinstance(tm, TuringMachine)):
            raise Exception("elseTM cannot be Not Turing Machine Object")
        if(name == None or name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        self.elseTm = tm
        self.elseTm.name = name
        #self.elseName = name

    def run(self, input_str):
        if(self.ifTm == None or (not isinstance(self.ifTm, TuringMachine))):
            raise Exception("Cannot run, Missing IF TM. Please Use SetIFtm to set the turing machine")
        if(self.thenTm == None or (not isinstance(self.thenTm, TuringMachine))):
            raise Exception("Cannot run, Missing Then TM. Please Use SetThentm to set the turing machine")
        # first run ifTm
        self.resultTM = self.thenTm
        machine_run_state = self.ifTm.run(input_str)
        if (machine_run_state.state in self.ifTm.accept_states):
            # then run thenTm
            machine_run_state = self.thenTm.run(input_str)
            self.resultTM = self.thenTm
            return machine_run_state
        elif(self.elseTm != None and isinstance(self.elseTm, TuringMachine)):
            # else run elseTm
            machine_run_state = self.elseTm.run(input_str)
            self.resultTM = self.elseTm
            return machine_run_state
    
    def get_input_alphabet(self):
        if(self.ifTm == None or (not isinstance(self.ifTm, TuringMachine))):
            raise Exception("Cannot get input alphabet, Missing IF TM. Please Use SetIFtm to set the turing machine")
        return self.setIfTM.input_alphabet
    
    def __str__(self):
            # st = ""
            # if self.ifTm != None and TuringMachine(self.ifTm,TuringMachine):
            #     st += "IF TM"
            #     st += ":::\n" + self.ifTm.__str__() + "\n"
            # if self.thenTm != None and TuringMachine(self.thenTm,TuringMachine):
            #     st += "THEN TM"
            #     st += ":::\n" + self.thenTm.__str__() + "\n"
            # if self.elseTm != None and TuringMachine(self.elseTm,TuringMachine):
            #     st += "ELSE TM"
            #     st += ":::\n" + self.elseTm.__str__() + "\n"
            # return st
            
            # IFTuringMachine("myif", ifTm, "mythen", thenTm, "myelse", elseTm)
            st = f"IFTuringMachine('{self.ifTm.name}', {self.ifTm}, '{self.thenTm.name}', {self.thenTm}, '{self.elseTm.name}', {self.elseTm})"
            return st