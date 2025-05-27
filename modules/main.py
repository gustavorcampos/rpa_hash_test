import init
import dispatcher
import process
import end


def main():
    # Iniciando variáveis do main
    global dt_excel_dispatcher, str_caminho_excel
    bool_continuar_execucao = True
    bool_primeira_execucao = True
    int_transaction_item = 0

    while bool_continuar_execucao:

        # Etapa 1: Init
        init.run(bool_primeira_execucao)

        # Etapa 2: Dispatcher
        if bool_primeira_execucao: dt_excel_dispatcher, str_caminho_excel = dispatcher.run()

        # Etapa 3: Get Transaction item
        if int_transaction_item < len(dt_excel_dispatcher):

            # Armazenar toda a linha da dt
            linha = dt_excel_dispatcher.iloc[int_transaction_item]

            # Configurar chave de primeira execução para False
            bool_primeira_execucao = False

            # Etapa 4: Process
            process.run(linha, int_transaction_item)

            # Preencher coluna status
            dt_excel_dispatcher.loc[int(int_transaction_item), "Status"] = "Sucesso"

            # Incrementar valor da transação
            int_transaction_item = int_transaction_item + 1

        else:
            bool_continuar_execucao = False

        # Etapa 5: End
        if not bool_continuar_execucao: end.run(dt_excel_dispatcher, str_caminho_excel)


if __name__ == "__main__":
    main()
