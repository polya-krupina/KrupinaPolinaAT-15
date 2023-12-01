import requests
import re


def get_subheadings(url):
    content = requests.get(url).text
    pattern = re.compile(r'<h3.*?>(.*?)<\/h3>')
    subheadings = pattern.findall(content)
    return subheadings


subheadings = get_subheadings("http://www.columbia.edu/~fdc/sample.html")
print(subheadings)
