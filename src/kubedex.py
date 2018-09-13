#!/usr/bin/env python

from __future__ import print_function
from prometheus_client import start_http_server
from prometheus_client.core import REGISTRY, Metric
import os
import sys
import time
from lib import tiller


tiller_endpoint = 'tiller-deploy.kube-system'

if 'ENV' in os.environ:
    if os.environ['ENV'] == 'dev':
        tiller_endpoint = '127.0.0.1'


class CustomCollector(object):
    def __init__(self):
        max_retries = 5
        for i in range(max_retries):
            try:
                self.tiller = tiller.Tiller(host=tiller_endpoint)
            except Exception as e:
                print(e)
                continue
            else:
                break
        else:
            print("Failed to connect to tiller on %s" % tiller_endpoint)
            sys.exit(1)

    def collect(self):
        while True:
            try:
                all_releases = self.tiller.list_releases()
                break
            except Exception as e:
                print(e)
                continue
        metric = Metric('helm_chart_info', 'Helm chart information', 'gauge')
        for release in all_releases:
            name = release.chart.metadata.name
            version = release.chart.metadata.version
            metric.add_sample('helm_chart_info', value=1, labels={"name": name, "version": version})
        yield metric


if __name__ == "__main__":
    start_http_server(9484)
    REGISTRY.register(CustomCollector())
    print('Serving metrics on http://localhost:9484')
    while True:
        time.sleep(30)
