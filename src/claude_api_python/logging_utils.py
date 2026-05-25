from loguru import logger


def setup_logging() -> None:
    logger.remove()
    logger.add(lambda m: print(m, end=""), level="INFO")
