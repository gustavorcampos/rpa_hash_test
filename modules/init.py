from general import config_log, ler_config_json, kill_process, init_all_applications
from general import enviar_email, obter_asset
from processo.site_rpa_challenge import tela_inicial
from rpaHashTest.config import driver_context

str_log = "[Init] - "


def run(bool_primeira_execucao):

    if bool_primeira_execucao:

        # Inicia a configuração do log
        config_log.setup_logger()
        config_log.log_info(str_log + "RPA iniciado")

        # Lê o arquivo de config
        arquivo_config = ler_config_json.carregar_config()
        config_log.log_info(str_log + "Arquivo config lido")

        # Obter senha do e-mail
        str_email_code = obter_asset.obter_asset(arquivo_config["settings"][0]["nome_asset_hash_email_code"])

        # Enviar e-mail de inicio
        str_email_destinatario = arquivo_config["settings"][0]["email_destinatario"]
        str_email_assunto = "HASH AUTOMATION - " + arquivo_config["settings"][0]["nome_processo"]
        str_email_corpo = "Inicio da execução do processo " + arquivo_config["settings"][0]["nome_processo"]
        str_email_remetente = arquivo_config["settings"][0]["email_hash"]

        enviar_email.enviar_email(str_email_destinatario, str_email_assunto, str_email_corpo, str_email_remetente, str_email_code)

        # Kill process
        # Inicia uma lista com o nome dos processos a fechar
        lista_processo_a_fechar = arquivo_config["settings"][0]["processos_a_fechar"]
        kill_process.kill_processos(lista_processo_a_fechar)

        # Iniciar aplicações
        driver_context.driver = init_all_applications.abrir_chrome(arquivo_config["settings"][0]["nome_site_rpa_challenge"])
        bool_site_carregado = tela_inicial.aguardar_botao_submit(driver_context.driver)
        config_log.log_info(str_log + "Site carregado: " + str(bool_site_carregado))
