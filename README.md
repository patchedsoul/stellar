# Stellar

### <a name="table-of-contents"></a>Table of Contents  
  * [Author](#Author)  
  * [Introduction](#Introduction)  
  * [Installation](#Installation)  

---

### <a name="Author"></a>Author  

__Shane Yost__  
[scy86dev@gmail.com](scy86dev@gmail.com)  
[shaneyost.io](https://www.shaneyost.io)  

---

### <a name="Introduction"></a>__Introduction__  

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

  * Stellar uses [jsCalendar](https://gramthanos.github.io/jsCalendar/index.html) 
    to allow you to easily browse recent entries for the month or even several 
    years back. It highlights days that you took entries so you don't waste time 
    searching days that have none.  

  * Stellar uses [django_filters](https://django-filter.readthedocs.io/en/master/) 
    to allow custom search methods. We can search via every attribute that a 
    entry is made up of (e.g. title, date, content, tags, etc...).  

  * Stellar allows tagging in a unique way that at first may seem at a 
    disadvantage. Only one tag can be given to each entry. If we assigned 5 tags 
    to every entry for a 1000 entries we would have quite the selection of tags 
    to search through. It would seem this would improve our queries 
    categorically but in fact it adds entropy making it harder to search a very 
    specific entry. Stellar allows one additional attribute called a __Genre__ 
    to add one extra level of classification. In combinatino of the __Genre__ 
    generic tag field called __Tag__ provides a more empirical method forcing 
    you to think about how an entry should be classified.  

---

### <a name="Installation"></a>__Installation__  