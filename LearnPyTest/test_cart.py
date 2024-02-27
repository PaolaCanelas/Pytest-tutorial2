import pytest

@pytest.yield_fixture()
def tc_setup():
    print("Launch Browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("close browser")


def testAddItemtoCart():
     print("Add ITEM Successful")

def testRemoveItemFromCart():
    print("Remove Item Succesful")