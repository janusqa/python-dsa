### UV
- uv init .
- uv tool install ruff

### Pytest
- uv run pytest
- uv run pytest tests/test_name_of_test.py
- constraints for test
  1. Write me a pytest with the following rules
  2. do not use fstrings directly in error constructors
  3. fstrings can be used otherwise if assinging to a variable for example
  4. use type hints where necessary
  5. only used the built in type hinting
  6. Do not use assert
  7. first line of descriptions should end with a period