[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fuji Power Cobol Byte Alignment ??

_28 messages · 7 participants · 2001-03_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Fuji Power Cobol Byte Alignment ??

- **From:** Rob Lec <RobLec@cinci-rr.com>
- **Date:** 2001-03-22T00:23:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AB945F5.90CA9005@cinci-rr.com>`

```

Trying to use PIC 99 COMP.  PowerCOBOL seems to treat it as two bytes
rather than just one.   I routinely use @OPTIONS BINARY(BYTE) to get
around this in COBOL97, but cannot find "what's the trick" in
Powercobol.  Can anyone help me?  I need this to read date fields in
Btrieve, which stores month and day each as a single byte.  Microfocus
always did this right.

-------------------------------------------------
(To reply by email change dash to dot in address)
```

#### ↳ Re: Finally found "the trick"

- **From:** Rob Lec <RobLec@cinci-rr.com>
- **Date:** 2001-03-22T23:21:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABA88F5.BD44C48C@cinci-rr.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com>`

```
Answering my own question...

> Trying to use PIC 99 COMP.  PowerCOBOL seems to treat it as two bytes
> rather than just one.   I routinely use @OPTIONS BINARY(BYTE) to get
> around this in COBOL97, but cannot find "what's the trick" in
> Powercobol.  Can anyone help me?

  The 'trick' is right-click on the EXE, select properties and enter
BINARY(BYTE) in the box on the compile options tab and click 'Set'.  It
only took me two days to discover this.  It could not have been hidden
any better if they had done so intentionally.

> Microfocus always did this right.

So I must ask, why is this not the default?
 
-------------------------------------------------
(To reply by email change dash to dot in address)
```

##### ↳ ↳ Re: Finally found "the trick"

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-03-23T12:10:48+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3aba9559_5@news.newsfeeds.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3ABA88F5.BD44C48C@cinci-rr.com>`

```

Rob Lec wrote in message <3ABA88F5.BD44C48C@cinci-rr.com>...

>
>So I must ask, why is this not the default?
>
Discovering a compiler option is hardly a "trick"...

If you had done the "Getting Started" tutorial it explains how to set
Compiler options.

"Byte" for Binary is not the default because most of us are NOT using
Btrieve, neither is single byte binary used to any great extent in other
software (ACCESS supports it for small integers), and where it is, it is a
simple matter to move it to the low order byte of a two-byte binary field.
Fujitsu probably believe that the majority want compatibility with IBM
mainframes which default to 32 bits (Halfword) for binary fields.

I have no idea why you "sweated" this, but having done so, please accept
that your own frustration is entirely a matter for you. It is no reason to
change the default.

If you believe that MicroFocus got it "right" (a curious interpretation, as
there is no "rightness" or "wrongness" here, just a question of what you
want to do) , use their product.

Pete.



-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

###### ↳ ↳ ↳ Re: Finally found "the trick"

- **From:** Rob Lec <RobLec@cinci-rr.com>
- **Date:** 2001-03-23T03:26:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABAC243.2B1DAFAD@cinci-rr.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3ABA88F5.BD44C48C@cinci-rr.com> <3aba9559_5@news.newsfeeds.com>`

```

Thank you Peter, for taking the time to reply.

"Peter E. C. Dashwood" wrote:
> Discovering a compiler option is hardly a "trick"...
> If you had done the "Getting Started" tutorial it explains how to set
> Compiler options.

I have not been able to find any statement in their online manuals about
the necessity to set this option in order to access a simple unsigned
character.  In fact, the term "byte" hardly appears anywhere in the
PowerCOBOL manuals.  (I searched specifically for this option and it is
simply NOT there).  Furthermore, it seems that I will need to remember
to go thru this exercise at the outset of each new program I write.

> "Byte" for Binary is not the default because most of us are NOT using
> Btrieve, neither is single byte binary used to any great extent in other
> software 

This is my first experience with Btrieve, and not having any manuals, I
am pretty much on my own to make things work any way I can.

> 
> I have no idea why you "sweated" this, but having done so, please accept
> that your own frustration is entirely a matter for you. 
>

I was hoping that perhaps SOMEONE in this NG may have encountered this
at some time, and might be willing to impart a bit of their knowledge.

> 
> If you believe that MicroFocus got it "right" (a curious interpretation, as
> there is no "rightness" or "wrongness" here, just a question of what you
> want to do) , use their product.

I have enjoyed using MF for the past decade, but Fujitsu seems to be
better suited for this assignment.  For various reasons, I could not in
good conscience recommend that this particular client invest in Merant's
product.
```

###### ↳ ↳ ↳ Re: Finally found "the trick"

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-03-23T23:33:41+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abb3866_7@news.newsfeeds.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3ABA88F5.BD44C48C@cinci-rr.com> <3aba9559_5@news.newsfeeds.com> <3ABAC243.2B1DAFAD@cinci-rr.com>`

```
Rob,

I sympathize with the difficulty in searching for something and not being
able to find it...many people experience this same frustration when they
first start using Web Search engines.

If I sounded a bit harsh (on second reading it does seem that way...) I'm
genuinely sorry.

I guess it just seemed so trivial to me that I was miffed when you suggested
the default be changed because you couldn't get to grips with it, or because
it doesn't work the way some other vendor's software does.  The answer is
"Deal with it", just like we all do when we use new software... If you do a
search on "byte" and it turns up nothing, try another search...

I hope you manage to get your Btrieve working, and I apologise if I sounded
short. (I'm actually 6 feet tall...<G>)

Pete.
Rob Lec wrote in message <3ABAC243.2B1DAFAD@cinci-rr.com>...
>
>Thank you Peter, for taking the time to reply.
…[29 more quoted lines elided]…
>> If you believe that MicroFocus got it "right" (a curious interpretation,
as
>> there is no "rightness" or "wrongness" here, just a question of what you
>> want to do) , use their product.
…[4 more quoted lines elided]…
>product.



-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

##### ↳ ↳ Re: Finally found "the trick"

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-03-23T00:31:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aPwu6.2120$ue1.145329@newsread2.prod.itd.earthlink.net>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3ABA88F5.BD44C48C@cinci-rr.com>`

```

"Rob Lec" <RobLec@cinci-rr.com> wrote in message
news:3ABA88F5.BD44C48C@cinci-rr.com...
> Answering my own question...
>
> > Trying to use PIC 99 COMP.  PowerCOBOL seems to treat it as two
bytes
> > rather than just one.   I routinely use @OPTIONS BINARY(BYTE) to
get
> > around this in COBOL97, but cannot find "what's the trick" in
> > Powercobol.  Can anyone help me?
>
>   The 'trick' is right-click on the EXE, select properties and enter
> BINARY(BYTE) in the box on the compile options tab and click 'Set'.
It
> only took me two days to discover this.  It could not have been
hidden
> any better if they had done so intentionally.
>

It was easier in a previous compiler we used too. And through mistakes
in awareness, this feature hosed us several times. We now prohibit
single-byte binary definitions. If a single byte is required to
contain a binary number, we access/create it the old-fashioned way.

While more work (like two lines instead of one), the code stands out
as if written in red as a warning to the maintenance guy.
```

##### ↳ ↳ Re: Finally found "the trick"

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-03-22T22:03:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<99ehv5$v4a$1@slb7.atl.mindspring.net>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3ABA88F5.BD44C48C@cinci-rr.com>`

```
Just for those who may have missed it in other threads, the draft of the
next Standard includes a new USAGE

    BINARY-CHAR

which will PROBABLY be implemented as a "one-byte" binary usage.  (There are
also BINARY-SHORT, BINARY-LONG - each with signed and unsigned versions).
```

###### ↳ ↳ ↳ Re: Finally found "the trick"

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-03-23T23:37:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abb3869_7@news.newsfeeds.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3ABA88F5.BD44C48C@cinci-rr.com> <99ehv5$v4a$1@slb7.atl.mindspring.net>`

```
William M. Klein wrote in message <99ehv5$v4a$1@slb7.atl.mindspring.net>...
>Just for those who may have missed it in other threads, the draft of the
>next Standard includes a new USAGE
…[3 more quoted lines elided]…
>which will PROBABLY be implemented as a "one-byte" binary usage.  (There
are
>also BINARY-SHORT, BINARY-LONG - each with signed and unsigned versions).
>
Sounds real good, Bill...

Shame we won't be seeing it until circa 2020...<G>

Pete.



-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

###### ↳ ↳ ↳ Re: Finally found "the trick"

_(reply depth: 4)_

- **From:** Rob Lec <RobLec@cinci-rr.com>
- **Date:** 2001-03-23T13:44:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABB5343.DE3B0F3@cinci-rr.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3ABA88F5.BD44C48C@cinci-rr.com> <99ehv5$v4a$1@slb7.atl.mindspring.net> <3abb3869_7@news.newsfeeds.com>`

```
> 
> Shame we won't be seeing it until circa 2020...<G>
> 

Thanks, I got a good chuckle out of that one
(also your apology was very much appreciated)

Have a great weekend!

-------------------------------------------------
(To reply by email change dash to dot in address)
```

###### ↳ ↳ ↳ Re: Finally found "the trick"

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-03-24T16:07:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abcc5bf.300356767@news1.attglobal.net>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3ABA88F5.BD44C48C@cinci-rr.com> <99ehv5$v4a$1@slb7.atl.mindspring.net> <3abb3869_7@news.newsfeeds.com>`

```
I've previously asked Fujitsu for several "features" many of which I
now see in v 6.1.

Removing trailing spaces in Line Sequential files is one of them.

I'll ask them to implement the Binary-Char (After I make sure it's not
in 6.1).

