from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
url = "https://www.cvedetails.com/top-50-products.php?year=0"
driver.get(url)
tbody = driver.find_element(By.XPATH, "//table[contains(@class, \"table-striped\")]/tbody")
tbody_rows = tbody.find_elements(By.TAG_NAME, "tr")

with open("cvedetails.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    for row in tbody_rows:
        row_data = []
        table_th = row.find_elements(By.TAG_NAME, "th")
        for data in table_th:
            row_data.append(data.text)

        table_data = row.find_elements(By.TAG_NAME, "td")
        for data in table_data:
            # print(data.text)
            if (data.get_attribute(By.LINK_TEXT) != None):
                row_data.append(data.get_attribute(By.LINK_TEXT))
            else:
                row_data.append(data.text)
        print(row_data, end='\n')
        writer.writerow(row_data)

driver.quit()
