## Project: Data Explorer
## Research Question: How will daily high temperatures change over the days July 16-22, 2026 in Bothell, WA?
 
## Data source: WeatherForYou.com, "Bothell, WA 98011 7 Day Weather Forecast" https://www.weatherforyou.com/report/bothell-wa/metric

import matplotlib.pyplot as plt
 
## python list
days = ["Thu 7/16", "Fri 7/17", "Sat 7/18", "Sun 7/19", "Mon 7/20", "Tue 7/21", "Wed 7/22"]
high_temps = [75, 79, 79, 82, 86, 90, 88]
 
# this part is the line graph, showing an increasing line then a slight dip at the end
plt.figure(figsize=(8, 5))
plt.plot(days, high_temps, marker="o", color="darkorange")
plt.title("Daily High Temperatures in Bothell, WA (Jul 16-22, 2026)")
plt.xlabel("Day")
plt.ylabel("High Temperature (F)")
plt.grid(True)
plt.tight_layout()
plt.savefig("temperature_trend.png")
plt.show()
 
# stats
mean_temp = sum(high_temps) / len(high_temps)
sorted_temps = sorted(high_temps)
n = len(sorted_temps)
median_temp = (sorted_temps[n // 2] if n % 2 == 1
               else (sorted_temps[n // 2 - 1] + sorted_temps[n // 2]) / 2)
 
print(f"Mean high temperature: {mean_temp:.1f}F")
print(f"Median high temperature: {median_temp}F")
print(f"Mode high temperature: {max(set(high_temps), key=high_temps.count)}F") 