from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import requests
import os


# Aguardar carregamento do botão submit
def aguardar_botao_submit(driver, timeout=30):
    try:
        WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "input[type='submit'][value='Submit']"))
        )
        return True
    except TimeoutException:
        return False


# Clicar no botão start
def clicar_botao_start(driver):
    botao = driver.find_element(By.XPATH, "//button[normalize-space()='Start']")
    botao.click()


# Baixar arquivo excel
def baixar_excel():
    url = "https://rpachallenge.com/assets/downloadFiles/challenge.xlsx"
    caminho_excel = os.path.join(os.path.expanduser("~"), "Downloads", "challenge.xlsx")

    response = requests.get(url)
    with open(caminho_excel, "wb") as f:
        f.write(response.content)

    return caminho_excel


# Preencher Role in Company
def preencher_role_company(driver, valor="Manager"):
    campo = driver.find_element(
        By.XPATH,
        "//label[normalize-space()='Role in Company']/following-sibling::input"
    )
    campo.clear()
    campo.send_keys(valor)
    campo.send_keys(Keys.TAB)


# Preencher First Name
def preencher_first_name(driver, valor="Manager"):
    campo = driver.find_element(
        By.XPATH,
        "//label[normalize-space()='First Name']/following-sibling::input"
    )
    campo.clear()
    campo.send_keys(valor)
    campo.send_keys(Keys.TAB)


# Preencher Last Name
def preencher_last_name(driver, valor="Manager"):
    campo = driver.find_element(
        By.XPATH,
        "//label[normalize-space()='Last Name']/following-sibling::input"
    )
    campo.clear()
    campo.send_keys(valor)
    campo.send_keys(Keys.TAB)


# Preencher Company Name
def preencher_company_name(driver, valor="Manager"):
    campo = driver.find_element(
        By.XPATH,
        "//label[normalize-space()='Company Name']/following-sibling::input"
    )
    campo.clear()
    campo.send_keys(valor)
    campo.send_keys(Keys.TAB)


# Preencher Address
def preencher_address(driver, valor="Manager"):
    campo = driver.find_element(
        By.XPATH,
        "//label[normalize-space()='Address']/following-sibling::input"
    )
    campo.clear()
    campo.send_keys(valor)
    campo.send_keys(Keys.TAB)


# Preencher Email
def preencher_email(driver, valor="Manager"):
    campo = driver.find_element(
        By.XPATH,
        "//label[normalize-space()='Email']/following-sibling::input"
    )
    campo.clear()
    campo.send_keys(valor)
    campo.send_keys(Keys.TAB)


# Phone Number
def preencher_phone_number(driver, valor="Manager"):
    campo = driver.find_element(
        By.XPATH,
        "//label[normalize-space()='Phone Number']/following-sibling::input"
    )
    campo.clear()
    campo.send_keys(valor)
    campo.send_keys(Keys.TAB)


# Clicar em submit
def clicar_submit(driver):
    botao = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Submit']")
    botao.click()
