import time
import json
import os
import requests
import uuid

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


if __name__ == '__main__':
    data = []

    # driver = webdriver.Chrome('./chromedriver')  # old style
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_position(0, 0)
    driver.maximize_window()

    driver.get('https://www.emag.ro/')
    # time.sleep(30)

    top_categories = driver.find_elements(by=By.XPATH, value='//*[contains(@class, "js-megamenu-list-department-link")]')
    for top_category in top_categories:
        top_category_data = {
            "name": top_category.text,
            "main_subcategories": []
        }

        hover_action = ActionChains(driver).move_to_element(top_category)
        hover_action.perform()

        visible_menu_container = driver.find_element(By.XPATH, '//*[contains(@class, "megamenu-visible")]')
        # visible_menu_container = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[contains(@class, "megamenu-visible")]'))

        main_subcategories_data = []
        list_items = visible_menu_container.find_elements(By.XPATH, '//li[@class="megamenu-column"]')
        for list_item in list_items:
            main_subcategories_elements = list_item.find_elements(By.XPATH, '*[contains(@class, "megamenu-item-heading")]')
            category_containers = list_item.find_elements(By.XPATH, '*[contains(@class, "megamenu-group")]')

            for main_subcategory_element, category_container in zip(main_subcategories_elements, category_containers):
                if bool(main_subcategory_element.text):
                    main_subcategory_data = {
                        "name": main_subcategory_element.text,
                        "categories": [],
                    }

                    main_subcategories_data.append(main_subcategory_data)

                    for index, link in enumerate(category_container.find_elements(By.TAG_NAME, 'a')):
                        if index == 0:
                            name = link.text
                        elif index == 1:
                            name = 'Laptopuri cu Windows'
                        else:
                            name = 'Laptopuri Gaming'
                        category_data = {
                            "name": name,
                            "products": []
                        }

                        driver.execute_script(f"window.open(\"{link.get_attribute('href')}\")")
                        driver.switch_to.window(driver.window_handles[-1])

                        # Get products for each category
                        products_container = driver.find_element(By.ID, "card_grid")
                        product_cards = products_container.find_elements(By.XPATH, '*[contains(@class, "card-item")]')
                        for product_card in product_cards:
                            product_link = product_card.find_element(By.TAG_NAME, 'a').get_attribute('href')

                            driver.execute_script(f"window.open(\"{product_link}\")")
                            driver.switch_to.window(driver.window_handles[-1])

                            unique_id = uuid.uuid4()
                            title = driver.find_element(By.XPATH, '//h1[@class="page-title"]').text
                            print('title', title)

                            image_src = driver.find_element(
                                By.XPATH,
                                "//div[@id='product-gallery']//div[contains(@class, 'thumbnail-wrapper')]//img"
                            ).get_attribute('src')
                            image_content = requests.get(image_src, stream=True).raw

                            image = Image.open(image_content)
                            image.save(os.path.join("images", f"{unique_id}.jpg"))

                            price = None
                            try:
                                price = driver.find_element(
                                    By.XPATH,
                                    "//div[@class='product-highlight product-page-pricing']//p[@class='product-new-price']"
                                ).text
                            except Exception as e:
                                print('e', e)

                            driver.find_element(
                                By.XPATH,
                                "//a[@href='#specification-section']"
                            ).click()

                            driver.find_element(
                                By.XPATH,
                                "//div[@class='specifications-body']//button"
                            ).click()

                            processor_owner = driver.find_element(
                                By.XPATH,
                                "//div[@id='specifications-body']//table[contains(@class, 'specifications-table')]//td[text()='Producator procesor']/../td[2]"
                            ).text

                            category_data["products"].append({
                                "id": str(unique_id),
                                "title": title,
                                "price": price,
                                "specifications": {
                                    "processor_owner": processor_owner
                                }
                            })

                            driver.close()
                            driver.switch_to.window(driver.window_handles[1])

                            break

                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])

                        main_subcategory_data["categories"].append(category_data)

                        if index == 2:
                            break
                break

            break

        top_category_data["main_subcategories"] = main_subcategories_data

        data.append(top_category_data)

        break

    driver.close()

    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)
