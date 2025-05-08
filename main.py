import sys
import requests
import os
import time

def main():
    # Get the suite run ID from command line arguments
    if len(sys.argv) > 1:
        suite_run_id = sys.argv[1]
        print(f"Received suite run ID: {suite_run_id}")
    else:
        print("No suite run ID provided")
        sys.exit(1)

    print("Hello, Github Action World!")

    # Get API key and base URL from environment variables
    api_key = os.getenv('LITMUS_API_KEY')
    base_url = os.getenv('LITMUS_API_URL')
    
    if not api_key:
        print("Error: API_KEY environment variable is not set")
        sys.exit(1)
    
    if not base_url:
        print("Error: LITMUS_API_URL environment variable is not set")
        sys.exit(1)

    # Construct the full URL
    url = f"{base_url}/{suite_run_id}/run"
    print(f'URL: {url}')
    print(f'API Key: {api_key}')

    payload = {}
    headers = {
        'api-key': api_key
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

    get_url = f"{base_url}/{suite_run_id}/runs"
    print(f'Get URL: {get_url}')
    # Poll the suite every 10 seconds until it is complete
    while True:
        response = requests.request("GET", get_url, headers=headers, data=payload)
        print(f"Polling response: {response.text}")
        ## Check if all suite_runs are completed
        suite_runs = response.json()['suite_runs']
        print(f"Suite runs: {suite_runs}")
        all_completed = True
        for suite_run in suite_runs:
            if suite_run['status'] != 'completed':
                all_completed = False

        if all_completed:
            break
        time.sleep(10)

if __name__ == "__main__":
    main()

