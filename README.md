# a turing machine simulator

here, we describe turing machine by a string. each line denoting a transition between machine states.

then the input string is fed into the machine which is the so called tape.  
after that simulation begins.

this program will have 2 modes: answer and show. in mode answer, the simulation will happen as fast as possible and answer of machine will be shown after it halts.  
in the show mode, machine will be simulated step by step and an appropriate output will be shown denoting each state of machine and modifications on the tape

## helps for myself

### Transition form:
when using strings to program the machine,  
transitions should be written like this:
```
initial_state input_string -> output_string, move_direction final_state
```

(spaces are optional)

for instance:
```
q0 0->x,R q1
```
which shows a transistion between state q0 and q1.
if state of the machine is q0,  
whenever read character is '0', the machine will overwrite an 'x' on it and go to the right.  
then state of the machine will be changed to q1.
