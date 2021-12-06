from os import environ
from typing import TYPE_CHECKING

if environ.get("PYTYPES") and not TYPE_CHECKING:
  import pytypes
  pytypes.enable_global_typechecked_profiler()
