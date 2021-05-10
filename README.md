# Demonstrating pylint issue [4437](https://github.com/PyCQA/pylint/issues/4437)

Steps to reproduce:

```bash
pipenv sync --dev

cd functional-u
isort functional/u/ungrouped_imports_namespace.py  # no change

pylint functional
```

will give the following output:

```
************* Module functional.u.ungrouped_imports_namespace
functional/u/ungrouped_imports_namespace.py:4:0: C0411: third party import "import numpy" should be placed before "import functional.w.wrong_import_order" (wrong-import-order)
functional/u/ungrouped_imports_namespace.py:6:0: C0412: Imports from package functional are not grouped (ungrouped-imports)

---------------------------------------------------------------------
Your code has been rated at 3.33/10 (previous run: -10.00/10, +13.33)
```

All the exact version numbers for the packages are locked in `Pipfile.lock`