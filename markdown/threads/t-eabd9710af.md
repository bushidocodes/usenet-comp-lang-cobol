[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# BLKSIZE=0

_2 messages · 2 participants · 2007-11_

---

### BLKSIZE=0

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-11-05T11:23:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2snui35a51b96rp2orfflet1mpmqjqvtn6@4ax.com>`

```
On Nov 3, 2007, at 8:05 PM, Clark Morris wrote:

> On 30 Oct 2007 09:18:04 -0700, in bit.listserv.ibm-main you wrote:
>
…[6 more quoted lines elided]…
> standard, both 1985 and 2002.  We should not have to code it.
------------------SNIP---------

Clark,

You bring up an interesting point. One unfortunately there is  
probably no good answer for (at least that will make everyone happy).
I sort of agree with you but I can definitely see where some  
companies would not agree to. None the less it would probably be  
worth writing up a SHARE requirement for. I would also be interested  
to hear how IBM would respond to it (other than a FO). I have not  
been part of the requirement process in quite some time, but the last
I was in the loop was that IBM was rather err loose in responding to  
requirements. Most of the times that I saw IBM would give a non  
answer (to anything but accepted). I guess that is their right but  
(to me) it left the audience guessing if IBM really agreed with it or
if they will bury it. I vaguely remember that (when GUIDE submitted  
requirements) it was floated around IBM and it usually got to the  
right people when they wanted to respond but most of the time it went
into the holding pen in the sky when they didn't want to.

I would think that there would be a rather spirited discussion in the
COBOL Group about the requirement.

Ed

----------------------------------------------------------------------
For IBM-MAIN subscribe / signoff / archive access instructions,
send email to listserv@bama.ua.edu with the message: GET IBM-MAIN INFO
Search the archives at http://bama.ua.edu/archives/ibm-main.html
```

#### ↳ Re: BLKSIZE=0

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-11-06T05:32:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Z%SXi.32219$D65.12498@fe09.news.easynews.com>`
- **References:** `<2snui35a51b96rp2orfflet1mpmqjqvtn6@4ax.com>`

```
Such a SHARE requirement already exists:

     SSLNGC03003  Compiler option to make BLOCK CONTAINS clause SMS sensitive

which states in part:

"This requirement requests a compiler option that would allow the default for 
when the "BLOCK CONTAINS" clause is omitted to be set to the same processing as 
the current handling of "BLOCK CONTAINS 0 RECORDS" instead of creating/reading 
unblocked files."

The current IBM response from IBM  on 2004-01-01 is
   ACCEPTED

although I (personally) haven't seen antying to tell me what IBM has done in the 
last 3 3/4 years related to it.

Anyone interested in such a feature can/should submit a "REQUEST" via their IBM 
marketting support referencing this SHARE requirement.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
