[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Checking RACF for CICS TS

_6 messages · 3 participants · 2003-03 → 2005-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Checking RACF for CICS TS

- **From:** jfry@ameritas.com (Jeff Fry)
- **Date:** 2003-03-24T08:42:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a381b426.0303240842.6bcf46b6@posting.google.com>`

```
We are migrating from APPC to TCP/IP.  I have defined a program in the
Security Exit for the CICS listener.  I am aware of the VERIFY
PASSWORD function to authenticate the uid/password.  What I am trying
to figure out is how to check RACF to make sure that the uid has
access to the transaction they are trying to issue.  So far, it
appears that a signon needs to be done.  Does anyone have examples of
how to do this?

Thanks,
Jeff
```

#### ↳ Re: Checking RACF for CICS TS

- **From:** "Roland Schiradin" <schiradi@tap.de>
- **Date:** 2003-03-24T23:23:26+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5o09a$2m8m$1@innferno.news.tiscali.de>`
- **References:** `<a381b426.0303240842.6bcf46b6@posting.google.com>`

```
Jeff,

AFAIR. If you return the userid to the CSKL transaction CICS will issue
to checks:

1. Could the userid of transaction CSKL invoke transaction for userid
xxxxxx. RACF CL(SURROGAT) profile
DFHAPPL or DFHSTART
2. Is the userid correct (revoked or whatever)
3. Does the userid have access to this transaction.

This means CICS does already what you want/need

Roland

"Jeff Fry" <jfry@ameritas.com> schrieb im Newsbeitrag
news:a381b426.0303240842.6bcf46b6@posting.google.com...
> We are migrating from APPC to TCP/IP.  I have defined a program in the
> Security Exit for the CICS listener.  I am aware of the VERIFY
…[7 more quoted lines elided]…
> Jeff
```

##### ↳ ↳ Re: Checking RACF for CICS TS

- **From:** jfry@ameritas.com (Jeff Fry)
- **Date:** 2003-03-25T06:01:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a381b426.0303250601.11cb0450@posting.google.com>`
- **References:** `<a381b426.0303240842.6bcf46b6@posting.google.com> <b5o09a$2m8m$1@innferno.news.tiscali.de>`

```
I am returning the userid to the CSKL transaction.  When the userid I
pass back has access to the transaction through RACF, everything works
correctly.  If the userid does not have access, the listener doesn't
start the transaction.  It also does not respond to the client
process.  The client process just sits on the listen waiting for a
response until it times out.  Is there something I need to change to
get the CSKL transaction to respond to the client for this condition? 
Also, you mention RACF CL(SURROGAT) profile.  Are you indicating that
we would need to turn on Surrogate security for this?  Our security
administrators are very hesitant to do this.

Thanks,
Jeff


"Roland Schiradin" <schiradi@tap.de> wrote in message news:<b5o09a$2m8m$1@innferno.news.tiscali.de>...
> Jeff,
> 
…[24 more quoted lines elided]…
> > Jeff
```

###### ↳ ↳ ↳ Re: Checking RACF for CICS TS

- **From:** "Roland Schiradin" <schiradi@tap.de>
- **Date:** 2003-03-25T22:42:57+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5qi9k$5oo$1@innferno.news.tiscali.de>`
- **References:** `<a381b426.0303240842.6bcf46b6@posting.google.com> <b5o09a$2m8m$1@innferno.news.tiscali.de> <a381b426.0303250601.11cb0450@posting.google.com>`

```
Jeff,

first problem:
Depending on a switch you return in your exit the CSKL will send a reply to
the client
or not. So it's your choice in the exit. Check the DfhCommArea layout for
the exit.

Second:
If the listener CSKL runs under userid XXXXX and try to start a transaction
FROG for
userid YYYYYY the XXXXXX need some surrogate permission to do so. It's *NOT*
SURROGATE at all its's just a profile like DFHSTART or DFHAPPL in
CL(SURROGAT).
Sorry I can't remember the exact name. Your security admin is right so
ensure userid XXXXXX (the CSKL userid)
can *NOT* be used via regular sign-on like userid for started tasks. A PLTPI
user or userid
of the started task might help. Bad effect of this is you can't start the
CSKL using the EZAO
transaction so you have to bounce the region. We do it the same to ensure
security and
also accounting as the accounting is based on the userid and we never had to
bounce the region
because of this for several years.

All it's not a Cobol problem and I don't read this newsgroup very often.

HTH
Roland

"Jeff Fry" <jfry@ameritas.com> schrieb im Newsbeitrag
news:a381b426.0303250601.11cb0450@posting.google.com...
> I am returning the userid to the CSKL transaction.  When the userid I
> pass back has access to the transaction through RACF, everything works
…[13 more quoted lines elided]…
> "Roland Schiradin" <schiradi@tap.de> wrote in message
news:<b5o09a$2m8m$1@innferno.news.tiscali.de>...
> > Jeff,
> >
…[24 more quoted lines elided]…
> > > Jeff
```

###### ↳ ↳ ↳ Re: Checking RACF for CICS TS

_(reply depth: 4)_

- **From:** "bauer08" <jens.bauer@muc.mtu.de>
- **Date:** 2005-07-26T08:47:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ea23e9f9a9cd49d1a578d654a103bb5f@localhost.talkaboutprogramming.com>`
- **References:** `<a381b426.0303240842.6bcf46b6@posting.google.com> <b5o09a$2m8m$1@innferno.news.tiscali.de> <a381b426.0303250601.11cb0450@posting.google.com> <b5qi9k$5oo$1@innferno.news.tiscali.de>`

```
Hi Jeff,

your problem is exactly my problem.

That is the solution ?

regards, 
bauer
```

###### ↳ ↳ ↳ Re: Checking RACF for CICS TS

- **From:** "Roland Schiradin" <schiradi@tap.de>
- **Date:** 2003-03-25T22:50:31+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5qimt$5r8$1@innferno.news.tiscali.de>`
- **References:** `<a381b426.0303240842.6bcf46b6@posting.google.com> <b5o09a$2m8m$1@innferno.news.tiscali.de> <a381b426.0303250601.11cb0450@posting.google.com>`

```
Jeff,

if your CICS SIT contains a XUSER=NO the surrogate checking is not done,
but anyone can start transactions with a different userid. I don't know if
your
security admin like this also. Maybe they don't know anything about this
option:-)))

So decide yourself what to do

Roland


"Jeff Fry" <jfry@ameritas.com> schrieb im Newsbeitrag
news:a381b426.0303250601.11cb0450@posting.google.com...
> I am returning the userid to the CSKL transaction.  When the userid I
> pass back has access to the transaction through RACF, everything works
…[13 more quoted lines elided]…
> "Roland Schiradin" <schiradi@tap.de> wrote in message
news:<b5o09a$2m8m$1@innferno.news.tiscali.de>...
> > Jeff,
> >
…[24 more quoted lines elided]…
> > > Jeff
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
