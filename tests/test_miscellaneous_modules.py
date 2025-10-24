##############################
# tests/test_miscellaneous_modules.py
##############################

import os
import pandas as pd
from pathlib import Path
from app import colors, help_decorator
from app.command_pattern import OperationCommand
from app.operations import Addition
from app.logger import LoggingObserver, AutoSaveObserver

def test_colors_functions():
    msg_success = colors.success("Calculation successful")
    msg_error = colors.error("Invalid operation")
    msg_warn = colors.warn("Be cautious")

    assert "✓" in msg_success
    assert "✗" in msg_error
    assert "!" in msg_warn

def test_help_menu_output(capsys):
    commands = {
        "add": "perform addition",
        "undo": "undo last operation",
        "exit": "close the app",
    }
    help_decorator.dynamic_help(commands)
    output = capsys.readouterr().out
    assert "Available Commands" in output
    assert "add" in output
    assert "undo" in output

def test_command_pattern_execution():
    operation = Addition()
    command = OperationCommand(operation, 10, 5)
    result = command.execute()
    assert result == 15  # Ensures Command pattern works correctly

def test_logging_and_autosave(tmp_path):
    # Temporary directories for isolated testing
    logs_dir = tmp_path / "logs"
    hist_dir = tmp_path / "history"
    logs_dir.mkdir()
    hist_dir.mkdir()

    # Monkey-patch environment paths
    os.environ["CALCULATOR_LOG_DIR"] = str(logs_dir)
    os.environ["CALCULATOR_HISTORY_DIR"] = str(hist_dir)

    observer1 = LoggingObserver()
    observer2 = AutoSaveObserver()

    # Simulate a calculation event
    history = [{"operation": "add", "a": 2, "b": 3, "result": 5}]
    data = {"operation": "add", "a": 2, "b": 3, "result": 5, "history": history}

    observer1.update("calculation_performed", data)
    observer2.update("calculation_performed", data)

    # Check if files are created
    log_files = list(logs_dir.glob("*.log"))
    csv_files = list(hist_dir.glob("*.csv"))

    assert len(log_files) > 0, "No log file created"
    assert len(csv_files) > 0, "No CSV history file created"

    df = pd.read_csv(csv_files[0])
    assert not df.empty
    assert "operation" in df.columns
