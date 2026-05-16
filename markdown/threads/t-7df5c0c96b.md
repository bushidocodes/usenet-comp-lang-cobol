[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Implementing concurrent system

_9 messages · 7 participants · 2000-02_

---

### Implementing concurrent system

- **From:** Ritchie Menzies <ritchie.menzies@gecm.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389A940E.55E5E973@gecm.com>`

```
I have to code an application which can be run over a network, which
will be run on two machines, and which will both run concurrently
exchanging data every 5 minutes, the data has to be a numerical value...

Would you all say that COBOL is the best language to use for this?
```

#### ↳ Re: Implementing concurrent system

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2UAm4.4294$45.187518@news2.rdc1.on.home.com>`
- **References:** `<389A940E.55E5E973@gecm.com>`

```
If it's the language you know and the language you are prepared to maintain
for the life of the application then it's the best language for the job.

Of course, you could do this by copying a file across the network every 5
minutes. In that case it could be written in your favorite shell scripting
language using the system task scheduler (cron, at, etc...) with no fancy
code at all.

-- Karl Wagner

"Ritchie Menzies" <ritchie.menzies@gecm.com> wrote in message
news:389A940E.55E5E973@gecm.com...
> I have to code an application which can be run over a network, which
> will be run on two machines, and which will both run concurrently
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Implementing concurrent system

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87f433$gqm$1@nnrp1.deja.com>`
- **References:** `<389A940E.55E5E973@gecm.com> <2UAm4.4294$45.187518@news2.rdc1.on.home.com>`

```
Hi:

I wonder whether something written in a shell scripting language
could be described as 'no fancy code at all'? Personally, I am
happy to say that I do not know any shell scripting language and
have no plans to learn one.

If people stopped messing about with shell scripting languages and
other stuff and kept it in COBOL, life would be a lot simpler, no?

Tony Dilworth


In article <2UAm4.4294$45.187518@news2.rdc1.on.home.com>,
  "Oscar T. Grouch" <dustbin@home.com> wrote:
> If it's the language you know and the language you are prepared to
maintain
> for the life of the application then it's the best language for the
job.
>
> Of course, you could do this by copying a file across the network
every 5
> minutes. In that case it could be written in your favorite shell
scripting
> language using the system task scheduler (cron, at, etc...) with no
fancy
> code at all.
>
…[6 more quoted lines elided]…
> > exchanging data every 5 minutes, the data has to be a numerical
value...
> >
> > Would you all say that COBOL is the best language to use for this?
> >
>
>
```

###### ↳ ↳ ↳ Re: Implementing concurrent system

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xZEm4.4556$45.209492@news2.rdc1.on.home.com>`
- **References:** `<389A940E.55E5E973@gecm.com> <2UAm4.4294$45.187518@news2.rdc1.on.home.com> <87f433$gqm$1@nnrp1.deja.com>`

```
Simpler for who?

Do you  honestly mean to tell me that you would prefer write and maintain a
COBOL program that does FTP, rather than write a one line script that makes
use of the FTP program that already exists on your system? Have you never
used REXX, CLIST, or JCL on the mainframe. What about scripts to handle
precompile, compile, link, bind for a COBOL program? Or do you recommend
writing a COBOL program to handle building a COBOL program?

Use the right tool for the job.

-Karl Wagner


"Foodman" <foodman123@aol.com> wrote in message
news:87f433$gqm$1@nnrp1.deja.com...
> Hi:
>
…[45 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: Implementing concurrent system

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87jlet$jfh$1@nnrp1.deja.com>`
- **References:** `<389A940E.55E5E973@gecm.com> <2UAm4.4294$45.187518@news2.rdc1.on.home.com> <87f433$gqm$1@nnrp1.deja.com> <xZEm4.4556$45.209492@news2.rdc1.on.home.com>`

```
Hi:

No, I have never used REXX or CLIST. I used JCL in the olden days
on IBM mainframes but I am happy to say that I have worked exclusively
on the PC since 1983.  Of course, I use DOS commands in a batch file
to compile and link. Otherwise I never seem to find the need for
using this other stuff. No, I would not write a COBOL program for
FTP (and wouldn't know how) since I use WS_FTP which works fine for
updating my websites. I also think that people wind up using things
like REXX (whatever that is) to solve problems which might not have
arisen if the system and its data files had been designed properly
in the first place, no?

People usually invent software systems to make money. Programmers
usually like to use as many different 'things' as they can so that
their resume will be more appealing. In other words, if someone
invents a tool, whether it is necessary or not, people will find
an excuse to use it.

Tony Dilworth




In article <xZEm4.4556$45.209492@news2.rdc1.on.home.com>,
  "Oscar T. Grouch" <dustbin@home.com> wrote:
> Simpler for who?
>
> Do you  honestly mean to tell me that you would prefer write and
maintain a
> COBOL program that does FTP, rather than write a one line script that
makes
> use of the FTP program that already exists on your system? Have you
never
> used REXX, CLIST, or JCL on the mainframe. What about scripts to
handle
> precompile, compile, link, bind for a COBOL program? Or do you
recommend
> writing a COBOL program to handle building a COBOL program?
>
…[23 more quoted lines elided]…
> > > for the life of the application then it's the best language for
the
> > job.
> > >
…[4 more quoted lines elided]…
> > > language using the system task scheduler (cron, at, etc...) with
no
> > fancy
> > > code at all.
…[5 more quoted lines elided]…
> > > > I have to code an application which can be run over a network,
which
> > > > will be run on two machines, and which will both run
concurrently
> > > > exchanging data every 5 minutes, the data has to be a numerical
> > value...
> > > >
> > > > Would you all say that COBOL is the best language to use for
this?
> > > >
> > >
…[9 more quoted lines elided]…
>
```

#### ↳ Re: Implementing concurrent system

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87fa2r$9ut$1@news.igs.net>`
- **References:** `<389A940E.55E5E973@gecm.com>`

```
The language choice has little to do with the fact that it is on a network,
though if you have two different platforms involved, Cobol has the advantage
that your data will be the same on both. I currently have several systems
that span multiple machines, written in Cobol. One thing that I would advise
you to do, if you can, and that is to make the files ASCII with no Comp
fields, and make them line sequential.  Communications becomes trivial to
debug when you can look at the data flowing between systems with a text
editor.

The easiest way to do this on PC's is to write the programs as if they were
batch, and then use the task scheduler to run them every five minutes.

Ritchie Menzies wrote in message <389A940E.55E5E973@gecm.com>...
>I have to code an application which can be run over a network, which
>will be run on two machines, and which will both run concurrently
…[3 more quoted lines elided]…
>
```

#### ↳ Re: Implementing concurrent system

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-02-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<580n9sg4vs9l02l1uriute8c41qthl8sju@4ax.com>`
- **References:** `<389A940E.55E5E973@gecm.com>`

```
Ritchie Menzies <ritchie.menzies@gecm.com> wrote:

>I have to code an application which can be run over a network, which
>will be run on two machines, and which will both run concurrently
>exchanging data every 5 minutes, the data has to be a numerical value...

>Would you all say that COBOL is the best language to use for this?

hmm. yes, if you know cobol, it would do. i don't exactly understand
the model you are using. it sounds like a match of peer to peer (only
2 machines) and load balancing.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
usenet has been down for awhile... switching audio card
```

#### ↳ Re: Implementing concurrent system

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389CE48F.7C046242@zip.com.au>`
- **References:** `<389A940E.55E5E973@gecm.com>`

```
Ritchie Menzies wrote:
> 
> I have to code an application which can be run over a network, which
…[3 more quoted lines elided]…
> Would you all say that COBOL is the best language to use for this?

You might want to look up sockets.  Was it Thane or Judson that had
the cheat sheet.

Regarding multiple language solutions.  There is always a right
language for a job, scripts are great as are batch files on PC's.  I
would agree that too many languages will cause a major problem but a
small handful is not generally a problem.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: Implementing concurrent system

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-02-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<389da68e.217400642@news.freewwweb.com>`
- **References:** `<389A940E.55E5E973@gecm.com> <389CE48F.7C046242@zip.com.au>`

```
On Sun, 06 Feb 2000 14:03:43 +1100, Ken Foskey <waratah@zip.com.au>
wrote:

>You might want to look up sockets.  Was it Thane or Judson that had
>the cheat sheet.
>

You can get it here: http://www.geocities.com/Eureka/2006/download.htm

Also, it has an update (Thanks Tony Riddle) that shows how to make the
calls dynamically.

I plan (someday) to attack the Fujitsu example again utilizing the new
typedef's they offer in v5.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
