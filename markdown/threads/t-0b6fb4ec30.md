[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Variable Length Files

_23 messages · 10 participants · 2005-01_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Variable Length Files

- **From:** "ki" <please@dontemail.me>
- **Date:** 2005-01-20T20:52:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net>`

```
Can someone answer this:
What do the 4 bytes at the beginning of a Variable Block File contain?

TIA
```

#### ↳ Re: Variable Length Files

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-01-20T15:16:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10v07t41rtm2u81@news.supernews.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net>`

```
ki wrote:
> Can someone answer this:
> What do the 4 bytes at the beginning of a Variable Block File contain?
>

At least the length of the record (how else would the program know?). 
Sometimes the length of the block also (else how would the program know?)
```

##### ↳ ↳ Re: Variable Length Files

- **From:** "ki" <please@dontemail.me>
- **Date:** 2005-01-20T21:19:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qfVHd.56551$w62.24998@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <10v07t41rtm2u81@news.supernews.com>`

```
Thanks,
what determines whether or not the  length of the block is there?



"JerryMouse" <nospam@bisusa.com> wrote in message 
news:10v07t41rtm2u81@news.supernews.com...
> ki wrote:
>> Can someone answer this:
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Variable Length Files

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-01-20T21:32:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lrVHd.1106502$2W1.86316@news.easynews.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <10v07t41rtm2u81@news.supernews.com> <qfVHd.56551$w62.24998@bgtnsc05-news.ops.worldnet.att.net>`

```
For a Variable length BLOCKED file (on IBM mainframes),  There are two sets of 
4-byte fields, the RDW and BDW.  The RDW (Record Descriptor Word) appears before 
each record - guess where the Block Descriptor Word is?

Both are in an "LLZZ" format.  The first 2-bytes are (in binary) the length - 
and the 3rd and 4th bytes are "reserved for IBM use" (as far as I know, they are 
always hex-zeroes, but I could be mistaken on this).
```

###### ↳ ↳ ↳ Re: Variable Length Files

_(reply depth: 4)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2005-01-21T00:42:22+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2tc0v0d5u4g5mii1uld5sr8g6d3rgp7df8@4ax.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <10v07t41rtm2u81@news.supernews.com> <qfVHd.56551$w62.24998@bgtnsc05-news.ops.worldnet.att.net> <lrVHd.1106502$2W1.86316@news.easynews.com>`

```
On Thu, 20 Jan 2005 21:32:01 GMT "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

:>For a Variable length BLOCKED file (on IBM mainframes),  There are two sets of 
:>4-byte fields, the RDW and BDW.  The RDW (Record Descriptor Word) appears before 
:>each record - guess where the Block Descriptor Word is?

:>Both are in an "LLZZ" format.  The first 2-bytes are (in binary) the length - 
:>and the 3rd and 4th bytes are "reserved for IBM use" (as far as I know, they are 
:>always hex-zeroes, but I could be mistaken on this).

They contain a spanning indication if using VBS. That way you can have a
record larger than the block size.
```

###### ↳ ↳ ↳ Re: Variable Length Files

_(reply depth: 4)_

- **From:** "ki" <please@dontemail.me>
- **Date:** 2005-01-20T23:15:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CYWHd.7642$8u5.1663@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <10v07t41rtm2u81@news.supernews.com> <qfVHd.56551$w62.24998@bgtnsc05-news.ops.worldnet.att.net> <lrVHd.1106502$2W1.86316@news.easynews.com>`

```
>>guess where the Block Descriptor Word is?

Before each block?  Other than coding an extra 4 bytes for blocksize in JCL 
does the BDW come in to play?




"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:lrVHd.1106502$2W1.86316@news.easynews.com...
> For a Variable length BLOCKED file (on IBM mainframes),  There are two 
> sets of 4-byte fields, the RDW and BDW.  The RDW (Record Descriptor Word) 
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Variable Length Files

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-01-20T23:37:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TgXHd.1113368$lR6.168111@news.easynews.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <10v07t41rtm2u81@news.supernews.com> <qfVHd.56551$w62.24998@bgtnsc05-news.ops.worldnet.att.net> <lrVHd.1106502$2W1.86316@news.easynews.com> <CYWHd.7642$8u5.1663@bgtnsc04-news.ops.worldnet.att.net>`

```
For COBOL, I don't know if you get a FS=39 if you explicitly code BLOCK CONTAINS 
n RECORDS (not "0") and the BDW doesn't match.  I would *guess* that this is a 
"hang over" from magnetic tape days - and maybe it could do something "more 
efficient" with it, but I don't know WHY it is there - just that it is <G>.
```

###### ↳ ↳ ↳ Re: Variable Length Files

_(reply depth: 6)_

- **From:** "ki" <please@dontemail.me>
- **Date:** 2005-01-20T23:48:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wrXHd.7726$8u5.2791@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <10v07t41rtm2u81@news.supernews.com> <qfVHd.56551$w62.24998@bgtnsc05-news.ops.worldnet.att.net> <lrVHd.1106502$2W1.86316@news.easynews.com> <CYWHd.7642$8u5.1663@bgtnsc04-news.ops.worldnet.att.net> <TgXHd.1113368$lR6.168111@news.easynews.com>`

```
Thanks for all your help.

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:TgXHd.1113368$lR6.168111@news.easynews.com...
> For COBOL, I don't know if you get a FS=39 if you explicitly code BLOCK 
> CONTAINS n RECORDS (not "0") and the BDW doesn't match.  I would *guess* 
…[57 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Variable Length Files

_(reply depth: 4)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-01-23T10:44:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-A95C5F.10440523012005@knology.usenetserver.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <10v07t41rtm2u81@news.supernews.com> <qfVHd.56551$w62.24998@bgtnsc05-news.ops.worldnet.att.net> <lrVHd.1106502$2W1.86316@news.easynews.com>`

```
In article <lrVHd.1106502$2W1.86316@news.easynews.com>,
 "William M. Klein" <wmklein@nospam.netcom.com> wrote:

> For a Variable length BLOCKED file (on IBM mainframes),  There are two sets 
> of 
…[7 more quoted lines elided]…
> always hex-zeroes, but I could be mistaken on this).

For RECFM V and VB they are always zeros -- but in cases of the rarely 
used RECFM=VS, variable spanned, they can contain a block offset.  I 
think also files that use large blocks, like tapes, will also have 
something there.
```

#### ↳ Re: Variable Length Files

- **From:** docdwarf@panix.com
- **Date:** 2005-01-20T16:58:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<csp9hm$p6j$1@panix5.panix.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net>`

```
In article <YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net>,
ki <please@dontemail.me> wrote:
>Can someone answer this:
>What do the 4 bytes at the beginning of a Variable Block File contain?

Please do your own homework.

DD
```

##### ↳ ↳ Re: Variable Length Files

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-01-25T07:47:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GQmJd.278930$6w6.191086@tornado.tampabay.rr.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <csp9hm$p6j$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:csp9hm$p6j$1@panix5.panix.com...
> In article <YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net>,
> ki <please@dontemail.me> wrote:
…[5 more quoted lines elided]…
> DD
I believe he is. His method is to utilize the resources available to him. 
How is using a newsgroup different than reading a book in this instance?
It's not exactly a thought provoking or mind engaging question.

JCE
```

###### ↳ ↳ ↳ Re: Variable Length Files

- **From:** docdwarf@panix.com
- **Date:** 2005-01-25T05:16:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ct56a9$rob$1@panix5.panix.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <csp9hm$p6j$1@panix5.panix.com> <GQmJd.278930$6w6.191086@tornado.tampabay.rr.com>`

```
In article <GQmJd.278930$6w6.191086@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
>
><docdwarf@panix.com> wrote in message news:csp9hm$p6j$1@panix5.panix.com...
…[8 more quoted lines elided]…
>How is using a newsgroup different than reading a book in this instance?

The same way that presenting another student's work as one's own instaed 
of doing one's research into the text is.

>It's not exactly a thought provoking or mind engaging question.

The quality of the question has little effect on the quality of the 
method; there is, in my experience, a difference between a practioner of 
*any* skill who learns by researching the texts and one who gets answers 
by allowing others to give them.

DD
```

###### ↳ ↳ ↳ Re: Variable Length Files

_(reply depth: 4)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-01-28T06:49:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7glKd.2646$JO2.1687@tornado.tampabay.rr.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <csp9hm$p6j$1@panix5.panix.com> <GQmJd.278930$6w6.191086@tornado.tampabay.rr.com> <ct56a9$rob$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:ct56a9$rob$1@panix5.panix.com...
> In article <GQmJd.278930$6w6.191086@tornado.tampabay.rr.com>,
> jce <defaultuser@hotmail.com> wrote:
…[14 more quoted lines elided]…
> of doing one's research into the text is.

If I found it in a book, it's still not my own work.

>>It's not exactly a thought provoking or mind engaging question.
>
…[3 more quoted lines elided]…
> by allowing others to give them.

I use an index of a book.  Generally speaking, the index gives me the 
location of the answer.  I usually then skip over the stuff I don't care 
about until I see something like....the "4 bytes at the beginning 
contain....."
All I've done is prove that I know how a reference book works.  Though it is 
quicker and more reliable than a newsgroup...

A question that I would expect in an assignment would be something that 
would force someone to do some cognitive processing: "What's the difference 
between a variable block and fixed block record?"
In those instances I would agree with your assessment - the question could 
lead down a path of extended learning.
I see little to gain in research above and beyond just getting the answer to 
a question that is "what is a <non abstract object>?"  The only quality that 
can be introduced here is a response that includes the answer but is not the 
answer alone.

JCE
```

###### ↳ ↳ ↳ Re: Variable Length Files

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-28T05:23:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ctd3rr$6iq$1@panix5.panix.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <GQmJd.278930$6w6.191086@tornado.tampabay.rr.com> <ct56a9$rob$1@panix5.panix.com> <7glKd.2646$JO2.1687@tornado.tampabay.rr.com>`

```
In article <7glKd.2646$JO2.1687@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:
>
><docdwarf@panix.com> wrote in message news:ct56a9$rob$1@panix5.panix.com...
…[18 more quoted lines elided]…
>If I found it in a book, it's still not my own work.

If you found it in a book you did your own research into the text, as 
stated above.

>
>>>It's not exactly a thought provoking or mind engaging question.
…[6 more quoted lines elided]…
>I use an index of a book.

Then you are researching the text, as stated above.

DD
```

#### ↳ Re: Variable Length Files

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2005-01-21T18:55:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20050121.18554336@rechner12.lerch.home>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net>`

```


>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 20.01.05, 20:52:08, schrieb "ki" <please@dontemail.me> zum Thema 
Variable Length Files:


> Can someone answer this:
> What do the 4 bytes at the beginning of a Variable Block File contain?

> TIA

Hi

normaly you can not have access to the RDW (Record Descriptor Word) in 
cobol, only you have a file:
(william:
For a Variable length BLOCKED file (on IBM mainframes),  There are two 
sets of 4-byte fields, the RDW and BDW.  The RDW (Record Descriptor 
Word) appears before each record - guess where the Block Descriptor 
Word is?
)
defined with U (undefined).
Then you will get every date, byte, of a file and must interprate 
yourselve.

See: Loadmodule: they are defined as 'undefined'. The loader does his 
work.

essential: look at the file attributes, and then you will see the 
data, the file contains!

Einen schoenen Tag
Andreas Lerch
```

##### ↳ ↳ Re: Variable Length Files

- **From:** "ki" <please@dontemail.me>
- **Date:** 2005-01-21T18:50:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3acId.62089$w62.39835@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <20050121.18554336@rechner12.lerch.home>`

```
Thanks for your help.
This was I question I only got half right on a technical.
Must have been confusing my SYNCSORT with my cobol programs
in SORT you need to account for the 4 byte RDW.
As far as the BDW, other than knowing I need to add 4 bytes to the blocksize 
in the JCL I never really paid attention to it, and missed that part of the 
question.

I have one more I missed, can anyone help me with this...

I've never actually compiled using the IBM compiler procs, I've only used 
ChangeMan, that's why I missed this...
What is ENTRY on a link card?
I presume this has something to do with entry in a cobol program, but....

Anybody?

TIA



"Andreas Lerch" <andreas@andreas-lerch.de> wrote in message 
news:20050121.18554336@rechner12.lerch.home...


>>>>>>>>>>>>>>>>>> Urspr�ngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 20.01.05, 20:52:08, schrieb "ki" <please@dontemail.me> zum Thema
Variable Length Files:


> Can someone answer this:
> What do the 4 bytes at the beginning of a Variable Block File contain?

> TIA

Hi

normaly you can not have access to the RDW (Record Descriptor Word) in
cobol, only you have a file:
(william:
For a Variable length BLOCKED file (on IBM mainframes),  There are two
sets of 4-byte fields, the RDW and BDW.  The RDW (Record Descriptor
Word) appears before each record - guess where the Block Descriptor
Word is?
)
defined with U (undefined).
Then you will get every date, byte, of a file and must interprate
yourselve.

See: Loadmodule: they are defined as 'undefined'. The loader does his
work.

essential: look at the file attributes, and then you will see the
data, the file contains!

Einen schoenen Tag
Andreas Lerch
```

###### ↳ ↳ ↳ ENTRY Linkage Editor/Binder (was: Variable Length Files

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-01-21T20:37:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nKdId.1171984$lR6.176622@news.easynews.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <20050121.18554336@rechner12.lerch.home> <3acId.62089$w62.39835@bgtnsc05-news.ops.worldnet.att.net>`

```
Well ....

"ENTRY" as an IBM link-edit (or binder) statement DOES relate to the ENTRY 
statement in COBOL (among other things).

If you compile with the (LE-conforming COBOL)
  NAME(ALIAS)
compiler option  - see:
   http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg20/2.4.31

It will produce the correct "ENTRY" linkage editor card (if needed).

See also the related topics at:
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg20/4.1.6.3

Some other "products" (most notably IMS and DB2) have specific ENTRY linkage 
requirements.

Do you have a specific question/problem - or is this a "general 
information/learning" question?
```

###### ↳ ↳ ↳ Re: ENTRY Linkage Editor/Binder (was: Variable Length Files

_(reply depth: 4)_

- **From:** "ki" <please@dontemail.me>
- **Date:** 2005-01-22T23:12:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n5BId.14487$8u5.14218@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <20050121.18554336@rechner12.lerch.home> <3acId.62089$w62.39835@bgtnsc05-news.ops.worldnet.att.net> <nKdId.1171984$lR6.176622@news.easynews.com>`

```
General question.
Thanks for the help

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:nKdId.1171984$lR6.176622@news.easynews.com...
> Well ....
>
…[89 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Variable Length Files

- **From:** "steve.t" <sthompson@ix.netcom.com>
- **Date:** 2005-01-21T13:37:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106343428.339968.229160@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<3acId.62089$w62.39835@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <20050121.18554336@rechner12.lerch.home> <3acId.62089$w62.39835@bgtnsc05-news.ops.worldnet.att.net>`

```
The full answer (from an applications view) is this:

1) When on MVS systems, if you have coded RECFM=VB you will get:

BDW RDW data

Unless you code in your JCL RECFM=U, the I/O system will only hand you
the RDW and data that goes with it. COBOL then suppresses the RDW and
only hands you the data.

If you code RECFM=U then your FD better be set up for UNDEFINED as
well. Then you will get the BDW and all the RDWs in a physical block of
data.

(BTW - there is a bit more that you have to do to get all this to
work.)

2) ENTRY is a command to the Linkage Editor that allows it to give an
alternate entry location for a load module. This is linked to the COBOL
ENTRY directive.
```

###### ↳ ↳ ↳ Re: Variable Length Files

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-01-21T23:36:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TlgId.1176850$lR6.177561@news.easynews.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <20050121.18554336@rechner12.lerch.home> <3acId.62089$w62.39835@bgtnsc05-news.ops.worldnet.att.net> <1106343428.339968.229160@z14g2000cwz.googlegroups.com>`

