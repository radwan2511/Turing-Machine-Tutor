import matplotlib.pyplot as plt
from IPython.display import clear_output
import time
import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.machine_run_state import Machine_Run_State
from turing_machine_tutor.MultiNext import MultiNext
from turing_machine_tutor.Call_Turing_Machine import Call_Turing_Machine

class MultiTapeTuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, transition_function, start_state, accept_state, reject_state, num_tapes=2):
        self.tms_dic = {}
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.num_tapes = num_tapes
        self.tapes = [['B']] * num_tapes
        self.head_positions = [0] * num_tapes
        self.current_state = start_state
        self.name = ""
        self.validate()
        self.flag = None
        

    def validate(self):
        # Check that start, accept, and reject states are in the set of states
        assert self.start_state in self.states, "Start state must be in the set of states"
        for x in self.accept_state:
            assert x in self.states, "Accept state must be in the set of states"
        #assert self.accept_state in self.states, "Accept state must be in the set of states"
        for x in self.reject_state:
            assert x in self.states, "Reject state must be in the set of states"
        #assert self.reject_state in self.states, "Reject state must be in the set of states"

        # Check that the input alphabet is a subset of the tape alphabet
        assert self.input_alphabet.issubset(self.tape_alphabet), "Input alphabet must be a subset of the tape alphabet"

        # Check that the transition function has valid states and symbols
        for state_symbols, transition in self.transition_function.items():
            if isinstance(transition, MultiNext):
                current_state = state_symbols[0]
                current_symbols = state_symbols[1:]
                new_state = transition[0]
                new_symbols = transition[1:self.num_tapes+1]
                directions = transition[self.num_tapes+1:]
                
                assert len(state_symbols)-1 == self.num_tapes, "Please check num_tapes if it matches the number of variables on a simple key in transitions."

                assert current_state in self.states, f"State {current_state} is not in the set of states"
                assert new_state in self.states, f"State {new_state} is not in the set of states"
                assert all(symbol in self.tape_alphabet for symbol in current_symbols), "Transition symbols must be in the tape alphabet"
                assert all(symbol in self.tape_alphabet for symbol in new_symbols), "New symbols must be in the tape alphabet"
                assert len(directions) == self.num_tapes, "There must be a direction for each tape"
                assert all(direction in ['L', 'R', 'S'] for direction in directions), "Directions must be 'L', 'R', or 'N'"
            elif isinstance(transition, Call_Turing_Machine):
                current_state = state_symbols[0]
                current_symbols = state_symbols[1:]
                assert current_state in self.states, f"State {current_state} is not in the set of states"
                assert all(symbol in self.tape_alphabet for symbol in current_symbols), "Transition symbols must be in the tape alphabet"

                #assert len(transition) == 4, "Call_Turing_Machine should pass 4 values: TM_name,list_of_tapes_indexes,call_state,return_state"
                TM_name = transition.TM_name
                assert isinstance(TM_name, str), "TM_name should be a string"
                assert TM_name.strip() != "", "TM_name should not be an empty string"

                assert isinstance(transition.tm,MultiTapeTuringMachine), "turing machine should be MultiTapeTuringMachine object"
                tm = transition.tm
                list_of_tapes_indexes = transition.list_of_tapes_indexes
                assert isinstance(list_of_tapes_indexes, list), "list_of_tapes_indexes should be a list"
                assert all(isinstance(index, int) for index in list_of_tapes_indexes), "All items in list_of_tapes_indexes should be integers"
                assert len(list_of_tapes_indexes) > 0, "list_of_tapes_indexes should not be empty"
                assert len(list_of_tapes_indexes) <= self.num_tapes, "list_of_tapes_indexes should be smaller or equal to num tapes of this TM"
                assert len(list_of_tapes_indexes) <= tm.num_tapes, "list_of_tapes_indexes should be smaller or equla to num tapes of the called TM"

                # call_state = transition[2]
                # assert call_state in self.states, "Call state must be in the set of states"
                return_state = transition.return_state_acc
                assert return_state in self.states, "accepted return state must be in the set of states"
                return_state = transition.return_state_rej
                assert return_state in self.states, "rejected return state must be in the set of states"
                tm.name = TM_name
                self.tms_dic[TM_name] = tm
            else:
                raise Exception("All Transition values should be MultiNext/Call_Turing_Machine objects")
            

    def initialize_tapes(self, inputs, flag=None):
        if (inputs == '' or inputs == ['']):
            if(inputs == ''):
                inputs = ['']
            pass
        elif(isinstance(inputs, str)):
            for char in inputs:
                assert char in self.input_alphabet, f"Character '{char}' in string '{item}' is not in the input alphabet"
            new_inputs = [inputs]
            for i in range(1,self.num_tapes):
                new_inputs.append('')
            inputs = new_inputs
        else:
            assert isinstance(inputs, list), "Inputs is not a list"
            if(isinstance(inputs[0], list)):
                new_inputs = []
                for x in inputs:
                    st = ""
                    for y in x:
                        st += y
                    new_inputs.append(st)
                inputs = new_inputs
            # Check if the list has a minimum length of 1
            assert len(inputs) >= 1, "List length is less than 1"
            assert len(inputs) <= self.num_tapes, "inputs number should be smaller or equal to num_tapes"
            # Check if all elements in the list are strings
            assert all(isinstance(item, str) for item in inputs), "Not all elements in the list are strings"
            for item in inputs:
                for char in item:
                    assert char in self.input_alphabet, f"Character '{char}' in string '{item}' is not in the input alphabet"

        self.current_state = self.start_state

        
        for i in range(len(inputs), self.num_tapes):
            inputs.append('')
        
        for i in range(self.num_tapes):
            self.tapes[i] = list(inputs[i]) + ['B']
            if flag == None or len(self.tapes[i])==1:
                self.head_positions[i] = 0

    def step(self):
        symbols = tuple(self.tapes[i][self.head_positions[i]] for i in range(self.num_tapes))
        state_symbols = (self.current_state,) + symbols

        if state_symbols in self.transition_function:
            transition = self.transition_function[state_symbols]
            if (isinstance(transition, MultiNext)):
                new_state = transition[0]
                new_symbols = transition[1:self.num_tapes+1]
                directions = transition[self.num_tapes+1:]
                self.current_state = new_state
                for i in range(self.num_tapes):
                    self.tapes[i][self.head_positions[i]] = new_symbols[i]
                    if directions[i] == 'R':
                        self.head_positions[i] += 1
                    elif directions[i] == 'L':
                        self.head_positions[i] -= 1
                    if self.head_positions[i] < 0:
                        #self.tapes[i].insert(0, 'B') # turing machine is infinte only on the right side
                        self.head_positions[i] = 0
                    if self.head_positions[i] >= len(self.tapes[i]):
                        self.tapes[i].append('B')
            elif(isinstance(transition, Call_Turing_Machine)):
                tm = self.tms_dic[transition.TM_name]
                assert isinstance(tm,MultiTapeTuringMachine), "all tms in transition should be MultiTapeTurinMachines"
                tapes_edit = []
                index = 0
                for i in transition.list_of_tapes_indexes:
                    num_b_before_index = 0
                    for x in self.tapes[i]:
                        if(x != 'B'):
                            break
                        num_b_before_index += 1
                    tapes_edit.append(self.tapes[i][num_b_before_index:])
                    tm.head_positions[index] = self.head_positions[i] - num_b_before_index
                    if tm.head_positions[index]<0:
                        tm.head_positions[index] = 0
                    index += 1
                def remove_B_from_list(char_list2):
                    res = []
                    for char_list in char_list2:
                        s = [char for char in char_list if char != 'B']
                        res.append(s)
                    return res
                tapes_edit2 = remove_B_from_list(tapes_edit)

                savedHeadPos = tm.head_positions[:]

                tm.run(tapes_edit2,True)
                index = 0
                for i in transition.list_of_tapes_indexes:
                    num_b_before_index = 0
                    for x in tm.tapes[index]:
                        if(x != 'B'):
                            break
                        num_b_before_index += 1
                    
                    tm.tapes[index] = tm.tapes[index][num_b_before_index:]
                    tm.head_positions[index] = tm.head_positions[index] - num_b_before_index

                    self.tapes[i] = tm.tapes[index]
                    self.head_positions[i] = tm.head_positions[index]
                    index += 1
                if tm.given_state_is_in_acceptance(tm.current_state):
                    self.current_state = transition.return_state_acc
                else:
                    self.current_state = transition.return_state_rej
                return True, transition.TM_name , tm , tapes_edit2, transition.list_of_tapes_indexes, savedHeadPos
        else:
            if(state_symbols[0] in self.accept_state):
                return True , 0,0,0,0
            print("no transition key found for the currenct state, multi tape TM halted.")
            return False,0,0,0,0
        return True,0,0,0,0
                

    def run(self, inputs,flag=None):
        self.initialize_tapes(inputs,flag)
        self.current_state = self.start_state
        condTransitionKeyFound = True
        while condTransitionKeyFound and self.current_state not in self.accept_state and self.current_state not in self.reject_state:
            condTransitionKeyFound = self.step()[0]
        result = self.current_state in self.accept_state
        print(f"TM: {self.name}")
        print(f"Result: {'Accepted' if result else 'Rejected'}")
        print("Final Tapes:")
        for i in range(self.num_tapes):
            print(f"Tape {i+1}: {''.join(self.tapes[i])}")
        print("state: "+str(self.current_state))

        # remove B from tape and update head positions

        final_machine_run_state=Machine_Run_State(self.tapes[-1],self.head_positions[-1],self.current_state)
        print("----------------------------")
        return final_machine_run_state
        

    def visualize(self, inputs,delay=1):
        self.initialize_tapes(inputs)
        self.current_state = self.start_state
        def display():
            for i in range(self.num_tapes):
                tape = ''.join(self.tapes[i])
                head_position = self.head_positions[i]
                print(f"Tape {i+1}: {tape}")
                print(" " * (head_position + 7) + "^")
            print(f"Current State: {self.current_state}")
            print("\n" + "-"*50 + "\n")
        
        condTransitionKeyFound = True
        while condTransitionKeyFound and self.current_state not in self.accept_state and self.current_state not in self.reject_state:
            clear_output(wait=True)
            display()
            time.sleep(delay)
            condTransitionKeyFound = self.step()[0]
            time.sleep(delay)
        
        clear_output(wait=True)
        display()
        print("Turing Machine Halted")


    def visualize_step_by_step(self, inputs):
        self.initialize_tapes(inputs)
        def display():
            clear_output(wait=True)
            for i in range(self.num_tapes):
                tape = ''.join(self.tapes[i])
                head_position = self.head_positions[i]
                print(f"Tape {i+1}: {tape}")
                print(" " * (head_position + 7) + "^")
            print(f"Current State: {self.current_state}")
            print("\n" + "-"*50 + "\n")
        
        display()
        condTransitionKeyFound = True
        while condTransitionKeyFound and self.current_state not in self.accept_state and self.current_state not in self.reject_state:
            input("Press Enter to proceed to the next step...")
            condTransitionKeyFound = self.step()[0]
            display()

        print("Turing Machine Halted")

    def given_state_is_in_acceptance(self, state):
        return state in self.accept_state
    
    def get_input_alphabet(self):
        return self.input_alphabet
    

    def __str__(self):
            #__init__(self, states, input_alphabet, tape_alphabet, transition_function, start_state, accept_state, reject_state, num_tapes=2):
            
            transitions_str = ",\n        ".join(
                f"({key}): {str(config)}"
                for (key), config in self.transition_function.items()
            )


            return (f"MultiTapeTuringMachine(\n"
                    f"    states={self.states},\n"
                    f"    input_alphabet={self.input_alphabet},\n"
                    f"    tape_alphabet={self.tape_alphabet},\n"
                    f"    transition_function={{\n        {transitions_str}\n    }},\n"
                    f"    start_state='{self.start_state}',\n"
                    f"    accept_state={self.accept_state},\n"
                    f"    reject_state={self.reject_state},\n"
                    f"    num_tapes={str(self.num_tapes)}\n"
                    f")")