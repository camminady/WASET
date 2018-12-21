# Credit:
The whole idea was motivated by the DEF CON 26 talk:
DEF CON 26 - Svea, Suggy, Till - Inside the Fake Science Factory

They mention that it is not possible to upload the data set but to upload scripts that generate the data set. So here we go. I do restrict the data sets to WASET.


# General notes:

## waset_categories.txt
contains the names of all the categories under which you can publish in WASET


## The abstracts 

download Metadata for all abstracts as XML with (assuming you have created a folder abstracts/ in the current directory)
`python2 dl_abstract.py 1 120000`

### Note 1: 
This is really slow! You can however, start the script in 10 different terminals and each with a different range, i.e.: 

`python2 dl_abstract.py 1 1000`
`python2 dl_abstract.py 1000 2000`
`...`

There is definitely a faster way to do this but I am limited by my python skills.

### Note 2: 
The first abstracts start with an ID above 1219.



## The papers
dl_paper.py works just like dl_abstract. it needs a folder publications/

This actually also downloads the "page not found" content as pdf. these are files of size almost zero and can be deleted afterwards with
`python dl_paper_remove_empty.py`
