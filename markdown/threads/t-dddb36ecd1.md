[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reading Flat File in COBOL

_11 messages · 8 participants · 2005-11_

---

### Reading Flat File in COBOL

- **From:** dibalok@gmail.com
- **Date:** 2005-11-05T01:02:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1131181358.023584.17900@o13g2000cwo.googlegroups.com>`

```
Hi,
I have a program which writes to a flat file. Can i access the same
flat file in my program to fetch data.
Suppose, i need to write 100 records and after writing  50 records, i
need to retrive some data from that file and then write the rest 50
records. Is it possible in COBOL ?

Regards,
Dib
```

#### ↳ Re: Reading Flat File in COBOL

- **From:** docdwarf@panix.com ()
- **Date:** 2005-11-05T10:31:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dki1l7$n5o$1@reader2.panix.com>`
- **References:** `<1131181358.023584.17900@o13g2000cwo.googlegroups.com>`

```
In article <1131181358.023584.17900@o13g2000cwo.googlegroups.com>,
 <dibalok@gmail.com> wrote:
>Hi,
>I have a program which writes to a flat file. Can i access the same
>flat file in my program to fetch data.

That depends on what is in the file.

>Suppose, i need to write 100 records and after writing  50 records, i
>need to retrive some data from that file and then write the rest 50
>records. Is it possible in COBOL ?

Maybe.  Why don't you post what you've tried to make this work?

DD
```

#### ↳ Re: Reading Flat File in COBOL

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-11-05T08:26:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11mpdq9el7mv89b@corp.supernews.com>`
- **References:** `<1131181358.023584.17900@o13g2000cwo.googlegroups.com>`

```

<dibalok@gmail.com> wrote in message
news:1131181358.023584.17900@o13g2000cwo.googlegroups.com...
> Hi,
> I have a program which writes to a flat file. Can i access the same
…[3 more quoted lines elided]…
> records. Is it possible in COBOL ?

Possible? Yes.

Probable? Depends.

Probably yes, if the file is on mass storage media.

Probably no, if the file is on sequential storage media.

Definitely, depends on using the right storage medium,
clauses, statements etc., and these depend on hardware,
OS, compiler, etc.
```

#### ↳ Re: Reading Flat File in COBOL

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2005-11-06T07:40:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8sibf.46588$zb5.24120@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<1131181358.023584.17900@o13g2000cwo.googlegroups.com>`
- **References:** `<1131181358.023584.17900@o13g2000cwo.googlegroups.com>`

```


dibalok@gmail.com wrote:
> Hi,
> I have a program which writes to a flat file. Can i access the same
…[7 more quoted lines elided]…
> 

OPEN OUTPUT FLAT-FILE
WRITE FLAT-FILE-RECORD (as often as necessary)
CLOSE FLAT-FILE
OPEN INPUT FLAT-FILE
READ FLAT-FILE-RECORD (as often as necessary)
CLOSE FLAT-FILE
OPEN EXTEND FLAT-FILE
WRITE FLAT-FILE-RECORD (as often as necessary)
CLOSE FLAT-FILE

The OPEN EXTEND option should be available in 85 COBOL.  It opens an 
existing file for output.  New records will be appended to the 
existing file.

I hope that helps.
```

##### ↳ ↳ Re: Reading Flat File in COBOL

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-11-06T05:39:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DVlbf.31401$NJ.22983@bignews7.bellsouth.net>`
- **References:** `<1131181358.023584.17900@o13g2000cwo.googlegroups.com> <8sibf.46588$zb5.24120@bgtnsc04-news.ops.worldnet.att.net>`

```
"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote:
> dibalok@gmail.com wrote:
>> I have a program which writes to a flat file. Can i access the same
…[17 more quoted lines elided]…
> file.


I don't know if this will help you, but a method I have used with success in 
processing batch balanced transaction files is to open the input file using 
two FD's. You can use the first FD to read through a batch and see if that 
batch is in balance. Then read through the batch again using the second FD, 
writing the transactions for update or to an error report as applicable. 
However, in your case it is uncertain whether a second FD would be able to 
read past a prior EOF point before the file was closed by the first FD. You 
could try it and see. It is (almost ?) certain that you will have to open 
the output file first, close it, then reopen it with APPEND before opening 
the file with the second FD.
```

#### ↳ Re: Reading Flat File in COBOL

- **From:** Paul Knudsen <bigkahuna@jupada.com>
- **Date:** 2005-11-15T00:31:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m57jn1d11hkbp3pueuu2f0o18adlvsmbg1@4ax.com>`
- **References:** `<1131181358.023584.17900@o13g2000cwo.googlegroups.com>`

```
On 5 Nov 2005 01:02:38 -0800, dibalok@gmail.com wrote:

>Hi,
>I have a program which writes to a flat file. Can i access the same
…[6 more quoted lines elided]…
>Dib
As you've been told, it probably can be done.  But is it a good idea?
Why not store the data in a table?
```

##### ↳ ↳ Re: Reading Flat File in COBOL

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-11-15T13:03:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b0lef.123$IC3.48@newssvr33.news.prodigy.com>`
- **References:** `<1131181358.023584.17900@o13g2000cwo.googlegroups.com> <m57jn1d11hkbp3pueuu2f0o18adlvsmbg1@4ax.com>`

```
"Paul Knudsen" <bigkahuna@jupada.com> wrote in message
news:m57jn1d11hkbp3pueuu2f0o18adlvsmbg1@4ax.com...
> On 5 Nov 2005 01:02:38 -0800, dibalok@gmail.com wrote:
>
…[8 more quoted lines elided]…
> Why not store the data in a table?

On "extremely remote off-chance" that '100 records' and '50 records' are
exemplary only and not actual values..

A) table size must be known at compile time
B) tables must fit in memory

