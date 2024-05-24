import click
from http_load_tester.core import load_test
import json

@click.command()
@click.argument('url')
@click.option('--qps', default=1, help='Queries per second')
@click.option('--duration', default=10, help='Duration of the test in seconds')
@click.option('--headers', default=None, help='Request headers as a JSON string')
@click.option('--payload', default=None, help='Request payload as a JSON string')

# The main function is the entry point of the application
def main(url, qps, duration, headers, payload):
    # Convert JSON strings to Python dictionaries
    headers = json.loads(headers) if headers else None
    payload = json.loads(payload) if payload else None
    # Perform the load test with the provided arguments and options
    load_test(url, qps, duration, headers, payload)

if __name__ == '__main__':
    # Call the main function
    main()