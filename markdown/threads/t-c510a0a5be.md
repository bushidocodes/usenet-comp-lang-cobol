[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress Dialog vs. OO GUI

_10 messages · 9 participants · 1999-06_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### NetExpress Dialog vs. OO GUI

- **From:** "Young Kim" <y_s_k@worldnet.att.net>
- **Date:** 1999-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kdotv$k6p$1@bgtnsc01.worldnet.att.net>`

```
We are evaluating NetExpress and have noticed that Dialog is basically the
old Dialog which MF used to market and then withdrew a few years ago.

1) I am wondering if anyone out there is using the new Dialog.

2) What are some of the pros and cons using MF GUI/OO modules (awfully
cumbersome) vs. using Dialog.

3) We are wondering if we should jump ahead and use NetExpress web 100% for
GUI/OO  - pros and cons?

TIA
```

#### ↳ Re: NetExpress Dialog vs. OO GUI

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-wFcEddkkK0Mi@Dwight_Miller.iix.com>`
- **References:** `<7kdotv$k6p$1@bgtnsc01.worldnet.att.net>`

```
On Fri, 18 Jun 1999 15:32:01, "Young Kim" <y_s_k@worldnet.att.net> 
wrote:

> We are evaluating NetExpress and have noticed that Dialog is basically the
> old Dialog which MF used to market and then withdrew a few years ago.
…[7 more quoted lines elided]…
> GUI/OO  - pros and cons?

Search http://www.deja for my e-mail with the word "Dialog" in the 
message.

I've made some posts concerning different approaches to the GUI.  

A great number of users are doing NEITHER - instead opting to use Sp2 
from Flexus (http://www.flexus.com) instead for their GUI.  

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: NetExpress Dialog vs. OO GUI

- **From:** "Charles F. Townsend" <ctowns@ix.netcom.com>
- **Date:** 1999-06-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3770E2F0.6B0ACB21@ix.netcom.com>`
- **References:** `<7kdotv$k6p$1@bgtnsc01.worldnet.att.net> <Jl0PnHJ5PvPd-pn2-wFcEddkkK0Mi@Dwight_Miller.iix.com>`

```
There are other alternatives such as Synkronix PERCobol
http://www.synkronix.com/sync_prod.html that will allow you to use the COBOL
screen section (allowing users to take their green screen anywhere) or build a
platform independent GUI.  PERCobol supports building IMS Clients, CICS Clients,
using MQSeries, WebNFS (remote data access), servlets, applets, COBOL Beans (Java
Beans out of COBOL).

Synkronix also has BlueJ(tm) that will build platform independent GUIs in COBOL
or Java.

Charles Townsend
Synkronix, Inc.
http://www.synkronix.com
925 467-1598 ext.11




Thane Hubbell wrote:

> On Fri, 18 Jun 1999 15:32:01, "Young Kim" <y_s_k@worldnet.att.net>
> wrote:
…[28 more quoted lines elided]…
> http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: NetExpress Dialog vs. OO GUI

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376AC775.FD16D566@home.com>`
- **References:** `<7kdotv$k6p$1@bgtnsc01.worldnet.att.net>`

