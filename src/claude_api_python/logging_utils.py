"""Logging setup helpers."""

from __future__ import annotations

import logging
import sys

try:
    from loguru import logger as _logger
except ImportError:  # pragma: no cover
    _logger = None


def setup_logging(level: str = "INFO") -> None:
    """Configure logging via loguru when available, else stdlib logging."""
    if _logger is not None:
        _logger.remove()
        _logger.add(sys.stderr, level=level.upper(), format="{time} | {level} | {message}")
        return
    logging.basicConfig(stream=sys.stderr, level=getattr(logging, level.upper(), logging.INFO))
