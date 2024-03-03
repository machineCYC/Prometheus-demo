# Prometheus-demo

## setup python env
    - poetry install

## build api image
    - make build-api-image

## run api, promethus and grafana
    - make run-api-server

## shut down api, promethus and grafana
    - make down-api-server

## service url
    - api: http://127.0.0.1:8000/docs#
    - promethus: http://127.0.0.1:9090/graph
    - promethus metrics: http://127.0.0.1:9090/metrics
    - grafana: http://127.0.0.1:3000/dashboards
    - cadvisor: http://localhost:8080/containers/

## Reference
    - [cadvisor-metrics-for-prometheus](https://www.metricfire.com/blog/top-10-cadvisor-metrics-for-prometheus/)