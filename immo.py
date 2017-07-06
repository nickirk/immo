from subprocess import call
import submit
import json
from pprint import pprint
import os.path
import time
from datetime import datetime
fname="href.json"
while True:
    if os.path.isfile(fname):
        call(["mv", fname, "href_old.json"])
        call(["scrapy", "crawl", "immoscout", "-o", "href.json", "-s", "LOG_ENABLED=false"])
        with open('href.json') as data_file:    
                data = json.load(data_file)
        data=list(set([i[u'href'] for i in data]))
        with open('href_old.json') as data_old_file:    
                data_old = json.load(data_old_file)
        data_old=list(set([i[u'href'] for i in data_old]))
    else:
        call(["scrapy", "crawl", "immoscout", "-o", "href.json", "-s", "LOG_ENABLED=false"])
        with open('href.json') as data_file:    
                data = json.load(data_file)
        data=list(set([i[u'href'] for i in data]))
        print data
        ini=raw_input("No href.json file found. Sending messages to all offers found above?(y/n)\n")
        if ini.lower() == "y":
            data_old = []
        elif ini.lower() == "n":
            call(["cp", fname, "href_old.json"])
            with open('href_old.json') as data_old_file:    
                    data_old = json.load(data_old_file)
            data_old=list(set([i[u'href'] for i in data_old]))
    #with open('href.json', 'w') as data_file:    
    #    json.dump(data,data_file)
    #print data
    #black list
    if os.path.isfile('blacklist.json'):
        with open('blacklist.json') as blacklist:
            blacklist = json.load(blacklist)
        blacklist = list(set([i[u'href'] for i in blacklist]))
    else:
        blacklist = []
    print "Blacklist: ", blacklist

    #with open('href_old.json', 'w') as data_old_file:    
    #    json.dump(data_old,data_old_file)
    #print data_old
    diff_id=list(set(data)-set(data_old)-set(blacklist))
    #print diff_id
    text_file = open("sent_request.dat", "a")
    text_file1 = open("diff.dat", "a")
    if len(diff_id) != 0:
        print len(diff_id), "new offers found"
        print "New offers id:", diff_id
        print "Time: ", datetime.now()
        for new in diff_id:
            print "Sending message to: ", new
            submit.submit_app(new)
            text_file.write("ID: %s \n" % new)
            text_file.write(str(datetime.now())+'\n')
            text_file1.write(str(new)+'\n')
        text_file.close()
        text_file1.close()
    else:
        print "No new offers."
        print "Time: ", datetime.now()
    time.sleep(60)
