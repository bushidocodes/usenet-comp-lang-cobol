[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol vs. PL/1

_4 messages · 4 participants · 1999-04_

---

### Re: Cobol vs. PL/1

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371e6059.11583045@news.netvision.net.il>`
- **References:** `<7evg1a$sr7$1@nnrp1.dejanews.com>`

```
On Tue, 13 Apr 1999 13:15:30 GMT jgis@my-dejanews.com wrote:

   [ snipped ]

:>My question is	what is the the equivalent of PIC S9(4)  COMP  IN PL/1 ? That
:>is how do you declare this in Pl/1?

BIN FIXED(15), if I recall correctly. Of course this will allow up to 32767,
which you can get as well in COBOL with the proper TRUNC option.

One of these days COBOL will support a binary length field such a S1(15) or
something like that.
```

#### ↳ Re: Cobol vs. PL/1

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f0a4i$bq1@dfw-ixnews9.ix.netcom.com>`
- **References:** `<7evg1a$sr7$1@nnrp1.dejanews.com> <371e6059.11583045@news.netvision.net.il>`

```
Binyamin Dissen wrote in message
<371e6059.11583045@news.netvision.net.il>...

>BIN FIXED(15), if I recall correctly. Of course this will allow up to
32767,
>which you can get as well in COBOL with the proper TRUNC option.
>
>One of these days COBOL will support a binary length field such a S1(15) or
>something like that.
>

"One of these days" might be sooner than you think.  The draft of the next
Standard provides support for "true binary" fields (signed and unsigned)
where a binary field can hold as large a number as will fit into the space
allocated.  This will be done via

  Usage Binary-Char
  Usage Binary-Short
  Usage Binary-Long
  Usage Binary-Double

Given the delays in the next Standard, you might want to contact your vendor
to see what plans (if any) they have for providing support for these
enhancements BEFORE the ANSI/ISO Standard gets approved.
```

##### ↳ ↳ Re: Cobol vs. PL/1

- **From:** "Robert M. Pritchett" <NewsCSIbus@rmpcp.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#MROCRhh#GA.366@nih2naad.prod2.compuserve.com>`
- **References:** `<7evg1a$sr7$1@nnrp1.dejanews.com> <371e6059.11583045@news.netvision.net.il> <7f0a4i$bq1@dfw-ixnews9.ix.netcom.com>`

```
Interesting. Maybe Cobol could/should take the Fortran approach like
Integer*2 or Real*8 etc. Also I think MicroFocus Cobol allows Comp Pic X(n)
where n is the desired number of bytes, it's still binary but you don't
have to worry about the number of decimal digits that way.


Robert M. Pritchett, President - RMP Consulting Partners LLC
http://rmpcp.com - rmpcp@pobox.com - Dallas, TX - Member ICCA
"Quality means doing it right the first time!"
See http://www.headhunter.net/jobstv/0j/j04651mjxt8trch80j.htm?ShowJob
Contractors: tired of hearing "W-2 only"? Join us and let us help you get
that same contract on a 1099 as a self-employed independent contractor!
```

###### ↳ ↳ ↳ Re: Cobol vs. PL/1

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3714A217.58A56BF2@zip.com.au>`
- **References:** `<7evg1a$sr7$1@nnrp1.dejanews.com> <371e6059.11583045@news.netvision.net.il> <7f0a4i$bq1@dfw-ixnews9.ix.netcom.com> <#MROCRhh#GA.366@nih2naad.prod2.compuserve.com>`

```
Robert M. Pritchett wrote:
> 
> Interesting. Maybe Cobol could/should take the Fortran approach like
…[3 more quoted lines elided]…
> 

I would rather not, a character can be eight, nine bits or 16 bits
giving totally different results.

After seeing the mess this can give C code that moves better 8
through 16 through 32 now into 64 bit I would hate the same
problems built into Cobol.  Bits is clear and explicit.

Ken
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
