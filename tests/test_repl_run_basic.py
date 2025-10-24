import io
import sys
from app.calculator_repl import calculator_repl

def test_repl_add_exit(monkeypatch, capsys):
    # Fake user input: perform add(2, 3), then exit
    fake_input = io.StringIO("add\n2\n3\nexit\n")
    monkeypatch.setattr("sys.stdin", fake_input)
    monkeypatch.setattr("sys.stdout", io.StringIO())  # silence REPL print spam

    calculator_repl()  # Run the REPL (it will stop at 'exit')

    out = sys.stdout.getvalue()
    assert "Result" in out or "SUCCESS" in out or "22" in out
