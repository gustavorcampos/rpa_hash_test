from general import config_log
from processo.site_rpa_challenge import tela_inicial
from rpaHashTest.config import driver_context

str_log = "[Process] - "


def run(linha, int_transaction_item):
    # Log de execução
    config_log.log_info(str_log + "Transação: " + str(int_transaction_item))

    # Armazenar todas as var's da fila de trabalho
    str_first_name = linha["First Name"]
    str_last_name = linha["Last Name "]
    str_company_name = linha["Company Name"]
    str_role_company = linha["Role in Company"]
    str_address = linha["Address"]
    str_email = linha["Email"]
    str_phone_number = linha["Phone Number"]

    # Preencher First Name
    tela_inicial.preencher_first_name(driver_context.driver, str_first_name)

    # Preencher Last Name
    tela_inicial.preencher_last_name(driver_context.driver, str_last_name)

    # Preencher Company Name
    tela_inicial.preencher_company_name(driver_context.driver, str_company_name)

    # Preencher Role in Company
    tela_inicial.preencher_role_company(driver_context.driver, str_role_company)

    # Preencher Address
    tela_inicial.preencher_address(driver_context.driver, str_address)

    # Preencher Email
    tela_inicial.preencher_email(driver_context.driver, str_email)

    # Preencher Phone Number
    tela_inicial.preencher_phone_number(driver_context.driver, str(str_phone_number))

    # Clicar em submit
    tela_inicial.clicar_submit(driver_context.driver)

    # Log de execução
    config_log.log_info(str_log + "Preenchimento finalizado")
