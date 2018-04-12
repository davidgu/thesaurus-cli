#!/usr/bin/env python3
import sys
import urllib.request
from bs4 import BeautifulSoup

def main():
    search_term=sys.argv[1]
    search_term = search_term.replace(' ', '%20')

    # Check for invalid word resulting in HTTPError
    try:
        fp = urllib.request.urlopen('http://www.thesaurus.com/browse/'+search_term)
    except urllib.error.HTTPError:
        print('The word '+search_term+' could not be found')
        exit()

    html_bytes = fp.read()
    html_doc = html_bytes.decode('utf-8')
    fp.close()

    soup = BeautifulSoup(html_doc, 'html.parser')
    synonyms = soup.find_all("div",{"class":"synonyms"})
    # Check again for an invalid word which may have returned a valid HTTP response
    if(len(synonyms)==0):
        print('The word '+search_term+' could not be found')
        exit()

    thesarus={}

    for synonym in synonyms:
        description = synonym.find("div",{"class":"synonym-description"}).find(
                "strong",{"class":"ttl"}).text
        thesarus[description]=[]
        for word in synonym.find("div",{"class":"relevancy-list"}).find_all(
                "span",{"class":"text"}):
            thesarus[description].append(word.text)

    print('Definitions for '+search_term+' are the following:')
    choices={}
    for idx,word in enumerate(thesarus.keys()):
        print('    '+str(idx)+') '+word)
        choices[idx]=word
    selection = input('Select a definition: ')
    print('Synonyms for '+choices[int(selection)]+':')
    for word in thesarus[choices[int(selection)]]:
        print(word)

if __name__ == '__main__':
    main()
