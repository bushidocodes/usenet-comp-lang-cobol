[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IDCAMS to load a HIGH VALUES record

_8 messages · 6 participants · 2003-07_

---

### IDCAMS to load a HIGH VALUES record

- **From:** studlow1@hotmail.com (The Mean Farmer)
- **Date:** 2003-07-29T07:56:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0465864.0307290656.117872f0@posting.google.com>`

```
Is there a way that a IDCAMS REPRO step can load a VSAM file and then
put a standard HIGH-VALUES record as the last record on the file?

I have a file that I will have to access randomly using START, then
READ NEXT.  If I am beyond the last record with the START command with
the key not < dmr-key.  I get a 23 for a file status because it did
not find the record in question, an acceptable condition.  However the
read next command returns a 46, meaning that the read caused an 'at
end' condition.

I can sort in a high-values record with the data prior to the IDCAMS
step,  or I found an ASSEMBLER module that will do this for me, but
the overhead is not pretty.

Can IDCAMS do this??

Thank you.
```

#### ↳ Re: IDCAMS to load a HIGH VALUES record

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-07-29T12:09:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0307291109.53f94957@posting.google.com>`
- **References:** `<e0465864.0307290656.117872f0@posting.google.com>`

```
Hello

1) You could concatenate a file containing just the single record
containing high values with the file that you wish to process,
obviously this file would be concatenated after the other one.  You
could create the file containing the single record with a utility such
as file-aid, then keep it permanently for reuse.

2) Consider amending the program that creates the file to generate the
high values record as its last action in writing the file.

3) Consider just handling the file status 46 as an at end condition
and process accordingly.  Or better still, just act on the file status
23 from the START statement and don't do the READ NEXT when this
condition occurs.

For example:

01  ws-afile-status.
    88  ws-afile-key-not-found             value '23'.
    88  ws-afile-no-valid-next-record      value '46'.
    03  ws-afile-status-1              pic x.
        88  ws-afile-ok                    value '0'.
        88  ws-afile-at-end                value '1'.
    03  ws-afile-status-2              pic x.
```

##### ↳ ↳ Re: IDCAMS to load a HIGH VALUES record

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-07-30T00:27:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vhEVa.28298$BM.9295776@newssrv26.news.prodigy.com>`
- **References:** `<e0465864.0307290656.117872f0@posting.google.com> <fcd09c56.0307291109.53f94957@posting.google.com>`

```
>standard HIGH-VALUES

No such thing. I asume from the rest of your comments you A) have a KSDS
VSAM file (not ESDS or RRDS) and B) want a record with a key of x'FFFFFF...'
inserted with the rest of that record space or zeros?

That said, just create the 'high-values' record with FileAid (or
SORT/IEBGENER it in a previous job step), concatenate your real file and
REPRO...

STEP   EXEC PGM=IDCAMS
INF         DD DSN=DSN.WITH.ONE.HIGH.VALUE.RECORD     << real or generated
in prior step
              DD DSN=REAL.DSN.WITH.REAL.DATA
OUTF     DD DSN=YOUR.VSAM.DATASET.NAME
 SYSIN  DD *
     REPRO INFILE(INF) OUTFILE(OUTF)
....
```

#### ↳ Re: IDCAMS to load a HIGH VALUES record

- **From:** "Anon" <anon@anon.org>
- **Date:** 2003-07-29T18:59:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<w_2dnVrRzuPUl7qiXTWQlg@giganews.com>`
- **References:** `<e0465864.0307290656.117872f0@posting.google.com>`

```
> Is there a way that a IDCAMS REPRO step can load a VSAM file and then
> put a standard HIGH-VALUES record as the last record on the file?
…[12 more quoted lines elided]…
> Can IDCAMS do this??

Why don't you just concatonate a high-values record in the input?

//FILEIN  DD DSN=THE.DATA.FILE,DISP=OLD
//        DD DSN=THE.FF.RECORD,DISP=OLD
//FILEOUT DD DSN=THE.VSAM.FILE,DISP=OLD
```

#### ↳ Re: IDCAMS to load a HIGH VALUES record

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-30T00:54:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SGEVa.76277$3o3.5223434@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<e0465864.0307290656.117872f0@posting.google.com>`

```
Top post only.

You realize that if you put a high-values dummy record at the end of the
file, every program that accesses the file sequentially will have to process
it.
You may be creating more work than you save, people will have to program
around your solution.
You seem to have a handle on the file status, so it doesn't make much sense
to add a high-values record.
I hope this is a new development project.
If it's maintenance, you may wind up with egg all over your face when
currently working sequential access programs start to fail on the high-value
record.

"The Mean Farmer" <studlow1@hotmail.com> wrote in message
news:e0465864.0307290656.117872f0@posting.google.com...
| Is there a way that a IDCAMS REPRO step can load a VSAM file and then
| put a standard HIGH-VALUES record as the last record on the file?
…[14 more quoted lines elided]…
| Thank you.
```

#### ↳ Re: IDCAMS to load a HIGH VALUES record

- **From:** studlow1@hotmail.com (The Mean Farmer)
- **Date:** 2003-07-30T06:51:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0465864.0307300551.14878c6f@posting.google.com>`
- **References:** `<e0465864.0307290656.117872f0@posting.google.com>`

```
Thank you for all of your replies.  It never ceases to surprise me the
wide spread ideas that come out to real questions on this board.

I had thought through this process so just to set some minds at ease:

* the input file I am using will be placed on the mainframe from a
DATABASE on the open system - so there is not a program that
manipulates the data prior to my needing to load it.  It would have
been all too easy to load a HV record after EOF in a prior program. 
Putting a HV dummy record in concatenation is easy enough a solution
as well - but I was sure that there has to be a better way...which is
why I came here.

* This is a new process and no one will need the file before or after
me.  It is only a validation file.  I put toghether the KEY from the
INPUT file, if it is on the VSAM file the record processes.  If it
isn't there on the START command I still need to read the next record
to determine which part(s) are missing so I can report why a record
was rejected.
* Using the File-Status of 46 sounds like a great way to go to me.  If
it comes back then the base element of the KEY is missing and I will
have what I needed.

Should take me 5 minutes to code and test for that.

Thanks again everyone.

> 
> I can sort in a high-values record with the data prior to the IDCAMS
> step,  or I found an ASSEMBLER module that will do this for me, but
> the overhead is not pretty.
```

#### ↳ Re: IDCAMS to load a HIGH VALUES record

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-30T16:15:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bg8qv0$oot$1@peabody.colorado.edu>`
- **References:** `<e0465864.0307290656.117872f0@posting.google.com>`

```

On 29-Jul-2003, studlow1@hotmail.com (The Mean Farmer) wrote:

> Is there a way that a IDCAMS REPRO step can load a VSAM file and then
> put a standard HIGH-VALUES record as the last record on the file?

Load the VSAM file from another file?   Why not concatenate the other file with
a high values record?
```

#### ↳ Re: IDCAMS to load a HIGH VALUES record

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-30T16:17:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bg8r36$op1$1@peabody.colorado.edu>`
- **References:** `<e0465864.0307290656.117872f0@posting.google.com>`

```

On 29-Jul-2003, studlow1@hotmail.com (The Mean Farmer) wrote:

> I have a file that I will have to access randomly using START, then
> READ NEXT.  If I am beyond the last record with the START command with
…[7 more quoted lines elided]…
> the overhead is not pretty.

I prefer a programming solution to creating a fake data record here.   Any
reason why you don't?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
