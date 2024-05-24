def generate_report(metrics):
    # Get a summary of the metrics
    summary = metrics.get_summary()
    
    # Print a report summarizing the metrics
    print(f"Total requests: {summary['total_requests']}")
    print(f"Errors: {summary['errors']}")
    print(f"Error rate: {summary['error_rate']:.2%}")
    print(f"Average latency: {summary['average_latency']:.4f} seconds")