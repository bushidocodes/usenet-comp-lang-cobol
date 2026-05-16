[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Displaying the contents of pointers in cobol...

_5 messages · 3 participants · 2005-01_

---

### Displaying the contents of pointers in cobol...

- **From:** "XPPROGRAMMER" <saud_abraham@hotmail.com>
- **Date:** 2005-01-25T11:17:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106680669.666956.203090@z14g2000cwz.googlegroups.com>`

```
Hello,

how do I display the content of a data-pointer and pointer
items in cobol? Case in point:

01  data-pointer   typedef pointer.
01  LPTSTR         typedef usage data-pointer.
01  Array is typedef.
03  CBsize      UINT.
03  Uflags      UINT.
03  lpszText1   pointer.
03  uId         UINT.
03  ToolRect    RECT.
03  hinst       HINSTANCE.
03  lpszText2   LPTSTR.

if lpszText1 and lpszText2 have received a text string,
how can I use the redefine clause to display the text?
thanks for the help.
```

#### ↳ Re: Displaying the contents of pointers in cobol...

- **From:** epc8@juno.com
- **Date:** 2005-01-25T12:35:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106685346.500989.252150@f14g2000cwb.googlegroups.com>`
- **References:** `<1106680669.666956.203090@z14g2000cwz.googlegroups.com>`

```
XPPROGRAMMER wrote:
> Hello,
>
…[16 more quoted lines elided]…
> thanks for the help.

1. A pointer contains an address (or equivalent) so displaying its
contents will be of no help to you.

2. REDEFINES simply allows different views of the same data item, for
example both as a string of characters and as a string of digits. This
does not apply either.

3. It looks like you are calling a Windows API. Usually the details of
passing variables by reference are taken care of in the linkage section
and by the syntax of the CALL.

AFAIK, COBOL does not have an operator which de-references a pointer,
as you would do in C, which is something that returns what the pointer
is pointing at. So if you are actually passing a data structure which
contains pointers to a routine, then you have to point them at other
appropriate data structures yourself.
```

##### ↳ ↳ Re: Displaying the contents of pointers in cobol...

- **From:** "XPPROGRAMMER" <saud_abraham@hotmail.com>
- **Date:** 2005-01-25T13:26:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106688369.667121.133860@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1106685346.500989.252150@f14g2000cwb.googlegroups.com>`
- **References:** `<1106680669.666956.203090@z14g2000cwz.googlegroups.com> <1106685346.500989.252150@f14g2000cwb.googlegroups.com>`

```

epc8@juno.com wrote:

> 1. A pointer contains an address (or equivalent) so displaying its
> contents will be of no help to you.
>
> 2. REDEFINES simply allows different views of the same data item, for
> example both as a string of characters and as a string of digits.
This
> does not apply either.
>
> 3. It looks like you are calling a Windows API. Usually the details
of
> passing variables by reference are taken care of in the linkage
section
> and by the syntax of the CALL.
>
> AFAIK, COBOL does not have an operator which de-references a pointer,
> as you would do in C, which is something that returns what the
pointer
> is pointing at. So if you are actually passing a data structure which
> contains pointers to a routine, then you have to point them at other
> appropriate data structures yourself.
John Wrote:
thanks for your reply.

john.
```

#### ↳ Re: Displaying the contents of pointers in cobol...

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-25T14:15:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106691325.815606.39790@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1106680669.666956.203090@z14g2000cwz.googlegroups.com>`
- **References:** `<1106680669.666956.203090@z14g2000cwz.googlegroups.com>`

```
> how can I use the redefine clause to display the text?

The redefine won't be of any use.  You dereference using LINKAGE
SECTION.

Create an appropriate record item in linkage section and (depending on
compiler):

SET ADDRESS OF linkage-record   TO pointer-name

Then use linkage-record fields as if they were working-storage items.
```

##### ↳ ↳ Re: Displaying the contents of pointers in cobol...

- **From:** "XPPROGRAMMER" <saud_abraham@hotmail.com>
- **Date:** 2005-01-25T14:23:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106691824.290249.198380@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1106691325.815606.39790@f14g2000cwb.googlegroups.com>`
- **References:** `<1106680669.666956.203090@z14g2000cwz.googlegroups.com> <1106691325.815606.39790@f14g2000cwb.googlegroups.com>`

```

Richard wrote:
> > how can I use the redefine clause to display the text?
>
…[3 more quoted lines elided]…
> Create an appropriate record item in linkage section and (depending
on
> compiler):
>
> SET ADDRESS OF linkage-record   TO pointer-name
>
> Then use linkage-record fields as if they were working-storage items.
John Wrote:

thanks a lot richard, very clever solution.
John.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
