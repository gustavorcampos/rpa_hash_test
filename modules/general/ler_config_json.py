import json
import os


def carregar_config(nome_arquivo="config.json"):
    # Caminho absoluto baseado na raiz do projeto
    raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    caminho = os.path.join(raiz_projeto, "config", nome_arquivo)

    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo de configuração não encontrado: {caminho}")  # Mudar exceção posteriormente

    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    arquivo_config = carregar_config()
