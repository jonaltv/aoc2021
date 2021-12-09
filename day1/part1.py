f = open("input.txt", "r")
line = f.readlines()

total_increases = 0
previous_value = 0

for i in line:
    current_value = int(i)
    if current_value > previous_value and previous_value != 0:
        total_increases += 1
    previous_value = current_value

print("Total increases = %s" % total_increases)

f.close()