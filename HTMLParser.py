from bs4 import BeautifulSoup
from nltk.tokenize import regexp_tokenize
import os

def HTML_parser(file_dir):
    content = {}
    pattern = r'[a-zA-Z]{2,}'
    for root, dirs, files in os.walk(file_dir):
        for index in files:
            if not index.endswith('html'):    # remove .DS_store
                continue
            thepath = os.path.join(root, index)
            htmlcontent = BeautifulSoup(open(thepath), 'lxml')
            content[index] = regexp_tokenize(htmlcontent.get_text(), pattern)
    return content

# allcontent = HTML_parser('./HtmlSource')
# print(allcontent)

