import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import csv
import shutil
import os

currentDate = datetime.today().strftime('%m/%d/%Y')
fileTracker = "C:/Users/R/PycharmProjects/anyabot/data/lookups/case_summary.csv"

# Setup Chrome headless
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")


def updateTracker(casesCount, deathsCount, recoveredCount):
    found = False
    fileTracker2 = "C:/Users/R/PycharmProjects/anyabot/data/lookups/case_summary_temp.csv"
    shutil.copyfile(fileTracker, fileTracker2)
    with open(fileTracker,'w', newline='') as in_file:
        with open(fileTracker2) as out_file:
            writer = csv.writer(in_file)
            for row in csv.reader(out_file):
                if row[0] == currentDate:
                    found = True
                    print("Matched found!")
                    writer.writerow([currentDate, casesCount, deathsCount, recoveredCount])
                    print("Data has been updated.")
                else:
                    writer.writerow(row)
        in_file.close()
    out_file.close()

    #Final File
    os.remove(fileTracker2)

    if not found:
        with open(fileTracker, mode='a+', newline="") as csv_file:
            writeNewCounts = csv.writer(csv_file)
            writeNewCounts.writerow([currentDate, casesCount, deathsCount, recoveredCount])
        csv_file.close()
        print("New data has been added.")
    return


# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver = webdriver.Chrome("C:/Users/R/PycharmProjects/anyabot/chromedriver.exe", options=chrome_options)
url = "https://www.covid19.gov.ph/"
driver.get(url)
time.sleep(5)
cases = "//*[@id='post-17']/div/div/div/div/section[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/span[2]"
deaths = "//*[@id='post-17']/div/div/div/div/section[1]/div/div/div[2]/div/div/div[3]/div/div/div[1]/span[2]"
recovered = "//*[@id='post-17']/div/div/div/div/section[1]/div/div/div[2]/div/div/div[4]/div/div/div[1]/span[2]"

casesCount = driver.find_element_by_xpath(cases).text
deathsCount = driver.find_element_by_xpath(deaths).text
recoveredCount = driver.find_element_by_xpath(recovered).text

driver.close()

print("Total cases: ", casesCount)
print("Total deaths: ", deathsCount)
print("Total recoveries: ", recoveredCount)

updateTracker(casesCount, deathsCount, recoveredCount)
