average_size = 100
num_qubits = 3

num_depths = 5

num_blocks_min = 1
num_blocks_max = 10
optimization_strength = 3
x_points = []

y_points_avg_ord_depth_max = []
y_points_avg_ord_depth_min = []
y_points_avg_ord_gate_count_max = []
y_points_avg_ord_gate_count_min = []

y_points_avg_PI_depth_max = []
y_points_avg_PI_depth_min = []
y_points_avg_PI_gate_count_max = []
y_points_avg_PI_gate_count_min = []



y_points_avg_depth_perc_diff_PI_ord_max = []
y_points_avg_depth_perc_diff_PI_ord_min = []
y_points_avg_gate_count_perc_diff_PI_ord_max = []
y_points_avg_gate_count_perc_diff_PI_ord_min = []


for b in range(num_blocks_min, num_blocks_max + 1):
    
    print("Progress report:", end = ' ')
    print("Calculating the", b, end='')
    print("-th case.", end="\r")
    
    
    x_points.append(b)
    
    vect_y_points_avg_ord_depth_max = []
    vect_y_points_avg_ord_depth_min = []
    vect_y_points_avg_ord_gate_count_max = []
    vect_y_points_avg_ord_gate_count_min = []
    
    vect_y_points_avg_PI_depth_max = []
    vect_y_points_avg_PI_depth_min = []
    vect_y_points_avg_PI_gate_count_max = []
    vect_y_points_avg_PI_gate_count_min = []
    
    

    
    vect_y_points_avg_depth_perc_diff_PI_ord_max = []
    vect_y_points_avg_depth_perc_diff_PI_ord_min = []
    vect_y_points_avg_gate_count_perc_diff_PI_ord_max = []
    vect_y_points_avg_gate_count_perc_diff_PI_ord_min = []
    
    for t in range(average_size):
        depth_ord_max, depth_ord_min, gate_count_ord_max, gate_count_ord_min, depth_PI_max, depth_PI_min, gate_count_PI_max, gate_count_PI_min = experiment_on_pattern_one(num_qubits, num_depths, b, optimization_strength)
        vect_y_points_avg_ord_depth_max.append(depth_ord_max)
        vect_y_points_avg_ord_depth_min.append(depth_ord_min)
        vect_y_points_avg_ord_gate_count_max.append(gate_count_ord_max)
        vect_y_points_avg_ord_gate_count_min.append(gate_count_ord_min)
        vect_y_points_avg_PI_depth_max.append(depth_PI_max)
        vect_y_points_avg_PI_depth_min.append(depth_PI_min)
        vect_y_points_avg_PI_gate_count_max.append(gate_count_PI_max)
        vect_y_points_avg_PI_gate_count_min.append(gate_count_PI_min)

        
        depth_diff_PI_ord_max = depth_ord_max - depth_PI_max
        depth_diff_PI_ord_min = depth_ord_min - depth_PI_min
        gate_count_diff_PI_ord_max = gate_count_ord_max - gate_count_PI_max
        gate_count_diff_PI_ord_min = gate_count_ord_min - gate_count_PI_min
        

        
        vect_y_points_avg_depth_perc_diff_PI_ord_max.append(depth_diff_PI_ord_max * 100.0 / depth_ord_max)
        vect_y_points_avg_depth_perc_diff_PI_ord_min.append(depth_diff_PI_ord_min * 100.0 / depth_ord_min)
        vect_y_points_avg_gate_count_perc_diff_PI_ord_max.append(gate_count_diff_PI_ord_max * 100.0 / gate_count_ord_max)
        vect_y_points_avg_gate_count_perc_diff_PI_ord_min.append(gate_count_diff_PI_ord_min * 100.0 / gate_count_ord_min)
    

    y_points_avg_ord_depth_max.append(list_average(vect_y_points_avg_ord_depth_max))
    y_points_avg_ord_depth_min.append(list_average(vect_y_points_avg_ord_depth_min))
    y_points_avg_ord_gate_count_max.append(list_average(vect_y_points_avg_ord_gate_count_max))
    y_points_avg_ord_gate_count_min.append(list_average(vect_y_points_avg_ord_gate_count_min))
    y_points_avg_PI_depth_max.append(list_average(vect_y_points_avg_PI_depth_max))
    y_points_avg_PI_depth_min.append(list_average(vect_y_points_avg_PI_depth_min))
    y_points_avg_PI_gate_count_max.append(list_average(vect_y_points_avg_PI_gate_count_max))
    y_points_avg_PI_gate_count_min.append(list_average(vect_y_points_avg_PI_gate_count_min))

    y_points_avg_depth_perc_diff_PI_ord_max.append(list_average(vect_y_points_avg_depth_perc_diff_PI_ord_max))
    y_points_avg_depth_perc_diff_PI_ord_min.append(list_average(vect_y_points_avg_depth_perc_diff_PI_ord_min))
    y_points_avg_gate_count_perc_diff_PI_ord_max.append(list_average(vect_y_points_avg_gate_count_perc_diff_PI_ord_max))
    y_points_avg_gate_count_perc_diff_PI_ord_min.append(list_average(vect_y_points_avg_gate_count_perc_diff_PI_ord_min))
