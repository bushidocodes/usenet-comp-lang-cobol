[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Allocating memory dynamically in cobol...

_18 messages · 9 participants · 2005-01_

---

### Allocating memory dynamically in cobol...

- **From:** "XPPROGRAMMER" <saud_abraham@hotmail.com>
- **Date:** 2005-01-26T09:48:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com>`

```
Hello,

when using win32 API functions in cobol, is it more
efficient performance wise to allocate the needed memory
dynamically for each function call -- or should I let the
the runtime system handles this task automatically?
i am using micro focus Net Express with windows 2000 pro.
thanks for the help.
```

#### ↳ Re: Allocating memory dynamically in cobol...

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-01-26T18:47:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1BRJd.23436$by5.4944@newssvr19.news.prodigy.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com>`

```
"XPPROGRAMMER" <saud_abraham@hotmail.com> wrote in message
news:1106761730.476849.173630@f14g2000cwb.googlegroups.com...
> Hello,
>
…[5 more quoted lines elided]…
> thanks for the help.

I'd say as a general rule let the compiler/runtime  handle it... after all,
that's why you use a high-level language, isn't it? So you can focus on the
APPLICATION rather than the operating system?

MCM
```

##### ↳ ↳ Re: Allocating memory dynamically in cobol...

- **From:** "XPPROGRAMMER" <saud_abraham@hotmail.com>
- **Date:** 2005-01-26T10:54:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106765676.939101.138050@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1BRJd.23436$by5.4944@newssvr19.news.prodigy.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <1BRJd.23436$by5.4944@newssvr19.news.prodigy.com>`

```
thanks MCM, You made a good point though.

john.
```

#### ↳ Re: Allocating memory dynamically in cobol...

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-01-26T22:56:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10vgt3f908bo721@news.supernews.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com>`

```
XPPROGRAMMER wrote:
> Hello,
>
…[5 more quoted lines elided]…
> thanks for the help.

First displaying pointers, now dynamic memory allocation!

Mark my words, young man, if you write C++ programs in COBOL, you'll come to 
grief.
```

##### ↳ ↳ Re: Allocating memory dynamically in cobol...

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-27T08:01:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<905hv0pb0n7da15us4uktn904ei705brg9@4ax.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com>`

```
On Wed, 26 Jan 2005 22:56:15 -0600, "JerryMouse" <nospam@bisusa.com>
wrote:

>XPPROGRAMMER wrote:
>> Hello,
…[11 more quoted lines elided]…
>grief. 

Constructors in OO Cobol and C++ work the same way: they manage
pointers to dynamic memory under the covers. For example, " invoke foo
'new' returning foo-handle (n)" and "foo *foo_handle[n] = new foo;"
are equivalent. Do you think OO Cobol is the spawn of the devil?
```

###### ↳ ↳ ↳ Re: Allocating memory dynamically in cobol...

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-27T11:23:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106853806.549187.294480@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<905hv0pb0n7da15us4uktn904ei705brg9@4ax.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com> <905hv0pb0n7da15us4uktn904ei705brg9@4ax.com>`

```
>> First displaying pointers, now dynamic memory allocation!

> Do you think OO Cobol is the spawn of the devil?

OO does not involve explicit programming for "displaying pointers, now
dynamic memory allocation!"
```

###### ↳ ↳ ↳ Re: Allocating memory dynamically in cobol...

- **From:** "XPPROGRAMMER" <saud_abraham@hotmail.com>
- **Date:** 2005-01-27T14:55:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106866500.619774.259780@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<905hv0pb0n7da15us4uktn904ei705brg9@4ax.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com> <905hv0pb0n7da15us4uktn904ei705brg9@4ax.com>`

```
No.  I think OO cobol is interesting. However, it does not have enough
Classes
for support as C++ language does.

John.
```

###### ↳ ↳ ↳ Re: Allocating memory dynamically in cobol...

_(reply depth: 4)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2005-01-27T18:40:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CZeKd.8863$Yg6.1306517@news20.bellglobal.com>`
- **In-Reply-To:** `<1106866500.619774.259780@f14g2000cwb.googlegroups.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com> <905hv0pb0n7da15us4uktn904ei705brg9@4ax.com> <1106866500.619774.259780@f14g2000cwb.googlegroups.com>`

```
XPPROGRAMMER wrote:
> No.  I think OO cobol is interesting. However, it does not have enough
> Classes
…[3 more quoted lines elided]…
> 

Classes of objects do nat have to be language-centric.

Donald
```

###### ↳ ↳ ↳ Re: Allocating memory dynamically in cobol...

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-01-28T00:20:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zzfKd.251137$f47.50011@news.easynews.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com> <905hv0pb0n7da15us4uktn904ei705brg9@4ax.com> <1106866500.619774.259780@f14g2000cwb.googlegroups.com>`

```
Which OO COBOL product are you using?  Is there any reason that you can't use 
existing C++ Classes with it?  (Some compilers make this easier than others). 
In that way, you can "gradually" migrate specific classes and/or applications 
from C++ to OO COBOL.

Unless something medium-odd is happening, you should NOT need to do dynamic 
storage allocations or displaying of pointers - to migrate existing applications 
to OO COBOL.  If you think of the "function" (not in the C - sense of that word 
<G>) that you want to accomplish, there may be (probably WILL be) either native 
COBOL facilities to do what you want without explicit storage manipulation - or 
there may be OO COBOL routines available to you.

Can you give any specific examples of WHY you think you need to have explicit 
dynamic storage allocation?  If you tell us the compiler, we may be able to 
provide you with a more "COBOL-like" solution than a literal translation of the 
C++ code.
```

###### ↳ ↳ ↳ Re: Allocating memory dynamically in cobol...

_(reply depth: 5)_

- **From:** "XPPROGRAMMER" <saud_abraham@hotmail.com>
- **Date:** 2005-01-27T19:42:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106883763.060268.82690@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<zzfKd.251137$f47.50011@news.easynews.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com> <905hv0pb0n7da15us4uktn904ei705brg9@4ax.com> <1106866500.619774.259780@f14g2000cwb.googlegroups.com> <zzfKd.251137$f47.50011@news.easynews.com>`

```
I am using micro focus Net Express cobol compiler --- when using C++
classes such
as win32_PRINTER or win32_CPU (which is WMI classes),  there is a lot
of overhead
and idiosynrasy when it comes to performance, compilation and the
generated native
code.  In C programming, it is more standard to allocate dynamic memory
during a call
to win32 API function,  especially if you are concerned about
performance.  Also,  when
a call should receive or return an array into memory, there is a need
to probe the array's
content by simply de-referencing the pointers, which I just learned to
do using the cobol
linkage section. Frankly, I am more concerned about dealing with or
rather opening large
files in OO cobol (indexed files with size of 8 gigabyte) than
allocating and de-allocating
dynamic memory --- I have heard that large indexed files tends to get
corrupted more
frequently than usual, but I donot know if thats true or not for Net
Express.
thanks for the feedback and the help.  Regards.

John.
```

###### ↳ ↳ ↳ Re: Allocating memory dynamically in cobol...

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-01-28T04:35:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1ijKd.274537$f47.54328@news.easynews.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com> <905hv0pb0n7da15us4uktn904ei705brg9@4ax.com> <1106866500.619774.259780@f14g2000cwb.googlegroups.com> <zzfKd.251137$f47.50011@news.easynews.com> <1106883763.060268.82690@c13g2000cwb.googlegroups.com>`

```
For win32_PRINTER, I would look and see if the PC_PRINTER routines available 
from Micro Focus wouldn't do what you want.  (Check your online help for more 
information about what they can do)

