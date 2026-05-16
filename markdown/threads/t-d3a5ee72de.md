[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EXIT PARAGRAPH, PERFORM...THRU etc. (was: First COBOL compiler)

_1 message · 1 participant · 1998-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax)

---

### Re: EXIT PARAGRAPH, PERFORM...THRU etc. (was: First COBOL compiler)

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 1998-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36586946.7782@swbell.net>`
- **References:** `<eJ4nMCA$x$U2EwSx@hayford.demon.co.uk> <19981119102634.09602.00000036@ng-cr1.aol.com> <Tpc52.297$Sf1.435979@news3.mia> <3655866a.0@news3.uswest.net> <lSl52.587$Gy.710084@news4.mia> <3655f11c.0@news1.ibm.net> <OmB52.1091$Sf1.1090000@news3.mia> <3656ed2c.0@news1.ibm.net> <36579F79.329A@swbell.net> <365828f9.0@news1.ibm.net> <E%V52.1541$Gy.1582910@news4.mia> <365830f2.0@news1.ibm.net> <36585316.E39CBD82@bdssoftware.com>`

```
Scott Ramey wrote:
> 
> It was precisely because COBOL is tedious when processing screen
…[9 more quoted lines elided]…
> on . . .    

[snip]

On a PC, or in most Unix or VMS environments, it is indeed a good
idea to validate each input field as the user enters it.

In some environments, however, this approach is not possible.  If an 
application uses a block-mode terminal such as a 3270, the user can 
spend ten minutes filling in the blanks in a form, but the host 
computer doesn't see any of it he hits the RETURN key (or a PF key, or 
any of several other special keys).  At that point the terminal sends 
an entire screenful of data back to the host, which must validate and 
process the screen as a whole.

The resulting interface is not as nice as one might like because you
don't get immediate feedback even for the grossest of typos.  

In some cases, editing my code and being very finicky, I have taken
too long to edit a single screen of text, and timed out.  The host 
thought I wasn't doing anything and logged me off.  Grrrr.

In CICS, Leif's suggestion (which I have snipped) is the standard
way of doing business.  Do the field-level validations in reverse
order.  Whenever you find an error, put the cursor on the field,
highlight it, and move an appropriate message to the error message
line.  By the time you get to the top, all field-level errors will
be highlighted; the cursor placement and error message will reflect
the last error found, which is the first on the screen.

Michael C. Kasten	mck9@swbell
http://home.swbell.net/mck9/cobol/cobol.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
