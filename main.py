import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

course_names = []
course_price = []
course_link = []
course_rating = []
course_methods = []
course_description = []


for i in range(1, 10):
    ROOT_URL = (f"https://www.springest.nl/abonnementen/onbeperkt/{i}")
    driver.get(ROOT_URL)
    sleep(3)
    print(i)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    h2_tags = soup.find_all("h2", class_="as-h3 product-item__title")
    list1 = [title.text for title in h2_tags]
    list2 = [f'https://www.springest.nl/{title.a["href"]}' for title in h2_tags]
    price_tags = soup.find_all("span", class_="price")
    list3 = [price.text[:-5] for price in price_tags]
    raw_score = soup.find_all("span", class_="institute-rating rating-score")
    list4 = [score.text for score in raw_score]
    method_raw = soup.find_all("span",  class_="method")
    list5 = [method.text for method in method_raw]
    data_divs = soup.find_all("div", class_="product-item__description")
    list6 = [data.p.text for data in data_divs]
    course_names.extend(list1)
    course_price.extend(list3)
    course_link.extend(list2)
    course_rating.extend(list4)
    course_methods.extend(list5)
    course_description.extend(list6)
    sleep(2)

data_object = {
    "Course title": course_names,
    "Course price": course_price,
    "Course rating": course_rating,
    "Course method": course_methods,
    "Brief description": course_description,
    "Course link": course_link
}

df = pd.DataFrame(data_object)
df.to_csv("sample_python.csv")
