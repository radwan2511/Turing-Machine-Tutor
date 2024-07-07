# from Tape import Tape
import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.machine_run_state import Machine_Run_State




class TuringMachine:
    def __init__(self, states, input_alphabet, tape_symbols, transitions, initial_state, accept_states, reject_states):
        self.isValidTM(states, input_alphabet, tape_symbols, transitions, initial_state, accept_states, reject_states)
        
        self.states = set(states)
        self.input_alphabet = set(input_alphabet)
        self.tape_alphabet = set(tape_symbols)
        self.transitions = transitions
        self.initial_state = initial_state
        self.accept_states = set(accept_states) ##list
        self.reject_states = set(reject_states) ##list
        self.blank = "B"
        self.current_machine_state=Machine_Run_State(list(),0,initial_state)
        self.name = ""

        # add Validate turing machine and throw exception if turing machine is not valid

    def get_input_alphabet(self):
        if(self.input_alphabet == None):
            raise Exception("Cannot get input alphabet, please construct the turing machine first")
        return self.input_alphabet
    
    def isValidTM(self, states, input_alphabet, tape_symbols, transitions, initial_state, accept_states, reject_states):
        # lambda function that checks all list items are string
        is_all_strings = lambda my_list: all(isinstance(item, str) and len(item) >= 1 for item in my_list)
        is_all_strings_of_len1 = lambda my_list: all(isinstance(item, str) and len(item) == 1 for item in my_list)
        try:
            if(states == None or len(states) == 0 or (not isinstance(states, (list,set))) or (not is_all_strings(states))):
                raise Exception("states cannot be None / empty list, and must be all string in list of len > 1")
            if(input_alphabet == None or len(input_alphabet) == 0 or (not isinstance(input_alphabet, (list,set))) or (not is_all_strings_of_len1(input_alphabet))):
                raise Exception("input_alphabet cannot be None / empty list, and must be all string in list of len = 1")
            if(tape_symbols == None or len(tape_symbols) == 0 or (not isinstance(tape_symbols, (list,set))) or (not is_all_strings_of_len1(tape_symbols))):
                raise Exception("tape_symbols cannot be None / empty list, and must be all string in list of len = 1")
            
            all_transitions_str = transitions == None or len(transitions) == 0 or (not isinstance(transitions, dict))
            if(all_transitions_str):
                raise Exception("transitions cannot be None / empty dict, and must be dict with all string values of key and all string values of Configuration of len > 1")
            all_transitions_str = isinstance(transitions,dict)
            if (all_transitions_str):
                for key,value in transitions.items():
                    if (key[0] == None or key[1] == None or value.state == None or value.symbol == None or value.action == None):
                        raise Exception("transitions cannot be None / empty dict, and must be dict with all string values of key and all string values of Configuration of len > 1")   
                    all_transitions_str = isinstance(key[0], str) and len(key[0])>0 and isinstance(key[1], str)and len(key[1])>0 and isinstance(value.state, str) and len(value.state)>0 and isinstance(value.symbol, str) and len(value.symbol)>0 and isinstance(value.action, str) and len(value.action)>0
                    if not all_transitions_str:
                        raise Exception("transitions cannot be None / empty dict, and must be dict with all string values of key and all string values of Configuration of len > 1")   
             
                            
            if(initial_state == None or len(initial_state) == 0 or (not isinstance(initial_state, str))):
                raise Exception("initial_state cannot be None / empty string, and must string of len > 1")
            if(accept_states == None or len(accept_states) == 0 or (not isinstance(accept_states, (list,set))) or (not is_all_strings(accept_states))):
                raise Exception("accept_states cannot be None / empty list, and must be all string in list of len > 1")
            if(reject_states == None or len(reject_states) == 0 or (not isinstance(reject_states, (list,set))) or (not is_all_strings(reject_states))):
                raise Exception("reject_states cannot be None / empty list, and must be all string in list of len > 1")
            
            check = "B" in tape_symbols
            if(not check):
                raise Exception("tape symbols must Must contain the blank symbol 'B'")
            check = True
            for alpha in input_alphabet:
                if alpha not in tape_symbols:
                    check = False
                    break
            if(not check):
                raise Exception("Input alphabet must be in tape symbols")
            check = initial_state in states
            if(not check):
                raise Exception("initial state must be in states")
            check = True
            for st in accept_states:
                if st not in states:
                    check = False
                    break
            if(not check):
                raise Exception("accept state must be in states")
            check = True
            for st in reject_states:
                if st not in states:
                    check = False
                    break
            if(not check):
                raise Exception("reject state must be in states")
            
            check = True
            for key,value in transitions.items():
                str_value = "(" + value.state + ", " + value.symbol + ", " + value.action + ")"
                error_msg = str(key) + " : " + str_value
                # check valid key
                if(key[0] not in states):
                    raise Exception("found error in key value at: "+error_msg+" state must be in states")
                if(key[1] not in tape_symbols):
                    raise Exception("found error in key value at: "+error_msg+" symbol must be in tape symbols")
                
                # check valid value
                if(value.state not in states):
                    raise Exception("found error in Configuration value at: "+error_msg+" state must be in states")
                if(value.symbol not in tape_symbols):
                    raise Exception("found error in Configuration value at: "+error_msg+" symbol must be in tape symbols")
                if(value.action not in ['R', 'L', 'S']):
                    raise Exception("found error in Configuration value at: "+error_msg+" action must be 'R' / 'L' / 'S'")            
        except Exception as e:
            raise e

    def setTMName(self, name):
        self.name = name

    def run_step(self, configuration):
        self.current_machine_state.execute_config(configuration)
        new_machine_run_state = Machine_Run_State(self.current_machine_state.tape.copy(),
                                                self.current_machine_state.head_position,
                                                self.current_machine_state.state)
        return new_machine_run_state


    def contains_chars(self, input_string):
        for ch in input_string:
            if(ch not in self.input_alphabet):
                #print(ch)
                return False
        return True

    def get_config(self):
        if self.current_machine_state.tape == '' or self.current_machine_state.tape == []:
            self.current_machine_state.tape = ['B'] # added this to fix bug
        symbol = self.current_machine_state.tape[self.current_machine_state.head_position]
        state=self.current_machine_state.state
        try:
            config = self.transitions[(state,symbol)]
        except:
            return "halt"
        return config


    def reset_turing_machine(self):
        self.current_machine_state.tape = list()
        self.current_machine_state.head_position = 0
        self.current_machine_state.state = self.initial_state

    def run(self, input_string,head_position=0):
        is_all_strings = lambda my_list: all(isinstance(item, str) and len(item) == 1 for item in my_list)
        if(input_string == None or not((isinstance(input_string,list) and is_all_strings(input_string)) or isinstance(input_string,str))):
            raise Exception("Input String cannot be None or not str object or list of chars")
        max_steps=100*len(input_string)
       # self.reset_turing_machine()
        self.current_machine_state.put_word_on_tape(input_string)
        self.current_machine_state.head_position= head_position
        steps = 0

        if not self.contains_chars(input_string):
            raise Exception("rejected input, input string contains char not from the alphabet.")
            ##return Configuration(''.join(tape), head_position,current_state in self.accept_states) ## @@@@ current_state in self.accept_states why boolean it should be state?


        while self.current_machine_state.state not in self.accept_states and self.current_machine_state.state not in self.reject_states and steps < max_steps:
            current_symbol = self.current_machine_state.tape[self.current_machine_state.head_position]
            if(current_symbol not in self.tape_alphabet):
                raise Exception("error on input: tape contains symbol not in tape alphabet.")
                ##return tape, -1, current_state # return head_position as -1
            if (self.current_machine_state.state, current_symbol) in self.transitions:
                current_config=self.transitions[(self.current_machine_state.state, current_symbol)]
                ##self.current_machine_state.write_to_tape(current_config)
                self.current_machine_state.execute_config(current_config)
                steps += 1
            else:
                break

        final_machine_run_state=Machine_Run_State(self.current_machine_state.tape,self.current_machine_state.head_position,self.current_machine_state.state)
        self.reset_turing_machine()
        return final_machine_run_state


    def given_state_is_in_acceptance(self,state):
        return state in self.accept_states

    # def run_combined(self, input_string,head_position): ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ head=0?
    #       max_steps=100*len(input_string)
    #       self.reset_turing_machine()
    #       self.current_machine_state.head_position=head_position
    #       self.current_machine_state.put_word_on_tape(input_string)
    #       steps = 0
    #
    #       while self.current_machine_state.state not in self.accept_states and self.current_machine_state.state not in self.reject_states and steps < max_steps:
    #           current_symbol = self.current_machine_state.tape[head_position]
    #
    #           if (self.current_machine_state.state, current_symbol) in self.transitions:
    #               current_config=self.transitions[(self.current_machine_state.state, current_symbol)]
    #
    #               self.current_machine_state.execute_config(current_config)
    #               steps += 1
    #           else:
    #               break
    #
    #       final_machine_run_state = Machine_Run_State(self.current_machine_state.tape,
    #                                                   self.current_machine_state.head_position,
    #                                                   self.current_machine_state.state)
    #
    #       return final_machine_run_state
    #       #return ''.join(tape), current_state in self.accept_states, head_position
    #      ## return ''.join(tape), current_state, head_position

    def __str__(self):
            transitions_str = ",\n        ".join(
                f"('{state}', '{symbol}'): {str(config)}"
                for (state, symbol), config in self.transitions.items()
            )
            return (f"TuringMachine(\n"
                    f"    states={self.states},\n"
                    f"    input_alphabet={self.input_alphabet},\n"
                    f"    tape_symbols={self.tape_alphabet},\n"
                    f"    transitions={{\n        {transitions_str}\n    }},\n"
                    f"    initial_state='{self.initial_state}',\n"
                    f"    accept_states={self.accept_states},\n"
                    f"    reject_states={self.reject_states}\n"
                    f")")




