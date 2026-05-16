[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Copybooks

_5 messages · 5 participants · 2001-03_

---

### Copybooks

- **From:** jim_royle_myarse@yahoo.com (Jim Royle)
- **Date:** 2001-03-07T22:15:59+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010307211557.48651.qmail@web10309.mail.yahoo.com>`

```
Can anyone tell me please how you include copybooks in
a cobol program compiled with the free Fujitsu
compiler. In my program I have coded it as 'COPY
copybook'. But when I compile it complains about the
Library not being set up. I think I've done this in
the compiler options but obviously I've gone wrong
somewhere.

Could anybody help please. I've read the documents
that came on the CD but they completely baffled me.

Thanks.

__________________________________________________
Do You Yahoo!?
Get email at your own domain with Yahoo! Mail. 
http://personal.mail.yahoo.com/
```

#### ↳ Re: Copybooks

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-03-08T01:37:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010307203756.11923.00000212@nso-fq.aol.com>`
- **References:** `<20010307211557.48651.qmail@web10309.mail.yahoo.com>`

```
In article <20010307211557.48651.qmail@web10309.mail.yahoo.com>,
jim_royle_myarse@yahoo.com (Jim Royle) writes:

>
>Can anyone tell me please how you include copybooks in
…[6 more quoted lines elided]…
>

Exactly how is your COPY statement coded and how is your
'copybook' file saved on your system?

if      COPY  'COPYBOOK'.
    then copybook should have NO Extension
if      COPY COPYBOOK.
    then copybook Could have No Extension or 
              an Extension of CPY or CBL or COB


At least this is the rule that I use when dealing with testing 
versions of libraries.
```

#### ↳ Re: Copybooks

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-03-08T02:59:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dACp6.216$sm4.24776@newsread2.prod.itd.earthlink.net>`
- **References:** `<20010307211557.48651.qmail@web10309.mail.yahoo.com>`

```
One way is to fully qualify the copy, viz:

COPY 'C:\SOURCE\COPYBOOK\MYFILE.COB'.


"Jim Royle" <jim_royle_myarse@yahoo.com> wrote in message
news:20010307211557.48651.qmail@web10309.mail.yahoo.com...
> Can anyone tell me please how you include copybooks in
> a cobol program compiled with the free Fujitsu
…[19 more quoted lines elided]…
>
```

#### ↳ Re: Copybooks

- **From:** "sandman" <vyjssm@hotmail.com>
- **Date:** 2001-03-08T22:37:09+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9897dd$oo8@netnews.hinet.net>`
- **References:** `<20010307211557.48651.qmail@web10309.mail.yahoo.com>`

```
I use full file name [includes drvie, directory and file name]
in my cobol programs like:
copy 'c:\fsccpy\my.cpy'.
or
copy "c:\fscdat\my.dat" replacing ==(xxx)== by ==abc==.
Forget the name COPYBOOK, it just a simple text file for saving
some typing work.
jason

Jim Royle <jim_royle_myarse@yahoo.com> wrote in message
news:20010307211557.48651.qmail@web10309.mail.yahoo.com...
> Can anyone tell me please how you include copybooks in
> a cobol program compiled with the free Fujitsu
…[18 more quoted lines elided]…
> via Mailgate.ORG Server - http://www.Mailgate.ORG
```

#### ↳ Re: Copybooks

- **From:** "Barry K. Clarke" <bkclarke@qwest.net>
- **Date:** 2001-03-08T19:19:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AA84BAA.4AC40297@qwest.net>`
- **References:** `<20010307211557.48651.qmail@web10309.mail.yahoo.com>`

```
Try to look through the docs for the file that holds the
copybooks, search copylib, copybooks.  The compiler is
telling  you that its looking for a file with the copybook,
but can't find it.  Also try using an include statement in
the program.

Barry

Jim Royle wrote:

> Can anyone tell me please how you include copybooks in
> a cobol program compiled with the free Fujitsu
…[18 more quoted lines elided]…
> via Mailgate.ORG Server - http://www.Mailgate.ORG
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
