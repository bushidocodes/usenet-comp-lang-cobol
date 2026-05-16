[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL v AcuCOBOL etc

_3 messages · 3 participants · 1999-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL v AcuCOBOL etc

- **From:** "Rick Price" <rick@hpdi.demon.co.uk>
- **Date:** 1999-04-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<925408676.7227.0.nnrp-13.9e98b131@news.demon.co.uk>`

```
We currently have an appilication that was originally based on
WANG VS, then moved to AS400 and then to unix.

I.e. it works on multiple platforms.

We handle screens ourselves.  We have also isolated IO.

We went for MF COBOL (sometime ago) on unix because this seemed to be the
standard on the unix platforms (hp and aix) that we wanted to support..

I must admit that MFCOBOL ISAM matched the way we processed files.

However, lately I've been worried about the way MF COBOL is going.

I've looked at the acucobol site but it doesn't give any information on the
way ISAM files are handled.   I don't know about other unix enabled COBOL,

These queries are unix specific.  Does anybody have information on:

Cost (runtime) of MFCOBOL v other COBOLS.

Views on ISAM files especially how they handle duplicate alternate keys.

Views on ISAM files especiallly how they handle optional alternate keys eg
if a = x then do not include on the key path.

How they handle files > 2 GB.

We have a problem in so far as we have an application that works but I feel
we are reaching some kind of limit in terms of what MFCOBOL can do or what
they are willing to do on unix.

I get a strong feeling that they are windows oriented and unix processing is
accidental.

Regards
Rick
```

#### ↳ Re: MF COBOL v AcuCOBOL etc

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-04-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gab8u$4u6$1@news.cerf.net>`
- **References:** `<925408676.7227.0.nnrp-13.9e98b131@news.demon.co.uk>`

```
Rick Price wrote in message
<925408676.7227.0.nnrp-13.9e98b131@news.demon.co.uk>...
>We currently have an appilication that was originally based on
>WANG VS, then moved to AS400 and then to unix.

I know a bank in Norway that successfully move from Wang to Acucobol, you
should find the story about them on www.acucorp.com, otherwise I know that a
former manager of their development team frequently visits this newsgroup,
he may be able to tell you something if he sees this mail. The bank's name
is BN Bank.

>I've looked at the acucobol site but it doesn't give any information on the
>way ISAM files are handled.

>Cost (runtime) of MFCOBOL v other COBOLS.

That you would probably need to question Acucorp about, I have no idea.

>Views on ISAM files especially how they handle duplicate alternate keys.
>Views on ISAM files especiallly how they handle optional alternate keys eg

I am not certain if I understand your question, duplicates are allowed if
specified.

>How they handle files > 2 GB.

They do support files bigger than 2GB.

>We have a problem in so far as we have an application that works but I feel
>we are reaching some kind of limit in terms of what MFCOBOL can do or what
>they are willing to do on unix.
>I get a strong feeling that they are windows oriented and unix processing
is
>accidental.


Well, I don't know anything about MF Cobol, I do however know that Acucobols
commitment to Unix is strong, in fact so strong that I have complained about
it (I am a PC programmer) :-)

Cheesle
```

#### ↳ Re: MF COBOL v AcuCOBOL etc

- **From:** "Erlend Moen" <erlend@disys.no>
- **Date:** 1999-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gbdm0$rtp$1@troll.powertech.no>`
- **References:** `<925408676.7227.0.nnrp-13.9e98b131@news.demon.co.uk>`

```
Rick Price wrote in the message
<925408676.7227.0.nnrp-13.9e98b131@news.demon.co.uk>...
>We currently have an appilication that was originally based on
>WANG VS, then moved to AS400 and then to unix.
>
>I.e. it works on multiple platforms.

Well - let me tell you about my experience in converting/adapting to Unix.

I used to work in a bank in Norway where we had Wang VS-Cobol-applications
running. These applications was self-developed, so we had access to all
source.
As we grew larger (the bank, not the emloyees!) the Wang-system was
overloaded and we decided to switch platform. We had several candidates, but
ended up with Acucobol running on SCO-Unix on Compaq-servers. We even went
to Munich in Germany to test the estimated load on our applications on
Compaqs test-lab, a test that convinced us that we had taken the right
decision.

I was "interviewed" by Acucorp after we finally had ported our application
telling about this (http://www.acucobol.com/Partners/Success/BNBank.html).
Although it may look like an ad for Acucorp, I stand for most of the text.
For what it's worth, I can recommend AcuCorp for two reasons: They have a
wonderful compiler with lots and lots of useful possibilities and they have
excellent service if you reach into trouble of any kind.

Don't hesitate to ask me any more if you need further information!

Erlend
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
