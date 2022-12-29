import logging
import sys

# Logging
logger = logging.getLogger("__name__")

logging.basicConfig(level=logging.DEBUG)

format = logging.Formatter(
    "%(levelname)s:%(module)s:%(asctime)s, %(message)s", "%m/%d/%Y %H:%M:%S"
)

debugHandler = logging.StreamHandler(sys.stdout)
debugHandler.setLevel(logging.DEBUG)
debugHandler.setFormatter(format)

logger.addHandler(debugHandler)
