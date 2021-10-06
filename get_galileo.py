import requests


def write_file(page, result):
    file = open(page, "w")
    file.write(result)
    file.close()


def get_request(url):
    result = requests.get(url)
    return result.text


# TODO write function to parsee out SALV and SALVIATI

# SALV or SALVIATI is Galileo, feed that into GPT3 upload initially 

page1 = "http://law2.umkc.edu/faculty/projects/ftrials/galileo/dialogue.html"
page2 = "http://law2.umkc.edu/faculty/projects/ftrials/galileo/dialogue2.html"
page3 = "http://law2.umkc.edu/faculty/projects/ftrials/galileo/dialogue3.html"
page4 = "http://law2.umkc.edu/faculty/projects/ftrials/galileo/dialogue4.html"

pages = [page1, page2, page3, page4]

i = 1
for pg in pages:
    result = get_request(pg)
    write_file("page" + str(i) + ".html", result)
    i = i + 1



'''
param = "page1.html"

file1 = open(param, "w") 

file1.write(result1.text)

file1.close()
'''
