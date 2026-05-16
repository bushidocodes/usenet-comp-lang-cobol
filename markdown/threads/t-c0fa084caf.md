[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need Assembly Lang Date Macros

_8 messages · 6 participants · 1999-07_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### Need Assembly Lang Date Macros

- **From:** "Phylis DeWeese" <pdeweese@highland.net>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nmu0o$pjd$1@news3.infoave.net>`

```
Hi everybody,
A gentleman who posts to this group sometimes referred me to y'all thinking
you may be able to help me.

I work on a Wang Vs and have made changes to our date routines to become y2k
compliant.  Everything was going great with testing until I ran into some
assembly programs  that are called.  Within the assembly program some macros
are used that deal with adding and subtracting julian dates. The real
problem comes when I am unable to find the source for these marcros.  I am
not an assembler programmer, so I don't feel that I can recreate these.  I
was hoping that maybe someone has some that they might share or know where I
might get some help!?

Phylis DeWeese
```

#### ↳ Re: Need Assembly Lang Date Macros

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379EFF2D.F893CEA2@zip.com.au>`
- **References:** `<7nmu0o$pjd$1@news3.infoave.net>`

```
Phylis DeWeese wrote:
> 
> Hi everybody,
…[12 more quoted lines elided]…
> Phylis DeWeese

For simple stuff like date mathematics I would suggest rewriting the
code in Cobol and using that Assembler for run time efficiency is just
not an issue any more with optimizing compilers and faster machines.

I think it was Judson that had a series of date modules on his home
page for download if you don't want to reinvent the wheel.

Ken
```

##### ↳ ↳ Re: Need Assembly Lang Date Macros

- **From:** "Phylis DeWeese" <pdeweese@highland.net>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nn152$puq$1@news3.infoave.net>`
- **References:** `<7nmu0o$pjd$1@news3.infoave.net> <379EFF2D.F893CEA2@zip.com.au>`

```

> For simple stuff like date mathematics I would suggest rewriting the
> code in Cobol and using that Assembler for run time efficiency is just
> not an issue any more with optimizing compilers and faster machines.

I Agree.

> I think it was Judson that had a series of date modules on his home
> page for download if you don't want to reinvent the wheel.

Okay, help me out here. ;-) Who is Judson? Do you know the address?
Thanks for responding.

Phylis
```

###### ↳ ↳ ↳ Re: Need Assembly Lang Date Macros

- **From:** "Warren Porter" <warrenp123@netdoor123.com>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<J_En3.389$_3.10333@axe.netdoor.com>`
- **References:** `<7nmu0o$pjd$1@news3.infoave.net> <379EFF2D.F893CEA2@zip.com.au> <7nn152$puq$1@news3.infoave.net>`

```
Phylis DeWeese wrote in message <7nn152$puq$1@news3.infoave.net>...
>
>> For simple stuff like date mathematics I would suggest rewriting the
…[9 more quoted lines elided]…
>Thanks for responding.


He must be on vacation.  Here is his signature from an earlier post.

Judson McClendon      judmc123@bellsouth.net  (remove numbers)
Sun Valley Systems    http://personal.bhm.bellsouth.net/~judmc
"For God so loved the world that He gave His only begotten Son, that
whoever believes in Him should not perish but have everlasting life."
```

#### ↳ Re: Need Assembly Lang Date Macros

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2IDn3.70$ds6.4533@dfiatx1-snr1.gtei.net>`
- **References:** `<7nmu0o$pjd$1@news3.infoave.net>`

```
Phylis DeWeese wrote in message <7nmu0o$pjd$1@news3.infoave.net>...
> ... macros
>are used that deal with adding and subtracting julian dates. The real
>problem comes when I am unable to find the source for these marcros.  I am
>not an assembler programmer, so I don't feel that I can recreate these.

Then don't. There are plenty of Julian date routines around in various code
libraries in multiple languages. (Y2K-compliant and others).

Instead of going on a treasure hunt to recreate the old macros, just
substitute new Julian routines.

MCM
```

##### ↳ ↳ Re: Need Assembly Lang Date Macros

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379F6E34.D40F3F82@home.com>`
- **References:** `<7nmu0o$pjd$1@news3.infoave.net> <2IDn3.70$ds6.4533@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> Then don't. There are plenty of Julian date routines around in various code
> libraries in multiple languages. (Y2K-compliant and others).
> 
Michael, specific COBOL links please ? And while I am it, (mechanically
challenged, remember), when you people see somebody giving a web
address, what's the technique you use to copy/paste it into a reference
address book - needs a note to say what the site is about.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Need Assembly Lang Date Macros

- **From:** "Jerry Peacock" <bismailspamno@bisusa.com>
- **Date:** 1999-07-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<msso3.577$i67.40351@typhoon01.swbell.net>`
- **References:** `<7nmu0o$pjd$1@news3.infoave.net> <2IDn3.70$ds6.4533@dfiatx1-snr1.gtei.net> <379F6E34.D40F3F82@home.com>`

```
Just click on the address displayed in the message - your
browser should open the site.
Then, in the browser, pick "Add to favorites"

James J. Gavan <jjgavan@home.com> wrote in message
news:379F6E34.D40F3F82@home.com...
> Michael Mattias wrote:
> >
> > Then don't. There are plenty of Julian date routines around in various
code
> > libraries in multiple languages. (Y2K-compliant and others).
> >
…[5 more quoted lines elided]…
> Jimmy, Calgary AB
```

##### ↳ ↳ Re: Need Assembly Lang Date Macros

- **From:** "Phylis DeWeese" <pdeweese@highland.net>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nn5l5$grp$1@news3.infoave.net>`
- **References:** `<7nmu0o$pjd$1@news3.infoave.net> <2IDn3.70$ds6.4533@dfiatx1-snr1.gtei.net>`

```

> Then don't. There are plenty of Julian date routines around in various
code
> libraries in multiple languages. (Y2K-compliant and others).

Could you be a little more specific as to where this code may be found.

> Instead of going on a treasure hunt to recreate the old macros, just
> substitute new Julian routines.

That is my plan. Where do I find new ones...I may not have stated it in my
original post very plainly.  I need addresses or if some one has some maybe
they would send them to me.

Phylis
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