If OTHERS will as well, then we will more likely see it before 2020.
Vendors to not have to wait for the draft to be approved in order to
implement portions of it.

For Example - In 6.1 Fujitsu has implemented Strongly typed data
items.

So, if MULTIPLE people ask for this feature we might get it.

email your request to support@adtools.com


On Fri, 23 Mar 2001 23:37:26 +1200, "Peter E. C. Dashwood"
<dashwood@enternet.co.nz.nospam> wrote:

>William M. Klein wrote in message <99ehv5$v4a$1@slb7.atl.mindspring.net>...
>>Just for those who may have missed it in other threads, the draft of the
…[18 more quoted lines elided]…
>-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

##### ↳ ↳ Re: Finally found "the trick"

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-03-24T16:04:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abcc54c.300241108@news1.attglobal.net>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3ABA88F5.BD44C48C@cinci-rr.com>`

```
Its not the default because Binary(BYTE) has some other unfortunate
side effects.

Try it on a Pic S9(5) COMP field for instance.  

On Thu, 22 Mar 2001 23:21:45 GMT, Rob Lec <RobLec@cinci-rr.com> wrote:

>Answering my own question...
>
…[15 more quoted lines elided]…
>(To reply by email change dash to dot in address)
```

#### ↳ Re: Fuji Power Cobol Byte Alignment ??

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-03-24T15:55:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abcc2c7.299599779@news1.attglobal.net>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com>`

