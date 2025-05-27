import subprocess
from rpaHashTest.modules.general import config_log
str_log = "[Kill Process] - "

# Inicia a configuração do log
config_log.setup_logger()


def kill_processos(lista_processos):
    for processo in lista_processos:
        try:
            subprocess.run(["taskkill", "/F", "/IM", processo],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            config_log.log_info(f"{str_log}Processo finalizado: {processo}")
        except Exception as e:
            config_log.log_info(f"{str_log}Erro ao finalizar {processo}: {e}")


if __name__ == "__main__":
    kill_processos(["excel.exe"])
