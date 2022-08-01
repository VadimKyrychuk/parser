import requests
from bs4 import BeautifulSoup as BS

URL = 'https://www.ctrs.com.ua/noutbuki-i-ultrabuki/brand-dell/'
response_main_page = requests.get(URL)
bs_main_page = BS(response_main_page.text, 'lxml')
# print(bs_main_page)
print(requests.get('https://www.ctrs.com.ua/noutbuki-i-ultrabuki/brand-dell/page_8/'))