```
I don't use PowerCOBOL but I'm suprised you can't set the directive
for PowerCOBOL just like COBOL97.

Another option is to read it into a PIC X and then move it like this:

01  Binary-Work.
     03  Data-Item Pic 9(4) COMP.
     03  Data-Item-R redefines Data-Item.
           03  Pic X.
           03  Data-Byte Pic X.

Then 
Move Zeros To Data-Item
Move Returned-Byte to Data-Byte

Data-Item will then have your proper numeric value.


On Thu, 22 Mar 2001 00:23:29 GMT, Rob Lec <RobLec@cinci-rr.com> wrote:

>
>Trying to use PIC 99 COMP.  PowerCOBOL seems to treat it as two bytes
…[7 more quoted lines elided]…
>(To reply by email change dash to dot in address)
```

##### ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-03-25T05:50:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HGfv6.9211$ue1.844441@newsread2.prod.itd.earthlink.net>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net>`

```
As I said earlier, that's the way we do it - after getting nailed to a
post in the middle of a corn field too many times. A small adjustment
on your fine code:

 01  Binary-Work VALUE LOW-VALUES.         *> "VALUE" statement new
      03  Data-Item Pic 9(4) COMP.
      03  Data-Item-R redefines Data-Item.
            05  Pic X.
            05  Data-Byte Pic X.

Thereafter,

MOVE RETURNED-BYTE TO Data-Byte.

Is sufficient to set Data-Item to the required value.

Now, to be able to handle negative numbers, one has to swap things
around a bit (otherwise a -1 turns out to be 255, i.e., 0000 0000 1111
1111):

01  Binary-Work Value Low-values.
   03  Data-Item  Pic S9(4) COMP-5.        *> COMP-5 instead of
COMP(-4)
   03  Filler redefines Data-Item.
      05  Data-Byte   Pic X.                           *>Swapped with
next byte
      05  Filler Pic X.

MOVE RETURNED-BYTE TO Data-Byte

works as before. To reverse - that is take an internal number and
represent it in one byte -

MOVE INTERNAL-NUMBER TO DATA-ITEM.
MOVE DATA-BYTE TO (output field PIC X)

Making sure before hand that INTERNAL-NUMBER does not exceed 127.



"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:3abcc2c7.299599779@news1.attglobal.net...
> I don't use PowerCOBOL but I'm suprised you can't set the directive
> for PowerCOBOL just like COBOL97.
>
> Another option is to read it into a PIC X and then move it like
this:
>
> 01  Binary-Work.
…[12 more quoted lines elided]…
> On Thu, 22 Mar 2001 00:23:29 GMT, Rob Lec <RobLec@cinci-rr.com>
wrote:
>
> >
> >Trying to use PIC 99 COMP.  PowerCOBOL seems to treat it as two
bytes
> >rather than just one.   I routinely use @OPTIONS BINARY(BYTE) to
get
> >around this in COBOL97, but cannot find "what's the trick" in
> >Powercobol.  Can anyone help me?  I need this to read date fields
in
> >Btrieve, which stores month and day each as a single byte.
Microfocus
> >always did this right.
> >
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

- **From:** Rob LeClaire <RobLec@cinci-rr.com>
- **Date:** 2001-03-25T21:56:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABE23AC.6B6DECCF@cinci-rr.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net>`

