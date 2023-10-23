---
title: 'CICD'
---

Jenkins
===

## Jenkins 
---
- Jenkins是一個開源的自動化排程工具，是自動化CICD中最熱門的工具。

## Why Jenkins ?
- 透過腳本自動化執行，節省人力測試與降低錯誤率。
- 統一測試環境自動 Build 程式，避免開發人員因環境、套件不同而造成服務異常。
- 擁有 Project 管理功能、階段性 (Pipeline ) 式執行，對於多人開發的專案上資訊能- 夠透明通透。
- Jenkins 的功能完整，提供非常多插件 (Plugins) 來搭配各種開發語言與工具。
- 對於容器 (Container) 整合也趨於完整。

## 本機Brew安裝
透過homebrew安裝
```
brew install jenkins
```
安裝JDK (如果沒有Java的話)
```
brew cask install caskroom/versions/java8
```
運行jenkins service
```
brew services start jenkins
```
顯示 ==> Successfully started `jenkins` (label: homebrew.mxcl.jenkins)
代表可以打開囉
```
http://localhost:8080
```
## GUI

透過brew安裝完後，可以打開Jenkins UI
![](image.png)

點選Dashboard左上角New Item後，選擇Jenkins Job種類
![](image-2.png)
有以下種類:
- Freestyle project
- Pipeline
- External Job
- Muti-configuration project
- Folder
- Multibranch Pipeline
- Organization Folder

### 設定Pipeline
是一個Jenkins針對自動化習維進行設定的擴展工具，設定NewItem後
在輸入框直接輸入Jenkinsfile，並按下save
```
pipeline {
    agent any // 不指定執行 agent
    stages { // 開始宣告 Pipeline 流程
        stage('ithome 2022 pipeline') {
            // 行為宣告
            steps {
                echo 'Hello Ben ~'
            }
        }
    }
}
```
執行 Buld Now後，則會開始Pipeline流程
![](image-3.png)
且可以檢視其Console output
![](image-4.png)

## 透過 Git/GitLab/Bitbucket 管理Jenkinsfile (Multibranch Pipeline)
---
透過 SCM 對Jenkinsfile做版控及存放，也可透過多個git branch做測試。

透過NewItem建立 Multibranch Pipeline後
在Branch Sources 選擇 Source
![](image-5.png)
接著Jenkins會掃描Repo下的branch，或手動按下Scan Repository Now做手動掃描。

設定Git Credential
需要設定資訊使其可以取得Jenkinsfile。
![](image-6.png)