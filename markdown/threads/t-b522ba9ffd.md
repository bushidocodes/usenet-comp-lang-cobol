[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM WebSphere Developer for zSeries V6.0

_3 messages · 3 participants · 2005-05_

---

### IBM WebSphere Developer for zSeries V6.0

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-05-12T05:05:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nuBge.332807$R24.68549@fe05!news.easynews.com>`

```
Just since there hasn't been much activity (even OT activity) recently, I 
thought I would point out an IBM announcement from earlier this week at:

 http://www.ibm.com/isource/cgi-bin/goto?it=usa_annred&on=205-112

a "code generator" (or application generator) for the 21st century .... and I 
thought these types of things had stopped being developed and enhancemed.

Notice that it has options for CICS or IMS; COBOL or PL/I (and Java); "and all 
that jazz"
```

#### ↳ Re: IBM WebSphere Developer for zSeries V6.0

- **From:** epc8@juno.com
- **Date:** 2005-05-12T06:22:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1115904172.351815.56130@g14g2000cwa.googlegroups.com>`
- **References:** `<nuBge.332807$R24.68549@fe05!news.easynews.com>`

```

William M. Klein wrote:
> Just since there hasn't been much activity (even OT activity)
recently, I
> thought I would point out an IBM announcement from earlier this week
at:
>
>  http://www.ibm.com/isource/cgi-bin/goto?it=usa_annred&on=205-112
>
> a "code generator" (or application generator) for the 21st century
.... and I
> thought these types of things had stopped being developed and
enhancemed.
>
> Notice that it has options for CICS or IMS; COBOL or PL/I (and Java);
"and all
> that jazz"
>
> --
> Bill Klein
>  wmklein <at> ix.netcom.com

Reading the blurb on the linked page indicates this program can do
almost "anything". It's obviously "buzzword compliant". I'm waiting for
some corporate HR drone to cut and paste its capabilities into a new
series of job ads. :-).

Seriously, I do remember when these program became popular, just before
so called "fourth generation" languages - database managers killed them
off. One of them was called (with obvious hubris) "The Last One". By
answering a series of questions, it generated a supposedly complete
application program - in AppleSoft BASIC on an Apple II microcomputer.

But what has this to do with COBOL? It points out one of the dangers of
"application developers". The program I mentioned produced code which
had to deal with the limitations of interpreted BASIC on a slow micro.
It ended up with minimal variable names, multiple statements per line
and other kluges (optimizations!) needed to get it to run at acceptable
speed on a 1 MHz processor such as putting frequently used variables
first. The resulting program was unreadable and useless except to run.
Modifying it was not possible. Obviously someone had also discovered
"vendor lock in".

It's one thing to use a language such as C as a form of intermediate
code which is then compiled to a native language. In fact, there are
several COBOL compiler projects which first translate to C then feed
the result through the GNU C compiler. (There is also a large set of
GNU programs which use the GNU back end without producing any C code.)

Likewise compiling to Java sounds great, except that in my experience,
these programs tend to be resource hogs and tend to run sluggishly
except on fast hardware.

Perhaps IBM has come up with something better, but given they type of
output I have seen in _Language_X_ to C translations, I feel sorry for
the maintenance programmer who will have to work with the COBOL (or
PL/I or whatever) output.
```

##### ↳ ↳ Re: IBM WebSphere Developer for zSeries V6.0

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-05-13T03:11:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eha12F34767U1@individual.net>`
- **References:** `<nuBge.332807$R24.68549@fe05!news.easynews.com> <1115904172.351815.56130@g14g2000cwa.googlegroups.com>`

```

<epc8@juno.com> wrote in message
news:1115904172.351815.56130@g14g2000cwa.googlegroups.com...
>
> William M. Klein wrote:
…[3 more quoted lines elided]…
>
That is SO true... :-)

> Seriously, I do remember when these program became popular, just before
> so called "fourth generation" languages - database managers killed them
…[3 more quoted lines elided]…
>

I believe there was also an implementation of it that ran on mainframes. I
remember hearing about it, but, of course, it could have been just
programmer beer talk. Apparently, the place that trialled it gave it up
after 6 months and went back to doing it in COBOL... (Knowing looks all
round... :-))

I heard that there was also a company that had another crack at the elusive
grail with a system called "The Next One" , but that may be apochryphal...

I have a certain sympathy for "The Last One"" because it was designed on the
same principles that I believe will be the basis of the smart systems of the
future.  i.e. Interactive iteration. I see smart software interacting with
end users to create applications. "The Last One" used a similar idea in
1981. It failed. But much has happened since then. If the same program was
written today and had acces to the internet knowledge base, the
comparatively infinite memory available, and several million times the
processing cycles that were available then, not to mention the advances in
programming like OO and Components, who knows what might become available?


 > But what has this to do with COBOL? It points out one of the dangers of
> "application developers". The program I mentioned produced code which
…[7 more quoted lines elided]…
>

Have you ever looked at the 'COBOL' generated by Jackson Structured
Programming....?

It is an object lesson in how NOT to write COBOL. The Jackson position is
that you are not supposed to maintain it, therefore it can be whatever
rubbish they decide is expedient.

Pete.

<snipped>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
