[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# error 37,07 EOF

_5 messages · 4 participants · 2001-03_

---

### error 37,07 EOF

- **From:** "Eric Gauthier" <ericg@dgcsolutions.qc.ca>
- **Date:** 2001-03-21T10:00:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Eo3u6.10125$7g.203305@wagner.videotron.net>`

```
Hello all!

I have an error 37,07 on my file (EOF).  We are using RM-Cobol with the
Runtime version 7 and
Novell 4.11.  We are trying to configure the windows runtime and this is the
only "problem" left.

What is strange is that in another program, the file is open in I-O and it
work great.  I got the error in a program when it open it in INPUT mode.
Also it was working fine with the DOS Runtime.

I don't know if it is the windows runtime or a configuration in Novell.

In the user guide, it say :
The requested operation conflicts with the permissions allowed to the run
unit for the file. This error ...

What's a run unit? Is it an objet program (.cob) or is it the user rigths?


Any idea?

Thank's in advance.
Eric.
```

#### ↳ Re: error 37,07 EOF

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-03-21T18:24:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AB8F443.7AFC5853@home.com>`
- **References:** `<Eo3u6.10125$7g.203305@wagner.videotron.net>`

```


Eric Gauthier wrote:

> Hello all!
>
…[17 more quoted lines elided]…
> Any idea?

In simple terms a 'run unit' is one execution of the application. For DOS this
would be where you enter a Command Line instruction with the name say of your
main program. In RM terms I think your command line would be 'runcobol
myprog1..." and you can also include switches S=00100001 whatever.

In 'Windows" terminology you have two options, start by selecting to get the
'Run'  dialog box and again you enter the starting program. Alternatively, you
have set up an icon that you can click on to start the application.

If you are getting the error with open INPUT check your RM manual for the
input/output table - as to which file VERBS are permissible in conjunction with
an open as INPUT. The error 37, 07 must appear in a table somewhere in your
manual or in on-line help with reference to file-status codes.

I use only a very old copy of RM - but basically the same rules (OPEN verbs
combined with READ/WRITE verbs), apply regardless of compiler.

If the above generalization doesn't help - then query with Liant. Not my forte,
but it might be a combination of using RM and Novell, requiring some specific
settings.

Jimmy, Calgary AB
```

#### ↳ Re: error 37,07 EOF

- **From:** "Chris Loy" <chrisl@maxom.net>
- **Date:** 2001-03-22T10:12:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3aba1641$1@newsfeed.vitts.com>`
- **References:** `<Eo3u6.10125$7g.203305@wagner.videotron.net>`

```
Hi Eric,

The 37,07 is usually a permission problem.  Check the Attributes of the file
and/or user rights if on a server.

The run unit, I believe, is the runtime (runcobol program).

On  a related topic, I have a similar problem from on a indexed file that I
received from one of our users, our program is returning a 37,07 (and
permissions/user rights don't seem to be an issue).  I tried to run recovery
program and it actually returns a 98,49 error (Corrupt index), so not sure
why the program returns 37,07 and the recovery program returns 98xx.  I
still haven't resolved that issue....

Good luck and I hope it helps.

Chris Loy
Maxom Enterprise Solutions
PO Box 520
91 Townsend Avenue
Boothbay Harbor, ME  04538
Web: http://www.maxom.com
Toll-free: 888.809.8127
Phone: 207.633.0036
Fax: 207.633.0053



"Eric Gauthier" <ericg@dgcsolutions.qc.ca> wrote in message
news:Eo3u6.10125$7g.203305@wagner.videotron.net...
> Hello all!
>
> I have an error 37,07 on my file (EOF).  We are using RM-Cobol with the
> Runtime version 7 and
> Novell 4.11.  We are trying to configure the windows runtime and this is
the
> only "problem" left.
>
…[23 more quoted lines elided]…
>
```

##### ↳ ↳ Re: error 37,07 EOF

- **From:** "Eric Gauthier" <ericg@dgcsolutions.qc.ca>
- **Date:** 2001-03-22T10:52:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xepu6.1221$le2.6748@weber.videotron.net>`
- **References:** `<Eo3u6.10125$7g.203305@wagner.videotron.net> <3aba1641$1@newsfeed.vitts.com>`

```
Thank's to you and also to James.

I will probably do a recovery on my file since we got a lot of file
corruption at this place.  I have nothing to loose here.
I willl verify again the rights but I suppose they are alrights since it was
working fine yesterday morning with the DOS Runtime.

Eric.


"Chris Loy" <chrisl@maxom.net> a �crit dans le message news:
3aba1641$1@newsfeed.vitts.com...
> Hi Eric,
>
> The 37,07 is usually a permission problem.  Check the Attributes of the
file
> and/or user rights if on a server.
>
> The run unit, I believe, is the runtime (runcobol program).
>
> On  a related topic, I have a similar problem from on a indexed file that
I
> received from one of our users, our program is returning a 37,07 (and
> permissions/user rights don't seem to be an issue).  I tried to run
recovery
> program and it actually returns a 98,49 error (Corrupt index), so not sure
> why the program returns 37,07 and the recovery program returns 98xx.  I
…[26 more quoted lines elided]…
> > What is strange is that in another program, the file is open in I-O and
it
> > work great.  I got the error in a program when it open it in INPUT mode.
> > Also it was working fine with the DOS Runtime.
…[4 more quoted lines elided]…
> > The requested operation conflicts with the permissions allowed to the
run
> > unit for the file. This error ...
> >
> > What's a run unit? Is it an objet program (.cob) or is it the user
rigths?
> >
> >
…[12 more quoted lines elided]…
>
```

#### ↳ Re: error 37,07 EOF

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2001-03-28T00:14:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gg72ct8u7gkaa9fmocak8c504rhh4abf5f@4ax.com>`
- **References:** `<Eo3u6.10125$7g.203305@wagner.videotron.net>`

```
>I have an error 37,07 on my file (EOF).  We are using RM-Cobol with the
>Runtime version 7 and
>Novell 4.11.  We are trying to configure the windows runtime and this is the
>only "problem" left.
This error is normally related to lack of permissions to the
file/directory.

Logged as a normal user, browse the directory where the file in
question resides, and see what are the novell permissions for it.

Note that it is possible that the admin has permissions for it, but
not a normal user.

It would also be helpfull if you could tell us the version of the
novel client that you are using, as this may have some effect on this.

>

>
>What's a run unit? Is it an objet program (.cob) or is it the user rigths?
A run unit is a instance of "runcobol.exe".

Cheers.

Frederico Fonseca
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
