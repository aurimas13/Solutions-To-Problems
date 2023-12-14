from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):  # defining functions within a class
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print("->", attr, ">", value)


html = ''
for _ in range(int(input())):  # integer input
    html += input().rstrip() + '\n'  # string HTMl input

parser = MyHTMLParser()
parser.feed(html)
parser.close()
