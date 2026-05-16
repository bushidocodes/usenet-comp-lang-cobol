[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to write a Callable file handler in Windows environment - Urgent

_3 messages · 2 participants · 2002-06_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to write a Callable file handler in Windows environment - Urgent

- **From:** san@softima.com (san)
- **Date:** 2002-06-07T21:01:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c10d0806.0206072001.a3f69e1@posting.google.com>`

```
Hi All,
   I am new to the area of writing Callable File Handler. I need to
write one for completely windows based application (OS - Windows NT
Workstation) using Visual C++ 6.0 tool. I don't know the exact
syntaxes and the header files included for it. Can anyone help me in
this regard? I am in urgent need to develop this task. If possible
please provide sample code.

Thanks a lot in advance for any help or guidance.

San
```

#### ↳ Re: How to write a Callable file handler in Windows environment - Urgent

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-06-08T07:36:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0206080636.6b6be6fa@posting.google.com>`
- **References:** `<c10d0806.0206072001.a3f69e1@posting.google.com>`

```
There is not enough information here for us to be of much help. 
Here's some questions that might help us to get the information so we
can assist.

Normally when we see "Callable File Handler" it's something like an
"External File Handler" for interfacing with a particular COBOL
vendor's product.  For example, both MicroFocus and Fujitsu have
External file handler specifications so that one may create such a
callable routine and plug it in, in place of or in addition to the
native vendor provided file handler.

Are you talking about writing one of these? 

The other thing we see is a desire to access COBOL data from other
languages via ODBC or via some "callable file handler" invoked from
this other language.  In these cases the handler can be designed in
many different ways.

Which of these are you attempting, or is it something else entirely?



san@softima.com (san) wrote in message news:<c10d0806.0206072001.a3f69e1@posting.google.com>...
> Hi All,
>    I am new to the area of writing Callable File Handler. I need to
…[8 more quoted lines elided]…
> San
```

##### ↳ ↳ Re: How to write a Callable file handler in Windows environment - Urgent

- **From:** san@softima.com (san)
- **Date:** 2002-06-12T00:58:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c10d0806.0206112358.246b7e0b@posting.google.com>`
- **References:** `<c10d0806.0206072001.a3f69e1@posting.google.com> <bfdfc3e8.0206080636.6b6be6fa@posting.google.com>`

```
Hi Thane,
   I am sorry for the ambiguity in my statement. I am talking about
the second of the two cases mentioned by you i.e. I need to write a
IDXFORMAT4 File Editor using Visual C console application, which will
be called from a COBOL application. I will be using the External File
Handler (EXTFH) of MicroFocus. Thanks for trying to help me. I hope to
get a reply soon.

Thanks
San.

thaneh@softwaresimple.com (Thane Hubbell) wrote in message news:<bfdfc3e8.0206080636.6b6be6fa@posting.google.com>...
> There is not enough information here for us to be of much help. 
> Here's some questions that might help us to get the information so we
…[31 more quoted lines elided]…
> > San
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