MCM
```

###### ↳ ↳ ↳ Re: Reading Flat File in COBOL

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-11-15T18:07:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ztpef.505456$oW2.74077@pd7tw1no>`
- **In-Reply-To:** `<b0lef.123$IC3.48@newssvr33.news.prodigy.com>`
- **References:** `<1131181358.023584.17900@o13g2000cwo.googlegroups.com> <m57jn1d11hkbp3pueuu2f0o18adlvsmbg1@4ax.com> <b0lef.123$IC3.48@newssvr33.news.prodigy.com>`

```
Michael Mattias wrote:
> "Paul Knudsen" <bigkahuna@jupada.com> wrote in message
> news:m57jn1d11hkbp3pueuu2f0o18adlvsmbg1@4ax.com...
…[22 more quoted lines elided]…
> MCM

Just as an aside, one gentleman, well versed in OO and lists 
(collections), almost in a fit of pique, I would suggest, because of the 
way the topic was going, wrote to J4 to the effect, "We probably should 
ignore collections and just write them to files". Well in OO terminology 
that approach would give you something closely following the concept of 
'persistent objects'.

I hope he was only kidding :-)

Still back to Compuserve days, recall you writing, as a result of a 
query from me, Relative files could be used as temporary tables.

Jimmy
```

###### ↳ ↳ ↳ Re: Reading Flat File in COBOL

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-11-15T20:13:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6kref.134$nA2.65@newssvr22.news.prodigy.net>`
- **References:** `<1131181358.023584.17900@o13g2000cwo.googlegroups.com> <m57jn1d11hkbp3pueuu2f0o18adlvsmbg1@4ax.com> <b0lef.123$IC3.48@newssvr33.news.prodigy.com> <ztpef.505456$oW2.74077@pd7tw1no>`

```
"James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
news:ztpef.505456$oW2.74077@pd7tw1no...
> Michael Mattias wrote:
> > On "extremely remote off-chance" that '100 records' and '50 records' are
…[6 more quoted lines elided]…
> query from me, Relative files could be used as temporary tables.


