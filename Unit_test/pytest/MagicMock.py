from pytest_mock import MockFixture


def test_mock_example(mocker):
    # 创建一个模拟对象
    mock_obj = mocker.Mock()
    
    # 打印模拟对象
    print(mock_obj)
    
test_mock_example()