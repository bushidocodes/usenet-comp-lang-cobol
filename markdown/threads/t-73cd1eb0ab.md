[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [Semi-OT] IBM's IMS V10 Announcement

_5 messages · 3 participants · 2007-10 → 2008-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### [Semi-OT] IBM's IMS V10 Announcement

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-09T16:24:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lXNOi.83394$6L.59679@fe03.news.easynews.com>`

```
(I think it was in this group that someone stated that IBM was 
"grand-fathering" - or some such term - its IMS support.  That is PART of the 
reason that I am sending this note)

Today, IBM announced its latest Version of IMS (both database and transaction 
servers).  Even for those NOT on IBM zOS, I think you might be interested in 
going to:

  http://www.ibm.com/vrm/newsletter_10577_2055_47930_email_DYN_1IN/WKlein12584487

and look particularly at the section,
    "Product positioning"

I don't think that the information (options?) would be universally accepted, but 
I think some within this group would find them interesting AND they do represent 
IBM's current OFFICIAL "position".  They address both the database (hierarchical 
vs relational) issues and the transaction (web and non-web-based) issues.
```

#### ↳ Re: [Semi-OT] IBM's IMS V10 Announcement

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-10-10T11:54:19+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5n2f4tFfuj22U1@mid.individual.net>`
- **References:** `<lXNOi.83394$6L.59679@fe03.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:lXNOi.83394$6L.59679@fe03.news.easynews.com...
> (I think it was in this group that someone stated that IBM was 
> "grand-fathering" - or some such term - its IMS support.  That is PART of 
…[8 more quoted lines elided]…
>
Sorry, Bill, I am unable to see anything at this link. ("Internet Explorer 
cannot display the web page" Looks like a 404 but can't be sure)

If it is a Newsletter, could you please forward to me, (or put it on a 
server where it CAN be accessed?)? I'd really like to read it.

Cheers,

Pete.
```

##### ↳ ↳ Re: [Semi-OT] IBM's IMS V10 Announcement

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-09T23:36:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<egUOi.87746$zh6.26538@fe10.news.easynews.com>`
- **References:** `<lXNOi.83394$6L.59679@fe03.news.easynews.com> <5n2f4tFfuj22U1@mid.individual.net>`

```
I don't know if there is something that checks for viewing from within the US or 
not.  Try the following LONG URL and see if it works:

http://www-01.ibm.com/common/ssi/cgi-bin/ssialias?subtype=ca&infotype=an&appname=iSource&supplier=897&letternum=ENUS207-241

That would get you to the official version.  I have also (in case this doesn't 
work) put a PDF version on my website at:

  http://home.comcast.net/~wmklein/IBM/IMS_V10.pdf
```

###### ↳ ↳ ↳ Re: [Semi-OT] IBM's IMS V10 Announcement

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-10-10T14:02:46+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5n2mlnFfno4qU1@mid.individual.net>`
- **References:** `<lXNOi.83394$6L.59679@fe03.news.easynews.com> <5n2f4tFfuj22U1@mid.individual.net> <egUOi.87746$zh6.26538@fe10.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:egUOi.87746$zh6.26538@fe10.news.easynews.com...
>I don't know if there is something that checks for viewing from within the 
>US or not.  Try the following LONG URL and see if it works:
>
> http://www-01.ibm.com/common/ssi/cgi-bin/ssialias?subtype=ca&infotype=an&appname=iSource&supplier=897&letternum=ENUS207-241

Didn't work for me.
>
> That would get you to the official version.  I have also (in case this 
…[3 more quoted lines elided]…
>

That was fine, thanks.

I've always had a soft spot for IMS :-) Used it for years before DB2 became 
available.

The main things I got from the document are as follows:

1. IBM is being HUGELY influenced by what is happening in the real world, 
and have realised they need to provide bridges to the OO environment. I 
think what they are doing is good.

2. Like all sales literature there were statements in the document that made 
me smile and laugh :-) The justification for hierarchic access as being best 
for "Mission Critical" and where the "query is known in advance" (hard 
coded) just made me chuckle. If IBM had abandoned IMS years ago there would 
be no such writing. I remember the pain in the arse traversing hierarchical 
DBs was and how we used Command codes to "remember" our positioning across 
dequeue boundaries. (Command Code 'C' stored the concatenated key of where 
you were in the "tree" so you didn't have to re-traverse it on re-entry.) 
The fact is that the Relational model can implement a hierarchical 
structure, but the hierarchical model cannot easily implement a relational 
structure. This is marketing justification for an existing product, not real 
data processing theory.

It is even more amusing because it was IBMers who formulated the Relational 
theory and showed it to be mathematically pure... Funny how Marketing can 
trumpet something when promoting one product, then ignore it when promoting 
another... :-)

You could substitute "VSAM" for IMS in the arguments described, and it 
wouldn't change the meaning (more efficient when queries are known in 
advance, good for saving object structures, etc.)

Nevertheless, they have obviously poured investment into IMS and the results 
are impressive.

3.  IBM are demonstrating commitment to a web based world  and the support 
for SOA and Web Services is good. As a co-owner of the SOAP copyright they 
obviously realise that they can leverage much with platform independent XML. 
Good to see.

Thanks for posting this, Bill. It was interesting and quite nostalgic for 
me.

Pete.
```

###### ↳ ↳ ↳ Re: [Semi-OT] IBM's IMS V10 Announcement

_(reply depth: 4)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2008-01-26T19:35:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<megnp3loq5u9e1ttbgbqa0vicejm5779qp@4ax.com>`
- **References:** `<lXNOi.83394$6L.59679@fe03.news.easynews.com> <5n2f4tFfuj22U1@mid.individual.net> <egUOi.87746$zh6.26538@fe10.news.easynews.com> <5n2mlnFfno4qU1@mid.individual.net>`

```
On Wed, 10 Oct 2007 14:02:46 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>
…[46 more quoted lines elided]…
>advance, good for saving object structures, etc.)

In both cases it may be that for the functions being implemented with
the response time requirements for those functions both IMS and VSAM
may be better suited than a relational data base.  In the various
mainframe worlds, other database organizations and indexed file access
were developed to a higher degree than on Unix and Winows systems.
>
>Nevertheless, they have obviously poured investment into IMS and the results 
…[10 more quoted lines elided]…
>Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
