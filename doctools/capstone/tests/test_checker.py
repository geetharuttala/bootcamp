# tests/test_checker.py

from passcheck.checker import evaluate_strength

def test_strength_levels():
    assert evaluate_strength("12345") == "Weak"
    assert evaluate_strength("hello123") == "Moderate"
    assert evaluate_strength("Str0ng!Passw0rd") == "Strong"
