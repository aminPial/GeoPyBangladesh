import requests
from bs4 import BeautifulSoup
import json

response = requests.get(
    'http://www.bangladesh.gov.bd/site/view/upazila-list/%E0%A6%89%E0%A6%AA%E0%A6%9C%E0%A7%87%E0%A6%B2%E0%A6%BE%E0%A6%B8%E0%A6%AE%E0%A7%82%E0%A6%B9')
soup = BeautifulSoup(response.text, "lxml")
parent_element = soup.find('div', {'id': 'printable_area'})

tables = parent_element.find_all('table', {'class': 'geotable'})
divisions = parent_element.find_all('strong', {'class': 'div-wise-upz'})

geo_data = {}

for division_name, zilla_row in zip(divisions, tables):
    division_name = division_name.text.strip()

    for row in zilla_row.find_all('tr'):
        zilla_name = None
        upazillas = None
        for idx, tds in enumerate(row.find_all('td')):
            if idx == 0:
                zilla_name = tds.text.strip()
            else:
                upazillas = list(set([_.strip() for _ in tds.text.split(",") if _ != '\n']))

        if division_name and zilla_name and upazillas:
            if division_name not in geo_data:
                geo_data[division_name] = {}
            geo_data[division_name][zilla_name] = upazillas

with open('geodata.json', 'w', encoding='utf-8') as f:
    json.dump(geo_data, f, ensure_ascii=False, indent=4)
