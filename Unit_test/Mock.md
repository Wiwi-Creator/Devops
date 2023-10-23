---
title: 'Mock'
---

Mock
===

## Beginners Guide

**Why Mock?**

測試條件有限，如遭遇環境難以準備(EX:網路server間的測試,DB間的讀寫)
甚至是使用場景->單元,整合,黑白箱..等

有兩種測試方式 :
- 利用fixture準備測試環境:但缺點是測試code開發長,測試時間也很長。
- 準備需虛假的資料:對code做模擬，無法達到最終效果，但確保測試覆蓋率，也避免重複測試的時間。

**What is Mock?**

在python中，所有都是object。而mock便是在測試時，在不修改code前提下，替換某些object，使其模擬了測試環境。

**Packages**

- unittest.mock: python內建的mock庫，有Mock,MagicMock,path可以使用。
- pytest-mock: 第三方插件，基於unittest.mock構建。
- monkeypatch: pytest內建的fixture，也提供mock功能，通常用於修改或模擬環境。
- mockito: 第三方，提供API創建模擬對象。

## Pytest-mcok

pytest-mock是pytest的套件，提供了mocker的fixture，僅在測試function,method時生效，而不用自行包裝。

## Pytest patch 替換
patch:
- test case 當中的參數部分打上 mocker 即可進行使用，可以使用 MockFixture 用來提示型態
- 建立一個變數用來存放假的回傳資料，此樹使用 new (對齊 mock.path 函式的參數)

1.使用 mocker.patch 直接進行抽換:
- target：使用 "字串" 指定要抽換的函式路徑，當成式執行到此函式時，會直接回傳一個假資料並不會實際執行該函式
- return_value：指定要回傳的假資料

demo.py
```
def add(num1, num2):
    return num1 + num2
def calculate(num1, num2):
    add_result = add(num1=num1, num2=num2)
    return add_result
```

test.py
```
import demo
def test_mock_function(mocker: MockFixture):
    return_value = 100

    mocker.patch(target="demo.add",
                 return_value=return_value)

    result = demo.calculate(num1=10, num2=10)
    print(result)

    assert result == return_value
```

2.使用 mocker.patch.object 進行變數的替換:
- target：指定要替換的物件
- attribute：指定要替換的物件的屬性
- new：要回傳的假資料
demo.py
```
import sys

def get_sys_platform():
    platform = sys.platform
    return platform
```
test.py
```
import demo
def test_mock_object(mocker):
    new = "test_mock"
    mocker.patch.object(target=sys,
                        attribute="platform",
                        new=new)
    result = demo.get_sys_platform()
    assert result == new
```
## Pytest 其他 method 說明
init:
- name: mock對象的標註。
- spec: 設定對象屬性。
- return_value: 使用mock對像所回傳的值。
- side_effect: 覆盖return_value, 當mock對像被使用時回傳。

Assert_method:
-     assert_called_with: 斷言mock對像 的参数是否正确
-     assert_called_once_with: 檢查該mock對像是否被使用多次並異常
-     assert_any_call: 檢查該mock對像是否被使用
-     assert_has_calls: 檢查該mock對像是否被使用參數和順序是否正确

Management:
-    attach_mock: 新增mock對像到另一個mock對像中
-    configure_mock: 重新設定mock對像的回傳值
-    mock_add_spec: 新增mock對像屬性
-    reset_mock: 重置mock對像

Count:

-  called: 对象调用的访问器
-  call_count: 对象调用次数
-  call_args: 对象调用时的参数（最近）
-  call_args_list: 获取对用时所有的参数list
-  method_calls: 统计对象调用的所有方法，返回list
-  mock_calls: 统计工厂调用、方法调用



