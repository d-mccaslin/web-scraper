import requests

from bs4 import BeautifulSoup

url_hardcode = 'https://www.nature.com/articles/d41586-023-00103-3'


def get_valid_response():
    """Attempts to retrieve a response from nature.com/articles specifically"""
    url = input("Please enter a URL (an article from nature.com): ")

    if 'nature.com/articles' in url:
        try:
            r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        except requests.exceptions:
            print("Invalid API resource!")
        else:
            if r.status_code == 200:
                return r
            else:
                print(f'Invalid API response status: {r.status_code}')
    else:
        print("Invalid page!")


def get_relevant_content(r):
    """Returns a content dictionary for the given response"""
    soup = BeautifulSoup(r.content, 'html.parser')

    title = soup.find('title').text
    description = soup.find('meta', {'name': 'description'}).get('content')

    content_dict = {"title": title, "description": description}

    return content_dict


if __name__ == '__main__':
    response = get_valid_response()
    if response:
        print(get_relevant_content(response))
