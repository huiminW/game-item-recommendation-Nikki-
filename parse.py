from bs4 import BeautifulSoup
import re


def parse_page(pagename):
    # open file, cook soup
    with open('pages/'+pagename,'r') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')

    #get top and general items from soup
    top_raw = [i.get_text() for i in soup.find_all('span', {'class':'top'})]
    general_raw = [i.get_text() for i in soup.findAll('span', {'class':'genera1'})]

    #format top and general
    top = []
    for line in top_raw:
        sublist = re.split('= ',line)
        for item in sublist:
            if item!='' and item!='顶配 > ':
                top.append(item)

    general = []
    for line in general_raw:
        sublist = re.split('> |>|= ',line)
        for item in sublist:
            if item!='':
                general.append(item)



    return (top,general)

if __name__ == '__main__':
    pagename = 'g1-1.html'
    top,general = parse_page(pagename)
    # with open('result.txt', 'w') as output:
    #     output.write(result)
    print(top)
    print(general)