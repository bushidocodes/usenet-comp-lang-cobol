[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# <<< MF 2.4.38 Compiler Problems - PLEASE HELP! >>>

_5 messages · 2 participants · 1996-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### <<< MF 2.4.38 Compiler Problems - PLEASE HELP! >>>

- **From:** "lo..." <ua-author-1109403@usenetarchives.gap>
- **Date:** 1996-09-26T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52gpsj$mja@camel0.mindspring.com>`

```

Hello. My company is currently using Micro Focus COBOL version
2.4.38. I have a couple of questions that Micro Focus could not
answer, so I figured I'd try here.

#1: MF 2.4.38 will NOT compile under a Windows environment
consistently. Sometimes it works, sometimes it doesn't. I wanted to
know if anyone has a fix/patch for this.

#2: We have a more recent version of the compiler 3.1.35, that I would
LOVE to port to, HOWEVER, MF could not tell me if I have to do DATA
FILE CONVERSIONS on my files. Now I'm not talking about just
rebuilding the indexes, I mean, would I have to use the REBUILD
utility to read the current data files and create "new" 3.1.35 data
files?!!??! Was there a file structure change in between these
versions of the compiler?!?

If you know the answers to these questions, please eMail me at:
dt··.@drs··e.com

Thanks!
D.
```

#### ↳ Re: <<< MF 2.4.38 Compiler Problems - PLEASE HELP! >>>

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-09-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d9d2c1e8ba-p2@usenetarchives.gap>`
- **In-Reply-To:** `<52gpsj$mja@camel0.mindspring.com>`
- **References:** `<52gpsj$mja@camel0.mindspring.com>`

```

Ego wrote:

› #1: MF 2.4.38 will NOT compile under a Windows environment
› consistently. Sometimes it works, sometimes it doesn't. I wanted to
› know if anyone has a fix/patch for this.

There's not really enough information here (for a start, how "doesn't" it work?
A description of exactly what symptoms you see would be a good start), so all
I can say about this is that in my experience, you might be looking at something
other than a software fault. The machine I'm writing this on used to have a
similar problem with MS Visual C++ - I'd set off a build using a makefile and
half the sources would fail to compile with internal compiler errors and all
sorts of nasties. Execute the make again and it worked fine - it was all down
to the CPU getting too hot on these large builds! I stuck a bigger fan and a
heat-sink on the CPU and it's MUCH more stable now.

I'm not saying it's NOT a Micro Focus problem (there really isn't enough info
to say one way or the other), just that you might want to look at other things
also.

› #2: We have a more recent version of the compiler 3.1.35, that I would
› LOVE to port to, HOWEVER, MF could not tell me if I have to do DATA
…[4 more quoted lines elided]…
› versions of the compiler?!?

I believe that care was taken to ensure that old data files would read and
update fine using newer versions of the file handler (the files have a version
number) in the event that any format change occurred. Any new files created
will automatically be of the most recent format, however.

I`m afraid that you can`t take this as gospel - I don`t have any direct dealings
with the file handler, but this is what I *believe* to be true.
If you`re in any doubt or require total peace of mind, use REBUILD or write a
little conversion program that simply reads through and old file and writes a
new one (same FD, yanked from current sources etc).

Cheers,
Kev.
```

##### ↳ ↳ Re: <<< MF 2.4.38 Compiler Problems - PLEASE HELP! >>>

- **From:** "lo..." <ua-author-1109403@usenetarchives.gap>
- **Date:** 1996-09-29T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d9d2c1e8ba-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d9d2c1e8ba-p2@usenetarchives.gap>`
- **References:** `<52gpsj$mja@camel0.mindspring.com> <gap-d9d2c1e8ba-p2@usenetarchives.gap>`

```

Kevin Digweed wrote:

› Ego wrote:
 
›› #1: MF 2.4.38 will NOT compile under a Windows environment
›› consistently.  Sometimes it works, sometimes it doesn't.  I wanted to
›› know if anyone has a fix/patch for this.
 
› There's not really enough information here (for a start, how "doesn't" it work?
› A description of exactly what symptoms you see would be a good start), so all
…[6 more quoted lines elided]…
› heat-sink on the CPU and it's MUCH more stable now.
 
› I'm not saying it's NOT a Micro Focus problem (there really isn't enough info
› to say one way or the other), just that you might want to look at other things 
› also.
 
›› #2: We have a more recent version of the compiler 3.1.35, that I would
›› LOVE to port to, HOWEVER, MF could not tell me if I have to do DATA
…[4 more quoted lines elided]…
›› versions of the compiler?!?
 
