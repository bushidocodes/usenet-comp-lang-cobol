[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# weirdness

_6 messages · 6 participants · 2002-12 → 2003-01_

---

### Re: weirdness

- **From:** David Essex <dessex@arvotek.net>
- **Date:** 2002-12-28T02:15:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e0d50ad_2@news.eol.ca>`

```
CJ wrote:

 >> Iï¿½m using TinyCOBOL on Linux.
 >>
…[26 more quoted lines elided]…
 >> reading from is defined as line sequential.

The problem here may be how the input data is defined and stored.

For signed numeric data, TC uses the last digit to store the sign. The
symbol '}' is zero, 'A' to 'I' is 1 to 9, and 'J' to 'R' is -1 to -9.

If your input data is stored in an unsigned format and your program 
reads it in as a signed, then you will run into problems.
```

#### ↳ Re: weirdness

- **From:** CJ <exspecto2000@yahoo.com>
- **Date:** 2002-12-28T12:27:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DMgP9.339477$pN3.24304@sccrnsc03>`
- **References:** `<3e0d50ad_2@news.eol.ca>`

```
that was indeed the problem. could you point me to documentation which 
describes how to enter signed data into an ascii file with a regular text 
editor?

David Essex wrote:

> The problem here may be how the input data is defined and stored.
> 
…[4 more quoted lines elided]…
> reads it in as a signed, then you will run into problems.
```

##### ↳ ↳ Re: weirdness

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-12-28T17:59:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<auldte$bv6$1@slb6.atl.mindspring.net>`
- **References:** `<3e0d50ad_2@news.eol.ca> <DMgP9.339477$pN3.24304@sccrnsc03>`

```
The "best" way to enter signed data into an "ASCII" file with a normal
editor is to use + and - signs and define the COBOL data with "sign is
separate" (leading or trailing).  Use of an "internal" sign with COBOL data
tends to be most useful in COBOL-only applications (no "normal editor" or
printer input/output).
```

###### ↳ ↳ ↳ Re: weirdness

- **From:** ronglaz6@aol.comnojunk (Ron Glazier)
- **Date:** 2003-01-03T04:31:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030102233159.22997.00000414@mb-mf.aol.com>`
- **References:** `<auldte$bv6$1@slb6.atl.mindspring.net>`

```
     where can a person get tiny cobol from 
     I am using windows and one of the compillers that I have is cobol 6.50
which is public domain but yet to get it to compille a program.  maybe there is
a key to make it work.  
 I guess I did not understand the instructions or they were incomplete maybe.
                      RonGlaz6@aol.com
```

###### ↳ ↳ ↳ Re: weirdness

_(reply depth: 4)_

- **From:** Billy O'Connor <billyoc@linuxfromscratch.org>
- **Date:** 2003-01-03T05:15:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81of6zf2wo.fsf@dps10.oconnoronline.net>`
- **References:** `<auldte$bv6$1@slb6.atl.mindspring.net> <20030102233159.22997.00000414@mb-mf.aol.com>`

```
ronglaz6@aol.comnojunk (Ron Glazier) writes:

>      where can a person get tiny cobol from 
>      I am using windows and one of the compillers that I have is cobol 6.50
…[4 more quoted lines elided]…
> 

www.tinycobol.org
```

###### ↳ ↳ ↳ Re: weirdness

_(reply depth: 4)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2003-01-04T08:33:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E169CA0.591A794A@worldnet.att.net>`
- **References:** `<auldte$bv6$1@slb6.atl.mindspring.net> <20030102233159.22997.00000414@mb-mf.aol.com>`

```
Ron Glazier wrote:
> 
>      where can a person get tiny cobol from
…[4 more quoted lines elided]…
>                       RonGlaz6@aol.com

Here's a website that might be helpful in getting Cobol 6.50 to work:
http://www.dol.net/~rcole/cobol650.htm
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
