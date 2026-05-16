[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Generated paragraph names in LE/COBOL-390

_6 messages · 4 participants · 2001-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Generated paragraph names in LE/COBOL-390

- **From:** Martin@pi-sysprog.de (Martin Truebner)
- **Date:** 2001-10-12T00:27:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5e288797.0110112326.7caa676f@posting.google.com>`

```
I have developed code that uses the hooks in the TGT to create what
was once FLOW (display the last n executed lines).

When I added support for paragraph-names, I found that COBOL generates
virtuell names. These do clobber my trace table- Any way to suppress
them?

to illustrate:  100  PARA1. 
                101      IF A = B 
                102         MOVE C TO D
                103      END-IF
                104      MOVE X TO Y

The trace looks like this  100 PARA1
                           101
                           103 ????
                           104

The 103 entry is a paragraph-entry with a generated name, but no
internal table has the name(of course).

One alternative is to do the analysis at creation. But this is way to
much overhead. Right now I only analyse the trace-table in case of an
abend.

Is there a way to convince COBOL (in OS or VSE) not to generate this
useless code.

Martin
```

#### ↳ Re: Generated paragraph names in LE/COBOL-390

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2001-10-12T10:41:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BC6C815.3977801F@istar.ca>`
- **References:** `<5e288797.0110112326.7caa676f@posting.google.com>`

```
Since the procedure division map is basically the resulting assembler
code the virtual paragraph names are assembler tags needed so that the
assembler can be read and in the rare case of a bug, verified.

Martin Truebner wrote:
> 
> I have developed code that uses the hooks in the TGT to create what
…[27 more quoted lines elided]…
> Martin
```

##### ↳ ↳ Re: Generated paragraph names in LE/COBOL-390

- **From:** martin@pi-sysprog.de (Martin Truebner)
- **Date:** 2001-10-14T06:05:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52635377.0110140505.382baebe@posting.google.com>`
- **References:** `<5e288797.0110112326.7caa676f@posting.google.com> <3BC6C815.3977801F@istar.ca>`

```
Clark,

>> ...virtual paragraph names are assembler tags needed so that the
assembler can be read and in the rare case ....<<

I understand the need for it and it is also nice for human readers
that they are indicated in the assembler-listing of the procedure
division.

I doubt that there is any use for the BAL generated to the hook in the
TGT.

or again with a sample 

   100 LABEL   generates a BAL R14,LABELHOOK
   101         generates a BAL R14,INSTRHOOK
   103 GN02    generates a BAL R14,LABELHOOK      


Martin
```

#### ↳ Re: Generated paragraph names in LE/COBOL-390

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-12T07:54:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9q6p7r$20r$1@nntp9.atl.mindspring.net>`
- **References:** `<5e288797.0110112326.7caa676f@posting.google.com>`

```
If you want a "READY TRACE" facility - why not use what IBM documents as the
way to do this?

See:
 http://publib.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igymg202/4.1.5?

and go down to the section called,
  "READY TRACE and RESET TRACE statements"

  ***

As far as "last n statements" - I assume you don't have a decent debugger -
so you have to "play" with TGT, etc.  This does mean that you will probably
have to modify your "analysis" tool every release or two - as IBM *does*
change their code generation about that often.
```

##### ↳ ↳ Re: Generated paragraph names in LE/COBOL-390

- **From:** martin@pi-sysprog.de (Martin Truebner)
- **Date:** 2001-10-14T06:09:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52635377.0110140509.64433ae9@posting.google.com>`
- **References:** `<5e288797.0110112326.7caa676f@posting.google.com> <9q6p7r$20r$1@nntp9.atl.mindspring.net>`

```
Bill,

>> If you want a "READY TRACE" facility ...<<

>> ...debugger ..<<

I do not want either. I want a substitute for what was FLOW=nn. Not as
expensive (pathlengthwise) as READY TRACE and therefor usable for
production-programs.

Martin
```

###### ↳ ↳ ↳ Re: Generated paragraph names in LE/COBOL-390

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2001-10-14T13:44:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tFgy7.292$or2.78481571@newssvr17.news.prodigy.com>`
- **References:** `<5e288797.0110112326.7caa676f@posting.google.com> <9q6p7r$20r$1@nntp9.atl.mindspring.net> <52635377.0110140509.64433ae9@posting.google.com>`

```
    I include my own home-grown version of a trace table in most new
programs these days.  It stores the most recent paragraph names and upon
encountering an abend condition, I display this trace table.  In the event
of an unexpected abend, the trace table can be located in the dump.  I can
e-mail the code to you if you like.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
