from pathlib import Path
import importlib

# import all pages dynamically, avoid doing manually like: 
# from .login_page import LoginPage

for file in Path(__file__).parent.glob("*_page.py"):
    module = importlib.import_module(f".{file.stem}", package=__name__)

    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, type):
            globals()[name] = obj