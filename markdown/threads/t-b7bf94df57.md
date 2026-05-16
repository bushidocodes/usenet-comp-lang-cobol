[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# XML generate

_4 messages · 3 participants · 2006-02 → 2006-03_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### XML generate

- **From:** "GENERALM" <mahesh.muppoor@gmail.com>
- **Date:** 2006-02-28T16:08:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141171695.336444.326700@i40g2000cwc.googlegroups.com>`

```
Given below is the output that I am able to generate from a Cobol pgm
using XML generate.   also given below is the copy book

Copybook:

01  PNSS                        GLOBAL.
     10 ActionRequested         PIC  X(75) value 'ArchiveTrades'.
     10 UserInfo.
          15 CompanyId            PIC X(12) value 'ABCDEFGHIJ'.
           15 UserEmail            PIC X(50)  value 'PNSS@abc.com'.
           15 UserType             PIC X(20)  value  'Archiving'
     10 TransactionDetails      PIC X(01)  value space.

Output I generated:

<PNSS >
<ActionRequested>ArchiveTrades</ActionRequested>
<UserInfo>
   	<CompanyId>ABCDEFGHIJ</CompanyId>
   	<UserEmail>PNSS@abc.com</UserEmail>
   	<UserType>Archiving</UserType>
</UserInfo>
>TransactionDetails> </TransactionDetails>
</PNSS>

Apparently, the format I generated is wrong.  Please see the corrected
one below.   I couldn't find the COBOL syntax to add an attribute
(ActionRequested="Archive Trades") for an element "PNSS" and also the
element TransactionDetails.  Can somebody help me out in the layout of
the copybook.

Output wanted:

<PNSS ActionRequested="ArchiveTrades">
<UserInfo>
   	<CompanyId>ABCDEFGHIJ</CompanyId>
   	<UserEmail>PNSS@abc.com</UserEmail>
   	<UserType>Archiving</UserType>
</UserInfo>
<TransactionDetails/>
</PNSS>

Thanks
```

#### ↳ Re: XML generate

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2006-03-01T18:22:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20060301.18225320@rechner12.lerch.xl>`
- **References:** `<1141171695.336444.326700@i40g2000cwc.googlegroups.com>`

```


?? Ursprüngliche Nachricht

Am 01.03.06, 00:08:15, schrieb "GENERALM" <mahesh.muppoor@gmail.com> zum 
Thema XML generate:

Hello GENERALM <is this true>

> Thanks

I am looking for an answer too. Have a look at Google: 'Cobol zOS 3.3 
XML Generate'

I think, IBM Cobol can only build simple XML, without DTD and anything 
else :-((

Einen schoenen Tag
Andreas Lerch
```

##### ↳ ↳ Re: XML generate

- **From:** Last Boy Scout <eggbtr@ezl.com>
- **Date:** 2006-03-05T23:00:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XiPOf.247$Fa.160@fe07.lga>`
- **In-Reply-To:** `<20060301.18225320@rechner12.lerch.xl>`
- **References:** `<1141171695.336444.326700@i40g2000cwc.googlegroups.com> <20060301.18225320@rechner12.lerch.xl>`

```
Andreas Lerch wrote:

> 
> ?? Ursprï¿½ngliche Nachricht
…[18 more quoted lines elided]…
> 
   15 CompanyId            PIC X(12) value 'ABCDEFGHIJ'.
            15 UserEmail            PIC X(50)  value 'PNSS@abc.com'.
            15 UserType             PIC X(20)  value  'Archiving'
*** Missing terminator???
      10 TransactionDetails      PIC X(01)  value space.

Output I generated:
```

#### ↳ Re: XML generate

- **From:** Last Boy Scout <eggbtr@ezl.com>
- **Date:** 2006-03-05T23:02:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1lPOf.248$Fa.103@fe07.lga>`
- **In-Reply-To:** `<1141171695.336444.326700@i40g2000cwc.googlegroups.com>`
- **References:** `<1141171695.336444.326700@i40g2000cwc.googlegroups.com>`

```
GENERALM wrote:

> Given below is the output that I am able to generate from a Cobol pgm
> using XML generate.   also given below is the copy book
…[43 more quoted lines elided]…
> 
Hopefully you understood that your are missing a period on the line before
10 TransactionDetails...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
