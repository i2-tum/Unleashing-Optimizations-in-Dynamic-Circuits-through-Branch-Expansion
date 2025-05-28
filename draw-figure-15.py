plt.grid()
plt.plot(x_points, y_points_avg_gate_count_perc_diff_PI_ord_max, label="Percentage decrease in max-p-gate-count")
plt.plot(x_points, y_points_avg_gate_count_perc_diff_PI_ord_min, label="Percentage decrease in min-p-gate-count")

plt.legend()
plt.show()
