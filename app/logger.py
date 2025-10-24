import logging
from datetime import datetime
from pathlib import Path
import pandas as pd
from app.calculator_config import CalculatorConfig

class LoggingObserver:
    """Observer that logs each calculation."""

    def __init__(self):
        self.config = CalculatorConfig()
        Path(self.config.log_dir).mkdir(parents=True, exist_ok=True)
        logging.basicConfig(
            filename=self.config.log_file,
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s]: %(message)s",
        )

    def update(self, event_type, data):
        if event_type == "calculation_performed":
            msg = f"{data['operation']}({data['a']}, {data['b']}) = {data['result']}"
            logging.info(msg)


class AutoSaveObserver:
    """Observer that auto-saves calculation history to CSV."""

    def __init__(self):
        self.config = CalculatorConfig()
        Path(self.config.history_dir).mkdir(parents=True, exist_ok=True)

    def update(self, event_type, data):
        if event_type == "calculation_performed":
            history = data.get("history", [])
            df = pd.DataFrame(history)
            df.to_csv(self.config.history_file, index=False)