import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.IFTuringMachine import IFTuringMachine
from turing_machine_tutor.machine_run_state import Machine_Run_State
from turing_machine_tutor.Next import Next

import unittest
# Purpose: Verify that individual units of code (functions, methods, or classes) work as intended.

ifTm = TuringMachine( # condition if input legth is less than 4 accept else reject
states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
input_alphabet={'0', '1'},
tape_symbols={'0', '1', 'B'},
transitions={
    ('q0', '0'): Next('q1', '0', 'R'),
    ('q0', '1'): Next('q1', '1', 'R'),

    ('q1', '0'): Next('q2', '0', 'R'),
    ('q1', '1'): Next('q2', '1', 'R'),

    ('q2', '0'): Next('q3', '0', 'R'),
    ('q2', '1'): Next('q3', '0', 'R'),
    
    ('q3', '0'): Next('q6', '0', 'R'),
    ('q3', '1'): Next('q6', '1', 'R'),
    ('q3', 'B'): Next('q5', 'B', 'S')
},
initial_state='q0',
accept_states={'q5'},
reject_states={'q6'}
)
    
thenTm = TuringMachine( # condition if input legth is less than 4 change every 1 to 0
states={'q0', 'q1', 'q2'},
input_alphabet={'0', '1'},
tape_symbols={'0', '1', 'B'},
transitions={
    ('q0', '0'): Next('q0', '0', 'R'),
    ('q0', '1'): Next('q0', '0', 'R'),
    ('q0', 'B'): Next('q1', 'B', 'R')
},
initial_state='q0',
accept_states={'q1'},
reject_states={'q2'}
)

