[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL ISPF problem

_6 messages · 6 participants · 1997-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### COBOL ISPF problem

- **From:** "steven hughes" <ua-author-794783@usenetarchives.gap>
- **Date:** 1997-03-20T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<333305FD.7CCC@netcomuk.co.uk>`

```

Hi,
I've recently put together several COBOL/ISPF/DB2 programs and they
execute as specified. Another programmer then split-screen and tried to
execute the same program in the second session.

It died. S0C4 in an IGZ module.

Turns out (I talked to IBM in London) that COBOLII won't allow
multi-tasking, which is apparently what happens is split-screen mode.

I'd previously written ISPF applications in PL/1 and never given this
any thought.

Anybody else encounter/know of this "feature" of COBOLII?

Steven.

P.S. Is it me noticing or is there an increase in the job ads in this
NG?
```

#### ↳ Re: COBOL ISPF problem

- **From:** "bill scofield" <ua-author-17072578@usenetarchives.gap>
- **Date:** 1997-03-21T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b7d05e3aa-p2@usenetarchives.gap>`
- **In-Reply-To:** `<333305FD.7CCC@netcomuk.co.uk>`
- **References:** `<333305FD.7CCC@netcomuk.co.uk>`

```

Steven Hughes wrote:

Hi,
I've recently put together several COBOL/ISPF/DB2 programs and
they
execute as specified. Another programmer then split-screen and
tried to
execute the same program in the second session.

It died. S0C4 in an IGZ module.

Turns out (I talked to IBM in London) that COBOLII won't allow
multi-tasking, which is apparently what happens is split-screen
mode.

I'd previously written ISPF applications in PL/1 and never given
this
any thought.

Anybody else encounter/know of this "feature" of COBOLII?

Steven.

P.S. Is it me noticing or is there an increase in the job ads in
this
NG?

Hi Steve,
we've had the same problem for the last 10 years and haven't been
able to get round it. A work round we use is to set a flag whenever a
COBOL program was started, then if the user attempted to start a second
COBOL program, display a warning screen. When the first program
completes, clear the flag.
If you find a more eligant solution, please let me know.

Bill
```

#### ↳ Re: COBOL ISPF problem

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-03-21T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b7d05e3aa-p3@usenetarchives.gap>`
- **In-Reply-To:** `<333305FD.7CCC@netcomuk.co.uk>`
- **References:** `<333305FD.7CCC@netcomuk.co.uk>`

```

This feature is a problem related to the RES option of COBOL, and will affect both V4, OS/VS, and VS COBOL II applications.

It is (I beleive) finally fixed in COBOL/370 / COBOL for MVS and VM with the corresponding LE/370 run-time.

Known to have happened in the early 80's with OS/VS COBOL, then continued to occur with VS COBOL II.

Known requirement against both of those products for 10 or 15 years.

Interim solution - do not split screen while driving COBOL aps, or at least avoid COBOL on both sides of the screen.

Rex Widmer
Builder of software archeology tools and other strange programs to help survive in a legacy based world.
```

##### ↳ ↳ Re: COBOL ISPF problem

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1997-03-27T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b7d05e3aa-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b7d05e3aa-p3@usenetarchives.gap>`
- **References:** `<333305FD.7CCC@netcomuk.co.uk> <gap-8b7d05e3aa-p3@usenetarchives.gap>`

```

In <199··.@lad··l.com>, rwi··.@a··.com writes:
› This feature is a problem related to the RES option of COBOL.

If RES is the problem, I wonder if simply compiling the program
with NORES would solve it?

You could also issue a ISPLINK CONTROL SPLIT DISABLE at the start
of the application to keep them from doing it in the first place.
Not much help though if you're already in split screen I guess. ;)
```

#### ↳ Re: COBOL ISPF problem

- **From:** "r..." <ua-author-43843@usenetarchives.gap>
- **Date:** 1997-03-21T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b7d05e3aa-p5@usenetarchives.gap>`
- **In-Reply-To:** `<333305FD.7CCC@netcomuk.co.uk>`
- **References:** `<333305FD.7CCC@netcomuk.co.uk>`

```

In article <333··.@net··o.uk>
› hug··.@net··o.uk "Steven Hughes" writes:
› [snip]
› P.S.  Is it me noticing or is there an increase in the
› job ads in this NG? [comp.lang.cobol]

They are increasing in number, and the discussions about rates
of pay etc cross-posted here seem to make it worse.

The advertisers I have emailed about this often respond:
"Well, I saw the other adverts and assumed it would be OK".

It isn't OK. Please don't advertise on comp.lang.cobol, go to one
where they *invite* you to advertise, eg:

biz.jobs.offered
comp.jobs, comp.jobs.offered
misc.jobs.contract, misc.jobs.misc
misc.jobs.offered, misc.jobs.offered.entry
uk.jobs.offered, uk.jobs.contract
... etc

Thanks
Richard Ross-Langley
```

#### ↳ Re: COBOL ISPF problem

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1997-03-31T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b7d05e3aa-p6@usenetarchives.gap>`
- **In-Reply-To:** `<333305FD.7CCC@netcomuk.co.uk>`
- **References:** `<333305FD.7CCC@netcomuk.co.uk>`

```

Steven Hughes wrote:

› Hi,
›   I've recently put together several COBOL/ISPF/DB2 programs and they
› execute as specified.  Another programmer then split-screen and tried to
› execute the same program in the second session.
 
›  It died.  S0C4 in an IGZ module.
 
›  Turns out (I talked to IBM in London) that COBOLII won't allow
› multi-tasking, which is apparently what happens is split-screen mode.
 
›  I'd previously written ISPF applications in PL/1 and never given this
› any thought.   
 
›  Anybody else encounter/know of this "feature" of COBOLII?
 
› Steven.
 
› P.S.  Is it me noticing or is there an increase in the job ads in this
› NG?

I've always had that problem with COBOL2/ISPF. The only solution I've
came up with is to exit out the last splited screen frist. I've
noticed the "feature" went away when I recompiled everything to
COBOL/370.

Hope this helps,
Boyce G. Williams, Jr.

.---------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a |
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon |
'---------------------------------------------------------------------'
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
