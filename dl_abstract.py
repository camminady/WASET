import urllib2,cookielib
import sys, getopt

def crawl(start,stop):
    for id in range(start,stop):
         site="https://waset.org/Publications/XML?abstract=" + str(id) + "&t=xml"
         hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Connection': 'keep-alive'}

         req = urllib2.Request(site, headers=hdr)

         try:
            page = urllib2.urlopen(req)

            content = page.read()
            filename = "abstracts/id"+str(id)+".xml"
            if id<10000:
                filename = "abstracts/id0"+str(id)+".xml"
            if id<1000:
                filename = "abstracts/id00"+str(id)+".xml"
            if id<100:
                filename = "abstracts/id000"+str(id)+".xml"
            if id<10:
                filename = "abstracts/id0000"+str(id)+".xml"

            with open(filename,"a+") as f:
                f.write(content)
         except urllib2.HTTPError, e:
            print("nothing at " + str(id))



if __name__ == "__main__":
    if len(sys.argv) <2:
        print("dl_abstract.py need exactly two command line inputs: start and stop for crawling")
    else:
        start = int(sys.argv[1])
        stop = int(sys.argv[2])
        crawl(start,stop)
