import sys
import requests
import os

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
    api_key = os.getenv('API_KEY')
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

if __name__ == "__main__":
    main()

