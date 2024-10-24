def soma (a,b):
    return a+b

def subtração (a,b):
    return a - b

def multplicação(a,b):
    return a * b

def divisão(a,b):
    return a/b

def test_se_a_mais_b():
    assert soma (8,9) == 17
    assert soma (10,5) == 15
    assert soma (8,5) == 13

def test_subtracao ():
    assert subtração (5,3) == 2
    assert subtração (3,3) == 0   
    assert subtração (5,4) == 1   
        
def test_multiplicacao ():
    assert multplicação (4,7) == 28
    assert multplicação (1,5) == 5     
    assert multplicação (6,5) == 30            

def test_divisão ():
    assert divisão (10,5) == 2
    assert divisão (20,2) == 10 
    assert divisão (40,2) == 20     