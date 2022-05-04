import time
import json

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

                    for link in category_container.find_elements(By.TAG_NAME, 'a'):
                        category_data = {
                            "name": link.text,
                            "products": []
                        }

                        driver.execute_script(f"window.open(\"{link.get_attribute('href')}\")")
                        driver.switch_to.window(driver.window_handles[-1])

                        # Get products for each category
                        products_container = driver.find_element(By.ID, "card_grid")
                        product_cards = products_container.find_elements(By.XPATH, '*[contains(@class, "card-item")]')
                        for product_card in product_cards:
                            title = product_card.find_element(By.XPATH, "//*[contains(@class, 'card-v2-title')]").text
                            price = product_card.find_element(By.XPATH, "//*[contains(@class, 'product-new-price')]").text
                            category_data["products"].append({
                                "title": title,
                                "price": price,
                            })

                        driver.switch_to.window(driver.window_handles[0])

                        main_subcategory_data["categories"].append(category_data)

                        break
                break

        top_category_data["main_subcategories"] = main_subcategories_data

        data.append(top_category_data)

        break

    driver.close()

    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)
