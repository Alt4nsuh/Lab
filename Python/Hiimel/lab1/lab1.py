day_1 = ["home ","school", "restaurant", "home", "school"]
day_2 = ["home", "school", "restaurant", "home"]
day_3 = ["home", "school", "restaurant", "home"]
day_4 = ["home", "school", "restaurant", "home"]

days = day_1 + day_2 + day_3 + day_4

b = []

for i in range(len(days)-1):
    a = days[i] +" "+ days[i+1]
    b.append(a)

print(b)

unique_locations = set(b)

for i in unique_locations:
    print(f"{i}: {b.count(i)}")
