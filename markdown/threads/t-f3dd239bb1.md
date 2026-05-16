[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Heeeelp! Cobol, windows 95 and Novell

_2 messages · 2 participants · 1999-03_

---

### Heeeelp! Cobol, windows 95 and Novell

- **From:** zaffy@my-dejanews.com
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7d8i1m$5mo$1@nnrp1.dejanews.com>`

```
what a nasty combination eh?

I use (the ancient) IBM cobol I  and  multi user btrieve for the files.

All this  under Novel Netware 3.12 and (unfortunately) the 2 workstations
 have windows 95B as o/s.

the problem: when the 2 users  try to run the same programme at the same time
 they get a lovely "access denied" message (and this has nothing to do with
btrieve, I have checked).

The same programmes can be accessed with no problem from terminals
 with dos as the main o/s.

Any idea what's up? It's the bloody windows isinit?

I would appreciate any help

Zaffy :)

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Heeeelp! Cobol, windows 95 and Novell

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-BnLrlyC6gIGY@Dwight_Miller.iix.com>`
- **References:** `<7d8i1m$5mo$1@nnrp1.dejanews.com>`

```
On Tue, 23 Mar 1999 17:12:30, zaffy@my-dejanews.com wrote:

> what a nasty combination eh?
> 
…[14 more quoted lines elided]…
> I would appreciate any help

Get the Novell Client 32 drivers from Novells website.  The Microsoft 
Novell drivers "SEEM" designed to frustrate.

Go to your control panel, system settings.  Choose the Performance 
tab, then the File System button. Next, click the troubleshooting tab.
 Make sure the checkbox next to "Disable new file sharing and locking 
semantics".  Apply, and restart the workstations.  

Once you do all this, things will behave much better.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
