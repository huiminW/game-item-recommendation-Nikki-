# game-item-recommendation-Nikki-
Another toy project

Nikki up2u3 is a Chinese dressing game. In this game, clothings have tags and attributes and scores (s,a,b,c and such) on each attributes. The scoring for each level depends mostly on a few per-determained attributes.

There are 7k+ different pieces of clothings in this game. This tiny project runs through 369 html pages (recommended clothing for each level)  and searches for the most frequently used clothing.(Also finding the most efficient clothing to buy with in game currency.)


source html files can be found in https://github.com/aojiaogongluezu/nikkiup2u3/tree/gh-pages/html
I manually deleted some unrelated or differently formated pages.

In this project, I used a tiny bit of beautifulsoup and re.
The two output files top.txt and general.txt have name of clothings and number of times they appear in html pages.(only the ones that were used)

ToDos:
Try to use http://seal100x.github.io/nikkiup2u3/ (more updated)instead. Figure out how to interact and scrape with webpage like this.
Try understanding the actual grading method of the game and compute scores.
Sort items in the output files by how it can be obtained for easier use.(different in game currency, evolving, dyeing and such)

BUG： general.txt file was calculated wrong(appearance count should not include score)
