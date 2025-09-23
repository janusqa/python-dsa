### UV
- uv init .
- uv tool install ruff

### Pytest
- uv run pytest
- uv run pytest tests/test_name_of_test.py
- constraints for test
    1. Write a pytest test suite following these specific rules.
    2. Never use f-strings directly as arguments to error constructors like pytest.fail().
    3. F-strings are permitted when assigned to variables first, then passed to error constructors.
    4. Use type hints where appropriate throughout the code.
    5. Only use built-in type hinting (no imports from typing module). Exceptions require explicit approval.
    6. Absolutely no assert statements - use pytest.fail() with error messages instead.
    7. All test method docstrings must have their first line ending with a period.
    8. Pay special attention to f-string usage (rules 2-3) and type hinting restrictions (rules 4-5).
    9. Use a test class structure with fixtures as shown in the example.
        ```python

      from my_class_module import Solution

      class MyTestClass:
        @pytest.fixture
        def solution(self) -> Solution:
            """Return a Solution instance for testing."""
            return Solution()
      ```
    10. The method being tested must literally be named function_under_test when called.
      ```python
        def my_test_1(self, solution: Solution) -> None
          solution.function_under_test()
      ```
    11. Import the Solution class from "my_class_module" as specified.


