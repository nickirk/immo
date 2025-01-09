# Automatic Wohnung Search Bot 

**Pay attention to the robots.txt file on websites and the related rules therein before you use any spiders to scrape data from websites, please respect the rules and use this script at your own risk**

**Support and bug fixes for immoscout24 are needed. Currently the script only works properly for wg-gesucht.de**

Now you need to put your message to the landlord in a file named "message.txt" instead of in the script. 

## Introduction

Looking for a flat in big cities can be a pain in the eye (ass) due to many different reasons, e.g. you are a student and many landlords don't like students; or you don't speak German so well and landlords, most of who are in their old ages, cannot speak English so well; or there are just simply too many people looking for a nice flat, whenever a new offer apears online the landlord will receive tons of applications and they have nothing to do but to choose the first ones who sent them the applications. So making sure that your application always apear among the first emails in the landlords' inbox is crucial to get you a chance to visit the apartment. I learned the lesson in a hard way by spending a lot of my time online monitoring the updates of apartment offers on [immobilienscout](!https://www.immobilienscout24.de/), [wg-gesucht](!https://www.wg-gesucht.de/wohnungen-in-Stuttgart.124.2.0.0.html) or [ebay](!https://www.ebay-kleinanzeigen.de/stadt/stuttgart/) everyday, but in the end almost all of my inquiries went straight into the vacuum and never got an echo back. After somedays, I realised that maybe it is true that there are too many people online looking for a flat, and my messages are just among the tons of messages the landlords receive, so to increase my chance, I need to send messages as soon as the offer is put online. This Bot in Python can monitor the websites every minute, once it finds new offers it will send messages to the landlord automatically. Basically the whole process won't take more than 2 minutes since the offer is put online. 


For wg-gesucht, here are things to pay attention to:

0. the corresponding files are 
	- immo.py --> wg-gesucht.py
	- submit.py --> submit_wg.py
	- immo_spider.py --> wg-gesucht-spider.py
1. wg-gesucht.de asks for your username and password, which you need to write in the places in the submit_wg.py script.
2. speaking German increases your chance of getting a offer. Try to force yourself speaking German. :)
3. please don't abuse the script by sending requests too frequently to the website, otherwise they could take some anti-measures to rule out the bot, which is bad for everyone who wants to look for a flat using the bot.
4. The script can be run on raspberry pi 3b. Some more questions please see (closed) issues before you open a new issue. Thanks. 

Good luck to your wohnung hunt.


### Requirement

I have only tested the Bot on Linux (Debian, Ubuntu) and Mac. I am not sure about whether you can do some tricks and make it work on Windows, too. But worth trying.

1. chromedriver. I take chrome as an example since it is my favorite browser, but you can also use other popular browsers because you can find their *driver*s. You need to have chrome installed. 

   On Linux use the followling command to check if you have chromedriver installed

   `which chromedriver`

   if it is installed, then something like the following which tells you the path to the driver should appear

   `/usr/local/bin/chromedriver` 

   if nothing appears, then you need to install chromedriver, using the following command on Linux (Debian or Ubuntu),

   `sudo apt-get install chromedriver`

   and use the following command on Mac (if you use [homebrew](!https://brew.sh/)),

   `brew install chromedriver`

2. [Scrapy](!https://scrapy.org/), which is a package based on Python for writing web spiders. After/if you have python installed, then the following command should install *Scrapy* for you

   `pip install scrapy`

### Files

There are just 3 python scripts. 

`immo.py`

`immo_spider.py`

`submit.py`

Get the scripts by 

`git clone https://github.com/nickirk/immo.git`


### How it works
Go into the directory: 

`cd immo`

#### Modify the scripts according to your needs

1. In `submit.py` file, you will see

`last_name.send_keys("last name")`

`first_name.send_keys("first name")`

`street.send_keys("your current living street")`

and etc. Replace the text with your own information. Especially in 

`text_area.send_keys(u"Hallo,\n\n your message to the landlord. keep the 'u' before the message to make showing German in the message available. use \n as newline in your message.")`

write your message to the landlord. Please keep the 'u' in front of the message so that the special German letters will show in the message on the browser side. After this line, there are no more things needed to be modified. 

2. In `immo_spider.py` file, you need to replace the website links that fits your need. For example,

   ````python
   start_urls = [
	'https://www.example.de/Suche/S-2/Wohnung-Miete/Umkreissuche/etc'
   	]
   ````
You can go to a website of your choice and enter your filter, e.g. price until 850 Euros. Click search, you will arrive at the page showing you the results. However, you need to choose the realtime (Aktualität) sorting so that the results you see are always the latest offers. Then copy the link address and paste it into the start_urls. You can put more than one links to it separated by comma.

#### Create a Scrapy Spider project

First, we need to [create a new scrapy project](!https://docs.scrapy.org/en/latest/intro/tutorial.html#creating-a-project) 
called immobot:

`scrapy startproject immobot`

then you will have the following structure of directories and files:

     immobot/                  #Working directory
         scrapy.cfg            # deploy configuration file
         immobot/             # project's Python module, you'll import your code from here
             __init__.py
             items.py          # project items definition file
             pipelines.py      # project pipelines file
             settings.py       # project settings file
             spiders/          # a directory where you'll later put your spiders
                 __init__.py

Now let's go to the working directory called `immobot` which contains the file `scrapy.cfg` and another direcory which is also called `immobot`:

`cd immobot`

Now copy the 3 files into the following directories:

`cp ../immo.py ../submit.py .`

`cp ../immo_spider.py ./immobot/spiders/`

after this you will have the following structure of directories and files 

     immobot/                  #Working directory
         immo.py
         submit.py
         scrapy.cfg            # deploy configuration file
         immobot/             # project's Python module, you'll import your code from here
             __init__.py
             items.py          # project items definition file
             pipelines.py      # project pipelines file
             settings.py       # project settings file
             spiders/          # a directory where you'll later put your spiders
                 __init__.py
                 immo_spider.py


In the end, just run 

`python immo.py`

under you working directory *immobot*, the Bot will be running and doing everything for you.

Further simpilfications of the scripts will be done to make it a blackbox tool.

## Tips and troubleshooting
You may run into issues, hopefully these tips can help:

**chromedriver may be installed somewhere else** then asumed by the script. You can check this by running `which chromedriver`, it's result should be: `/usr/local/bin/chromedriver`. If it's not, then change this value in [submit.py]() in the line with `webdriver.Chrome('<pass in your value here>')`.

**you've made changes, but nothing changed**. Remember to copy the `.py` files into the `immobot` folder.

**testing** can be easily done by removing one of the id's from the `diff.dat` file. During the next check, the script will just consider this specific advertisement as a new one.