```
Young Kim wrote:
> 
> We are evaluating NetExpress and have noticed that Dialog is basically the
…[10 more quoted lines elided]…
> TIA

Having gone straight from DOS to Visoc(which didn't have Dialog System) 
I committed to OO/GUI. Now that I have NetExpress V 3 - it does have
Dialog System.

Purely a guesstimate - but probably 90% of N/E developers are using D/S.
Those I've spoken to swear by the new D/S. If you are already familiar
with D/S - then that would be a sensible route to pursue. Be aware
though, it does have some limitations, tables with multi-column entry
fields, and should you wish to do something like a Progress Bar - you'll
have to do it in OO/GUI. Look at the D/S demos to see if it gives an 80%
"fit" to what you are trying to achieve with GUIs.

Having committed to OO/GUI I've stuck with it; a L-A-R-G-E learning
curve to understand Windows inter-action, (if you haven't been the
Windows route before), but the actual Object Orientation is a snip. Your
comment about OO/GUI being "awfully cumbersome" is a legitimate
reaction. I was horrified when I first looked at the Phone and Bank
demos - so much coding - but yuou have to look at it in the context of
separating the business application from the windowing techniques! 

For OO - a MicroFocus version of Dialog Editor is provided, includes
four more symbols than Microsoft - and you can generate your menus,
dialogs, retaining them in your myapp.rc. My own application is largely
table-driven and I intermix windows drawn with Dialog Editor, (giving a
frame, text labels etc), and add subpane tables of dynamically created
right-justified entry-fields.

Strictly speaking, there is nothing to stop you mixing OO/GUI with
Dialog System windows in an application - you can get the best of both
worlds.

As you know, you can describe to a layman, what COBOL is about in a
couple of sentences - not so with OO COBOL. If you want to get a handle
on OO before making a decision, check out following, which go beyond
theoretical, and use the MicroFocus compiler with coded examples :-

ISBN 0-13-261140-6 - Object-Oriented COBOL - Edmund C. Arranga and
Frank 	P Coyle ( I believe Edward Arranga has produced a later book)

	This one takes you through the theory and finishes up with a 
	complete application for a corporate in-house library system.
	(They do "cheat" however; the data-files are tables in Working
	Storage - but nevertheless does illustrate OO well).

ISBN 0-9655945-0-5 - Elements of Object-Oriented Cobol - Wilson Price
	(http://www.objectz.com) 

	Tutorial-based, aimed at students progressing from 		"conventional" 
into OO. The neat thing is Will Price shows 		REUSABILITY - I've adapted
his concepts for file handling. 		Briefly,  :-

        Main Menu       DBIMethods(Super)       FileMethods(Super)
           .                    .               .     .
           .                    .               .     .
        ClientsEdit     ClientsDBI              .   ClientsFile
                                                .
                                                FileErrors

For file handling ClientsEdit invokes ClientsDBI(*** - see below) which
automatically passes on requests to DBI Methods (a generic class -
containng methods for all COBOL file VERBS), accessing ClientsFile which
does following :-

"good-data" - record is returned from ClientsFile to DBIMethods which 
can either return complete record or CliensEdit can make additional
invokes for specific data in the record. (I could be accessing 30
different files and DBIMethods "knows" which file I'm calling because
for each there is an object reference handle).

"file-errors" - ClientsFile sends a message to FileMethods for file
status errors, which in turn invokes FileErros. 

*** ClientsDBI - I use this basically for creating dictionaries and
collections, (to become listboxes or droplists) and it invokes super
(DBIMethods) to access records.

*> ---------

Chances are you will go the Dialog System route - but come the Year 2005
we should all be using OO COBOL or the other OO languages, C's, Java etc
will take over.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: NetExpress Dialog vs. OO GUI

- **From:** "Simon Hart" <hart1@technologist.com>
- **Date:** 1999-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WWJa3.2833$w61.725@stones>`
- **References:** `<7kdotv$k6p$1@bgtnsc01.worldnet.att.net> <376AC775.FD16D566@home.com>`

```
> Having gone straight from DOS to Visoc(which didn't have Dialog System)
> I committed to OO/GUI. Now that I have NetExpress V 3 - it does have
…[79 more quoted lines elided]…
>

Have you ever wrote your own class to interact with a GUI object, im
thinking about taking the
GUI script from MSVC++ to handle IP numbers, as their is no object in the MF
dialog editor, nor
is there any class's that handle this, then writting a class in the GUI
libary to handle this new object.

Simon Hart
```

###### ↳ ↳ ↳ Re: NetExpress Dialog vs. OO GUI

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-06-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376C6F0B.B78958D0@home.com>`
- **References:** `<7kdotv$k6p$1@bgtnsc01.worldnet.att.net> <376AC775.FD16D566@home.com> <WWJa3.2833$w61.725@stones>`

```
Simon Hart wrote:
> 
> Have you ever wrote your own class to interact with a GUI object, im
> thinking about taking the GUI script from MSVC++ to handle IP numbers, > as their is no object in the MF dialog editor, nor  is there any 
>class's that handle this, then writting a class in the GUI 
> libary to handle this new object.

The quick answer to your question is No. Thank goodness I got Microsoft
Press Computer Dictionary on Friday before you wrote. I'm assuming 
MSVC++ must be M/S Visual C++ and IP(internet Protcol) - got me floored!

But being a rare breed, analyst turned programmer, rather than the other
way around - let's take it from an analytical perspective. Using the
Base class as your gateway to the platform (Windows98/NT), in theory at
least, there would be nothing to stop you inventing all your own classes
to replace MicroFocus classes; in practice of course, you would be nuts
if you did so! But there is nothing to prevent you sub-classing.

The class hierarchy structure isn't clear from the on-line help, because
for convenience, classes are shown as two groups Base and GUIs, with
subordinates listed alphabetically. But the name of the game is that
they are all subordinate to Base, including GUI itself.

The on-line help for class methods is sometimes terse, (taken from
comment notes written by the class developer) and in certain instances
method-names can be ambiguous. Consider the method "growto" for
collections - implies it can 'grow' to size n - but in fact the same
method will 'decrease' your collection to size n. (I only mention this
to illustrate that you could be led on a red herring trail).

I assume you've already done some browsing on the class source code -
not being clear what you are after I guess it could be a combination of
intrinsics and GUI. Before you re-invent the wheel, check-out with
Microfocus on your specific query; one of the OO gurus may confirm that
you could do it "this way" or "if you take a bit of this class and a bit
of that class" etc.....

