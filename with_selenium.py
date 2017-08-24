from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re


browser = webdriver.Chrome()
browser.get('http://seal100x.github.io/nikkiup2u3/')

theme_selector = browser.find_element_by_id('theme')
select = webdriver.support.ui.Select(theme_selector)
item_dict = {}

for i in range(1,len(select.options)):
    select.select_by_index(i)
    browser.find_element_by_id('onekey').click()

    one_key_strategy = browser.find_element_by_class_name('strategy_info_div')
    stgy_clothes_list_raw = one_key_strategy.find_elements_by_class_name('stgy_clothes')
    stgy_clothes_list = list(map(lambda item: item.text, stgy_clothes_list_raw))

    for entry in stgy_clothes_list:
        item_string = re.sub('.+: ', '', entry)
        item_sublist = re.split('> |>> |= ', item_string)
        item_max_score = 0
        for item in item_sublist:
            item_score = int(re.search('[0-9]+', item).group())
            if item_max_score == 0:
                item_max_score = item_score
            item_score = round(item_score/item_max_score, 3)
            item_name = re.sub('「.+」', '', item)
            item_dict[item_name] = round(item_dict.get(item_name, 0) + item_score, 3)

sorted_item = [(k, item_dict[k]) for k in sorted(item_dict, key = item_dict.get, reverse=True)]
# print(str(sorted_item))

with open('result.txt', 'w') as output:
    output.write(str(sorted_item[:1000]))
