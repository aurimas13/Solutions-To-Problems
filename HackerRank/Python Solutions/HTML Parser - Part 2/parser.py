from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):  # define a HTML parser for comments

    def handle_comment(self, data):
        if len(data.split('\n')) != 1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print("Comment  :", data)

    def handle_data(self, data):
        if data.strip():
            print('>>> Data')
            print("Data     :", data)


html = ""
for i in range(int(input())):  # integer input and a loop
    html += input().rstrip()  # HTML input
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
