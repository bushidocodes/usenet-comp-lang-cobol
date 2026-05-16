[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Screen Section?

_5 messages · 4 participants · 2000-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Screen Section?

- **From:** "Colonel" <colonel@psxzone.freeserve.co.uk>
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S1rc5.3193$AS5.8501@east2.usenetserver.com>`

```
Hi guys,

If there anyone/anywhere on the net that can help describe the full function
of the `screen section`?
I`ve seen it in more than enough code. I`m also wondering is it standard
COBOL?

Colonel.
psxzone@btinternet.com
```

#### ↳ Re: Screen Section?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ktf3v$cef$1@slb2.atl.mindspring.net>`
- **References:** `<S1rc5.3193$AS5.8501@east2.usenetserver.com>`

```
Concerning the question of whether or not it is "standard" - well that
depends <G>.

The existing ANSI/ISO Standards do NOT include it at all.

The existing X/Open specification *does* include it.

The draft of the next ANSI/ISO COBOL Standard includes it (similar - but not
identical to what X/Open specified).

AcuCOBOL (for example) has "enhanced" SIGNIFICANTLY the Screen Section beyond
what was in X/Open (and is in the draft Standard).

MERANT (Micro Focus) has an extension to work with CGI's.

   ***

Does this help - or confuse even more?
```

##### ↳ ↳ Re: Screen Section?

- **From:** "Colonel" <colonel@psxzone.freeserve.co.uk>
- **Date:** 2000-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XGrc5.3215$AS5.8416@east2.usenetserver.com>`
- **References:** `<S1rc5.3193$AS5.8501@east2.usenetserver.com> <8ktf3v$cef$1@slb2.atl.mindspring.net>`

```
Hmm. X/Open??? Sorry Bill, I`m a student learning COBOL.
I apologise for the previous lack of detail. I`m using Fujitsu V3.0 on win98
(home pc).
I know it has `Screen Section`, but I`m interested in learning to get the
most possible from it - more attractive screen layouts for one reason, as
well as others.
I`ve seen in previous posts what seems like you can read data from the
screen which has been typed from keyboard? Or am I getting completely lost??
( like I say, I`m willing to learn as much as possible ).
By `standard` I meant - is it standard COBOL85, or is it maybe compiler
specific as to level of implementation??

Thanks

Colonel
psxzone@btinternet.com

William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:8ktf3v$cef$1@slb2.atl.mindspring.net...
> Concerning the question of whether or not it is "standard" - well that
> depends <G>.
…[5 more quoted lines elided]…
> The draft of the next ANSI/ISO COBOL Standard includes it (similar - but
not
> identical to what X/Open specified).
>
> AcuCOBOL (for example) has "enhanced" SIGNIFICANTLY the Screen Section
beyond
> what was in X/Open (and is in the draft Standard).
>
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Screen Section?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39726A5F.A279C9AB@home.com>`
- **References:** `<S1rc5.3193$AS5.8501@east2.usenetserver.com> <8ktf3v$cef$1@slb2.atl.mindspring.net> <XGrc5.3215$AS5.8416@east2.usenetserver.com>`

```


Colonel wrote:
> 
> Hmm. X/Open??? Sorry Bill, I`m a student learning COBOL.
…[9 more quoted lines elided]…
> specific as to level of implementation??

I can understand your confusion as to Bill's reply - but as posed your
question seemed academic rather than a student "How to ?". At this time
there are different flavours - (BIG BITCH here from me - it means you
lose portability with source code, what works in Fujitsu wont
necessarily work in AcuCOBOL or Micro Focus (MERANT) COBOL).

So for the moment you CAN do what you want as described using any of the
three I've mentioned plus others with Screen Sections - but they vary
slightly. In you case concentrate on the Fujitsu - if you haven't
already got it, get Thane Hubbell's book "Teach Yourself COBOL in 24
Hours" which has Screen Section examples for Fujitsu.

In answer to your 'specific' - you  are on the right track - from a file
you can READ a record and then DISPLAY on a Screen, conversely you
ACCEPT on the Screen and you WRITE a new or changed record to file.

Thane will have to supply this, but there is a web address to look at
his book on-line.

PS:  While in UK I didn't think about miles/kms or inches/cms or
litres/Galls, OR - dollars/pounds - I just shut my eyes and paid - that
way it made the holiday more enjoyable <G>

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Screen Section?

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39728e32.6624159@207.126.101.100>`
- **References:** `<S1rc5.3193$AS5.8501@east2.usenetserver.com> <8ktf3v$cef$1@slb2.atl.mindspring.net> <XGrc5.3215$AS5.8416@east2.usenetserver.com> <39726A5F.A279C9AB@home.com>`

```
On Mon, 17 Jul 2000 02:08:43 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:


>Thane will have to supply this, but there is a web address to look at
>his book on-line.
>

http://www.ibooks.com

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
