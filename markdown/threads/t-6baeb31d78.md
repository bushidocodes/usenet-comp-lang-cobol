[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New DFSORT/ICETOOL Features (Feb, 2003)

_5 messages · 3 participants · 2003-02_

---

### New DFSORT/ICETOOL Features (Feb, 2003)

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-14T13:28:12-06:00
- **Newsgroups:** comp.lang.cobol,ibm.software.cobol
- **Message-ID:** `<b2jg0h$pvo$1@slb6.atl.mindspring.net>`
- **References:** `<OFDE42E6A4.2037E542-ON88256CCD.005CDBDF-88256CCD.005D0516@us.ibm.com>`

```
This note appeared in the IBM-MAIN list-server.  I thought that it might
also be of interest to some (IBM) COBOL people as well.  From a "brief"
glance at the documentation, I don't see any "COBOL" or "internal sort"
specific enhancements - but I do think that the general enhancements may
still be of interest in many IBM mainframe shops - that don't read
"IBM-MAIN".

Please pass this on "within your shop" - as you think it appropriate.
```

#### ↳ Re: New DFSORT/ICETOOL Features (Feb, 2003)

- **From:** Frank Yaeger <yaeger@us.ibm.com>
- **Date:** 2003-02-14T12:39:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E4D541A.8060400@us.ibm.com>`
- **References:** `<OFDE42E6A4.2037E542-ON88256CCD.005CDBDF-88256CCD.005D0516@us.ibm.com> <b2jg0h$pvo$1@slb6.atl.mindspring.net>`

```
William M. Klein wrote:

>This note appeared in the IBM-MAIN list-server.  I thought that it might
>also be of interest to some (IBM) COBOL people as well.  From a "brief"
…[19 more quoted lines elided]…
>>
Thanks for posting this, Bill.  I posted it on the ibm-main and racf-l 
lists (as well as several help boards) where DFSORT/ICETOOL are 
frequently discussed.  I decided not to post it to the Cobol lists 
because DFSORT/ICETOOL is only discussed on them infrequently.   You're 
right that there are no specific enhancements for COBOL this time, but 
the new SPLICE, SAMPLE, REPEAT, SPLITBY, and arithmetic operations with 
fields and constants (with or without symbols) features might be of 
interest to those COBOL programmers who are open to using DFSORT features.

Frank Yaeger - DFSORT Team
Specialties: ICETOOL, OUTFIL, Symbols, Migration
=> DFSORT/MVS is on the WWW at http://www.ibm.com/storage/dfsort
```

#### ↳ Re: New DFSORT/ICETOOL Features (Feb, 2003)

- **From:** Frank Yaeger <yaeger@us.ibm.com>
- **Date:** 2003-02-14T12:56:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E4D57F4.40009@us.ibm.com>`
- **References:** `<OFDE42E6A4.2037E542-ON88256CCD.005CDBDF-88256CCD.005D0516@us.ibm.com> <b2jg0h$pvo$1@slb6.atl.mindspring.net>`

```
William M. Klein wrote:

>This note appeared in the IBM-MAIN list-server.  I thought that it might
>also be of interest to some (IBM) COBOL people as well.  From a "brief"
…[13 more quoted lines elided]…
>>
Thanks for posting this, Bill.  I posted it on the ibm-main and racf-l 
lists (as well as several help boards) where DFSORT/ICETOOL are 
frequently discussed.  I decided not to post it to the Cobol lists 
because DFSORT/ICETOOL is only discussed on them infrequently.   You're 
right that there are no specific enhancements for COBOL this time, but 
the new SPLICE, SAMPLE, REPEAT, SPLITBY, and arithmetic operations with 
fields and constants (with or without symbols) features might be of 
interest to those COBOL programmers who are open to using DFSORT features.

-

Frank Yaeger - DFSORT Team
Specialties: ICETOOL, OUTFIL, Symbols, Migration
=> DFSORT/MVS is on the WWW at http://www.ibm.com/storage/dfsort/
```

##### ↳ ↳ Re: New DFSORT/ICETOOL Features (Feb, 2003)

- **From:** "Don Leahy" <xdb2imsN@nospam.whatever.net>
- **Date:** 2003-02-14T16:03:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0Rc3a.5517$606.1078548@news20.bellglobal.com>`
- **References:** `<OFDE42E6A4.2037E542-ON88256CCD.005CDBDF-88256CCD.005D0516@us.ibm.com> <b2jg0h$pvo$1@slb6.atl.mindspring.net> <3E4D57F4.40009@us.ibm.com>`

```
"Frank Yaeger" <yaeger@us.ibm.com> wrote in message
news:3E4D57F4.40009@us.ibm.com...
> William M. Klein wrote:
>
…[30 more quoted lines elided]…
>
Hey, are you trying to put me out of work??  I just spent all morning
writing a file match program in Cobol.   :-)
```

###### ↳ ↳ ↳ Re: New DFSORT/ICETOOL Features (Feb, 2003)

- **From:** Frank Yaeger <yaeger@us.ibm.com>
- **Date:** 2003-02-14T14:17:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E4D6AE8.2040102@us.ibm.com>`
- **References:** `<OFDE42E6A4.2037E542-ON88256CCD.005CDBDF-88256CCD.005D0516@us.ibm.com> <b2jg0h$pvo$1@slb6.atl.mindspring.net> <3E4D57F4.40009@us.ibm.com> <0Rc3a.5517$606.1078548@news20.bellglobal.com>`

```
Don Leahy wrote:

>Hey, are you trying to put me out of work??  I just spent all morning
>writing a file match program in Cobol.   :-)
>
I'm just trying to free you up to do more complex work.  :-) :-)   But 
you may be safe since SPLICE  can't do EVERY possible type of file match.

- 
Frank Yaeger - DFSORT Team
Specialties: ICETOOL, OUTFIL, Symbols, Migration
=> DFSORT/MVS is on the WWW at http://www.ibm.com/storage/dfsort/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
