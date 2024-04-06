from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Пример принятия POST запроса
@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    # Здесь можно обработать полученные данные
    response = {"message": "Данные успешно обработаны"}
    return jsonify(response)



# Пример отправки POST запроса
def send_post_request(serverURL: str = 'http://vin320il.beget.tech/process_data', value: str = '', debug: bool = False):
    print('Подготовка запроса') if debug else None
    url = serverURL
    data = {'value': value}  # Создаем словарь с данными
    jsonData = json.dumps(data)  # Преобразуем данные в формат JSON

    response = requests.post(url, json=jsonData)  # Отправляем POST запрос на сервер

    if response.status_code == 200:
        print('Запрос успешно отправлен') if debug else None
    else:
        print('Произошла ошибка при отправке запроса') if debug else None


app.run()

# import requests
# import time

# while True:
#     url = 'http://vin320il.beget.tech/index.html'
#     data = {'value': 'Ping'}
#     response = requests.post(url, json=data)

#     print(response.text)
#     time.sleep(2)

if __name__ == '__main__':
    while True:
        a = input('Введите запрос: ')
        send_post_request(value=a, debug=True)