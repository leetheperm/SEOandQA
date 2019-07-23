# SEO and QA Multi Link tester

This script uses Python and Selenium Webdriver to output the SEO data, alt tags for all images, page title, and the status codes of every link on the page and can take an unlimited amount of links.

## Getting started

The following scripts require Python and selenium webdriver. Python is a scripting language used for many purposes from data science, object oriented programming, machine learning and many more.Selenium Webdriver is a third-party python module, which allows your script to access the internet and perform tasks automatically. Webdriver has a number of different versions, such as remote driver(for virtual machines), selenium grid (to do tests on multiple machines simultaneously), but we only need Chromedriver and Geckodriver for this script.

## Dependencies
To run this script, first you will need to download Python 3.7 or later from https://www.python.org/download/releases/3.0/

* Chromedriver is the webdriver for Google Chrome 
(http://chromedriver.chromium.org/downloads)

* GeckoDriver is the driver for all other browsers
(https://github.com/mozilla/geckodriver/releases)

You will need one or both of these for the scripts, depending on which tests or which browsers you want to use to test

Then you will need other Py dependencies, which I have listed here:
```
pip3 install selenium
pip3 install requests
```

To install these, you can open your terminal or command prompt and copy and paste them as they are.
*Notice the 3 next to pip. That means these dependencies will only work on python 3.

You will also need to download the scripts from this repository. This can be done by downloading the zip file. (Git coming soon)

You can also download the dependencies quickly by running the dependencies bash file
```
~./dependencies.sh
```
if you do not have permission, change your permissions by running this code in terminal
```
chmod dependencies 7705
```

## Installing and running

The best way to run this script is using an IDE (basically a notepad that can do way more and you can add extensions and predictive text for coding languages) and in my opinion the best and easiest to use is Sublime Text. (https://www.sublimetext.com/)

Once you have installed sublime text, you should set up your environment to enable Python 3 syntax and build capabilities. To do this, *open Sublime* then click *tools > build system > build new system*. It will opn a new window and you can simply copy and paste this text into that window:
```
{
"cmd": ["/usr/local/bin/python3", "-u", "$file"],
"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
"selector": "source.python",
"encoding": "utf8",
"path": "/usr/local/Frameworks/Python.framework/Versions/3.3/bin/"
}
```
Now, you should be good to go.

When launching the script for the first time, make sure that the location of the driver or 'self.browser' in this case is the same as where you left your Chromedriver or Geckodriver. I leave mine as the downloads folder because that's where it will appear when I download something.

```
self.browser = webdriver.Chrome('/Users/yourName/Downloads/Chromedriver')
```
Launching from the terminal means you have to change your current directory to the location of the script. For eg. if your script is in the Downloads folder. Try:
```
cd Downloads
```

the script can be launched from the terminal like using this simple python3 command (make sure you change the script.py to the name of the file you want to launch eg. python3 testAllLinks.py and if the file name has spaces use quotations like- python3 "test all links.py")

```
python3 script.py
```
or you can launch it using your IDE or text editor if it has python functionality.

### Headless or browser mode

Headless browser is a feature of selenium that allows a script to be run in the background of your machine instead of being able to see the script run, so it doesn't disrupt what you're doing. This is ideal if you are certain the script runs as intended and you are trying to do something that does not require your attention on the front such as grabbing data from a website or checking for certain attributes in the code. 

To turn headless on just make sure it is not commented out (has a hashtag in-front) and to turn on headed, just add a hashtag in-front of the headless option. This applies to all options. In the example below, headless has been turned off so we can watch the script run.

```
#options.add_argument('--headless')
```

and almost like magic, we can turn headless mode back on.

```
options.add_argument('--headless')
```
### Changing target url

You can change the target url by pasting your desired url within the quotations.

```
url = ("https://www.website.com")
```
### Errors
Issue:
Link cannot be qaweb-shop link
Fix:
remove shop and try qaweb.website.com


## Authors

* **Lee Davies** - *Initial work* - (https://github.com/LeethePerm)
