# Demo in Kubernetes
Overview
---
-  目前我們得知:我們有複數個Pod(Container)，我們有以下目標須做到:
    -  Bulid Containers 
        -   Deploy Pods
    -  Enable Connectivity (建立Pod彼此的溝通方式)
        -   Create Services (Cluster IP , NodePort)  
---

K8S in Demo 
---
![](https://i.imgur.com/mLI9VQY.png)

Migo 
---
![](https://i.imgur.com/7HzARSE.png)

KaaS(Kubernetes As A Service)
---
- 指透過雲端平台(GCP,Azure,Amazon)第三方平台提供的K8S Cluster託管服務，替User管理Cluster及底層架構，使User可以有更多時間在應用程式及部署上

- 讓User可以使用UI , Google Shell ..等方式部署Cluster