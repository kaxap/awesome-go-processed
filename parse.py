import requests
from requests import Response
import re

RE_LINK = re.compile(r'\* \[.*?\]\(https://github\.com/(.*?)\) - .*')
KEY_STARS = 'watchers_count'
KEY_FORKS = 'forks_count'
KEY_ISSUES = 'open_issues'


def get_readme(raw_url: str) -> str:
    response: Response = requests.get(raw_url)
    try:
        return response.text
    finally:
        response.close()


def get_github_stats(repo: str) -> dict:
    response: Response = requests.get(f'https://api.github.com/repos/{repo}')
    try:
        return response.json()
    finally:
        response.close()


def get_repo(line: str) -> str:
    matches = RE_LINK.findall(line)
    try:
        return matches[0]
    except IndexError:
        return ''


def add_stats(readme: str) -> str:
    result = []
    lines = readme.split('\n')
    i = 0
    total = len(lines)
    for line in lines:
        repo: str = get_repo(line)
        if repo:
            stats = get_github_stats(repo)
            line += \
                f' -> _stars: *{stats.get(KEY_STARS)}*, forks: {stats.get(KEY_FORKS)}, open issues:{stats.get(KEY_ISSUES)}_'
        result.append(line)
        i += 1
        print(f'{i}/{total} complete')

    return "\n".join(result)


def process(url: str) -> None:
    print('processing...')
    readme: str = get_readme(url)
    augmented_readme = add_stats(readme)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(f'this is a processed copy of {url}\n\n')
        f.write(augmented_readme)

if __name__ == '__main__':
    process('https://raw.githubusercontent.com/avelino/awesome-go/master/README.md')