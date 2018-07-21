def test1():
    print("This is test")
    print("This is test")
    print("This is test")
    print("This is test")
    print("This is test")

def test2():
    print("This is test2")
    print("This is test2")
    print("This is test2")
    print("This is test2")
    print("This is test2")

class TestClass:
    def __init__(self):
        test = 1

    def test_func(self):
        print("test_func")

    def test_func1(self):
        print("test_func")

class TestClass1:
    def __init__(self):
        test = TestClass()

    def test_func2(self):
        print("test")

    def test_func3(self):
        print("test")