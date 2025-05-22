import os
import sys
import logging
from ChessUI import ChessUI

def initialize_logging():
    # Configure basic logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

if __name__ == "__main__":
    initialize_logging()
    logging.info("Starting Chess UI.....")
    board = ChessUI()