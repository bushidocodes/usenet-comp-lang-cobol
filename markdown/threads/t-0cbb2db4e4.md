[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# WDz - COBOL access local files

_10 messages · 5 participants · 2006-07 → 2006-08_

---

### WDz - COBOL access local files

- **From:** "dkk" <taxpress@gmail.com>
- **Date:** 2006-07-28T12:17:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1154114264.018898.228770@i3g2000cwc.googlegroups.com>`

```
New to WDz.
Can I debug/run a COBOL program which has file access statement
(open/read/write/close) in WDz to access local files? (offline)
```

#### ↳ Re: WDz - COBOL access local files

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-28T19:34:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HEtyg.422256$SQ6.234926@fe09.news.easynews.com>`
- **References:** `<1154114264.018898.228770@i3g2000cwc.googlegroups.com>`

```
Yes, you can.  Check out the chapter:

 "Chapter 8. Processing files "

in the WDz COBOL Programming Guide.  If you still have problems, let us know 
exactly what they are.
```

##### ↳ ↳ Re: WDz - COBOL access local files

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-07-29T06:57:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sFDyg.188359$mF2.87903@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<HEtyg.422256$SQ6.234926@fe09.news.easynews.com>`
- **References:** `<1154114264.018898.228770@i3g2000cwc.googlegroups.com> <HEtyg.422256$SQ6.234926@fe09.news.easynews.com>`

```


William M. Klein wrote:
> Yes, you can.  Check out the chapter:
> 
…[4 more quoted lines elided]…
> 

I was mystified by this.  Google shows me that WDz likely means 
"Websphere Developer for z-Series" (the current IBM Mainframe).

Lots of new acronyms to learn, but basically it means building web 
widgets that talk to mainframe CICS COBOL.
```

###### ↳ ↳ ↳ Re: WDz - COBOL access local files

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-29T07:16:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pXDyg.150886$tQ4.2283@fe01.news.easynews.com>`
- **References:** `<1154114264.018898.228770@i3g2000cwc.googlegroups.com> <HEtyg.422256$SQ6.234926@fe09.news.easynews.com> <sFDyg.188359$mF2.87903@bgtnsc04-news.ops.worldnet.att.net>`

```
WDz  is the follow-on product to "WSED" (Websphere Studio Enterprise Edition) 
and is the "PC" debugger for PC *and* z/OS applications (PL/I, CICS, DB2, IMS, 
HLASM *and* COBOL - of course.)  The current documentation is pretty weak on the 
"developing for the PC" stuff, but the product DOES support it.

The home page (if you are interested) is at:

 http://www-306.ibm.com/software/awdtools/devzseries/

Don't look for the COBOL (for Windows) LRM and PG, there, but they are available 
at:

  http://www-306.ibm.com/software/awdtools/cobol/library/

NOTE WELL:
  IBM no longer sells "separate" PL/I and COBOL compilers for Windows; you need 
to buy the "whole thing" to get either.
```

###### ↳ ↳ ↳ Re: WDz - COBOL access local files

_(reply depth: 4)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-07-31T10:00:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4j6no8F6iuh2U1@individual.net>`
- **References:** `<1154114264.018898.228770@i3g2000cwc.googlegroups.com> <HEtyg.422256$SQ6.234926@fe09.news.easynews.com> <sFDyg.188359$mF2.87903@bgtnsc04-news.ops.worldnet.att.net> <pXDyg.150886$tQ4.2283@fe01.news.easynews.com>`

```
I assume that WDz has no use in a VSE environment, but I'm not sure exactly
where to look to confirm or deny this.  Do you know where I could find this
information?  I'm thinking of submitting a requirement to IBM for VSE
support.  (Good luck; I know.)

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> William M. Klein<wmklein@nospam.netcom.com> 07/29/06 1:16 AM >>>
WDz  is the follow-on product to "WSED" (Websphere Studio Enterprise
Edition) 
and is the "PC" debugger for PC *and* z/OS applications (PL/I, CICS, DB2,
IMS, 
HLASM *and* COBOL - of course.)  The current documentation is pretty weak on
the 
"developing for the PC" stuff, but the product DOES support it.

The home page (if you are interested) is at:

 http://www-306.ibm.com/software/awdtools/devzseries/ 

Don't look for the COBOL (for Windows) LRM and PG, there, but they are
available 
at:

  http://www-306.ibm.com/software/awdtools/cobol/library/ 

NOTE WELL:
  IBM no longer sells "separate" PL/I and COBOL compilers for Windows; you
need 
to buy the "whole thing" to get either.
```

###### ↳ ↳ ↳ Re: WDz - COBOL access local files

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-07-31T22:16:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Hivzg.288183$Mn5.219870@pd7tw3no>`
- **In-Reply-To:** `<pXDyg.150886$tQ4.2283@fe01.news.easynews.com>`
- **References:** `<1154114264.018898.228770@i3g2000cwc.googlegroups.com> <HEtyg.422256$SQ6.234926@fe09.news.easynews.com> <sFDyg.188359$mF2.87903@bgtnsc04-news.ops.worldnet.att.net> <pXDyg.150886$tQ4.2283@fe01.news.easynews.com>`

```
William M. Klein wrote:
> WDz  is the follow-on product to "WSED" (Websphere Studio Enterprise Edition) 
> and is the "PC" debugger for PC *and* z/OS applications (PL/I, CICS, DB2, IMS, 
…[15 more quoted lines elided]…
> 
Bill,

Just out of curiosity I went looking at the LRM which is in Adobe Reader 
V 7.0 format. When I bring up manuals for either Liant(RM/COBOL) or 
Fujitsu, looks like they are using the same tool.

You have the Treeview on the left and clicking on a node you can expand 
a chapter and clicking on the lower nodes brings up the relevant text. 
But if you are looking say for 'file status', I would go to the index at 
the bottom of the manual. Unless I've missed it I don't see any way of 
going directly to a page, or pages that cover your search. Am I 
overlooking any shortcuts ?

By contrast, Micro Focus is using a different tool, (and I doubt they 
wrote it themselves). Same Treeview technique but if I do go to the 
index, I can click on an item and go directly to the text which is 
relevant; alternatively it will give me a child-window for several 
references to the same topic. I'm not plugging the M/F approach as being 
"superior",  but it seems to me they have latched on to a more flexible 
tool.

Jimmy
```

###### ↳ ↳ ↳ Re: WDz - COBOL access local files

_(reply depth: 5)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-07-31T17:18:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4j7hdhF6hpo1U1@individual.net>`
- **References:** `<1154114264.018898.228770@i3g2000cwc.googlegroups.com> <HEtyg.422256$SQ6.234926@fe09.news.easynews.com> <sFDyg.188359$mF2.87903@bgtnsc04-news.ops.worldnet.att.net> <pXDyg.150886$tQ4.2283@fe01.news.easynews.com> <Hivzg.288183$Mn5.219870@pd7tw3no>`

```
>
>
…[19 more quoted lines elided]…
>tool.

I'm going to have to take the opposite stance here.  I can't stand the
online format of the M/F documentation.  Is there even a way to search a
whole document for an individual word or phrase?

With IBM's PDF format you can indeed go to the index and click on a word and
be brought to the appropriate page.

What I most like about PDF is that you can download them to your computer
and not have to go to the website for every little thing!

I don't even much care for IBM's "newfangled" way (their Information Center
pages).  Take for example the one for DB2:
http://publib.boulder.ibm.com/infocenter/db2luw/v9/index.jsp.

It's good for searching, especially if you don't know which manual it's in,
but it's fairly useless for just reading an entire manual, or even just an
entire chapter.

JMHO

Frank
```

###### ↳ ↳ ↳ Re: WDz - COBOL access local files

_(reply depth: 6)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-08-01T00:04:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iUwzg.288837$iF6.287673@pd7tw2no>`
- **In-Reply-To:** `<4j7hdhF6hpo1U1@individual.net>`
- **References:** `<1154114264.018898.228770@i3g2000cwc.googlegroups.com> <HEtyg.422256$SQ6.234926@fe09.news.easynews.com> <sFDyg.188359$mF2.87903@bgtnsc04-news.ops.worldnet.att.net> <pXDyg.150886$tQ4.2283@fe01.news.easynews.com> <Hivzg.288183$Mn5.219870@pd7tw3no> <4j7hdhF6hpo1U1@individual.net>`

```
Frank Swarbrick wrote:
>>
>>>>>James J. Gavan<jgavandeletethis@shaw.ca> 07/31/06 4:16 PM >>>
…[23 more quoted lines elided]…
> whole document for an individual word or phrase?

Frankly I'm not interested in searching a whole document to get a count 
on the phrase, "To be or not to be". I want to get say, the low down on 
  "file status" and the index takes me to that; same approach as if I'm 
reading a hard copy text book, rather than flipping through likely chapters.
> 
> With IBM's PDF format you can indeed go to the index and click on a word and
> be brought to the appropriate page.
>

Now having been most emphatic that it can be done - and bearing in mind 
that was my question - care now to spell out the steps to do it ? Thanks 
in advance for info provided, if it is relevant.

> What I most like about PDF is that you can download them to your computer
> and not have to go to the website for every little thing!

Well you can/could download their manuals. Unfortunately I've forgotten 
how. I last used Net Express V 3.1 which didn't have an OO Manual. 
Version 4 onwards does. (Does a pretty good job). I did download and 
printed it out. As a "refresher" I wanted to sit down with a hard copy 
to browse in the comfort of an armchair, rather than staring at a 
computer screen.

(It's been fairly rare that I've needed to reference manuals, other than 
my interest in OO, as above. So I take a quick look-see at manuals 
on-line for a specific topic. Recall I did a program that worked for 
Chris displaying a box with Unix/Server Express. Did a quick look at the 
on-line manuals for Server Express, and confirmed that the Screen 
Section was compatible with what I had in Net Express - otherwise it 
would have been pointless me coding an example).

Perhaps Bill or one of the M/F lurkers can advise you how to download ?

Jimmy

> 
> I don't even much care for IBM's "newfangled" way (their Information Center
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: WDz - COBOL access local files

_(reply depth: 7)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-08-01T10:00:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4j9c5iF5aocfU1@individual.net>`
- **References:** `<1154114264.018898.228770@i3g2000cwc.googlegroups.com> <HEtyg.422256$SQ6.234926@fe09.news.easynews.com> <sFDyg.188359$mF2.87903@bgtnsc04-news.ops.worldnet.att.net> <pXDyg.150886$tQ4.2283@fe01.news.easynews.com> <Hivzg.288183$Mn5.219870@pd7tw3no> <4j7hdhF6hpo1U1@individual.net> <iUwzg.288837$iF6.287673@pd7tw2no>`

```
James J. Gavan<jgavandeletethis@shaw.ca> 07/31/06 6:04 PM >>>
>
>Frankly I'm not interested in searching a whole document to get a count 
>on the phrase, "To be or not to be". I want to get say, the low down on 
>  "file status" and the index takes me to that; same approach as if I'm 
>reading a hard copy text book, rather than flipping through likely
chapters.

That's not what I was getting at.  I am interested in two things
1) Using 'find' to find the next or previous occurance of a word (or
phrase)
2) Using 'search' to give me a list of all occurances of a word or phrase

>> 
>> With IBM's PDF format you can indeed go to the index and click on a word
and
>> be brought to the appropriate page.
>>
…[3 more quoted lines elided]…
>in advance for info provided, if it is relevant.

OK...I'm not sure I am getting what problem you are having with this.  But
here's an example...  
Point your browser to
http://publibfp.boulder.ibm.com/epubs/pdf/igywlr00.pdf.  This will download
the PDF and load it in to your browser.  (Assuming you have Adobe Acrobat
Reader and the browser plugin is installed properly.)  You can then click on
the "bookmarks" tab (assuming it's not already open) and it will give you a
list of chapters.  One of the "chapters" is Index.  Click on it.  Find an
indexed word you are interested in and click on the page number.  That page
should now display.


Frank

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

###### ↳ ↳ ↳ Re: WDz - COBOL access local files

_(reply depth: 8)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-08-01T17:02:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BOLzg.300571$Mn5.177639@pd7tw3no>`
- **In-Reply-To:** `<4j9c5iF5aocfU1@individual.net>`
- **References:** `<1154114264.018898.228770@i3g2000cwc.googlegroups.com> <HEtyg.422256$SQ6.234926@fe09.news.easynews.com> <sFDyg.188359$mF2.87903@bgtnsc04-news.ops.worldnet.att.net> <pXDyg.150886$tQ4.2283@fe01.news.easynews.com> <Hivzg.288183$Mn5.219870@pd7tw3no> <4j7hdhF6hpo1U1@individual.net> <iUwzg.288837$iF6.287673@pd7tw2no> <4j9c5iF5aocfU1@individual.net>`

```
Frank Swarbrick wrote:
> James J. Gavan<jgavandeletethis@shaw.ca> 07/31/06 6:04 PM >>>
> 
…[35 more quoted lines elided]…
>
Thanks Frank,

I didn't download but it still worked. What I was doing was going to the 
Index and clicking on the word/descriptor, for example "Delete" - I got 
nothing - works fine when you click on the actual page reference. (A 
classic example of 'Windows' where you are supposed to know 'how it 
works'. I have never considered the concept of Wndows as being user 
friendly).

So having got the page number - both are compatible. Just one minor 
detail, and no big deal.

- Adobe - click on the Index in the left pane gives you the alphabetized 
index; scroll/page down to topic, select the page number gives you the 
relevant text. But, your left pane now shows the Treeview again. (Five 
entries for 'Delete' for IBM LRM)

- Product 'X' as used by M/F - click on Index and the left pane shows 
topics alphabetically, prefixed by a table of alphabetic letters. You 
can click on a letter to jump to entries for that or scroll down through 
the list to get to the topics for that letter. (Three entries for 
'Delete' for the MF LRM). Display the topic - BUT - that left pane still 
shows the Index information which you can return to.

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
