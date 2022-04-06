# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# ыбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  ...
#    raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re
import traceback

e_mail1 = 'someone3@geekbrains.ru'
e_mail2 = 'som№eone@geekbrainsru'
e_mail3 = 'someonegeekbrainsru'
e_mail4 = 'd.m.aleksandrov@yandex.ru'
e_mail5 = 'd.m.##aleksandrov@yandex.ru'


def email_parse(email_address):
    my_dict = []
    return_dict_email = {}
    error_symbol_1 = []
    msg = 'wrong email:'
    pattern = re.compile('(?P<username>.+)@(?P<domain>\w+)\.(?P<domain_zone>.+)')
    all_result = pattern.finditer(email_address)
    for res in all_result:
        my_dict = res.groupdict()
    pattern = re.compile(r'[#~$%!=,№&\s]')  # ищу дополнительные недопустимые симовлы
    error_symbol_1 = pattern.findall(email_address)
    try:
        if len(error_symbol_1) == 0:
            # print('нет недопустимых символов')
            if len(my_dict) == 0:
                raise ValueError
            else:
                return_dict_email['username'] = my_dict.get('username')
                return_dict_email['domain'] = my_dict.get('domain') + '.' + my_dict.get('domain_zone')
                print(return_dict_email)
        else:
            raise ValueError
    except (IOError, ValueError) as er:
        print(traceback.format_exc() + msg + email_address)
    if len(return_dict_email) > 0:
        return return_dict_email


email_parse(e_mail1)
email_parse(e_mail2)
#email_parse(e_mail3)
email_parse(e_mail4)
#email_parse(e_mail5)
