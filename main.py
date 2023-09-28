# TODO здесь писать код
import re, requests
from typing import List


def find_h3(text: str) -> List:
    """
    Функция для нахождения подзаголовков h3 в html файлах.

    """
    heads = re.findall(r'<h3>.*</h3>', text)
    result = []
    for element in heads:
        result.append(element.replace('<h3>', '').replace('</h3>', ''))
    return result


with open('examples.html', 'r') as f:
    html_example = f.read()
print(find_h3(html_example))

data = requests.get('https://habr.com/ru/companies/wunderfund/articles/683880/')
new_text = data.text
print(find_h3(new_text))


