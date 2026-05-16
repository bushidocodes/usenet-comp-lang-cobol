[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# INCLUDE statement: Y2K Compliance made easier

_3 messages · 3 participants · 1998-11_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### INCLUDE statement: Y2K Compliance made easier

- **From:** fyaeger5@vnet.ibm.com
- **Date:** 1998-11-03T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<71llop$bn0$1@nnrp1.dejanews.com>`

```
Back in June, there was a discussion of INCLUDE statements of:

  INCLUDE COND=(184,4,CH,GT,C'9212',AND,184,4,CH,LT,C'9302') or
  INCLUDE COND=(184,4,ZD,GT,9212,AND,184,4,ZD,LT,9302)

... which needed to be changed for Y2K compliance.

A solution with Y2C was suggested which people were not happy with because it
was too complicated and unreadable.

DFSORT was listening and we now have a simple, readable solution with our new
full date formats, available via PTFs for DFSORT R13 and DFSORT R14.  To wit:

  INCLUDE COND=(184,4,Y2T,GT,Y'9212',AND,184,4,Y2T,LT,Y'9302')

The specified fixed or sliding century window will be used for the Y2T format
fields and the Y-constants.

There are 6 new full date formats (Y2T, Y2U, Y2V, Y2W, Y2X and Y2Y) for CH, ZD
and PD date fields like yymmdd, yyddd, yymm, yyq, mmddyy, dddyy, mmyy and qyy.
Besides comparing full date fields to full date constants and other full date
fields, you can also sort and merge full dates, transform CH, ZD and PD full
two-digit year dates to CH and PD full four-digit year dates, use full date
formats with COBOL, and more.

For complete information on DFSORT's new generation of Year 2000 features,
visit the DFSORT home page at URL:

http://www.ibm.com/storage/dfsort/

Frank Yaeger - DFSORT Team (Specialties: Y2K, Symbols, OUTFIL, ICETOOL)
fyaeger@vnet.ibm.com










-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: INCLUDE statement: Y2K Compliance made easier

- **From:** The Goobers <docdwarf@erols.com>
- **Date:** 1998-11-02T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<363E6AEB.3F6B@erols.com>`
- **References:** `<71llop$bn0$1@nnrp1.dejanews.com>`

```
fyaeger5@vnet.ibm.com wrote:
> 
> Back in June, there was a discussion of INCLUDE statements of:
> 
>   INCLUDE COND=(184,4,CH,GT,C'9212',AND,184,4,CH,LT,C'9302') or
>   INCLUDE COND=(184,4,ZD,GT,9212,AND,184,4,ZD,LT,9302)

By Gadfrey, that sure looks familiar!

> 
> ... which needed to be changed for Y2K compliance.

Aye, that it did.

> 
> A solution with Y2C was suggested which people were not happy with because it
> was too complicated and unreadable.

... but, sadly enough, was the only thing available at the time.

> 
> DFSORT was listening and we now have a simple, readable solution with our new
> full date formats, available via PTFs for DFSORT R13 and DFSORT R14.  To wit:
> 
>   INCLUDE COND=(184,4,Y2T,GT,Y'9212',AND,184,4,Y2T,LT,Y'9302')

How lovely... but... the installation where this was a concern (speaking
as the one who posted the original difficulty) uses SyncSort, not
DFSORT... and they are rather loathe to change packages.

Now, of course, the folks at SyncSort will probably reverse-engineer the
change and make it available... and somewhere down the line *someone*
will say 'Hey, why didn't you do *this*?'

DD
```

##### ↳ ↳ Re: INCLUDE statement: Y2K Compliance made easier

- **From:** Dave Eastabrook <news@elmbronze.demon.co.uk>
- **Date:** 1998-11-03T00:00:00
- **Newsgroups:** comp.software.year-2000,comp.lang.cobol
- **Message-ID:** `<R$GmrBAyZuP2EwZL@elmbronze.demon.co.uk>`
- **References:** `<71llop$bn0$1@nnrp1.dejanews.com> <363E6AEB.3F6B@erols.com>`

```
on Mon, 2 Nov 1998 The Goobers <docdwarf@erols.com> wrote
>fyaeger5@vnet.ibm.com wrote:
>> 
…[30 more quoted lines elided]…
>will say 'Hey, why didn't you do *this*?'

You're totally right.  Ask Frank if he'd give you an email [1] that says
something like "IBM and DFSORT listened to DD and put this change in but
presently SYNCSORT does not have this facility.".

Not that that will make any difference - you'll still be a dinosaur.

[1].  Dare I say a cheque [2] might be better .....

[2].  Or even a check!

Congrats to Frank and his team anyway - not every company would bother
paying any attention to postings on a newsgroup.

:Dave
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
