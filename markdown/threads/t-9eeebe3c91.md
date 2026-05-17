[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol to run under windows over a Novell Network

_2 messages · 2 participants · 1996-04_

---

### Cobol to run under windows over a Novell Network

- **From:** "jo..." <ua-author-754048@usenetarchives.gap>
- **Date:** 1996-04-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<829167922.3081@smithjd.demon.co.uk>`

```
Wonder if anyone can help, I have a friend who is currently running
his business on a comart multi user
PC under concurrent CP/M86 all his applications are bespoke written in
MciroFocus Level II COBOL.
We are looking for upgrade options preferably involving as little code
change as possible and easy
migration (we can all hope )

I admit to having been out of the COBOL arena for a long time and
wonder if anyone can suggest a
suitable compiler and runtime set-up preferable running across a Novel
3.12 network allowing multi-
access to the files.

Thanks

JD Smith

jo··.@smi··o.uk
```

#### ↳ Re: Cobol to run under windows over a Novell Network

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-04-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9eeebe3c91-p2@usenetarchives.gap>`
- **In-Reply-To:** `<829167922.3081@smithjd.demon.co.uk>`
- **References:** `<829167922.3081@smithjd.demon.co.uk>`

```
In message <<829··.@smi··o.uk>> jo··.@smi··o.uk writes:
› his business on a comart multi user 
› PC under concurrent CP/M86 all his applications are bespoke written in
…[3 more quoted lines elided]…
› migration (we can all hope ) 

The fact that you say Concurrent-CP/M-86 implies a very old version.
It went from CCP/M-86 3.1 to Concurrent-DOS 4.1, 5.1, 6.x, to
CDOS-386 versions 1,2,3, then to DR-Multiuser-DOS 5.0, 5.1 and
is available in developed forms as DataPac's System Manager and
IMS's Real:32 and CCS's something-or-other.

The latest derivatives of this OS are full 32bit Operating systems
that support networking, running Windows 3.11, DOS programs and
still run CP/M-86 and MP/M-86 programs.

They still support multi-tasking on the terminals which may be
'dumb' PC-TERM terminals, remote dial-in, or networked PCs.

I have clients on these systems still using the Cobol systems
they ran on ICL Quattros and ICL DRS300s. ]

› 
› I admit to having been out of the COBOL arena for a long time and
…[3 more quoted lines elided]…
› access to the files.

Given that you are using CCP/M-86 then the Cobol is likely to be
MF Level II (hopefully 2.54) or RM Cobol. Both of these can be
easily moved to recent compilers.

I have several systems that I still compile for Level II on CCP/M
and for far more modern compilers, and several others that I no
longer compile for the older systems but probably could if it
were _really_ required.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
