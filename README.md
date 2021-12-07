# pytypes-env

If PYTYPES env var is set when you import this module then pytypes.enable_global_typechecked_profiler() will be called to enable typechecking.
Typechecking will be applied to any import or definition after the import statement.

Usage: Import pytypes_env in a script:

```
import pytypes_env

def test(foo: str) -> bool:
  return "hello"


test(1)

```

Then run:

```
 > python3 test.py
Traceback (most recent call last):
  File "test.py", line 7, in <module>
    test(1)
  File "test.py", line 3, in test
    def test(foo: str) -> bool:
pytypes.exceptions.InputTypeError:
  __main__.test
  called with incompatible types:
Expected: Tuple[str]
Received: Tuple[int]

```