```


Thane Hubbell wrote:
> 
> I don't use PowerCOBOL but I'm suprised you can't set the directive
> for PowerCOBOL just like COBOL97.
> 

In Cobol97 you can specify options "in line" within the source code
using the "@option" directive (just as $set in MF), but there is nowhere
in PowerCOBOL to put such a statement.  The source is broken into
multiple branches in a explorer-like tree structure.  There is not even
an Identification Division, and everywhere I tried to include a
directive produced an error message.  Instead, compiler directives are
specified by right-clicking on the "script" section of the code tree,
which IMHO tends to make the source code fragmented and obscure. 

Also:
>> 
>> Its not the default because Binary(BYTE) has some other unfortunate
…[3 more quoted lines elided]…
>>

Let me guess ... it produces a 3-byte field, right?  I am assuming that
Fujitsu defaults to NOTRUNC and therefore allows a full 65,536 range of
values for a 9(4)comp field.  If you've found otherwise, please let me
know so I don't have to stumble across this by accident!

> Another option is to read it into a PIC X and then move it like this:
> 01  Binary-Work.
…[9 more quoted lines elided]…
>
Yes, this was certainly one of the options I had considered, but given
the number of dates which appear in the database this would produce a
lot of essentially unnecessary code.  And PowerCOBOL is IMO not
conducive to efficient management of large source files (I know the
flames and arrows will follow...)  Above all, COBOL source code *should*
be CLEAR and easily understood.

-------------------------------------------------
(To reply by email change dash to dot in address)
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-03-25T23:30:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<acvv6.458998$f36.14556065@news20.bellglobal.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com>`

