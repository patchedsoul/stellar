![](./gifs/stellar.gif)  

# __Welcome to Stellar!__  

#### <a name="table-of-contents"></a>__Table of Contents__  
  * [Author](#Author)  
  * [Introduction](#Introduction)  
  * [Installation](#Installation)  
  * [Running](#Running)  
  * [Stopping](#Stopping)  
  * [UserGuide](#UserGuide)  
  * [Sources](#Sources)  

#### <a name="Author"></a>__Author__  

__Shane Yost__  
[scy86dev@gmail.com](scy86dev@gmail.com)  

#### <a name="Introduction"></a>__Introduction__  

There are two types of students/engineers, those that maintain a stellar looking journal and those that do not. How effective a journal can be is directly proportional to how efficient it can be in maintaining it.  

Here are the requirements of stellar  

  * Stellar shall use an editor supporting plain text format and markup while rendering markup as you type.  

  * Stellar shall use the jsCalendar widget to provide querying by date through click-based selectors (e.g. day, month, year).  

  * Stellar shall use the package django-filters for custom searching of each models attribute and support additional filters if need be.  

  * Stellar shall provide the genre tag to divide notes into their respective categories (e.g. book, project, program, email, etc...) and classification tags for grouping items showing similarity.  

  * Stellar shall include a light weight server where the web app can be broadcasted off the localhost or a provided IP address. It is assumed the user understands the security and performance limitation of Django's light weight server. It is also assumed that when broadcasting off an IP address the user is doing so inside an intranet from behind a protected firewall with limited traffic between end points.  

  * Stellar shall run on Windows, Linux, MacOSX and at the minimum support the 
  four browsers IE, Chrome, Firefox, and Brave without any noticable issues regarding bootstrap formatting.  

  * Stellar shall support updates by simply executing `git pull`. It is assumed that by deleting the `.git` folder the user is opting out of receiving updates. It is also assumed that if the user wishes to version control their database files they must do so themselves.  

  * Stellar shall include instructions on install and will also strongle emphasize the importance of using _Virtualenv_.  

  * Stellar shall include the creation and managing of tasks and goals.  

  * Stellar shall include the SOAR methodology for tracking achievements and performance metrics to make annual reviews go smoother.  

  * Stellar shall include a link to the admin page in the navigation bar and enforce familiarization with it's interface.  

#### <a name="Installation"></a>__Installation__  

##### __Prerequisites__  

  * Python Version 3.6+  
    [Downloading](https://wiki.python.org/moin/BeginnersGuide/Download)  
    [Installing](https://realpython.com/installing-python/)  

  * Pip  
    Pip usually comes with the installation of Python but in the case it doesn't refer to the following link.  
    [Installing](https://pip.pypa.io/en/stable/)  

  * Shell  
    A shell is a command line based environment referred to as the terminal on linux and Powershell or CommandPrompt on Windows. You will need it and as such will need to validate that your path variable is setup accordingly so that python and pip can be executed from the shell environment.  
    [Windows Users](https://docs.python.org/3.3/using/windows.html)  
    [Linux/MacOSX Users](https://docs.python.org/3.3/using/unix.html)  

  * Git  
    Git is a version tracking tool and is recommended for downloadnig (aka cloning) the stellar repository down to your computer. The alternative is downloading the compressed archived.  
    [Download](https://git-scm.com)  

  * Virtualenv  
    First off, if you don't use virtualenv then you should be. It is incredibly easy and will isolate the stellar python environment from your systems environment. This will need to be installed prior to the next section should you choose to use virtualenv. It is not a requirement to use but please do so for the sake of your environment.  
    [Pip Install](https://pypi.org/project/virtualenv/)  

![](./gifs/installation.gif)  

##### __Installation__  

  * Clone the repository at this time or download the compressed archive.  
    `git clone https://gitlab.com/shanedora/stellar.git`  

  * Open your shell and navigate to the top level directory.  
    `cd stellar/`  

  * Create and activate virtual environment (recommended but not required)  
    `virtualenv venv`  
    `source ./venv/bin/activate`  
     NOTE: The second command above for activating your virtual environment may differ slightly in its syntax for Windows users. See the below section on __Running__ for what it might look like.  

  * Install all the required dependencies.  
    `pip install -r stellar/requirements.txt`  

  * If you timezone is not `America/Denver` then refer to [__this link__](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for your preferred timezone. Once you have it open the file __`stellar/top_stellar/pjx_stellar/settings.py`__ and edit the line __`TIME_ZONE = 'America/Denver'`__ according to your timezone.  

  * Create and apply database migrations while creating a admin account and collecting up all the static files into one place.  
    `python manage.py makemigrations`  
    `python manage.py migrate`  
    `python manage.py createsuperuser`  
    `python manage.py collectstatic`  

#### <a name="Running"></a>__Running__  

  1. Open a shell and navigate to `stellar/` to activate your vitural environment if you haven't already. Coming straight from the installation section above then this will already be done.  

     __Windows Powershell__  
     `cd .\stellar\venv\Scripts`  
     `.\activate.ps1`  

     __Windows Command Prompt__  
     `cd .\stellar\venv\Scripts`  
     `.\activate.bat`  

     __Linux__  
     `source ./stellar/venv/bin/activate`  

  2. Start the light weight django server.  

     __For broadcasting off localhost:8000...__  
     `python manage.py runserver`  

     __For broadcasting off IP:8000...__  
     `python manage.py runserver 1.2.3.4:8000`  

     NOTE:  
     When broadcasting off an IP other than localhost it is your responsibility to create an inbound rule on your firewall. Only broadcast on an IP like this when you are behind a firewall within an intranet and you need to share your notes with a colleague or two. The django development server is not meant for production but it can handly a light load of users. For instructions on creating a inbound rule see the following links.  
     [Linux Users](http://davidwilson.me/2013/08/18/Testing-Django-on-mobile-device-locally.html)  
     [Window Users](https://www.tomshardware.com/news/how-to-open-firewall-ports-in-windows-10,36451.html)  

  3. Open a browser and navigate to `localhost:8000` or `yourIP:8000`. Stellar will appear landing you on the homepage.  

#### <a name="Stopping"></a>__Stopping__  

Stopping stellar is quite easy but feel free to leave it running as long as you want. To stop execute `Ctrl+C` keystrokes from within your shell then deactivate your virtual environment by typing `deactivate` into the shell and pressing enter.  

#### <a name="UserGuide"></a>__UserGuide__  

__Admin__  

Login with the credentials you created above in the last step of the installation section. From here you can access your notes, SOAR, goals, and tasks. This is the only way to edit past entries that you've made.  

__Home__  

Home displays the jsCalendar widget. Click through the calendar for selecting different months/years. Click a day will display the notes off into the right hand column. Days with notes are highlighted in the calendar as a light gray color. Tags appear off the left. Clicking the tags will land you on another page showing all entries related to that tag. Ongoing (incomplete) Goals and Tasks are shown on the right column along with a badge to the left indicating the amount of days left to complete them.  

__Create--Notes__  

The dropdown link _Create_ and sublink _Notes_ will redirect you to the page for creating note entries. Only the fields Tag and Genre are optional as sometimes you may not want to create a genere and/or tag but it is recommended you do for the sake of recalling entries in the future. Dates must be entered in the format shown. Today's date will be used by default. The body section is a markdown editor. Enter text with markup and a rendered view will be shown off to the right. Click the button _Create_ to submit the entry to the database.  

__Create--SOAR__  

The dropdown link _Create_ and sublink _SOAR_ will redirect you to the page for creating SOAR entries. Only the fields Tag and Genre are optional as sometimes you may not want to create a genre and/or tag but it is recommended you do for the sake of recalling entries in the future. Dates must be entered in the format shown. Today's date will be used by default. Each body's field is a markdown field. Enter text with markup and a rendered view will be shown off to the right. Click the button _Create_ to submit the entry to the database. Pre-inserted text is already entered into each body's field explaining what each field is. SOAR is how we make our end of year reviews easier. It's for capturing achievements and peformance metrics of things you've done. SOAR entries can be filled out weekly, monthly or whenever you feel like it.  

__Create--Goals & Create--Tasks__  

The dropdown link _Create_ and sublink _Goals or Tasks_ will redirect you to the page for creating goal/task entries. All fields are required here. The date field is the date that you expect to compelete the goal/task. The body field is a markdown field. Enter text with markup and a rendered view will be shown off to the right. click the button _Create_ to submit the entry to the database. By default all incomplete goals/tasks will be displayed on the homepage. Therefore, when you have completed the goal/task you must log into the admin interface, select _Goals or Tasks_, and find the goal/task of interest. _Goals or Tasks_ incomplete have a red colored `x` in the table. Click this entry and edit the complete field by checking the box which will mark it as complete. Now it will be removed from the homepage. On the homepage you will see badges to the left of each goal/task indicating the amount of days left to complete it. When you get down to 0 days the badge will be red. When you get down to 1 day the badge will be yellow and for 2 or more days out the badge will be a navy blue.  

__Search__  

The dropdown link _Search_ will provide sublinks to various models to search which if not clear now are _Notes, SOAR, Goals and Tasks_. None of the fields are required so you can just pick one of them or two of them or even all them for carrying out relatively advanced searches of that respective model. Leaving all fields blank and clicking _Search_ will result in all notes being displayed. If you would like to export this page to a pdf simply do so by using your browsers print-to-pdf feature. Printing to pdf will not only capture what entries are displayed on the page but will show the data entered into the form so you can recreate the results in the future if need be.  

#### <a name="Sources"></a>__Sources__  

Building stellar has been an on going effort. Each year I add to stellar increasing it's scope and intended audience. If you have a suggestion feel free to email and I'll take it into consideration for the next release. A big thanks to the django reddit community for providing guidance when I needed it.  

Cheers ~  
Shane  
