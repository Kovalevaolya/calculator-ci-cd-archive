"""Создаёт HTML-документацию по калькулятору."""

from pathlib import Path


HTML = """<!doctype html>
<html lang=\"ru\">
<head>
  <meta charset=\"utf-8\">
  <title>Документация калькулятора</title>
</head>
<body>
  <h1>Калькулятор</h1>
  <p>Программа поддерживает сложение, вычитание, умножение и деление.</p>
  <h2>Функции</h2>
  <ul>
    <li><code>add(a, b)</code> — сложение;</li>
    <li><code>subtract(a, b)</code> — вычитание;</li>
    <li><code>multiply(a, b)</code> — умножение;</li>
    <li><code>divide(a, b)</code> — деление. Деление на ноль вызывает ошибку.</li>
  </ul>
</body>
</html>
"""


def main() -> None:
    output = Path("docs/calculator.html")
    output.parent.mkdir(exist_ok=True)
    output.write_text(HTML, encoding="utf-8")
    print(f"Документация создана: {output}")


if __name__ == "__main__":
    main()
