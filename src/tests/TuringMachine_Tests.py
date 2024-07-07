import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.machine_run_state import Machine_Run_State
from turing_machine_tutor.Next import Next

import unittest
# Purpose: Verify that individual units of code (functions, methods, or classes) work as intended.


class TestTuringMachine(unittest.TestCase):
    # test Valid TM Constructor
    def test_TM_Constructor_withValidTuringMachine(self):
        try:
            result = TuringMachine(
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
        except Exception as e:
            self.fail("TuringMachine() raised Exception: "+str(e)+", with valid TuringMachine input unexpectedly!")
    ###############################################################################################################
            
    # test Not Valid TM Initial State
    def test_TM_Constructor_withInValidInitialState(self):
        not_valid_initial_state = [          ''       ,        None            ,    'q0']
        not_valid_states = [{'q0', 'q1', 'q2'},          {'q0', 'q1', 'q2'}    , {'q3', 'q1', 'q2'}]
        for index in range(0,2):

            try: 
                TuringMachine(
                states=not_valid_states[index],
                input_alphabet={'0', '1'},
                tape_symbols={'0', '1', 'B'},
                transitions={
                    ('q0', '0'): Next('q0', '0', 'R'),
                    ('q0', '1'): Next('q0', '0', 'R'),
                    ('q0', 'B'): Next('q1', 'B', 'R')
                },
                initial_state=not_valid_initial_state[index],
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                self.assertEqual("initial_state cannot be None / empty string, and must string of len > 1", str(e))

        for index in range(2,3):
            try:
                TuringMachine(
                states=not_valid_states[index],
                input_alphabet={'0', '1'},
                tape_symbols={'0', '1', 'B'},
                transitions={
                    ('q0', '0'): Next('q0', '0', 'R'),
                    ('q0', '1'): Next('q0', '0', 'R'),
                    ('q0', 'B'): Next('q1', 'B', 'R')
                },
                initial_state=not_valid_initial_state[index],
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                self.assertEqual("initial state must be in states", str(e))
    ###############################################################################################################
# test Not Valid TM input alphabet State
    def test_TM_Constructor_withInValidInputAlphabet(self):
        not_valid_input_alphabet = [          {}       ,        None         , {'00', '0' '1', 'B'}  ,    {'0'}]
        not_valid_tape_symbols = [{'0', '1', 'B'},          {'0', '1', 'B'}    , {'0', '1', 'B'},  {'B', '1', '2'}]
        for index in range(0,2):

            try: 
                TuringMachine(
                states={'q0', 'q1', 'q2'},
                input_alphabet=not_valid_input_alphabet[index],
                tape_symbols=not_valid_tape_symbols[index],
                transitions={
                    ('q0', '0'): Next('q0', '0', 'R'),
                    ('q0', '1'): Next('q0', '0', 'R'),
                    ('q0', 'B'): Next('q1', 'B', 'R')
                },
                initial_state='q0',
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                self.assertEqual("input_alphabet cannot be None / empty list, and must be all string in list of len = 1", str(e))

        for index in range(3,4):
            try:
                TuringMachine(
                states={'q0', 'q1', 'q2'},
                input_alphabet=not_valid_input_alphabet[index],
                tape_symbols=not_valid_tape_symbols[index],
                transitions={
                    ('q0', '0'): Next('q0', '0', 'R'),
                    ('q0', '1'): Next('q0', '0', 'R'),
                    ('q0', 'B'): Next('q1', 'B', 'R')
                },
                initial_state='q0',
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                self.assertEqual("Input alphabet must be in tape symbols", str(e))
    ###############################################################################################################
    # test Not Valid TM input tape symbols
    def test_TM_Constructor_withInValidTapeSymbols(self):
        not_valid_tape_symbols = [          {}       ,        None            ,    {'0','1'}]
        not_valid_input_alphabet = [{'0', '1'},          {'0', '1'}    , {'1', '2'}]
        for index in range(0,2):

            try: 
                TuringMachine(
                states={'q0', 'q1', 'q2'},
                input_alphabet=not_valid_input_alphabet[index],
                tape_symbols=not_valid_tape_symbols[index],
                transitions={
                    ('q0', '0'): Next('q0', '0', 'R'),
                    ('q0', '1'): Next('q0', '0', 'R'),
                    ('q0', 'B'): Next('q1', 'B', 'R')
                },
                initial_state='q0',
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                self.assertEqual("tape_symbols cannot be None / empty list, and must be all string in list of len = 1", str(e))

        for index in range(2,3):
            try:
                TuringMachine(
                states={'q0', 'q1', 'q2'},
                input_alphabet=not_valid_input_alphabet[index],
                tape_symbols=not_valid_tape_symbols[index],
                transitions={
                    ('q0', '0'): Next('q0', '0', 'R'),
                    ('q0', '1'): Next('q0', '0', 'R'),
                    ('q0', 'B'): Next('q1', 'B', 'R')
                },
                initial_state='q0',
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                self.assertEqual("tape symbols must Must contain the blank symbol 'B'", str(e))
    ###############################################################################################################
    # test Not Valid TM transition
    def test_TM_Constructor_withInValidTransitions(self):
        not_valid_transition = [          {}       ,        None      ]
        for index in range(0,2):
            try: 
                TuringMachine(
                states={'q0', 'q1', 'q2'},
                input_alphabet={'0','1'},
                tape_symbols={'0','1','B'},
                transitions=not_valid_transition[index],
                initial_state='q0',
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                self.assertEqual("transitions cannot be None / empty dict, and must be dict with all string values of key and all string values of Configuration of len > 1", str(e))

        # not valid key[0]
        not_valid_key_0 = ['q5','4','2','']
        for key_0 in not_valid_key_0:
            try:
                TuringMachine(
                states={'q0', 'q1', 'q2'},
                    input_alphabet={'0','1'},
                    tape_symbols={'0','1','B'},
                transitions={
                    (key_0, '0'): Next('q0', '0', 'R'),
                    ('q0', '1'): Next('q0', '0', 'R'),
                    ('q0', 'B'): Next('q1', 'B', 'R')
                },
                initial_state='q0',
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                if key_0 == '':
                    self.assertEqual("transitions cannot be None / empty dict, and must be dict with all string values of key and all string values of Configuration of len > 1", str(e))
                else:
                    self.assertEqual("found error in key value at: ('"+str(key_0)+"', '0') : (q0, 0, R) state must be in states", str(e))
    ###############################################################################################################
    # not valid key[1]
        not_valid_key_1 = ['','5','6','Z']
        for key_1 in not_valid_key_1:
            try:
                TuringMachine(
                states={'q0', 'q1', 'q2'},
                    input_alphabet={'0','1'},
                    tape_symbols={'0','1','B'},
                transitions={
                    ('q0', key_1): Next('q0', '0', 'R'),
                    ('q0', '1'): Next('q0', '0', 'R'),
                    ('q0', 'B'): Next('q1', 'B', 'R')
                },
                initial_state='q0',
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                if key_1 == '':
                    self.assertEqual("transitions cannot be None / empty dict, and must be dict with all string values of key and all string values of Configuration of len > 1", str(e))
                else:
                    self.assertEqual("found error in key value at: ('q0', '"+str(key_1)+"') : (q0, 0, R) symbol must be in tape symbols", str(e))
    ###############################################################################################################
    # not valid value[0]
        not_valid_value_0 = ['','5','q6','Z']
        for value_0 in not_valid_value_0:
            try:
                TuringMachine(
                states={'q0', 'q1', 'q2'},
                    input_alphabet={'0','1'},
                    tape_symbols={'0','1','B'},
                transitions={
                    ('q0', '0'): Next(value_0, '0', 'R'),
                    ('q0', '1'): Next('q0', '0', 'R'),
                    ('q0', 'B'): Next('q1', 'B', 'R')
                },
                initial_state='q0',
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                if value_0 == '':
                    self.assertEqual("transitions cannot be None / empty dict, and must be dict with all string values of key and all string values of Configuration of len > 1", str(e))
                else:
                    self.assertEqual("found error in Configuration value at: ('q0', '0') : ("+str(value_0)+", 0, R) state must be in states", str(e))
    ###############################################################################################################
    # not valid value[1]
        not_valid_value_1 = ['','5','q6','Z']
        for value_1 in not_valid_value_1:
            try:
                TuringMachine(
                states={'q0', 'q1', 'q2'},
                    input_alphabet={'0','1'},
                    tape_symbols={'0','1','B'},
                transitions={
                    ('q0', '0'): Next('q0', value_1, 'R'),
                    ('q0', '1'): Next('q0', '0', 'R'),
                    ('q0', 'B'): Next('q1', 'B', 'R')
                },
                initial_state='q0',
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                if value_1 == '':
                    self.assertEqual("transitions cannot be None / empty dict, and must be dict with all string values of key and all string values of Configuration of len > 1", str(e))
                else: 
                    self.assertEqual("found error in Configuration value at: ('q0', '0') : (q0, "+str(value_1)+", R) symbol must be in tape symbols", str(e))
    ###############################################################################################################
    # not valid value[2]
        not_valid_value_2 = ['','5','q6','Z','B']
        for value_2 in not_valid_value_2:
            try:
                TuringMachine(
                states={'q0', 'q1', 'q2'},
                    input_alphabet={'0','1'},
                    tape_symbols={'0','1','B'},
                transitions={
                    ('q0', '0'): Next('q0', '0', value_2),
                    ('q0', '1'): Next('q0', '0', 'R'),
                    ('q0', 'B'): Next('q1', 'B', 'R')
                },
                initial_state='q0',
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                if value_2 == '':
                    self.assertEqual("transitions cannot be None / empty dict, and must be dict with all string values of key and all string values of Configuration of len > 1", str(e))
                else: 
                    self.assertEqual("found error in Configuration value at: ('q0', '0') : (q0, 0, "+str(value_2)+") action must be 'R' / 'L' / 'S'", str(e))
    ###############################################################################################################
    # test Not Valid TM accept States
    def test_TM_Constructor_withInValidAcceptStates(self):
        not_valid_accept_state = [         {}      ,        None            ,    {'q5'}]
        for index in range(0,2):

            try: 
                TuringMachine(
                states={'q0', 'q1', 'q2'},
                input_alphabet={'0', '1'},
                tape_symbols={'0', '1', 'B'},
                transitions={
                    ('q0', '0'): Next('q0', '0', 'R'),
                    ('q0', '1'): Next('q0', '0', 'R'),
                    ('q0', 'B'): Next('q1', 'B', 'R')
                },
                initial_state='q0',
                accept_states=not_valid_accept_state[index],
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                self.assertEqual("accept_states cannot be None / empty list, and must be all string in list of len > 1", str(e))

        for index in range(2,3):
            try:
                TuringMachine(
                states={'q0', 'q1', 'q2'},
                input_alphabet={'0', '1'},
                tape_symbols={'0', '1', 'B'},
                transitions={
                    ('q0', '0'): Next('q0', '0', 'R'),
                    ('q0', '1'): Next('q0', '0', 'R'),
                    ('q0', 'B'): Next('q1', 'B', 'R')
                },
                initial_state='q0',
                accept_states=not_valid_accept_state[index],
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                self.assertEqual("accept state must be in states", str(e))
    ###############################################################################################################
    # test Not Valid TM reject States
    def test_TM_Constructor_withInValidRejectStates(self):
        not_valid_reject_state = [         {}      ,        None            ,    {'q5'}]
        for index in range(0,2):

            try: 
                TuringMachine(
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
                reject_states=not_valid_reject_state[index]
                )
                self.fail("should throw exception")
            except Exception as e:
                self.assertEqual("reject_states cannot be None / empty list, and must be all string in list of len > 1", str(e))

        for index in range(2,3):
            try:
                TuringMachine(
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
                reject_states=not_valid_reject_state[index]
                )
                self.fail("should throw exception")
            except Exception as e:
                self.assertEqual("reject state must be in states", str(e))
    ###############################################################################################################

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ###############################################################################################################
    #test Valid TM run with valid input
    def test_TM_Run_withValidTuringMachineInput(self):
        try:
            result = TuringMachine(
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
            result.run("001")
        except Exception as e:
            self.fail("TuringMachine() raised Exception: "+str(e)+", with valid TuringMachine and valid input unexpectedly!")
    ###############################################################################################################
    #test Valid TM run with valid input
    def test_TM_Run_withValidEmptyStringTuringMachineInput(self):
        try:
            result = TuringMachine(
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
            result.run("")
        except Exception as e:
            self.fail("TuringMachine() raised Exception: "+str(e)+", with valid TuringMachine and valid input unexpectedly!")
    ###############################################################################################################
    #test Valid TM run with not valid input
    def test_TM_Run_withInValidTuringMachineInput(self):
        try:
            result = TuringMachine(
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
            result.run(None)
        except Exception as e:
            self.assertEqual("Input String cannot be None or not str object or list of chars",str(e))
    ###############################################################################################################
    #test Valid TM run with not valid input
    def test_TM_Run_withInValid2TuringMachineInput(self):
        try:
            result = TuringMachine(
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
            result.run("2222")
        except Exception as e:
            self.assertEqual("rejected input, input string contains char not from the alphabet.",str(e))
    ###############################################################################################################
    
    


if __name__ == '__main__':
    unittest.main()