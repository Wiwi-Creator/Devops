---
title: 'setup/tear_down'
---

Setup/Tear_down
===

## Beginners Guide

**Why Setup/Tear_down?**

在每次測試程式開始和結束時執行，通常用於環境設定，EX:建立資料庫資料表、建立 superuser ... 等，
讓我們在單元測試的時候時候無須再額撰寫一次這些步驟。

**Function**

在 function 等級設定 setup、teardown 時，會於每個 function 的開始以及結束時都會執行一次。

在義 setup_function 與 teardown_function 時，函式名稱要完全吻合，pytest 會自動抓取在同個檔案當中是否有相關名稱的函式，並自動執行 setup 與 teardown

```
def setup_function():
    print("setup_function")

def teardown_function():
    print("teardown_function")

def test_demo():
    assert 1 + 1 == 2

def test_demo_2():
    assert 2 + 2 == 4
```
執行結果則都會有 "setup_function" , "teardown_function"

**Model**
同Function，module 等級則是在整個 module 當中只會執行一次，而在 python 當中，每一個 .py 檔就代表一個 module

同理，也務必確認函式的名稱完全一致，pytest 會自動去蒐集是否有相關名稱的函式
```
def setup_module():
    print("setup_module")

def teardown_module():
    print("teardown_module")

def setup_function():
    print("setup_function")

def teardown_function():
    print("teardown_function")

def test_demo():
    assert 1 + 1 == 2

def test_demo_2():
    assert 2 + 2 == 4
```

## When 
- 通常使用到環境變數(EX:帳號,密碼,資料庫網址,...等)
- 可以透過Module等級方式，於測試前執行一次！