from selenium import webdriver
from selenium.webdriver.chrome.options import Options

_driver_global = None  # variável persistente no módulo


def abrir_chrome(site):
    global _driver_global

    if not site.startswith("http"):
        site = "https://" + site

    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)  # <-- isso impede o fechamento automático

    _driver_global = webdriver.Chrome(options=options)
    _driver_global.get(site)

    return _driver_global


def get_driver(site):
    return abrir_chrome(site)


if __name__ == "__main__":
    abrir_chrome("https://consopt.www8.receita.fazenda.gov.br/consultaoptantes")
