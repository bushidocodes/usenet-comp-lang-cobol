[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Search for a string using SORT

_7 messages · 3 participants · 2006-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`VSAM, files, sorting`](../topics.md#files)

---

### Search for a string using SORT

- **From:** "mftips@gmail.com" <mftips@gmail.com>
- **Date:** 2006-02-07T18:32:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1139365923.420617.13760@g14g2000cwa.googlegroups.com>`

```
To Search for a particular string within a file when the exact position
of that string within a record is not known and to write that record in
the Output file the following SORT card can be used.

Example 1:
SORT FIELDS=COPY
INCLUDE COND= (1, 80, SS, EQ, C'FIND STRING')

Here,

SS - Sub string,
1 - Starting position of the range
80 - Width of the search range
EQ - Comparison operators

The Sort card for this will need information like range of columns
within which you want the search to be performed. To search in the
whole file you can give the start position as 1 and LRECL of the file
as the width of the search range as done above. We can also replace the
'EQ' parameter by 'NE' which will fetch us all the records which don't
have the specified string. Only EQ & NE can be used for comparison. We
can even use OMIT COND instead of INCLUDE.

This can also be used to find the records with string that match one of
the strings in the COND.

Example 2:
SORT FIELDS=COPY
INCLUDE COND= (1, 80, SS, EQ, C'HDR,TRL')

The above sort card returns all records with the substring ' HDR' or
'TRL' occurring within the search range(1-80) of the record in the
input file. 
 
Thanks,
MFTIPS
http://mftips.blogspot.com/
```

#### ↳ Re: Search for a string using SORT

- **From:** yaeger@us.ibm.com
- **Date:** 2006-02-09T09:51:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1139507489.420693.97720@o13g2000cwo.googlegroups.com>`
- **References:** `<1139365923.420617.13760@g14g2000cwa.googlegroups.com>`

```
mftips@gmail.com wrote:
> To Search for a particular string within a file when the exact position
> of that string within a record is not known and to write that record in
> the Output file the following SORT card can be used.
>...

Your examples are actually incorrect.  Your control statements contain
blanks that will result in syntax errors.  For example 1, the INCLUDE
statement should be:

   INCLUDE COND=(1,80,SS,EQ,C'FIND STRING')

Your second example does NOT do what you say it does.

   INCLUDE COND=(1,80,SS,EQ,C'HDR,TRL')

will actually include records with the string 'HDR,TRL' in them.  To
include records with the string 'HDR' or the string 'TRL' in them, you
would use this DFSORT INCLUDE statement:

   INCLUDE COND=(1,80,SS,EQ,C'HDR',OR,
                1,80,SS,EQ,C'TRL')

To include records with the string 'HDR' or the string 'TRL' in
positions 11-13, you could use this DFSORT INCLUDE statement:

   INCLUDE COND=(11,3,SS,EQ,C'HDR,TRL')

For those who are not familiar with DFSORT and DFSORT's ICETOOL, I'd
suggest reading through "z/OS DFSORT:  Getting Started".  It's an
excellent tutorial, with lots of examples, that will show you how to
use DFSORT, DFSORT's ICETOOL and DFSORT Symbols.  You can access it
online, along with all of the other DFSORT books, from:

www.ibm.com/servers/storage/support/software/sort/mvs/srtmpub.html

Frank Yaeger - DFSORT Team  (IBM) - yaeger@us.ibm.com
Specialties: ICETOOL, IFTHEN, OVERLAY, Symbols, Migration
=> DFSORT/MVS is on the Web at http://www.ibm.com/storage/dfsort/
```

#### ↳ Re: Search for a string using SORT

- **From:** yaeger@us.ibm.com
- **Date:** 2006-02-09T09:51:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1139507493.163267.214220@g47g2000cwa.googlegroups.com>`
- **References:** `<1139365923.420617.13760@g14g2000cwa.googlegroups.com>`

```
mftips@gmail.com wrote:
> To Search for a particular string within a file when the exact position
> of that string within a record is not known and to write that record in
> the Output file the following SORT card can be used.
>...

Your examples are actually incorrect.  Your control statements contain
blanks that will result in syntax errors.  For example 1, the INCLUDE
statement should be:

   INCLUDE COND=(1,80,SS,EQ,C'FIND STRING')

Your second example does NOT do what you say it does.

   INCLUDE COND=(1,80,SS,EQ,C'HDR,TRL')

will actually include records with the string 'HDR,TRL' in them.  To
include records with the string 'HDR' or the string 'TRL' in them, you
would use this DFSORT INCLUDE statement:

   INCLUDE COND=(1,80,SS,EQ,C'HDR',OR,
                1,80,SS,EQ,C'TRL')

To include records with the string 'HDR' or the string 'TRL' in
positions 11-13, you could use this DFSORT INCLUDE statement:

   INCLUDE COND=(11,3,SS,EQ,C'HDR,TRL')

For those who are not familiar with DFSORT and DFSORT's ICETOOL, I'd
suggest reading through "z/OS DFSORT:  Getting Started".  It's an
excellent tutorial, with lots of examples, that will show you how to
use DFSORT, DFSORT's ICETOOL and DFSORT Symbols.  You can access it
online, along with all of the other DFSORT books, from:

www.ibm.com/servers/storage/support/software/sort/mvs/srtmpub.html

Frank Yaeger - DFSORT Team  (IBM) - yaeger@us.ibm.com
Specialties: ICETOOL, IFTHEN, OVERLAY, Symbols, Migration
=> DFSORT/MVS is on the Web at http://www.ibm.com/storage/dfsort/
```

##### ↳ ↳ Re: Search for a string using SORT

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-02-09T10:59:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vm0nu15e5hfhv61m5e95981tjiv0mueq87@4ax.com>`
- **References:** `<1139365923.420617.13760@g14g2000cwa.googlegroups.com> <1139507493.163267.214220@g47g2000cwa.googlegroups.com>`

```
On 9 Feb 2006 09:51:33 -0800, yaeger@us.ibm.com wrote:

>For those who are not familiar with DFSORT and DFSORT's ICETOOL, I'd
>suggest reading through "z/OS DFSORT:  Getting Started".  It's an
…[8 more quoted lines elided]…
>=> DFSORT/MVS is on the Web at http://www.ibm.com/storage/dfsort/


What happened to
HTTP://PUBLIBZ.BOULDER.IBM.COM/CGI-BIN/BOOKMGR_OS390/BOOKS/ISPZU220/APPENDIX1
?
```

###### ↳ ↳ ↳ Re: Search for a string using SORT

- **From:** yaeger@us.ibm.com
- **Date:** 2006-02-09T10:09:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1139508556.637134.57390@g14g2000cwa.googlegroups.com>`
- **References:** `<1139365923.420617.13760@g14g2000cwa.googlegroups.com> <1139507493.163267.214220@g47g2000cwa.googlegroups.com> <vm0nu15e5hfhv61m5e95981tjiv0mueq87@4ax.com>`

```
Howard Brazee wrote:
> What happened to
> HTTP://PUBLIBZ.BOULDER.IBM.COM/CGI-BIN/BOOKMGR_OS390/BOOKS/ISPZU220/APPENDIX1
> ?

Howard,

Sorry, but I don't understand your question.  Are you looking for an
Appendix in a specific DFSORT book?  If so, which Appendix in which
book?  If not, please clarify.

Frank Yaeger - DFSORT Team  (IBM) - yaeger@us.ibm.com
Specialties: ICETOOL, IFTHEN, OVERLAY, Symbols, Migration
=> DFSORT/MVS is on the Web at http://www.ibm.com/storage/dfsort/
```

###### ↳ ↳ ↳ Re: Search for a string using SORT

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-02-09T11:34:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sm2nu1hu8nd8n0hku69bjaoiblgrcstfnk@4ax.com>`
- **References:** `<1139365923.420617.13760@g14g2000cwa.googlegroups.com> <1139507493.163267.214220@g47g2000cwa.googlegroups.com> <vm0nu15e5hfhv61m5e95981tjiv0mueq87@4ax.com> <1139508556.637134.57390@g14g2000cwa.googlegroups.com>`

```
On 9 Feb 2006 10:09:16 -0800, yaeger@us.ibm.com wrote:

>> What happened to
>> HTTP://PUBLIBZ.BOULDER.IBM.COM/CGI-BIN/BOOKMGR_OS390/BOOKS/ISPZU220/APPENDIX1
…[6 more quoted lines elided]…
>book?  If not, please clarify.

I had it as a link written in as documentation for a job.  It no
longer points to anything and I want to update my documentation with
wherever that old documentation was moved to.   Trouble is, I don't
remember what it said.
```

###### ↳ ↳ ↳ Re: Search for a string using SORT

_(reply depth: 5)_

- **From:** yaeger@us.ibm.com
- **Date:** 2006-02-10T09:40:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1139593241.446404.286070@g44g2000cwa.googlegroups.com>`
- **References:** `<1139365923.420617.13760@g14g2000cwa.googlegroups.com> <1139507493.163267.214220@g47g2000cwa.googlegroups.com> <vm0nu15e5hfhv61m5e95981tjiv0mueq87@4ax.com> <1139508556.637134.57390@g14g2000cwa.googlegroups.com> <sm2nu1hu8nd8n0hku69bjaoiblgrcstfnk@4ax.com>`

```

Howard Brazee wrote:
> On 9 Feb 2006 10:09:16 -0800, yaeger@us.ibm.com wrote:
>
…[5 more quoted lines elided]…
> remember what it said.

Sorry, I don't know what that used to point to so I can't help.

If you're looking for the DFSORT books, you can access them all from:

www.ibm.com/servers/storage/support/software/sort/mvs/srtmpub.html

Frank Yaeger - DFSORT Team  (IBM) - yaeger@us.ibm.com
Specialties: ICETOOL, IFTHEN, OVERLAY, Symbols, Migration
=> DFSORT/MVS is on the Web at http://www.ibm.com/storage/dfsort/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
