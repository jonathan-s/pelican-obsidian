import os
import sys

from loguru import logger

from .obsidian import *  # noqa

__all__ = ["ObsidianMarkdownReader"]

# configure logging on debug level
logger.remove()
DEFAULT_LOG_LEVEL = "INFO"
logger.add(
    os.path.join(os.getcwd(), "obsidian.log"),
    level=DEFAULT_LOG_LEVEL,
    format="{time} {level} {message}",
    rotation="1 MB",
    compression="zip",
    enqueue=True,
)
# add a handler to print to stdout
logger.add(
    sys.stderr,
    level=DEFAULT_LOG_LEVEL,
    format="{level} {message}",
    enqueue=True,
    colorize=True,
)
