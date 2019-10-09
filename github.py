#!/usr/bin/python
from bs4 import BeautifulSoup
import json
import requests

class GithubException(Exception): pass


def search_on_github(query=''):
    url = 'https://github.com/search?q=%s' % query
    resp = requests.get(url)
    if not resp:
        raise GithubException("Could not search the query %s" % query)
    return resp.content

def main():
    content = search_on_github('python')
    soup = BeautifulSoup(content, features='html.parser')
    repo_list = soup.find('ul', {'class': 'repo-list'})
    repo_list_item = repo_list.find_all('li', {'class': 'repo-list-item'})
    for item in repo_list_item:
        div_url = item.find('a', {'class': 'v-align-middle'})
        data_hydro_click = div_url.get('data-hydro-click', {})
        try:
            data_hydro_click = json.loads(data_hydro_click)
        except Exception:
            raise GithubException('Could not parse the URL')
        payload = data_hydro_click.get('payload', {})
        result = payload.get('result', {})
        url = result.get('url', '')
        print(url)

if __name__ == '__main__':
    main()