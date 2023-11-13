---
title: 'Kubernetes Summit 2023'
---

Kubernetes Summit 2023
===
## Issues

- Background
- Duet AI
- Why K8S?
- Infra Before V.S. After 
- Workshop
- Lecture

##  Background

Google所提供的數據 

在 2021年 僅約 40 % 的公司 已經 Containerlized

預估 在 2027 90 %的公司 Containerlized

也就是說 容器化 幾乎可以說是趨勢。

另外也越來越多的公司上雲，大部分的機器也將從本地轉移至雲端。

後VM時代將到來。雲原生服務也變得更重要。

## Why K8S?

### 
- Better For AI

    - MLOps : 針對套件有提升很大的延展性。(架設Node及部署套件快速)

- Manage Multi-Container Infra : 用來管理多個容器(容器間如果有溝通，K8S優勢更會呈現。)

- Openness & Ecosystem 

    開源社群環境及越來越多的相關工具。

- Health Checks & Self-healing

  - 持續監控容器和節點的健康狀況。如果發現問題，可以嘗試重啟失效的容器
  
  - 根據負載變化，能夠自動擴展或縮減Node的數量。

- Secret Management 

  - 可以管理Secret，並更新和部署密鑰而不用重建Image。


### In Case

- Maicoin (In-house):

  - 認為Migo案例適合K8S，透過 Node Auto-scale 可以有效節省機器成本(更彈性地伸縮Node)。

  - 有效管理多個Container。

- Webcomm (SI廠商): 

  - 搭配K8S並提供對應Ifra報價可以提高，且K8S需求越來越高。

  - 針對高度容器化的公司，有效管理多個Container。

- Google (K8S 提供商): 

  - 當Container之前有彼此有連線(Network)時，可以透過K8S監控整個Infra。


## Infra Before V.S. After

### Before 
- 自架K8S (EX: AWS EC2 as VM)

   - infra : Autoscaling有自行判斷

- Cloud- half-managed

  - EKS (AWS K8S serveless)

  - Workder -> self-managed

    - Log 先入檔案，再透過Filebeats去收

### CI/CD
- Before ：Jenkins + kubectl deploy
- 現在：github Action + Argo CD deploy

  - Argo 優點：更容易看到版本差異

### IaC
- Ansible > CloudFormation > Terraform
- Terraform (管理多座的k8s cluster)

  - 跨平台

  - state跟infra實際狀態有差的時候比較好修

  - modularizef

### Logging

- Before : log 到檔案，需維運 file fluentbit
- Now : [kube-logging (Logging operator)](https://kube-logging.dev/)
，簡化管理，避免 config 散落各地

## Workshop

## Lecture

