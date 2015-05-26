import json
import requests
import bs4
import time
from selenium import webdriver


recipe_index = 1
result = []

browser = webdriver.Firefox()


for page in range(1, 700 + 1):
    browser.get('http://www.food.com/recipe/all/popular?pn=' + str(page))
    source = browser.page_source

    soup = bs4.BeautifulSoup(source)
    links = soup.select('.details .title a')

    urls = [a.attrs.get('href') for a in links]

    print('Downloaded recipe list ' + str(page))

    for url in urls:
        try:
            current_recipe = {}
            recipe_page_html = requests.get(url)
            recipe_page = bs4.BeautifulSoup(recipe_page_html.text)

            title = recipe_page.select('.recipe h1')[0].text
            current_recipe['name'] = title

            ingredients = recipe_page.select('.ingredients ul')[0].text
            current_recipe['products'] = ingredients.strip()

            prepare_element = recipe_page.select('.total-time span')
            if len(prepare_element) == 0:
                continue
            prepare_time = prepare_element[0].text
            current_recipe['prepare_time'] = prepare_time

            total_fat = float(recipe_page.select('.nutrition .fat')[0].text)
            current_recipe['total_fat'] = total_fat

            protein = float(recipe_page.select('.nutrition .protein')[0].text)
            current_recipe['protein'] = protein

            servings_elements = recipe_page.select('.servings .value')
            if len(servings_elements) == 0:
                continue
            servings_text = recipe_page.select('.servings .value')[0].text
            try:
                servings = int(servings_text)
            except ValueError:
                try:
                    servings = int(servings_text.split('-')[0])
                except:
                    print('could not parse servings text ' + servings_text)
                    continue
            current_recipe['servings'] = servings

            instructions = recipe_page.select('.directions ol')[0].text
            current_recipe['instructions'] = instructions.strip()

            image = recipe_page.select('.trans-img img')[0]["data-src"]
            current_recipe['image'] = image

            result.append(current_recipe)
            print('saved recipe ' + str(recipe_index))
            recipe_index += 1
        except Exception as e:
            print(e)
            continue

    time.sleep(1)

    with open('popular-1-' + str(page) + '.json', 'w') as current_file:
        json.dump(result, current_file, indent=True, ensure_ascii=False)


with open('crawl_food.json', 'w') as f:
    json.dump(result, f, indent=True, ensure_ascii=False)

browser.quit()
