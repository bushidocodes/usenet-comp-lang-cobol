[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Read Back in Cobol (microsoft 4.0)

_13 messages · 7 participants · 1997-11_

---

### Read Back in Cobol (microsoft 4.0)

- **From:** "mpns..." <ua-author-17071264@usenetarchives.gap>
- **Date:** 1997-11-18T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64th7i$1ag$2@rjo03.embratel.net.br>`

```

Does Anyone know how can I read back a record in microsoft 4.0 ?


select file1 assign to disk
organization is indexed
access mode is dynamic
record key is key-1
file status is ...


read-forward.
read file1 next ..........




read-backward.
? ? ? ?


The file can be Indexed , Line sequential or sequential , doen't matter.

Thanks in advance !

J. Monteiro
Brasil
```

#### ↳ Re: Read Back in Cobol (microsoft 4.0)

- **From:** "bi..." <ua-author-8405640@usenetarchives.gap>
- **Date:** 1997-11-17T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad007eb65d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<64th7i$1ag$2@rjo03.embratel.net.br>`
- **References:** `<64th7i$1ag$2@rjo03.embratel.net.br>`

```

In article <64th7i$1ag$2.··.@rjo··t.br>,
"mpn··.@emb··t.br (Username) wrote:
› Does Anyone know how can I read back a record in microsoft 4.0 ?
› 
…[23 more quoted lines elided]…
› Brasil

It is:

READ FILE1 PREVIOUS RECORD

That's the good news; the bad news is that IT DOES MATTER, as you can only do
this with relative and indexed files and it is a MicroFocus extension. I am
assuming here that the MS COBOL 4.0 is similiar enough to MF COBOL 3.2 for the
above to be true. (I don't have any docs for the older MS compiler.)
```

##### ↳ ↳ Re: Read Back in Cobol (microsoft 4.0)

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-18T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad007eb65d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad007eb65d-p2@usenetarchives.gap>`
- **References:** `<64th7i$1ag$2@rjo03.embratel.net.br> <gap-ad007eb65d-p2@usenetarchives.gap>`

```

William Murray wrote:
› J. Monteiro mpn··.@emb··t.br wrote:
›› Does Anyone know how can I read back a record in microsoft 4.0 ?
…[24 more quoted lines elided]…
› the above to be true.  (I don't have any docs for the older MS compiler.)

You are correct. As you appear to know, the Microsoft COBOL compilers,
starting with 3.0, were MS adaptations of Micro Focus COBOL, and do support
PREVIOUS as you describe. MS COBOL 2.0, evidently an in-house compiler, did
not support PREVIOUS; I don't know about version 1. Microsoft quit marketing
their COBOL compiler after version 5.0.

It is amazing to me that something as obviously valuable and needed as READ
PREVIOUS has not been included in the ANSI COBOL standard. For example, it
is extremely useful in enabling users to page backward and forward through a
list of names or other sequential keys in an indexed file. Don't leave home
without it!
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: Read Back in Cobol (microsoft 4.0)

- **From:** "donts..." <ua-author-8744626@usenetarchives.gap>
- **Date:** 1997-11-18T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad007eb65d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad007eb65d-p3@usenetarchives.gap>`
- **References:** `<64th7i$1ag$2@rjo03.embratel.net.br> <gap-ad007eb65d-p2@usenetarchives.gap> <gap-ad007eb65d-p3@usenetarchives.gap>`

```

On 19 Nov 1997 11:24:19 GMT, "Judson D. McClendon"
wrote:

› It is amazing to me that something as obviously valuable and needed as READ
› PREVIOUS has not been included in the ANSI COBOL standard.  For example, it
› is extremely useful in enabling users to page backward and forward through a
› list of names or other sequential keys in an indexed file.  Don't leave home
› without it.
My DEC COBOL manual does not show READ PREVIOUS as an extension so it
may very well be part of the standard.

George Trudeau
```

###### ↳ ↳ ↳ Re: Read Back in Cobol (microsoft 4.0)

_(reply depth: 4)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-18T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad007eb65d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad007eb65d-p4@usenetarchives.gap>`
- **References:** `<64th7i$1ag$2@rjo03.embratel.net.br> <gap-ad007eb65d-p2@usenetarchives.gap> <gap-ad007eb65d-p3@usenetarchives.gap> <gap-ad007eb65d-p4@usenetarchives.gap>`

```

George Trudeau wrote:
› 
› Judson D. McClendon  wrote:
…[12 more quoted lines elided]…
› may very well be part of the standard.

George, I would love to be proven wrong on this one. But my ANSI COBOL 85
standards book does not list PREVIOUS as part of the READ syntax, and
PREVIOUS is not listed as a reserved word.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: Read Back in Cobol (microsoft 4.0)

_(reply depth: 4)_

- **From:** "bgwi..." <ua-author-599269@usenetarchives.gap>
- **Date:** 1997-11-19T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad007eb65d-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad007eb65d-p4@usenetarchives.gap>`
- **References:** `<64th7i$1ag$2@rjo03.embratel.net.br> <gap-ad007eb65d-p2@usenetarchives.gap> <gap-ad007eb65d-p3@usenetarchives.gap> <gap-ad007eb65d-p4@usenetarchives.gap>`

```

don··.@roc··l.com (George Trudeau) wrote:

› On 19 Nov 1997 11:24:19 GMT, "Judson D. McClendon"
› wrote:
…[9 more quoted lines elided]…
› George Trudeau

I looked at my "IBM COBOL for MVS & VM Language Reference"
(SC26-4769-01) and found READ PREVIOUS on page 354. However, it's
good only on the AIX and OS/2 platforms. For the rest, we have to do
it the hard way.

Boyce G. Williams, Jr.

.--------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a|
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon|
'--------------------------------------------------------------------'
```

###### ↳ ↳ ↳ Re: Read Back in Cobol (microsoft 4.0)

_(reply depth: 4)_

- **From:** "bgwi..." <ua-author-599269@usenetarchives.gap>
- **Date:** 1997-11-19T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad007eb65d-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad007eb65d-p4@usenetarchives.gap>`
- **References:** `<64th7i$1ag$2@rjo03.embratel.net.br> <gap-ad007eb65d-p2@usenetarchives.gap> <gap-ad007eb65d-p3@usenetarchives.gap> <gap-ad007eb65d-p4@usenetarchives.gap>`

```

don··.@roc··l.com (George Trudeau) wrote:

› On 19 Nov 1997 11:24:19 GMT, "Judson D. McClendon"
› wrote:
…[9 more quoted lines elided]…
› George Trudeau

As an add-on on in my previous post: can one sort the keys (in a
seperate second field, of course) in decending order and load them as
an alternate key to serve as the reverse key sequence. That way one
only has to change the record of focus from the primary to alternate
then READ NEXT on the alternate key.

Has anyone thought of the idea?

Boyce G. Williams, Jr.

.--------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a|
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon|
'--------------------------------------------------------------------'
```

###### ↳ ↳ ↳ Re: Read Back in Cobol (microsoft 4.0)

_(reply depth: 5)_

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-11-27T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad007eb65d-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad007eb65d-p7@usenetarchives.gap>`
- **References:** `<64th7i$1ag$2@rjo03.embratel.net.br> <gap-ad007eb65d-p2@usenetarchives.gap> <gap-ad007eb65d-p3@usenetarchives.gap> <gap-ad007eb65d-p4@usenetarchives.gap> <gap-ad007eb65d-p7@usenetarchives.gap>`

```



Boyce G. Williams, Jr. wrote in article
<347··.@use··u.edu>...
› don··.@roc··l.com (George Trudeau) wrote:
› 
…[24 more quoted lines elided]…
› 

Sort of. We re-defined the key field as numeric binary and multiplied by
-1.
There are some problems with the approach (zero keys etc) but for the most
part it worked.
```

###### ↳ ↳ ↳ Re: Read Back in Cobol (microsoft 4.0)

_(reply depth: 4)_

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-11-27T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad007eb65d-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad007eb65d-p4@usenetarchives.gap>`
- **References:** `<64th7i$1ag$2@rjo03.embratel.net.br> <gap-ad007eb65d-p2@usenetarchives.gap> <gap-ad007eb65d-p3@usenetarchives.gap> <gap-ad007eb65d-p4@usenetarchives.gap>`

```



George Trudeau wrote in article
<347··.@new··e.com>...
› On 19 Nov 1997 11:24:19 GMT, "Judson D. McClendon"
›  wrote:
…[12 more quoted lines elided]…
› 

It is not part of the '85 standard. It is considered in the '97 - '00
standard.

Most PC compilers implement it in some method - Fujitsu via the PREVIOUS,
Realia - via PRIOR.
```

###### ↳ ↳ ↳ Re: Read Back in Cobol (microsoft 4.0)

- **From:** "pa..." <ua-author-6589140@usenetarchives.gap>
- **Date:** 1997-11-18T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad007eb65d-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad007eb65d-p3@usenetarchives.gap>`
- **References:** `<64th7i$1ag$2@rjo03.embratel.net.br> <gap-ad007eb65d-p2@usenetarchives.gap> <gap-ad007eb65d-p3@usenetarchives.gap>`

```

Re: read previous.

There is a mthod you can use of course. Simple restart the file from the
current record *in reverse*, which is in the COBOL-85 standard.

A couple more lines of code of course, but then again, it is optimized
very nicely by most compilers anyway.

I would prefer read previous myself, but reversing the file direction
is not onerous.

-Paul


Judson D. McClendon (jud··.@min··g.com) wrote:
: William Murray wrote:
: > J. Monteiro mpn··.@emb··t.br wrote:
: > > Does Anyone know how can I read back a record in microsoft 4.0 ?
: > >
: > > select file1 assign to disk
: > > organization is indexed
: > > access mode is dynamic
: > > record key is key-1
: > > file status is ...
: > >
: > > read-forward.
: > > read file1 next ..........
: > >
: > > read-backward.
: > > ? ? ? ?
: > >
: > > The file can be Indexed , Line sequential or sequential , doen't matter.
: >
: > It is:
: >
: > READ FILE1 PREVIOUS RECORD
: >
: > That's the good news; the bad news is that IT DOES MATTER, as you can only
: do
: > this with relative and indexed files and it is a MicroFocus extension. I
: am
: > assuming here that the MS COBOL 4.0 is similiar enough to MF COBOL 3.2 for
: > the above to be true. (I don't have any docs for the older MS compiler.)

: You are correct. As you appear to know, the Microsoft COBOL compilers,
: starting with 3.0, were MS adaptations of Micro Focus COBOL, and do support
: PREVIOUS as you describe. MS COBOL 2.0, evidently an in-house compiler, did
: not support PREVIOUS; I don't know about version 1. Microsoft quit marketing
: their COBOL compiler after version 5.0.

: It is amazing to me that something as obviously valuable and needed as READ
: PREVIOUS has not been included in the ANSI COBOL standard. For example, it
: is extremely useful in enabling users to page backward and forward through a
: list of names or other sequential keys in an indexed file. Don't leave home
: without it!
: --
: Judson McClendon This is a faithful saying and worthy of all
: Sun Valley Systems acceptance, that Christ Jesus came into the
: jud··.@min··g.com world to save sinners (1 Timothy 1:15)
: (please remove zzz from email id to respond)
```

###### ↳ ↳ ↳ Re: Read Back in Cobol (microsoft 4.0)

_(reply depth: 4)_

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-11-18T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad007eb65d-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad007eb65d-p10@usenetarchives.gap>`
- **References:** `<64th7i$1ag$2@rjo03.embratel.net.br> <gap-ad007eb65d-p2@usenetarchives.gap> <gap-ad007eb65d-p3@usenetarchives.gap> <gap-ad007eb65d-p10@usenetarchives.gap>`

```

The ANSI standard COBOL 85 START verb doesn't have a 'reverse' option. The
word REVERSE is not a reserved word, and REVERSED is only used with OPEN
INPUT.

If you are referring to OPEN INPUT REVERSED, that is good only for
sequential, not indexed files, and only good for input files, and only starts
from the end of the file, and is scheduled to be dropped from the next COBOL
standard.

If you are referring to something else, I don't know what you mean.
```

#### ↳ Re: Read Back in Cobol (microsoft 4.0)

- **From:** "bgwi..." <ua-author-599269@usenetarchives.gap>
- **Date:** 1997-11-18T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad007eb65d-p12@usenetarchives.gap>`
- **In-Reply-To:** `<64th7i$1ag$2@rjo03.embratel.net.br>`
- **References:** `<64th7i$1ag$2@rjo03.embratel.net.br>`

```

"mpn··.@emb··t.br (Username) wrote:

› Does Anyone know how can I read back a record in microsoft 4.0 ?
› 
…[23 more quoted lines elided]…
› Brasil

As far as I know, one cannot read a VSAM (or ISAM since you're on a
PC) file backwards in batch mode with a command. MS-COBOL, like Micro
Focus, uses the same syntax core as mainframe COBOL for compatability.
You'll need to set your key back by program logic then READ again.
Now if you're using CICS, that's a different story.

Anyone has a difference experience?

Boyce G. Williams, Jr.

.--------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a|
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon|
'--------------------------------------------------------------------'
```

##### ↳ ↳ Re: Read Back in Cobol (microsoft 4.0)

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-11-27T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ad007eb65d-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ad007eb65d-p12@usenetarchives.gap>`
- **References:** `<64th7i$1ag$2@rjo03.embratel.net.br> <gap-ad007eb65d-p12@usenetarchives.gap>`

```



Boyce G. Williams, Jr. wrote in article
› As far as I know, one cannot read a VSAM (or ISAM since you're on a
› PC) file backwards in batch mode with a command.  MS-COBOL, like Micro
…[5 more quoted lines elided]…
› 

We always created reverse key file alternate indexes for reading backward
in batch.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
