plt.grid()

plt.plot(x_points, y_points_avg_gate_count_perc_diff_PI_ord_max_d1, label="max-p-gate-count, depth_limit=1", linestyle=list_line_style[0])
plt.plot(x_points, y_points_avg_gate_count_perc_diff_PI_ord_min_d1, label="min-p-gate-count, depth_limit=1", linestyle=list_line_style[0])

plt.plot(x_points, y_points_avg_gate_count_perc_diff_PI_ord_max_d2, label="max-p-gate-count, depth_limit=2", linestyle=list_line_style[1])
plt.plot(x_points, y_points_avg_gate_count_perc_diff_PI_ord_min_d2, label="min-p-gate-count, depth_limit=2", linestyle=list_line_style[1])

plt.plot(x_points, y_points_avg_gate_count_perc_diff_PI_ord_max_d3, label="max-p-gate-count, depth_limit=3", linestyle=list_line_style[2])
plt.plot(x_points, y_points_avg_gate_count_perc_diff_PI_ord_min_d3, label="min-p-gate-count, depth_limit=3", linestyle=list_line_style[2])

plt.legend(loc='center left', bbox_to_anchor=(-0.02, -0.25))
plt.show()
