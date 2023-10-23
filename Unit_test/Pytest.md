---
title: 'Pytest'
---

Pytest
===

## Beginners Guide
Pytest是作為python整合setup/teardown/fixture..等測試常用功能的測試框架。


install 
```
pip install pytest
```

## Getting start

**格式** 

前綴帶有test的檔案(EX:test_function.py)

**Fixture** 
```
import pytest

@pytest.fixture()
def my_data():
    return "dataset"

class MyTest2:
    def test_second_testcase(self, my_data):
        print("data: ", my_data)
        assert my_data == "dataset"
```
執行
```
pytest test_function.py
```

- @pytest.fuxture 這一行下方的function就會被轉成fixture, fixture可以當作參數直接傳到 testcase內.
- fixture被視為設定檔, 所以pytest提供了conftest.py的設定檔來存放所有fixture
- assert 及斷言，測試程式執行結果是否如預期。

預期結果為 Pass 

撰寫Unit test時，可以使用該結構去完成測試案例！
