# HTTP Load Tester

## Description

HTTP Load Tester is a general-purpose HTTP load-testing and benchmarking library written in Python. It allows users to simulate high-traffic scenarios by sending a specified number of requests per second to a target URL. This tool provides detailed reports on latencies, error rates, and can be configured with custom headers and payloads.

## Features

- Custom QPS (Queries Per Second): Generate requests at a specified QPS.
- Configurable Duration: Run tests for a specified duration.
- Detailed Metrics: Reports total requests, error rates, and average latency.
- Retry Logic: Retries requests on failure up to 3 times.
- Custom Headers: Specify custom headers for requests.
- Custom Payloads: Send custom payloads with requests.
- Supports Multiple HTTP Methods: Supports GET and POST methods based on the presence of a payload.
- Unit Tests: Comprehensive unit tests to ensure code quality and reliability.

## Usage

### Local Usage

1. Clone the Repository: `git clone <repository_url>` and `cd http_load_tester`
2. Set Up a Virtual Environment: `python3 -m venv venv` and `source venv/bin/activate` (On Windows, use `venv\Scripts\activate`)
3. Install Dependencies and Package: `pip install -e .`
4. Run the Load Test: `http_load_tester <url> --qps <qps> --duration <duration> [--headers '<headers>'] [--payload '<payload>']`

#### Examples

- Without Headers and Payload:
  `http_load_tester https://httpbin.org/get --qps 100 --duration 5`
- With Headers:
  `http_load_tester https://httpbin.org/get --qps 100 --duration 5 --headers '{"Authorization": "Bearer your_token"}'`
- With Payload:
  `http_load_tester https://httpbin.org/post --qps 100 --duration 5 --payload '{"key1": "value1", "key2": "value2"}'`
- With Both Headers and Payload:
  `http_load_tester https://httpbin.org/post --qps 100 --duration 5 --headers '{"Authorization": "Bearer your_token"}' --payload '{"key1": "value1", "key2": "value2"}'`

### Using Docker

1. Build the Docker Image: `docker build -t http_load_tester .`
2. Run the Docker Container: `docker run http_load_tester <url> --qps <qps> --duration <duration> [--headers '<headers>'] [--payload '<payload>']`

#### Examples

- Without Headers and Payload: `docker run http_load_tester https://httpbin.org/get --qps 100 --duration 5`
- With Headers: `docker run http_load_tester https://httpbin.org/get --qps 100 --duration 5 --headers '{"Authorization": "Bearer your_token"}'`
- With Payload: `docker run http_load_tester https://httpbin.org/post --qps 100 --duration 5 --payload '{"key1": "value1", "key2": "value2"}'`
- With Both Headers and Payload: `docker run http_load_tester https://httpbin.org/post --qps 100 --duration 5 --headers '{"Authorization": "Bearer your_token"}' --payload '{"key1": "value1", "key2": "value2"}'`

## Unit Test

- Run Tests: `python -m unittest discover -s tests`
