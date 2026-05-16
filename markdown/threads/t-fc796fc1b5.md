[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Euro Phase Two.

_3 messages · 3 participants · 1999-06_

---

### Euro Phase Two.

- **From:** "Charles Handy" <charles_handy@hotmail.com>
- **Date:** 1999-06-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ODiDcLEt#GA.283@cpmsnbbsa03>`

```
We have just finished the high level analysis stage of Euro phase two which
involves converting financial systems to dual currency mode i.e holding and
manipulating data in both NCD and Euro currencies.  We estimate the effort
to be at least twice that required for Y2K with the major impact being on
numeric field sizes in our mainly COBOL programs and performance issues
related to back office processing and data storage. For example there is a
requirement to hold numeric values to six decimal points and possibly a
requirement to process credit card transactions in both the NCD and EURO,
and print combined NCD and Euro statements.  I am interested in talking to
anyone on this newsgroup who has carried out similar investigations with a
view to sharing ideas and strategies.
```

#### ↳ Re: Euro Phase Two.

- **From:** "Ira D. Baxter" <idbaxter@semdesigns.com>
- **Date:** 1999-06-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376173BA.AEE49FE9@semdesigns.com>`
- **References:** `<ODiDcLEt#GA.283@cpmsnbbsa03>`

```
Such a huge effort almost demands automation to carry it out.
Check out www.semdesigns.com for the DMS Reengineering Toolkit,
which could be used to define and carry out the transformations
required to update the data schemas and the code modifications.

Charles Handy wrote:

> We have just finished the high level analysis stage of Euro phase two which
> involves converting financial systems to dual currency mode i.e holding and
…[8 more quoted lines elided]…
> view to sharing ideas and strategies.
```

#### ↳ Re: Euro Phase Two.

- **From:** "Paulo Vieira" <pvieira@emporsoft.pt>
- **Date:** 1999-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7k2ghn$9u4$1@duke.telepac.pt>`
- **References:** `<ODiDcLEt#GA.283@cpmsnbbsa03>`

```
We've been doing that for the past 18 months now. The system is stable and
running, but the solution was to recode most of the pakage. Of course the
currency conversion is held in a single module, but we had to include
information in almost all files. The selection parameters for reporting was
also an issue since know, the user as the choice of the NCD (or Euro) in
wich the report is to be printed.
For historical data, every program performs a conversion based on dates, if
applicable, in order to make comparisons possible.

----------------------------------------------
Paulo Vieira
- pvieira@emporsoft.pt,http://www.emporsoft.pt
- Sailor on Weekends :)
- Programmer on business days



Charles Handy escreveu na mensagem ...
>We have just finished the high level analysis stage of Euro phase two which
>involves converting financial systems to dual currency mode i.e holding and
…[15 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
