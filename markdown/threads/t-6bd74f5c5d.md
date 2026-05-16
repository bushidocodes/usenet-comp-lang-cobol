[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# compilation error.

_9 messages · 7 participants · 2006-04_

---

### compilation error.

- **From:** "arrbee" <arrbee@gmail.com>
- **Date:** 2006-04-24T01:03:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1145865783.188124.31530@t31g2000cwb.googlegroups.com>`

```
Hi,

I am getting the following compilation error when I used
"MOVE FUNCTION LENGTH (INPUT-FIELD) TO VAR-1".

But, if I use
COMPUTE VAR-1 = FUNCTION LENGTH (INPUT-FIELD) it is going smooth.

The filed is declared as VAR-1 PIC X(50).

The severe compilation error I got was as shown below:

"IGYPA3245-S - Numeric function "INTEGER FUNCTION LENGTH" was not
allowed in this context.  The statement was  discarded.

Can anybody tell me what is the problem?

I am using "IBM Enterprise COBOL for z/OS  3.3.1".

TIA.
```

#### ↳ Re: compilation error.

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-04-24T06:59:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<124pc1d5pro6id6@corp.supernews.com>`
- **References:** `<1145865783.188124.31530@t31g2000cwb.googlegroups.com>`

```

"arrbee" <arrbee@gmail.com> wrote in message
news:1145865783.188124.31530@t31g2000cwb.googlegroups.com...
> Hi,
>
…[15 more quoted lines elided]…
> I am using "IBM Enterprise COBOL for z/OS  3.3.1".

FUNCTION LENGTH is an integer function.

An integer function (or numeric function) can be used
only in an arithmetic expression. (COBOL 85 intrinsic
functions amendment)

The sending field for a MOVE statement may be either
an identifier or a literal. (COBOL 85 standard)

The message is saying, in effect, that an integer function
is not allowed where an identifier or a literal is required.

The problem is that the COBOL 85 intrinsic functions
amendment placed limits on the uses of intrinsic functions
and, as nearly as I can tell, IBM seems to have
conformed to that limit. <g>
```

##### ↳ ↳ Re: compilation error.

- **From:** "arrbee" <arrbee@gmail.com>
- **Date:** 2006-04-24T21:56:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1145941014.402235.290620@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<124pc1d5pro6id6@corp.supernews.com>`
- **References:** `<1145865783.188124.31530@t31g2000cwb.googlegroups.com> <124pc1d5pro6id6@corp.supernews.com>`

```
Thanks a lot Rick. I believe there are set of rules on the usage of
these functions. I find it simpler by using it then get a compilation
error and finally fix it. It required much knowledge to make use of
these functions. It is not easy.
```

###### ↳ ↳ ↳ Re: compilation error.

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2006-04-25T14:45:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KqednQ78vrgVBdPZnZ2dnUVZ_vGdnZ2d@adelphia.com>`
- **In-Reply-To:** `<1145941014.402235.290620@u72g2000cwu.googlegroups.com>`
- **References:** `<1145865783.188124.31530@t31g2000cwb.googlegroups.com> <124pc1d5pro6id6@corp.supernews.com> <1145941014.402235.290620@u72g2000cwu.googlegroups.com>`

```
arrbee wrote:
> Thanks a lot Rick. I believe there are set of rules on the usage of
> these functions. I find it simpler by using it then get a compilation
…[3 more quoted lines elided]…
>   
Reading before doing is a valid alternative (no matter how seldom it is 
used) to trial and error.
```

###### ↳ ↳ ↳ Re: compilation error.

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-04-25T23:48:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9zy3g.137079$7i1.48449@fe06.news.easynews.com>`
- **References:** `<1145865783.188124.31530@t31g2000cwb.googlegroups.com> <124pc1d5pro6id6@corp.supernews.com> <1145941014.402235.290620@u72g2000cwu.googlegroups.com>`

```
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/IGY3LR30/7.1.4

 Seems like a pretty good place to "start" your research on such things.

P.S.  IBM has some extensions to the '89 Intrinsic Function amendment - but does 
NOT allow everything allowed in the '02 Standard or as extensions to some other 
implementations.
```

#### ↳ Re: compilation error.

- **From:** epc8@juno.com
- **Date:** 2006-04-24T04:04:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1145876652.299281.149200@u72g2000cwu.googlegroups.com>`
- **References:** `<1145865783.188124.31530@t31g2000cwb.googlegroups.com>`

```

arrbee wrote:
> Hi,
>
…[17 more quoted lines elided]…
> TIA.

What happens if the PIC is 9(50) instead of X(50)?

What might have happened if FUNCTION LENGTH had returned a SIGNED
result?
```

##### ↳ ↳ Re: compilation error.

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-04-24T07:27:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0gkp42p9qtihr5ep0gii0r4oots9vunk2k@4ax.com>`
- **References:** `<1145865783.188124.31530@t31g2000cwb.googlegroups.com> <1145876652.299281.149200@u72g2000cwu.googlegroups.com>`

```
On 24 Apr 2006 04:04:12 -0700, epc8@juno.com wrote:

>What happens if the PIC is 9(50) instead of X(50)?

Unfortunately, the standard does not require such a big numeric field,
and I don't believe any compiler supports it.

>What might have happened if FUNCTION LENGTH had returned a SIGNED
>result?

You still can't compute a to string, you need to compute to a number.

 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: compilation error.

- **From:** epc8@juno.com
- **Date:** 2006-04-24T07:08:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1145887714.378204.52560@y43g2000cwc.googlegroups.com>`
- **References:** `<1145865783.188124.31530@t31g2000cwb.googlegroups.com> <1145876652.299281.149200@u72g2000cwu.googlegroups.com> <0gkp42p9qtihr5ep0gii0r4oots9vunk2k@4ax.com>`

```

Howard Brazee wrote:
> On 24 Apr 2006 04:04:12 -0700, epc8@juno.com wrote:
>
…[4 more quoted lines elided]…
>
Oops. Posting before morning coffee :-<.

> >What might have happened if FUNCTION LENGTH had returned a SIGNED
> >result?
>

No cream or sugar yet either :-(.

> You still can't compute a to string, you need to compute to a number.
>

Yes, I missed the point while looking at the apparent type mismatch. I
also was fooled by seeing examples where MOVE FUNCTION .... TO .....
did work when the function returned a character string.

Still it seems odd that COMPUTE works but MOVE does not when the net
effect is to perform an assignment of an integer value produced by a
function. I guess that a function result has no source field???
```

##### ↳ ↳ Re: compilation error.

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2006-04-24T16:29:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bc5f$444d4337$45491de7$24545@KNOLOGY.NET>`
- **In-Reply-To:** `<1145876652.299281.149200@u72g2000cwu.googlegroups.com>`
- **References:** `<1145865783.188124.31530@t31g2000cwb.googlegroups.com> <1145876652.299281.149200@u72g2000cwu.googlegroups.com>`

```
epc8@juno.com wrote:
> arrbee wrote:
>> Hi,
…[20 more quoted lines elided]…
> What happens if the PIC is 9(50) instead of X(50)?

Another compilation error - PIC 9(18) is the max, AFAIK...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