That would make you.... an old fart?

MCM
```

###### ↳ ↳ ↳ Re: Reading Flat File in COBOL

_(reply depth: 5)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-11-15T21:08:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B7sef.515742$tl2.78030@pd7tw3no>`
- **In-Reply-To:** `<6kref.134$nA2.65@newssvr22.news.prodigy.net>`
- **References:** `<1131181358.023584.17900@o13g2000cwo.googlegroups.com> <m57jn1d11hkbp3pueuu2f0o18adlvsmbg1@4ax.com> <b0lef.123$IC3.48@newssvr33.news.prodigy.com> <ztpef.505456$oW2.74077@pd7tw1no> <6kref.134$nA2.65@newssvr22.news.prodigy.net>`

```
Michael Mattias wrote:
> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
> news:ztpef.505456$oW2.74077@pd7tw1no...
…[18 more quoted lines elided]…
> 
Thou art truly wise. How did you know I had just gone to my doctor who 
told me to use a product called Beano, (which triggered the thought 
'baked beans'), to overcome the acute embarrassment of flatulation.

Jimmy
```

###### ↳ ↳ ↳ Re: Reading Flat File in COBOL

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-11-16T06:23:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dlej9t$ddr$1@reader2.panix.com>`
- **References:** `<1131181358.023584.17900@o13g2000cwo.googlegroups.com> <ztpef.505456$oW2.74077@pd7tw1no> <6kref.134$nA2.65@newssvr22.news.prodigy.net> <B7sef.515742$tl2.78030@pd7tw3no>`

```
In article <B7sef.515742$tl2.78030@pd7tw3no>,
James J. Gavan <jgavandeletethis@shaw.ca> wrote:
>Michael Mattias wrote:
>> "James J. Gavan" <jgavandeletethis@shaw.ca> wrote in message
>> news:ztpef.505456$oW2.74077@pd7tw1no...

[snip]

>>>Still back to Compuserve days, recall you writing, as a result of a
>>>query from me, Relative files could be used as temporary tables.
…[7 more quoted lines elided]…
>'baked beans'), to overcome the acute embarrassment of flatulation.

Hmmmm... back in those days I used a service called American PeopleLink, 
or PLink, because it was less expensive even with WATS Telenet fees added 
on... but also, more importantly, back in those days I spent some time in 
Kansas City, Missouri, where I encountered the most wonderful baked beans 
I have ever had in my life, bar *none*, from the Smokestack Barbecue (also 
known as Fiorello's Jack Stack) at 135th & Holmes.

I have just been informed that they have a Web presence, with home-page to 
be found at http://www.jackstackbbq.com/default.asp ... and thanks to the 
miracles of such things as Beano and Pepcid Complete (a stunningly 
effective blend of calcium carbonate, magnesium hydroxide and famotidine) 
I've felt encouraged to place an order to see if I *can* 'go home again' 
and Wolfe some of this stuff down.

I'm awating the arrival of the 'Duet' package 
(http://www.jackstackbbq.com/product.asp?pn=PKDU2050), the version with 
two half-slabs of sauced ribs... ordered an extra pint of beans, while I 
was at it... and I'll see how it goes, I have *extraordinarily* fond 
memories of their hickory-smoked lamb ribs 
(http://www.jackstackbbq.com/product.asp?pn=PKLR2074) and I'm not sure how 
I'm going to be able to resist what is described as 'Kobe Beef Burnt 
Ends'... I mean, I know it is American Kobe, from Waygu cattle raised 
Stateside... but burnt ends prepared from that delicate a meat?  The mind 
boggles, the salivary glands go into overdrive.

(Note - I do not gain any financial benefit from anyone's purchases of 
Fiorello's Jack Stack products, Pepcid Complete or Beano... and from folks 
using the latter two my gains are strictly 'atmospheric').

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
