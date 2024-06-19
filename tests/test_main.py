import pytest
from python3_starter.main import suma, resta, main
import sys

def test_suma():
    assert suma(1, 2) == 3
    assert suma(-1, 1) == 0

def test_resta():
    assert resta(2, 1) == 1
    assert resta(2, 2) == 0

def test_main_suma(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['calc', 'suma', '3', '5'])
    main()
    captured = capsys.readouterr()
    assert "The result of adding 3 + 5 is 8" in captured.out

def test_main_resta(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['calc', 'resta', '10', '4'])
    main()
    captured = capsys.readouterr()
    assert "The result of subtracting 4 from 10 is 6" in captured.out

def test_main_no_command(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['calc'])
    main()
    captured = capsys.readouterr()
    assert "usage:" in captured.out
