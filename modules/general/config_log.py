import logging


def setup_logger(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[logging.StreamHandler()]
    )


def log_info(message):
    logging.info(message)


if __name__ == "__main__":
    setup_logger()
    log_info("TESTE")
