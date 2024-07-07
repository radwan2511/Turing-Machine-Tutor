import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from IPython.display import display, clear_output
 ##@@@@@@@@@@@@@@@@@@@@@@222 if you run sandbox remove this turing_machine_tutor.
##@@@@@@@@@@@@@@@@@@@@@@222 if you run test put this turing_machine_tutor.
from turing_machine_tutor.CombinedTuringMachine import CombinedTuringMachine
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.machine_run_state import Machine_Run_State
from turing_machine_tutor.IFTuringMachine import IFTuringMachine
from turing_machine_tutor.WhileTuringMachine import WhileTuringMachine
from turing_machine_tutor.ConcatenateTM import ConcatenateTM
from turing_machine_tutor.MultiTapeTuringMachine import MultiTapeTuringMachine



class TuringMachineVisualizer:
    def __init__(self, turing_machine):
        if not(isinstance(turing_machine,IFTuringMachine) or isinstance(turing_machine,CombinedTuringMachine) or isinstance(turing_machine,TuringMachine) or isinstance(turing_machine,WhileTuringMachine) or isinstance(turing_machine,ConcatenateTM) or isinstance(turing_machine,MultiTapeTuringMachine) ):
            raise Exception("TM cannot be Not (TuringMachine / IFTuringMachine / CombinedTuringMachine / ConcatenateTM / WhileTuringMachine / MultiTapeTuringMachine) Object")
        self.tm = turing_machine
        self.steps = [] ##type is Machine_Run_State
        self.originTM = None
        self.editedIndexes = None

    def run_and_visualize(self, input_string, max_steps=10,head_position=0):
        if(isinstance(self.tm, MultiTapeTuringMachine)):
            return self.run_and_visualize_multi_tape_turing_machine(input_string, self.tm.flag)
        if(isinstance(self.tm,IFTuringMachine)):
            return self.run_and_visualize_if_turing_machine(input_string)
        elif(isinstance(self.tm,CombinedTuringMachine) or isinstance(self.tm,WhileTuringMachine) or isinstance(self.tm,ConcatenateTM)):
            return self.run_and_visualize_combined_turing_machine(input_string)
        elif(isinstance(self.tm,TuringMachine)):
            #clear_output(wait=True)  # clear first output of getting user input
            # Reset visualization steps
            self.steps = []
            if not self.tm.contains_chars(input_string):
                self.steps.append("rejected input, input string contains char not from the alphabet.")
                return self.steps
            self.tm.reset_turing_machine()
            self.tm.current_machine_state.head_position=head_position
            self.tm.current_machine_state.put_word_on_tape(input_string)
            new_machine_run_state = Machine_Run_State(self.tm.current_machine_state.tape.copy(),
                                                      self.tm.current_machine_state.head_position,
                                                      self.tm.current_machine_state.state)
            new_machine_run_state.put_word_on_tape(input_string)
            self.steps.append(new_machine_run_state)
            # Run the Turing machine and capture visualization steps for a limited number of steps
            for step in range(max_steps):
                if ((self.tm.current_machine_state.state in self.tm.accept_states) or (
                        self.tm.current_machine_state.state in self.tm.reject_states)):
                    self.steps.append(self.tm.current_machine_state)
                    break
                current_config = self.tm.get_config()
                # new change here
                if current_config == "halt":
                    symbol = self.tm.current_machine_state.tape[self.tm.current_machine_state.head_position]
                    state=self.tm.current_machine_state.state
                    self.steps.append("TM halted at (state: "+str(state)+", symbol: "+str(symbol)+") with no valid transition.")
                    break
                else:
                    self.steps.append(self.tm.run_step(current_config))

            if self.tm.current_machine_state.state in self.tm.accept_states:
                self.steps.append("reached accept state") # To do: add name at the first of line
            elif self.tm.current_machine_state.state in self.tm.reject_states:
                self.steps.append("reached reject state") # To do: add name at the first of line
            else:
                self.steps.append("turing machine halted at non accepting state")
            return self.steps


    def run_and_visualize_combined_turing_machine(self, input_string,head_position=0):
        clear_output(wait=True)  # clear first output of getting user input
        # Reset visualization steps
        self.steps = []
        first_step_is_over_flag = 0
        machine_run_state=None
        self.tm.turing_machines[0].reset_turing_machine() ## only reset first machine
        cond = False
        #index = 0
        index_tm_name = 0
        while not cond:
            for turing_machine in self.tm.turing_machines:
                visualizer = TuringMachineVisualizer(turing_machine)
                if not turing_machine.contains_chars(input_string):
                    self.steps.append("rejected input, input string contains char not from the alphabet.")
                    return self.steps
                if first_step_is_over_flag==0:
                    try:
                        self.steps.append("starting with turing machine with the name: "+self.tm.turing_machines[index_tm_name].name)
                        self.steps=self.steps+visualizer.run_and_visualize(input_string, 5000,head_position)
                        index_tm_name += 1
                        if(index_tm_name < len(self.tm.turing_machines) and self.steps[-1] == "reached accept state"):
                            self.steps.append("proceeding to next turing machine with the name: "+self.tm.turing_machines[index_tm_name].name)
                        turing_machine.reset_turing_machine()
                        machine_run_state=turing_machine.run(input_string,head_position)
                    except Exception as e:
                        self.steps.append("reached reject state")
                        return self.steps
                    first_step_is_over_flag=1
                else:
                    try:
                        self.steps=self.steps+visualizer.run_and_visualize(machine_run_state.tape, 5000,machine_run_state.head_position)
                        index_tm_name += 1
                        if(index_tm_name < len(self.tm.turing_machines) and self.steps[-1] == "reached accept state"):
                            self.steps.append("proceeding to next turing machine with the name: "+self.tm.turing_machines[index_tm_name].name)
                        turing_machine.reset_turing_machine()
                        machine_run_state = turing_machine.run(machine_run_state.tape,machine_run_state.head_position)
                    except Exception as e:
                        self.steps.append("reached reject state")
                        return self.steps
                # self.steps.append("halted on "+self.tm.turing_machines_names[index] + " on acceptance state")
                # index += 1
            #index = 0

            # remove steps with tape [] 
            for s in self.steps:
                if(not isinstance(s,str)):
                    if(len(s.tape) == 0):
                        self.steps.remove(s)

            if (self.tm.while_condition == None):
                return self.steps

            self.steps.append("proceeding to next cond turing machine with the name: "+self.tm.while_condition.name)
            # self.tm.while_condition.run_and_visualize()
            ## run and visulaize While Condition Turing machine
            turing_machine = self.tm.while_condition
            visualizer = TuringMachineVisualizer(turing_machine)
            if not turing_machine.contains_chars(input_string):
                self.steps.append("rejected input, input string contains char not from the alphabet.")
                return self.steps
            if first_step_is_over_flag==0:
                try:
                    self.steps=self.steps+visualizer.run_and_visualize(input_string, 5000,head_position)
                    turing_machine.reset_turing_machine()
                    machine_run_state=turing_machine.run(input_string,head_position)
                except Exception as e:
                    self.steps.append("reached reject state")
                    return self.steps
                first_step_is_over_flag=1
            else:
                try:
                    self.steps=self.steps+visualizer.run_and_visualize(machine_run_state.tape, 5000,machine_run_state.head_position)
                    turing_machine.reset_turing_machine()
                    machine_run_state = turing_machine.run(machine_run_state.tape,machine_run_state.head_position)
                except Exception as e:
                    self.steps.append("reached reject state")
                    return self.steps
            if(self.tm.while_condition != None):
                cond = not self.tm.while_condition.given_state_is_in_acceptance(machine_run_state.state)
            else:
                cond = True
            if not cond:
                index_tm_name = 0
                self.steps.append("starting again with turing machine with the name: "+self.tm.turing_machines[index_tm_name].name)

        return self.steps


    def run_and_visualize_if_turing_machine(self, input_string):
        if_visualizer = TuringMachineVisualizer(self.tm.ifTm)
        if_visualizer.run_and_visualize(input_string, 5000)
        if if_visualizer.tm.current_machine_state.state in if_visualizer.tm.accept_states:
            then_visualizer = TuringMachineVisualizer(self.tm.thenTm)
            then_visualizer.run_and_visualize(input_string, 5000)
            return ["starting with turing machine with the name: "+self.tm.ifTm.name] + if_visualizer.steps + ["proceeding to next turing machine with the name: "+self.tm.thenTm.name] + then_visualizer.steps
        else:
            else_visualizer = TuringMachineVisualizer(self.tm.elseTm)
            else_visualizer.run_and_visualize(input_string, 5000)
            return ["starting with turing machine with the name: "+self.tm.ifTm.name] + if_visualizer.steps  + ["proceeding to next turing machine with the name: "+self.tm.elseTm.name] + else_visualizer.steps

    def run_and_visualize_multi_tape_turing_machine(self, inputs, flag=None):
        self.tm.initialize_tapes(inputs,flag)
        self.tm.current_state = self.tm.start_state
        steps = []
        def display(steps):
            st = ""
            if self.originTM == None:
                for i in range(self.tm.num_tapes):
                    tape = ''.join(self.tm.tapes[i])
                    head_position = self.tm.head_positions[i]
                    st += f"Tape {i+1}: {tape}\n " + " " * (head_position + 7) + "^\n"
                    # st += f"head_position = {head_position}\n" # used for fixing a bug
            else:
                index = 0
                for i in range(self.originTM.num_tapes):
                    if i in self.editedIndexes:
                        tape = ''.join(self.tm.tapes[index])
                        head_position = self.tm.head_positions[index]
                        st += f"Tape {i+1}: {tape}\n " + " " * (head_position + 7) + "^\n"
                        # st += f"head_position = {head_position}\n" # used for fixing a bug 
                        index += 1
                    else:
                        tape = ''.join(self.originTM.tapes[i])
                        head_position = self.originTM.head_positions[i]
                        st += f"Tape {i+1}: {tape}\n " + " " * (head_position + 7) + "^\n"
             
            st += f"Current State: {self.tm.current_state}\n"
            st += "\n" + "-"*50 + "\n"
            steps += [str(st)]
            return steps
        
        condTransitionKeyFound = True
        while condTransitionKeyFound and self.tm.current_state not in self.tm.accept_state and self.tm.current_state not in self.tm.reject_state:
            steps = display(steps)
            condTransitionKeyFound = self.tm.step()
            if condTransitionKeyFound[1] != 0:
                s = ""
                for x in condTransitionKeyFound[4]:
                    s += ", " + str(x+1)
                s = s[2:]
                steps += ["switching to TM: "+condTransitionKeyFound[1]+"\nPassing the tapes number: "+s]
                visualizer1 =TuringMachineVisualizer(condTransitionKeyFound[2])
                visualizer1.tm.flag = True
                visualizer1.originTM = self.tm
                visualizer1.editedIndexes = condTransitionKeyFound[4][:]
                index = 0
                for i in condTransitionKeyFound[4]:
                    visualizer1.tm.head_positions[index] = condTransitionKeyFound[5][index]
                    index += 1
                steps1 = visualizer1.run_and_visualize(condTransitionKeyFound[3],5000)
                visualizer1.tm.flag = None
                visualizer1.originTM = None
                visualizer1.editedIndexes = None
                steps += steps1
                steps += ["returning to TM: "+self.tm.name+"\nUpdating the tapes number: "+s]
            condTransitionKeyFound = condTransitionKeyFound[0]
            
        steps = display(steps)
        steps += ["Turing Machine Halted"]
        clear_output(wait=True)
        return steps