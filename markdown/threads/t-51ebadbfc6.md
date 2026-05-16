[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# help with OUTREC - SHORT RECORD

_3 messages · 3 participants · 2004-08_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### help with OUTREC - SHORT RECORD

- **From:** sdsf <member@mainframeforum.com>
- **Date:** 2004-08-18T04:17:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XLAUc.27251$kC6.5758@cyclops.nntpserver.com>`

```
Im getting a U0016 ABEND that says.. OUTREC - SHORT RECORD

SORT FIELDS=(19,7,PD,A, 128,8,CH,A, 136,8,CH,A)

SUM FIELDS=(255,9,PD, 488,4,PD, 629,8,PD, 653,6,PD, 765,4,ZD, 769,2,ZD,
772,1,ZD) OUTREC FIELDS=(1:1,63,64:X'9999999999C',70:70,5003)

My file is a variable block file and the above code is running
successfully.. but for a particular file, it is abending.. i tried
removing the OUTREC FIELDS line.. and my job run successfully. The
outrec overrides the value in position 60 with +99999999999. ( the field
is defined as comp-3, that's why it only takes up 6 bytes)
```

#### ↳ Re: help with OUTREC - SHORT RECORD

- **From:** Frank Yaeger <yaeger@us.ibm.com>
- **Date:** 2004-08-18T10:05:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41238C5B.90805@us.ibm.com>`
- **References:** `<XLAUc.27251$kC6.5758@cyclops.nntpserver.com>`

```
sdsf wrote:
> Im getting a U0016 ABEND that says.. OUTREC - SHORT RECORD
> 
…[9 more quoted lines elided]…
> is defined as comp-3, that's why it only takes up 6 bytes)

It would be better to post sort questions in the ibm-main list or on one 
of the help boards (www.mvshelp.com, www.mvsforums.com), rather than in 
the COBOL list, but ...

You specified 70,5003 in the OUTREC statement.  This says that each 
record must be at least 5072 bytes long.  The message tells you that one 
or more of your variable-length records is not that long.

If you're just trying to copy the bytes from 70 to the end of the 
record, then you can use:

    OUTREC FIELDS=(1:1,63,64:X'09999999999C',70:70)

This says that each record must be at least 69 bytes long, which I 
suspect they are.

Frank Yaeger - DFSORT Team  (IBM) - yaeger@us.ibm.com
Specialties: ICETOOL, OUTFIL, Symbols, Migration
=> DFSORT/MVS is on the Web at http://www.ibm.com/storage/dfsort
```

#### ↳ Re: help with OUTREC - SHORT RECORD

- **From:** rjones0@hotmail.com (Robert Jones)
- **Date:** 2004-08-18T12:29:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dd8322.0408181129.a51b73e@posting.google.com>`
- **References:** `<XLAUc.27251$kC6.5758@cyclops.nntpserver.com>`

```
sdsf <member@mainframeforum.com> wrote in message news:<XLAUc.27251$kC6.5758@cyclops.nntpserver.com>...
> Im getting a U0016 ABEND that says.. OUTREC - SHORT RECORD
> 
…[9 more quoted lines elided]…
> is defined as comp-3, that's why it only takes up 6 bytes)

You don't say whether you are using SYNCSORT or DFSORT or ICESORT,
though I doubt that it makes any difference.  It would also be good
practice to say what hardware and operating system you are using.

However, it seems to me that you have probably not properly followed
the rules for handling variable length records and that you have
probably not allowed for the 4 byte descriptor field when you should,
you will have to check the manual.  I also note that your hex field
has an odd number of characters, I don't know what effect that would
have, but I think it is probably a mistake.

Regards, Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
