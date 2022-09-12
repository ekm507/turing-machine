from pprint import pprint
from turing_machine import *


program = """
q0 x -> x, R q0
q0 0 -> x, R q10
q0 1 -> x, R q11
q0 # -> #, R q50

q10 1 -> 1, R q10
q10 0 -> 0, R q10
q10 # -> #, R q20

q11 1 -> 1, R q11
q11 0 -> 0, R q11
q11 # -> #, R q21

q20 x -> x, R q20
q20 0 -> x, L q30
q20 1 -> 1, L q_reject
q20 _ -> _, L q_reject

q21 x -> x, R q21
q21 1 -> x, L q31
q21 0 -> 0, L q_reject
q21 _ -> _, L q_reject

q30 x -> x, L q30
q30 # -> #, L q40

q31 x -> x, L q31
q31 # -> #, L q41

q40 0 -> 0, L q40
q40 1 -> 1, L q40
q40 x -> x, R q0

q41 0 -> 0, L q41
q41 1 -> 1, L q41
q41 x -> x, R q0

q50 x -> x, R q50
q50 _ -> _, L q_accept
q50 0 -> 0, L q_reject
q50 1 -> 1, L q_reject


""".replace('\n\n', '\n').strip('\n')

tape_string = '0001#0001_'

m1 = Turing()
m1.set_program_by_string(program)

# test if setting program works

m1.tape.set_tape(tape_string)
# pprint(m1.program)

maximum_steps = 1000
for _ in range(maximum_steps):
    print('-'*len(tape_string))
    print(m1.state)
    print(' '*m1.index+'o')
    print(m1.tape.get_tape_string())
    m1.one_step()
    if m1.halt == True:
        print()
        print()
        print('final state is', m1.state)
        break
else:
    print('machine did not halt!')