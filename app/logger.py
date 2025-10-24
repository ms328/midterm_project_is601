########################
# Logger Module        #
########################

import logging
import os
import pandas as pd
from datetime import datetime
from app.calculator_config import CalculatorConfig

def setup_logger():
    """Set up logging configuration with current environment settings."""
    # Load configuration AFTER checking env vars (so tmp_path ones take effect)
    config = CalculatorConfig()

    # Dynamically pick up env-based log/history directories
    log_dir = os.getenv("CALCULATOR_LOG_DIR", str(config.log_dir))
    hist_dir = os.getenv("CALCULATOR_HISTORY_DIR", str(config.history_dir))
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(hist_dir, exist_ok=True)

    LOG_FILE = os.path.join(log_dir, "calculator.log")

    # Create logger with a unique name
    logger = logging.getLogger("app.logger")
    # Remove any existing handlers
    logger.handlers.clear()
    
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Add file handler
    file_handler = logging.FileHandler(LOG_FILE, mode="a")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Add console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Prevent duplicate logs
    logger.propagate = False
    
    return logger, log_dir, hist_dir

# Initial setup
logger, log_dir, hist_dir = setup_logger()


class LoggingObserver:
    """Observer that logs calculator events to a file and console."""

    def __init__(self):
        # Get fresh logger configuration
        self.logger, _, _ = setup_logger()

    def update(self, event: str, data: dict):
        if event == "calculation_performed":
            op = data.get("operation")
            a = data.get("a")
            b = data.get("b")
            result = data.get("result")
            message = f"{op}({a}, {b}) = {result}"
            self.logger.info(message)


class AutoSaveObserver:
    """Observer that saves history to CSV automatically."""

    def __init__(self):
        # Get fresh history directory configuration
        _, _, self.hist_dir = setup_logger()

    def update(self, event: str, data: dict):
        if event == "calculation_performed":
            history = data.get("history")
            if not history:
                return
            df = pd.DataFrame(history)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"history_{timestamp}.csv"
            file_path = os.path.join(self.hist_dir, filename)
            df.to_csv(file_path, index=False)
