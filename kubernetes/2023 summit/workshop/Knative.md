---
title: 'Kubernetes Summit 2023 - Knative'
---

Kubernetes Summit 2023 - Knative
===
Google

## Deploying a GKE cluster with Knative Serving

### Issues

- Set Environment Variables
- Enable Google APIs
- Set service account

- Set Google Cloud CLI configuration variables
```
gcloud config set run/cluster $CLUSTER_NAME
gcloud config set run/cluster_location $ZONE
gcloud config set run/platform gke
```
- You could check the result with following command
```
gcloud config list
```

- Create the GKE cluster
``` 
gcloud container clusters create $CLUSTER_NAME \
  --addons=HttpLoadBalancing,CloudRun \
  --zone=$ZONE \
  --machine-type=n1-standard-4 \
  --enable-stackdriver-kubernetes \
  --scopes=cloud-platform,logging-write,monitoring-write,pubsub
```
- List Kubernetes nodes of your cluster 

```
gcloud container clusters get-credentials $CLUSTER_NAME --zone=$ZONE --project $PROJECT_ID
kubectl get nodes
```
## Verify the Knative Serving deployment
Command
```
kubectl get deployment -n knative-serving
```
Output
```
NAME                READY   UP-TO-DATE   AVAILABLE   AGE
activator           1/1     1            1           2m3s
autoscaler          1/1     1            1           2m3s
controller          1/1     1            1           2m2s
metrics-collector   1/1     1            1           32s
webhook             1/1     1            1           2m2s
```

## Integrating GCP managed Prometheus for Knative

- Update Helm:

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

- Install the Prometheus Operator by using Helm:

```
git clone https://gitlab.com/owensengoku/serverless-on-kubernetes.git
cd ~/serverless-on-kubernetes/prometheus
kubectl create namespace monitoring
helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring -f values.yaml --version 41.4.0
```

- Apply the ServiceMonitors/PodMonitors to collect metrics from Knative

```
kubectl apply -f servicemonitor.yaml
```

- Load the dashboards by applying the following configmaps.
```
kubectl apply -f dashboards.yaml       
```
- Verify Prometheus & Grafana
```
kubectl edit -n monitoring service prometheus-grafana
```

### Autoscaling
 
