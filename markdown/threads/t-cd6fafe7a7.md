[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DB2 to COBOL translation

_9 messages · 5 participants · 2003-09_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### DB2 to COBOL translation

- **From:** "Gonzo" <ckhamel1961.nospam@yahoo.com>
- **Date:** 2003-09-11T16:31:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%r18b.88$iT5.27@newssvr24.news.prodigy.com>`

```
Hi folks,

I was given a DB2 layout without the benefit of a DCLGEN translation, and
I've got field definition of DECIMAL(22,7). How would you change this to a
COBOL PIC? I'm working with COBOL OS/390, and according to the doc I have,
the rule is supposed to be:

DECIMAL(p,s)      ->     PIC S9(p-s)V9(s) COMP-3.

As I plug it in, I obviously get PIC S9(15)V9(7) COMP-3. My maximum length
for COMP-3 fields is 18 digit positions, and I bust that by 4 positions.

I was just going to pad the first two bytes as filler and handle the excess
in the procedure division, but I was hoping someone might have another idea
at hand.
```

#### ↳ Re: DB2 to COBOL translation

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-11T18:01:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VL28b.134971$0v4.9877829@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<%r18b.88$iT5.27@newssvr24.news.prodigy.com>`

```

"Gonzo" <ckhamel1961.nospam@yahoo.com> wrote in message
news:%r18b.88$iT5.27@newssvr24.news.prodigy.com...
| Hi folks,
|
…[10 more quoted lines elided]…
| I was just going to pad the first two bytes as filler and handle the
excess
| in the procedure division, but I was hoping someone might have another
idea
| at hand.

Operating system, compiler & version would be helpful.
```

#### ↳ Re: DB2 to COBOL translation

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-11T18:07:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UR28b.134977$0v4.9878087@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<%r18b.88$iT5.27@newssvr24.news.prodigy.com>`

```
TOP Post ONLY:

do you have ARITH(EXTEND) in your manual?

"Gonzo" <ckhamel1961.nospam@yahoo.com> wrote in message
news:%r18b.88$iT5.27@newssvr24.news.prodigy.com...
| Hi folks,
|
…[10 more quoted lines elided]…
| I was just going to pad the first two bytes as filler and handle the
excess
| in the procedure division, but I was hoping someone might have another
idea
| at hand.
|
…[5 more quoted lines elided]…
|
```

##### ↳ ↳ Re: DB2 to COBOL translation

- **From:** "Gonzo" <ckhamel1961.nospam@yahoo.com>
- **Date:** 2003-09-12T14:47:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o0l8b.283$rS3.165@newssvr24.news.prodigy.com>`
- **References:** `<%r18b.88$iT5.27@newssvr24.news.prodigy.com> <UR28b.134977$0v4.9878087@bgtnsc04-news.ops.worldnet.att.net>`

```

"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote:
>
> do you have ARITH(EXTEND) in your manual?
>

Sorry, ARITH is not available to me on this version. Sounds like just what I
needed, tho...

> "Gonzo" <ckhamel1961.nospam@yahoo.com> wrote:
> | I'm working with COBOL OS/390, <snip>

Pardon me, I get a little too focused sometimes....

I'm working with IBM COBOL for MVS & VM 1.2.2, operating on an IBM OS/390
MVS system.
```

###### ↳ ↳ ↳ Re: DB2 to COBOL translation

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-12T20:20:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZTp8b.480$Aq2.81@newsread1.news.atl.earthlink.net>`
- **References:** `<%r18b.88$iT5.27@newssvr24.news.prodigy.com> <UR28b.134977$0v4.9878087@bgtnsc04-news.ops.worldnet.att.net> <o0l8b.283$rS3.165@newssvr24.news.prodigy.com>`

```
Then you are out of luck, and need to "discuss" with your software support
people WHY they have upgraded to a version of DB2 that supports 31-digit
numeric fields but have NOT updated your COBOL to such a release.
```

###### ↳ ↳ ↳ Re: DB2 to COBOL translation

_(reply depth: 4)_

- **From:** "Gonzo" <ckhamel1961.nospam@yahoo.com>
- **Date:** 2003-09-12T23:07:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1ls8b.406$_15.145@newssvr24.news.prodigy.com>`
- **References:** `<%r18b.88$iT5.27@newssvr24.news.prodigy.com> <UR28b.134977$0v4.9878087@bgtnsc04-news.ops.worldnet.att.net> <o0l8b.283$rS3.165@newssvr24.news.prodigy.com> <ZTp8b.480$Aq2.81@newsread1.news.atl.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote:
> Then you are out of luck, <snip>

Yep, Bill... fortunately just OOL and not SOL.... for the moment. Writing
specs for a conversion, and right now it's just a straight move. Hopefully
it'll stay that way, otherwise I'm in for some extra coding.

Contracting means you take what they give ya.... 'tis a good question,
though, why they haven't updated their compiler. My client is so big I doubt
I'd ever find the right person to ask in the timeframe I have, much less do
anything about it.

Gonzo
```

###### ↳ ↳ ↳ Re: DB2 to COBOL translation

_(reply depth: 5)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-13T05:06:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wBx8b.53467$Mb2.1744107@twister.tampabay.rr.com>`
- **References:** `<%r18b.88$iT5.27@newssvr24.news.prodigy.com> <UR28b.134977$0v4.9878087@bgtnsc04-news.ops.worldnet.att.net> <o0l8b.283$rS3.165@newssvr24.news.prodigy.com> <ZTp8b.480$Aq2.81@newsread1.news.atl.earthlink.net> <1ls8b.406$_15.145@newssvr24.news.prodigy.com>`

```

"Gonzo" <ckhamel1961.nospam@yahoo.com> wrote in message
news:1ls8b.406$_15.145@newssvr24.news.prodigy.com...
>
> "William M. Klein" <wmklein@nospam.netcom.com> wrote:
…[7 more quoted lines elided]…
> though, why they haven't updated their compiler. My client is so big I
doubt
> I'd ever find the right person to ask in the timeframe I have, much less
do
> anything about it.
>
> Gonzo
I believe this compiler isn't supported by IBM anymore (may be wrong).
Depending on what they do, this could be an auditable business exposure. You
could always tell them to call IBM for help to support this and get IBM to
tell them they need to upgrade :-)

