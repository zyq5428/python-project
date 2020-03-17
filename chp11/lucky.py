import requests, sys, webbrowser, bs4

print('Baiduing...')
res = requests.get('https://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('."result c-container " a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://www.baidu.com' + linkElems[i].get('href'))