import re


def email_parse(email):
    regular_email = re.compile(r'^([A-Za-z0-9]+[.|_|-])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})$')
    regular_domain = re.compile(r'@+[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')
    list_email = []
    dict_email = {}
    msg = f'Wrong email: {email}'
    if re.fullmatch(regular_email, email):
        list_email.append(email.split('@')[0])
        list_email.append(email.split('@')[1])
        i = 0
        while i < len(list_email):
            dict_email['username'] = list_email[i]
            dict_email['domain'] = list_email[i + 1]
            i += 2
        print(dict_email)
    else:
        if not re.search(regular_domain, email):
            raise ValueError(msg)
        else:
            print('username not valid')


email_parse('matt_baker@mail.ru')
email_parse('name.surname@gmail.com')
email_parse('name.surname@gmailcom')
email_parse('name_surname@gmailcom')

