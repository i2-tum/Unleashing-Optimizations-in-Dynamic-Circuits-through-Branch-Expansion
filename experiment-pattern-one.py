def experiment_on_pattern_one(num_qubits, num_depths, num_blocks, optimization_strength):
    cr = ClassicalRegister(1)
    qc = QuantumCircuit(num_qubits)
    qc.add_register(cr)
    qc_expanded = QuantumCircuit(num_qubits)
    qc_expanded.add_register(cr)

    for n_blocks in range(num_blocks):
        
        head_circuit = random_circuit(num_qubits, num_depths, measure=False)
        circ_in_if = random_circuit(num_qubits, num_depths, measure=False)
        circ_in_else = random_circuit(num_qubits, num_depths, measure=False)

        # Compose the head circuit to our main construction
        qc = qc.compose(head_circuit, qc.qubits)
        # Construct if-else block
        circ_if_and_else = QuantumCircuit(num_qubits)
        circ_if_and_else.add_register(cr)
        with qc.if_test((cr[0], 0)) as _else:
            for instruction in circ_in_if.data:
                qc.append(instruction)
        with _else:
            for instruction in circ_in_else.data:
                qc.append(instruction)

        # Construct the circuit where each block is expanded         
        with qc_expanded.if_test((cr[0], 0)) as _else:
            for instruction in head_circuit.data:
                qc_expanded.append(instruction)
            for instruction in circ_in_if.data:
                qc_expanded.append(instruction)
        with _else:
            for instruction in head_circuit.data:
                qc_expanded.append(instruction)
            for instruction in circ_in_else.data:
                qc_expanded.append(instruction)



    qc_optimized = transpile(qc, optimization_level=optimization_strength)
    depth_ord_max, depth_ord_min, gate_count_ord_max, gate_count_ord_min = calc_max_min_depth_and_gate_count(qc_optimized)

    depth_PI_max, depth_PI_min, gate_count_PI_max, gate_count_PI_min = calc_max_min_depth_and_gate_count_after_branch_wise_optimization(qc_expanded, optimization_strength)
    
    return depth_ord_max, depth_ord_min, gate_count_ord_max, gate_count_ord_min, depth_PI_max, depth_PI_min, gate_count_PI_max, gate_count_PI_min
