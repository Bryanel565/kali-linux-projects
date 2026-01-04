import subprocess
import sys


def run_module(module_name):
    # Run the module as a script and return exit code
    res = subprocess.run(
        [sys.executable, "-m", module_name], capture_output=True, text=True
    )
    return res.returncode, res.stdout, res.stderr


def test_classic_module_runs():
    code, out, err = run_module("deckofcards.classic")
    assert code == 0
    assert "Initial deck" in out


def test_collection_module_runs():
    code, out, err = run_module("deckofcards.collection")
    assert code == 0
    assert "Player 1" in out
