from general import config_log, ler_config_json, enviar_email, kill_process, obter_asset

str_log = "[End] - "


def run(dt_excel_dispatcher, str_caminho_excel):
    # Atualizar relatório de execução
    dt_excel_dispatcher.to_excel(str_caminho_excel, index=False)

    # Lê o arquivo de config
    arquivo_config = ler_config_json.carregar_config()
    config_log.log_info(str_log + "Arquivo config lido")

    # Kill process
    # Inicia uma lista com o nome dos processos a fechar
    lista_processo_a_fechar = arquivo_config["settings"][0]["processos_a_fechar"]
    kill_process.kill_processos(lista_processo_a_fechar)

    # Obter senha do e-mail
    str_email_code = obter_asset.obter_asset(arquivo_config["settings"][0]["nome_asset_hash_email_code"])

    # Enviar e-mail de inicio
    str_email_destinatario = arquivo_config["settings"][0]["email_destinatario"]
    str_email_assunto = "HASH AUTOMATION - " + arquivo_config["settings"][0]["nome_processo"]
    str_email_corpo = "Finalização da execução do processo " + arquivo_config["settings"][0]["nome_processo"]
    str_email_remetente = arquivo_config["settings"][0]["email_hash"]

    enviar_email.enviar_email(
        str_email_destinatario,
        str_email_assunto,
        str_email_corpo,
        str_email_remetente,
        str_email_code,
        str_caminho_excel
    )