As a last measure, you could write a completely new class as long as it
is subordinate to the relevant Super and obeys the rules about calls to
WinAPI.

Isn't this what C is all about, developers writing libraries of
routines(sub-classes). Instead of dynamically creating sub-pane tables
of entry-fields I would have preferred an elegant grid, (as in
spread-sheets) - but just don't have the time to research it. Such a
class, with parameters specifying say, subpane size (x y w h), number of
lines, number of columns, column widths etc. would be subordinate to
subpane(?) or paint(?)

Curious - let me know how you make out.

Jimmy, Calgary AB
```

#### ↳ Re: NetExpress Dialog vs. OO GUI

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kesl7$oce@dfw-ixnews13.ix.netcom.com>`
- **References:** `<7kdotv$k6p$1@bgtnsc01.worldnet.att.net>`

```
First, (to the best of my knowledge) Micro Focus *never* withdrew "Dialog
System".  Rather they "bundled it in" with some other products (different
products with different names at different times).

I haven't really looked at it yet, but it is my understanding that the
Dialog Systems in NetExpress V3 has some very definite enhancements over
previous versions.  Is the version of NetExpress that you are looking at V3?
```

#### ↳ Re: NetExpress Dialog vs. OO GUI

- **From:** "Robert Kovacic" <rjk@bigpond.com>
- **Date:** 1999-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ViJa3.12656$PN5.33442@newsfeeds.bigpond.com>`
- **References:** `<7kdotv$k6p$1@bgtnsc01.worldnet.att.net>`

```
Young Kim wrote in message <7kdotv$k6p$1@bgtnsc01.worldnet.att.net>...
>We are evaluating NetExpress and have noticed that Dialog is basically the
>old Dialog which MF used to market and then withdrew a few years ago.
>
>1) I am wondering if anyone out there is using the new Dialog......

We are using NetExpress 3.0. We decided that MF GUI/OO modules and Dialog
was not the way to go for us. Instead we have purchased the Flexus sp2
product for use with NetExpress. You should evaluate and include sp2 in your
options.
```

#### ↳ Re: NetExpress Dialog vs. OO GUI

- **From:** Scott Ramey <scottr@bdssoftware.com>
- **Date:** 1999-06-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376ED518.1227569A@bdssoftware.com>`
- **References:** `<7kdotv$k6p$1@bgtnsc01.worldnet.att.net>`

```
Young Kim wrote:
> 
> We are evaluating NetExpress and have noticed that Dialog is basically the
…[10 more quoted lines elided]…
> TIA

After doing years of GUI stuff in C, C++, and versions of Foxpro when I had to
start doing GUI in COBOL I chose SP2 from Flexus.  It lets me do what I need to
maintain fairly complete control over the screens, which can get pretty complex,
so I'm happy.  As far as the OO stuff is concerned, such as Fujitsu COBOL, I'm
not impressed.

Just my humble opinion.

Scott
```

##### ↳ ↳ Re: NetExpress Dialog vs. OO GUI

- **From:** "Dennis Griffith" <dgriffit@admin.usf.edu>
- **Date:** 1999-06-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7koo7k$7uq$1@news.usf.edu>`
- **References:** `<7kdotv$k6p$1@bgtnsc01.worldnet.att.net> <376ED518.1227569A@bdssoftware.com>`

```
Just a little bone to pick with people who post ....   I appreciate and am
enlightened with your comments... but please do not include comments like "I
am not impressed"... This gives no information at all other than your
personal feelings... Why are you not impressed????....  Give us some details
on what you are not impressed about... the speed?..the look?.. the
portability?..the maintenance?

I always want to wring the neck of someone who makes comments like "I hate
Unix..I hate VB...I hate COBOL"...tell me why? why? why? WHY???

Scott Ramey wrote in message <376ED518.1227569A@bdssoftware.com>...
>Young Kim wrote:
>>
>> We are evaluating NetExpress and have noticed that Dialog is basically
the
>> old Dialog which MF used to market and then withdrew a few years ago.
>>
…[5 more quoted lines elided]…
>> 3) We are wondering if we should jump ahead and use NetExpress web 100%
for
>> GUI/OO  - pros and cons?
>>
>> TIA
>
>After doing years of GUI stuff in C, C++, and versions of Foxpro when I had
to
>start doing GUI in COBOL I chose SP2 from Flexus.  It lets me do what I
need to
>maintain fairly complete control over the screens, which can get pretty
complex,
>so I'm happy.  As far as the OO stuff is concerned, such as Fujitsu COBOL,
I'm
>not impressed.
>
>Just my humble opinion.
>
>Scott
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
