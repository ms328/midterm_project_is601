########################
# Logger Module        #
########################

import logging
import os
import pandas as pd
from datetime import datetime
from app.calculator_config import CalculatorConfig

config = CalculatorConfig()

# Ensure log directory exists
os.makedirs(config.log_dir, exist_ok=True)

# Configure logger to write to file and console
LOG_FILE = config.log_file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class LoggingObserver:
    """Observer that logs calculator events to a log file."""

    def update(self, event: str, data: dict):
        if event == "calculation_performed":
            op = data.get("operation")
            a = data.get("a")
            b = data.get("b")
            result = data.get("result")
            logger.info(f"{op}({a}, {b}) = {result}")


class AutoSaveObserver:
    """Observer that automatically saves history to CSV."""

    def update(self, event: str, data: dict):
        if event == "calculation_performed":
            history = data.get("history")
            if not history:
                return
            df = pd.DataFrame(history)
            os.makedirs(config.history_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"history_{timestamp}.csv"
            file_path = os.path.join(config.history_dir, filename)
            df.to_csv(file_path, index=False)
