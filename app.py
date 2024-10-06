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
    # Start the metrics server on port 8080
    start_http_server(8080)

    while True:
        handle_request("GET")  # Simulate handling GET requests
