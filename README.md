# __Welcome to Stellar!__  

# <a name="table-of-contents"></a>__Table of Contents__  
  * [Author](#Author)  
  * [Introduction](#Introduction)  
  * [Installation](#Installation)  
  * [Running](#Running)  
  * [UserGuide](#UserGuide)  
  * [Sources](#Sources)  

# <a name="Author"></a>__Author__  

__Shane Yost__  
[scy86dev@gmail.com](scy86dev@gmail.com)  
[shaneyost.io](https://www.shaneyost.io)  

# <a name="Introduction"></a>__Introduction__  

As an active software engineer, hobbyist and student I struggle with 
maintaining what I learn over time especially as these newly acquired skills 
pick up in complexity. Reiterating over subjects and keeping a journal are two 
potentional methods I implement to overcome this whether I'm in class taking 
notes, at work solving complex problems, or just at home learning a new 
programming language.  

Taking notes in classes usually starts off with precision, well indented lines, 
bullet points, graphs, organization, timestamps and much more. However, after 
two or three weeks we generally lose this stamina and discipline. Eventually our 
notes become rambled lines of choatic chicken scratch. Sometimes we even stop 
taking notes entirely or less frequently than we should. In addition to this 
keeping a hand written journal takes work and becomes horribly inefficient to 
recall specific entries.  

Stellar aims to help in these challenges. We can digitial manage our entries in 
a database, use an object oriented model of querying these entries, and create 
entries with either highly formatted markdown syntax or plain text format. In 
addition, Stellar can track goals and tasks letting you know what is complete, 
incomplete, and days left to complete them.  

This tool has grown in complexity over the years. I've tried to keep a unix like 
philosophy which is to do one thing well versus too much.  Stellar is portable 
across Windows, MacOSX and Linux allowing anyone to scale the project to their 
needs. Stellar is a unlicensed application. Anyone is free to copy, modify, 
publish, use, sell, or distribute this software, either in source code form or 
as a compiled binary, for any purpose, comercial or non-commercial, and by any 
means.  

What are some key features of Stellar? See below for some gif's and descriptions 
of what it can do.  

  * Stellar uses the editor plugin called __MarkdownX__ to create notes, goals 
    and tasks. When using markdown syntax the editor will display the rendered 
    syntax in realtime to help you correct and format your entires only once 
    versus going back and forth in getting your syntax right.  

    ![](./gifs/markdownx.gif)  

  * Stellar uses [jsCalendar](https://gramthanos.github.io/jsCalendar/index.html) 
    to allow you to easily browse recent entries for the month or even several 
    years back. It highlights days that you took entries so you don't waste time 
    searching days that have none.  

    ![](./gifs/jscalendar.gif)  

  * Stellar uses [django_filters](https://django-filter.readthedocs.io/en/master/) 
    to allow custom search methods. We can search via every attribute that a 
    entry is made up of (e.g. title, date, content, tags, etc...).  

    ![](./gifs/search.gif)  

  * Stellar allows tagging in a unique way that at first may seem at a 
    disadvantage. Only one tag can be given to each entry. If we assigned 5 tags 
    to every entry for a 1000 entries we would have quite the selection of tags 
    to search through. It would seem this would improve our queries 
    categorically but in fact it adds entropy making it harder to search a very 
    specific entry. Stellar allows one additional attribute called a __Genre__ 
    to add one extra level of classification. In combination of the __Genre__ 
    and a generic tag called __Tag__ provides a more empirical method forcing 
    you to think about how an entry should be classified.  

    ![](./gifs/tags.gif)  

# <a name="Installation"></a>__Installation__  

### __Prerequisites__  

  * Python 3+  
    [Downloading](https://wiki.python.org/moin/BeginnersGuide/Download)  
    [Installing](https://realpython.com/installing-python/)  

  * Pip  
    Usually comes upon installing Python 3+. In not you can refer to the 
    following link [here](https://pip.pypa.io/en/stable/) for specifics.  

  * Shell  
    Starting the application requires starting a server. This application runs 
    locally so the built in django development server will do fine and thus no 
    configuring of another server is required. To run the server you must have 
    a shell such as a bash shell in Linux/MacOSX or powershell in Windows. For 
    configuration of each regarding python refer to the following links.  
    [Python on Windows](https://docs.python.org/3.3/using/windows.html)  
    [Python on Linux/MacOSX](https://docs.python.org/3.3/using/unix.html)  

### __Installation__  

##### **CLICK GIF FOR ENLARGED VIEW**  

![](./gifs/installation.gif)  

  1. Clone the repository either via `git clone` or downloading the repository as 
     a compressed archive.  
     `git clone https://gitlab.com/shanedora/stellar.git`  

  2. Navigate into the top level directory `cd stellar/` and create a virtual 
     environment and activate it.  
     `virtualenv venv`  
     `source ./venv/bin/activate`

  3. Install all the requirements for Stellar listed in the `requirements.txt` 
     file or all at once via the following command.  
     `pip install -r /path/to/requirements.txt`  

  4. Edit the `pjx_stellar/settings.py` on the line that says the following...  

     `TIME_ZONE = 'America/Denver'`

     to a timezone of your choosing. Viable timezones can be acquired from this 
     [link](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). Refer 
     to the __TZ database name__ column for your prefered option.   

  4. The following commands only need to be run once.  
     `python manage.py makemigrations`  
     `python manage.py migrate`  
     `python manage.py createsuperuser`  
     `python manage.py collectstatic`  

# <a name="Running"></a>__Running__  

Running Stellar can be configured in several ways but it all boils down to one 
command.  

`python manage.py runserver`  

This command will start the django development server and will make Stellar 
visiable at the URL __localhost:8000__ in your browser.  

Additional configuration can be done such as creating an alias in your `.bashrc` 
to start the server such as `alias stellar='python manage.py runserver`.  

---

# <a name="UserGuide"></a>__UserGuide__  

__Adim__  

The admin page is where you can create entries for notes, tasks and goals but 
also edit past entries which is really the only need here for Admin. It's 
important to note that the only way you can mark a task or goal as complete or 
incomplete is via the Admin interface. Other than this you will not need to 
login to the Admin interface. If you do use the username and password you 
created above when executing `python manage.py createsuperuser`.  

__Home__  

You can get to home via clicking on the navbar link or the __S__ logo in the 
navbar. Home displays tags, tasks, goals, and notes based on what day you've 
selected in the calendar. The calendar shows you days you've taken notes and 
allows easy navigation to past entries.  

Goals and tasks are only showed if they are incomplete. Remember you must go 
into the Admin interface to mark a goal/task as complete or incomplete. Days 
remaining to complete the goals/tasks are indicated to the left.  

Tags are also shown on the left panel. These tags are listed left to right as 
most popular to least popular. A number is printed along side each tag 
indicating the exact number of entries related to it. These tags are clickable 
down to one level deep. This means that by clicking a tag it will redirect you 
to another page that displays every note ever taken related to that tag. From 
this page there are no further features that allow additional queries. If 
further querying of entries are needed visit the search page.  

__Notes__  

Notes can be created by clicking on the "Notes" link in the navbar. Simply enter 
information into all the fields. All fields are required! The slug field is an 
exception. You do not need to enter a slug as this is handled automatically.  

__Search__  

The search page presents a form. This form will allow querying of your entries 
via every attribute related to a single entry. This form will not allow you to 
search tasks and goals. For that you need to visit the Admin interface. If you 
would like to export a list of entries from a search to PDF simply do the search 
and then in your browser click print-save_as-pdf.  

__Goals__  

Goals can be created via the same method as you create notes. When entering the 
date be sure to following a `mm/dd/yyyy` format while makeing sure you zero pad 
the `mm/dd/` appropriately. So if it's March 03, 2019 you would enter `03/03/2019`. 
Remember this is the date that the goal is estimated to be completed by. Remember 
that once you complete a Goal you will have to visit the Admin interface by 
clicking on the "Admin" link in the navbar and visiting that specific entry. From 
there you can mark it as complete.  

__Tasks__  

Tasks can be created via the same method as Goals and Notes.  

# <a name="Sources"></a>Sources  

You're go-to-guide for learning more about Django.  
[Django Docs](https://docs.djangoproject.com/en/2.1/)  
