[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Tables In COBOL

_5 messages · 5 participants · 2000-03 → 2000-04_

---

### Tables In COBOL

- **From:** Charles Hammond <ceh1@ritz.cec.wustl.edu>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.SOL.3.96.1000331142224.10088A-100000@ritz.cec.wustl.edu>`

```
I guess I am just used to this small 32 megs of memory and limited by a 4
disk stroage system on this old legacy VSE/ESA System 370.  Maybe I need a
job where they have better equipment.  Or maybe I don't know what it
really can do.

I am used to watching a program run for 15 minutes...

Charles Hammond, BSIM Undergraduate Program
```

#### ↳ Re: Tables In COBOL

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c3pdh01od@enews3.newsguy.com>`
- **References:** `<Pine.SOL.3.96.1000331142224.10088A-100000@ritz.cec.wustl.edu>`

```
15 minutes is not a long time depending on how much work the program is 
doing.

Jeff

----------
In article <Pine.SOL.3.96.1000331142224.10088A-100000@ritz.cec.wustl.edu>,
Charles Hammond <ceh1@ritz.cec.wustl.edu> wrote:


> I guess I am just used to this small 32 megs of memory and limited by a 4
> disk stroage system on this old legacy VSE/ESA System 370.  Maybe I need a
…[6 more quoted lines elided]…
>
```

#### ↳ Re: Tables In COBOL

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c36eu$99$1@slb2.atl.mindspring.net>`
- **References:** `<Pine.SOL.3.96.1000331142224.10088A-100000@ritz.cec.wustl.edu>`

```
Just FYI -
  Both VS COBOL II and the LE COBOL for VSE *do* support 16M tables.  Then
again, they probably "assume" you are running a current VSE system.
```

#### ↳ Re: Tables In COBOL

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uribpO6m$GA.271@cpmsnbbsa04>`
- **References:** `<Pine.SOL.3.96.1000331142224.10088A-100000@ritz.cec.wustl.edu>`

```

Charles Hammond <ceh1@ritz.cec.wustl.edu> wrote in message
news:Pine.SOL.3.96.1000331142224.10088A-100000@ritz.cec.wustl.edu...
> I guess I am just used to this small 32 megs of memory and limited
by a 4
> disk stroage system on this old legacy VSE/ESA System 370.  Maybe I
need a
> job where they have better equipment.  Or maybe I don't know what it
> really can do.
>
> I am used to watching a program run for 15 minutes...
>
 The latest table handling thread (Destroying a COBOL Array) does not
represent a normal application design. I would try to avoid the need
to store all my input in a table.

Most of the time tables are limited to reasonable sizes.
It is better to break a complex operation into simple steps, and
endure the additional I/O overhead.
The added program complexity involved in trying to do it all in one
step will generally increase the program development and maintenance
costs.

The methods you would use, are the methods I would use in OS/390.
```

##### ↳ ↳ Re: Tables In COBOL

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E73F07.7D30E560@iinet.net.au>`
- **References:** `<Pine.SOL.3.96.1000331142224.10088A-100000@ritz.cec.wustl.edu> <uribpO6m$GA.271@cpmsnbbsa04>`

```

DennisHarley wrote:
> 
>  The latest table handling thread (Destroying a COBOL Array) does not
…[10 more quoted lines elided]…
> The methods you would use, are the methods I would use in OS/390.
Actually, this make an important distinction between 'mainframe' and Unix/Windows
style programming.

On a mainframe the cost of I/O to a program is relatively cheap. Odds are that
the Cache controller already has your data in cache, also depending upon the
block size of the data, I/O will ensure that the next record to read is almost always
in the computers memory. What this translates to, is that the 'mainframe' reads
data in HUGE gulps at a time. So the typical technique is to read the data a single
record at a time and attempt to process it directly.

These days, you would not even attempt to handle the problem this way. The users data
would have been loaded into a DB2 or Oracle database, and SQL calls would be made to
retrieve the data. If you used DB2, and you set the appropriate controls on the table,
you could have DB2 read the ENTIRE table into memory. In which case you would be
accessing data in memory - just like an array.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
