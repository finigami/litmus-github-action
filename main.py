import sys
import requests
import os
import time

def main():
    # Get the suite run ID from command line arguments
    if len(sys.argv) > 1:
        suite_id = sys.argv[1]
        print(f"Running Suite ID:: {suite_id}")
    else:
        print("No suite run ID provided")
        sys.exit(1)

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
    url = f"{base_url}/{suite_id}/run"

    payload = {}
    headers = {
        'api-key': api_key
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json()['message'])
    suite_run_id = response.json()['suite_run_id']
    get_url = f"{base_url}/{suite_id}/run/{suite_run_id}"
    # Poll the suite every 10 seconds until it is complete
    print(f"Suite ID: {suite_id}")
    while True:
        response = requests.request("GET", get_url, headers=headers)
        print(f"Polling response: {response.text}")
        ## Check if all testruns are completed
        testruns = response.json()['testruns']
        print(f"Suite runs: {testruns}")
        all_completed = True
        for testrun in testruns:
            if testrun['status'] != 'success':
                all_completed = False

        if all_completed:
            break
        time.sleep(10)

if __name__ == "__main__":
    main()

