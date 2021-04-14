import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
import ssl
import re
import xml.etree.ElementTree as ET
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_moode = ssl.CERT_NONE

def func1():
    html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_819685.html", context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    spans = soup('span')
    numbers = []
    n = re.findall("[0-9]+", str(spans))
    for i in range(len(n)):
        numbers.append(int(n[i]))  
    
    print(spans)
    print("The first sum is: ", sum(numbers))

    print("The second sum is: ", sum( [ int(x) for x in re.findall("[0-9]+", BeautifulSoup(urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_819685.html", context = ctx).read()), 'html.parser')]))
    rint("Second sum:", sum( [ int(x) for x in re.findall("[0-9]+", open("regex.txt").read() ) ] ) )
    return 0

def func2():
    link = "http://py4e-data.dr-chuck.net/known_by_Sol.html"
    for i in range(7):
        html = urllib.request.urlopen(link, context = ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        anchor = soup('a')
        anc = anchor[17]
        linkr = str(re.findall("href=\"(\S+)\"", str(anc)))
        link = linkr[2:-2]
        print(link)
    return 0


def func3():
    xml = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_819687.xml", context = ctx).read()
    counts = re.findall("<count>([0-9]+)</count>", str(xml))
    numbers = []
    for i in range(len(counts)):
        numbers.append(int(counts[i]))

    print("The total is: ", sum(numbers))
    return 0

def func4():
    j = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_819688.json", context = ctx).read()
    jay = json.loads(j)
    comments = jay["comments"]
    numbers = []
    for i in range(len(comments)):
        numbers.append(comments[i]["count"])
    print("The total is: ", sum(numbers))
    return 0
