---
title: 'Fixture'
---

Fixture
===

## Beginners Guide

**建立**
通常會避免混亂，將fixture寫在fixture.py要用時再import。

fixture裝飾器參數介紹:
- scope：表示作用域，預設為 "function"，亦即每個有用到此 fixture 的 test case 都會執行，另外還有 module、class 以及 session 三種
- name：用來設定 fixture 的別名，預設為函式名稱
- autouse：預設為 False，若為 True，則會自動進行使用 (根據 scope 作用域而定)

程式解釋:
- 利用 @pytest.fixture 標註該函式為 fixture
- 利用 fake_useragent 隨機生成一個 User-Agent (需另外安裝 - fake-useragent 套件)
- 回傳 headers 給有使用此 fixture 的 test case

```
import pytest
from fake_useragent import FakeUserAgent

@pytest.fixture(name="headers", scope="function", autouse=False)
def headers_fixture() -> dict:
    ua = FakeUserAgent()
    headers = {"User-Agent": ua.random}
    return headers
```

**使用**
在 test case 接收參數的地方打上剛剛為 fixture 命名的名稱 (若無則預設為 fixture 的 function name)，接著我們就可以在 test case 內使用此 fixture 回傳出的內容了。
程式解析:
- import 要使用的 fixture 
- 利用 https://httpbin.org/headers 來取得我們送出去的 headers
- 最後驗證取得的 headers 和我們利用 fixture 製作的 headers 是否相等

```
import requests
from fixtures import headers_fixture

# 單純不讓 pycharm 跳驚嘆號，沒有實際用途
use_fixtures = [headers_fixture]


def test_assert_headers(headers: dict):
    url = "https://httpbin.org/headers"  
    res = requests.get(url=url, headers=headers)

    print(res.status_code)
    print(res.json())

    assert res.status_code == 200
    assert res.json()['headers']["User-Agent"] == headers["User-Agent"]
```
## 使用時機
- 為test_case建立環境時:
    若是有多個test case在測試前需要一些環境建置,參數準備，則很適合。
- 當不希望使用setup/teardown時:
    使用 setup、teardown 會造成該 .py 檔內的所有 test case 都被引響，而 fixture 若沒有被寫在 test case 接收的參數內，則不會被影響 (除非作用域不為 function 且 autouse=False)。


