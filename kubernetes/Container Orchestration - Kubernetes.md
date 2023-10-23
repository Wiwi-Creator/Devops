# Container Orchestration - Kubernetes 
###### tags: `K8S` `Container` `Pod`


Docs
---
- [Tutorials](https://kubernetes.io/docs/tutorials/)
- [CLI](https://kubernetes.io/docs/reference/kubectl/)


Micorservices Architecture 微服務架構
---
微服務架構是一種軟體開發方法論，其中複雜的Appcliation被拆解成最小的獨立元件。每個微服務都可以獨立地部署、維護和擴展，針對每個應用程式的需求和負載量，設置適當的硬體資源和容器，並且用不同的語言和工具來開發。彼此再透過API溝通、合作運行。- [Demo](https://hackmd.io/qCLHTQ-RS32aFyJgCTpJmg)

- 與傳統的 Monolithic 單體式架構比較:(所有項目都在同一系統中)

![](https://i.imgur.com/zWja3s6.png)

**主要目的** : 提高軟體和商務對接的速度，提升開發速度及產能

1.依據需求，各自交付,部署，彼此互不干涉，且易維運
2.確保整體系統的穩定性和效能。
3.降低風險(單體式架構:當一台Server掛掉，可能影響多個服務)
4.可以最大化地利用硬體資源，提高伺服器的效率。

**缺點**:
- Expensive Calls:
原本放在一起的元件都被拆成獨立的Service，會讓傳遞及溝通的成本變大
    - 實例1:每個Pod(Container)彼此做溝通或是使用service做連接
    - 實例2:做Docker run 執行Local程式時，須解決環境相容或跨環境執行的問題
    
- Complicated Composition:
如何為每個服務畫出界線，又符合軟體需要的界線->元件間的關係設計
- Eventual Consitency:
當資料被Update，處理及呈現的應用程式是不同Service，會有空窗期

Overview
---
- Container Orchestration : 在各個不同容器運行的環境中，使各應用程式能夠協同運作
- 常見的有Docker swarm , Amazon ECS , Kubernetes (k8s) ...
- What it can do:
   1.將多個主機 (Node) 整合成一個叢集 (Cluster)，每個主機都是叢集的一部分
   2.調度及運行多個Container到不同主機上
   3.服務承載有變化時，針對Container做自動擴展(Scaling)
   4.管理多個Container，自動偵測及重啟故障的Container
   5.不需存取Container，而是封裝成更高階的服務(EX:Service,Ingress)


## Guideline
1. Elements Of Kubernetes
2. Basic Architecture
3. Insatll

Elements Of Kubernetes
---
- **Pod**: 
    - K8S中運作最小的單位，每個Pod對應1個應用服務
    - 每個Pod都有一個yml檔
    - 每個Pod可以有多個Container，但最好是1個
    - 同個Pod中的Container透過Local Port number共享相同資源及網路
- **Workder Node**:
    - K8S運作中硬體最小的單位，1個Node對應1台機器(EX:本機,VM,GCP上一台computer engine或是AWS中1台EC2)
    - 每個Node中共有三個組件:kublete,kube-proxy,Container Runtime
        - kublete : 該Node的admin，管理其所有Pod並與master溝通
        - kube-proxy : 該Node的傳訊者，負責更新Node上的iptables，讓K8S中不在該Node的物件可以得知該Node上所有Pod的狀態
        - Container Runtime : Node中負責執行Container的程式，類似Docker Engine
- **Master Node**: 
    - K8S的指揮中心，一個特化的Node負責管理其他所有Node．個Master Node中有4個組件:
        - kube-apiserver:
            - 管理整個K8S所需API的接口(Endpoint)，如從CLI下kubectl指令就會把指令送到這裡
            - 每個Node間需透過apiserver轉介
            - 負責K8S中每個請求的身份認證及授權
        - etcd:用來存放K8S的Cluster的Key-value store，當Master故障時，可以透過其還原
        - kube-controller-manager:
            - 負責管理並運行K8S controller的組件．Controller是一個K8S中負責監視Cluster狀態的Process(EX:Node Controller,Replication Controller 這些Process會在Cluster與預期狀態(desire state)不符時嘗試更新現有狀態)
            - Controller-Manager的監視與更新也需透過apiserver達成
        - kube-scheduler:Pods的調度員，Scheduler會監視新建立但還沒有被指定要跑在哪個Node的Pod，並根據各個Node的資源及硬體等去協調適合放置的Node
- **Cluster**:
    K8S中Node與Master的集合
    
    
## Build
---
![](https://i.imgur.com/BfoJ220.png)




-  **Basic** 
    -  **K8S如何建立Pod?**
    
    當User要部署新的Pod到Cluster時，需先透過CLI(kubectl)輸入建立Pod的指令，而此指令會經過一層認證去審核傳送方的身份後，傳到master Node中的API Server，而API Server把指令備份到etcd
    
    接下來controller-manager會從API Server收到需要創建新的Pod的訊息，並建立新的Pod．最後Scheduler定期訪問API Server時，會詢問Controller-manager是否有新的Pod，有發現新的Pod，則Scheduler則會把Pod配送到最適合的Node上
        

## Install
- [Kubernetes Minikube](https://hackmd.io/qXLMkvrhQ8GxWrmR8I4ypg)
- [Elements In Kubernetes](https://hackmd.io/fw22d0eMSHmiaslgiUuD9w)
- [Demo](https://hackmd.io/qCLHTQ-RS32aFyJgCTpJmg)






