[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Call DLL from Screenset

_2 messages · 2 participants · 2004-01_

---

### Call DLL from Screenset

- **From:** bigmarwin@seznam.cz (BigMarwin)
- **Date:** 2004-01-19T02:46:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1c5b0131.0401190246.6fc64b16@posting.google.com>`

```
Hi,
I need to call procedure "Someting" in "somedll.dll" from screenset.
Know somebody how I do this?
Thanks 
BigMarwin
```

#### ↳ Re: Call DLL from Screenset

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2004-01-19T19:46:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0401191946.38a66091@posting.google.com>`
- **References:** `<1c5b0131.0401190246.6fc64b16@posting.google.com>`

```
Lots of assumptions here.

I assume that you are calling it via Dialog System and MicroFocus
COBOL.

You can call the DLL from Dialog - MAYBE - using a COUT.  However, if
this doesn't work for you - wrap the call to the DLL in a COBOL
program and use COUT to do it.

If you are not talking about Dialog system - ignore this message.



bigmarwin@seznam.cz (BigMarwin) wrote in message news:<1c5b0131.0401190246.6fc64b16@posting.google.com>...
> Hi,
> I need to call procedure "Someting" in "somedll.dll" from screenset.
> Know somebody how I do this?
> Thanks 
> BigMarwin
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
