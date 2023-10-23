import sys
import demo
from pytest_mock import MockFixture


def test_mock_object(mocker: MockFixture):
    new = "test_mock"
    
    mocker.patch.object(target=sys, attribute="platform", new=new)
    
    result = demo.get_sys_platform()
    print(result)
    assert result == new