```
Rob, this might sound a bit weird, but could you not just write a Cobol97
subroutine to do the job, then call it from PowerCobol?  I think you *can*
set in-line directives in a subroutine .. Thane would know the answer to
that.

"Rob LeClaire" <RobLec@cinci-rr.com> wrote in message
news:3ABE23AC.6B6DECCF@cinci-rr.com...
>
>
…[48 more quoted lines elided]…
> (To reply by email change dash to dot in address)
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-03-26T01:26:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abe9a98.32492859@news1.attglobal.net>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com> <acvv6.458998$f36.14556065@news20.bellglobal.com>`

```
I don't KNOW, but I have seen it documented that you can call
"regular" COBOL programs from PowerCOBOL.  And I do know that
different called programs can be compiled with differing compiler
options.


On Sun, 25 Mar 2001 23:30:14 GMT, "Donald Tees"
<donald_tees@sympatico.ca> wrote:

>Rob, this might sound a bit weird, but could you not just write a Cobol97
>subroutine to do the job, then call it from PowerCobol?  I think you *can*
…[57 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-03-26T22:50:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abf1ed3_2@news.newsfeeds.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com> <acvv6.458998$f36.14556065@news20.bellglobal.com> <3abe9a98.32492859@news1.attglobal.net>`

```
I DO know because I do it regularly....

You can call COBOL 97 from PowerCOBOL without problem, but you must compile
the COBOL 97 to .DLL.

Going the other way (calling PowerCOBOL from COBOL 97) can also be achieved
but an interface module must be used, and when I tried it, it didn't work.
Fujitsu tell me it is corrected in Version 6.

On occasions when I need certain compiler directives which I DON'T want to
apply to the whole of my PowerCOBOL I do exactly what Don suggested,
compile a COBOL 97 subroutine with the compiler directives I want (a prime
example is calling the Windows API where the COBOL directive ALPHAL(WORD) is
needed, but it ISN'T needed with anything else you call.)

The other comments which have been made are the opinions of someone who is
unfamiliar with the product.  I can't believe the mountain which has been
made out of this particular molehill... but I've been using PowerCOBOL for 3
years now. It is familiar and easy. I accept that people coming new to it
will see problems. That doesn't mean there ARE any...<G> Wall?! What wall?!
....

Pete.

Thane Hubbell wrote in message <3abe9a98.32492859@news1.attglobal.net>...
>I don't KNOW, but I have seen it documented that you can call
>"regular" COBOL programs from PowerCOBOL.  And I do know that
…[14 more quoted lines elided]…
>>>









-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

_(reply depth: 4)_

- **From:** Rob Lec <RobLec@cinci-rr.com>
- **Date:** 2001-03-26T04:19:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABEC32D.5E20639A@cinci-rr.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com> <acvv6.458998$f36.14556065@news20.bellglobal.com>`

```

Donald Tees wrote:
> 
> Rob, this might sound a bit weird, but could you not just write a Cobol97
…[3 more quoted lines elided]…
> 

No, not at all 'wierd'.  This was another one of the options I had
considered, but it would again unnecessarily complicate the application
by adding additional modules to maintain.  In fact, this whole thing
came up when I tried to move the code entirely from Fujitsu COBOL97 to
Fujitsu PowerCOBOL.  Everything worked fine in COBOL97 (with inline
directives) but when I moved it to PowerCOBOL, each record somehow lost
several bytes of data.  Oddly enough, the lost bytes appeared to occur
in pairs and always followed a date field (Hmmm).  The nature of the
problem quickly became obvious. 

>
> "Rob LeClaire" <RobLec@cinci-rr.com> wrote in message
…[9 more quoted lines elided]…
> > (To reply by email change dash to dot in address)
 
-------------------------------------------------
(To reply by email change dash to dot in address)
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-03-26T22:50:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abf1ed7_2@news.newsfeeds.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com> <acvv6.458998$f36.14556065@news20.bellglobal.com> <3ABEC32D.5E20639A@cinci-rr.com>`