elseTm = TuringMachine( # condition if input legth is less than 4 change every 0 to 1
states={'q0', 'q1', 'q2'},
input_alphabet={'0', '1'},
tape_symbols={'0', '1', 'B'},
transitions={
    ('q0', '0'): Next('q0', '1', 'R'),
    ('q0', '1'): Next('q0', '1', 'R'),
    ('q0', 'B'): Next('q1', 'B', 'R')
},
initial_state='q0',
accept_states={'q1'},
reject_states={'q2'}
)
class TestIFTuringMachine(unittest.TestCase):
 
    ###############################################################################################################
    # test Not Valid IF TM Run with Not valid set IF TM
    def test_IFTM_Run_withNotValid1IFTM_IFTM_TuringMachine(self):
        try:
            result = IFTuringMachine("myif", ifTm, "mythen", thenTm, "myelse", elseTm)
            result.setIfTM("",None)
            result.run("001")
        except Exception as e:
            self.assertEqual("ifTM cannot be Not Turing Machine Object", str(e))
    ###############################################################################################################
    # test Not Valid IF TM Run with Not valid set IF TM
    def test_IFTM_Run_withNotValid2IFTM_IFTM_TuringMachine(self):
        not_valid = [2,'w',["2","2"]]
        for n_v in not_valid:
            try:
                result = IFTuringMachine("myif", ifTm, "mythen", thenTm, "myelse", elseTm)
                result.setIfTM(n_v,"")
                result.run("001")
            except Exception as e:
                self.assertEqual("ifTM cannot be Not Turing Machine Object", str(e))
    ###############################################################################################################
    # test Not Valid IF TM Run with Not valid set IF TM
    def test_IFTM_Run_withNotValid3IFTM_IFTM_TuringMachine(self):
        
        ifTm = TuringMachine( # condition if input legth is less than 4 accept else reject
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_alphabet={'0', '1'},
    tape_symbols={'0', '1', 'B'},
    transitions={
        ('q0', '0'): Next('q1', '0', 'R'),
        ('q0', '1'): Next('q1', '1', 'R'),

        ('q1', '0'): Next('q2', '0', 'R'),
        ('q1', '1'): Next('q2', '1', 'R'),

        ('q2', '0'): Next('q3', '0', 'R'),
        ('q2', '1'): Next('q3', '0', 'R'),
        
        ('q3', '0'): Next('q6', '0', 'R'),
        ('q3', '1'): Next('q6', '1', 'R'),
        ('q3', 'B'): Next('q5', 'B', 'S')
    },
    initial_state='q0',
    accept_states={'q5'},
    reject_states={'q6'}
)
        not_valid = [None, ""]
        for n_v in not_valid:
            try:
                result = IFTuringMachine("myif", ifTm, "mythen", thenTm, "myelse", elseTm)
                result.setIfTM(ifTm,n_v)
                result.run("001")
            except Exception as e:
                self.assertEqual("Name cannot be None", str(e))
    ###############################################################################################################
    # test Not Valid IF TM Run with Not valid set IF TM
    def test_IFTM_Run_withNotValid3IFTM_IFTM_TuringMachine(self):
        
        ifTm = TuringMachine( # condition if input legth is less than 4 accept else reject
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_alphabet={'0', '1'},
    tape_symbols={'0', '1', 'B'},
    transitions={
        ('q0', '0'): Next('q1', '0', 'R'),
        ('q0', '1'): Next('q1', '1', 'R'),

        ('q1', '0'): Next('q2', '0', 'R'),
        ('q1', '1'): Next('q2', '1', 'R'),

        ('q2', '0'): Next('q3', '0', 'R'),
        ('q2', '1'): Next('q3', '0', 'R'),
        
        ('q3', '0'): Next('q6', '0', 'R'),
        ('q3', '1'): Next('q6', '1', 'R'),
        ('q3', 'B'): Next('q5', 'B', 'S')
    },
    initial_state='q0',
    accept_states={'q5'},
    reject_states={'q6'}
)
        not_valid = [["asd"], 555]
        for n_v in not_valid:
            try:
                result = IFTuringMachine("myif", ifTm, "mythen", thenTm, "myelse", elseTm)
                result.setIfTM(ifTm,n_v)
                result.run("001")
            except Exception as e:
                self.assertEqual("Name cannot be not str object", str(e))
    ###############################################################################################################
    # test Not Valid IF_TM Run with missing Then TM
    def test_IFTM_Run_withMissing_ThenTM_TuringMachine(self):
        ifTm = TuringMachine( # condition if input legth is less than 4 accept else reject
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_alphabet={'0', '1'},
    tape_symbols={'0', '1', 'B'},
    transitions={
        ('q0', '0'): Next('q1', '0', 'R'),
        ('q0', '1'): Next('q1', '1', 'R'),

        ('q1', '0'): Next('q2', '0', 'R'),
        ('q1', '1'): Next('q2', '1', 'R'),

        ('q2', '0'): Next('q3', '0', 'R'),
        ('q2', '1'): Next('q3', '0', 'R'),
        
        ('q3', '0'): Next('q6', '0', 'R'),
        ('q3', '1'): Next('q6', '1', 'R'),
        ('q3', 'B'): Next('q5', 'B', 'S')
    },
    initial_state='q0',
    accept_states={'q5'},
    reject_states={'q6'}
)
        try:
            result = IFTuringMachine("myif", ifTm, "mythen", thenTm, "myelse", elseTm)
            result.setIfTM(ifTm, "myIf")
            result.run("001")
        except Exception as e:
            self.assertEqual("Cannot run, Missing Then TM. Please Use SetThentm to set the turing machine", str(e))
    ###############################################################################################################
    # test Valid IF_TM Run
    def test_IFTM_Valid1_Run_TuringMachine(self):
        ifTm = TuringMachine( # condition if input legth is less than 4 accept else reject
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_alphabet={'0', '1'},
    tape_symbols={'0', '1', 'B'},
    transitions={
        ('q0', '0'): Next('q1', '0', 'R'),
        ('q0', '1'): Next('q1', '1', 'R'),

        ('q1', '0'): Next('q2', '0', 'R'),
        ('q1', '1'): Next('q2', '1', 'R'),

        ('q2', '0'): Next('q3', '0', 'R'),
        ('q2', '1'): Next('q3', '0', 'R'),
        
        ('q3', '0'): Next('q6', '0', 'R'),
        ('q3', '1'): Next('q6', '1', 'R'),
        ('q3', 'B'): Next('q5', 'B', 'S')
    },
    initial_state='q0',
    accept_states={'q5'},
    reject_states={'q6'}
)
        
        thenTm = TuringMachine( # condition if input legth is less than 4 change every 1 to 0
    states={'q0', 'q1', 'q2'},
    input_alphabet={'0', '1'},
    tape_symbols={'0', '1', 'B'},
    transitions={
        ('q0', '0'): Next('q0', '0', 'R'),
        ('q0', '1'): Next('q0', '0', 'R'),
        ('q0', 'B'): Next('q1', 'B', 'R')
    },
    initial_state='q0',
    accept_states={'q1'},
    reject_states={'q2'}
)

        try:
            result = IFTuringMachine("myif", ifTm, "mythen", thenTm, "myelse", elseTm)
            result.setIfTM(ifTm, "myIf")
            result.setThenTM(thenTm,"mythen")
            self.assertEqual(''.join((result.run("001").tape)).replace('B',''),"000")
        except Exception as e:
            self.fail("If Tm Run throwed exception where it shouldn't")

    ###############################################################################################################
    # test Valid IF_TM Run
    def test_IFTM_Valid2_Run_TuringMachine(self):

        try:
            result = IFTuringMachine("myif", ifTm, "mythen", thenTm, "myelse", elseTm)
            result.setIfTM(ifTm, "myIf")
            result.setThenTM(thenTm,"mythen")
            result.setElseTM(elseTm,"myelse")
            self.assertEqual(''.join((result.run("001").tape)).replace('B',''),"000")
            self.assertEqual(''.join((result.run("001011").tape)).replace('B',''),"111111")
        except Exception as e:
            self.fail("If Tm Run throwed exception where it shouldn't")
    

if __name__ == '__main__':
    unittest.main()
