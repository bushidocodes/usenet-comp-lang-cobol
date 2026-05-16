[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to restore PDS member statistics

_2 messages · 2 participants · 2002-02_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to restore PDS member statistics

- **From:** Håkan Sjunnestrand <sjunnestrand@mac.com>
- **Date:** 2002-02-11T11:28:41+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C679CD9.CEEE6BC@mac.com>`

```
I send a job from my PC to a IBM Mainframe. The job have two steps.
First a IEBGENER step that save data transfered from the PC in a PDS
member. The second job step is a start of a REXX procedure. When
IEBGENER save in the PDS member I don't get any PDS statistics - I
mostly want change date and user ID. How can I generate this
information, in the IEBGENER step or in the REXX procedure?

/Hï¿½kan
```

#### ↳ Re: How to restore PDS member statistics

- **From:** Steve Thompson <sthompsonNOSPAM@ix.netcom.com>
- **Date:** 2002-02-11T07:03:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C67B31C.A738BA20@ix.netcom.com>`
- **References:** `<3C679CD9.CEEE6BC@mac.com>`

```
Hï¿½kan Sjunnestrand wrote:
> 
> I send a job from my PC to a IBM Mainframe. The job have two steps.
…[6 more quoted lines elided]…
> /Hï¿½kan

IEBGENER will not put out the "USER" part of the PDS
entries. Probably the easiest way for you to deal with this
is via REXX and calling ISPF routines. There are a few which
will allow you to "edit" the file you have loaded via
IEBGENER. By setting certain options, you will be able to
get the editor to put out the stats in such a way that it
appears that you were the one that did the edit.

If on the other hand, you would like to have some real fun,
you can get your REXX code to read the PDS directory and
UPDATE it with the stats. I suggest dumping a PDS directory
that has the stats already in it so that you can see what it
is you are after. Be sure to take a careful look at the I/O
manuals that spell out how a directory block is built.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
