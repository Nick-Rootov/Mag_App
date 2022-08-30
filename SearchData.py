import requests, zipfile, io, re, json, os
from bs4 import BeautifulSoup
import pandas as pd

def SearchDTP(year_dtp, month):
    month_number_list_dtp = {
        'январь': '1',
        'февраль': '2',
        'март': '3',
        'апрель': '4',
        'май': '5',
        'июнь': '6',
        'июль': '7',
        'август': '8',
        'сентябрь': '9',
        'октябрь': '10',
        'ноябрь': '11',
        'декабрь': '12'
    }
    month_name_list_dtp = {
        '1': 'january',
        '2': 'february',
        '3': 'march',
        '4': 'april',
        '5': 'may',
        '6': 'june',
        '7': 'july',
        '8': 'august',
        '9': 'september',
        '10': 'october',
        '11': 'nivember',
        '12': 'december'
    }
    month_number_dtp = month_number_list_dtp[month]
    month_name_dtp = month_name_list_dtp[month_number_dtp]
    # year_dtp = '2021'
    cards_dict = {"data": {"date": [f"MONTHS:{month_number_dtp}.{year_dtp}"], "ParReg": "71100", "order": {"type": "1", "fieldName": "dat"},
                           "reg": "71118", "ind": "1", "st": "1", "en": "16"}}
    cards_dict["data"]["ParReg"] = "56"  # Пензенская область
    cards_dict["data"]["reg"] = "56255"  # район Пензенский район
    cards_dict["data"]["st"] = "1"  # первая карточка
    cards_dict["data"]["en"] = "50"  # последняя карточка
    cards_dict_json = {}
    cards_dict_json["data"] = json.dumps(cards_dict["data"], separators=(',', ':')).encode('utf8').decode(
        'unicode-escape')  # вот так мы упаковываем данные в строку

    r = requests.post("http://stat.gibdd.ru/map/getDTPCardDataXML", json=cards_dict_json)  # ссылка на команду + настроечные данные к ней
    number = r.text

    value = re.sub('["{}°С+/мрс. %dat:]', '', number)
    url = 'http://stat.gibdd.ru/getPDFbyId?data=' + value

    get_data = requests.get(url, allow_redirects=True)
    z = zipfile.ZipFile(io.BytesIO(get_data.content))
    z.extractall('data')
    try:
        os.remove(f'data/dtp_{month_name_dtp}_{year_dtp}.xml')
    except:
        print('Папка уже создана')
    os.rename('data/Список карточек ДТП.xml', f'data/dtp_{month_name_dtp}_{year_dtp}.xml')


def SearchWeatherInfo(year_weather,month):
    month_list_weather = {
        'январь': 'yanvar',
        'февраль': 'fevral',
        'март': 'mart',
        'апрель': 'aprel',
        'май': 'may',
        'июнь': 'iun',
        'июль': 'iul',
        'август': 'avgust',
        'сентябрь': 'sentyabr',
        'октябрь': 'oktyabr',
        'ноябрь': 'noyabr',
        'декабрь': 'dekabr'
    }
    month_name_list_weather = {
        'январь': 'january',
        'февраль': 'february',
        'март': 'march',
        'апрель': 'april',
        'май': 'may',
        'июнь': 'june',
        'июль': 'july',
        'август': 'august',
        'сентябрь': 'september',
        'октябрь': 'october',
        'ноябрь': 'nivember',
        'декабрь': 'december'
    }
    # функция удаления ненужных символов в строке с НУЖНЫМ числом
    def to_num(temp):
        value = re.sub('[°С+/мрс. %]', '', temp)
        return float(value)

    # функция формирования ссылки и получения HTML-кода страницы
    def get_url(month, year):
        # поиск в определённой зоне
        url = 'https://ya-pogoda.ru/pogoda/' + month + '-' + year + '/penza/'

        # делаем запрос и получаем html
        html_text = requests.get(url).text

        # используем парсер lxml
        soup = BeautifulSoup(html_text, 'lxml')
        return soup

    month_code_weather = month_list_weather[month]
    month_name_weather = month_name_list_weather[month]
    #month_weather = input('Введите месяц: ')
    #year_weather = input('Введите год: ')

    map = {}
    id = 0

    # получаем все элементы
    days = get_url(month_code_weather, year_weather).find_all('div', class_='description')
    common_len = 0
    old_common_len = 4
    old_dop_info = '0%'
    for i in range(len(days)):
        day = days[i]
        x = day['class']
        if (len(x) == 2):
            continue
        id += 1
        map[id] = {}
        common = {}
        dop_info = day.find_all('p')
        common_len = len(dop_info)
        if old_common_len > common_len:
            common[common_len] = old_dop_info
        else:
            old_dop_info = dop_info[common_len - 1].string

        for j in range(common_len):
            # находим общие данные,скорость ветра,кол-во осадков,относительную влажность
            common[j] = dop_info[j].string

        # находим максимальную температуру
        max_temperature = day.find('div', class_='night tr-12').string
        # находим минимальную температуру
        min_temperature = day.find('div', class_='day tr-07').string
        # записываем данные в словарь
        map[id]["max_temperature"] = int(to_num(max_temperature))
        map[id]["min_temperature"] = int(to_num(min_temperature))
        if old_common_len > common_len:
            common_len = old_common_len

        for j in range(common_len):
            if j == 0:
                map[id]['common' + str(j)] = common[j]
                continue
            map[id]["common" + str(j)] = int(to_num(common[j]))

        old_common_len = common_len

    # преобразуем словарь в список списков
    common_len = 4
    result = []
    cur_common = {}
    cur_row = 0
    for id in map.keys():
        cur_max_temperature = map[id]["max_temperature"]
        cur_min_temperature = map[id]["min_temperature"]
        for idj in range(common_len):
            cur_common[idj] = map[id]["common" + str(idj)]
        result.append([])
        result[cur_row].append(cur_max_temperature)
        result[cur_row].append(cur_min_temperature)
        for idj in range(common_len):
            result[cur_row].append(cur_common[idj])
        cur_row += 1

    # преобразование в датафрейм
    df = pd.DataFrame(result, columns=['Максимальная температура, °С', 'Минимальная температура, °С', 'Состояние',
                                       'Скорость ветра, м/c', 'Кол-во осадков, мм р.с.', 'Относительная влажность, %'])
    df.index += 1

    # экспорт в csv
    filename_csv = month_name_weather + '_' + year_weather + '.csv'
    try:
        os.mkdir("data")
    except:
        print('Папка уже создана')
    finally:
        df.to_csv(f'data/weather_{filename_csv}',index= False, encoding="utf-8-sig")
    # экспорт в xlsx
    df = pd.read_csv(f'data/weather_{filename_csv}')
    filename_xlsx = month_name_weather + '_' + year_weather + '.xlsx'
    df.to_excel(f'data/weather_{filename_xlsx}',index= False, encoding='utf8')
    return (f'data/weather_{filename_xlsx}')
