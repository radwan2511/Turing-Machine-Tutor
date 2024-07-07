import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.machine_run_state import Machine_Run_State
from turing_machine_tutor.Next import Next

import unittest


# Purpose: Verify that individual units of code (functions, methods, or classes) work as intended.


class Machine_Run_State_Tests(unittest.TestCase):
    # test execute_config function
    def test_execute_config_success(self):
        config_test=Next("q0", "a", "R")
        machine_run_state_test=Machine_Run_State(["t","e","s","t"],0,"q1")
        #assume this transition ('q1','t') -> ('q0','a','R') exists
        machine_run_state_test.execute_config(config_test)
        self.assertEquals(machine_run_state_test.head_position,1)
        self.assertEquals(machine_run_state_test.state,'q0')
        self.assertEquals(machine_run_state_test.tape, ["a","e","s","t"])


    def test_execute_config_insert_blank_to_the_left(self):
        config_test=Next("q0", "t", "L")
        machine_run_state_test=Machine_Run_State(["t","e","s","t"],0,"q1")
        #assume this transition ('q1','t') -> ('q0','t','L') exists
        machine_run_state_test.execute_config(config_test)
        self.assertEquals(machine_run_state_test.head_position,0)
        self.assertEquals(machine_run_state_test.state,'q0')
        self.assertEquals(machine_run_state_test.tape, ["t","e","s","t"])

    def test_execute_config_insert_blank_to_the_right(self):
        config_test=Next("q0", "t", "R")
        machine_run_state_test=Machine_Run_State(["t","e","s","t"],3,"q1")
        #assume this transition ('q1','t') -> ('q0','t','R') exists
        machine_run_state_test.execute_config(config_test)
        self.assertEquals(machine_run_state_test.head_position,4)
        self.assertEquals(machine_run_state_test.state,'q0')
        self.assertEquals(machine_run_state_test.tape, ["t","e","s","t","B"])

    def test_execute_config_stay_option(self):
        config_test=Next("q0", "t", "S")
        machine_run_state_test=Machine_Run_State(["t","e","s","t"],3,"q1")
        #assume this transition ('q1','t') -> ('q0','t','S') exists
        machine_run_state_test.execute_config(config_test)
        self.assertEquals(machine_run_state_test.head_position,3)
        self.assertEquals(machine_run_state_test.state,'q0')
        self.assertEquals(machine_run_state_test.tape, ["t","e","s","t"])

    def test_put_word_on_tape(self):
        machine_run_state_test=Machine_Run_State([],3,"q1")
        machine_run_state_test.put_word_on_tape("test")
        self.assertEquals(machine_run_state_test.head_position,3)
        self.assertEquals(machine_run_state_test.state,'q1')
        self.assertEquals(machine_run_state_test.tape, ["t","e","s","t"])

if __name__ == '__main__':
    unittest.main()