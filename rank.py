from os import listdir
import parse

def update_count(d,l):
    for item in l:
        d[item] = d.get(item, 0) + 1

def sort_dict(d):
    s = [(k, d[k]) for k in sorted(d, key = d.get, reverse = True)]
    return s

top_dict = {}
general_dict = {}
for page in listdir('./pages'):
    top, general = parse.parse_page(page)
    update_count(top_dict, top)
    update_count(general_dict, general)

top_sorted = sort_dict(top_dict)
general_sorted = sort_dict(general_dict)

with open('top.txt', 'w') as top_output:
    top_output.write(str(top_sorted))
with open('general.txt', 'w') as general_output:
    general_output.write(str(general_sorted))

print(top_sorted[:10])
print(general_sorted[:10])


if __name__=='__main__':
    pass