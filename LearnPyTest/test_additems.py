import pytest

@pytest.mark.sanity
def testlogin():
     print("login Successful")

@pytest.mark.regresion
def testLogoff():
    print("logoff Successful")

def testcacullation():
    assert  2+2 == 4

