from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(1)) == 1*1
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(2)) == 3*2
    quadratic_multiply_test(2, 2, quadratic_multiply) == 2*2
    quadratic_multiply_test(3, 2, quadratic_multiply) == 3*2
    quadratic_multiply_test(3, 3, quadratic_multiply) == 3*3
    quadratic_multiply_test(3, 4, quadratic_multiply) == 3*4
    quadratic_multiply_test(3, 5, quadratic_multiply) == 3*5
