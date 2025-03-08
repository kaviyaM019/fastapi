from app.calculations import add

def add(x, y):
    return x + y

def test_add():
    print("testing add function")
    sum = add(5,3)
    assert sum == 8
