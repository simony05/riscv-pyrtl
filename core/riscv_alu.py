import pyrtl
from riscv_defs import *

# Inputs
alu_op_i = pyrtl.Input(4, 'alu_op_i')
alu_a_i  = pyrtl.Input(32, 'alu_a_i')
alu_b_i  = pyrtl.Input(32, 'alu_b_i')

# Output
alu_p_o = pyrtl.Output(32, 'alu_p_o')

# Registers
result_r = pyrtl.WireVector(32, 'result_r')
shift_r = alu_b_i[0:5]

with pyrtl.conditional_assignment:
    # Shift left
    with alu_op_i == ALU_SHIFTL:
        result_r |= pyrtl.shift_left_logical(alu_a_i, shift_r)
    
    # Shift right
    with alu_op_i == ALU_SHIFTR:
        result_r |= pyrtl.shift_right_logical(alu_a_i, shift_r)
    
    with alu_op_i == ALU_SHIFTR_ARITH:
        result_r |= pyrtl.shift_right_arithmetic(alu_a_i, shift_r)

    # Arithmetic
    with alu_op_i == ALU_ADD:
        result_r |= alu_a_i + alu_b_i

    with alu_op_i == ALU_SUB:
        result_r |= alu_a_i - alu_b_i

    # Logical
    with alu_op_i == ALU_AND:
        result_r |= alu_a_i & alu_b_i

    with alu_op_i == ALU_OR:
        result_r |= alu_a_i | alu_b_i

    with alu_op_i == ALU_XOR:
        result_r |= alu_a_i ^ alu_b_i
    
    # Comparison
    with alu_op_i == ALU_LESS_THAN:
        result_r |= (alu_a_i < alu_b_i).zero_extended(32)
    
    with alu_op_i == ALU_LESS_THAN_SIGNED:
        result_r |= pyrtl.signed_lt(alu_a_i, alu_b_i).zero_extended(32)

    # Default
    with pyrtl.otherwise:
        result_r |= alu_a_i

alu_p_o <<= result_r
