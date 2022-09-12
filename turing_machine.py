#!/usr/bin/python3
import re

class Turing():
    def __init__(self) -> None:
        self.tape = ''
        self.program = dict()

    def set_program_by_string(self, program:str):
        transitions = program.split('\n')
        for transition in transitions:
            parameters = re.findall(r'(.+) +(.+) *-> *(.+) *, *(.+) +(.+)', transition)[0]
            init_state, read_string, overwrite_string, next_direction, final_state = parameters

            if init_state not in self.program:
                self.program[init_state] = dict()
            
            self.program[init_state][read_string] = (overwrite_string, next_direction, final_state)
            

    def set_program_by_dict(self, program:dict):
        self.program = program


class Tape():
    def __init__(self) -> None:
        self.tape = ''
    
    def set_tape(self, tape:str):
        self.tape = tape
    
    def get_character(self, index:int):
        return self.tape[index]
    
    def set_character(self, index:int, character:str):
        self.tape[index] = character
