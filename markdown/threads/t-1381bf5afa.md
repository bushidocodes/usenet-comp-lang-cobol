[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Learning OO COBOL - File Access Objects.

_29 messages · 8 participants · 2000-03_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo) · [`Tutorials, books, learning`](../topics.md#learning)

---

### Learning OO COBOL - File Access Objects.

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c557b1.59629519@news.cox-internet.com>`

```
When accessing data files using OO COBOL, how do you OO COBOL folks
organize your classes and methods?

Do you have a single Indexed File acces class with
Open/Read/Write/Rewrite/Delete/Close methods?  

How are the different FD's handled?  Do you have to have an override
method for each different file and
open/read/write/rewrite/delete/close method?

Is there any way to use different data definitions but common methods
for open/read/write/write/delete/close?

That's enough of a subject for this thread.  Looking forward to the
answers.
```

#### ↳ Re: Learning OO COBOL - File Access Objects.

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C569E5.5DD1912D@home.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com>`

```


Thane Hubbell wrote:
> 
> When accessing data files using OO COBOL, how do you OO COBOL folks
…[13 more quoted lines elided]…
> answers.

I think you've already picked up on my file-handling source. If you
haven't, e-mail me and I'll send it again. (Just to jog your memory it
was based on Wilson Price's (objectz.com) technique - (1) an editing
program requiring access to a file/files, (2) the DB interface for the
specific file (3) A class Super DBI that the individual DBIs get methods
from and (4) the specific file containing use of all the file verbs).

Jimmy
```

#### ↳ Re: Learning OO COBOL - File Access Objects.

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z3ex4.123709$45.6251485@news2.rdc1.on.home.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com>`

```
Welcome to the world of OO design. Don't assume that data is stored in a
file that can be accessed using COBOL verbs. It may be a relational
database, IMSDB database, ODBC interface, proprietary API, streams, etc. The
real trick in building a class library is thinking about likely future
modifications and doing a reasonable amount of work initially to make those
future modifications easy.

While I may have a class that deals with COBOL files it would be subclassed
to hide the mechanics of a READ (OPEN, START, READNEXT,etc.) in a get()
method, using global variables or some other method to keep track of whether
or not a file is already open. The class would also be responsible for it's
own error handling, probably making use of a common error handling class.

Karl Wagner

"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:38c557b1.59629519@news.cox-internet.com...
> When accessing data files using OO COBOL, how do you OO COBOL folks
> organize your classes and methods?
…[12 more quoted lines elided]…
> answers.
```

##### ↳ ↳ Re: Learning OO COBOL - File Access Objects.

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c57de7.69413320@news.cox-internet.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com>`

```
On Tue, 07 Mar 2000 20:58:07 GMT, "Oscar T. Grouch" <dustbin@home.com>
wrote:

>Welcome to the world of OO design. Don't assume that data is stored in a
>file that can be accessed using COBOL verbs. It may be a relational
…[10 more quoted lines elided]…
>

Very good and valid points.  Let's talk about these Global variable
flags for a minute.  I can see the need.  You invoke a method to
create an object.  This method uses the "get" method described above.
This method must invoke the Open and Read methods - Where does one
keep this flag?  Not part of the object!  Or does one create a file
state object and examine it's properties before deciding if another
open is required?  When talking about a Global variable, are you
saying to keep it in the mainline routine, then reference it in your
"get" method?  Doesn't that violate encapsulation?

Fujitsu offers the ability to create an exception that is caught in
the declaratives of the invoking routine, by using the RAISE verb.
Does MicroFocus offer this?

Also, do any other COBOL vendors off OO extensions.
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a4k6o$n7$1@slb7.atl.mindspring.net>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <38c57de7.69413320@news.cox-internet.com>`

```
Thane Hubbell <thaneH@softwaresimple.com> wrote in message
>
> Fujitsu offers the ability to create an exception that is caught in
> the declaratives of the invoking routine, by using the RAISE verb.
> Does MicroFocus offer this?
>

FYI,
  RAISE, RESUME, exception-objects, and exception declaratives are all part
of the draft Standard.  I don't know if NetExpress supports them yet or not -
but they will when/if MERANT provides a (future) Standard conforming
implmentation.
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64ix4.125091$45.6316954@news2.rdc1.on.home.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <38c57de7.69413320@news.cox-internet.com>`

```

"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:38c57de7.69413320@news.cox-internet.com...
> On Tue, 07 Mar 2000 20:58:07 GMT, "Oscar T. Grouch" <dustbin@home.com>
> wrote:
…[3 more quoted lines elided]…
> >database, IMSDB database, ODBC interface, proprietary API, streams, etc.
The
> >real trick in building a class library is thinking about likely future
> >modifications and doing a reasonable amount of work initially to make
those
> >future modifications easy.
> >
> >While I may have a class that deals with COBOL files it would be
subclassed
> >to hide the mechanics of a READ (OPEN, START, READNEXT,etc.) in a get()
> >method, using global variables or some other method to keep track of
whether
> >or not a file is already open. The class would also be responsible for
it's
> >own error handling, probably making use of a common error handling class.
> >
…[9 more quoted lines elided]…
> "get" method?  Doesn't that violate encapsulation?

I used the term 'global variable' to couch it in terms that you would find
familiar. Java would call it a 'class variable' which is scoped at the class
level, rather than at the object level. A common technique is to define the
class variable then define methods to modify or query it. A method like
isOpen() would return it's value within the object. If the implementation
does not support class variables then there are other ways to accomplish the
same thing, with varying performance and coding impacts.

>
> Fujitsu offers the ability to create an exception that is caught in
> the declaratives of the invoking routine, by using the RAISE verb.
> Does MicroFocus offer this?

Other languages use throw, try and catch to implement exception handlers.
I'm sure one of the Merant OO COBOL types will provide an answer. Most of my
familiarity with OO programming comes from languages other than COBOL.
Blasphemy! I know but what can you do?

>
> Also, do any other COBOL vendors off OO extensions.

My company has a product (almost 20 years old now) that implements a
quasi-OO paradigm to assemble source code. I use that to get the benefits of
OO in COBOL without locking in to a particular vendor's implementation. It's
NOT OO but there are a lot of parallels in how it assembles source code,
including inheritance (including multiple inheritance), polymorphism and
encapsulation.

Karl Wagner
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C69B1E.8BDF788@home.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <38c57de7.69413320@news.cox-internet.com> <64ix4.125091$45.6316954@news2.rdc1.on.home.com>`

```


"Oscar T. Grouch" wrote:
> 
> "Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
> news:38c57de7.69413320@news.cox-internet.com...
> > On Tue, 07 Mar 2000 20:58:07 GMT, "Oscar T. Grouch" <dustbin@home.com>
> > wrote:

Karl,

Thane has raised a whole daffy of questions regarding file handling -
and has now asked me to send the source of what I'm doing. It resolves
all the questions he was asking about file handling - and even with it's
imperfections - is a working model that can be used for flat files.

You both mentioned the topic exception handling. Fujitsu and Merant both
provide it - they have to - if you invoke a missing method or make a
typo on the method-name they have to have a mechanism to report it - the
exception handling takes you to class FjBase or Base (in the case of
Merant) and you get 'Don't understand message ...."; I don't use it but
you can override the exception handling and insert your own for a given
circumstance.

Now with regard to Thane's query about file handling - and specifically
flat-files - and I'm pretty sure the technique could be adapted to
whichever DB you are using - this diagram illustrates what I have I have
designed, based on the model produced by Wilson (Will) Price of
objectz.com :-

	(1) Main App/Main Menu
	    .
	    .
	    .
	(2a)Print Program(Class)
	(2b)Edit Program
	    .
	    .
	    .
   (3)Customer DBI....inherits from ..>(4) DBI Methods...>(5)Customer
							     File
								.
								.
								.
							  (6) File 								      Errors
	

- In my case I have established handles for all files I need at (1)
- from (1) I invoke (2a) or (2b) passing (1) as a handle MyApp to either
- 2a or 2b. 2 invokes 'back' to (1) to get any file handles that it
  needs (I've 'assembled' filenames at (1) because I'm using many 
  sub-packages of data, (Oil Company # 1 Plant # 16)
- 2 invokes 3 to open file which is passed via Super (4) on to (5) where
  only one method uses all the file verbs - so file-status is retained
  in (5) - any file-status errors are passed on to the generic (6)      
saying which filename and which file-error and (6) then spits out a    
messagebox with the error. ( 6 contains all the ANSI file errors plus
  Merant extensions in Working-storage tables).

- typically 2 just says invoke MyCustomerDBI "read-next-record"; if it
  was "start-primekey" or "read-primekey" then it also passes the key.
- 3 doesn't concern itself but passes that message on to 4 - which
sets   a flag saying which verb to use - this verb flag is passed to 5 -
  which accesses the record and found/notfound - returning the          
access-result plus a copy of the record - to 4 - which means 3 has got  
it, because it is a sub-class 4.
- Note most of the donkey-work for file-handling occurs in 4, completely
  by-passing 3 - the latter serves as a 'retainer' where I can say    
from (2) invoke MyCustomerDBI "get-zipcode" or (3) also acts as a    
'retainer' to build up lists(collections/dictionaries) primarily used  
for listboxes/droplists. 
- now either the whole record is returned to 2 or only specific data
  to meet the particular query, based on the original message
passed      from 2.

Hope the above doesn't sound like mumbo jumbo - and I've used the
numbers, hoping to illustrate easier what it is doing.

So forget all about your syntactical get() set () etc... You do it in
plain English in COBOL - and use our traditional file-status to pick up
on errors.  :-)

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c72d41.6642459@news.cox-internet.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <38c57de7.69413320@news.cox-internet.com> <64ix4.125091$45.6316954@news2.rdc1.on.home.com> <38C69B1E.8BDF788@home.com>`

```
On Wed, 08 Mar 2000 18:29:16 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:


>Now with regard to Thane's query about file handling - and specifically
>flat-files - and I'm pretty sure the technique could be adapted to
…[3 more quoted lines elided]…
>

Congrats Jimmy - this is the first Unsenet message I have ever printed
out.  I do appreciate your taking the time to type all this in!
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C65D66.682459A2@zip.com.au>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <38c57de7.69413320@news.cox-internet.com>`

```
Thane Hubbell wrote:
> 
> Very good and valid points.  Let's talk about these Global variable
…[7 more quoted lines elided]…
> "get" method?  Doesn't that violate encapsulation?

The file object would actually store a status variable as part of it's
instance (this object not any other).  This is an optimization you may
choose to do later.  I would design it to automatically open the file
when I create the class.  Current cobol standards imply you would have
to code a 'completion' or finalize method that is explicitly called by
you program (I would like it automatically called during the object
cleanup).  This finalize method would close the file.

Global variables are very, very bad.  Everything is an object and must
be thought of as one.

By the way mapping of data to a relational database is one of the
classic problems of OO.  They are designed differently.  You
effectively totally hide the database behind an object cover and then
think about when you really read the data off the table.  Day one you
simply load everything, when you work out you are trying to read to
much you can put in lazy initialization, only read data when truly
accessed.

Interesting site, migrating from procedural to OO: 

http://www.projtech.com/pdfs/migr.pdf

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c73091.7490843@news.cox-internet.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <38c57de7.69413320@news.cox-internet.com> <38C65D66.682459A2@zip.com.au>`

```
On Thu, 09 Mar 2000 01:02:14 +1100, Ken Foskey <waratah@zip.com.au>
wrote:


>The file object would actually store a status variable as part of it's
>instance (this object not any other).  This is an optimization you may
…[5 more quoted lines elided]…
>

Maybe I am thinking at too low a level.  I was considering a "record"
object (Possibly populated from multiple files).  Now I don't know why
it couldn't get the data from a file object.

I dislike having the files left open (especially I/O) when not
actually being updated.  My present code closes the files unless being
used.  The extra overhead of opening for each use is usally hidden by
the local machines cachine, and more than offsets the inconvenience of
corrupted files.  That will certainly impact my design.  But I suppose
that if you create a file object for each access, you really don't
need to track it's open status.

BTW: Fujitsu's finalize is as you desire with v5 at least - I don't
know if it closes open files.  Bill - does the standard mention that
all files are closed after an exit-method (I hope NOT) as was true
with Exit-Program?

>
>Interesting site, migrating from procedural to OO: 
>
>http://www.projtech.com/pdfs/migr.pdf
>

I have not had time to visit all of the sites you have mentioned yet,
but I do appreciate your mentioning them!
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 5)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C74362.2AEB2CF@zip.com.au>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <38c57de7.69413320@news.cox-internet.com> <38C65D66.682459A2@zip.com.au> <38c73091.7490843@news.cox-internet.com>`

```
Thane Hubbell wrote:
> 
> Maybe I am thinking at too low a level.  I was considering a "record"
> object (Possibly populated from multiple files).  Now I don't know
> why it couldn't get the data from a file object.

Simply put, would you start any application by defining what file
structure you would use.

First define your business object, just quickly I can see we have
projects, a time sheet, employees, ....

Next what do these object do?

Methods should be asking the object to do something.  Getting
information and setting information is really breaking encapsulation.

If we talk about shoes again, we can ask how many shoes this object
has and then put them on or we can just ask the object the put them on
and not care about how many, or special tricks to attach them to a
millipede.

I have not sat down and thought about your stuff yet.  I will get to
this promise.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: Learning OO COBOL - File Access Objects.

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a5kr8$gvf$1@nnrp1.deja.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com>`

```
In article <z3ex4.123709$45.6251485@news2.rdc1.on.home.com>,
  "Oscar T. Grouch" <dustbin@home.com> wrote:

>>The class would also be responsible for it's
>>own error handling, probably making use of a common error handling
>>class.

Although my knowledge of OO could be engraved on the head of a
pin with enough room left over for a PL/I manual, perhaps I should
shut up.

In my experience, a 'common error handling class' (routine) is a curse.
This class (subroutine) which would open, read, etc. must
be able to distinguish between application errors (no data),
locked files and records, system errors (damaged file), etc.  I have
never been able to come up with satisfactory common I/O routines which
would consider EVERY eventuality and provide MEANINGFUL error messages
to the user without making the routine complicated.

For example, the 'READNEXT' must differentiate between an
AT END on the first read versus all reads after the first.
Depending on the application, perhaps the OPEN should create
the file if it does not already exist, etc. So, I think your classes
need to consider this level of detail otherwise they are NG.

Since Thane plans on developing a simple application and presenting
its evolution to the forum, we should consider real-world requirements
rather than handing off one's responsibilities to a 'common error
handling class' and make the application complete.

Thanks

TOny DIlworth



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Ptx4.512$K5.20796@news2.rdc1.on.home.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com>`

```
A common error handler, or any class for that matter, does not necessarility
deal with EVERY eventuality in every context. It deals with the things that
are generic. If you want to concern yourself with a specific eventuality
then you override the default handler with one that makes more sense in that
specific context.

Clearly a getNext() method should return an 'at end' condition in MOST
cases. I would argue that the best way to do this is to have the data access
method 'throw' the exception and have my application code 'catch' the
exception, rather than allowing it to pass to the default error handler.

The default exception handler should probably know the difference between a
recoverable and a fatal error. I would expect the data access error routine
to provide notification methods (logging, operator 'shouts', etc.), default
methods for fatal errors (disk full, file not found, etc.) maybe some
deadlock detection and anything else that should be handled, but not coded
again and again and again and again and again and...

Karl Wagner



"Foodman" <foodman123@aol.com> wrote in message
news:8a5kr8$gvf$1@nnrp1.deja.com...
> In article <z3ex4.123709$45.6251485@news2.rdc1.on.home.com>,
>   "Oscar T. Grouch" <dustbin@home.com> wrote:
…[35 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a5s2p$uo$1@news.igs.net>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com>`

```
The approach that I am taking is a mixture.  I have some common utility
routines (like a common place to store file ID's, and standardised waits for
lock routines) that can be inherited. Then I create a new object for each
file in a system.

Those are file dependent, but with standardised names for the methods.  One
thing that I have included in the standard class is a dump to a sequential
file, and a reload from a sequential file for all Isam files.  That allows
emergency patching with a text editor, and makes conversions from one
version of the software to the next much easier.

The methods that I am using are very close to what Thane laid out. In effect
open-file, close-file, start-key-name1, start-key-name-two, read, read-next,
write, etc.

I am not quite sure if this will be the way I do it a year or two from now.
Unfortunately, the learning curve on this stuff is fairly steep, and I have
a hunch that it will be the third or fourth system that gets it right.  One
thing that I do see buried in the file object is all the recovery methods.
The standard file dump and reload has also proved to be a godsend during
development.  I am thinking of adding a method that dumps to sequential,
edits with a file editor, and reloads just for program development. The
advantage of OOP is that as soon as I add it to the base method, it is
available for every file on every system.


Foodman wrote in message <8a5kr8$gvf$1@nnrp1.deja.com>...
>In article <z3ex4.123709$45.6251485@news2.rdc1.on.home.com>,
>  "Oscar T. Grouch" <dustbin@home.com> wrote:
…[35 more quoted lines elided]…
>Before you buy.
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c72fb8.7273664@news.cox-internet.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com> <8a5s2p$uo$1@news.igs.net>`

```
On Wed, 8 Mar 2000 10:40:07 -0500, "donald tees" <donald@willmack.com>
wrote:

>The standard file dump and reload has also proved to be a godsend during
>development.  I am thinking of adding a method that dumps to sequential,
…[4 more quoted lines elided]…
>

This is where I am "blocked" presently.  I can see, because of FD's
that a separate object must be created for each file.  How can you
create a method that handles the dump/reload with all the different
data/key structures of your indexed files - without recoding an
override method for each file description?  I just don't see how it
will be availabe for every file.  Unless... as I am typing the light
went on I think.  FLASH.  The method uses the read method of whatever
file object it is accessing - so it CAN be available to all of them.
Wow.  See how that works?
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C81B5F.69A907AE@home.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com> <8a5s2p$uo$1@news.igs.net> <38c72fb8.7273664@news.cox-internet.com>`

```


Thane Hubbell wrote:
> 
> On Wed, 8 Mar 2000 10:40:07 -0500, "donald tees" <donald@willmack.com>
…[18 more quoted lines elided]…
> Wow.  See how that works?

Click..., click..., click..... See you are getting it. The more you get
into this OO stuff the more you realize how infinitely flexible the
whole thing is. And here we are in COBOL just dipping our toes into the
water at the edge of the lake - merely on the threshold.

And I think Don's suggestion about standardizing - not just OO - on
representing numerics is an extremely good idea for 'swapping' data -
but unfortunately, because of many arguments that would be put forward
about performance - it is likely to get the cold shoulder.

Jimmy
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a9iet$309$1@news.igs.net>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com> <8a5s2p$uo$1@news.igs.net> <38c72fb8.7273664@news.cox-internet.com> <38C81B5F.69A907AE@home.com>`

```
James J. Gavan wrote in message <38C81B5F.69A907AE@home.com>...
>
>
…[32 more quoted lines elided]…
>

Yup.  At to-days hardware prices, it would probably use up enough CPU time
to buy coffee for at least two programmers a year.  I see they are giving
away Pentiums in cornflake boxes this week ...

BTW, did I tell you about my new watch?  It has a cellular internet
connection, 2 megs of memory, a 2 gig hardisk ... but boy those tiny little
keys are a bitch for my tired old eyes ...

;<*~
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c886e4.95139128@news.cox-internet.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com> <8a5s2p$uo$1@news.igs.net> <38c72fb8.7273664@news.cox-internet.com> <38C81B5F.69A907AE@home.com>`

```
On Thu, 09 Mar 2000 21:50:59 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

Posted and mailed.

>And I think Don's suggestion about standardizing - not just OO - on
>representing numerics is an extremely good idea for 'swapping' data -
>but unfortunately, because of many arguments that would be put forward
>about performance - it is likely to get the cold shoulder.
>

That's too bad, too.  Where I am now, our standard file structure is
just as Don described.  We have rehosted, ported and shared data for
and with just about everyone, from Ebcdic to Ascii, from AS/400 to
S/390 and from DEC (Compaq) to Wang.  The benefits far far outweigh
any performance hit.
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C6BF97.EBC2FD0F@home.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> In article <z3ex4.123709$45.6251485@news2.rdc1.on.home.com>,
…[16 more quoted lines elided]…
> to the user without making the routine complicated.

The following is for flat-files and a single user, but it can be
adapated to your EVERY, including locks. This is for my Clent File
(Customer File if you will). This is the only method that actually
'touches' Client records, is self-contained on file-status checks,
invoking FileErrors when they occur. I have listed only those verbs that
apply to this particular indexed file, for sequentials and relatives,
I add the appropriate verbs and also discard those not applicable  :-

It doesn't show in the source here, but my " +++ ", using a template for
a file, indicates which lines to change to fit a specific file. Given
the data structure of a new file, it can be reproduced within some
thirty minutes giving you a compiled error-free program. 

So far as your application is concerned - this is the only access to the
file. Sure, you can make logic errors in your calling programs, but
where appropriate they will show here as file-status errors.

*>-----------------------------------------------------------           
Method-ID. "access-file".                                               
*>-----------------------------------------------------------           
input-output section.                                                   
                                                                        
 set keycompress"7"                                                     
 set datacompress"1"                                                    
                                                                        
*>    NOTE :      link with cbldc001.obj                                
                                                                        
*>  Add additional info for alternate keys                              
                                                                        
copy "clients1.cpy" replacing ==(tag)== by ==Data==.                    
                                                                        
File Section.                                                           
FD  Data-File.                                                          
01  Data-record.                                                        
copy "clients2.cpy" replacing ==(tag)== by ==Data==.           *> +++   
                                                                        
Linkage Section.                                                        
copy "fileactn.cpy".                                                    
01 lnk-PrimeKey                          pic x(06).            *> +++   
01 lnk-result                            pic x(4) comp-5.               
                                                                        
Procedure Division Using     file-action                                
                             lnk-PrimeKey                      *> +++   
                   returning lnk-result.                                
                                                                        
*> "evaluates" below are listed in most likely frequency sequence       
*> for this particular file                                             
                                                                        
   set file-result-ok to true                                           
   initialize ws-Error-Data                                             
                                                                        
   if   dont-initialize                                                 
        continue                                                        
                                                                        
   else initialize os-record                                            
   End-if                                                               
                                                                        
   Evaluate TRUE                                                        
                                                                        
     When read-PrimeKey                                                 
                                                                        
      move lnk-PrimeKey to Data-PrimeKey                                
      Read Data-File                                                    
        Invalid key                                                     
          Set record-not-found to True                                  
        Not invalid key                                                 
          Move Data-record to os-record                                 
      End-Read                                                          
                                                                        
     When read-next                                                     
                                                                        
      Read Data-File next record                                        
        At End                                                          
          Set file-finis to True                                        
        Not at End                                                      
          Move Data-record to os-record                                 
      End-Read                                                          
                                                                        
     When start-PrimeKey                                                
                                                                        
      Move lnk-PrimeKey to Data-PrimeKey                                
      Start Data-File key >= Data-PrimeKey                              
        Invalid key                                                     
          Set file-finis to True                                        
      End-Start                                                         
                            *> DBIMethods "rewrite-record"              
                            *> uses 'set-file-object' below             
     When rewrite-record                                                
                                                                        
      move os-record to Data-record                                     
      Rewrite Data-record                                               
                                                                        
                            *> DBIMethods "write-record"                
                            *> uses "set-file-object' below             
     When write-record                                                  
                                                                        
      move os-record to Data-record                                     
      Write Data-record                                                 
                                                                        
     When delete-record                                                 
                                                                        
      if  lnk-PrimeKey = os-PrimeKey                                    
          Delete  Data-File record                                      
      End-if                                                            
                                                                        
     When read-previous                                                 
                                                                        
      Read Data-File previous record                                    
        At End                                                          
          Set file-finis to True                                        
        Not at End                                                      
          Move Data-record to os-record                                 
      End-Read                                                          
                                                                        
     When close-file         Close Data-File                            
     When open-io-file       Open I-O Data-File                         
     When open-input-file    Open input Data-File                       
     When open-output-file   Open output Data-file                      
                                                                        
                                                                        
    When other                                                          
      invoke super "invalid-action" using file-action                   
      set file-error to true                                            
                                                                        
   End-evaluate                                                         
                                                                        
   if ws-filestatus <> "00"                                             
      move os-PrimeKey  to ws-error-key        *> +++                   
      move os-Shortname to ws-error-name       *> +++                   
      invoke super "check-file-status"                                  
             using     ws-ErrorFields                                   
                       file-action                                      
                       ws-file-result                                   
             returning lnk-result                                       
                                                                        
   else move ws-file-result to lnk-result                               
   End-if                                                               
End Method "access-file".                                               
*>---------------------------------------------------------------       


Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a85sf$coj$1@nnrp1.deja.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com> <38C6BF97.EBC2FD0F@home.com>`

```
In article <38C6BF97.EBC2FD0F@home.com>,
  "James J. Gavan" <jjgavan@home.com> wrote:

> Method "Access-File"

Thanks for taking the time to send 'Access-File'.

However, I do think that it is a little over-simplified.
Surely, most files have multiple keys. Your method would
require starts for each of those keys, and perhaps different
types of starts. Furthermore, depending on the application,
the same file-status may have different meanings. Presumably,
these are handled in the program which calls 'access-file'.
Is it an oversight that you do not check for errors in 'write-record',
'rewrite-record', and 'delete'?

I think if your method had to consider all these other things,
it would become much larger. Anyway, does the Main program
not have to test the status anyway, to find out what the method
did?

If it isn't too much trouble, could you provide a copy of the
Main program which would show the use of 'Access-File'.

Thanks

Tony Dilworth



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C822CF.2F639422@home.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com> <38C6BF97.EBC2FD0F@home.com> <8a85sf$coj$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> In article <38C6BF97.EBC2FD0F@home.com>,
…[4 more quoted lines elided]…
> Thanks for taking the time to send 'Access-File'.

Believe me it isn't over-simplified. Thane, at Tony's request I'll do
some extracts to show how it pieces together - and it will also answer
your query about my "invalid file-action" bit which our friend Ken would
probably say is XP - me I call it belt and braces or perhaps more
clearly "peace-of-mind" for me; I know it's going to work and I've
trapped yet another eventuality of an error occurring in a message being
passed to the file class. 

Regarding the oversight on writing, rewriting, deleting etc... that
puzzled me a bit until I went back and looked at the source. Now here's
the problem - I've hived off the file handling as a totally separate
entity - so the method I'm showing you doesn't show the complete story.
I think the extracts I produce will. Your oversight is covered in the
''Edit Customer File' class so :-

	read record
	if found set RecordFound to true
	         set RecordNotChanged to true
		 then display it
		 (set flag-changed if user changes anything)

	if not found
		 set RecordNotFound to true
		 set Record NotChanged to true
		 start accepting new data

Now following on (in the Edit) from :-

	OK update :-

	if	recordFound
		rewrite record

	else	write record

and 	from OK to delete this ? -

	delete-no display empty-screen

	delete-yes if RecordFound
		      then delete
		      display empty-screen

Bear with me Tony, while I do those extracts. I think you see it is more
advantageous to develop something through a series of articles for
cobolreport.com rather than random bits and pieces here.

Howard - I noted you recently used the phrase 'belt and suspenders' - is
that legit Yankee talk or did you folks yet again Americanize - by
translating my  English-English 'belt and braces' ?

Jimmy
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c8862b.94954318@news.cox-internet.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com> <38C6BF97.EBC2FD0F@home.com> <8a85sf$coj$1@nnrp1.deja.com> <38C822CF.2F639422@home.com>`

```
On Thu, 09 Mar 2000 22:23:11 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

Posted and mailed.

>
>	read record
>	if found set RecordFound to true
>	         set RecordNotChanged to true
>		 then display it

A not really OO Query here.

I notice you using a RecordNotChanged flag.  What causes it to get set
to RecordChanged?

Presently, when I read a record, I store a copy in a "Last Record"
area, so that I can compare before tossing the present record and warn
the user of a not saved state.  It's wasteful, but only a single
compare.  Tell me a bit about your flag - I like it better than what I
have done.
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C89830.6AE1422F@home.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com> <38C6BF97.EBC2FD0F@home.com> <8a85sf$coj$1@nnrp1.deja.com> <38C822CF.2F639422@home.com> <38c8862b.94954318@news.cox-internet.com>`

```


Thane Hubbell wrote:
> 
> On Thu, 09 Mar 2000 22:23:11 GMT, "James J. Gavan" <jjgavan@home.com>
…[19 more quoted lines elided]…
> have done.

Briefly the return entry-field/droplist-selection/radio-button selection
etc ....event from Dialog - if it's not the PrimeKey then set
RecordChanged to true and of course, change contents of field in the
'carbon-copy' I'm holding in the Edit program.

Now watch it - don't start throwing things away. Are you into a
multi-user situation, because if so then maybe your carbon-copy approach
has benefit. (In what I'm trying to send you at the moment 23:30
Mountain Time - you'll see a reference to these flags.).

Curious Ken ? - this guy is jumping hoppity-hoppity so I'm giving him an
early-bird on TechsEdit - while I finish testing a third dialog where
I'm dynamically creating entryfields.

Ohhhhhh Yes. Steve - no doubt you will read this. When is M/F going to
play catch-up with Dialog Editor and give me single-line, right,
centered, left-justified a la Microsoft ? - the headaches I've had with
MLEs and the ENTER key ..... :-) 

Jimmy
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C8983A.2F15C59F@home.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com> <38C6BF97.EBC2FD0F@home.com> <8a85sf$coj$1@nnrp1.deja.com> <38C822CF.2F639422@home.com> <38c8862b.94954318@news.cox-internet.com>`

```


Thane Hubbell wrote:
> 
> On Thu, 09 Mar 2000 22:23:11 GMT, "James J. Gavan" <jjgavan@home.com>
…[19 more quoted lines elided]…
> have done.

Briefly the return entry-field/droplist-selection/radio-button selection
etc ....event from Dialog - if it's not the PrimeKey then set
RecordChanged to true and of course, change contents of field in the
'carbon-copy' I'm holding in the Edit program.

Now watch it - don't start throwing things away. Are you into a
multi-user situation, because if so then maybe your carbon-copy approach
has benefit. (In what I'm trying to send you at the moment 23:30
Mountain Time - you'll see a reference to these flags.).

Curious Ken ? - this guy is jumping hoppity-hoppity so I'm giving him an
early-bird on TechsEdit - while I finish testing a third dialog where
I'm dynamically creating entryfields.

Ohhhhhh Yes. Steve - no doubt you will read this. When is M/F going to
play catch-up with Dialog Editor and give me single-line, right,
centered, left-justified a la Microsoft ? - the headaches I've had with
MLEs and the ENTER key ..... :-) 

Jimmy
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c7312d.7646604@news.cox-internet.com>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com> <38C6BF97.EBC2FD0F@home.com>`

```
On Wed, 08 Mar 2000 21:06:11 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:


GREAT!  Thanks Jimmy.  Let's dissect just one small portion of this
for me.


 >

>    When other                                                          
>      invoke super "invalid-action" using file-action                   
>      set file-error to true                                            
>                                                                        
>   End-evaluate                                                         


This one.  When you invoke "invalid-action" you are using SUPER as the
class reference.  What does tihs mean to you?  To me this means that
you are invokng a method in the class you inherit from - even if a
method of the same name exists in your present class - and that no
related object has been created.  Is that true?  What did I miss?
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

_(reply depth: 5)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C741A8.8E0C660B@zip.com.au>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <z3ex4.123709$45.6251485@news2.rdc1.on.home.com> <8a5kr8$gvf$1@nnrp1.deja.com> <38C6BF97.EBC2FD0F@home.com> <38c7312d.7646604@news.cox-internet.com>`

```
Thane Hubbell wrote:
> 
> This one.  When you invoke "invalid-action" you are using SUPER as
…[3 more quoted lines elided]…
> related object has been created.  Is that true?  What did I miss?

That's a gold star for you...

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: Learning OO COBOL - File Access Objects.

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a7683$m98$1@news.igs.net>`
- **References:** `<38c557b1.59629519@news.cox-internet.com>`

```
As I see it, we start with some simple objects that can be implemented with
accept/display statements.  Things like
DISPLAY "THIS IS STATIC TEXT" AT LINE X COLUMN Y BACKGROUND-COLOUR
PALE-BLUE.."
.
Using those and basic mouse trapping, I can write a text GUI that would run
on an XT if I still had one.

 A pushbutton should take an expert about an hour.

 We then emulate those objects with SP2. Swap DLLS, and we have a gui.
Later, we can add new attributes like borders arround the buttons.  Existing
code can be converted to that as a standard. Nothing but standard Cobol is
needed, not even a screen section, and we can covert anything to GUI.

The key is that upgrading now becomes quite simple.  We can test setting new
attributes and starting to add new pictorial attributes to existing objects
on an existing screen.  Systems can make graphical attributes available to
the user as they are tested. The business aspects of the of the software
have nothing to do with the human interface, and it can be changed strictly
within the DLL.

Give us an expert at HTML, and we have another DLL. Swap DLLS and upgrade to
CGI.

Same with Isam.  Build some simple objects and standardize the interface
early.  I will propose a standard right here and now.  Object data records
should never contain comp field of any type, BCD should never be used, and
all signed numeric data should be SIGN SEPARATE LEADING. That way, every
cobol in the world can talk to every other Cobol in the world.  If everybody
in this echo agreed to use that, we would have made a good start.

Then swap a central data base DLL, or client server DLL. If I can code it as
simple open, close, start, read-next, or whatever, then you can convert the
I/O to anything you like.

Keep it simple, and the same program runs as a dos program with a mouse, a
GUI or a net application, all at the cost of renaming a DLL.

Thane Hubbell wrote in message <38c557b1.59629519@news.cox-internet.com>...
>When accessing data files using OO COBOL, how do you OO COBOL folks
>organize your classes and methods?
…[12 more quoted lines elided]…
>answers.
```

##### ↳ ↳ Re: Learning OO COBOL - File Access Objects.

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a8koh$lpa$1@news.cerf.net>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <8a7683$m98$1@news.igs.net>`

```
"donald tees" <donald@willmack.com> wrote in message
news:8a7683$m98$1@news.igs.net...
> DISPLAY "THIS IS STATIC TEXT" AT LINE X COLUMN Y BACKGROUND-COLOUR
> PALE-BLUE.."

> Give us an expert at HTML, and we have another DLL. Swap DLLS and upgrade
to
> CGI.

To my understanding, with Acucobol the above will display on gui, character
and www. Without swapping DLLs.

The killer here would of course be to use screen section and then be able to
provide graphical controls too, leaving to the runtime to determine whether
to use the gui or character definition.

Isn't that easy enough?

Cheesle
```

###### ↳ ↳ ↳ Re: Learning OO COBOL - File Access Objects.

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-03-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a917f$msi$1@news.igs.net>`
- **References:** `<38c557b1.59629519@news.cox-internet.com> <8a7683$m98$1@news.igs.net> <8a8koh$lpa$1@news.cerf.net>`

```

Cheesle wrote in message <8a8koh$lpa$1@news.cerf.net>...
>"donald tees" <donald@willmack.com> wrote in message
>news:8a7683$m98$1@news.igs.net...
…[10 more quoted lines elided]…
>The killer here would of course be to use screen section and then be able
to
>provide graphical controls too, leaving to the runtime to determine whether
>to use the gui or character definition.
…[4 more quoted lines elided]…
>
No, it is not easy.  Damnit.  But I am getting there.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
