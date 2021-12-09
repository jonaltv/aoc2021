f = open("input.txt", "r")
line = f.readlines()

total_increases = 0
previous_total = 0
current_value = [0,0,0]

for i in line:
    current_value[2] = current_value[1]
    current_value[1] = current_value[0]
    current_value[0] = int(i)
    current_total = current_value[0] + current_value[1] + current_value[2]
    if current_value[2] != 0:
        if current_total > previous_total and previous_total != 0:
            total_increases += 1
        previous_total = current_total

print("Total increases = %s" % total_increases)

f.close()