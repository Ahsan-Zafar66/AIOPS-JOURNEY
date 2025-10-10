import pytest

# defining a function that takes a person name and age, as I have passed only one tuple so this function will run once
# adding a pytest parametrize
@pytest.mark.parametrize("name,age",[("ahsan",24),])
def test_data1(name,age):
    print(" The person age is")
    print(name,age)
    print("=" * 20)


# in this function i am passing two tuples so this function will run 2 times
# first time ahsan and 24 are the function argument values and 2nd time ahmed and 26
@pytest.mark.parametrize("name,age",[("ahsan",24),("ahmed",26)])
def test_data2(name,age):
    print(" The person age is")
    print(name,age)
    print("=" * 20)


# now rather then passing values above function, i can define a function containing values and call it
def my_cred():
    return [("ahsan",24),
            ("ahmed",26),
            ("nasir",25)

    ]

# now calling this function
@pytest.mark.parametrize("name,age",my_cred())
def test_data3(name,age):
    print(" The person age is")
    print(name,age)
    print("=" * 20)


# function to check if two things are same or not

def test_verify_title():
    expected_title= "Education Benefits All | Al Nafi"
    actual_title = "Al Nafi"

# if actual_title == expected_title:
#     print("My test cases is passed ")
# else:
#     print("my test cases is failed ")
    assert actual_title == expected_title ,"My matched are not as expected "