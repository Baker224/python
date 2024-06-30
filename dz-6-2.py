file = open('nginx_logs.txt')
file_data = []
ip_data = {}
for line in file:
    line_split = line.split()
    file_data.append((line_split[0], line_split[5].replace('"', ''), line_split[6]))
    ip_data.setdefault(line_split[0], 0)
    ip_data[line_split[0]] += 1

max_spam = max(ip_data.items(), key=lambda x: x[1])
print(max_spam)



