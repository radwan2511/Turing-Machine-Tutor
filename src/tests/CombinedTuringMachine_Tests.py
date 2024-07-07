import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.CombinedTuringMachine import CombinedTuringMachine
from turing_machine_tutor.machine_run_state import Machine_Run_State
from turing_machine_tutor.Next import Next

import unittest
# Purpose: Verify that individual units of code (functions, methods, or classes) work as intended.


class TestCombinedTuringMachine(unittest.TestCase):
    # test Combined TM add function
    def test_CombinedTuringMachine_Add_WithNotValid1TM(self):
        notValid_list = [None, "", [], 5, 'asd']
        for n_v in notValid_list:
            try:
                result = CombinedTuringMachine({'0', '1'})
                result.add("test", n_v)
            except Exception as e:
                if n_v == None:
                    self.assertEqual("TM cannot be None", str(e))
                else:
                    self.assertEqual("TM cannot be Not Turing Machine Object", str(e))
    ###############################################################################################################
    # test Combined TM add function
    def test_CombinedTuringMachine_Add_WithNotValid2TM(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        notValid_list = [None, "", '']
        for n_v in notValid_list:
            try:
                result = CombinedTuringMachine({'0', '1'})
                result.add(n_v, step1)
            except Exception as e:
                self.assertEqual("Name cannot be None", str(e))
    ###############################################################################################################
    # test Combined TM add function
    def test_CombinedTuringMachine_Add_WithNotValid3TM(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        notValid_list = [5, [55], {5}]
        for n_v in notValid_list:
            try:
                result = CombinedTuringMachine({'0', '1'})
                result.add(n_v, step1)
            except Exception as e:
                self.assertEqual("Name cannot be not str object", str(e))
    ###############################################################################################################
    # test Combined TM add function
    def test_CombinedTuringMachine_Add_WithNotValid4TM(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        notValid_list = ["add1", "add1"]
        for n_v in notValid_list:
            try:
                result = CombinedTuringMachine({'0', '1'})
                result.add(n_v, step1)
            except Exception as e:
                self.assertEqual("Turing machine with this name already exists in the list", str(e))
    ###############################################################################################################
    # test Combined TM set while condition function
    def test_CombinedTuringMachine_SetWhileCondition_WithNotValid1TM(self):
        notValid_list = [None, "", [], 5, 'asd']
        for n_v in notValid_list:
            try:
                result = CombinedTuringMachine({'0', '1'})
                result.setTuringMachineWhileCondition("test", n_v)
            except Exception as e:
                if n_v == None:
                    self.assertEqual("While TM cannot be None", str(e))
                else:
                    self.assertEqual("While TM cannot be Not Turing Machine Object", str(e))
    ###############################################################################################################
                    

    # test Combined TM set while condition function
    def test_CombinedTuringMachine_SetWhileCondition_WithNotValid2TM(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        notValid_list = [None, "", '']
        for n_v in notValid_list:
            try:
                result = CombinedTuringMachine({'0', '1'})
                result.setTuringMachineWhileCondition(n_v, step1)
            except Exception as e:
                self.assertEqual("Name cannot be None", str(e))
    ###############################################################################################################
    # test Combined TM set while condition function
    def test_CombinedTuringMachine_SetWhileCondition_WithNotValid3TM(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        notValid_list = [5, [55], {5}]
        for n_v in notValid_list:
            try:
                result = CombinedTuringMachine({'0', '1'})
                result.setTuringMachineWhileCondition(n_v, step1)
            except Exception as e:
                self.assertEqual("Name cannot be not str object", str(e))
    ###############################################################################################################
    



    # test Combined TM remove function
    def test_CombinedTuringMachine_Remove_WithNotValid1TM(self):
        notValid_list = [None, ""]
        for n_v in notValid_list:
            try:
                result = CombinedTuringMachine({'0', '1'})
                result.remove(n_v)
            except Exception as e:
                self.assertEqual("Name cannot be None", str(e))
    ###############################################################################################################
    # test Combined TM remove function
    def test_CombinedTuringMachine_Remove_WithNotValid2TM(self):
        notValid_list = [5, [5], {"55"}]
        for n_v in notValid_list:
            try:
                result = CombinedTuringMachine({'0', '1'})
                result.remove(n_v)
            except Exception as e:
                self.assertEqual("Name cannot be not str object", str(e))
    ###############################################################################################################
    # test Combined TM remove function
    def test_CombinedTuringMachine_Remove_WithNotValid3TM(self):
        notValid_list = ["test1", "test2", "a"]
        for n_v in notValid_list:
            try:
                result = CombinedTuringMachine({'0', '1'})
                result.remove(n_v)
            except Exception as e:
                self.assertEqual("Turing machine with this name doesn't exists in the list", str(e))
    ###############################################################################################################
    # test Combined TM remove function
    def test_CombinedTuringMachine_Remove_ValidTM(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        Valid_list = ["test1"]
        for v in Valid_list:
            try:
                result = CombinedTuringMachine({'0', '1'})
                result.add(v,step1)
                result.remove(v)
            except Exception as e:
                self.fail("remove should succeded, shouldn't throw exception")
    
    ###############################################################################################################
    # test Combined TM run function without while condition
    def test_CombinedTuringMachine_Run_Valid1TM(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        step2 = TuringMachine(
        states={'q0', 'q1', 'q2', 'q3'},
        input_alphabet={'0', '1', 'X', 'Y', 'B'},
        tape_symbols={'0', '1', 'X', 'Y', 'B'},
        transitions={
            ('q0', '0'): Next('q0', '0', 'R'),  # Step 2 move right to the first 1
            ('q0', '1'): Next('q2', '1', 'S'),  # if you do not find symbol 1, reject the language
            ('q0', 'X'): Next('q0', 'X', 'R'),
            ('q0', 'Y'): Next('q0', 'Y', 'R'),
            ('q0', 'B'): Next('q3', 'B', 'S')
        },
        initial_state='q0',
        accept_states={'q2'},
        reject_states={'q3'}
    )

        step3 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q3', '0', 'S'),  # Step 3 change 1 to Y
                ('q0', '1'): Next('q2', 'Y', 'L'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )

        step4 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q0', '0', 'L'),  # Step 4 Move Left to Leftmost 0
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q2', 'X', 'R'),
                ('q0', 'Y'): Next('q0', 'Y', 'L'),
                ('q0', 'B'): Next('q3', 'B', 'R')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        combined_tm = CombinedTuringMachine({'0', '1'})
        combined_tm.add('Change 0 to X', step1)
        combined_tm.add('Move Right To First 1', step2)
        combined_tm.add('Change 1 to Y', step3)
        combined_tm.add('Move Left to Leftmost 0', step4)
        result = combined_tm.run("0011")
        result = ''.join(result.tape)
        result = result.replace('B','')
        self.assertEqual(result, "X0Y1")
    ###############################################################################################################
    # test Combined TM run function with while condition
    def test_CombinedTuringMachine_Run_Valid2TM(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        step2 = TuringMachine(
        states={'q0', 'q1', 'q2', 'q3'},
        input_alphabet={'0', '1', 'X', 'Y', 'B'},
        tape_symbols={'0', '1', 'X', 'Y', 'B'},
        transitions={
            ('q0', '0'): Next('q0', '0', 'R'),  # Step 2 move right to the first 1
            ('q0', '1'): Next('q2', '1', 'S'),  # if you do not find symbol 1, reject the language
            ('q0', 'X'): Next('q0', 'X', 'R'),
            ('q0', 'Y'): Next('q0', 'Y', 'R'),
            ('q0', 'B'): Next('q3', 'B', 'S')
        },
        initial_state='q0',
        accept_states={'q2'},
        reject_states={'q3'}
    )

        step3 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q3', '0', 'S'),  # Step 3 change 1 to Y
                ('q0', '1'): Next('q2', 'Y', 'L'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )

        step4 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q0', '0', 'L'),  # Step 4 Move Left to Leftmost 0
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q2', 'X', 'R'),
                ('q0', 'Y'): Next('q0', 'Y', 'L'),
                ('q0', 'B'): Next('q3', 'B', 'R')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )

        #step 5 repeat steps number 01 to 04 until no more 0 and 1 remain in the input tape
        step5 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q2', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
                ('q0', '1'): Next('q2', '1', 'S'),
                ('q0', 'X'): Next('q0', 'X', 'R'),
                ('q0', 'Y'): Next('q0', 'Y', 'R'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        step6 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q3', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q0', 'X', 'R'),
                ('q0', 'Y'): Next('q0', 'Y', 'R'),
                ('q0', 'B'): Next('q2', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )

        combined_tm = CombinedTuringMachine({'0', '1'})
        combined_tm.add('Change 0 to X', step1)
        combined_tm.add('Move Right To First 1', step2)
        combined_tm.add('Change 1 to Y', step3)
        combined_tm.add('Move Left to Leftmost 0', step4)
        combined_tm.setTuringMachineWhileCondition("0 or 1 in tape", step5)
        result = combined_tm.run("0011")
        result = ''.join(result.tape)
        result = result.replace('B','')
        self.assertEqual(result, "XXYY")
    ###############################################################################################################
    # test Combined TM run function with not valid input
    def test_CombinedTuringMachine_Run_NotValid1TMInput(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        step2 = TuringMachine(
        states={'q0', 'q1', 'q2', 'q3'},
        input_alphabet={'0', '1', 'X', 'Y', 'B'},
        tape_symbols={'0', '1', 'X', 'Y', 'B'},
        transitions={
            ('q0', '0'): Next('q0', '0', 'R'),  # Step 2 move right to the first 1
            ('q0', '1'): Next('q2', '1', 'S'),  # if you do not find symbol 1, reject the language
            ('q0', 'X'): Next('q0', 'X', 'R'),
            ('q0', 'Y'): Next('q0', 'Y', 'R'),
            ('q0', 'B'): Next('q3', 'B', 'S')
        },
        initial_state='q0',
        accept_states={'q2'},
        reject_states={'q3'}
    )

        step3 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q3', '0', 'S'),  # Step 3 change 1 to Y
                ('q0', '1'): Next('q2', 'Y', 'L'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )

        step4 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q0', '0', 'L'),  # Step 4 Move Left to Leftmost 0
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q2', 'X', 'R'),
                ('q0', 'Y'): Next('q0', 'Y', 'L'),
                ('q0', 'B'): Next('q3', 'B', 'R')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )

        #step 5 repeat steps number 01 to 04 until no more 0 and 1 remain in the input tape
        step5 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q2', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
                ('q0', '1'): Next('q2', '1', 'S'),
                ('q0', 'X'): Next('q0', 'X', 'R'),
                ('q0', 'Y'): Next('q0', 'Y', 'R'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        step6 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q3', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q0', 'X', 'R'),
                ('q0', 'Y'): Next('q0', 'Y', 'R'),
                ('q0', 'B'): Next('q2', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )

        combined_tm = CombinedTuringMachine({'0', '1'})
        combined_tm.add('Change 0 to X', step1)
        combined_tm.add('Move Right To First 1', step2)
        combined_tm.add('Change 1 to Y', step3)
        combined_tm.add('Move Left to Leftmost 0', step4)
        combined_tm.setTuringMachineWhileCondition("0 or 1 in tape", step5)
        not_valid_list = [None, 5, [5], {5}, ["55", "5"]]
        for n_v in not_valid_list:
            try:
                result = combined_tm.run(n_v)
            except Exception as e:
                self.assertEqual("Input String cannot be None or not str object or list of chars",str(e))
    ###############################################################################################################
    # test Combined TM run function with not valid input
    def test_CombinedTuringMachine_Run_NotValid2TMInput(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        step2 = TuringMachine(
        states={'q0', 'q1', 'q2', 'q3'},
        input_alphabet={'0', '1', 'X', 'Y', 'B'},
        tape_symbols={'0', '1', 'X', 'Y', 'B'},
        transitions={
            ('q0', '0'): Next('q0', '0', 'R'),  # Step 2 move right to the first 1
            ('q0', '1'): Next('q2', '1', 'S'),  # if you do not find symbol 1, reject the language
            ('q0', 'X'): Next('q0', 'X', 'R'),
            ('q0', 'Y'): Next('q0', 'Y', 'R'),
            ('q0', 'B'): Next('q3', 'B', 'S')
        },
        initial_state='q0',
        accept_states={'q2'},
        reject_states={'q3'}
    )

        step3 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q3', '0', 'S'),  # Step 3 change 1 to Y
                ('q0', '1'): Next('q2', 'Y', 'L'),
                ('q0', 'X'): Next('q3', 'X', 'S'),
                ('q0', 'Y'): Next('q3', 'Y', 'S'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )

        step4 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q0', '0', 'L'),  # Step 4 Move Left to Leftmost 0
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q2', 'X', 'R'),
                ('q0', 'Y'): Next('q0', 'Y', 'L'),
                ('q0', 'B'): Next('q3', 'B', 'R')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )

        #step 5 repeat steps number 01 to 04 until no more 0 and 1 remain in the input tape
        step5 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q2', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
                ('q0', '1'): Next('q2', '1', 'S'),
                ('q0', 'X'): Next('q0', 'X', 'R'),
                ('q0', 'Y'): Next('q0', 'Y', 'R'),
                ('q0', 'B'): Next('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        step6 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Next('q3', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
                ('q0', '1'): Next('q3', '1', 'S'),
                ('q0', 'X'): Next('q0', 'X', 'R'),
                ('q0', 'Y'): Next('q0', 'Y', 'R'),
                ('q0', 'B'): Next('q2', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )

        combined_tm = CombinedTuringMachine({'0', '1'})
        combined_tm.add('Change 0 to X', step1)
        combined_tm.add('Move Right To First 1', step2)
        combined_tm.add('Change 1 to Y', step3)
        combined_tm.add('Move Left to Leftmost 0', step4)
        combined_tm.setTuringMachineWhileCondition("0 or 1 in tape", step5)
        not_valid_list = ["2", "424", ['5','5','5']]
        for n_v in not_valid_list:
            try:
                result = combined_tm.run(n_v)
            except Exception as e:
                self.assertEqual("rejected input, input string contains char not from the alphabet.",str(e))
    ###############################################################################################################
    


if __name__ == '__main__':
    unittest.main()
