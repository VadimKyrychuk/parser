import requests
from bs4 import BeautifulSoup as BS

URL = 'https://allo.ua/ua/products/mobile/proizvoditel-xiaomi/'
response_main_page = requests.get(URL)
bs_main_page = BS(response_main_page.text, 'lxml')
pagination = int(bs_main_page.find('div', class_='pagination').text.split()[-1])  # get last page
pagination_link = bs_main_page.find('div', class_='pagination').find('ul', class_='pagination__list').find('li'). \
    find('a').get('href')  # get firts link of pagination
links_phone = []
for i in range(1, pagination + 1):
    if i != 1:
        pagination_link = pagination_link.replace(str(i - 1), str(i))
    temp_page = requests.get(pagination_link)
    bs_page = BS(temp_page.text, 'lxml')
    try:
        ls_links_phones = bs_page.find('div', class_='products-layout__container products-layout--grid').find_all('div',
                                                                                                                  class_='product-card__img')
        for link in ls_links_phones: # get links phone
            temp_result = link.find('a', class_='img-carousel').get('href')
            if temp_result:
                links_phone.append(temp_result)
    except Exception:
        print('Error')

for phone in links_phone:
    print(phone)