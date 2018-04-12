# Thesaurus-cli

Ever had to search for that ~~perfect~~ ~~splendid~~ cromulent word? Faster and easier than a browser,
this CLI is unquestionably, unconditionally, the superlative solution.

## Getting Started



### Prerequisites

Python 3 and BeautifulSoup must be installed. They can be installed as follows:

```
apt-get install python3
pip install beautifulsoup4
```

### Installing

Distribution through pip will be added shortly. For now, since the entire script is self-contained
and quite small, just download the thesaurus-cli repo and copy the script to a directory on your PATH.
I have my installation in my ~/bin/ directory.

```
git clone https://github.com/davidgu/thesaurus-cli.git
cd thesaurus-cli
mv thesaurus ~/bin/
```

### Using
Thesaurus-cli takes a single argument, the word that is being searched. For example, to find synonyms
for "well"

```
./thesaurus-cli well
```

You will be able to select a specific definition for the searched word

```
Definitions for well are the following:
    0) healthy
    1) lucky, fortunate
    2) happily, pleasantly; capably
    3) sufficiently
    4) water hole
Select a definition: 
```

After choosing one, you will receive a list of synonyms

```
Synonyms for healthy:
strong
together
...
```
