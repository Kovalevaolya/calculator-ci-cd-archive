# Калькулятор с CI

Учебный проект для настройки непрерывной интеграции в GitHub Actions.

## Запуск тестов

```bash
python -m unittest discover -s tests -v
```

## Генерация документации

```bash
python generate_docs.py
```

После выполнения команды создаётся файл `docs/calculator.html`.
