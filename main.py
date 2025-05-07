import sys
import requests
import os

def main():
    # Get the custom text from command line arguments
    if len(sys.argv) > 1:
        suite_run_id = sys.argv[1]
        print(f"Received custom text: {suite_run_id}")
    else:
        print("No custom text provided")
        sys.exit(1)

    print("Hello, Github Action World!")

    # Get API key from environment variable
    api_key = os.getenv('API_KEY')
    if not api_key:
        print("Error: API_KEY environment variable is not set")
        sys.exit(1)

    # Call the litmus run API
    url = "https://qualiumdev.finigami.com/api/v1/suite/suite_run_id/run"
    print(f'url: {url}')
    print(f'api_key: {api_key}')

    payload = {}
    headers = {
        'api-key': api_key
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

if __name__ == "__main__":
    main()

