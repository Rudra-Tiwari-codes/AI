# Import necessary libraries
import os
import requests
import json

# Set your API key (ideally from environment variables)
# You'll need to replace this with your actual API key or set the environment variable
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    print("Please set your API key using one of these methods:")
    print("1. Set environment variable: set OPENAI_API_KEY=your_api_key_here")
    print("2. Or create a .env file with: OPENAI_API_KEY=your_api_key_here")
    exit(1)

# API endpoint
url = "https://api.openai.com/v1/chat/completions"

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Request payload
payload = {
    "model": "gpt-4o-mini",  # You can change this to other models
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is machine learning?"}
    ],
    "temperature": 0.7,
    "max_tokens": 150
}

# Make the request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check if the request was successful
if response.status_code == 200:
    # Parse the response
    response_data = response.json()
    print("Response received successfully!")
    print("\nModel used:", response_data["model"])
    print("\nResponse content:")
    print(response_data["choices"][0]["message"]["content"])

    # Print the complete response structure
    print("\nComplete response structure:")
    print(json.dumps(response_data, indent=2))
else:
    print(f"Request failed with status code: {response.status_code}")
    print("Error details:")
    try:
        error_data = response.json()
        print(json.dumps(error_data, indent=2))
    except:
        print(response.text)
    
    # Provide helpful error messages
    if response.status_code == 401:
        print("\nThis is an authentication error. Please check:")
        print("1. Your API key is correct and valid")
        print("2. Your OpenAI account has credits or billing set up")
        print("3. You're using the correct API key for your account")
    elif response.status_code == 429:
        print("\nRate limit exceeded. Please wait a moment and try again.")
    elif response.status_code == 400:
        print("\nBad request. Please check your request parameters.")
