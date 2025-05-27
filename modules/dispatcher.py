from processo.site_rpa_challenge.tela_inicial import baixar_excel
from general import config_log
import os
import pandas as pd

str_log = "[Dispatcher] - "


def run():
    config_log.log_info(str_log + "Iniciando download do arquivo")

    # Realizar download do arquivo excel
    caminho_excel = baixar_excel()
    existe_arquivo_excel = os.path.isfile(caminho_excel)
    config_log.log_info(str_log + "Download realizado: " + str(existe_arquivo_excel))

    # Iniciar a var dt_excel_dispatcher
    dt_excel_dispatcher = None

    # Ler arquivo excel
    if existe_arquivo_excel:
        dt_excel_dispatcher = pd.read_excel(caminho_excel)

        # Criar coluna Status
        dt_excel_dispatcher["Status"] = ""

    return dt_excel_dispatcher, caminho_excel


if __name__ == "__main__":
    run()
