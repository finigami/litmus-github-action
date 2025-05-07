import sys
import requests

def main():
    # Get the custom text from command line arguments
    if len(sys.argv) > 1:
        custom_text = sys.argv[1]
        print(f"Received custom text: {custom_text}")
    else:
        print("No custom text provided")
        sys.exit(1)

    print("Hello, Github Action World!")

    # Call the litmus run API

if __name__ == "__main__":
    main()

