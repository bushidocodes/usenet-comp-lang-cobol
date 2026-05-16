[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Errors in Cobol for MVS

_2 messages · 2 participants · 1999-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Errors in Cobol for MVS

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-02-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36D92D71.5FB3673A@zip.com.au>`

```
Bill you offered some help a while ago eliminating some messages for me. 

3825  IGYPS2168-W   "CORRESPONDING" was specified, but subordinate item 
"FILLER" within "TS-DATE" did not qualify according to the rules for the
"CORRESPONDING" phrase.  Subordinate item "FILLER" was ignored.

253  IGYGR1216-I   A "RECORDING MODE" of "F" was assumed for file
"CDR-FILE"

I did state that the recording mode message was a warning.  It is only
an informational.  It would be nice to eliminate this one totally as it
is 'outside the standard'.

I investigated a compile option FLGSTD as this one seemed promising
flagging obsoleted code.  The problem is that this flags everything
COMP-3, FUNCTION, etc.  How do you get a minimise this to truly obsolete
code

Thanks
Ken
```

#### ↳ Re: Errors in Cobol for MVS

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bcef4$oeq@dfw-ixnews10.ix.netcom.com>`
- **References:** `<36D92D71.5FB3673A@zip.com.au>`

```
OK, let's do the easy part first. the FLAGSTD compiler option is the only
way to get OBSOLETE (as defined in the '85 Standard) features flagged.
UNfortunately, it is designed to ALWAYS flag IBM extensions - even if what
you really want is just to see obsolete items.

As for the I-level message for RECORDING MODE F being assumed, what I would
suggest is to "normally" compile with the FLAG(W,W) compiler option and NOT
to get the I-level messages.  I would suggest that you do at least one
compile with FLAG(I) before moving to production - just in case there is
actually something "interesting" - but I have never heard of an I-level IBM
message that would actually get me to change my code.

As for the W-level message on the CORRESPONDING, the obvious (but probably
unworkable) solution is to change to explicit individual MOVE statements.
This fits in with the general "I hate MOVE CORRESPONDING" sentiment in the
world - and the W-level message actually does point out something that COULD
be a maintenance problem.  However, I will pass this note on to someone else
who may have some other ideas on what to do about it.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
