# to create pytest reports you need to install pytest-html, command: pip install pytest-html
# python -m pytest ./test_lecture_32.py -n 2 --self-contained-html --html=myreport.html
# breakdown python -m pytest ./test_lecture_32.py -n 2, run the 2 task parallely of the file test_lecture_32.py
# --self-container-html is the command to use and --html=filename.html where report will be saved



# HOW TO INSTALL ALLURE?
# Step # 1 go to allure website and go to install for windows
# then chose manual installation and download the zip file 
# unzip the zip file and then go to bin directory
# copy the path after entering in bin directory#
# go to advance system settings and go to system variable, click on PATH, click Edit, and give new path 
# now open the cm and check allure --version

# now install allure in pytest : pip install allure-pytest

# HOW TO CREATE ALLURE REPORTS
# step: 1 command to create allure reports of file: python -m pytest ./test_lecture_32.py -n 2 --alluredir="./allure_reports"
# now there will be json files in the directory you mentioned
# to read allure report go to cmd and enter the directory where allure reports are present
# run this command to read reports which are in json format: allure serve .