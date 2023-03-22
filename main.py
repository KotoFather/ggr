import requests

# Function to get the response from Google
def get_google_results(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": "YOUR_API_KEY",
        "cx": "YOUR_CUSTOM_SEARCH_ENGINE_ID",
        "q": query,
        "num": 1  # Number of search results to return
    }
    response = requests.get(url, params=params)
    return response.json()

# Main function
def main():
    query = input("Enter a search query: ")
    result = get_google_results(query)
    print(result['items'][0]['snippet']) # Print a brief description of the top search result

# Run the program
if __name__ == '__main__':
    main()
