from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome("C:\\Users\\ido geminer\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
#driver.get("https://www.ad.co.il/nadlanprice?year=2005,2007&orderby=1&city=nahariya")

#table_body = driver.find_element(By.TAG_NAME, "tbody")
#table_rows = table_body.find_elements(By.TAG_NAME, "tr")
#index = 2

#data = []

#for row in table_rows:
 #   time.sleep(1)
  #  driver.execute_script("arguments[0].scrollIntoView(true);", row)
   # table_data = row.find_elements(By.TAG_NAME, "td")
   # time.sleep(1)
   # row.click()

   # row_data = [cell.text for cell in table_data]
   # driver.execute_script("arguments[0].scrollIntoView(true);", row)
   # time.sleep(3)

#    x = row.find_element(By.XPATH, '//*[@id="cards"]/div/table/tbody/tr[{0}]/td/div[1]/div[2]/div[3]/dl/dd'.format(index)).text
 #   row_data.append(x)
  #  x = row.find_element(By.XPATH, '//*[@id="cards"]/div/table/tbody/tr[{0}]/td/div[1]/div[2]/div[4]/dl/dd'.format(index)).text
   # row_data.append(x)
   # data.append(row_data)
   # index += 2

#driver.quit()

    # Create a DataFrame from the list of data
#df = pd.DataFrame(data, columns=["Date", "City", "Street", "Rooms", "Size bruto", "Floor","Price", "Price per sqm", "Build Year", "Type of Property", "Part Sold"])

    # Export the DataFrame to an Excel file
#df.to_excel("C:\\Users\\ido geminer\\Desktop\\TAU\\SEM E\\סמינר נדלן\\nahariya excels\\nahariya_page1.xlsx", index=False)
#print("DONE NO 1")

data = []
for i in range(41,48):
    url="https://www.ad.co.il/nadlanprice?year=2005,2007&orderby=1&city=nahariya&pageindex={0}".format(i)
    driver.get(url)

    table_body = driver.find_element(By.TAG_NAME, "tbody")
    table_rows = table_body.find_elements(By.TAG_NAME, "tr")
    index = 2

    data = []

    for row in table_rows:
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(true);", row)
        table_data = row.find_elements(By.TAG_NAME, "td")
        time.sleep(1)
        row.click()

        row_data = [cell.text for cell in table_data]
        driver.execute_script("arguments[0].scrollIntoView(true);", row)
        time.sleep(3)

        x = row.find_element(By.XPATH, '//*[@id="cards"]/div/table/tbody/tr[{0}]/td/div[1]/div[2]/div[3]/dl/dd'.format(index)).text
        row_data.append(x)
       # time.sleep(1)
        x = row.find_element(By.XPATH, '//*[@id="cards"]/div/table/tbody/tr[{0}]/td/div[1]/div[2]/div[4]/dl/dd'.format(index)).text
        row_data.append(x)
        data.append(row_data)
        index += 2


    # Create a DataFrame from the list of data
    df = pd.DataFrame(data,columns=["Date", "City", "Street", "Rooms", "Size bruto", "Floor","Price", "Price per sqm", "Build Year", "Type of Property", "Part Sold"])
    my_file_path="C:\\Users\\ido geminer\\Desktop\\TAU\\SEM E\\סמינר נדלן\\nahariya excels\\nahariya_page{0}.xlsx".format(i)
    # Export the DataFrame to an Excel file
    df.to_excel(my_file_path, index=False)
    print("DONE exceling file Number: {0}".format(i))
    data = []
driver.quit()

print("__________________________________________")
print("FINNISHED ALL JOBSSSSSSS!!!!!!!!!!!!!!!!")
