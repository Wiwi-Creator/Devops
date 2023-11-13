---
title: 'Resource as Code for Kubernetes: Stop kubectl apply'
---

Resource as Code for Kubernetes: Stop kubectl apply
===

## yaml 地獄
yaml上版控變成yaml維護師

## HELM
讓你從管理 K8s object 變成一整包的 package (更高層級的封裝)

配合 HELM 生態系有現成的一堆人家已經設定好的 helm chart 可以直接使用。


更高層級的封裝：
版本更新可以更具一致性
維護更容易

## ARGO CD
ARGO CD 在使用上的流程整合更容易：

- git generator : 讀取 git repo 指定的路徑，只要有內容變化就會自動產生新的 ApplicationSet 產生出一組新的應用集合定義，就可用於部署。

- cluster generator : 可在 yaml 設定裡定義 matchLabel ，定義當碰到某種 label 時根據不同的設定去使用不同的 k8s 服務(ex: EKS, AKS, GKE)