[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Procedure-Pointers and Fujitsu 4.20

_2 messages · 2 participants · 1999-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Procedure-Pointers and Fujitsu 4.20

- **From:** keithwalk@aol.com (KeithWalk)
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990410161411.06183.00001166@ng128.aol.com>`

```
All...

Just for the heck of it I've been trying to convert the classic
"WINHELLO.CBL" MF Cobol source into Fujitsu 4.20 standard Cobol.
To the best of my knowledge, Fujitsu 4.20 has no Procedure-Pointer
capability.  Does anyone have an idea on a work-around that will
allow me to complete this exercise without resorting to PowerCobol.
Thank you!

Keith F. Walker   :-)
```

#### ↳ Re: Procedure-Pointers and Fujitsu 4.20

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37101f35.1357448@news1.ibm.net>`
- **References:** `<19990410161411.06183.00001166@ng128.aol.com>`

```
On 10 Apr 1999 20:14:11 GMT, keithwalk@aol.com (KeithWalk) wrote:

>All...
>
…[5 more quoted lines elided]…
>Thank you!

I've been fiddling with the Windows API and such of late with Fujitsu
COBOL 4.2 no less.  (I like the new directive ALPHAL(WORD) btw).

Anyway, my problem is one of vocabulary.  By a procedure pointer, do
you meat using the MF method of "SET xxxx to ENTRY xxxx"?  If so,
these just are not necessary with Fujitsu COBOL.  You DO need the
Windows API however, which I just downloaded today.  Go to:

http://msdn.microsoft.com/developer/sdk/platform.asp

and download the ibldenv.exe and add the appropriate libraries from
the \lib dir after install, to your project.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
