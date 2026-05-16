[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Windows or MicroFocus NetExpress Problem???

_1 message · 1 participant · 1998-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Re: Windows or MicroFocus NetExpress Problem???

- **From:** "Gael Wilson" <gw@mfltd.co.uk>
- **Date:** 1998-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd9f62$619a8590$905481c1@gw-nt>`
- **References:** `<6mg8b1$6u1$1@camel18.mindspring.com> <01bd9db8$9606c010$905481c1@gw-nt> <6mlk5g$q7d$1@camel25.mindspring.com>`

```



kenmullins@mindspring.com wrote in article
<6mlk5g$q7d$1@camel25.mindspring.com>...
> 
> <snip>
> 
> >The problem occurs because the entry names and associated program
> >information are stored globally inside the run-time system, and
therefore
> >there is a problem when an attempt to load more than one program/entry
> >point with a name matching one already loaded is made.
…[7 more quoted lines elided]…
> existing module first...If it is then use it...

Ken, as someone who has a wealth of experience I'm sure you will appreciate
that problems are almost always much more complex once you get into the
actual details than they appear at a glance. However, despite the fact that
I could describe at great length what is occurring at a low-level it won't
be of any help in resolving your problems. So, I'll focus on what may be
possible to help overcome them.

> 
> >However, the duplicate named code should only be loaded if it is
directly
> >referenced suggesting that the calls to your date/time routines are
> >LITLINKed, either by use of the directive or CALL-CONVENTION. So, if the
> >routines are actually the same, the workaround is to remove the LITLINK
and
> >it will work because the run-time will then use the same version each
time
> >it is called. If, however, the routines are actually different I'm
afraid
> >your only option is to rename them.
> 
> I tried an experiment this morning after reading your posting...I added a
> second and unique entry point to the obj being called...When I call the
new
> entry point from the .dll, I receive the same internal error message,
even
> though I am calling a unique entry point...I guess this confirms that you
> cannot use litlink...The problem there is that we have many thousand of
> lines of code that would have to be modified, retested, etc...Our
> applications are native windows api applications, and it is my
understanding
> that litlink is a requirement...
> 
> Any other suggestions that might get us around this problem...
> 

I believe that the reason you continued to encounter the error after making
changes is that despite the fact that you have used a uniqely named entry
point, presumably the program name or program-id is not unique.

LITLINK is not actually a requirement for native Windows API applications.
I would certainly recommend it for Win32 API calls to ensure maximum
efficiency but it is not actually necessary. That being so, my suggestion
would be to use CALL-CONVENTIONs for calls to the APIs and normal calls (ie
non-LITLINKed) for the COBOL programs or entries. From what you have said
above, if that involves too many changes I suspect you will need to supply
somebody in Technical Support with an example to determine whether there
are any other alternatives.

> >> Is the problem a MicroFocus runtime problem, or a Windows restriction
on
> >the
> >> use of entry point names???
…[3 more quoted lines elided]…
> >entry names, it is not a Windows problem, and we are working on changes
at
> >present.
> 
> 
> Can you give some additional insight...When do you expect to deliver the
> correction...

As I'm not representing Micro Focus in any official capacity on the
newsgroup (being a humble developer) I'm not in a position to be able to
say specifically when the change will appear. 
All I can suggest is that you contact your sales representative for
infomation. Unofficially though, next release would be a reasonable
expectation.

> 
> THIS IS INDEED A MAJOR, MAJOR BUG...
…[3 more quoted lines elided]…
> 

Yes, I fully accept that for your application this is a major problem and I
did acknowledge that in my previous reply. However, the situation you have
described is actually quite rare which is why it was not addressed until
recently.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
