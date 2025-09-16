### UV
- uv init .
- uv tool install ruff

### Pytest
- uv run pytest
- uv run pytest tests/test_name_of_test.py
- constraints for test
  1. Write me a pytest with the following rules
  2. no fstrings in error constructors
  3. use type hints where neccessary
  4. Do not use assert
  5. first line of descriptions should end with a period