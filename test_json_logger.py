import logging
import time

from json_formatter import JSONFormatter

# Get logger
logger = logging.getLogger(__name__)

# Create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs/my_app.log')

# Create formatter
json_formatter = JSONFormatter()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Add formatter to handler
file_handler.setFormatter(json_formatter)
stream_handler.setFormatter(json_formatter)

# Add handler to logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# Set log level to DEBUG
logger.setLevel(logging.DEBUG)


def some_function():
    start = time.perf_counter()
    logger.info("Start function")
    time.sleep(5)
    end = time.perf_counter()
    logger.info("End function", {"time_used": end - start})


def some_error_function():
    try:
        raise Exception("Some error ....")
    except Exception:
        logger.exception("Ouch !!!!")


logger.info("Hello", {"world": "this", "is": "structured logs"})
some_function()
some_error_function()
try:
    1 / 0
except Exception as e:
    logger.exception(f"Hey there is error here >> {repr(e)}", {"check": "this out"})
