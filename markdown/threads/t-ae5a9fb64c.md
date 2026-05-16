[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dynamic file naming & HP3000 Buffer size issues

_4 messages · 4 participants · 2002-04_

---

### Dynamic file naming & HP3000 Buffer size issues

- **From:** marydegallo@yahoo.com (Mary Degallo)
- **Date:** 2002-04-26T09:12:18-07:00
- **Newsgroups:** comp.sys.hp.mpe,alt.cobol,comp.lang.cobol
- **Message-ID:** `<f0bf00c.0204260812.7579f4d1@posting.google.com>`

```
hi Everybody!

   thanx for those participating in the discussion and providing valuable 
   help to newbies like me. 

   ---------------------------------------
   FILENAME known at RunTime
   FILENAME is NOT known at COMPILE time.
   ---------------------------------------
   C, C++, Java provide a file name that can be specified at RunTime. 
   Where as the way the FD and File Sections in COBOL are, 
    we have to specify the file name at COMPILE time. 
   We have to design our applications around this "feature/limitation". 
   Has anybody, worked around this, using some other "tricks".
   JCL is one way, but we donot want to get into JCL stuff. 
   How does one do it in a more elegant way? 

   

   ----------------------------------------
   HP3000 buffer sizes etc,...
   ----------------------------------------
   We have to read this data from a THIRD PARTY software objects. 
   And these Objects can run into 1 or 2 or 4 or somtimes even 7 Megs of Data.
   Do I have to define such a HUGE working Storage Area, to read the 
   Object data Into?

   I could define a 1K or 2K kind of Buffers and tested my code on AS400. 
   
   How will the scenario change when it becomes, a 1 MEG buffer?
    1.   What are the issues involved. 
    2.   Can we do it? 
    
   Some geeks in my office are playing "C++, JAVA vs  COBOL"  politics  in 
    issues like these.    Well its not new anyways.      :) 

   thanx in advance. 
-Mary
```

#### ↳ Re: Dynamic file naming & HP3000 Buffer size issues

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-04-26T21:06:59+00:00
- **Newsgroups:** comp.sys.hp.mpe,alt.cobol,comp.lang.cobol
- **Message-ID:** `<Tjjy8.202674$%l3.16594481@bin8.nnrp.aus1.giganews.com>`
- **References:** `<f0bf00c.0204260812.7579f4d1@posting.google.com>`

```

"Mary Degallo" <marydegallo@yahoo.com> wrote in message
news:f0bf00c.0204260812.7579f4d1@posting.google.com...
> hi Everybody!
>
…[13 more quoted lines elided]…
>    How does one do it in a more elegant way?

Hmm. If you don't want to specify the file name at compile time, and don't
want to specify the file name at execution time (via JCL), you could ask the
operator.

>
>
…[5 more quoted lines elided]…
>    And these Objects can run into 1 or 2 or 4 or somtimes even 7 Megs of
Data.
>    Do I have to define such a HUGE working Storage Area, to read the
>    Object data Into?
…[8 more quoted lines elided]…
>     issues like these.    Well its not new anyways.      :)

I have no idea on the third-party software objects. But you've got to stamp
out this Java vs. COBOL shit before it gets out of hand. I recommend killing
the Java people.
```

#### ↳ Re: Dynamic file naming & HP3000 Buffer size issues

- **From:** leclaire <leclaire@nospam.rr.com>
- **Date:** 2002-04-27T01:20:45+00:00
- **Newsgroups:** comp.sys.hp.mpe,alt.cobol,comp.lang.cobol
- **Message-ID:** `<3CC9FB82.140D73A0@nospam.rr.com>`
- **References:** `<f0bf00c.0204260812.7579f4d1@posting.google.com>`

```

Mary Degallo wrote:
>    ---------------------------------------
>    FILENAME known at RunTime
…[9 more quoted lines elided]…
> 
  I assume that your filename question refers to the HP3000 also, and I
remember being *appalled* that HP would not allow an identifier in the
assign-to clause of the select statement.  As I recall (and this goes
back a while) one is forced to resort to an external OS variable which
can be set before execution via UDC (what most would call a macro) and
referenced thru special-names or something of the sort.
```

#### ↳ Re: Dynamic file naming & HP3000 Buffer size issues

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2002-04-27T23:33:00+01:00
- **Newsgroups:** comp.sys.hp.mpe,alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000001d3.033d9e25@ieee.org>`
- **References:** `<f0bf00c.0204260812.7579f4d1@posting.google.com>`

```
Mary,

> FILENAME known at RunTime
>    FILENAME is NOT known at COMPILE time.

I think the way we solved this was to copy the file to a pre-defined file 
name. It means using JCL, but it's pretty simple to do.

---

Doug

dwscott@ieee.org
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