```
Comments in line...

Rob Lec wrote in message <3ABEC32D.5E20639A@cinci-rr.com>...
>
>Donald Tees wrote:
>>
>> Rob, this might sound a bit weird, but could you not just write a Cobol97
>> subroutine to do the job, then call it from PowerCobol?  I think you
*can*
>> set in-line directives in a subroutine .. Thane would know the answer to
>> that.
…[4 more quoted lines elided]…
>by adding additional modules to maintain.

Well, sometimes there's a price to be paid for migrating...


>In fact, this whole thing
>came up when I tried to move the code entirely from Fujitsu COBOL97 to
…[5 more quoted lines elided]…
>

You are working with OTHER files as well as BTRIEVE, right? That's why you
can't specify the directive Globally in the Script Compiler Directives?

>>
>> "Rob LeClaire" <RobLec@cinci-rr.com> wrote in message
…[5 more quoted lines elided]…
>> > flames and arrows will follow...)  Above all, COBOL source code
*should*
>> > be CLEAR and easily understood.


No flames and arrows. You are entitled to your opinion.

Are you actually saying that the code you write in PowerCOBOL is NOT clear
and easily understood? When you look at an event procedure or a common
procedure in PowerCOBOL they are somehow DIFFERENT to the crystal code you
would write outside the PowerCOBOL environment?

My version of PowerCOBOL doesn't do that... (It's the same old crap no
matter where I write it...<G>)

As Michael is famous for reminding us..."It's NOT the paintbrush, it's the
Artist..."

Pete.






-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

_(reply depth: 6)_

- **From:** Rob Lec <RobLec@cinci-rr.com>
- **Date:** 2001-03-26T14:59:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABF5957.2D6C2F22@cinci-rr.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com> <acvv6.458998$f36.14556065@news20.bellglobal.com> <3ABEC32D.5E20639A@cinci-rr.com> <3abf1ed7_2@news.newsfeeds.com>`

```


"Peter E. C. Dashwood" wrote:
> but it would again unnecessarily complicate the application
> >by adding additional modules to maintain.
> 
> Well, sometimes there's a price to be paid for migrating...
>
  If a single line of code can eliminate having an additional source
file, library, and DLL (not to mention all the intermediate files the
compiler produces), then I would certainly choose that one line.  

> > Everything worked fine in COBOL97 (with inline
> >directives) but when I moved it to PowerCOBOL, each record somehow lost
…[3 more quoted lines elided]…
> can't specify the directive Globally in the Script Compiler Directives?

The 'script compiler directives' was exactly what I was asking for in my
original post.  Please note that I already knew which directive to use
but had not yet 'discovered' where it should be specified.  (Incidently,
I later ran across a note which I had made in the manual about right
clicking on the script branch.)  If someone with your level of
experience had merely mentioned that, then most of this thread would
have been unnecessary.  But then we would have missed the valuable and
pertinent info from Bill and Thane.  That's what this NG is for, right?

> 
>>  Above all, COBOL source code *should* be CLEAR and easily understood.
> 

That's the whole point of COBOL.  If we wanted to write clever, cryptic
code then we would be using some other language.

> Are you actually saying that the code you write in PowerCOBOL is NOT clear
> and easily understood? When you look at an event procedure or a common
> procedure in PowerCOBOL they are somehow DIFFERENT to the crystal code you
> would write outside the PowerCOBOL environment?

PowerCOBOL has the same characteristic of all visual IDE's.  The code is
neatly organized in three distinct areas: here, there, and everywhere. 
Personally I would rather work with a single comprehensive source file
rather than having it scattered among dozens of windows.  But that's
merely my preference.  Actually I like this product, but I'm grateful to
have had some prior experience with VB & VC before trying to move my
code from COBOL97 to PowerCOBOL.

Please realize that I have only been using the Fujitsu compilers for
about six weeks now.  Forgive me if I do not yet have the familiarity
with the product which you have.  This all began with a fairly simple
question.  

-------------------------------------------------
(To reply by email change dash to dot in address)
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

_(reply depth: 7)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-03-27T04:17:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tvUv6.16385$ue1.1384656@newsread2.prod.itd.earthlink.net>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com> <acvv6.458998$f36.14556065@news20.bellglobal.com> <3ABEC32D.5E20639A@cinci-rr.com> <3abf1ed7_2@news.newsfeeds.com> <3ABF5957.2D6C2F22@cinci-rr.com>`

