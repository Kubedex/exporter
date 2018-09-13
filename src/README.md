# kubedex

Local dev config connects to Tiller grpc endpoint on localhost via port-forward.

Start minikube and then port-forward using.

```
kubectl port-forward $(kubectl get pod --selector app=helm,name=tiller -o jsonpath={.items..metadata.name} -n kube-system) 44134:44134 -n kube-system
```

Install the requirements.

```
pip install -r requirements.txt
```

Then start the exporter with.

```
ENV=dev ./kubedex.py
```

You can now curl the metrics endpoint.

```
curl localhost:9484/metrics
```

# Production

This exporter will try to connect to tiller-deploy.kube-system on default grpc port 44134.

Enable Prometheus scrape annotation to collect the metrics.
