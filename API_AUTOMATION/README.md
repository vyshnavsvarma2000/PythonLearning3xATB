### How to Work with the Pytest
- pip install pytest
- Filename - test_name.py
- Testname - test_name_of_test():
- Assert - Expected Result == Actual Result


### How to run the Pytest
- open cmd -> go to the folder - pytest

### Pytest Commands
- pytest -h (in terminal) -> Help / commands in pytest
- To run all test cases
    - Pytest
- To run specific Test cases
    - specify the path and the filename
- To run specific Test case with pattern
    - pytest -k "pattern"
- To run marked test case
    - Add an annotation @pytest.mark.name
    - pytest -m "name" "path_of_file"

### How to see the Report of the Pytest Testcases
- Make Sure that allure command line is installed
- Download the nodejs
- node -v
- npm install -g allure-commandline
- Verify that allure is installed -> run allure in command line
- Run your Pytest test case by using ->  pytest API_AUTOMATION/test_Lab03.py --alluredir=%allure_result
- Run allure serve allure_result/