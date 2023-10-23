---
title: 'Elements In Kubernetes'
---

Elements In Kubernetes
===

每個Pod都有一個身份證，也就是屬於Pod的Yaml檔

---
**API Vsersion**:The version of the K8s API. --> 該元件的版本號
**kind**:The type of object we are trying to create.--> 該元件的屬性(EX:Pod,Node,Service..)
**metadata**:
    - name: 該Pod的名稱 
    - labels: 指定該Pod的標籤 
**spec**: Specification Depends on the object we are going to create.
    - (container)name:指定運行的Container 
    - (container)image:指定Container要運行的image
    - (container)ports: 指定該Container有哪些Ip供外部做存取
kubernetes-demo.yml
```
apiVersion: v1
kind: Pod
metadata:
    name: myapp-pod
    labels: 
        app: myapp
        type: front-end
spec:
    containers: 
        - name: nginx-container
          image: nginx  
          ports:
            - containerPort: 3000
```
**接下來透過kubectl建立Pod** 
```
kubectl create -f kubernetes-demo.yml
```
有了created的字樣，代表成功建立了Pod
我們可以看到運行中的pods
![](https://i.imgur.com/b5hD6rr.png)
```
kubectl get pods
```
**連線至Pod服務資源**
建立好Pod後。 Pod 中所指定的 port，跟Local端的 port 是不相通的。因此，我們必須還要透過 kubectl port-forward，把我們兩端的 port 做 mapping。
```
kubectl port-forward kubernetes-demo-pod 3000:3000
```
將兩邊Port Mapping後，即可正常檢視囉!

Service
===
K8S中用來定義多個Pod如何被連線及存取的元件->當需要多個Pods同時被連線時，我們可以使用到Service
**spec**:
    - selector:意指該Service的規則是用哪些Pods，在建立Pod時，有在label上加標籤，於是可以透過所加的標籤(app:demoApp)去找到屬性為demoApp的Pods們
    - ports
- targetPort:指定Pod上允許外部資源存取的Port Number
- port:指定Pod上的targetPort要mapping到Service中Cluster IP中的哪個Port
- nodeport:指定Pod上的targetPort要mapping到Node上的哪個port
    
service.yml
```
apiVersion: v1
kind: Service
metadata:
   name: my-service
spec:
   selector:
     app: demoApp
   type: NodePort
   ports:
     - protocol: TCP
       port: 3001
```
透過service.yml建立Service元件
```
kubectl create -f service.yaml
```
透過kubectl get services取得最新service資料
```
kubectl get services
```
有了建立好的Service後，可以透過2種方式連線我們的Pod的服務資源，首先從外部連線到Pod的資源服務，必須先有K8S Cluster對外開放的IP(這邊使用minikube)
```
minikube ip
```
得到ip後，打開瀏覽器並輸入ip加上yaml檔中指定的nodePort，就可以看到了
若不從瀏覽器，也可直接從minikube連線到Pod
```
minikube ssh
```
並輸入指令
```
curl <Cluster-IP>:<port>
```
其中Cluster-Ip及為透過kubectl get services得到的IP，port則是yaml檔指定

Deployment
===
今天當我們同時要把一個 Pod 做橫向擴展，也就是複製多個相同的 Pod 在 Cluster 中同時提供服務，並監控如果有 Pod 當機我們就要重新把它啟動時，如果我們要一個 Pod 一個 Pod 透過指令建立並監控是很花時間的。因此，我們可以透過 Deployment 這個特殊元件幫我們達成上述的要求。


**spec**:

- replicas:指定要建立多少個相同的 Pod，即所謂的 Desire State，當Cluster 運行時如果 Pod 數量低於此數字，K8S就會自動增加 pod，反之就會關掉 Pod
- template:指定這個 Deployment 建立的 Pod 們統一的設定，包括 metadata 以及這些 Pod 的 Containers，這邊我們就沿用之前建立 Pod 的設定
- selector指定這個 Deployment 的規則要適用到哪些 Pod，在這邊就是指定我們在 template 中指定的 labels

deployment.yml
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: demoApp
  template:
    metadata:
      labels:
        app: demoApp
    spec:
      containers:
        - name: kubernetes-demo-container
          image: digdag_server
          ports:
```
透過指定建立
```
kubectl create -f deployment.yaml
```
檢視建立的deployment
```
kubectl get deploy
```
可以確認成功建立了3個Pod，即所謂Pod的自動擴展，另一個優點是可以幫我們做到無停機系統升級(Zero Downtime Rollout)
意義為:當需要更新Pod時，K8S不會直接砍掉全部Pod，而是建立新Pod，等新的Pod正常運行後才來取代舊的Pod

範例:更新Pod對外的Port，可透過指令
```
kubectl edit deployments my-deployment
```
將檔案中的port修改3001後儲存，K8s會自動幫我們做更新
這時使用kubectl get pods會看到，會永遠保持"3"個Pods運作，若有新的Pod是屬於"ContainerCreating"階段，其並不會關掉對應的Pod

靠著這樣的機制，可以確保系統在更新時，Server不會有無法使用的狀況

以下指令看到我們更改過的版本
```
kubectl rollout history deployment my-deployment
```
或是透過指令，Rollback到以往的版本
```
kubectl rollout undo deploy my-deployment --to-revision=2
```

Ingress
===
