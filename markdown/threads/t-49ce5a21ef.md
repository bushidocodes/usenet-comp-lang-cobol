[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Looking for address parsing code

_9 messages · 9 participants · 2003-08 → 2004-02_

---

### Looking for address parsing code

- **From:** "Simeon Nevel" <snevel@sonic.net>
- **Date:** 2003-08-22T18:49:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RAt1b.14270$dk4.497898@typhoon.sonic.net>`

```
Hi All..

I've a new project at work where I need to parse a free-format address
line into the pieces necessary to do a Zip+4 lookup.

Does anyone know if there is a product (commercial or otherwise) that
will do the parsing and/or the Zip+4 assignment.

I feel I can make a good case w/ my management to buy a solution rather
than spend months interpreting US Postal regulations and re-inventing the
wheel.

For those who know the postal biz, the eventual goal is CASS (Coding
Accuracy Support System) certification.

Clues gratefully accepted.

adTHANKSvance!

Simeon
```

#### ↳ Re: Looking for address parsing code

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-08-22T14:54:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B1qdnedyg9eS6NuiXTWJkA@giganews.com>`
- **References:** `<RAt1b.14270$dk4.497898@typhoon.sonic.net>`

```
Simeon Nevel wrote:
> Hi All..
>
…[13 more quoted lines elided]…
> Clues gratefully accepted.

If it were easy, everyone would be doing it and there would be no need for
the three or four companies in the field.

The pitfalls are too numerous to count (is "St." an abbreviation for "Saint"
as in St. Lewis, or for "Street"? How many abbreviations can you think of
for "Boulevard"?)

Also, you can't just DO it; you have to keep DOING it. That is, your
software must undergo periodic re-certification by the USPS. Using a
commercial product, the certified updates come to you as part of your annual
maintenance.

But, look at your end goal. If the end result is save money on mailings, you
might be WAY ahead to farm the whole thing out to a mailing service. The
mailing service can give you back your addresses already parsed into the
fields you want.

This won't do you any good for future mailings, though, because your mailing
software won't be certified by USPS. But you will have a cleaned list.
```

#### ↳ Re: Looking for address parsing code

- **From:** "Anon" <anon@anon.org>
- **Date:** 2003-08-22T16:29:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4_-cnZ37c7OgFtuiXTWQkQ@giganews.com>`
- **References:** `<RAt1b.14270$dk4.497898@typhoon.sonic.net>`

```
On my last job we used a product called Code-1 Plus from
"Group 1 Software". Type in "Code-1" on Google. It
worked pretty well on some pretty screwed up input
addresses returning USPS valid addresses. It ain't
cheap however. Good Luck.
```

#### ↳ Re: Looking for address parsing code

- **From:** Frank Swarbrick<Frank.Swarbrick@efirstbank.com>
- **Date:** 2003-08-22T17:04:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bi67hj$5p2ql$1@ID-184804.news.uni-berlin.de>`
- **References:** `<RAt1b.14270$dk4.497898@typhoon.sonic.net>`

```
Code 1 Plus from Group 1 Software:
http://www.g1.com/solutions/ds.asp?DS_ID=17&Category_ID=1

It's a pretty complex and huge system, but seems to work quite well.  But I
find it highly unlikely you'd come even close to doing it well building such
a thing in-house.


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications Development
FirstBank Data Corporation

>>> Simeon Nevel<snevel@sonic.net> 08/22/03 12:49PM >>>
Hi All..

I've a new project at work where I need to parse a free-format address
line into the pieces necessary to do a Zip+4 lookup.

Does anyone know if there is a product (commercial or otherwise) that
will do the parsing and/or the Zip+4 assignment.

I feel I can make a good case w/ my management to buy a solution rather
than spend months interpreting US Postal regulations and re-inventing the
wheel.

For those who know the postal biz, the eventual goal is CASS (Coding
Accuracy Support System) certification.

Clues gratefully accepted.

adTHANKSvance!

Simeon
```

#### ↳ Re: Looking for address parsing code

- **From:** "ShadowFox" <me@email.com>
- **Date:** 2003-08-23T12:28:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16J1b.178456$Oz4.48097@rwcrnsc54>`
- **References:** `<RAt1b.14270$dk4.497898@typhoon.sonic.net>`

```
First logic has a desktop mailing software program that will do all that you
need. Also if you don't want to spend the money or setup and run the
software there are plenty of business out there tath will do it for you
www.computerfulfillment.com
Enjoy Bob
"Simeon Nevel" <snevel@sonic.net> wrote in message
news:RAt1b.14270$dk4.497898@typhoon.sonic.net...
> Hi All..
>
…[19 more quoted lines elided]…
>
```

#### ↳ Re: Looking for address parsing code

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-23T12:48:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eoJ1b.110516$3o3.7768415@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<RAt1b.14270$dk4.497898@typhoon.sonic.net>`

```

"Simeon Nevel" <snevel@sonic.net> wrote in message
news:RAt1b.14270$dk4.497898@typhoon.sonic.net...
| Hi All..
|
…[4 more quoted lines elided]…
| will do the parsing and/or the Zip+4 assignment.

I know of 2, Code-1 from Group 1, and Finalist.
There are probably others, they may be listed at USPS web site.
|
| I feel I can make a good case w/ my management to buy a solution rather
…[4 more quoted lines elided]…
| Accuracy Support System) certification.

If you develop your own solution, you will have to pass the CASS
certification.
That will mean having the Post Office do a QA on your solution.

You will also want to look into Bar Coding of the Zip Code.
```

#### ↳ Re: Looking for address parsing code

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-08-25T06:14:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0308250514.4b013fe6@posting.google.com>`
- **References:** `<RAt1b.14270$dk4.497898@typhoon.sonic.net>`

```
Simeon,

melissadata.com has something called "Address Object".  It's
competively priced and is an OLE server.  I use it with Sp2 and any of
the PC COBOL's you care to imagine.  If you are on the mainframe, I
suggest CODE1 - or you can actually (with my help!) make use of the
Address Object running on a PC attached via TCP/IP so the mainframe
can see it.  Email me at thane at softwaresimple.com if you want some
consulting assistance on this.


"Simeon Nevel" <snevel@sonic.net> wrote in message news:<RAt1b.14270$dk4.497898@typhoon.sonic.net>...
> Hi All..
> 
…[17 more quoted lines elided]…
> Simeon
```

#### ↳ Re: Looking for address parsing code

- **From:** "ChangizW" <NOMAIL@yahoo.com>
- **Date:** 2003-08-25T10:13:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bid5ad02eio@enews4.newsguy.com>`
- **References:** `<RAt1b.14270$dk4.497898@typhoon.sonic.net>`

```
Look into "Group 1 Software" solutions. They support all IBM platforms, most
of UNIX, NT, web services, etc... They have US, Canada, and almost every
country with formal postal services.

www.g1.com



"Simeon Nevel" <snevel@sonic.net> wrote in message
news:RAt1b.14270$dk4.497898@typhoon.sonic.net...
> Hi All..
>
…[19 more quoted lines elided]…
>
```

#### ↳ Re: Looking for address parsing code

- **From:** kunal_sahay <member@mainframeforum.com>
- **Date:** 2004-02-26T06:50:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12491ccefbd490f57d9e89bf4eea667a@news.onlynews.com>`
- **References:** `<RAt1b.14270$dk4.497898@typhoon.sonic.net>`

```
Andrea Bizzocchi  wrote:
  > hello!! I would like to know if exist a utility to convert cobol/cics
  > back into VISUALAGE IBM for java (esf file) If possible free. Thanks
  > in advance.
as you've been replied, you can use the CODE1 software. i've used it for
address parsing in one of my projects and found it very effective. it
also searches for the closest match. it is called as C1MATCHS also.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
