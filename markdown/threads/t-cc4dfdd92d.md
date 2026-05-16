[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with MF Cobol being very slow under OS/2

_6 messages · 4 participants · 1999-08 → 1999-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Help with MF Cobol being very slow under OS/2

- **From:** Jürgen Ibelgaufts <ibelgaufts@gfc-net.de>
- **Date:** 1999-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37CBDCCE.C773215E@gfc-net.de>`

```
Hi,

I ran into a serious runtime problem under OS2. I have Microfocus Cobol 4.0.36
for Win32 and for OS2. I have one application that makes extensive use (120
calls per transaction) of calling a function from a DLL (created with cbllink
-d).

While working under Win32, the program is not as fast as it should, but it is
OK.

Under OS2, the response time counts up to five times the Win32 response time.

The source codes are identical.

I found out that a simple call into an entry inside the DLL takes about 10
milliseconds on NT and 30-40 milliseconds on OS2 that steals more than 3 seconds
for one transaction.

What's going wrong here ?

Any suggestions highly welcome.

Juergen Ibelgaufts
```

#### ↳ Re: Help with MF Cobol being very slow under OS/2

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qgk6p$80f$1@nntp6.atl.mindspring.net>`
- **References:** `<37CBDCCE.C773215E@gfc-net.de>`

```
>>I ran into a serious runtime problem under OS2. I have Microfocus Cobol
4.0.36
for Win32 and for OS2. I have one application that makes extensive use (120
calls per transaction) of calling a function from a DLL (created with
cbllink
-d).

Try making the function(s) in the dll a subroutine(s) in the main program
and eliminate the dll...Compile the module that is currently a dll as an
.obj and include the .obj in the link for the main program...Should be very
little source changes required...

kenmullins
```

##### ↳ ↳ Re: Help with MF Cobol being very slow under OS/2

- **From:** Jürgen Ibelgaufts <ibelgaufts@gfc-net.de>
- **Date:** 1999-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37CBEC2A.399434C7@gfc-net.de>`
- **References:** `<37CBDCCE.C773215E@gfc-net.de> <7qgk6p$80f$1@nntp6.atl.mindspring.net>`

```
Ken,

many thanks for your hint, but, I'm sorry to say, the response time is exactly
the same (differs about 20 milliseconds for a whole transaction with about 100
calls).

Juergen Ibelgaufts

---------------------------------------------------------

Ken Mullins schrieb:
> 
> >>I ran into a serious runtime problem under OS2. I have Microfocus Cobol
…[11 more quoted lines elided]…
> kenmullins
```

###### ↳ ↳ ↳ Re: Help with MF Cobol being very slow under OS/2

- **From:** aleph3@unknown.com (Aleph3)
- **Date:** 1999-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qj8nh$2vl1@enews3.newsguy.com>`
- **References:** `<37CBDCCE.C773215E@gfc-net.de> <7qgk6p$80f$1@nntp6.atl.mindspring.net> <37CBEC2A.399434C7@gfc-net.de>`

```
In article <37CBEC2A.399434C7@gfc-net.de>, =?iso-8859-1?Q?J=FCrgen?= 
Ibelgaufts <ibelgaufts@gfc-net.de> wrote:

Hi 

I have another suggestion which works on win9x.

Use the compiler directive FASTLINK
This makes call rich programs more efficient since it disables all the tests 
Cobol runs on each call.

Hope it helps
Ilan

>Ken,
>
…[22 more quoted lines elided]…
>> kenmullins
```

###### ↳ ↳ ↳ Re: Help with MF Cobol being very slow under OS/2

_(reply depth: 4)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qlp4e$g5j$1@ssauraab-i-1.production.compuserve.com>`
- **References:** `<37CBDCCE.C773215E@gfc-net.de> <7qgk6p$80f$1@nntp6.atl.mindspring.net> <37CBEC2A.399434C7@gfc-net.de> <7qj8nh$2vl1@enews3.newsguy.com>`

```
    It sounds like there is something in your function that
is slower on OS/2, rather than call overhead.  Is the source code for this
function large?  What does it do that involves the operating system?

    At this time I can think of nothing better than eyeballing the source
code
to locate something that uses an operating system call.  It could be any
number of things:  keyboard, screen, com, print, disk, memory allocation.

    It would probably not be a compute or something "local".


> >
> >many thanks for your hint, but, I'm sorry to say, the response time is
exactly
> >the same (differs about 20 milliseconds for a whole transaction with
about 100
> >calls).
> >
…[6 more quoted lines elided]…
> >> >>I ran into a serious runtime problem under OS2. I have Microfocus
Cobol
> >> 4.0.36
> >> for Win32 and for OS2. I have one application that makes extensive use
(120
> >> calls per transaction) of calling a function from a DLL (created with
> >> cbllink
> >> -d).
> >>
> >> Try making the function(s) in the dll a subroutine(s) in the main
program
> >> and eliminate the dll...Compile the module that is currently a dll as
an
> >> .obj and include the .obj in the link for the main program...Should be
very
> >> little source changes required...
> >>
> >> kenmullins
```

###### ↳ ↳ ↳ Problem fixed: Cobol being very slow under OS/2

_(reply depth: 5)_

- **From:** Jürgen Ibelgaufts <ibelgaufts@gfc-net.de>
- **Date:** 1999-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37CF7CD6.7B8C8ECF@gfc-net.de>`
- **References:** `<37CBDCCE.C773215E@gfc-net.de> <7qgk6p$80f$1@nntp6.atl.mindspring.net> <37CBEC2A.399434C7@gfc-net.de> <7qj8nh$2vl1@enews3.newsguy.com> <7qlp4e$g5j$1@ssauraab-i-1.production.compuserve.com>`

```


Russell Styles schrieb:
> 
>     It sounds like there is something in your function that
…[9 more quoted lines elided]…
> 

Russell,

perfectly right. In the meantime I found the reason in OS2's dossleep function.
We had to issue a sleep-time of one millisecond for some reasons. OS2 always
seems to round it up to the next 30 milliseconds, while NT rounds it up to about
10 milliseconds. We found a solution that does not need the sleep function. Now
everything works as fast as expected.

Thanks to all contributors in this branch

Juergen Ibelgaufts
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