JCE
```

#### ↳ Re: DB2 to COBOL translation

- **From:** "Don Leahy" <dleahy@rogers.com>
- **Date:** 2003-09-12T16:19:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1Tp8b.4160$Nx6.626737@news20.bellglobal.com>`
- **References:** `<%r18b.88$iT5.27@newssvr24.news.prodigy.com>`

```
You could try SELECTing the column with the DIGITS() function, which will
convert it to character.  Then you can fetch the column into a PIC
X(whatever) field.

EXEC SQL
   SELECT DIGITS(DECIMAL_COL)
        FROM some_table
        INTO  :WS-CHAR-FIELD
END-EXEC

"Gonzo" <ckhamel1961.nospam@yahoo.com> wrote in message
news:%r18b.88$iT5.27@newssvr24.news.prodigy.com...
> Hi folks,
>
…[10 more quoted lines elided]…
> I was just going to pad the first two bytes as filler and handle the
excess
> in the procedure division, but I was hoping someone might have another
idea
> at hand.
>
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: DB2 to COBOL translation

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-13T05:13:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0Ix8b.53489$Mb2.1745073@twister.tampabay.rr.com>`
- **References:** `<%r18b.88$iT5.27@newssvr24.news.prodigy.com> <1Tp8b.4160$Nx6.626737@news20.bellglobal.com>`

```
Ask an obvious question....does the data in the table actually reflect the
data definition?
If the fields are all 15,5 then you could do similar and try casting to a
DECIMAL(15,5) in the same manner as this DIGITS select only it leaves the
same value.

Of course if you are doing math with the numbers and they are big (ie.
adding) there is always the chance that you will still exceed the internal
storage anyway.  In this case the DIGITS scalar f. works well because you
can store the lod and rod separately....

It wouldn't be the first time that a DBA and application guy didn't talk.

JCE

"Don Leahy" <dleahy@rogers.com> wrote in message
news:1Tp8b.4160$Nx6.626737@news20.bellglobal.com...
> You could try SELECTing the column with the DIGITS() function, which will
> convert it to character.  Then you can fetch the column into a PIC
…[12 more quoted lines elided]…
> > I was given a DB2 layout without the benefit of a DCLGEN translation,
and
> > I've got field definition of DECIMAL(22,7). How would you change this to
a
> > COBOL PIC? I'm working with COBOL OS/390, and according to the doc I
have,
> > the rule is supposed to be:
> >
> > DECIMAL(p,s)      ->     PIC S9(p-s)V9(s) COMP-3.
> >
> > As I plug it in, I obviously get PIC S9(15)V9(7) COMP-3. My maximum
length
> > for COMP-3 fields is 18 digit positions, and I bust that by 4 positions.
> >
…[14 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
