# установить библиотеки pytest, requests
# pip install pytest requests
# запустить файл с флагами -v и -s
# pytest -v -s path/to/folder/with/file/test_2gis.py

import requests

URL = "https://regions-test.2gis.com/1.0/regions"

# Тест параметра 'q' по свойствам "Регистр не имеет значения" и "Минимум - 3 символа"
def test_q1():
    response = requests.get(f"{URL}?q=мос")
    response_json = response.json()
    assert response_json == {'total': 22, 'items': [{'id': 32, 'name': 'Москва', 'code': 'moscow', 'country': {'name': 'Россия', 'code': 'ru'}}]}, 'Тест параметра "q" по свойствам "Регистр не имеет значения" и "Минимум - 3 символа" провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'q' по свойству "Если передан этот параметр, то все остальные параметры игнорируются"
def test_q2():
    response = requests.get(f"{URL}?q=москва&country_code=us&page=10&page_size=0")
    response_json = response.json()
    assert response_json == {'total': 22, 'items': [{'id': 32, 'name': 'Москва', 'code': 'moscow', 'country': {'name': 'Россия', 'code': 'ru'}}]}, 'Тест параметра "q" по свойству "Если передан этот параметр, то все остальные параметры игнорируются" провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа {response.status_code}"

# Тест параметра 'q' по свойству "Минимум - 3 символа"
def test_q3():
    response = requests.get(f"{URL}?q=м_")
    response_json = response.json()
    assert response_json['error']['message'] == "Параметр 'q' должен быть не менее 3 символов", 'Тест параметра "q" по свойству "Минимум - 3 символа" провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'country_code' со значением 'ru'
def test_cc1():
    response = requests.get(f"{URL}?country_code=ru")
    response_json = response.json()
    len_items = len(response_json['items'])
    list1 = []
    for i in range(0,len_items):
        if response_json['items'][i]['country']['code'] != "ru":
            list1.append(response_json['items'][i]['country']['code'])
    assert len(list1) == 0, 'Тест параметра "country_code" со значением "ru" провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'country_code' со значением 'kg'
def test_cc2():
    response = requests.get(f"{URL}?country_code=kg")
    response_json = response.json()
    len_items = len(response_json['items'])
    list1 = []
    for i in range(0, len_items):
        if response_json['items'][i]['country']['code'] != "kg":
            list1.append(response_json['items'][i]['country']['code'])
    assert len(list1) == 0, 'Тест параметра "country_code" со значением "kg" провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'country_code' со значением 'kz'
def test_cc3():
    response = requests.get(f"{URL}?country_code=kz")
    response_json = response.json()
    len_items = len(response_json['items'])
    list1 = []
    for i in range(0, len_items):
        if response_json['items'][i]['country']['code'] != "kz":
            list1.append(response_json['items'][i]['country']['code'])
    assert len(list1) == 0, 'Тест параметра "country_code" со значением "kz" провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'country_code' со значением 'сz'
def test_cc4():
    response = requests.get(f"{URL}?country_code=cz")
    response_json = response.json()
    len_items = len(response_json['items'])
    list1 = []
    for i in range(0, len_items):
        if response_json['items'][i]['country']['code'] != "cz":
            list1.append(response_json['items'][i]['country']['code'])
    assert len(list1) == 0, 'Тест параметра "country_code" со значением "cz" провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'country_code' со значением 'ua'
def test_cc5():
    response = requests.get(f"{URL}?country_code=ua")
    response_json = response.json()
    assert response_json['error']['message'] == "Параметр 'country_code' может быть одним из следующих значений: ru, kg, kz, cz", 'Тест параметра "country_code" со значением ua провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'country_code' со значением '1;_%ъ'
def test_cc6():
    response = requests.get(f"{URL}?country_code=1;_%ъ")
    response_json = response.json()
    assert response_json['error']['message'] == "Параметр 'country_code' может быть одним из следующих значений: ru, kg, kz, cz", 'Тест параметра "country_code" со значением 1;_%ъ провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'country_code' по свойству "По умолчанию отображаются регионы из всех стран"
