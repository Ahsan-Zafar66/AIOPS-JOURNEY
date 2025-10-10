import pytest


# defing setup_module, this function works only once in the beginning
def setup_module(setup):
    print("This is starting function that runs in the beginning only once")



# defining a starting function, it will work in the begining of each function
def setup_function():
    print("This is setup function, it will appear in both below functions")

# first function to test
def test_mylogin1():
    print("This is experimenting pytest")

# second function to test
def test_mylogin2():
    print("This is experimenting pytest2")


# defining teardown function, it will work in the ending of each function
def teardown_function():
    print("THis function will be executed after conducting the test on functions")


# defning teardown_module, that works only at the end of the script
def teardown_module(module):
    print("This function works only once at the end")