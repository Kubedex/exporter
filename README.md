# Prometheus metrics exporter for Helm Tiller

```
helm repo add kubedex https://kubedex.github.io/charts
helm repo update
helm install kubedex/kubedex-exporter
```


# Development

```
docker build -t kubedex/kubedex-exporter .
```