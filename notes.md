# Notes

###### Creating a uv project with pytest:
1. Create a new uv project:
```Code
uv init my_uv_project --package
cd my_uv_project
```
This command initializes a new Python package project named my_uv_project and navigates into its directory. 
The --package flag sets up a package structure with a src directory.

2. Add pytest as a development dependency:
```Code
uv add --dev pytest
```
This command adds pytest to your project's development dependencies, meaning it will be installed in your project's virtual environment but not included when your package is built for distribution.

3. Create a simple Python module:
Inside the src/my_uv_project directory, create a file named main.py with the following content:

###### src/my_uv_project/main.py
```
def add_numbers(a: int, b: int) -> int:
    return a + b

def subtract_numbers(a: int, b: int) -> int:
    return a - b
```
4. Create a test file:
Create a tests directory at the root of your project and inside it, create a file named test_main.py with the following content:

###### tests/test_main.py
```
import pytest
from my_uv_project.main import add_numbers, subtract_numbers

@pytest.mark.parametrize(
    "num_1, num_2, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ],
)
def test_add_numbers(num_1: int, num_2: int, expected: int) -> None:
    assert add_numbers(num_1, num_2) == expected

@pytest.mark.parametrize(
    "num_1, num_2, expected",
    [
        (5, 2, 3),
        (10, 10, 0),
        (0, 5, -5),
    ],
)
def test_subtract_numbers(num_1: int, num_2: int, expected: int) -> None:
    assert subtract_numbers(num_1, num_2) == expected
```
5. Run the tests with uv:
```Code
uv run pytest
```
This command executes pytest within your uv project's virtual environment, running all the tests defined in test_main.py. You should see output indicating that all tests passed.

<br /><br />
###### Using the Character Viewer: 
1. Press "Command-Control-Space" to open the Character Viewer.
2. Type "superscript" into the search bar.
3. Double-click the superscript character you want to insert.
4. For numbers, you may find them more easily under the "Digits" category in the sidebar.

Note: Superscripts were used in converters.py to create exponents in the base_2_to_base_10 function (ex. (1 x 2⁷) + (1 x 2⁶) + (0 x 2⁵) + (0 x 2⁴) + (1 x 2³) + (0 x 2²) + (1 x 2¹) + (0 x 2⁰))

<br /><br />
###### Entry point to CLI: 

In mpyproject.toml:
```
[project.scripts]
# cli_command_name = "module_path:function_name"
# If your code is in src/example/main.py, 
# the entry would be "example.main:main". 
convert = "convert.convert:main"
```
I also needed to:
In convert.py, line 25 is "from converters import (",
would need to change to:  "from .converters import ("

I could run:
```
$ uv run convert -h
```
but not:
```
$ uv run pytest
```

I googled: google for help, but still had issues: 
entry point to cli in uv application and i get ImportError: cannot import name 'main' from 'example'

A helpful URL:
https://pybit.es/articles/developing-and-testing-python-packages-with-uv/

