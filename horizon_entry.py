"""Horizon deployment entrypoint."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from tradingview_mcp.server import mcp

__all__ = ["mcp"]