```
Although a COBOL program may not LEGALLY access the storage area of the RDW, it 
was relatively common for OS/VS COBOL programs to "negative subscript" to access 
it.

With VS COBOL II, R3 and later, an ('85 Standard conforming) COBOL program can 
EASILY get the VALUE of the "LL" (length) info from the RDW - by using the

  RECORD VARYING IN SIZE DEPENDING ON

clause of the FD.

(This allows one to find out the length of a record that was read - or to 
determine the length to be written)
```

###### ↳ ↳ ↳ Re: Variable Length Files

_(reply depth: 4)_

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2005-01-22T14:40:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106433639.519266.192380@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1106343428.339968.229160@z14g2000cwz.googlegroups.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <20050121.18554336@rechner12.lerch.home> <3acId.62089$w62.39835@bgtnsc05-news.ops.worldnet.att.net> <1106343428.339968.229160@z14g2000cwz.googlegroups.com>`

```
Hi Steve,

I know what the BDW does and I know what the RDW does.  What does the
BTW do?

Regards, Jack.
```

###### ↳ ↳ ↳ Re: Variable Length Files

_(reply depth: 5)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-01-23T10:45:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-139613.10455323012005@knology.usenetserver.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <20050121.18554336@rechner12.lerch.home> <3acId.62089$w62.39835@bgtnsc05-news.ops.worldnet.att.net> <1106343428.339968.229160@z14g2000cwz.googlegroups.com> <1106433639.519266.192380@c13g2000cwb.googlegroups.com>`

```
In article <1106433639.519266.192380@c13g2000cwb.googlegroups.com>,
 "slade2" <jacksleight@hotmail.com> wrote:

> Hi Steve,
> 
…[3 more quoted lines elided]…
> Regards, Jack.

It's an acronym for "By The Way"...
```

###### ↳ ↳ ↳ Re: Variable Length Files

_(reply depth: 6)_

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2005-01-23T10:53:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106506425.168932.107080@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<joe_zitzelberger-139613.10455323012005@knology.usenetserver.com>`
- **References:** `<YRUHd.56426$w62.44185@bgtnsc05-news.ops.worldnet.att.net> <20050121.18554336@rechner12.lerch.home> <3acId.62089$w62.39835@bgtnsc05-news.ops.worldnet.att.net> <1106343428.339968.229160@z14g2000cwz.googlegroups.com> <1106433639.519266.192380@c13g2000cwb.googlegroups.com> <joe_zitzelberger-139613.10455323012005@knology.usenetserver.com>`

```
Sorry Joe, that was just my feeble attempt at humor.  I couldn't
resist.

Jack.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
