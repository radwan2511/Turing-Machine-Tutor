import matplotlib.pyplot as plt
from IPython.display import clear_output
import time
import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class MultiTapeTuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, transition_function, start_state, accept_state, reject_state, num_tapes=2):
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

        self.validate()

    def validate(self):
        # Check that start, accept, and reject states are in the set of states
        assert self.start_state in self.states, "Start state must be in the set of states"
        assert self.accept_state in self.states, "Accept state must be in the set of states"
        assert self.reject_state in self.states, "Reject state must be in the set of states"

        # Check that the input alphabet is a subset of the tape alphabet
        assert self.input_alphabet.issubset(self.tape_alphabet), "Input alphabet must be a subset of the tape alphabet"

        # Check that the transition function has valid states and symbols
        for state_symbols, transition in self.transition_function.items():
            current_state = state_symbols[0]
            current_symbols = state_symbols[1:]
            new_state = transition[0]
            new_symbols = transition[1:self.num_tapes+1]
            directions = transition[self.num_tapes+1:]

            assert current_state in self.states, f"State {current_state} is not in the set of states"
            assert new_state in self.states, f"State {new_state} is not in the set of states"
            assert all(symbol in self.tape_alphabet for symbol in current_symbols), "Transition symbols must be in the tape alphabet"
            assert all(symbol in self.tape_alphabet for symbol in new_symbols), "New symbols must be in the tape alphabet"
            assert len(directions) == self.num_tapes, "There must be a direction for each tape"
            assert all(direction in ['L', 'R', 'S'] for direction in directions), "Directions must be 'L', 'R', or 'N'"

    def initialize_tapes(self, inputs):
        self.current_state = self.start_state
        for i in range(self.num_tapes):
            self.tapes[i] = list(inputs[i]) + ['B']
            self.head_positions[i] = 0

    def step(self):
        symbols = tuple(self.tapes[i][self.head_positions[i]] for i in range(self.num_tapes))
        state_symbols = (self.current_state,) + symbols

        if state_symbols in self.transition_function:
            transition = self.transition_function[state_symbols]
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
                    self.tapes[i].insert(0, 'B')
                    self.head_positions[i] = 0
                if self.head_positions[i] >= len(self.tapes[i]):
                    self.tapes[i].append('B')
        

    def run(self, inputs):
        self.initialize_tapes(inputs)
        while self.current_state != self.accept_state and self.current_state != self.reject_state:
            self.step()
        result = self.current_state == self.accept_state
        print(f"Result: {'Accepted' if result else 'Rejected'}")
        print("Final Tapes:")
        for i in range(self.num_tapes):
            print(f"Tape {i+1}: {''.join(self.tapes[i])}")
        return result

    def visualize(self, inputs):
        self.initialize_tapes(inputs)
        def display():
            for i in range(self.num_tapes):
                tape = ''.join(self.tapes[i])
                head_position = self.head_positions[i]
                print(f"Tape {i+1}: {tape}")
                print(" " * (head_position + 7) + "^")
            print(f"Current State: {self.current_state}")
            print("\n" + "-"*50 + "\n")
        
        while self.current_state != self.accept_state and self.current_state != self.reject_state:
            clear_output(wait=True)
            display()
            time.sleep(0.5)
            self.step()
            time.sleep(0.5)
        
        clear_output(wait=True)
        display()
        print("Turing Machine Halted")