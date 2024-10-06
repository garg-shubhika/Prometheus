## Step 1: Download and Install Prometheus

1. Open your terminal.
2. Download the Prometheus tarball:

```bash
   wget https://github.com/prometheus/prometheus/releases/download/v2.54.1/prometheus-2.54.1.linux-amd64.tar.gz
```

3. Extract the downloaded tarball:

```bash
tar xvfz prometheus-2.54.1.linux-amd64.tar.gz
```

4. Change to the Prometheus directory:
```bash
cd prometheus-2.54.1.linux-amd64
```

5. Start Prometheus with the default configuration:

```bash
./prometheus --config.file=prometheus.yml
```

6. Install prometheus_client
```bash
pip3 install prometheus_client
```

7. Write app.py
```bash
from prometheus_client import start_http_server, Counter
import random
import time

# Create a counter metric
REQUEST_COUNT = Counter('http_requests_total', 'Total number of HTTP requests', ['method'])

# Simulate handling requests
def handle_request(method):
    REQUEST_COUNT.labels(method=method).inc()
    time.sleep(random.uniform(0.1, 0.5))  # Simulate variable processing time

if __name__ == '__main__':
    # Start the metrics server on port 8000
    start_http_server(8000)

    while True:
        handle_request("GET")  # Simulate handling GET requests
```
8. Run app.py
```bash
python app.py
```
9. Open the prometheus.yml file in the Prometheus directory. Add the below configuration
```bash
scrape_configs:
  - job_name: 'python_app'
    static_configs:
      - targets: ['localhost:8000']  # Python app metrics endpoint
```
10. Restart Prometheus
11. Your Python application will expose metrics at:
```bash
http://localhost:8000/metrics
```
12. You can view the Prometheus server at:
```bash
http://localhost:9090/graph
```
13. To query the total number of HTTP requests, use the query:
```bash
http_requests_total
```
