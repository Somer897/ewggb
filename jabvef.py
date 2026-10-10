from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

date = str(input('Дата(25): '))
place_from = str(input('Откуда ( Минск-Пассажирский / Барановичи): '))              #ЗНАЧЕНИЯ ВВОДА
place_from = 'Минск-Пассажирский' if place_from == '1' else 'Барановичи'
place_to = str(input('Куда ( Минск-Пассажирский / Барановичи): '))
place_to = 'Минск-Пассажирский' if place_to == '1' else 'Барановичи'
main_date = ''

if place_from == 'Минск-Пассажирский' and place_to == 'Барановичи':
    main_date = '//*[@id="sch-route"]/div[3]/div[2]/div[1]/div[3]/div/div[9]/div/div[4]/div[1]/div[2]/a'

driver = webdriver.Firefox()
driver.get('https://www.rw.by/')                                              #БРАУЗЕР

button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "button.mc-btn-all")))                       #COOKIES
button.click()
time.sleep(2)

tFrom = driver.find_element(By.ID, value='acFrom').send_keys(place_from)
tTo = driver.find_element(By.ID, value='acTo').send_keys(place_to)
tWhen = driver.find_element(By.ID, value='yDate')                                     #ВВОДИМ ЗНАЧЕНИЯ
tWhen.click()
time.sleep(0.5) 
desired_day = driver.find_element(By.XPATH, f"//a[contains(@class, 'ui-state-default')][text()='{date}']")
desired_day.click()
time.sleep(2)
tOk = driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()          

button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[9]/div[2]/div/div[2]/button[1]')))       #COOKIES   
button.click()
time.sleep(3)

try:
    exist = driver.find_element(By.XPATH, value = main_date)                                     #exists ticket
except NoSuchElementException:
    time.sleep(8)
    driver.refresh()

button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//*[@id='sch-route']/div[3]/div[2]/div[1]/div[3]/div/div[9]/div/div[4]/div[2]/form/a")))     #to buy ticket
button.click()

list = ['Вагон №01 (2П) ', 'Вагон №02 (2П)', 'Вагон №03 (2П)', 'Вагон №04 (2П)', 'Вагон №05 (2П)', 'Вагон №06 (2П)']

for railcar in list:
    try:
        wagon_locator = (By.XPATH, f"//span[contains(text(), '{railcar}')]")
        wagon_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(wagon_locator))
        wagon_button.click()
    except TimeoutException:
        continue
    else:
        break