[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Alas, poor ILBOWAT0, I knew you well <G>

_4 messages · 2 participants · 2007-02_

---

### Alas, poor ILBOWAT0, I knew you well <G>

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-02-07T06:20:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yceyh.12577$dB4.594@fe08.news.easynews.com>`

```
to: comp.lang.cobol and IBM-MAIN

For those of you who may have missed it in IBM's z/OS 1.9 "preview" at (long 
URL)
   http://www-306.ibm.com/common/ssi/fcgi-bin/ssialias?subtype=ca&infotype=an&appname=iSource&supplier=897&letternum=ENUS207-018

There is a paragraph that says,

"A pair of new callable services are planned, CEE3DLY and CEEDLYM, that will be 
designed to enable Language Environment-conforming applications to suspend 
execution. These new services are intended to allow you to migrate COBOL 
applications away from ILBOWAT0."

See existing SHARE requirement:

 SSLNGC0313580  Port CEE5DLY functionality to LE for z/OS and for z/VM


(even if that requirement was showing "RECOGNIZED" and not ACCEPTED)
```

#### ↳ Re: Alas, poor ILBOWAT0, I knew you well <G>

- **From:** docdwarf@panix.com ()
- **Date:** 2007-02-07T13:54:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eqcllu$ae7$1@reader2.panix.com>`
- **References:** `<yceyh.12577$dB4.594@fe08.news.easynews.com>`

```
In article <yceyh.12577$dB4.594@fe08.news.easynews.com>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>to: comp.lang.cobol and IBM-MAIN
>
…[10 more quoted lines elided]…
>applications away from ILBOWAT0."

Maybe it's just my current environment... but I've had difficulties in 
calling ILBOWAT0 for a few years.

I will not post the code (or compile or jcl) unless someone wants to 
discuss it.

DD
```

##### ↳ ↳ Re: Alas, poor ILBOWAT0, I knew you well <G>

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-02-07T19:00:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mlpyh.190451$L62.76183@fe12.news.easynews.com>`
- **References:** `<yceyh.12577$dB4.594@fe08.news.easynews.com> <eqcllu$ae7$1@reader2.panix.com>`

```
Doc,
  The usual problems with using ILBOWAT0 are:

1) Calling program not compiled with DATA(24) (as ILBOWAT can't understand 
31-bit addresses)

2) Someone has "played games" with run-time libraries trying to concatenate LE 
and OS/VS COBOL (or VS COBOL II) run-times "together" in STEPLIB or LINKLIST

3) Problem with TRUNC setting.

If you actually WANT to try and get it working, send me email off list and we 
can see what is happening.
```

###### ↳ ↳ ↳ Re: Alas, poor ILBOWAT0, I knew you well <G>

- **From:** docdwarf@panix.com ()
- **Date:** 2007-02-07T19:38:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eqd9rv$msk$1@reader2.panix.com>`
- **References:** `<yceyh.12577$dB4.594@fe08.news.easynews.com> <eqcllu$ae7$1@reader2.panix.com> <mlpyh.190451$L62.76183@fe12.news.easynews.com>`

```
In article <mlpyh.190451$L62.76183@fe12.news.easynews.com>,
William M. Klein <wmklein@nospam.netcom.com> wrote:

[snip]

>If you actually WANT to try and get it working, send me email off list and we 
>can see what is happening.

Moved to email.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
