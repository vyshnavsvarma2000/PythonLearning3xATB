# Python 3x Learning - ATB 
Below are the key topics to learn in Python, organized as bullet points for easy reference:

- **Python Basics**
  - Introduction to Python
  - Installation and Setup
  - Running Python Programs
  - Python Syntax
  - Variables and Data Types
  - Basic Operators
  - Control Flow
    - If Statements
    - Loops (For, While)

- **Functions**
  - Defining Functions
  - Function Arguments
  - Return Statement
  - Lambda Functions
  - Map, Filter, and Reduce Functions
  - Recursion

- **Strings**
  - String Manipulation
  - String Methods
  - Formatting Strings
  - Regular Expressions

- **Data Structures**
  - Lists
    - List Methods
    - List Comprehensions
  - Tuples
  - Dictionaries
    - Dictionary Methods
  - Sets
    - Set Methods

- **Modules and Packages**
  - Importing Modules
  - Standard Library Modules
  - Creating and Using Packages

- **File Handling**
  - Reading and Writing Files
  - Working with CSV and JSON Files

- **Error and Exception Handling**
  - Try, Except Blocks
  - Finally and Else Clauses
  - Custom Exceptions

- **Object-Oriented Programming (OOP)**
  - Classes and Objects
  - Inheritance
  - Polymorphism
  - Encapsulation
  - Method Overriding

- **Testing**
  - Test Automation with `pytest`


- **Web Development**
  - Introduction to Web Frameworks (Flask, Django)
  - Building Simple Web Applications

- **APIs**
  - Working with APIs
  - RESTful Services

- **Concurrency**
  - Multithreading
  - Multiprocessing
  - Asynchronous Programming (asyncio)

- **Version Control with Git**
  - Basic Git Commands
  - Branching and Merging
  - Collaborating with GitHub


### How to Work with the PyTest?
- pip install pytest
- File name - test_name.py
- Test name - test_name_of_test():
- Assert - Actual Result == Expected Result.

### How to run the PyTest?
- open cmd ->go the the folder - pytest
-  run icon

### PyTest Commands
- pytest -h
- To run all the testcases
  - pytest 
- To run specific testcase 
  - pytest ex02_July/22072024/test_Lab181.py
- To run specific testcase with pattern
  - pytest -k "18"
- To run a specific marked Testcase 
  - Add a annotation @pytest.mark.regression
  - pytest -m "regression" ex02_July/22072024/test_Lab182.py


### How to see the Report of the PyTest Testcases?
- Make sure that allure commandline is installed
- Download the Node JS
- node -v
- npm install -g npm allure-commandline
- Verify that allure -> options
- Run your Pytestcase - pytest ex02_July/22072024/test_Lab183.py --alluredir=allure_result
- allure serve allure_result

### How to Add Request Module to the Project
- pip install requests
- pytest ex02_July/24072024/test_Lab184.py --alluredir=allure_result
- -s -help you to print the details by print command









