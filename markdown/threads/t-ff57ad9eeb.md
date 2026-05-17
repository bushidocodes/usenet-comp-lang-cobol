[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Windows or MicroFocus NetExpress Problem???

_4 messages · 2 participants · 1998-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Windows or MicroFocus NetExpress Problem???

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1998-06-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6mg8b1$6u1$1@camel18.mindspring.com>`

```

I have recently encountered a problem developing a Micro Focus cobol
application for Windows...I have tons of .cbl members that get compiled as
.objs...An example would be say, some date and time routines...10 entry
points in the .obj...These entry points are called by the various .exe and
.dll files for the project...

Using the .obj in a normal windows program calling the individual entry
points is no problem...However if I try to call an entry point in a Micro
Focus cobol DLL that includes the same date and time .obj with the 10 entry
points, I receive

"200 - Runtime System Internal Logic Error (in ldobj.c:27, line 357)" and
the application abends...

The problem is obviously because of the duplicate entry points in the .exe
and in the .dll being called by the .exe...Easily recreateable and is
currently being "researched" by MF tech support...A similar problem was
reported back in the VISOC days, but nothing for NetExpress...

Has anyone else encountered this problem...???

Is there a workaround that would allow the same .obj to be in and .exe and a
.dll at the same time without having 2 sets of source and entry point
names???

Is the problem a MicroFocus runtime problem, or a Windows restriction on the
use of entry point names???

Any asistance would be greatly appreciated...


Thanks

KenMullins
Atlanta, GA
```

#### ↳ Re: Windows or MicroFocus NetExpress Problem???

- **From:** "gael wilson" <ua-author-6589191@usenetarchives.gap>
- **Date:** 1998-06-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff57ad9eeb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6mg8b1$6u1$1@camel18.mindspring.com>`
- **References:** `<6mg8b1$6u1$1@camel18.mindspring.com>`

```



ken··.@min··g.com wrote in article
<6mg8b1$6u1$1.··.@cam··g.com>...
› I have recently encountered a problem developing a Micro Focus cobol
› application for Windows...I have tons of .cbl members that get compiled
…[21 more quoted lines elided]…
› Has anyone else encountered this problem...???

Yes, a couple of people have encountered this problem. As you suspected,
the problem occurs because the same entry point names exist in more than
one module.

› 
› Is there a workaround that would allow the same .obj to be in and .exe
…[3 more quoted lines elided]…
› 

The problem occurs because the entry names and associated program
information are stored globally inside the run-time system, and therefore
there is a problem when an attempt to load more than one program/entry
point with a name matching one already loaded is made.

The reason behind that is that it is not possible to identify a specific
module when doing a call ie when you do CALL 'X' and 'X' is in more than
one module, which module should be used ?

However, the duplicate named code should only be loaded if it is directly
referenced suggesting that the calls to your date/time routines are
LITLINKed, either by use of the directive or CALL-CONVENTION. So, if the
routines are actually the same, the workaround is to remove the LITLINK and
it will work because the run-time will then use the same version each time
it is called. If, however, the routines are actually different I'm afraid
your only option is to rename them.

› Is the problem a MicroFocus runtime problem, or a Windows restriction on
› the
› use of entry point names???
›

The problem is a restriction in the way the MicroFocus runtime handles
entry names, it is not a Windows problem, and we are working on changes at
present.

› Any asistance would be greatly appreciated...
› 
…[8 more quoted lines elided]…
› 

I hope that this helps.
```

##### ↳ ↳ Re: Windows or MicroFocus NetExpress Problem???

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1998-06-21T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff57ad9eeb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ff57ad9eeb-p2@usenetarchives.gap>`
- **References:** `<6mg8b1$6u1$1@camel18.mindspring.com> <gap-ff57ad9eeb-p2@usenetarchives.gap>`

```




› The problem occurs because the entry names and associated program
› information are stored globally inside the run-time system, and therefore
…[5 more quoted lines elided]…
› one module, which module should be used ?

I have never written anything like a runtime system, but it would seem
logical to me to check to see if the entry point being called is in the
existing module first...If it is then use it...

› However, the duplicate named code should only be loaded if it is directly
› referenced suggesting that the calls to your date/time routines are
…[4 more quoted lines elided]…
› your only option is to rename them.

I tried an experiment this morning after reading your posting...I added a
second and unique entry point to the obj being called...When I call the new
entry point from the .dll, I receive the same internal error message, even
though I am calling a unique entry point...I guess this confirms that you
cannot use litlink...The problem there is that we have many thousand of
lines of code that would have to be modified, retested, etc...Our
applications are native windows api applications, and it is my understanding
that litlink is a requirement...

Any other suggestions that might get us around this problem...

›› Is the problem a MicroFocus runtime problem, or a Windows restriction on
› the
…[5 more quoted lines elided]…
› present.


Can you give some additional insight...When do you expect to deliver the
correction...

THIS IS INDEED A MAJOR, MAJOR BUG...
```

###### ↳ ↳ ↳ Re: Windows or MicroFocus NetExpress Problem???

- **From:** "gael wilson" <ua-author-6589191@usenetarchives.gap>
- **Date:** 1998-06-23T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff57ad9eeb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ff57ad9eeb-p3@usenetarchives.gap>`
- **References:** `<6mg8b1$6u1$1@camel18.mindspring.com> <gap-ff57ad9eeb-p2@usenetarchives.gap> <gap-ff57ad9eeb-p3@usenetarchives.gap>`

```



ken··.@min··g.com wrote in article
<6mlk5g$q7d$1.··.@cam··g.com>...
› 
› 
…[13 more quoted lines elided]…
› existing module first...If it is then use it...

Ken, as someone who has a wealth of experience I'm sure you will appreciate
that problems are almost always much more complex once you get into the
actual details than they appear at a glance. However, despite the fact that
I could describe at great length what is occurring at a low-level it won't
be of any help in resolving your problems. So, I'll focus on what may be
possible to help overcome them.

› 
›› However, the duplicate named code should only be loaded if it is
…[24 more quoted lines elided]…
› 

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

››› Is the problem a MicroFocus runtime problem, or a Windows restriction
›› on
…[11 more quoted lines elided]…
› correction...

As I'm not representing Micro Focus in any official capacity on the
newsgroup (being a humble developer) I'm not in a position to be able to
say specifically when the change will appear.
All I can suggest is that you contact your sales representative for
infomation. Unofficially though, next release would be a reasonable
expectation.

›
› THIS IS INDEED A MAJOR, MAJOR BUG...
…[3 more quoted lines elided]…
›

Yes, I fully accept that for your application this is a major problem and I
did acknowledge that in my previous reply. However, the situation you have
described is actually quite rare which is why it was not addressed until
recently.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
