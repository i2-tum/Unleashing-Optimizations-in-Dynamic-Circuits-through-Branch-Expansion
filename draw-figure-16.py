average_size = 10
num_qubits = 3
# min_qubit_num = 2
# max_qubit_num = 6
num_depths = 3
# num_blocks = 10
recur_depth = 3
# recur_depth_min=1
# recur_depth_max=2
num_blocks_min = 1
num_blocks_max = 100
optimization_strength = 3

plt.grid()
line_style_index = 0
list_line_style = ['solid', 'dotted', 'dashed', 'dashdot']

x_points = []
y_points_avg_depth_perc_diff_PI_ord_max_d1 = []
y_points_avg_depth_perc_diff_PI_ord_min_d1 = []
y_points_avg_gate_count_perc_diff_PI_ord_max_d1 = []
y_points_avg_gate_count_perc_diff_PI_ord_min_d1 = []

y_points_avg_depth_perc_diff_PI_ord_max_d2 = []
y_points_avg_depth_perc_diff_PI_ord_min_d2 = []
y_points_avg_gate_count_perc_diff_PI_ord_max_d2 = []
y_points_avg_gate_count_perc_diff_PI_ord_min_d2 = []

y_points_avg_depth_perc_diff_PI_ord_max_d3 = []
y_points_avg_depth_perc_diff_PI_ord_min_d3 = []
y_points_avg_gate_count_perc_diff_PI_ord_max_d3 = []
y_points_avg_gate_count_perc_diff_PI_ord_min_d3 = []

