[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Finding Variable-Length Record Length

_1 message · 1 participant · 1998-09_

---

### Re: Finding Variable-Length Record Length

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tk60v$4m1$1@garnet.nbnet.nb.ca>`
- **References:** `<Jl0PnHJ5PvPd-pn2-ExXi45TkedGY@Dwight_Miller.iix.com> <35f56717.5477962@news-s01.ny.us.ibm.net>`

```
Assuming both input and output files have variable length records, the files   
should be described in the FD's as RECORD VARYING DEPENDING ON INPUT-SIZE and   
RECORD VARYING DEPENDING ON OUTPUT-SIZE where INPUT-SIZE and OUTPUT-SIZE are   
PIC 9(9) BINARY working storage fields.  When a record is selected move   
INPUT-SIZE to OUTPUT-SIZE and then WRITE OUTPUT-RECORD FROM INPUT-RECORD (1 :   
INPUT-SIZE)  
 
>  
> On Sat, 5 Sep 1998 16:34:27, Paul_Knudsen@ibm.net (Paul Knudsen)  
…[16 more quoted lines elided]…
> 

Clark F. Morris, Jr. 
CFM Technical Programming Services 
Bridgetown, Nova Scotia, Canada 
cmorris@fox.nstn.ca 
on assignment at morrisc@nbnet.nb.ca
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