```

"Rob Lec" <RobLec@cinci-rr.com

>  But then we would have missed the valuable and
> pertinent info from Bill and Thane.  That's what this NG is for,
right?
>
Hey! I contributed too.
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

_(reply depth: 8)_

- **From:** Rob Lec <RobLec@cinci-rr.com>
- **Date:** 2001-03-27T04:34:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AC0183C.C5EEAD1@cinci-rr.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com> <acvv6.458998$f36.14556065@news20.bellglobal.com> <3ABEC32D.5E20639A@cinci-rr.com> <3abf1ed7_2@news.newsfeeds.com> <3ABF5957.2D6C2F22@cinci-rr.com> <tvUv6.16385$ue1.1384656@newsread2.prod.itd.earthlink.net>`

```
Oops! Yes you did, and the omission was certainly not intentional!
If I mention everyone, this could turn into another Oscar ceremony.
(Actually I think it was Peter's replies that did the most to perpetuate
this thread).

Jerry P wrote:
> 
> "Rob Lec" <RobLec@cinci-rr.com
…[5 more quoted lines elided]…
> Hey! I contributed too.
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

_(reply depth: 9)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-03-27T17:07:00+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ac01fc6_6@news.newsfeeds.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com> <acvv6.458998$f36.14556065@news20.bellglobal.com> <3ABEC32D.5E20639A@cinci-rr.com> <3abf1ed7_2@news.newsfeeds.com> <3ABF5957.2D6C2F22@cinci-rr.com> <tvUv6.16385$ue1.1384656@newsread2.prod.itd.earthlink.net> <3AC0183C.C5EEAD1@cinci-rr.com>`

```
Don't blame me for it...I'm outta here...!

Pete

Rob Lec wrote in message <3AC0183C.C5EEAD1@cinci-rr.com>...
>Oops! Yes you did, and the omission was certainly not intentional!
>If I mention everyone, this could turn into another Oscar ceremony.
>(Actually I think it was Peter's replies that did the most to perpetuate
>this thread).
>




-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

_(reply depth: 7)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-03-27T17:04:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ac01fbe_6@news.newsfeeds.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com> <acvv6.458998$f36.14556065@news20.bellglobal.com> <3ABEC32D.5E20639A@cinci-rr.com> <3abf1ed7_2@news.newsfeeds.com> <3ABF5957.2D6C2F22@cinci-rr.com>`

