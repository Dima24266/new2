result = {}

with open('CAM_table.txt') as f:
    for line in f:
        line = line.split(' ')
        if line and line[1][0].isdigit():
            vlan, address, *other = line
            result[vlan] = address
print(result)
