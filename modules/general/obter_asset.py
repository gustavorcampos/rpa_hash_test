import os


def obter_asset(nome):
    asset_name = os.getenv(nome)
    return asset_name


if __name__ == "__main__":
    asset = obter_asset("EMAIL_HASH_CODE")
    print(asset)
