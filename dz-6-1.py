file = open('nginx_logs.txt')
file_data = []
for line in file:
    line_split = line.split()
    file_data.append((line_split[0], line_split[5].replace('"', ''), line_split[6]))

print(file_data)