def test_cc7():
    response = requests.get(URL)
    response_json = response.json()
    len_items = len(response_json['items'])
    list1 = []
    for i in range(0, len_items):
        list1.append(response_json['items'][i]['country']['code'])
    assert "ru" and "kz" and "kg" and "cz" in list1, 'Тест параметра "country_code" по свойству "По умолчанию отображаются регионы из всех стран" провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'page_size' со значением  5
def test_ps1():
    k = 5
    response = requests.get(f"{URL}?page_size={k}")
    response_json = response.json()
    len_items = len(response_json['items'])
    assert len_items == k, f'Тест параметра "page_size" со значением {k} провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'page_size' со значением 10
def test_ps2():
    k = 10
    response = requests.get(f"{URL}?page_size={k}")
    response_json = response.json()
    len_items = len(response_json['items'])
    assert len_items == k, f'Тест параметра "page_size" со значением {k} провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'page_size' со значением 15
def test_ps3():
    k = 15
    response = requests.get(f"{URL}?page_size={k}")
    response_json = response.json()
    len_items = len(response_json['items'])
    assert len_items != k, f'Тест параметра "page_size" со значением {k} провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'page_size' со значением 20
def test_ps4():
    k = 20
    response = requests.get(f"{URL}?page_size={k}")
    response_json = response.json()
    assert response_json['error']['message'] == "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15", 'Тест параметра "page_size" со значением 20 провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'page_size' со значением -5
def test_ps5():
    k = -5
    response = requests.get(f"{URL}?page_size={k}")
    response_json = response.json()
    assert response_json['error']['message'] == "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15", 'Тест параметра "page_size" со значением -5 провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметров 'page_size' и 'page' со значениями по умолчанию
def test_psp1():
    response = requests.get(f"{URL}?page_size=15&page=1")
    response_json = response.json()
    len_items = len(response_json['items'])
    assert len_items != 15, f'Тест параметров "page_size" и "page" со значениями по умолчанию провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'page_size' со значением 5 и параметра 'page' со значением 3
def test_psp2():
    response = requests.get(f"{URL}?page_size=5&page=3")
    response_json = response.json()
    len_items = len(response_json['items'])
    assert len_items == 0, 'Тест параметра "page_size" со значением 5 и параметра "page" со значением 3 провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметра 'page_size' со значением 10 и параметра 'page' со значением 2
def test_psp3():
    response = requests.get(f"{URL}?page_size=10&page=2")
    response_json = response.json()
    len_items = len(response_json['items'])
    print(len_items)
    assert len_items == 0, 'Тест параметра "page_size" со значением 10 и параметра "page" со значением 2 провален'
    assert response.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"

# Тест параметров country_code=ru,page_size=5, page=1
def test_ccpsp1():
    response = requests.get(URL)
    response_json = response.json()
    list1 = []
    len_items = len(response_json['items'])
    for i in range(0,len_items):
        if response_json['items'][i]['country']['code'] == "ru":
            list1.append(response_json['items'][i]['name'])
    assert len(list1) != 0, f"Тест параметров country_code=ru,page_size=5, page=1 провален. Запрос работу страницы {URL}"
    # print(list1)
    response2 = requests.get(f"{URL}?country_code=ru&page_size=5&page=1")
    response_json2 = response2.json()
    len_items2 = len(response_json2['items'])
    list2 = []
    for i in range(0, len_items2):
        if response_json2['items'][i]['country']['code'] == "ru":
            list2.append(response_json2['items'][i]['name'])
    # print(list2)
    list3 = []
    for i in list2:
        try:
            list1.remove(i)
        except ValueError:
            list3.append(i)
    # print(list3)
    assert len(list2) != 0, "Тест параметров country_code=ru,page_size=5, page=1 провален по причине некорректной работы одного из них"
    assert len(list3) == 0, f"Тест параметров country_code=ru,page_size=5, page=1 провален, т.к. в ответе сервера появились новые элементы: {','.join(list3)}"
    assert response2.status_code == 200, f"Это не код ответа 200. Полученный код ответа - {response.status_code}"