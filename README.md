# Thesaurus-cli

Ever had to search for that ~~perfect~~ ~~splendid~~ cromulent word? Faster and easier than a browser,
this CLI is unquestionably, unconditionally, the superlative solution.

## Getting Started



### Prerequisites

Python 3 and pip must be installed. They can be installed as follows:

```
apt-get install python3
apt-get install pip3
```

Other dependencies such as BeautifulSoup will be installed by pip.

### Installing

Thesaurus-cli can be installed through pip:

```
pip install thesaurus-cli
```

### Using
Thesaurus-cli takes a single argument, the word that is being searched. For example, to find synonyms
for "well"

```
thesaurus well
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
