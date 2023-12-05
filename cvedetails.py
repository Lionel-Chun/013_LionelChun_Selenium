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

# Open file and return a stream.
with open("cvedetails.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    for row in tbody_rows:
        row_data = []

        # find th
        table_th = row.find_elements(By.TAG_NAME, "th")

        # loop every th
        for data in table_th:
            # append each th tag content to row_data
            row_data.append(data.text)

        # find td
        table_data = row.find_elements(By.TAG_NAME, "td")

        # loop every td
        for data in table_data:
            # check anchor tag if exists
            if (data.get_attribute(By.LINK_TEXT) != None):
                # anchor tag if exists append its text content to row_data
                row_data.append(data.get_attribute(By.LINK_TEXT))
            else:
                # otherwise append td content to row_data
                row_data.append(data.text)
        print(row_data, end='\n')

        # writer data to csv
        writer.writerow(row_data)

driver.quit()