```

Rob Lec wrote in message <3ABF5957.2D6C2F22@cinci-rr.com>...
>
>If someone with your level of experience had merely mentioned that, then
most of this thread
>would have been unnecessary.  But then we would have
missed the valuable and
>pertinent info from Bill and Thane.  That's what this NG is for, right?
>
Three mistakes here, Rob.

1. Neither I, nor others here with equivalent experience, are OBLIGED to
give anyone advice (especially when they're not paying for it...<G>). There
is NO God Given right on the part of people posting here to EXPECT someone
to help them.

As a consultant, I make my living by giving advice, and what I post here is
a few free samples...(And they're probably worth the price...<G>)

I reserve the right to decide for myself what I'll respond to, and what I
won't. Trivial problems which are solved in minutes with a little thought
don't normally get my attention.

On the very rare occasions when I need advice, I pay for it. Or I trade for
it. I don't EXPECT people in forums to give it to me for nothing. Obviously,
kids starting out in COBOL are a different case, but you have 20 years
experience.

The only reason I post here at all is because I want to give something back
for the
help and guidance I have received over the years (and sometimes it is fun
too...). But don't impose on my good nature...<G>  Your comment is way out
of line.

2. If you had "done your homework" you would've found the solution, as
indeed you did, when "help" was not forthcoming. You are now wiser and more
accomplished for having done it yourself.

3. Although it may seem like it sometimes <G>, this NG is NOT here so Bill
and Thane (or any of us) can post "valuable and pertinent advice" (yeah,
right!). This NG is here because  a bunch of people share a common interest
in COBOL and because somebody makes money every time you or I post to it or
look at it.  It continues because enough people have a vested interest in it
to ensure that it does. If it isn't viable it will disappear like snow in
July...

This thread is closed as far as I'm concerned. (It should have been days
ago).

Pete.







-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

_(reply depth: 8)_

- **From:** Rob Lec <RobLec@cinci-rr.com>
- **Date:** 2001-03-27T14:19:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AC0A14A.9BE037F2@cinci-rr.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com> <acvv6.458998$f36.14556065@news20.bellglobal.com> <3ABEC32D.5E20639A@cinci-rr.com> <3abf1ed7_2@news.newsfeeds.com> <3ABF5957.2D6C2F22@cinci-rr.com> <3ac01fbe_6@news.newsfeeds.com>`

```

Excuse me, I seem to have stumbled into the wrong forum.

Please direct me to the newsgroup for those of us who
are not yet experts on every vendor's product.

-------------------------------------------------
(To reply by email change dash to dot in address)
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

_(reply depth: 8)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-03-27T15:18:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ta2w6.94$pV5.76089@paloalto-snr1.gtei.net>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com> <acvv6.458998$f36.14556065@news20.bellglobal.com> <3ABEC32D.5E20639A@cinci-rr.com> <3abf1ed7_2@news.newsfeeds.com> <3ABF5957.2D6C2F22@cinci-rr.com> <3ac01fbe_6@news.newsfeeds.com>`

```
You'd make a crummy Communist, Pete.
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

_(reply depth: 9)_

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-03-28T11:15:35+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ac121e6_1@my.newsfeeds.com>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com> <acvv6.458998$f36.14556065@news20.bellglobal.com> <3ABEC32D.5E20639A@cinci-rr.com> <3abf1ed7_2@news.newsfeeds.com> <3ABF5957.2D6C2F22@cinci-rr.com> <3ac01fbe_6@news.newsfeeds.com> <Ta2w6.94$pV5.76089@paloalto-snr1.gtei.net>`

```

Michael Mattias wrote in message ...
>You'd make a crummy Communist, Pete.
>
Hahaha!

"From each according to his ability, to each, according to his needs." -
Karl Marx

A wonderful idea. No problem with it as long as the "need" is real and not
pretended, in order to get a handout...

Besides, I stand on my track record. And I have the "thank you"s on
file...<G>

Dammit, Michael, you've conned me into posting to this thread again... I
guess religion and politics are two things that are very hard to resist when
it comes to debate...

Pete.




-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

###### ↳ ↳ ↳ Re: Fuji Power Cobol Byte Alignment ??

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-03-26T01:25:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abe9a5c.32432931@news1.attglobal.net>`
- **References:** `<3AB945F5.90CA9005@cinci-rr.com> <3abcc2c7.299599779@news1.attglobal.net> <3ABE23AC.6B6DECCF@cinci-rr.com>`

```
On Sun, 25 Mar 2001 21:56:58 GMT, Rob LeClaire <RobLec@cinci-rr.com>
wrote:


>Let me guess ... it produces a 3-byte field, right?  I am assuming that
>Fujitsu defaults to NOTRUNC and therefore allows a full 65,536 range of
>values for a 9(4)comp field.  If you've found otherwise, please let me
>know so I don't have to stumble across this by accident!
>

Right on the length, wrong on the default of Truncation.  NOTRUNC is
NOT the default.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
