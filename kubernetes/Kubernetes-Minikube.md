---
title: 'Kubernetes-Minikube'
---

Kubernetes-Minikube
===

## Beginners Guide

實際操作Kubernetes前，需要下載Minikube,VirtualBox,kubectl三個套件

- **Minikube** : 
    1個Google發布的輕量級工具，讓User體驗K8S Cluster
    其會在Local建立VM，並在其中運行1個Single-Node的K8S Cluster
- **VirtualBox** : 
    因為Minikube會透過VM執行K8S，因此需要安裝一個跑虛擬化的工具
- **kubectl** : 
    K8S的CLI工具

User story
---
如何建立1個Pod
**Minikube**
```
minikube start
```
檢視minikube狀態
```
minikube status
```
停止minikube運作
```
minikube stop
```
透過ssh進入minikube
```
minikube ssh
```
查詢minikube對外ip
```
minikube ip
```
透過minikube提供瀏覽器GUI檢視Cluster狀況
```
minikube dashboard
```

:::info
**Find this document incomplete?** Leave a comment!
:::

###### tags: `Templates` `Documentation`
