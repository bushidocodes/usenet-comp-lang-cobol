[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# jcl sort question

_6 messages · 4 participants · 2006-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`VSAM, files, sorting`](../topics.md#files)

---

### jcl sort question

- **From:** "frenchy" <mf101723@msn.com>
- **Date:** 2006-04-13T08:49:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1144943346.285803.251270@i40g2000cwc.googlegroups.com>`

```
Is there a way to read in two files, and if there are duplicates, DON'T
write either one of the duplicates to an output file?  I.e. end up with
an output file that only has recs (from either file)that didn't have
duplicates?  I've been doing it with Cobol but figured there's got to
be a trick way to do this with the sort I've been using too.  thanks!
```

#### ↳ Re: jcl sort question

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-04-13T10:02:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bats32t8d9l476idb77r07bj9jr7lm89dr@4ax.com>`
- **References:** `<1144943346.285803.251270@i40g2000cwc.googlegroups.com>`

```
On 13 Apr 2006 08:49:06 -0700, "frenchy" <mf101723@msn.com> wrote:

>Is there a way to read in two files, and if there are duplicates, DON'T
>write either one of the duplicates to an output file?  I.e. end up with
>an output file that only has recs (from either file)that didn't have
>duplicates?  I've been doing it with Cobol but figured there's got to
>be a trick way to do this with the sort I've been using too.  thanks!

Yep.   I copied Frank Yaeger with your message.
```

#### ↳ Re: jcl sort question

- **From:** yaeger@us.ibm.com
- **Date:** 2006-04-13T09:56:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1144947378.870125.28200@v46g2000cwv.googlegroups.com>`
- **References:** `<1144943346.285803.251270@i40g2000cwc.googlegroups.com>`

```
You can use a DFSORT/ICETOOL job like the following:

//S1 EXEC PGM=ICETOOL
//TOOLMSG DD SYSOUT=*
//CON DD DSN=...  input file1
//     DD DSN=...  input file2
//OUT DD DSN=...  output file
//TOOLIN DD *
SELECT FROM(CON) TO(OUT) ON(p,m,f) NODUPS
/*

where p,m,f is the starting position, length and format of the "key"
you want to use to check for duplicates, e,g. ON(1,50,CH).  NODUPS says
to select records with no duplicates.

If you're not familiar with DFSORT and DFSORT's ICETOOL, I'd suggest
reading through "z/OS DFSORT:  Getting Started".  It's an excellent
tutorial, with lots of examples, that will show you how to use DFSORT,
DFSORT's ICETOOL and DFSORT Symbols.  You can access it online, along
with all of the other DFSORT books, from:

www.ibm.com/servers/storage/support/software/sort/mvs/srtmpub.html

Frank Yaeger - DFSORT Team  (IBM) - yaeger@us.ibm.com
Specialties: ICETOOL, IFTHEN, OVERLAY, Symbols, Migration
=> DFSORT/MVS is on the Web at http://www.ibm.com/storage/dfsort/
```

##### ↳ ↳ Re: jcl sort question

- **From:** "frenchy" <mf101723@msn.com>
- **Date:** 2006-04-13T10:24:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1144949065.324540.16570@i40g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1144947378.870125.28200@v46g2000cwv.googlegroups.com>`
- **References:** `<1144943346.285803.251270@i40g2000cwc.googlegroups.com> <1144947378.870125.28200@v46g2000cwv.googlegroups.com>`

```
That worked after I added a dummy ssmsg dd, very slick, we basically
just use pgm=sort for everything here so I passed this around.  thanks!
Frenchy
```

###### ↳ ↳ ↳ Re: jcl sort question

- **From:** yaeger@us.ibm.com
- **Date:** 2006-04-13T12:14:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1144955654.974433.4370@v46g2000cwv.googlegroups.com>`
- **References:** `<1144943346.285803.251270@i40g2000cwc.googlegroups.com> <1144947378.870125.28200@v46g2000cwv.googlegroups.com> <1144949065.324540.16570@i40g2000cwc.googlegroups.com>`

```
Oh, sorry ... I forgot the //DFSMSG DD SYSOUT=* statement for the
DFSORT messages.  //SSMSG DD SYSOUT=* will work too.

Frank Yaeger - DFSORT Team  (IBM) - yaeger@us.ibm.com
Specialties: ICETOOL, IFTHEN, OVERLAY, Symbols, Migration
=> DFSORT/MVS is on the Web at http://www.ibm.com/storage/dfsort/
```

###### ↳ ↳ ↳ Re: jcl sort question

_(reply depth: 4)_

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2006-04-29T08:41:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1146325271.642892.88180@y43g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1144955654.974433.4370@v46g2000cwv.googlegroups.com>`
- **References:** `<1144943346.285803.251270@i40g2000cwc.googlegroups.com> <1144947378.870125.28200@v46g2000cwv.googlegroups.com> <1144949065.324540.16570@i40g2000cwc.googlegroups.com> <1144955654.974433.4370@v46g2000cwv.googlegroups.com>`

```
Hi Frenchy,

Frank's the expert but I  thought you could get the same result
w/pgm=sort and sum fields=none.

If you can do it that way, is there any advantage of one over the other?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
