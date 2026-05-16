[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# net express promlem

_4 messages · 3 participants · 2003-06_

---

### net express promlem

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-06-19T14:32:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rnIa.7811$9y3.753137@news20.bellglobal.com>`

```
I have a customer with a net express problem that seems rather strange ...
perhaps someone has an idea of what to try.  The version is Version 3.0.

A cheque file is being printed with signatures.  The signatures are in BMP
form, and the BMP file is read in once at the start of the program.  It is 1
meg in size.

When the program runs under test (IE-under animation), it runs perfectly.
When the exact same INTS are run (no re-compile) with the exact same data in
production mode, but not under animation, it runs fine until about check
number 30 or so, at which time the disk goes berserk and the machine starts
thrashing. It appears that the swap file is running out of space.

Is there any reason that runnng under animation should use less memory than
production?

Donald
```

#### ↳ Re: net express promlem

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-06-19T19:15:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MZnIa.230$BM.184826@newssrv26.news.prodigy.com>`
- **References:** `<9rnIa.7811$9y3.753137@news20.bellglobal.com>`

```
"Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
news:9rnIa.7811$9y3.753137@news20.bellglobal.com...
> I have a customer with a net express problem that seems rather strange ...
> perhaps someone has an idea of what to try.  The version is Version 3.0.
>
> A cheque file is being printed with signatures.  The signatures are in BMP
> form, and the BMP file is read in once at the start of the program.  It is
1
> meg in size.
>
> When the program runs under test (IE-under animation), it runs perfectly.
> When the exact same INTS are run (no re-compile) with the exact same data
in
> production mode, but not under animation, it runs fine until about check
> number 30 or so, at which time the disk goes berserk and the machine
starts
> thrashing. It appears that the swap file is running out of space.
>
> Is there any reason that runnng under animation should use less memory
than
> production?

Well, if the animated run is for fewer checks than the production, and the
code which displays the bitmap image does not properly release prior
allocations, yes.

I've seen this fairly often with Windows GDI: you forget to DeleteObject and
BINGO! you have what is often called a "resource leak", which only has
physical manifestations when you've leaked a lot.

I'm not familiar with NetExpress at all, but I'd check whatever code the
programmer does write to insure that "get" and "release" functions are
properly paired.
```

##### ↳ ↳ Re: net express promlem

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-06-19T15:29:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgoIa.7874$9y3.756714@news20.bellglobal.com>`
- **References:** `<9rnIa.7811$9y3.753137@news20.bellglobal.com> <MZnIa.230$BM.184826@newssrv26.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:MZnIa.230$BM.184826@newssrv26.news.prodigy.com...
> "Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
> news:9rnIa.7811$9y3.753137@news20.bellglobal.com...
> > I have a customer with a net express problem that seems rather strange
...
> > perhaps someone has an idea of what to try.  The version is Version 3.0.
> >
> > A cheque file is being printed with signatures.  The signatures are in
BMP
> > form, and the BMP file is read in once at the start of the program.  It
is
> 1
> > meg in size.
> >
> > When the program runs under test (IE-under animation), it runs
perfectly.
> > When the exact same INTS are run (no re-compile) with the exact same
data
> in
> > production mode, but not under animation, it runs fine until about check
…[10 more quoted lines elided]…
> allocations, yes.

That was my first thought, and the first thing we checked was to grab the
complete set of production data, bring it in entirety over to the test
machine, and run it.  The problem did not exist.  We then checked
configurations on the two machines.  Identical.  The only confirmed
difference we have found is that the problem ONLY happens when not run in
test mode.

>
> I've seen this fairly often with Windows GDI: you forget to DeleteObject
and
> BINGO! you have what is often called a "resource leak", which only has
> physical manifestations when you've leaked a lot.
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: net express promlem

- **From:** chris.glazier@microfocus.com (Chris Glazier)
- **Date:** 2003-06-20T09:23:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<260cd566.0306200823.78dd7a0a@posting.google.com>`
- **References:** `<9rnIa.7811$9y3.753137@news20.bellglobal.com> <MZnIa.230$BM.184826@newssrv26.news.prodigy.com> <cgoIa.7874$9y3.756714@news20.bellglobal.com>`

```
Are you using the PC_PRINTER_LOAD_BITMAP, PC_PRINTER_WRITE_BITMAP
calls to print the bitmap on the check?

Do you also use PC_PRINTER_FREE_BITMAP when you are done with it?

Do you check the return-status after the calls, as a non-zero code
indicates an error.

If you are not using these calls, then what exactly are you using to
accomplish this task?


"Donald Tees" <Donald_Tees@sympatico.ca> wrote in message news:<cgoIa.7874$9y3.756714@news20.bellglobal.com>...
> "Michael Mattias" <michael.mattias@gte.net> wrote in message
> news:MZnIa.230$BM.184826@newssrv26.news.prodigy.com...
…[60 more quoted lines elided]…
> >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
