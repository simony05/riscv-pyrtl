import pyrtl
from riscv_defs import *
import riscv_alu

sim = pyrtl.Simulation()

tests = [
    (ALU_ADD, 10, 20, 30),
    (ALU_SUB, 50, 8, 42),
    (ALU_AND, 0b1100, 0b1010, 0b1000),
    (ALU_OR,  0b1100, 0b1010, 0b1110),
    (ALU_XOR, 0b1100, 0b1010, 0b0110),
    (ALU_SHIFTL, 0b0001, 3, 0b1000),
    (ALU_SHIFTR, 0b1000, 3, 0b0001),
    (ALU_SHIFTR_ARITH, 0xF0000000, 4, 0xFF000000),
    (ALU_LESS_THAN, 5, 10, 1),
    (ALU_LESS_THAN, 10, 5, 0),
    (ALU_LESS_THAN_SIGNED, -5, 10, 1),
    (ALU_LESS_THAN_SIGNED, 10, -5, 0),
    (ALU_NONE, 42, 123, 42),
]

for op, a, b, expected in tests:
    sim.step({'alu_op_i': op, 'alu_a_i': a, 'alu_b_i': b})
    result = sim.inspect('alu_p_o')
    assert result == expected, f"Test failed: op={op}, a={a}, b={b}, got={result}, expected={expected}"

print("All PyRTL ALU tests passed!")
