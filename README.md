# Demonstrating pylint issue [4437](https://github.com/PyCQA/pylint/issues/4437)

Steps to reproduce:

1. Setup environment
```bash
pipenv sync --dev
```

2. Different pylint behaviour based on working directory
```bash
> # in the repo root directory
> pylint --rcfile .pylintrc apple/fruit2/apple/__init__.py

************* Module apple
apple/fruit2/apple/__init__.py:6:0: C0412: Imports from package fruit2 are not grouped (ungrouped-imports)

------------------------------------------------------------------
Your code has been rated at 7.50/10 (previous run: 7.50/10, +0.00)




cd apple
> pylint --rcfile ../.pylintrc fruit2/apple/__init__.py

************* Module apple
fruit2/apple/__init__.py:4:0: C0411: third party import "import numpy" should be placed before "import fruit2.banana.data" (wrong-import-order)
fruit2/apple/__init__.py:6:0: C0412: Imports from package fruit2 are not grouped (ungrouped-imports)

------------------------------------------------------------------
Your code has been rated at 5.00/10 (previous run: 2.50/10, +2.50)
```

3. Different isort behaviour based on working directory

Invoking isort from the `apple` directory produces no changes:

```bash
cd apple
isort fruit2/apple/__init__.py

# no output, no changes

cd ..  # back to repo root
isort apple/fruit2/apple/__init__.py
> Fixing pylint-issue-demo/apple/fruit2/apple/__init__.py
```

with this `diff`:

```diff
diff --git a/apple/fruit2/apple/__init__.py b/apple/fruit2/apple/__init__.py
index fd23b38..1970b58 100644
--- a/apple/fruit2/apple/__init__.py
+++ b/apple/fruit2/apple/__init__.py
@@ -1,6 +1,5 @@
 import math

+import fruit2.apple.data
 import fruit2.banana.data
 import numpy
-
-import fruit2.apple.data
```

All the exact version numbers for the packages are locked in `Pipfile.lock`