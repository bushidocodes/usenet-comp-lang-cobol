[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol data files

_9 messages · 7 participants · 1999-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol data files

- **From:** "NEIL MATHESON" <neilm@retemail.es>
- **Date:** 1999-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ug515$3a624@SGI3651ef0.iddeo.es>`
- **References:** `<MPG.127437a4fc1711389896a0@news> <380AB9C3.84FAAD8C@home.com>`

```
Hi

Forgive my ignorance - I really don't know anything about Cobol, but I
need to be able to convert the data files for a customer's old MF Cobol
application to MS Access.

There must be a tool out there on the web somewere that does this.

If anyone can give me a pointer, I'd really appreciate it

    THANKS A LOT,

    Neil Matheson
```

#### ↳ R: MF Cobol data files

- **From:** "igor" <igor@euro-soft.it>
- **Date:** 1999-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7uhm26$3r4$1@nslave1.tin.it>`
- **References:** `<MPG.127437a4fc1711389896a0@news> <380AB9C3.84FAAD8C@home.com> <7ug515$3a624@SGI3651ef0.iddeo.es>`

```
on acucobol there's an utility (vutil) that extract form an indexed file an
ashii file

I don't know if the acucobol utility reads a mfcobol file....
if you want to try .....

bye bye

Igor Stefenelli

-----------------------------------------------
Igor Stefenelli

  |\/\/\/|     iglinux@freemail.it
  |      |
  |      |
  | (o)(o)
  C      _)
   | ,___|
   |   /
  /____\
/      \











NEIL MATHESON <neilm@retemail.es> wrote in message
7ug515$3a624@SGI3651ef0.iddeo.es...
> Hi
>
…[13 more quoted lines elided]…
>
```

#### ↳ Re: MF Cobol data files

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380c9162.10911459@news.enter.net>`
- **References:** `<MPG.127437a4fc1711389896a0@news> <380AB9C3.84FAAD8C@home.com> <7ug515$3a624@SGI3651ef0.iddeo.es>`

```
"NEIL MATHESON" <neilm@retemail.es> wrote:

>Hi
>
…[10 more quoted lines elided]…
>    Neil Matheson

Try www.datajunction.com or www.siber.com

I believe that Siber Systems has a data conversion tool, but if you
don't find anything on the web site, you can also send an e-mail
message to info@siber.com.

I hope that your data files aren't too large.  I wouldn't want to rely
on Access to handle massive amounts of data.  That is certainly taking
two steps backward, but these days people seem to opt for anything
with a Microsoft label on it...even if it means slower, buggier and
less efficient....just my opinion.




Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: MF Cobol data files

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0gaP3.361$7X2.29654@typhoon01.swbell.net>`
- **References:** `<MPG.127437a4fc1711389896a0@news> <380AB9C3.84FAAD8C@home.com> <7ug515$3a624@SGI3651ef0.iddeo.es> <380c9162.10911459@news.enter.net>`

```

Bob Wolfe <rtwolfe@flexus.com

> I hope that your data files aren't too large.  I wouldn't want to
rely
> on Access to handle massive amounts of data.  That is certainly
taking
> two steps backward, but these days people seem to opt for anything
> with a Microsoft label on it...even if it means slower, buggier and
> less efficient....just my opinion.

BUT. Access lets you get started on the cheap. When you begin
to experience unacceptable slowdowns, get a faster computer or
install SQ7 with no source code changes or file conversions.
```

###### ↳ ↳ ↳ Re: MF Cobol data files

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380deba8.15361122@news.enter.net>`
- **References:** `<MPG.127437a4fc1711389896a0@news> <380AB9C3.84FAAD8C@home.com> <7ug515$3a624@SGI3651ef0.iddeo.es> <380c9162.10911459@news.enter.net> <0gaP3.361$7X2.29654@typhoon01.swbell.net>`

```
"Jerry P" <bismail@bisusa.com> wrote:

>
>Bob Wolfe <rtwolfe@flexus.com
…[12 more quoted lines elided]…
>

You are absolutely correct....with the price of PC's so cheap these
days, getting a bigger/better/faster machine isn't a huge investment. 

It's just that I'm from the "good old days" when getting a faster
machine was always the "backup plan."  Optimizing the software was
always the first plan...it's very hard to break these old habits!


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: MF Cobol data files

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7uig6f$q6r$1@plutonium.btinternet.com>`
- **References:** `<MPG.127437a4fc1711389896a0@news> <380AB9C3.84FAAD8C@home.com> <7ug515$3a624@SGI3651ef0.iddeo.es> <380c9162.10911459@news.enter.net>`

```

Bob Wolfe wrote in message <380c9162.10911459@news.enter.net>...
>"NEIL MATHESON" <neilm@retemail.es> wrote:
>
…[25 more quoted lines elided]…
>


Indeed, Bob, a colleque of mine uses Access for large amounts of data
storage - I mean large!, he's using a database over 2GB and Access struggles
with this, I guess we can all go back to flat indexed files....on second
thought, nah!!.


Simon R Hart
Eaton, Ottery St. Mary, UK.
```

###### ↳ ↳ ↳ Re: MF Cobol data files

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 1999-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380CF6CB.8CE8F911@siber.com>`
- **References:** `<MPG.127437a4fc1711389896a0@news> <380AB9C3.84FAAD8C@home.com> <7ug515$3a624@SGI3651ef0.iddeo.es> <380c9162.10911459@news.enter.net> <7uig6f$q6r$1@plutonium.btinternet.com>`

```
Simon R Hart wrote:
> 
> Bob Wolfe wrote in message <380c9162.10911459@news.enter.net>...
…[11 more quoted lines elided]…
> >less efficient....just my opinion.

Indeed, we have a tool called data2flat that converts MF (or FSC)
data files to CVS format (comma-separated values) that can be easily
imported into Aceess or any other database. 

More information on this tool is available at
http://www.siber.com/sct/datafile/

We also have a different variation of these tools that
imports data from Cobol data files into Crystal Reports
which is really nice GUI-driven report generator by 
Seagate Software.

We also have a converter from Cobol data files to 
DBF files (DBase IV format).

And finally, we have a general DataAccess library 
that is used to build all these converters and
it can be used by our customers to build their own
Cobol data readers/converters to their liking.

Regards,
Vadim Maslov
```

###### ↳ ↳ ↳ Re: MF Cobol data files

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ul5dm$95p$1@uranium.btinternet.com>`
- **References:** `<MPG.127437a4fc1711389896a0@news> <380AB9C3.84FAAD8C@home.com> <7ug515$3a624@SGI3651ef0.iddeo.es> <380c9162.10911459@news.enter.net> <7uig6f$q6r$1@plutonium.btinternet.com>`

```

Simon R Hart wrote in message <7uig6f$q6r$1@plutonium.btinternet.com>...
>
>Bob Wolfe wrote in message <380c9162.10911459@news.enter.net>...
…[31 more quoted lines elided]…
>storage - I mean large!, he's using a database over 2GB and Access
struggles
>with this, I guess we can all go back to flat indexed files....on second
>thought, nah!!.
…[6 more quoted lines elided]…
>


Anybody experienced large dBase files, I would like to know how dBase
performs when processing large GB files?


Simon R Hart
Eaton, Ottery St. Mary, UK.
```

#### ↳ Re: MF Cobol data files

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 1999-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380CB161.2A7E@NOSPAMguysoftware.com>`
- **References:** `<MPG.127437a4fc1711389896a0@news> <380AB9C3.84FAAD8C@home.com> <7ug515$3a624@SGI3651ef0.iddeo.es>`

```
NEIL MATHESON wrote:
> 
> Hi
…[5 more quoted lines elided]…
> There must be a tool out there on the web somewere that does this.

Try a generic parsing tool like ParseRat (http://www.guysoftware.com/parserat.htm).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
