# calculator/calculator_logic.py
import re

class CalculatorLogic:
    def append(self, current: str, text: str) -> str:
        return current + text

    def evaluate_expression(self, expr: str) -> str:
        if not re.fullmatch(r"[0-9+\-*/(). ]*", expr):
            return "Error"
        try:
            return str(eval(expr, {"__builtins__": None}, {}))
        except Exception:
            return "Error"

    def clear(self) -> str:
        return ""

    def backspace(self, current: str) -> str:
        return current[:-1]
