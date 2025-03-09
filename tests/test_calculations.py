from app.calculations import add, subtract, multipy, divide

  

def test_add():
    print("testing add function")
    
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(9, 4) == 5

def test_multipy():
    
    assert multipy(4, 3) == 12

def test_divide():
    assert divide(20, 5) == 4