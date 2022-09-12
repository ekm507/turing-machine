from pprint import pprint
from turing_machine import *


program = """
q0 x -> x, R q0
q0 0 -> x, R q10
q0 1 -> x, R q11
q0 # -> #, R, q50

q10 1 -> 1, R q10
q10 0 -> 0, R q10
q10 # -> #, R q20

q20 x -> x, R q20
q20 0 -> x, L q30
q20 1 -> 1, L, q_reject
q20 _ -> _, L, q_reject

q30 x -> x, L, q30
q30 # -> #, L, q40

q40 0 -> 0, L q40
q40 1 -> 1, L q40
q40 x -> x, R q0

q50 x -> x, R q50
q50 _ -> _, L q_accept
q50 0 -> 0, L q_reject
q50 1 -> 1, L q_reject


""".replace('\n\n', '\n').strip('\n')

m1 = Turing()
m1.set_program_by_string(program)

# test if setting program works
pprint(m1.program)