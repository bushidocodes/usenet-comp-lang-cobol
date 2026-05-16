[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol for 0S/390 VSAM-Filest. 39

_12 messages · 3 participants · 1998-10_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Cobol for 0S/390 VSAM-Filest. 39

- **From:** Hans-Georg Decker <Decker@kzvk.de>
- **Date:** 1998-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3619FD1D.7E8451D7@kzvk.de>`

```
Hi,

in our company we try to go from IBM-COBOL II to COBOL for
OS/390 & VM.

Now I have a problem:

In a program I have a VSAM-File with a variable
record-length (a fix part plus a part with OCCURS DEPENDING
ON).  Under COBOL II it works fine.

I changed no cluster-information.

The test under the run-time modules of COBOL for OS/390
results an filestatus 39 from the OPEN-statement for that
Vsam-file. When I compile the program with the new compiler
I get the same result.

Did anything have had the same Problem? Who can help me?

Does anyone in germany use the new compiler too?

Geetings Georg
```

#### ↳ Re: Cobol for 0S/390 VSAM-Filest. 39

- **From:** John Calahan <jcalahan@magpage.com>
- **Date:** 1998-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vdpdl$6vo$0@204.179.92.50>`
- **References:** `<3619FD1D.7E8451D7@kzvk.de>`

```
Georg,

I've experienced the same problem recently. To correct this, add this line
to your file's FD statement in your program:

        RECORD VARYING FROM 1 TO XXXX CHARACTERS

where XXXX represents your maximum record length.

Hope this helps,

John 

On Tue, 6 Oct 1998, Hans-Georg Decker wrote:

> Hi,
> 
…[23 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol for 0S/390 VSAM-Filest. 39

- **From:** Hans-Georg Decker <Decker@kzvk.de>
- **Date:** 1998-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361B6ACC.2635DECE@kzvk.de>`
- **References:** `<3619FD1D.7E8451D7@kzvk.de> <6vdpdl$6vo$0@204.179.92.50>`

```
John Calahan schrieb:

> Georg,
>
…[6 more quoted lines elided]…
>

Hi John,

the code in the program is

FD RBESTT
      RECORD CONTAINS 4160 to 25146 CHARACTERS.

Do you have had the same clause before and then changed it to RECORD VARYING
...?

Thanks,

Georg
```

###### ↳ ↳ ↳ Re: Cobol for 0S/390 VSAM-Filest. 39

- **From:** John Calahan <jcalahan@magpage.com>
- **Date:** 1998-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vg5j3$o5l$0@204.179.92.50>`
- **References:** `<3619FD1D.7E8451D7@kzvk.de> <6vdpdl$6vo$0@204.179.92.50> <361B6ACC.2635DECE@kzvk.de>`

```
Georg,

If you've already got that line in there, the next thing I'd look at is
how your VSAM cluster is defined. The definition should be 4 bytes longer
than the record description in the program (COBOL ignores the RDW at the
beginning of both VSAM and QSAM files in its record layouts, from what I
can see). If that doesn't work, let me know. 

John 

On Wed, 7 Oct 1998, Hans-Georg Decker wrote:

> John Calahan schrieb:
> 
…[25 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol for 0S/390 VSAM-Filest. 39

_(reply depth: 4)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361bd0a7.0@news2.uswest.net>`
- **References:** `<3619FD1D.7E8451D7@kzvk.de> <6vdpdl$6vo$0@204.179.92.50> <361B6ACC.2635DECE@kzvk.de> <6vg5j3$o5l$0@204.179.92.50>`

```

John Calahan wrote in message <6vg5j3$o5l$0@204.179.92.50>...
>Georg,
>
…[4 more quoted lines elided]…
>can see). If that doesn't work, let me know.


Doesn't the VSAM Control Interval's (CI's) Control Interval Descriptor Field
(CIDF) and Record Descriptor Field (RDF) handle the variable nature of the
records automatically through Access Method Services (AMS)?

I would think that  RECORDSIZE (4160 25160) would be what was required (i.e.
no adjustment of lrecls due to using variable length records, as would be
done with physical sequential files).

>John
>
…[6 more quoted lines elided]…
>> > I've experienced the same problem recently. To correct this, add this
line
>> > to your file's FD statement in your program:
>> >
…[12 more quoted lines elided]…
>> Do you have had the same clause before and then changed it to RECORD
VARYING
>> ...?
>>
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol for 0S/390 VSAM-Filest. 39

_(reply depth: 4)_

- **From:** Hans-Georg Decker <Decker@kzvk.de>
- **Date:** 1998-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361CA7F0.827018F5@kzvk.de>`
- **References:** `<3619FD1D.7E8451D7@kzvk.de> <6vdpdl$6vo$0@204.179.92.50> <361B6ACC.2635DECE@kzvk.de> <6vg5j3$o5l$0@204.179.92.50>`

```
Hi John,
hi Chris,

thank you for your answers and for your help -

Now I have found the solution:

File-status 39 wasn't an errror in the record-length or
cluster-definition.
The error results from an empty alternate-index.

For explain (I asume you are interested):

In the Programm, I load (with open output) a VSAM-File (by
the way: with variable recordlength).
This file has an alternate record too. First I create the
file (cluster) with IDCAMS and NULLFILE and
then run BLDINDEX. Past it works very fine - but now we are
testing the new Cobol-Compiler :-(

How did I found the error: In the SELECT-statement I coded
the optional data-name-2 in the file-status-claus
and the 3 fields with COMP in the working-storage section.
I got the return-code 04 and the reason-code 100.  For
interpreting this codes you have
to see the manual DFSMS/MVS Macro Instructions for Data
Sets.
Caution ==> 04 means: >Data set was opened successfully, but
an attention message were issued<.
                    But the file wasn't opened!!!!

Now I have removed the alternate-key clause in the program
and run the BLDINDEX after the
program.

So, I hope my english (incl. grammar) was good enough and
you do understand me!

Greetings from Cologne
Georg
```

###### ↳ ↳ ↳ Re: Cobol for 0S/390 VSAM-Filest. 39

_(reply depth: 5)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361cc38a.0@news2.uswest.net>`
- **References:** `<3619FD1D.7E8451D7@kzvk.de> <6vdpdl$6vo$0@204.179.92.50> <361B6ACC.2635DECE@kzvk.de> <6vg5j3$o5l$0@204.179.92.50> <361CA7F0.827018F5@kzvk.de>`

```
Is the program working now?


Hans-Georg Decker wrote in message <361CA7F0.827018F5@kzvk.de>...
>Hi John,
>hi Chris,
…[39 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol for 0S/390 VSAM-Filest. 39

_(reply depth: 6)_

- **From:** Hans-Georg Decker <Decker@kzvk.de>
- **Date:** 1998-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361DAA13.DA7F2B57@kzvk.de>`
- **References:** `<3619FD1D.7E8451D7@kzvk.de> <6vdpdl$6vo$0@204.179.92.50> <361B6ACC.2635DECE@kzvk.de> <6vg5j3$o5l$0@204.179.92.50> <361CA7F0.827018F5@kzvk.de> <361cc38a.0@news2.uswest.net>`

```


Chris Osborne schrieb:

> Is the program working now?
>

Yes, Chris, I have explain the correction in my message before

Georg
```

##### ↳ ↳ Re: Cobol for 0S/390 VSAM-Filest. 39

- **From:** Hans-Georg Decker <Decker@kzvk.de>
- **Date:** 1998-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361B7E1B.2362A7BF@kzvk.de>`
- **References:** `<3619FD1D.7E8451D7@kzvk.de> <6vdpdl$6vo$0@204.179.92.50>`

```
John Calahan schrieb:

> Georg,
>
…[4 more quoted lines elided]…
>

Hi John,

now I have had time to try with your clause ... VARYING FROM 4160 to 25146 ...

(4160 Byte is the fix part plus max.1500 x 14 Byte for the occurs part

 07      I16BA-ABDATEN      OCCURS 1 TO 1500
                            DEPENDING ON I16BN-ANZ IN I16B.
)
, but I get File-Status 39 again.

I get no compiler-error, only this run-time-error. Is this an problem with the
new
run-time-modules.

By the way: the Vsam-DEFINE-Cluster for that file is  ... RECORDSIZE(4160
25146) - ..
and I also tried it with 4160 25150

Georg
```

###### ↳ ↳ ↳ Re: Cobol for 0S/390 VSAM-Filest. 39

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361b8cdf.0@news2.uswest.net>`
- **References:** `<3619FD1D.7E8451D7@kzvk.de> <6vdpdl$6vo$0@204.179.92.50> <361B7E1B.2362A7BF@kzvk.de>`

```
Hans-Georg Decker wrote in message <361B7E1B.2362A7BF@kzvk.de>...
>John Calahan schrieb:
>
>> Georg,
>>
>> I've experienced the same problem recently. To correct this, add this
line
>> to your file's FD statement in your program:
>>
…[5 more quoted lines elided]…
>now I have had time to try with your clause ... VARYING FROM 4160 to 25146
...
>
>(4160 Byte is the fix part plus max.1500 x 14 Byte for the occurs part
…[6 more quoted lines elided]…
>I get no compiler-error, only this run-time-error. Is this an problem with
the
>new
>run-time-modules.
…[6 more quoted lines elided]…
>


Um, forgive me if I did this wrong (or if the 25150 above is just a typo on
your part when entering this info):

1500 x 14 = 21000
21000 + 4160 = 25160

(25146 or 25150) <> 25160, and you've been typing in 25146 and 25150.  Try
changing to 25160 and see what happens.
```

#### ↳ Re: Cobol for 0S/390 VSAM-Filest. 39

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361a6fa8.0@news2.uswest.net>`
- **References:** `<3619FD1D.7E8451D7@kzvk.de>`

```
Please post the relevant code.


Hans-Georg Decker wrote in message <3619FD1D.7E8451D7@kzvk.de>...
>Hi,
>
…[21 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol for 0S/390 VSAM-Filest. 39

- **From:** Hans-Georg Decker <Decker@kzvk.de>
- **Date:** 1998-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361B6B40.548F8F9B@kzvk.de>`
- **References:** `<3619FD1D.7E8451D7@kzvk.de> <361a6fa8.0@news2.uswest.net>`

```
Chris Osborne schrieb:

> Please post the relevant code.
>

Hi Chris,

thanks for the answer.

The code see in my answer to John.

Georg
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
