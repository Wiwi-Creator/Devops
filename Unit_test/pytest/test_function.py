import demo


def test_mock_function(mocker):
    return_value = 100

    mocker.patch(target="demo.add",
                 return_value=return_value)

    result = demo.calculate(num1=10, num2=10)
    print 
    print(result)

    assert result == return_value