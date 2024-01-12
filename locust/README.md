# Locust

<https://locust.io/>

<https://abdelrhmanhamouda.github.io/locust-k8s-operator/#where-can-it-run>

## Dedicated AKS for Locust

```bash
az aks create --resource-group rg-apim1 --name akslocust --network-plugin azure --node-vm-size Standard_D4s_v5 --node-count 64 --vnet-subnet-id /subscriptions/c9c8ae57-acdb-48a9-99f8-d57704f18dee/resourceGroups/rg-apim1/providers/Microsoft.Network/virtualNetworks/vnet-apim1/subnets/aks-subnet --service-cidr 10.200.0.0/16 --dns-service-ip 10.200.0.100 --enable-azure-monitor-metrics

az aks get-credentials --resource-group rg-apim1 --name akslocust
```

## Install

```bash
helm repo add locust-k8s-operator https://abdelrhmanhamouda.github.io/locust-k8s-operator/

kubectl config use-context akslocust

kubectl get nodes

helm install locust-operator locust-k8s-operator/locust-k8s-operator

kubectl create configmap demo-test-map --from-file demo_test.py

kubectl apply -f locusttest-cr.yaml
```

## View Locust UI

```bash
kubectl get pods -o wide
kubectl expose pod demo-test-master-9xpsh --name=demo-test-master-web --type=NodePort --port=8089
kubectl port-forward svc/demo-test-master-web 8089:8089
```

## Uninstall

```bash
kubectl delete -f locusttest-cr.yaml
kubectl delete configmap demo-test-map
kubectl delete svc demo-test-master-web
helm uninstall locust-operator
```
