from datetime import datetime
import random
import time
import os
import sys

import gspread
import pandas as pd
from google.colab import auth
from google.auth import default
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.CombinedTuringMachine import CombinedTuringMachine
from turing_machine_tutor.IFTuringMachine import IFTuringMachine
from turing_machine_tutor.TuringMachineVisualizer import TuringMachineVisualizer
from turing_machine_tutor.Challenge import Challenge
from turing_machine_tutor.Next import Next
from IPython.display import display, clear_output
import ast
import inspect
from turing_machine_tutor.WhileTuringMachine import WhileTuringMachine
from turing_machine_tutor.ConcatenateTM import ConcatenateTM
from turing_machine_tutor.MultiTapeTuringMachine import MultiTapeTuringMachine
#imports for submission
import requests
import json





class TuringMachineController:
    def __init__(self):
        self.__turing_machines = {}
        self.__challenges = dict()
        self.__turing_machines_types = {} # types should be Bool or Tape

    @property
    def turing_machines(self):
        return self.__turing_machines

    @property
    def challenges(self):
        return self.__challenges

    def add_turing_machine(self, name, turing_machine, type="bool"):
        if(turing_machine == None):
            raise Exception("TM cannot be None")
        if not(isinstance(turing_machine, TuringMachine) or isinstance(turing_machine, IFTuringMachine) or isinstance(turing_machine, CombinedTuringMachine) or isinstance(turing_machine, WhileTuringMachine) or isinstance(turing_machine, ConcatenateTM) or isinstance(turing_machine, MultiTapeTuringMachine)):
            raise Exception("TM cannot be Not (TuringMachine / IFTuringMachine / CombinedTuringMachine / WhileTuringMachine / ConcatenateTM / MultiTapeTuringMachine) Object")
        if(name == None or name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        if(name in self.__turing_machines.keys()):
            raise Exception("Turing machine with this name already exists in the dict")
        if(type != "bool" and type != "tape"):
            raise Exception("Found error in Turing machine return type, should be bool or tape.")

        turing_machine.name = name
        self.__turing_machines[name] = turing_machine
        self.__turing_machines_types[name] = type

    def update_turing_machine(self, name, turing_machine, type="bool"):
        if(turing_machine == None):
            raise Exception("TM cannot be None")
        if not(isinstance(turing_machine, TuringMachine) or isinstance(turing_machine, IFTuringMachine) or isinstance(turing_machine, CombinedTuringMachine) or isinstance(turing_machine, WhileTuringMachine) or isinstance(turing_machine, ConcatenateTM) or isinstance(turing_machine, MultiTapeTuringMachine)):
            raise Exception("TM cannot be Not (TuringMachine / IFTuringMachine / CombinedTuringMachine / WhileTuringMachine / ConcatenateTM / MultiTapeTuringMachine) Object")
        if(name == None or name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        if(type != "bool" and type != "tape"):
            raise Exception("Found error in Turing machine return type, should be bool or tape.")
        turing_machine.name = name
        self.turing_machines[name] = turing_machine
        self.__turing_machines_types[name] = type

    def remove(self,name):
        if(name == None or name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        if name in self.__turing_machines.keys():
            self.__turing_machines.pop(name)
            self.__turing_machines_types.pop(name)
        else:
            raise Exception("Turing machine with this name doesn't exists in the dict")

    def get_turing_machine(self,name):
        if(name == None or name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        if name in self.__turing_machines.keys():
            return self.__turing_machines[name]
        else:
            raise Exception("Turing machine with this name:"+ str(name) +" doesn't exists in the dict")

    def get_all_names(self):
        return self.__turing_machines.keys()

    def run_turing_machine(self, name, input_string):
        try:
            self.get_turing_machine(name)
        except Exception as e:
            print(str(e))
        try:
            output = self.__turing_machines[name].run(input_string)
            try:
                print("tape:= " + ''.join(output.tape.copy()))
                print("accepted:= " + str(self.__turing_machines[name].given_state_is_in_acceptance(output.state)))
                print("state:= "+str(output.state))
            except Exception as e:
                print(e)
            return output
        except Exception as e:
            print(str(e))


    def visualize(self,turing_name,input, delay=1):
        #self.__turing_machines[turing_name].reset_turing_machine()
        visualizer =TuringMachineVisualizer(self.__turing_machines[turing_name])
        steps = visualizer.run_and_visualize(input,5000)

        self.display_steps_of_visualizer(steps,delay)


    def visualize_step_by_step(self,turing_name,machine_input):
        #self.__turing_machines[turing_name].reset_turing_machine()
        visualizer =TuringMachineVisualizer(self.__turing_machines[turing_name])
        steps= visualizer.run_and_visualize(machine_input,5000)
        user_input = "start"
        index=0
        step_counter=0

        # remove steps with tape [] 
        for s in steps:
            if(not isinstance(s,str)):
                if(len(s.tape) == 0):
                    steps.remove(s)

        while user_input.lower() !="stop":
            #clear_output(wait=True)
            step_counter=self.display_step_at_index(steps,index,step_counter)
            if(step_counter==-1):
                return
            user_input = input("Press Enter to continue or type 'stop' to end: ")
            #clear_output(wait=True)
            index=index+1
            



    def display_step_at_index(self, steps,index,step_counter):
        if (isinstance(steps[index], str)):
            if index<len(steps)-1:
                clear_output(wait=True)
                print(steps[index])
                time.sleep(1)
                return step_counter + 1
            else:
                clear_output(wait=True)
                print(steps[index])
                time.sleep(1)
                return -1
        self.print_step(steps[index], step_counter)
        #clear_output(wait=True)
        return step_counter + 1





    def display_steps_of_visualizer(self,steps, delay=1):
        steps_counter=0
        for step in steps:
            # Display the tape as an array
            if(isinstance(step, str)):
                print(step)
                time.sleep(delay)
                clear_output(wait=True)
                continue
            self.print_step(step,steps_counter,delay)
            clear_output(wait=True)
            steps_counter=steps_counter+1
    

    def print_step(self, step, step_counter,delay=1):
        clear_output(wait=True)
        tape_str = ' '.join(step.tape)

        head_position_str = ' ' * (2 * step.head_position) + '^'
        # Display current state and step number
        state_step_info = f"State: {step.state} | Step: {step_counter + 1}"
        if (len(step.tape) == 0):
            # print("proceeding to next turing machine")
            # time.sleep(0.5)  # Pause for a short duration to visualize each step
            # clear_output(wait=True)
            # print(f"Step: {step_counter + 1}")
            # time.sleep(1)  # Pause for a short duration to visualize each step
            # clear_output(wait=True)
            return
        # Print the visualization
        print(tape_str)
        print(head_position_str)
        print(state_step_info)
        print('-' * (2 * len(step.tape) + 1))  # Separator line
        time.sleep(delay)  # Pause for a short duration to visualize each step
        #clear_output(wait=True)


    def validate_turing_machineTA(self, name, test_count=100,max_input_length=20):
        turing_name = name

        if(turing_name == None or turing_name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(turing_name, str)):
            raise Exception("Name cannot be not str object")
        if turing_name not in self.__turing_machines.keys():
            raise Exception("there is no turing machine with the name: "+turing_name)
        function_object = self.__challenges[turing_name].function
        
        if(function_object == None):
            raise Exception("func cannot be None")
        if(not callable(function_object)):
            raise Exception("func cannot be not function object")
        try:
            if(not isinstance(function_object(""),bool)):
                if not isinstance(function_object(""), str):
                    raise Exception()
            str_msg = self.validateFuncReturnOnlyBool(function_object)
            str_msg2 = ""
            if len(str_msg) != 0:
                str_msg2 = self.validateFuncReturnOnlyStr(function_object, self.__turing_machines[turing_name].get_input_alphabet())
            if(len(str_msg) > 0 and len(str_msg2) > 0):
                raise Exception("found error in func at line value: "+str_msg+" , func should return only True/False")
        except Exception as e:
            if(len(str(e)) > 0 and "found error in func at line value: " in str(e)):
                raise e
            elif(len(str(e))>0 and "Function did not return a string for input:" in str(e)):
                raise e
            else:
                raise Exception("func cannot be function object that doesnt get string input and output True/False (boolean)")
        
        is_all_strings = lambda my_list: all(isinstance(item, str) and len(item) >= 1 for item in my_list)
        extreme_cases= self.__challenges[turing_name].edge_cases
        if(extreme_cases == None):
            raise Exception("extreme_cases cannot be None")
        if((not isinstance(extreme_cases, (list,set))) or not is_all_strings(extreme_cases)):
            raise Exception("extreme_cases cannot contain a non string object")
        
        check_alphabet_equal = self.get_turing_machine(name) # to throw exception if turing machine name and challenge doesn't match
        if(check_alphabet_equal.get_input_alphabet() != self.__challenges[turing_name].get_input_alphabet()):
            raise Exception("TM " + str(name) +" alphabet must be " + str(self.__challenges[turing_name].get_input_alphabet()))

        # first test mustPass and mustFail#############################################################################################
        if self.__challenges[turing_name].mustPass != None:
            print("testing Must Pass cases:\n ")
            for case, res0 in self.__challenges[turing_name].mustPass: ##test must pass cases
                final_machine_state=None
                try:
                    final_machine_state = self.__turing_machines[turing_name].run(case if not isinstance(self.__turing_machines[turing_name], MultiTapeTuringMachine) else [case])
                except Exception as e:
                    print(e)

                function_result = function_object(case)
                if(self.__turing_machines_types[turing_name] == "bool"):
                    if (final_machine_state == None):
                        if function_result == False:
                            print(f"Validation passed for input: {case}")
                        else:
                            print(f"Validation failed for input: {case}")
                            return False
                        continue
                is_in_acceptance_checker = self.__turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state) if self.__turing_machines_types[turing_name] == "bool" else self.remove_b(final_machine_state.tape)
                if function_result != is_in_acceptance_checker:
                    print(f"Validation failed for input: {case}")
                    return False
                else:
                    print(f"Validation passed for input: {case}")

        if self.__challenges[turing_name].mustFail != None:
            print("testing Must Fail cases:\n ")
            for case, res0 in self.__challenges[turing_name].mustFail: ##test must Fail cases
                final_machine_state=None
                try:
                    final_machine_state = self.__turing_machines[turing_name].run(case if not isinstance(self.__turing_machines[turing_name], MultiTapeTuringMachine) else [case])
                except Exception as e:
                    print(e)

                function_result = function_object(case)
                if(self.__turing_machines_types[turing_name] == "bool"):
                    if (final_machine_state == None):
                        if function_result == False:
                            print(f"Validation passed for input: {case}")
                        else:
                            print(f"Validation failed for input: {case}")
                            return False
                        continue
                is_in_acceptance_checker = self.__turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state) if self.__turing_machines_types[turing_name] == "bool" else self.remove_b(final_machine_state.tape)
                if function_result != is_in_acceptance_checker:
                    print(f"Validation failed for input: {case}")
                    return False
                else:
                    print(f"Validation passed for input: {case}")

        ###############################################################################################################################
        # then run generated test
        for _ in range(test_count): ## generate random words and test them
            for input_length in range(1,max_input_length):
                #print("My alphabet is : " + str(self.__turing_machines[turing_name].get_input_alphabet()))
                alphabet = ''.join(self.__challenges[turing_name].get_input_alphabet())
                input_string = ""
                if isinstance(self.__turing_machines[turing_name], MultiTapeTuringMachine):
                    res = []
                    #for i in range(0,self.__turing_machines[turing_name].num_tapes):
                    res.append(''.join(random.choice(alphabet) for _ in range(input_length)))
                    input_string = res
                else:
                    input_string = ''.join(random.choice(alphabet) for _ in range(input_length))  
                print("testing on input: "+ (input_string if isinstance(input_string,str) else input_string[0]))
                final_machine_state=None
                try:
                    final_machine_state=self.__turing_machines[turing_name].run(input_string)
                    #final_machine_state=self.__turing_machines[turing_name].run("01")
                except Exception as e:
                    print(e)
                    final_machine_state = None
                function_result=function_object(input_string if isinstance(input_string,str) else input_string[0]) ## boolean function i guess
                if(self.__turing_machines_types[turing_name] == "bool"):
                    if (final_machine_state == None):
                        str_results = "func returned: " + str(function_result) + " TM returned: False"
                        if function_result == False:
                            print(f"Validation passed for input: {input_string}")
                        else:
                            print(f"Validation failed for input: {input_string}" + " , " + str_results)
                            return False
                        continue
                if (isinstance(self.__turing_machines[turing_name], TuringMachine) or isinstance(self.__turing_machines[turing_name], IFTuringMachine)):
                    ##it is normal turing machine
                    is_in_acceptance_checker=self.__turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state) if self.__turing_machines_types[turing_name] == "bool" else self.remove_b(final_machine_state.tape)
                elif(isinstance(self.__turing_machines[turing_name], CombinedTuringMachine) or isinstance(self.__turing_machines[turing_name], WhileTuringMachine) or isinstance(self.__turing_machines[turing_name], ConcatenateTM)):
                    ##it is combined_turing_machine
                    is_in_acceptance_checker = self.__turing_machines[turing_name].turing_machines[-1].given_state_is_in_acceptance(
                        final_machine_state.state) if self.__turing_machines_types[turing_name] == "bool" else final_machine_state.tape
                elif(isinstance(self.__turing_machines[turing_name], MultiTapeTuringMachine)):
                    is_in_acceptance_checker = self.__turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state) if self.__turing_machines_types[turing_name] == "bool" else self.remove_b(final_machine_state.tape)
                if function_result!=is_in_acceptance_checker:
                    str_results = "func returned: " + str(function_result) + " TM returned: "+str(is_in_acceptance_checker)
                    print(f"Validation failed for input: {input_string}" + " , " + str_results)
                    return False
                else :
                    print(f"Validation passed for input: {input_string if isinstance(input_string,str) else input_string[0]}")
        print("testing extreme cases:\n ")
        for extreme_case in extreme_cases: ##test extreme cases
            final_machine_state=None
            try:
                final_machine_state = self.__turing_machines[turing_name].run(extreme_case if not isinstance(self.__turing_machines[turing_name], MultiTapeTuringMachine) else [extreme_case])
            except Exception as e:
                print(e)

            function_result = function_object(extreme_case)
            if self.__turing_machines_types[turing_name] == "bool":
                if (final_machine_state == None):
                    if function_result == False:
                        print(f"Validation passed for input: {extreme_case}")
                    else:
                        print(f"Validation failed for input: {extreme_case}")
                        return False
                    continue
            is_in_acceptance_checker = self.__turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state) if self.__turing_machines_types[turing_name] == "bool" else self.remove_b(final_machine_state.tape)
            if function_result != is_in_acceptance_checker:
                print(f"Validation failed for input: {extreme_case}")
                return False
            else:
                print(f"Validation passed for input: {extreme_case}")

        print(f"\n\nall Validation passed for {turing_name} Turing machine.")
        return True

    # user can use this function
    def validate_turing_machine(self,turing_name,function_object,extreme_cases=[],test_count=100,max_input_length=20):
            if(turing_name == None or turing_name == ""):
                raise Exception("Name cannot be None")
            if(not isinstance(turing_name, str)):
                raise Exception("Name cannot be not str object")
            if turing_name not in self.__turing_machines.keys():
                raise Exception("there is no turing machine with the name: "+turing_name)
            if(function_object == None):
                raise Exception("func cannot be None")
            if(not callable(function_object)):
                raise Exception("func cannot be not function object")
            try:
                if(not isinstance(function_object(""),bool)):
                    if not isinstance(function_object(""), str):
                        raise Exception()
                str_msg = self.validateFuncReturnOnlyBool(function_object)
                str_msg2 = ""
                if len(str_msg) != 0:
                    str_msg2 = self.validateFuncReturnOnlyStr(function_object, self.__turing_machines[turing_name].get_input_alphabet())
                if(len(str_msg) > 0 and len(str_msg2) > 0):
                    raise Exception("found error in func at line value: "+str_msg+" , func should return only True/False")
            except Exception as e:
                if(len(str(e)) > 0 and "found error in func at line value: " in str(e)):
                    raise e
                elif(len(str(e))>0 and "Function did not return a string for input:" in str(e)):
                    raise e
                else:
                    raise Exception("func cannot be function object that doesnt get string input and output True/False (boolean) or string")
            is_all_strings = lambda my_list: all(isinstance(item, str) and len(item) >= 1 for item in my_list)
            if(extreme_cases == None):
                raise Exception("extreme_cases cannot be None")
            if((not isinstance(extreme_cases, (list,set))) or not is_all_strings(extreme_cases)):
                raise Exception("extreme_cases cannot contain a non string object")

            for _ in range(test_count): ## generate random words and test them
                for input_length in range(1,max_input_length):
                    #print("My alphabet is : " + str(self.__turing_machines[turing_name].get_input_alphabet()))
                    alphabet = ''.join(self.__turing_machines[turing_name].get_input_alphabet())
                    input_string = ""
                    if isinstance(self.__turing_machines[turing_name], MultiTapeTuringMachine):
                        res = []
                        #for i in range(0,self.__turing_machines[turing_name].num_tapes):
                        res.append(''.join(random.choice(alphabet) for _ in range(input_length)))
                        input_string = res
                    else:
                        input_string = ''.join(random.choice(alphabet) for _ in range(input_length))
                    print("testing on input: "+ (input_string if isinstance(input_string,str) else input_string[0]))
                    final_machine_state=None
                    try:
                        final_machine_state=self.__turing_machines[turing_name].run(input_string)
                        #final_machine_state=self.__turing_machines[turing_name].run("01")
                    except Exception as e:
                        print(e)
                        final_machine_state = None
                    function_result=function_object(input_string if isinstance(input_string,str) else input_string[0]) ## boolean function i guess
                    if self.__turing_machines_types[turing_name] == "bool":
                        if (final_machine_state == None):
                            str_results = "func returned: " + str(function_result) + " TM returned: False"
                            if function_result == False:
                                print(f"Validation passed for input: {input_string if isinstance(input_string,str) else input_string[0]}")
                            else:
                                print(f"Validation failed for input: {input_string if isinstance(input_string,str) else input_string[0]}" + " , " + str_results)
                                return False
                            continue
                    if (isinstance(self.__turing_machines[turing_name], TuringMachine) or isinstance(self.__turing_machines[turing_name], IFTuringMachine)):
                        ##it is normal turing machine
                        is_in_acceptance_checker=self.__turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state) if self.__turing_machines_types[turing_name] == "bool" else self.remove_b(final_machine_state.tape)
                    elif(isinstance(self.__turing_machines[turing_name], CombinedTuringMachine) or isinstance(self.__turing_machines[turing_name], WhileTuringMachine) or isinstance(self.__turing_machines[turing_name], ConcatenateTM)):
                        ##it is combined_turing_machine
                        is_in_acceptance_checker = self.__turing_machines[turing_name].turing_machines[-1].given_state_is_in_acceptance(
                            final_machine_state.state) if self.__turing_machines_types[turing_name] == "bool" else self.remove_b(final_machine_state.tape)
                    elif(isinstance(self.__turing_machines[turing_name], MultiTapeTuringMachine)):
                        is_in_acceptance_checker = self.__turing_machines[turing_name].given_state_is_in_acceptance(
                            final_machine_state.state) if self.__turing_machines_types[turing_name] == "bool" else self.remove_b(final_machine_state.tape)

                    
                    if function_result!=is_in_acceptance_checker:
                        str_results = "func returned: " + str(function_result) + " TM returned: "+str(is_in_acceptance_checker)
                        print(f"Validation failed for input: {input_string if isinstance(input_string,str) else input_string[0]}" + " , " + str_results)
                        return False
                    else :
                        print(f"Validation passed for input: {input_string if isinstance(input_string,str) else input_string[0]}")
            print("testing extreme cases:\n ")
            for extreme_case in extreme_cases: ##test extreme cases
                #extreme_case = extreme_case if isinstance(extreme_case, str) else extreme_case[0]
                final_machine_state=None
                try:
                    final_machine_state = self.__turing_machines[turing_name].run(extreme_case if not isinstance(self.__turing_machines[turing_name], MultiTapeTuringMachine) else [extreme_case])
                except Exception as e:
                    print(e)

                function_result = function_object(extreme_case)

                if self.__turing_machines_types[turing_name] == "bool":
                    if (final_machine_state == None):
                        if function_result == False:
                            print(f"Validation passed for input: {extreme_case}")
                        else:
                            print(f"Validation failed for input: {extreme_case}")
                            return False
                        continue
                is_in_acceptance_checker = self.__turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state) if self.__turing_machines_types[turing_name] == "bool" else self.remove_b(final_machine_state.tape)
                if function_result != is_in_acceptance_checker:
                    print(f"Validation failed for input: {extreme_case}")
                    return False
                else:
                    print(f"Validation passed for input: {extreme_case}")

            print("Validation passed for all Turing machines.")
            return True
    
    def remove_b(self, chars):
        return ''.join(char for char in chars if char != 'B')


    def convert_string_to_set(self,given_string):
        corrected_true = given_string.replace('true', 'True')
        corrected_string = corrected_true.replace('false', 'False')
        list_of_tuples = ast.literal_eval(corrected_string)

        return list_of_tuples

    def extract_func_name(self,function_string):
        def_index = function_string.find('def ')
        function_name_start = def_index + len('def ')
        function_name_end = function_string.find('(', function_name_start)
        function_name = function_string[function_name_start:function_name_end].strip()

        return function_name

    def collect_machines_and_challenges(self):
        auth.authenticate_user()
        creds, _ = default()
        challenges_url = 'https://docs.google.com/spreadsheets/d/1FB0mj8TfmP93VShGwjy0OFyWgMzefmjBbg6LfgGmbDE/edit?gid=0#gid=0'
        gc = gspread.authorize(creds)
        sheet = gc.open_by_url(challenges_url)
        worksheet = sheet.get_worksheet(0)
        rows = worksheet.get_all_values()
        headers = rows[0]
        rows_as_dicts = []
        exec_globals = {}
        for row_values in rows[1:]:
            # Create a dictionary for the current row
            row_dict = {}
            for i, header in enumerate(headers):
                row_dict[header] = row_values[i] if i < len(row_values) else ''
            # Add the dictionary to the list
            rows_as_dicts.append(row_dict)
        challenges = dict()
        for row in rows_as_dicts:
            name = row["name"]
            description = row["description"]
            function_string = row["function"]
            exec(function_string, exec_globals)
            if row["edge_cases"] != "" or row["edge_cases"] != None:
                edge_cases = self.convert_string_to_set(row["edge_cases"])
            alphabet_string = row["input_alphabet"]
            must_pass = self.convert_string_to_set(row["must_pass"])
            must_fail = None
            if "must_fail" in row.keys():
                must_fail_string = row['must_fail']
                if must_fail_string != None and must_fail_string != '':
                    must_fail = self.convert_string_to_set(must_fail_string)

            input_alphabet = self.convert_string_to_set(alphabet_string)
            function_name = self.extract_func_name(function_string)
            function_object = exec_globals[function_name]
            new_challenge = Challenge(name, input_alphabet, description, function_object, edge_cases,function_string)
            new_challenge.MustPass(must_pass)
            if must_fail != None:
                new_challenge.MustFail(must_fail)
            challenges[name]=new_challenge
        machines_url = 'https://docs.google.com/spreadsheets/d/1eQYfMXWgzz8PyRBzIaUqlAvx1Vm7ASXujEaY9WDpG2s/edit?gid=0#gid=0'
        gc = gspread.authorize(creds)
        sheet = gc.open_by_url(machines_url)
        worksheet = sheet.get_worksheet(0)
        rows = worksheet.get_all_values()
        current_name_index = 2
        id_to_dicts = dict()
        for row in rows[1:]:
            if not (isinstance(row[0], str) and row[0].isdigit() and len(row[0]) == 9):
                continue
            machines_dict = dict()
            while current_name_index < len(row):
                if row[current_name_index] != '':
                    machine_string = row[current_name_index + 1]
                    machine_obj = eval(machine_string)
                    machines_dict[row[current_name_index]] = machine_obj
                current_name_index = current_name_index + 3
            current_name_index = 2
            id_to_dicts[row[0]] = machines_dict
        return id_to_dicts,challenges

    def validate_submissions(self):
         password = input("Please enter password: ")
         headers = {'Content-Type': 'application/json'}
         data = {"password": password}
         response = requests.post(self.authorizer_url, data=json.dumps(data), headers=headers)
         if response.text=='access granted':
             submit_row=[]
             id_to_dicts,challenges=self.collect_machines_and_challenges()
             for id in id_to_dicts:
                submit_row += [id]
                for machine in id_to_dicts[id]:
                    result=self.validate_results(id_to_dicts[id][machine], challenges[machine])
                    if result:
                        submit_row += [machine,"Passed"]
                    else:
                        submit_row += [machine,"Failed"]
                self.append_or_update_row_challenge_summary(submit_row)
                submit_row=[]
             print("DONE!, please preview the sheets.")
         else :
             print(response.text)

    def validate_results(self, machine, challenge):
        function_object = challenge.function
        is_all_strings = lambda my_list: all(isinstance(item, str) and len(item) >= 1 for item in my_list)
        extreme_cases = challenge.edge_cases
        if (extreme_cases == None):
            return
        if ((not isinstance(extreme_cases, (list, set))) or not is_all_strings(extreme_cases)):
            return
        if (machine.get_input_alphabet() != challenge.get_input_alphabet()):
            return
        # first test mustPass and mustFail#############################################################################################
        if challenge.mustPass != None:
            for case , res0 in challenge.mustPass:  ##test must pass cases
                final_machine_state = None
                try:
                    final_machine_state = machine.run(case)
                except Exception as e:
                    print(e)

                function_result = function_object(case)
                if (final_machine_state == None):
                    if function_result == True:
                        ##append to the sheet that validates the challenge and the machine
                        return False
                    continue
                is_in_acceptance_checker = machine.given_state_is_in_acceptance(final_machine_state.state)
                if function_result != is_in_acceptance_checker:
                    return False

        if challenge.mustFail != None:
            for case, res0 in challenge.mustFail:  ##test must Fail cases
                final_machine_state = None
                try:
                    final_machine_state = machine.run(case)
                except Exception as e:
                    print(e)

                function_result = function_object(case)
                if (final_machine_state == None):
                    if function_result == True:
                        return False
                    continue
                is_in_acceptance_checker = machine.given_state_is_in_acceptance(final_machine_state.state)
                if function_result != is_in_acceptance_checker:
                    return False

        ###############################################################################################################################
        # then run generated test
        for _ in range(100):  ## generate random words and test them
            for input_length in range(1, 20):
                alphabet = ''.join(challenge.get_input_alphabet())
                input_string = ''.join(random.choice(alphabet) for _ in range(input_length))
                final_machine_state = None
                try:
                    final_machine_state = machine.run(input_string)
                except Exception as e:
                    print(e)
                    final_machine_state = None
                function_result = function_object(input_string)  ## boolean function i guess
                if (final_machine_state == None):
                    str_results = "func returned: " + str(function_result) + " TM returned: False"
                    if function_result != False:
                        return False
                    continue
                if (isinstance(machine, TuringMachine) or isinstance(machine, IFTuringMachine)):
                    ##it is normal turing machine
                    is_in_acceptance_checker=machine.given_state_is_in_acceptance(final_machine_state.state)
                elif(isinstance(machine, CombinedTuringMachine) or isinstance(machine, WhileTuringMachine) or isinstance(machine, ConcatenateTM)):
                    ##it is combined_turing_machine
                    is_in_acceptance_checker = machine.turing_machines[-1].given_state_is_in_acceptance(
                        final_machine_state.state)
                elif(isinstance(machine, MultiTapeTuringMachine)):
                    is_in_acceptance_checker = final_machine_state
                if function_result != is_in_acceptance_checker:
                    str_results = "func returned: " + str(function_result) + " TM returned: " + str(
                        is_in_acceptance_checker)
                    return False
        for extreme_case in extreme_cases:  ##test extreme cases
            final_machine_state = None
            try:
                final_machine_state = machine.run(extreme_case)
            except Exception as e:
                print(e)

            function_result = function_object(extreme_case)
            if (final_machine_state == None):
                if function_result != False:
                    return False
                continue
            is_in_acceptance_checker = machine.given_state_is_in_acceptance(final_machine_state.state)
            if function_result != is_in_acceptance_checker:
                return False
        return True

    def add_challenge(self, turing_machine_name, input_alphabet, turing_machine_description, function_that_accepts_the_language_of_tm,
                      edge_cases_list):
        challenge = Challenge(turing_machine_name, input_alphabet, turing_machine_description, function_that_accepts_the_language_of_tm, edge_cases_list)
        if(turing_machine_name in self.__challenges.keys()):
            raise Exception("challenge with this name already exists")
        self.__challenges[turing_machine_name] = challenge

    def get_challenges(self):
        print("\n\ncurrent available challenges:\n")
        index = 1
        for key in self.__challenges.keys():
            print(f"[{index}]turing machine name: {key}")
            print(f"description: {self.__challenges[key].description}\n")
            index = index + 1

    def validateFuncReturnOnlyBool(self, func):
        # Get the source code of the function
        source_lines, _ = inspect.getsourcelines(func)
        source_code = ''.join(source_lines)

        # Parse the source code into an AST (Abstract Syntax Tree)
        tree = ast.parse(source_code)

        # Extract return statements from the AST
        for node in ast.walk(tree):
            if isinstance(node, ast.Return):
                # Get the value of the return statement if it exists
                if node.value is not None:
                    return_stmt = ast.unparse(node).strip()
                    if return_stmt not in ["return True", "return False"]:
                        return return_stmt
                else:
                    return "return"  # Empty return statement

        return ""  # All return statements are valid

    def validateFuncReturnOnlyStr(self, func, input_alphabet, num_tests=200, max_length=20):
        for _ in range(num_tests):
            random_length = random.randint(1, max_length)
            random_string = ''.join(random.choice(list(input_alphabet)) for _ in range(random_length))
            result = func(random_string)
            assert isinstance(result, str), f"Function did not return a string for input: {random_string}. Returned: {type(result)}"
        #print("All tests passed. Function returns a string for all inputs.")
        return ""


    # URL of your Google Apps Script web app
    web_app_url = 'https://script.google.com/macros/s/AKfycbw5fZTPDVxk1IGrMGQWA3F5ENLAsXI2QyOkht7drz6riJz1uKdbU0XLqUuW5S_My3n09g/exec'
    authorizer_url='https://script.google.com/macros/s/AKfycbwN_-E2WO6zo-yqrQdT7CcssmtDK5hv2b2cs7nRL2iimrqUDU88G1mij13lXguZm0xo/exec'
    challenge_summary_url='https://script.google.com/macros/s/AKfycbzHa83lNIFXtczQr5vw3gSUy9QwjfpfvcyLjoRRMLi0eB6NZLppzabaXHWIxJRri2b3/exec'

    def append_or_update_row(self, data):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.web_app_url, data=json.dumps(data), headers=headers)
        return response.text
    def append_or_update_row_challenge_summary(self, data):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.challenge_summary_url, data=json.dumps(data), headers=headers)
        return response.text
    def submit(self):
        # if spreadsheet_url == None:
        #     spreadsheet_url = os.getenv('GOOGLE_SHEET_URL')
        # Authorize the Google Sheets API
        # auth.authenticate_user()
        # creds, _ = default()
        # gc = gspread.authorize(creds)
        # sheet = gc.open_by_url(spreadsheet_url).sheet1
        # Get User ID
        user_id = input("Please enter your ID number: ")
        if not(isinstance(user_id, str) and user_id.isdigit() and len(user_id) == 9):
            raise Exception("Not Valid ID, id should be all numbers and of len 9!")
        user_id_confrim = input("Please Confirm your ID again: ")
        if(user_id_confrim != user_id):
            raise Exception("ID and ConfirmID do not match, Try Again!")
        
        #sheet.append_row([user_id, self.get_turing_machine(TM).__str__(), "Passed" if self.validate_turing_machineTA('0n1n') else "Failed"])
        #"""Log the test results to Google Sheets."""
        def append_or_overwrite(sheet, row_data):
            ids = sheet.col_values(1)
            new_id = row_data[0]

            if new_id in ids:
                row_index = ids.index(new_id) + 1
                sheet.update(f'A{row_index}:Z{row_index}', [row_data])
                print(f"Row with ID {new_id} updated.")
            else:
                sheet.append_row(row_data)
                print(f"Row with ID {new_id} appended.")
        #append_or_overwrite(sheet,[user_id, self.get_turing_machine(TM).__str__(), "Passed" if self.validate_turing_machineTA('0n1n') else "Failed"])
        
        timeOfSubmission = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        submission = [user_id, timeOfSubmission]
        # tms = ""
        # results = ""
        for TM in self.__challenges.keys():
            submission += [TM, self.get_turing_machine(TM).__str__(), "Passed" if self.validate_turing_machineTA(TM) else "Failed"]
        

        res = self.append_or_update_row(submission)
        if(res == "Success"):
            print("\n\nSubmited your TMs, id: "+str(user_id)+" , at: "+str(timeOfSubmission))
            print("Your result:")
            for i in range(2,len(submission)-1,3):
                print(submission[i] + ": "+submission[i+2])
        else:
            print("\n\nFailed To Submit, Try Again!")
        #if(res == )
        #self.append_or_update_row([user_id, self.get_turing_machine(TM).__str__(), "Passed"])
