import requests
import re
import json
import glob
from bs4 import BeautifulSoup


def write_file(page, result):
    file = open(page, "w")
    file.write(result)
    file.close()


def get_request(url):
    result = requests.get(url, allow_redirects=False)
    return result.text


# TODO write function to parsee out SALV and SALVIATI

# SALV or SALVIATI is Galileo, feed that into GPT3 upload initially 

page1 = "http://law2.umkc.edu/faculty/projects/ftrials/galileo/dialogue.html"
page2 = "http://law2.umkc.edu/faculty/projects/ftrials/galileo/dialogue2.html"
page3 = "http://law2.umkc.edu/faculty/projects/ftrials/galileo/dialogue3.html"
page4 = "http://law2.umkc.edu/faculty/projects/ftrials/galileo/dialogue4.html"

pages = [page1, page2, page3, page4]

def sorter(item):
    return item[4]

def parse_page():

    download = False

    if download == True:
        for pg in pages:
            result = get_request(pg)
    else:
        files = sorted(glob.glob('*.html'), key=sorter)

        for fi in files:
            with open(fi) as f:
                content = f.read()
                soup = BeautifulSoup(content,'html.parser')
                # salv = soup.find_all('b', string=re.compile("^READER|SALV|SIMP|SAGR"))
                salv = soup.find_all('b',string=re.compile("SALV|SALVIATI"))
                for s in salv:
                    print(s.next_sibling)


def text_to_jsonl():
    # Generate a list of dictionaries
    lines = []
    with open("text.txt", encoding="utf8") as f:
        for line in f.read().splitlines():
            if line:
                lines.append({"text": line})

    # Convert to a list of JSON strings
    json_lines = [json.dumps(l) for l in lines]

    # Join lines and save to .jsonl file
    json_data = '\n'.join(json_lines)
    with open('my_file.jsonl', 'w') as f:
        f.write(json_data)            

def main():
    print("parse book to json lines")
    parse_page()


if __name__ == "__main__":
    main()



'''
i = 1
for pg in pages:
    result = get_request(pg)
    write_file("page" + str(i) + ".html", result)
    i = i + 1
'''

'''
param = "page1.html"

file1 = open(param, "w") 

file1.write(result1.text)

file1.close()
'''
