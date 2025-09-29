import sys
import requests
import os
import time
import json

def main():
    # Get the suite run ID from command line arguments
    if len(sys.argv) > 1:
        suite_id = sys.argv[1]
        print(f"Running Suite ID:: {suite_id}")
    else:
        print("No suite run ID provided")
        sys.exit(1)

    # Get API key, base URL, config, and environment ID from environment variables
    api_key = os.getenv('LITMUS_API_KEY')
    base_url = os.getenv('LITMUS_API_URL')
    config_str = os.getenv('LITMUS_CONFIG')
    environment_id = os.getenv('LITMUS_ENVIRONMENT_ID')
    environment_name = os.getenv('LITMUS_ENVIRONMENT_NAME')
    environment_variables = os.getenv('LITMUS_ENVIRONMENT_VARIABLES')

    print(f'{base_url} - url to run suite')
    
    if not api_key:
        print("Error: LITMUS_API_KEY environment variable is not set")
        sys.exit(1)
    
    if not base_url:
        print("Error: LITMUS_API_URL environment variable is not set")
        sys.exit(1)

    # Construct the full URL
    url = f"{base_url}/{suite_id}/run"

    # Parse config JSON
    try:
        if config_str and config_str.strip():
            config = json.loads(config_str)
        else:
            config = None
    except json.JSONDecodeError as e:
        print(f"Malformed config JSON for {config_str}: {e}")
        sys.exit(1)

    # Build payload
    payload = {}
    
    # Add config only if it's provided and not empty
    if config is not None:
        payload["config"] = config
    
    # Add environment_id only if it's provided (even if blank)
    if environment_id is not None and environment_id != '':
        payload["environment_id"] = environment_id
    if environment_name is not None and environment_name != '':
        payload["environment_name"] = environment_name
    if environment_variables is not None and environment_variables != '':
        # parse variables json
        try:
            env_vars = json.loads(environment_variables)
        except json.JSONDecodeError as e:
            print(f"environment variables must be valid JSON readable string: {e}")
            sys.exit(1)
        payload["environment_variables"] = env_vars
    
    headers = {
        'apikey': api_key
    }

    try:
        response = requests.request("POST", url, headers=headers, json=payload)
        print(f"Response: {response.json()}")
        response.raise_for_status()  # Raises an HTTPError for bad responses
        response_data = response.json()
        print(response_data)
        print(response_data['message'])
        suite_run_id = response_data['suite_run_id']
    except requests.exceptions.RequestException as e:
        print(f"Error starting suite run: {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Unexpected response format: missing key {e}")
        sys.exit(1)
    get_url = f"{base_url}/{suite_id}/run/{suite_run_id}"
    # Poll the suite every 10 seconds until it is complete
    print(f"Suite ID: {suite_id}")
    while True:
        try:
            time.sleep(10)
            response = requests.request("GET", get_url, headers=headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            # print(f"Polling response: {response.text}")
            response_json = response.json()
            ## Print Success: xx | Failure: xx | Skipped: xx
            success_count = int(response_json.get('success_count', 0))
            failure_count = int(response_json.get('failure_count', 0))
            error_count = int(response_json.get('error_count', 0))
            print(f"Success: {success_count} | Failure: {failure_count} | Error: {error_count}")
            
            if response_json.get('status') == 'completed':
                # Write the final result to GitHub output
                github_output_file = os.getenv('GITHUB_OUTPUT')
                if github_output_file:
                    with open(github_output_file, 'a') as f:
                        f.write(f"suite-result={json.dumps(response_json)}\n")
                # print(f"Suite completed successfully!")
                # if failure count is not 0 and error count is not 0, then return failure
                if failure_count != 0 or error_count != 0:
                    print(f"Suite completed with failures or errors")
                    sys.exit(1)
                else:
                    print(f"Suite completed successfully!")
                    sys.exit(0)
                break
        except requests.exceptions.RequestException as e:
            print(f"Error polling suite status: {e}")
            sys.exit(1)
        except KeyError as e:
            print(f"Unexpected response format during polling: missing key {e}")
            sys.exit(1)
        

if __name__ == "__main__":
    main()






