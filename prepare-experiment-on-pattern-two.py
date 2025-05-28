import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from qiskit.circuit.random import random_circuit
from qiskit import transpile
from qiskit import QuantumCircuit
from qiskit.circuit import Qubit, Clbit, QuantumRegister, ClassicalRegister

def fake_with_list_construct_recursive_block_circuit(num_qubits=1, depth_block_circuit=1, depth_recursive=1):
    fake_circuit_block = []
    
    if depth_recursive == 0:
        fake_circuit_block.append([random_circuit(num_qubits, depth_block_circuit, measure=False)])
        return fake_circuit_block
    
    for d in range(depth_recursive + 1):
        fake_circuit_at_current_depth = []
        for _ in range(2**d):
            fake_circuit_at_current_depth.append(random_circuit(num_qubits, depth_block_circuit, measure=False))
        fake_circuit_block.append(fake_circuit_at_current_depth)
    return fake_circuit_block

def interprete_fake_with_list_recursive_block_circuit(fake_list):
    num_blocks = len(fake_list)
    depth_recursive = len(fake_list[0]) - 1
    depth_block_circuit = fake_list[0][0][0].depth()
    num_qubits = len(fake_list[0][0][0].qubits)
    
    return num_blocks, num_qubits, depth_block_circuit, depth_recursive

def fake_with_list_construct_circuit_with_recursive_block_circuit(num_blocks=1, num_qubits=1, depth_block_circuit=1, depth_recursive=1):
    fake_circuit_with_recursive_block_pattern = []
    for _ in range(num_blocks):
        fake_circuit_with_recursive_block_pattern.append(fake_with_list_construct_recursive_block_circuit(num_qubits, depth_block_circuit, depth_recursive))
    return fake_circuit_with_recursive_block_pattern

def fake_with_list_ordinary_optimization(fake_list, optimization_strength=3):
    return list(map(lambda l: list(map(lambda l: list(map(lambda qc: transpile(qc, optimization_level=optimization_strength), l)), l)), fake_list))

def fake_with_list_max_min_depth_and_gate_count(fake_list):
    num_blocks, num_qubits, depth_block_circuit, depth_recursive = interprete_fake_with_list_recursive_block_circuit(fake_list)
    max_depth = 0    
    min_depth = 0
    max_gate_count = 0    
    min_gate_count = 0    
    
    for b in range(num_blocks):
        for d in range(depth_recursive + 1):
            depths_at_current_depth = []
            gate_counts_at_current_depth = []
            for i in range(2**d):
                depth = fake_list[b][d][i].depth()
                gate_count = len(fake_list[b][d][i].data)
                
                depths_at_current_depth.append(depth)
                gate_counts_at_current_depth.append(gate_count)
            
            max_depth += max(depths_at_current_depth)
            min_depth += min(depths_at_current_depth)
            max_gate_count += max(gate_counts_at_current_depth)
            min_gate_count += min(gate_counts_at_current_depth)
    
    return max_depth, min_depth, max_gate_count, min_gate_count

def fake_with_list_max_min_depth_and_gate_count_after_flatten_each_block_and_optimize(fake_list, optimization_strength=3):
    num_blocks, num_qubits, depth_block_circuit, depth_recursive = interprete_fake_with_list_recursive_block_circuit(fake_list)
    max_depth = 0    
    min_depth = 0
    max_gate_count = 0    
    min_gate_count = 0    
    
    for b in range(num_blocks):
        qc_list = [QuantumCircuit(num_qubits)]
        for d in range(depth_recursive + 1):
            qc_list_new = []
            for qc in qc_list:
                for i in range(2**d):
                    current_circ = qc.compose(fake_list[b][d][i])
                    qc_list_new.append(current_circ)
                
            qc_list = qc_list_new
        
        list_depths = []
        list_gate_counts = []
        
        for qc in qc_list:
            qc_optimized = transpile(qc, optimization_level=optimization_strength)
            depth = qc_optimized.depth()
            gate_count = len(qc_optimized.data)
            
            list_depths.append(depth)
            list_gate_counts.append(gate_count)
        
        max_depth += max(list_depths)
        min_depth += min(list_depths)
        max_gate_count += max(list_gate_counts)
        min_gate_count += min(list_gate_counts)
    
    return max_depth, min_depth, max_gate_count, min_gate_count

def fake_with_list_max_min_depth_and_gate_count_after_flatten_up_to_depth_each_block_and_optimize(fake_list, deapest, optimization_strength=3):
    num_blocks, num_qubits, depth_block_circuit, depth_recursive = interprete_fake_with_list_recursive_block_circuit(fake_list)
    
    assert(deapest <= depth_recursive)
    
    max_depth = 0    
    min_depth = 0
    max_gate_count = 0    
    min_gate_count = 0    
    
    for b in range(num_blocks):
        qc_list = [QuantumCircuit(num_qubits)]
        for d in range(deapest + 1):
            qc_list_new = []
            for qc in qc_list:
                for i in range(2**d):
                    current_circ = qc.compose(fake_list[b][d][i])
                    qc_list_new.append(current_circ)
                
            qc_list = qc_list_new
        
        list_depths_up_to_depth = []
        list_gate_counts_up_to_depth = []
        
        for qc in qc_list:
            qc_optimized = transpile(qc, optimization_level=optimization_strength)
            depth = qc_optimized.depth()
            gate_count = len(qc_optimized.data)
            
            list_depths_up_to_depth.append(depth)
            list_gate_counts_up_to_depth.append(gate_count)
        
        max_depth += max(list_depths_up_to_depth)
        min_depth += min(list_depths_up_to_depth)
        max_gate_count += max(list_gate_counts_up_to_depth)
        min_gate_count += min(list_gate_counts_up_to_depth)
        
        
        
        for d in range(deapest + 1, depth_recursive + 1):
            list_depths_current_depth = []
            list_gate_counts_current_depth = []
            for i in range(2**d):
                qc_optimized = transpile(fake_list[b][d][i], optimization_level=optimization_strength)
                depth = qc_optimized.depth()
                gate_count = len(qc_optimized.data)
                
                list_depths_current_depth.append(depth)
                list_gate_counts_current_depth.append(gate_count)
            
            max_depth += max(list_depths_current_depth)
            min_depth += min(list_depths_current_depth)
            max_gate_count += max(list_gate_counts_current_depth)
            min_gate_count += min(list_gate_counts_current_depth)
    
    return max_depth, min_depth, max_gate_count, min_gate_count
