import requests


def currency_rates(ccy):
    ccy = ccy.upper()
    currency_res = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    res_ccy = currency_res.text
    ccy_start = res_ccy.find(ccy)
    if ccy_start == -1:
        print(f'None {ccy}')
    else:
        req_str_ccy = res_ccy[ccy_start:]
        ccy_value_st = req_str_ccy.find('<Value>')
        ccy_value_end = req_str_ccy.find('</Value>')
        ccy_value = req_str_ccy[(ccy_value_st+7):ccy_value_end]
        ccy_value = float(ccy_value[:ccy_value.find(',')] + '.' + ccy_value[ccy_value.find(',') + 1:])
        nom_value_st = req_str_ccy.find('<Nominal>')
        nom_value_end = req_str_ccy.find('</Nominal>')
        nominal = int(req_str_ccy[(nom_value_st + 9):nom_value_end])
        print(nominal, ccy, '=', ccy_value, 'RUB')
                

currency_rates('UZS')
currency_rates('USD')
currency_rates('GBP')
currency_rates('Eur')
currency_rates('aasd')
