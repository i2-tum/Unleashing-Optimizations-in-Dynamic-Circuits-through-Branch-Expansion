import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from qiskit.circuit.random import random_circuit
from qiskit import transpile
from qiskit import QuantumCircuit
from qiskit.circuit import Qubit, Clbit, QuantumRegister, ClassicalRegister

def list_average(l):
    return sum(l) / float(len(l))

def calc_max_min_depth_and_gate_count(qc: QuantumCircuit):
    depth_max = qc.depth()
    depth_min = qc.depth()
    gate_count_max = len(qc.data)
    gate_count_min = len(qc.data)
    for instruction in qc:
        if instruction.operation.name == 'if_else':
            if_c, else_c = instruction.operation.params
            max_if_else_depth = max(if_c.depth(), else_c.depth())
            min_if_else_depth = min(if_c.depth(), else_c.depth())
            max_if_else_gate = max(len(if_c.data), len(else_c.data))
            min_if_else_gate = min(len(if_c.data), len(else_c.data))
            depth_max = depth_max - 1 + max_if_else_depth            
            depth_min = depth_min - 1 + min_if_else_depth            
            gate_count_max = gate_count_max - 1 + max_if_else_gate
            gate_count_min = gate_count_min - 1 + min_if_else_gate
    return depth_max, depth_min, gate_count_max, gate_count_min

def calc_max_min_depth_and_gate_count_after_branch_wise_optimization(qc: QuantumCircuit, optimization_strength):
    depth_max = qc.depth()
    depth_min = qc.depth()
    gate_count_max = len(qc.data)
    gate_count_min = len(qc.data)
    for instruction in qc:
        if instruction.operation.name == 'if_else':
            if_c, else_c = instruction.operation.params
            if_c = transpile(if_c, optimization_level=optimization_strength)
            else_c = transpile(else_c, optimization_level=optimization_strength)
            max_if_else_depth = max(if_c.depth(), else_c.depth())
            min_if_else_depth = min(if_c.depth(), else_c.depth())
            max_if_else_gate = max(len(if_c.data), len(else_c.data))
            min_if_else_gate = min(len(if_c.data), len(else_c.data))
            depth_max = depth_max - 1 + max_if_else_depth            
            depth_min = depth_min - 1 + min_if_else_depth            
            gate_count_max = gate_count_max - 1 + max_if_else_gate
            gate_count_min = gate_count_min - 1 + min_if_else_gate
    return depth_max, depth_min, gate_count_max, gate_count_min