There may also be "built in" features for win32_CPU - but not (personally know 
what it is - or what MF would do with it, I don't know).

As far as "large files" go, I assume you know about "IDXFORMAT(8)".  However, 
even with it, I wonder if have an 8G indexed file is REALLY what you want (as 
opposed to - say for example - a SQL database).

P.S.  As someone who is NOT a current Net Express user, anything I say may be 
wrong, out-of-date, or misleading.  I assume that Jimmy or someone else has 
already suggested that you check out the MF forum.
```

###### ↳ ↳ ↳ Re: Allocating memory dynamically in cobol...

_(reply depth: 6)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-28T06:42:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iomjv05sle0sinqkofdgvc4sonib3vlvk0@4ax.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com> <905hv0pb0n7da15us4uktn904ei705brg9@4ax.com> <1106866500.619774.259780@f14g2000cwb.googlegroups.com> <zzfKd.251137$f47.50011@news.easynews.com> <1106883763.060268.82690@c13g2000cwb.googlegroups.com>`

```
On 27 Jan 2005 19:42:43 -0800, "XPPROGRAMMER"
<saud_abraham@hotmail.com> wrote:

> Frankly, I am more concerned about dealing with or rather opening large
>files in OO cobol (indexed files with size of 8 gigabyte) than allocating and de-allocating
>dynamic memory --- I have heard that large indexed files tends to get
>corrupted more frequently than usual, but I donot know if thats true or not for Net
>Express.

Here's what I would do/have done:

.. Write an I/O module per file. Run each as a separate process.
.. When applications want to do I/O, have them communicate with the
I/O modules through shared memory. See Win API functions
CreateFileMapping(), OpenFileMapping(), and MapViewOfFile().
You'll also need to lock the message area using homemade semiphores,
which can be in the same chunk of memory.
.. Don't lock records. Read a record, update it in the application's
memory, when you're ready to update the file, read it again (in the
I/O module)  and check to make sure it hasn't changed, using a version
number. While the update is in progress, the file server will be
locked by the fact that it's not looking for an input message and the
message area remains locked.

Corruption occurs because multiple programs have the same file open.
This approach avoids that condition. Only one process has the file
open.
```

###### ↳ ↳ ↳ Re: Allocating memory dynamically in cobol...

_(reply depth: 7)_

- **From:** "XPPROGRAMMER" <saud_abraham@hotmail.com>
- **Date:** 2005-01-28T09:37:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106933827.379260.251020@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<iomjv05sle0sinqkofdgvc4sonib3vlvk0@4ax.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com> <905hv0pb0n7da15us4uktn904ei705brg9@4ax.com> <1106866500.619774.259780@f14g2000cwb.googlegroups.com> <zzfKd.251137$f47.50011@news.easynews.com> <1106883763.060268.82690@c13g2000cwb.googlegroups.com> <iomjv05sle0sinqkofdgvc4sonib3vlvk0@4ax.com>`

```
excellent feedback robert.  Thanks.

John.
```

###### ↳ ↳ ↳ Re: Allocating memory dynamically in cobol...

_(reply depth: 6)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-01-28T07:23:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OLlKd.194839$6l.83016@pd7tw2no>`
- **In-Reply-To:** `<1106883763.060268.82690@c13g2000cwb.googlegroups.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com> <905hv0pb0n7da15us4uktn904ei705brg9@4ax.com> <1106866500.619774.259780@f14g2000cwb.googlegroups.com> <zzfKd.251137$f47.50011@news.easynews.com> <1106883763.060268.82690@c13g2000cwb.googlegroups.com>`

```
XPPROGRAMMER wrote:
> I am using micro focus Net Express cobol compiler --- when using C++
> classes such
…[23 more quoted lines elided]…
> 
1. Let's take one of Bill's points - here's the link to join M/F Answer 
Exchange :-

http://www.cobolportal.com/microfocusforum/menu.asp

2. Printing - I gather you were using C initially but have looked at C++ 
for its print features. You can look at other packages for printing, 
Flexus, RPV, Crystal etc., or if your printing is fairly basic, (i.e. no 
graphing), then as Bill suggested, you could take a look at PC_PRINT - 
there are quite a number of PC_PRINT examples on the M/F site. Just for 
info - rather than CALL individual PC_PRINT routines, for those I use, I 
have them in an OO Class PcPrint, creating an instance for each report 
and then invoke specific methods which make the PC_PRINT CALLs. I 
haven't done it yet, but as each report invariably has a standard header 
block, I will be looking at passing the header info as an 
OrderedCollection to PcPrint Class to be re-used by invoking the method 
'PrintHeader'.

3 (a). File Handling - Bill has already mentioned the IDXFORMAT syntax - 
it's one that comes up from time to time in the N/E WebBoard. Use Answer 
Exchange to query any problems with volumes. (I have absolutely no 
expertise on large volume files). Presumably you will be using something 
like Fileshare ?

3 (b) File Handling using OO - no problem. If interested, I can even 
supply you OO file handling templates, which you can adapt, (ISAM, ISAM 
with one Alternate Key, Sequential, Line Sequential and Relative). Five 
classes which will handle all file types. If you want to look at an all 
singin' all dancin' example in OO wrapped inside Rational Rose, take a 
look at Gene Webb's :-

http://objectz.com/oocobol/tutorial/samples/

  - for the Byte Stream File Class

3. Corruption of large files. Again not familiar, but seems to me it has 
to be covered by your backup procedures, which I would suggest should 
automatically trigger M/F REBUILD routines, if there is a lot of 
'Adding' or 'Deleting' on ISAMs. Look at the on-line help, you can call 
REBUILD directly from within your COBOL programs/classes. I just did 
this simple one on a test program :-

        01 ws-FileStatus            pic x(02).

        01 RebuildParameters        pic x(600) value
                       "CustomersFile.dat, Temp.dat /i /v".
        01 RebuildStatus            pic 9(04) comp-x.

	perform THE-REBUILD

        THE-REBUILD.

        call "CALLRB" using RebuildParameters, RebuildStatus
        end-call
        move Return-Code to n
        display n
        accept charx
        .
        *>-------------------------------------------------------------

4. Bill mentioned SQL as an option. The ESQL Assistant from the IDE is a 
"dream". Means of course you have to familiarize yourself with (R)DBMS, 
but you use the SQL tool to generate all your SQL statements, once you 
have determined your tables and registered the appropriate ODBC driver.
ESQL Assistant generates the necessary formats for COBOL files and the 
SQL statements.

HTH

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Allocating memory dynamically in cobol...

_(reply depth: 7)_

- **From:** "XPPROGRAMMER" <saud_abraham@hotmail.com>
- **Date:** 2005-01-28T08:46:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106930790.029427.207890@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<OLlKd.194839$6l.83016@pd7tw2no>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com> <905hv0pb0n7da15us4uktn904ei705brg9@4ax.com> <1106866500.619774.259780@f14g2000cwb.googlegroups.com> <zzfKd.251137$f47.50011@news.easynews.com> <1106883763.060268.82690@c13g2000cwb.googlegroups.com> <OLlKd.194839$6l.83016@pd7tw2no>`

```
Thanks for the valuable feedback. As for the Fileshare you should
know that its Passe to use it --- even micro focus tech staff have
been advising their clients not to use it, direct access thru the
Client/Server connection is more preferred nowadays.  Thanks.

John.
```

##### ↳ ↳ Re: Allocating memory dynamically in cobol...

- **From:** "XPPROGRAMMER" <saud_abraham@hotmail.com>
- **Date:** 2005-01-27T14:50:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106866207.731929.153850@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<10vgt3f908bo721@news.supernews.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com>`

```
I am converting C++ programs into Cobol code --- why, because cobol is
cool.
John.
```

###### ↳ ↳ ↳ Re: Allocating memory dynamically in cobol...

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-28T03:39:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<htcjv0hqqvh1con4vt5jifu8cnm2sjaqgn@4ax.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com> <1106866207.731929.153850@c13g2000cwb.googlegroups.com>`

```
On 27 Jan 2005 14:50:07 -0800, "XPPROGRAMMER"
<saud_abraham@hotmail.com> wrote:

>I am converting C++ programs into Cobol code --- why, because cobol is
>cool.

Real C++ or straight C? To OO Cobol or traditional? An account of
converting C++ to OO Cobol would be very interesting. Perhaps you
could post code for missing support classes.
```

###### ↳ ↳ ↳ Re: Allocating memory dynamically in cobol...

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-01-28T05:17:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3WjKd.2191$JO2.2@tornado.tampabay.rr.com>`
- **References:** `<1106761730.476849.173630@f14g2000cwb.googlegroups.com> <10vgt3f908bo721@news.supernews.com> <1106866207.731929.153850@c13g2000cwb.googlegroups.com>`

```
"XPPROGRAMMER" <saud_abraham@hotmail.com> wrote in message 
news:1106866207.731929.153850@c13g2000cwb.googlegroups.com...
>I am converting C++ programs into Cobol code --- why, because cobol is
> cool.
> John.

"ADD 1 TO C GIVING C" surely has to be cooler - it's more moderner after 
all....

I recently saw a COBOL program "translated" to Java.. it was mildly 
amusing....One instance with 300 instance variables all updated by one 
colossal method....oh, and of course a  main to run it....if you're lucky 
that's how your C++ classes are written...

JCE
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
