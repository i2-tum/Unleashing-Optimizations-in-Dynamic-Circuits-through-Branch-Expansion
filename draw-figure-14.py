plt.grid()
plt.plot(x_points, y_points_avg_depth_perc_diff_PI_ord_max, label="Percentage decrease in max-p-depth")
plt.plot(x_points, y_points_avg_depth_perc_diff_PI_ord_min, label="Percentage decrease in min-p-depth")

plt.legend()
plt.show()