for b in range(num_blocks_min, num_blocks_max + 1):
    
    print("Progress report:", end = ' ')
    print("Calculating the", b, end='')
    print("-th case.", end="\r")

    x_points.append(b)

    vect_y_points_avg_depth_perc_diff_PI_ord_max_d1 = []
    vect_y_points_avg_depth_perc_diff_PI_ord_min_d1 = []
    vect_y_points_avg_gate_count_perc_diff_PI_ord_max_d1 = []
    vect_y_points_avg_gate_count_perc_diff_PI_ord_min_d1 = []

    vect_y_points_avg_depth_perc_diff_PI_ord_max_d2 = []
    vect_y_points_avg_depth_perc_diff_PI_ord_min_d2 = []
    vect_y_points_avg_gate_count_perc_diff_PI_ord_max_d2 = []
    vect_y_points_avg_gate_count_perc_diff_PI_ord_min_d2 = []
    
    vect_y_points_avg_depth_perc_diff_PI_ord_max_d3 = []
    vect_y_points_avg_depth_perc_diff_PI_ord_min_d3 = []
    vect_y_points_avg_gate_count_perc_diff_PI_ord_max_d3 = []
    vect_y_points_avg_gate_count_perc_diff_PI_ord_min_d3 = []
    
    for t in range(average_size):
        cur_circ = fake_with_list_construct_circuit_with_recursive_block_circuit(b,num_qubits,num_depths,recur_depth)
        ordinary_optimized_circ = fake_with_list_ordinary_optimization(cur_circ)
        depth_ord_max, depth_ord_min, gate_count_ord_max, gate_count_ord_min = fake_with_list_max_min_depth_and_gate_count(ordinary_optimized_circ)
        depth_PI_max_d1, depth_PI_min_d1, gate_count_PI_max_d1, gate_count_PI_min_d1 = fake_with_list_max_min_depth_and_gate_count_after_flatten_up_to_depth_each_block_and_optimize(cur_circ, 1)
        depth_PI_max_d2, depth_PI_min_d2, gate_count_PI_max_d2, gate_count_PI_min_d2 = fake_with_list_max_min_depth_and_gate_count_after_flatten_up_to_depth_each_block_and_optimize(cur_circ, 2)
        depth_PI_max_d3, depth_PI_min_d3, gate_count_PI_max_d3, gate_count_PI_min_d3 = fake_with_list_max_min_depth_and_gate_count_after_flatten_up_to_depth_each_block_and_optimize(cur_circ, 3)
                
        
        depth_diff_PI_ord_max_d1 = depth_ord_max - depth_PI_max_d1
        depth_diff_PI_ord_min_d1 = depth_ord_min - depth_PI_min_d1
        gate_count_diff_PI_ord_max_d1 = gate_count_ord_max - gate_count_PI_max_d1
        gate_count_diff_PI_ord_min_d1 = gate_count_ord_min - gate_count_PI_min_d1
        
        depth_diff_PI_ord_max_d2 = depth_ord_max - depth_PI_max_d2
        depth_diff_PI_ord_min_d2 = depth_ord_min - depth_PI_min_d2
        gate_count_diff_PI_ord_max_d2 = gate_count_ord_max - gate_count_PI_max_d2
        gate_count_diff_PI_ord_min_d2 = gate_count_ord_min - gate_count_PI_min_d2
        
        depth_diff_PI_ord_max_d3 = depth_ord_max - depth_PI_max_d3
        depth_diff_PI_ord_min_d3 = depth_ord_min - depth_PI_min_d3
        gate_count_diff_PI_ord_max_d3 = gate_count_ord_max - gate_count_PI_max_d3
        gate_count_diff_PI_ord_min_d3 = gate_count_ord_min - gate_count_PI_min_d3        


        vect_y_points_avg_depth_perc_diff_PI_ord_max_d1.append(depth_diff_PI_ord_max_d1 * 100.0 / depth_ord_max)
        vect_y_points_avg_depth_perc_diff_PI_ord_min_d1.append(depth_diff_PI_ord_min_d1 * 100.0 / depth_ord_min)
        vect_y_points_avg_gate_count_perc_diff_PI_ord_max_d1.append(gate_count_diff_PI_ord_max_d1 * 100.0 / gate_count_ord_max)
        vect_y_points_avg_gate_count_perc_diff_PI_ord_min_d1.append(gate_count_diff_PI_ord_min_d1 * 100.0 / gate_count_ord_min)        

        vect_y_points_avg_depth_perc_diff_PI_ord_max_d2.append(depth_diff_PI_ord_max_d2 * 100.0 / depth_ord_max)
        vect_y_points_avg_depth_perc_diff_PI_ord_min_d2.append(depth_diff_PI_ord_min_d2 * 100.0 / depth_ord_min)
        vect_y_points_avg_gate_count_perc_diff_PI_ord_max_d2.append(gate_count_diff_PI_ord_max_d2 * 100.0 / gate_count_ord_max)
        vect_y_points_avg_gate_count_perc_diff_PI_ord_min_d2.append(gate_count_diff_PI_ord_min_d2 * 100.0 / gate_count_ord_min)

        vect_y_points_avg_depth_perc_diff_PI_ord_max_d3.append(depth_diff_PI_ord_max_d3 * 100.0 / depth_ord_max)
        vect_y_points_avg_depth_perc_diff_PI_ord_min_d3.append(depth_diff_PI_ord_min_d3 * 100.0 / depth_ord_min)
        vect_y_points_avg_gate_count_perc_diff_PI_ord_max_d3.append(gate_count_diff_PI_ord_max_d3 * 100.0 / gate_count_ord_max)
        vect_y_points_avg_gate_count_perc_diff_PI_ord_min_d3.append(gate_count_diff_PI_ord_min_d3 * 100.0 / gate_count_ord_min)        
        
    y_points_avg_depth_perc_diff_PI_ord_max_d1.append(list_average(vect_y_points_avg_depth_perc_diff_PI_ord_max_d1))
    y_points_avg_depth_perc_diff_PI_ord_min_d1.append(list_average(vect_y_points_avg_depth_perc_diff_PI_ord_min_d1))
    y_points_avg_gate_count_perc_diff_PI_ord_max_d1.append(list_average(vect_y_points_avg_gate_count_perc_diff_PI_ord_max_d1))
    y_points_avg_gate_count_perc_diff_PI_ord_min_d1.append(list_average(vect_y_points_avg_gate_count_perc_diff_PI_ord_min_d1))
        
    y_points_avg_depth_perc_diff_PI_ord_max_d2.append(list_average(vect_y_points_avg_depth_perc_diff_PI_ord_max_d2))
    y_points_avg_depth_perc_diff_PI_ord_min_d2.append(list_average(vect_y_points_avg_depth_perc_diff_PI_ord_min_d2))
    y_points_avg_gate_count_perc_diff_PI_ord_max_d2.append(list_average(vect_y_points_avg_gate_count_perc_diff_PI_ord_max_d2))
    y_points_avg_gate_count_perc_diff_PI_ord_min_d2.append(list_average(vect_y_points_avg_gate_count_perc_diff_PI_ord_min_d2))
    
    y_points_avg_depth_perc_diff_PI_ord_max_d3.append(list_average(vect_y_points_avg_depth_perc_diff_PI_ord_max_d3))
    y_points_avg_depth_perc_diff_PI_ord_min_d3.append(list_average(vect_y_points_avg_depth_perc_diff_PI_ord_min_d3))
    y_points_avg_gate_count_perc_diff_PI_ord_max_d3.append(list_average(vect_y_points_avg_gate_count_perc_diff_PI_ord_max_d3))
    y_points_avg_gate_count_perc_diff_PI_ord_min_d3.append(list_average(vect_y_points_avg_gate_count_perc_diff_PI_ord_min_d3))
        
plt.plot(x_points, y_points_avg_depth_perc_diff_PI_ord_max_d1, label="max-p-depth, depth_limit=1", linestyle=list_line_style[0])
plt.plot(x_points, y_points_avg_depth_perc_diff_PI_ord_min_d1, label="min-p-depth, depth_limit=1", linestyle=list_line_style[0])

plt.plot(x_points, y_points_avg_depth_perc_diff_PI_ord_max_d2, label="max-p-depth, depth_limit=2", linestyle=list_line_style[1])
plt.plot(x_points, y_points_avg_depth_perc_diff_PI_ord_min_d2, label="min-p-depth, depth_limit=2", linestyle=list_line_style[1])

plt.plot(x_points, y_points_avg_depth_perc_diff_PI_ord_max_d3, label="max-p-depth, depth_limit=3", linestyle=list_line_style[2])
plt.plot(x_points, y_points_avg_depth_perc_diff_PI_ord_min_d3, label="min-p-depth, depth_limit=3", linestyle=list_line_style[2])



plt.legend(loc='center left', bbox_to_anchor=(-0.02, -0.25))
plt.show()
