[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How many files to open at once?

_6 messages · 4 participants · 2000-02_

---

### Re: How many files to open at once?

- **From:** "keldin" <keldin@mciworld.com>
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<x%Kq4.16049$NP6.194779@pm02news>`
- **References:** `<889qd6$fkg$1@watserv3.uwaterloo.ca> <fyoq4.5846$QK6.70448@news4.mia> <88d82c$ivv$1@nntp6.atl.mindspring.net>`

```
Another factor is that the more files you open, espicially on tape.  The
worse run class you are allowed to run in.  Would you rather be in a run
never class. or a faster class with two or three passes through the data....


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:88d82c$ivv$1@nntp6.atl.mindspring.net...
> I read the LRM "limit" as meaning that you could only (gasp) have
>
…[6 more quoted lines elided]…
> problems before you would ever have all of these OPEN at the same time (as
a
> COBOL restriction).
>
…[5 more quoted lines elided]…
> > Bill, I think you are correct there, it seems for some reason, you are
```

#### ↳ Re: How many files to open at once?

- **From:** SimonLElliott <"Simon.L.Elliott[Delete.Me]"@CapGemini.Co.UK>
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ABBD9A.A51FC2C6@CapGemini.Co.UK>`
- **References:** `<889qd6$fkg$1@watserv3.uwaterloo.ca> <fyoq4.5846$QK6.70448@news4.mia> <88d82c$ivv$1@nntp6.atl.mindspring.net> <x%Kq4.16049$NP6.194779@pm02news>`

```

We had a problem a while back with a CICS region that tried to allocate too many
files at one time and we stumbled across this. The following cutting comes from
the OS/390 Initialisation and Tuning Reference and refers to the
SYS1.PARMLIB(ALLOCxx) member.


TIOT
    Specifies the installation defaults for the task I/O table (TIOT)

    SIZE(nn)
        Specifies the size of the TIOT. The TIOT contains an entry for each DD
statement.

        The size of the TIOT controls how many DDs are allowed per jobstep. By
specifying any integer from 16 to 64 as the value of this parameter,
        the installation controls the default DD allowance.

        The following table shows the relationship between the size of the TIOT
and the maximum number of DDs allowed:

            SIZE Value                    Maximum number
            Dec (Hex)    Size of TIOT     of DDs allowed
            16   10      16384 (16K)         816
            24   18      24576 (24K)        1225
            32   20      32768 (32K)        1635
            40   28      40960 (40K)        2045
            48   30      49152 (48K)        2454
            56   38      57344 (56K)        2864
            64   40      65536 (64K)        3273
```

#### ↳ Re: How many files to open at once?

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38AC04CD.C86E3263@cusys.edu>`
- **References:** `<889qd6$fkg$1@watserv3.uwaterloo.ca> <fyoq4.5846$QK6.70448@news4.mia> <88d82c$ivv$1@nntp6.atl.mindspring.net> <x%Kq4.16049$NP6.194779@pm02news>`

```
I suppose the OS has to be able to handle the numbers of files which databases
and on line shell programs require (lots), but I am curious:

What kinds of batch applications want to open large quantities of files at once?

I suppose it could be a ledger program with one file per ledger, but there are
better ways to do this.
```

##### ↳ ↳ Re: How many files to open at once?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88h9vm$4gc$1@nntp3.atl.mindspring.net>`
- **References:** `<889qd6$fkg$1@watserv3.uwaterloo.ca> <fyoq4.5846$QK6.70448@news4.mia> <88d82c$ivv$1@nntp6.atl.mindspring.net> <x%Kq4.16049$NP6.194779@pm02news> <38AC04CD.C86E3263@cusys.edu>`

```
Stipulating that there are DEFINITELY better ways of doing this, I could
imagine a program with 365 (or 366) files for each day of the year. This
would have exceeded the old IBM MVS "255" limit.
```

###### ↳ ↳ ↳ Re: How many files to open at once?

- **From:** "keldin" <keldin@mciworld.com>
- **Date:** 2000-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<936r4.16218$NP6.225236@pm02news>`
- **References:** `<889qd6$fkg$1@watserv3.uwaterloo.ca> <fyoq4.5846$QK6.70448@news4.mia> <88d82c$ivv$1@nntp6.atl.mindspring.net> <x%Kq4.16049$NP6.194779@pm02news> <38AC04CD.C86E3263@cusys.edu> <88h9vm$4gc$1@nntp3.atl.mindspring.net>`

```
Yes, but wouldn't someone make monthly files out of these first. or even a
rolling 12 month file...


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:88h9vm$4gc$1@nntp3.atl.mindspring.net...
> Stipulating that there are DEFINITELY better ways of doing this, I could
> imagine a program with 365 (or 366) files for each day of the year. This
> would have exceeded the old IBM MVS "255" limit.
>
```

##### ↳ ↳ Re: How many files to open at once?

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O5QA4xWe$GA.117@cpmsnbbsa03>`
- **References:** `<889qd6$fkg$1@watserv3.uwaterloo.ca> <fyoq4.5846$QK6.70448@news4.mia> <88d82c$ivv$1@nntp6.atl.mindspring.net> <x%Kq4.16049$NP6.194779@pm02news> <38AC04CD.C86E3263@cusys.edu>`

```

Howard Brazee <howard.brazee@cusys.edu> wrote in message
news:38AC04CD.C86E3263@cusys.edu...
>
> What kinds of batch applications want to open large quantities of files at
once?
>

From what I have seen:

1) There are programs designed to pass a LARGE master file once, and pass
several (usually 15-25) transaction files to other processes. I have seen
this with 24-7 systems which cannot afford to have files off-line for
extended periods of time. They do all end-of-day/week/month processing in a
single pass.
I have used this method to create over 20 extracts from a master for a data
warehouse application.

2) In some shops I have seen files split for parallel processing. Split the
transaction files, and then start n JOBs which run the same programs against
the split files.

I have never seen more that 30 files produced.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
