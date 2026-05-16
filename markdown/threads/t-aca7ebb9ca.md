[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help! Converting files from a Cobol app

_12 messages · 6 participants · 2004-10_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Help requests and how-to`](../topics.md#help)

---

### Help! Converting files from a Cobol app

- **From:** "Vilco" <a@b.c>
- **Date:** 2004-10-26T08:41:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C4ofd.1494$Es2.35217@twister2.libero.it>`

```
I'm new to this group, so... hello everybody!
I'm going to move data from an old application written in Cobol
my win32 application. To do this, I should export the data files
to plain text format. They're indexed files, the data files have
no extnsion and the index files have IDX extension. The
application is in Cobol because, if I try to run it in a wrong
path, I get the error "Cobol runtime not installed", and moreover
there is the COB directory & stuff.

My first difficulty is to determine the exact format of these
archives. I've found the EXTFH.EXE application, which I found to
be a kind of library used by cobol to access different kinds of
archives, but I can not figure out which is used in this
application. There is also a REBUILD.EXE utility which I found
confusing infos about: it should be a file maintenance utility of
some sort.

How can I determine the exact format of these files? And,
moreover, where can I find an utility to convert them into plain
ASCII format?

Thanks in advance
    Vilco
```

#### ↳ Re: Help! Converting files from a Cobol app

- **From:** "Vilco" <a@b.c>
- **Date:** 2004-10-26T09:14:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Uzofd.1414$Ni.42525@twister1.libero.it>`
- **References:** `<C4ofd.1494$Es2.35217@twister2.libero.it>`

```
BTW, I copy here the BAT which launches the Cobol application,
maybe this makes the file version easier to determine:

SET COBDIR=..\COB
SET TEMP=..\TEMP
SET EXTFHBUL=65535
SET IDXDATBUF=65535
SET COBSW=+M
CLS
..\COB\GESTMENU (-F-N+1+L+B+B1)
APP
PAUSE
CLS

It looks like this is a Microsoft - Micro Focus Cobol
application.
Here's what it says when I try to run the REBUILD utility:
Microsoft (R) COBOL file management utility version 5.0
COBOL software by Micro Focus
Copyright Microsoft ...
Copyright Micro Focus...

I hope this helps.
```

##### ↳ ↳ Re: Help! Converting files from a Cobol app

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-10-26T17:54:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bwfd.30558$nl.10946@pd7tw3no>`
- **In-Reply-To:** `<Uzofd.1414$Ni.42525@twister1.libero.it>`
- **References:** `<C4ofd.1494$Es2.35217@twister2.libero.it> <Uzofd.1414$Ni.42525@twister1.libero.it>`

```
Vilco wrote:

>BTW, I copy here the BAT which launches the Cobol application,
>maybe this makes the file version easier to determine:
…[22 more quoted lines elided]…
>
Your programs were compiled using Microsoft COBOL V 5.0 which is a 
re-badged Micro Focus  Version 3+ (the old DOS version)  -  formats  are 
identical. Your filename (no extension) is the data file and the 
filename.idx is an index containing your PrimeKeys and perhaps Alternate 
Keys.

Do you only have the compiled programs - in which case you are somewhat 
stuck. You need the SOURCE of the M/S programs that contain the file 
layouts. For example a record layout could be something like following :-

01 MyRecord.
 05 PrimeKey      pic x(06) or pic 9(06).
 05 Name            pic x(30).
 05 Value1           pic 9(03)v9(02) comp-3.
 05 Value2           pic s9(06) comp-3.   ------ signed value (minus if 
negative)

Without the format it is difficult to establish where fields start and 
finish and how numerics are stored, could be 'packed' as above or just 
plain 9(03)v9(02) and s9(06). (The 'v' is an implied decimal point).

Given you have the formats - then you need to write programs reading the 
above ISAM (Indexed Sequential Access Mode) files, sequentially.

01 MyTextRecord.
 05 T-PrimeKey      pic x(06) or pic 9(06).
 05 pic x value ",".
 05 T-Name            pic x(30).
 05 pic x value ",".
 05 T-Value1           pic 999.99.
 05 pic x value ",".
 05 T-Value2           pic -999999.   ------ signed value (minus if 
negative)
 05 pic x value ",".

Open input MyfileName
Open output MyTextFile
set fileNotFinis to true
perform until fileFinis
   read MyFilename next record
        at end set FileFinis to true
        not at end
            move PrimeKey to T-PrimeKey
            move Name to  T-Name          
            move Value1 to T-Value1        
            move Value2 to T-Value2        
            write MyTextRecord
    end-read

end-perform

Close MyfileName
Close MyTextFile

But you need those record formats and either a Microsoft or Micro Focus 
compiler to access the existing files.  (The alternative go googling as 
suggested in other messages, looking for support on this topic in this 
Newsgroup).

HTH

Jimmy, Calgary AB
```

#### ↳ Re: Help! Converting files from a Cobol app

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-10-26T14:44:00+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2vksn0t2irnddkaivrg807p9v472j7ggp9@4ax.com>`
- **References:** `<C4ofd.1494$Es2.35217@twister2.libero.it>`

```
On Tue, 26 Oct 2004 08:41:06 GMT, "Vilco" <a@b.c> wrote:

>I'm new to this group, so... hello everybody!
>I'm going to move data from an old application written in Cobol
…[17 more quoted lines elided]…
>ASCII format?

If you have the source of the Selectï¿½s and File Descriptions then you
can do/ask someone to do it for you, a small program that will extract
te information from the files and write this as a text file, with or
without field separators, and with all numeric fields converted to
usage display.

You can also search this group (www.deja.com) for similar threads and
see what has been said about this subject.
This has happend a lot, and there are links to some sites that sell
commercial products to help you do this if you donï¿½t have the sources
mentioned above.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: Help! Converting files from a Cobol app

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-26T14:50:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jnksn09fmqrpkq5bqjv5ubcs8ls4ohe265@4ax.com>`
- **References:** `<C4ofd.1494$Es2.35217@twister2.libero.it>`

```
On Tue, 26 Oct 2004 08:41:06 GMT, "Vilco" <a@b.c> wrote:

>I'm new to this group, so... hello everybody!
>I'm going to move data from an old application written in Cobol
…[4 more quoted lines elided]…
>ASCII format?

Look for dfed (data file editor) and dfconv (data file converter).
Also look for source code and copybooks, which will have extension
cob, cbl or cpy.

If there are no packed or binary fields, conversion is a snap. If
there are, you'll have to expand those fields to display-format. 

If you have copybooks, I posted a program that will use them to
convert the files to comma-delimited.
```

##### ↳ ↳ Re: Help! Converting files from a Cobol app

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-10-26T16:58:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9JawBIjeflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<C4ofd.1494$Es2.35217@twister2.libero.it> <jnksn09fmqrpkq5bqjv5ubcs8ls4ohe265@4ax.com>`

```
.    On  26.10.04
  wrote  robert@wagner.net.yourmammaharvests (Robert Wagner)
     on  /COMP/LANG/COBOL
     in  jnksn09fmqrpkq5bqjv5ubcs8ls4ohe265@4ax.com
  about  Re: Help! Converting files from a Cobol app


RW> If you have copybooks, I posted a program that will use them to
RW> convert the files to comma-delimited.

   I posted another one.

   As to the original question -- I am just curious if the person or  
organization which produced that application is no longer around, does  
offer or not an upgrade of that application to current Windows  
technologies, can provide data conversion services ... or are you  
dissatisfied with that application that you do no longer want to rely  
on its original author?


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Nach einem dreiï¿½igjï¿½hrigen Krieg mit sich selbst kam es endlich zu einem Vergleich, aber die Zeit war verloren. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Help! Converting files from a Cobol app

- **From:** "Vilco" <t@h.c>
- **Date:** 2004-10-26T21:40:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Avzfd.90311$b5.4361003@news3.tin.it>`
- **References:** `<C4ofd.1494$Es2.35217@twister2.libero.it> <jnksn09fmqrpkq5bqjv5ubcs8ls4ohe265@4ax.com> <9JawBIjeflB@jpberlin-l.willms.jpberlin.de>`

```
Lueko Willms wrote:
>   about  Re: Help! Converting files from a Cobol app

>> If you have copybooks, I posted a program that will use them to
>> convert the files to comma-delimited.

>    I posted another one.
>    As to the original question -- I am just curious if the person or
…[4 more quoted lines elided]…
> on its original author?

First of all, thanks to all :)
Then, to answer to Lueko's question, this cobol ERP software is still in use at the customer's site: he wants a new software because
the original producer does no more produce updates for that software, which will be absolete in less then six months due to incoming
changes in the taxation laws.
To come back to the matter, from what R.Wagner posted I understand that if I have these Cobol clipbooks or source files I can use
some free utilities to extract the files? OK, tomorrow at work I will check for these files. I remember having seen many .cob files
around.
I also have seen that the data files (no extension) contain compressed numeric values. The data are enough easy to understand since
the numeric fields are very few, many fields are text and so are easy to recognize (name, surname, address...) so I can clearly see
the "persons" file starting with the numeric ID (compressed, rectangular character or special characters like Danish "D", germaun
umlauts etc in text viewer) and going on with surname, name, etc. The character fields, like the surname and name of the persons,
are not full-plain text: every some six-to-ten characters there is one inconsistent character, like a german umlaut in the half of
an otherwise plain italian surname (like "ferra�i" instead of "ferrari").
I have seen many other file formats akin to this one, like those used in an acucobol application I converted data from in the past,
but even with compressed numeric fields the text fields always showed up correctly, with no corruption like the one I see in these
files.
Any clues?
Thanks again, will show up tomorrow morning
From GMT+1 time-zone
```

###### ↳ ↳ ↳ Re: Help! Converting files from a Cobol app

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-10-26T22:37:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ukAfd.38596$Pl.22357@pd7tw1no>`
- **In-Reply-To:** `<Avzfd.90311$b5.4361003@news3.tin.it>`
- **References:** `<C4ofd.1494$Es2.35217@twister2.libero.it> <jnksn09fmqrpkq5bqjv5ubcs8ls4ohe265@4ax.com> <9JawBIjeflB@jpberlin-l.willms.jpberlin.de> <Avzfd.90311$b5.4361003@news3.tin.it>`

```
Vilco wrote:

>Lueko Willms wrote:
>  
…[44 more quoted lines elided]…
>

If you haven't got MS or MF manuals - use the following link to the 
current Net Express V 4 on-line books :-

http://supportline.microfocus.com/supportline/documentation/books/nx40/nx40indx.htm

Not necessarily so, but those packed numeric values are in all 
likelihood specified as variations of the format of comp-3.  Have a look 
at the Language Reference Manual for comp-3 - 2.6.4.4. and 8.26.

I'm not sure, but from what you have written with regard to the text 
fields - it's possible that the originator designed the files with data 
compression. Again,  look at the book on File Handling, Section 6.3.

Without question, if you can get copies of the file format sources from 
the original developer - that's far the easiest route to go. For a few 
bucks they might even be prepared to write you the programs putting out 
the data as comma delimited text files. So the 'few bucks' might be 
$200-500 - still probably cheaper than your time figuring it out.

Jimmy
```

###### ↳ ↳ ↳ Re: Help! Converting files from a Cobol app

_(reply depth: 4)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-10-27T03:16:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tn4un0lsqubqb7p3ddvma93rvks9c4ilml@4ax.com>`
- **References:** `<C4ofd.1494$Es2.35217@twister2.libero.it> <jnksn09fmqrpkq5bqjv5ubcs8ls4ohe265@4ax.com> <9JawBIjeflB@jpberlin-l.willms.jpberlin.de> <Avzfd.90311$b5.4361003@news3.tin.it>`

```
On Tue, 26 Oct 2004 21:40:48 GMT, "Vilco" <t@h.c> wrote:

>The character fields, like the surname and name of the persons,
>are not full-plain text: every some six-to-ten characters there is one inconsistent character, like a german umlaut in the half of
>an otherwise plain italian surname (like "ferraï¿½i" instead of "ferrari").

The file system was extfh and DATACOMPRESS was turned on. It uses two
similar RLL algorithms, which compress strings of repeating
characters. One has two bytes, the first being binary 2-31 and the
second, the character. The other has three bytes, the first being DC4
(ASCII 20, the character shown above), the second is binary 2-255 and
the third, the character. If you read the file via extfh, you don't
need to worry about expansion.
```

###### ↳ ↳ ↳ Re: Help! Converting files from a Cobol app

_(reply depth: 5)_

- **From:** "Vilco" <a@b.c>
- **Date:** 2004-10-27T13:10:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D7Nfd.3470$Ni.102658@twister1.libero.it>`
- **References:** `<C4ofd.1494$Es2.35217@twister2.libero.it> <jnksn09fmqrpkq5bqjv5ubcs8ls4ohe265@4ax.com> <9JawBIjeflB@jpberlin-l.willms.jpberlin.de> <Avzfd.90311$b5.4361003@news3.tin.it> <tn4un0lsqubqb7p3ddvma93rvks9c4ilml@4ax.com>`

```
Robert Wagner wrote:

> The file system was extfh and DATACOMPRESS was turned on.
> It uses two similar RLL algorithms, which compress
…[5 more quoted lines elided]…
> extfh, you don't need to worry about expansion.

I looked around the web and I found tons of pages talking
about EXTFH.CFG, but this file is not present in the app's
folders. Is this a problem?
Moreover, is this ExtFH.EXE callable only from Cobol apps?
Because I have never used Cobol and I do not have any cobol
related tool.

Regarding your previous post, where you wrote:

> Look for dfed (data file editor) and dfconv (data file
> converter). Also look for source code and copybooks,
…[5 more quoted lines elided]…
> them to convert the files to comma-delimited

I checked the app's folders and found:
- no dfed / dfconv files
- cpy files: none
- cbl files: just one (and 2 empty, as well). One seems to
  reorganize data in one table (the main archive) and also
  specifies the fields type and length of that archive.
  But there are many archives in the app, not just that one.
- cob files: 6 under the COB folder, 1 under the FILES folder,
  where the data files are stored. They look to be compiled,
  and contain many non alphanumeric characters along with
  many user-interface strings (like the user defined error
  messages).

So, how can I read these data files to convert them to plain
text?
Ah, last but not least: if it was still unclear for someone,
I'm a total newbie in cobol & stuff :(
```

###### ↳ ↳ ↳ DONE ! Thanks everybody :)

_(reply depth: 6)_

- **From:** "Vilco" <a@b.c>
- **Date:** 2004-10-27T14:21:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T9Ofd.3591$Ni.104917@twister1.libero.it>`
- **References:** `<C4ofd.1494$Es2.35217@twister2.libero.it> <jnksn09fmqrpkq5bqjv5ubcs8ls4ohe265@4ax.com> <9JawBIjeflB@jpberlin-l.willms.jpberlin.de> <Avzfd.90311$b5.4361003@news3.tin.it> <tn4un0lsqubqb7p3ddvma93rvks9c4ilml@4ax.com> <D7Nfd.3470$Ni.102658@twister1.libero.it>`

```
Messing around with the REBUILD utility, I found out how to
convert the files in C-ISAM plain text format:
REBUILD.EXE ARCHIVENAME. , NEWARCHIVENAME.TXT /s:MF /t:C-ISAM
Compression resolved both on numeric and thext values.

Thanks very much to all who helped :)
```

###### ↳ ↳ ↳ Re: Help! Converting files from a Cobol app

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-10-27T13:54:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0410271254.7a22cbf8@posting.google.com>`
- **References:** `<C4ofd.1494$Es2.35217@twister2.libero.it> <jnksn09fmqrpkq5bqjv5ubcs8ls4ohe265@4ax.com> <9JawBIjeflB@jpberlin-l.willms.jpberlin.de> <Avzfd.90311$b5.4361003@news3.tin.it> <tn4un0lsqubqb7p3ddvma93rvks9c4ilml@4ax.com> <D7Nfd.3470$Ni.102658@twister1.libero.it>`

```
"Vilco" <a@b.c> wrote 

> RW> If you read the file via
> RW> extfh, you don't need to worry about expansion.
 
> I looked around the web and I found tons of pages talking
> about EXTFH.CFG, but this file is not present in the app's
> folders. Is this a problem?

No.

> Moreover, is this ExtFH.EXE callable only from Cobol apps?
> Because I have never used Cobol and I do not have any cobol
> related tool.

The MF/MS Cobol development system includes EXTFH.OBJ which can be
linked into a C program and used to access the data files. 
Documentation to do this, and a license allowing this to be done, is
supplied with the product.

Microsoft Cobol 5 is a rebadged version of MicroFocus Cobol 3.0 (not
Server Express 3.0).  If you can find docs for EXTFH for MF Cobol 2.5
- 3.4 then you can see how to use it in C.

> RW> Look for dfed (data file editor) and dfconv (data file
> RW> converter). 

> I checked the app's folders and found:
> - no dfed / dfconv files

No you won't have RW was talking about something completely different.
 In any case, even if those existed in MS Cobol 5 they may not have
been issued with the application.

> RW> If you have copybooks, I posted a program that will use
> RW> them to convert the files to comma-delimited

Robert, that was completely useless to someone without the compiler.

> So, how can I read these data files to convert them to plain
> text?

It seems that you have managed to coerse the REBUILD to convert to
uncompressed. The hard bit now is to identify what the numbers mean
which you will have to do by inference.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