› I believe that care was taken to ensure that old data files would read and
› update fine using newer versions of the file handler (the files have a version
› number) in the event that any format change occurred. Any new files created
› will automatically be of the most recent format, however.
 
› I`m afraid that you can`t take this as gospel - I don`t have any direct dealings
› with the file handler, but this is what I *believe* to be true.
› If you`re in any doubt or require total peace of mind, use REBUILD or write a
› little conversion program that simply reads through and old file and writes a
› new one (same FD, yanked from current sources etc).
 
› Cheers,
› Kev.
 
› --
› Kevin. Advancing all electric at Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
› These views are strictly my own. I doubt that anyone else would want them.
› STUFF FOR SALE: Here!


Kevin:

As you requested, here is the EXACT error message I receive.

The Application Program Interface (API) entered will only work in
Microsoft Operating System/2 mode.


I can reproduce this error, at will, on any computer, regardless of
type/make/model, so long as I am trying to compile in a Windows 3.1x
or 95/NT environment. We believe that it is a DOS environment setting
issue, because if I change the number of DOS environment settings, I
can get it to compile.

D..

If you want to contact me, my internet address is:
dt··.@drs··e.com
Thanks.
```

###### ↳ ↳ ↳ Re: <<< MF 2.4.38 Compiler Problems - PLEASE HELP! >>>

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-09-29T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d9d2c1e8ba-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d9d2c1e8ba-p3@usenetarchives.gap>`
- **References:** `<52gpsj$mja@camel0.mindspring.com> <gap-d9d2c1e8ba-p2@usenetarchives.gap> <gap-d9d2c1e8ba-p3@usenetarchives.gap>`

```

Ego wrote:
› Kevin:
 
› Hi.
 
› As you requested, here is the EXACT error message I receive.
› 
…[7 more quoted lines elided]…
› can get it to compile.

OK, this is a lot more useful! I`m reliably informed that this is due to a problem
while trying to detect "Virtual 8086 mode" within a "bound EXE". The way this is
done (in what is a very old product) may not be compatible with the newer OS's you
are trying to run it on.

As you have already upgraded to a version of COBOL that IS supported on those OS's
I'd recommend that you concentrate on getting over your other problem with files
(it would seem that REBUILD is all that you need?) and use that. Of course, you
will also gain additional benefits from the improvements made to the COBOL system
since the old version you are trying to use.

Please don't hesitate to ask (this newsgroup or Technical Support would be your
best options) if you have any more problems.

Cheers,
Kev.
```

###### ↳ ↳ ↳ Re: <<< MF 2.4.38 Compiler Problems - PLEASE HELP! >>>

_(reply depth: 4)_

- **From:** "lo..." <ua-author-1109403@usenetarchives.gap>
- **Date:** 1996-09-30T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d9d2c1e8ba-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d9d2c1e8ba-p4@usenetarchives.gap>`
- **References:** `<52gpsj$mja@camel0.mindspring.com> <gap-d9d2c1e8ba-p2@usenetarchives.gap> <gap-d9d2c1e8ba-p3@usenetarchives.gap> <gap-d9d2c1e8ba-p4@usenetarchives.gap>`

```

Kevin Digweed wrote:

› Ego wrote:
›› Kevin:
 
› Hi.
 
›› As you requested, here is the EXACT error message I receive.
›› 
…[7 more quoted lines elided]…
›› can get it to compile.
 
› OK, this is a lot more useful! I`m reliably informed that this is due to a problem
› while trying to detect "Virtual 8086 mode" within a "bound EXE". The way this is
› done (in what is a very old product) may not be compatible with the newer OS's you
› are trying to run it on.
 
› As you have already upgraded to a version of COBOL that IS supported on those OS's
› I'd recommend that you concentrate on getting over your other problem with files
› (it would seem that REBUILD is all that you need?) and use that. Of course, you
› will also gain additional benefits from the improvements made to the COBOL system
› since the old version you are trying to use.
 
› Please don't hesitate to ask (this newsgroup or Technical Support would be your
› best options) if you have any more problems.
 
› Cheers,
› Kev.
 
› --
› Kevin. Advancing all electric at Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
› These views are strictly my own. I doubt that anyone else would want them.
› STUFF FOR SALE: Here!

Kevin:

Thank you for your insight, I was worried that I would have to go the
"update the compiler" route; but none the less, I'm glad I have too.
I will have one of my people develope an App with Variable Length
records and compile it under 2.4.38 and 3.1.35 and then check the
resulting .DAT files. Plus I'll have him run the same data files
under the two different .EXE files to see if the data becomes
"unstable".

Thanks again.
D.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
