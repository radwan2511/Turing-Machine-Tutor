import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest


# Purpose: Verify that individual units of code (functions, methods, or classes) work as intended.
from turing_machine_tutor.IFTuringMachine import IFTuringMachine
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.TuringMachineVisualizer import TuringMachineVisualizer
from turing_machine_tutor.Next import Next
from turing_machine_tutor.machine_run_state import Machine_Run_State
from turing_machine_tutor.CombinedTuringMachine import CombinedTuringMachine


class TuringMachineVisualizer_Tests(unittest.TestCase):
    # test execute_config function
    def test_run_and_visualize_regular_machine(self):
        simple_turing_machine = TuringMachine(   #this machine converts first encountered 0 to 1
            states={'q0', 'q1', 'q2'},
            input_alphabet={'0', '1'},
            tape_symbols={'0', '1', 'B'},
            transitions={
                ('q0', '0'): Next('q1', '1', 'R'),  # if encountered 0 put 1 and move right
                ('q0', '1'): Next('q0', '1', 'R'),  # if encountered 1 just move right
                ('q0', 'B'): Next('q1', 'B', 'S'),  # if encountered 1 just move right
                ('q1', '0'): Next('q1', '0', 'S'),  # after reaching q1 don't do anything
                ('q1', '1'): Next('q1', '1', 'S'),  # after reaching q1 don't do anything
                ('q1', 'B'): Next('q1', 'B', 'S'),  # after reaching q1 don't do anything
            },
            initial_state='q0',
            accept_states={'q1'},
            reject_states={'q2'}
        )
        visualizer = TuringMachineVisualizer(simple_turing_machine)
        steps = visualizer.run_and_visualize("01", 5000)
        self.assertEquals(steps[0].tape,["0","1"])
        self.assertEquals(steps[0].head_position, 0)
        self.assertEquals(steps[0].state, "q0")
        self.assertEquals(steps[1].tape, ["1", "1"])
        self.assertEquals(steps[1].head_position, 1)
        self.assertEquals(steps[1].state, "q1")
        self.assertEquals(steps[2].tape, ["1", "1"])
        self.assertEquals(steps[2].head_position, 1)
        self.assertEquals(steps[2].state, "q1")
        self.assertEquals(steps[3], "reached accept state")

    def test_run_and_visualize_combined_machine(self):
        simple_turing_machine_1 = TuringMachine(  # this machine converts first encountered 0 to 1
            states={'q0', 'q1', 'q2'},
            input_alphabet={'0', '1'},
            tape_symbols={'0', '1', 'B'},
            transitions={
                ('q0', '0'): Next('q1', '1', 'R'),  # if encountered 0 put 1 and move right
                ('q0', '1'): Next('q0', '1', 'R'),  # if encountered 1 just move right
                ('q0', 'B'): Next('q1', 'B', 'S'),  # if encountered 1 just move right
                ('q1', '0'): Next('q1', '0', 'S'),  # after reaching q1 don't do anything
                ('q1', '1'): Next('q1', '1', 'S'),  # after reaching q1 don't do anything
                ('q1', 'B'): Next('q1', 'B', 'S'),  # after reaching q1 don't do anything
            },
            initial_state='q0',
            accept_states={'q1'},
            reject_states={'q2'}
        )
        simple_turing_machine_2 = TuringMachine(# this machine converts first encountered 1 to 0
            states={'q0', 'q1', 'q2'},
            input_alphabet={'0', '1'},
            tape_symbols={'0', '1', 'B'},
            transitions={
                ('q0', '0'): Next('q0', '0', 'R'),  # if encountered 0 just move right
                ('q0', '1'): Next('q1', '0', 'R'),  # if encountered 1 put 0 and move right
                ('q0', 'B'): Next('q1', 'B', 'S'),
                ('q1', '0'): Next('q1', '0', 'S'),  # after reaching q1 don't do anything
                ('q1', '1'): Next('q1', '1', 'S'),  # after reaching q1 don't do anything
                ('q1', 'B'): Next('q1', 'B', 'S'),  # after reaching q1 don't do anything

            },
            initial_state='q0',
            accept_states={'q1'},
            reject_states={'q2'}
        )
        combined_tm = CombinedTuringMachine({'0', '1'})
        combined_tm.add("step1", simple_turing_machine_1)
        combined_tm.add("step2", simple_turing_machine_2)
        visualizer = TuringMachineVisualizer(combined_tm)
        steps = visualizer.run_and_visualize("01", 5000)
        self.assertEquals(steps[1].tape, ["0", "1"])
        self.assertEquals(steps[1].head_position, 0)
        self.assertEquals(steps[1].state, "q0")

        self.assertEquals(steps[2].tape, ["1", "1"])
        self.assertEquals(steps[2].head_position, 1)
        self.assertEquals(steps[2].state, "q1")

        # self.assertEquals(steps[3].tape, [])
        # self.assertEquals(steps[3].head_position, 0)
        # self.assertEquals(steps[3].state, "q0")

        self.assertEquals(steps[3], "reached accept state")

        self.assertEquals(steps[5].tape, ["1", "1"])
        self.assertEquals(steps[5].head_position, 1)
        self.assertEquals(steps[5].state, "q0")

        self.assertEquals(steps[6].tape, ["1", "0","B"])
        self.assertEquals(steps[6].head_position, 2)
        self.assertEquals(steps[6].state, "q1")

        # self.assertEquals(steps[8].tape, [])
        # self.assertEquals(steps[8].head_position, 0)
        # self.assertEquals(steps[8].state, "q0")

        self.assertEquals(steps[7], "reached accept state")

    def test_run_and_visualize_while_condition_machine(self):
        self.assertEquals(1,1)

    def test_run_and_visualize_if_condition_enters_then(self):
        ifcond_machine = TuringMachine(  ## if first letter is 1
            states={'q0', 'q1', 'q2'},
            input_alphabet={'0', '1'},
            tape_symbols={'0', '1', 'B'},
            transitions={
                ('q0', '0'): Next('q2', '0', 'S'),
                ('q0', '1'): Next('q1', '1', 'R'),
                ('q0', 'B'): Next('q2', 'B', 'S'),

            },
            initial_state='q0',
            accept_states={'q1'},
            reject_states={'q2'}
        )
        simple_turing_machine_1 = TuringMachine(  # this machine converts first encountered 0 to 1
            states={'q0', 'q1', 'q2'},
            input_alphabet={'0', '1'},
            tape_symbols={'0', '1', 'B'},
            transitions={
                ('q0', '0'): Next('q1', '1', 'R'),  # if encountered 0 put 1 and move right
                ('q0', '1'): Next('q0', '1', 'R'),  # if encountered 1 just move right
                ('q0', 'B'): Next('q1', 'B', 'S'),  # if encountered 1 just move right
                ('q1', '0'): Next('q1', '0', 'S'),  # after reaching q1 don't do anything
                ('q1', '1'): Next('q1', '1', 'S'),  # after reaching q1 don't do anything
                ('q1', 'B'): Next('q1', 'B', 'S'),  # after reaching q1 don't do anything
            },
            initial_state='q0',
            accept_states={'q1'},
            reject_states={'q2'}
        )
        simple_turing_machine_2 = TuringMachine(  # this machine converts first encountered 1 to 0
            states={'q0', 'q1', 'q2'},
            input_alphabet={'0', '1'},
            tape_symbols={'0', '1', 'B'},
            transitions={
                ('q0', '0'): Next('q0', '0', 'R'),  # if encountered 0 just move right
                ('q0', '1'): Next('q1', '0', 'R'),  # if encountered 1 put 0 and move right
                ('q0', 'B'): Next('q1', 'B', 'S'),
                ('q1', '0'): Next('q1', '0', 'S'),  # after reaching q1 don't do anything
                ('q1', '1'): Next('q1', '1', 'S'),  # after reaching q1 don't do anything
                ('q1', 'B'): Next('q1', 'B', 'S'),  # after reaching q1 don't do anything

            },
            initial_state='q0',
            accept_states={'q1'},
            reject_states={'q2'}
        )
        if_machine = IFTuringMachine("idcond", ifcond_machine, "convert_0_to_1", simple_turing_machine_1, "convert_1_to_0", simple_turing_machine_2)  # if first letter is 1 then convert first 0 to 1 else convert first 1 to 0
        # if_machine.setIfTM(ifcond_machine, "ifcond")
        # if_machine.setThenTM(simple_turing_machine_1, "convert_0_to_1")
        # if_machine.setElseTM(simple_turing_machine_2, "convert_1_to_0")
        visualizer = TuringMachineVisualizer(if_machine)
        steps = visualizer.run_and_visualize("01", 5000)
        print(steps)
        self.assertEquals(steps[1].tape, ["0", "1"])
        self.assertEquals(steps[1].head_position, 0)
        self.assertEquals(steps[1].state, "q0")

        self.assertEquals(steps[2].tape, ["0", "1"])
        self.assertEquals(steps[2].head_position, 0)
        self.assertEquals(steps[2].state, "q2")

        self.assertEquals(steps[3].tape, ["0", "1"])
        self.assertEquals(steps[3].head_position, 0)
        self.assertEquals(steps[3].state, "q2")

        self.assertEquals(steps[4], "reached reject state")

        self.assertEquals(steps[6].tape, ["0", "1"])
        self.assertEquals(steps[6].head_position, 0)
        self.assertEquals(steps[6].state, "q0")

        self.assertEquals(steps[7].tape, ["0", "1"])
        self.assertEquals(steps[7].head_position, 1)
        self.assertEquals(steps[7].state, "q0")


        self.assertEquals(steps[8].tape, ["0", "0","B"])
        self.assertEquals(steps[8].head_position, 2)
        self.assertEquals(steps[8].state, "q1")

        self.assertEquals(steps[9].tape, ["0", "0", "B"])
        self.assertEquals(steps[9].head_position, 2)
        self.assertEquals(steps[9].state, "q1")

        self.assertEquals(steps[10], "reached accept state")

        def test_run_and_visualize_if_condition_enters_else(self):
            if_machine = IFTuringMachine()  # if first letter is 1 then convert first 0 to 1 else convert first 1 to 0
            ifcond_machine = TuringMachine(  ## if first letter is 1
                states={'q0', 'q1', 'q2'},
                input_alphabet={'0', '1'},
                tape_symbols={'0', '1', 'B'},
                transitions={
                    ('q0', '0'): Next('q2', '0', 'S'),
                    ('q0', '1'): Next('q1', '1', 'R'),
                    ('q0', 'B'): Next('q2', 'B', 'S'),

                },
                initial_state='q0',
                accept_states={'q1'},
                reject_states={'q2'}
            )
            simple_turing_machine_1 = TuringMachine(  # this machine converts first encountered 0 to 1
                states={'q0', 'q1', 'q2'},
                input_alphabet={'0', '1'},
                tape_symbols={'0', '1', 'B'},
                transitions={
                    ('q0', '0'): Next('q1', '1', 'R'),  # if encountered 0 put 1 and move right
                    ('q0', '1'): Next('q0', '1', 'R'),  # if encountered 1 just move right
                    ('q0', 'B'): Next('q1', 'B', 'S'),  # if encountered 1 just move right
                    ('q1', '0'): Next('q1', '0', 'S'),  # after reaching q1 don't do anything
                    ('q1', '1'): Next('q1', '1', 'S'),  # after reaching q1 don't do anything
                    ('q1', 'B'): Next('q1', 'B', 'S'),  # after reaching q1 don't do anything
                },
                initial_state='q0',
                accept_states={'q1'},
                reject_states={'q2'}
            )
            simple_turing_machine_2 = TuringMachine(  # this machine converts first encountered 1 to 0
                states={'q0', 'q1', 'q2'},
                input_alphabet={'0', '1'},
                tape_symbols={'0', '1', 'B'},
                transitions={
                    ('q0', '0'): Next('q0', '0', 'R'),  # if encountered 0 just move right
                    ('q0', '1'): Next('q1', '0', 'R'),  # if encountered 1 put 0 and move right
                    ('q0', 'B'): Next('q1', 'B', 'S'),
                    ('q1', '0'): Next('q1', '0', 'S'),  # after reaching q1 don't do anything
                    ('q1', '1'): Next('q1', '1', 'S'),  # after reaching q1 don't do anything
                    ('q1', 'B'): Next('q1', 'B', 'S'),  # after reaching q1 don't do anything

                },
                initial_state='q0',
                accept_states={'q1'},
                reject_states={'q2'}
            )
            if_machine.setIfTM(ifcond_machine, "ifcond")
            if_machine.setThenTM(simple_turing_machine_1, "convert_0_to_1")
            if_machine.setElseTM(simple_turing_machine_2, "convert_1_to_0")
            visualizer = TuringMachineVisualizer(if_machine)
            steps = visualizer.run_and_visualize("10", 5000)

            self.assertEquals(steps[0].tape, ["1", "0"])
            self.assertEquals(steps[0].head_position, 0)
            self.assertEquals(steps[0].state, "q0")

            self.assertEquals(steps[1].tape, ["1", "0"])
            self.assertEquals(steps[1].head_position, 1)
            self.assertEquals(steps[1].state, "q1")

            self.assertEquals(steps[2].tape, ["1", "0"])
            self.assertEquals(steps[2].head_position, 1)
            self.assertEquals(steps[2].state, "q1")

            self.assertEquals(steps[3], "reached accept state")

            self.assertEquals(steps[4].tape, ["1", "0"])
            self.assertEquals(steps[4].head_position, 0)
            self.assertEquals(steps[4].state, "q0")

            self.assertEquals(steps[5].tape, ["1", "0"])
            self.assertEquals(steps[5].head_position, 1)
            self.assertEquals(steps[5].state, "q0")

            self.assertEquals(steps[6].tape, ["1", "1", "B"])
            self.assertEquals(steps[6].head_position, 2)
            self.assertEquals(steps[6].state, "q1")

            self.assertEquals(steps[7].tape, ["1", "1", "B"])
            self.assertEquals(steps[7].head_position, 2)
            self.assertEquals(steps[7].state, "q1")

            self.assertEquals(steps[8], "reached accept state")

if __name__ == '__main__':
    unittest.main()