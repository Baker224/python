import re


file = open('nginx_logs.txt')
for line in file:
    file_data = []
    try:
        remote_addr = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
        file_data.append(remote_addr[0])
    except:
        # remote_addr = 'ipv6'
        remote_addr = re.search(r'([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|', line)
        file_data.append(remote_addr[0])
    request_datetime = re.search(r'\d{2}\D{5}\d{4}\D\d{2}\D\d{2}\D\d{2} \+\d{4}', line)
    request_type = re.search(r'[A-Z]{3,8}', line)
    requested_resource = re.search(r'\D{19}\d', line)
    response_code = re.search(r'[1-5][0-9][0-9]', line)
    response_size = re.search(r'\d{1,} "', line)

    file_data.append(request_datetime[0])
    file_data.append(request_type[0])
    file_data.append(requested_resource[0])
    file_data.append(response_code[0])
    response_size = response_size[0]
    response_size = response_size[0:-2]
    file_data.append(response_size)
    print(file_data)

