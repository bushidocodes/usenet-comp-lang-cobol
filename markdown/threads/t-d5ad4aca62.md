[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus Dialog

_6 messages · 4 participants · 2002-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus Dialog

- **From:** "JohnTheNonBaptist" <johnhhowe@cfl.rr.com>
- **Date:** 2002-09-23T11:36:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d8f355a_2@news.teranews.com>`

```
We have a screen set with multiple screens.  On the primary screen an F10
(11 and 12 also)key can defined and works great.  On any subsequent screen,
NOTHING.  F10 is completely ignored.  F9 will work but F10 will not.

Any suggestions!
```

#### ↳ Re: Micro Focus Dialog

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-09-23T22:05:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-mi3q4dpEsdqj@h24-82-204-17.wp.shawcable.net>`
- **References:** `<3d8f355a_2@news.teranews.com>`

```
On Mon, 23 Sep 2002 16:36:44 UTC, "JohnTheNonBaptist" 
<johnhhowe@cfl.rr.com> wrote:

> We have a screen set with multiple screens.  On the primary screen an F10
> (11 and 12 also)key can defined and works great.  On any subsequent screen,
…[3 more quoted lines elided]…
> 

I assume you have dialog defined for the F10 event on the subsequent 
screens, yes?

I have seen the F10 key trapped by Windows and directed to the window 
menu bar. What OS are you running?
```

##### ↳ ↳ Re: Micro Focus Dialog

- **From:** "JohnTheNonBaptist" <johnhhowe@cfl.rr.com>
- **Date:** 2002-09-25T09:28:25-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d91ba59$1_5@news.teranews.com>`
- **References:** `<3d8f355a_2@news.teranews.com> <ZpzG4UNLyRNq-pn2-mi3q4dpEsdqj@h24-82-204-17.wp.shawcable.net>`

```
Windows 2000 is the OS.

I understand about windows trapping F10, but what I don't understand is that
Dialog traps it on the first screen but not on the second.  Now that doesn't
make any sense.

<lsunley@mb.sympatico.ca> wrote in message
news:ZpzG4UNLyRNq-pn2-mi3q4dpEsdqj@h24-82-204-17.wp.shawcable.net...
> On Mon, 23 Sep 2002 16:36:44 UTC, "JohnTheNonBaptist"
> <johnhhowe@cfl.rr.com> wrote:
>
> > We have a screen set with multiple screens.  On the primary screen an
F10
> > (11 and 12 also)key can defined and works great.  On any subsequent
screen,
> > NOTHING.  F10 is completely ignored.  F9 will work but F10 will not.
> >
…[10 more quoted lines elided]…
> Lorne Sunley
```

###### ↳ ↳ ↳ Re: Micro Focus Dialog

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-09-25T23:47:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-v1Kz2X5QKdIZ@h24-82-204-17.wp.shawcable.net>`
- **References:** `<3d8f355a_2@news.teranews.com> <ZpzG4UNLyRNq-pn2-mi3q4dpEsdqj@h24-82-204-17.wp.shawcable.net> <3d91ba59$1_5@news.teranews.com>`

```
I have seen stranger things happen.

About the only way to avoid it is to re-code to use an F key that is 
not "reserved"

Lorne

On Wed, 25 Sep 2002 14:28:25 UTC, "JohnTheNonBaptist" 
<johnhhowe@cfl.rr.com> wrote:

> Windows 2000 is the OS.
> 
…[27 more quoted lines elided]…
> 
```

#### ↳ Re: Micro Focus Dialog

- **From:** Harald.Cordes@microfocus.com (Harald Cordes)
- **Date:** 2002-09-24T00:15:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1fabdc0d.0209232315.387de384@posting.google.com>`
- **References:** `<3d8f355a_2@news.teranews.com>`

```
F10 belongs to the Windows operating system for Windows with a system
menue. In this case Windows does not forward F10 (and Alt-F-4, I
think) to DialogSystem.
```

##### ↳ ↳ Re: Micro Focus Dialog

- **From:** MRandall3@AOL.com (M. Randall)
- **Date:** 2002-09-29T23:57:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dacb0f5.0209292257.363794f8@posting.google.com>`
- **References:** `<3d8f355a_2@news.teranews.com> <1fabdc0d.0209232315.387de384@posting.google.com>`

```
Harald.Cordes@microfocus.com (Harald Cordes) wrote in message news:<1fabdc0d.0209232315.387de384@posting.google.com>...
> F10 belongs to the Windows operating system for Windows with a system
> menue. In this case Windows does not forward F10 (and Alt-F-4, I
> think) to DialogSystem.

Dear Harald:

I am guessing that is what they teach you in training for Dialog
because that is what Chris Glazier told me.  When Chris was out of the
office I ended up talking to Brian Economy on a seperate issue, and
mentioned to him my desire to capture F10.  He researched and gave me
some dialog to capture the event.

Which leads me to question the original post:

Dear John:

You have to hate those dear John letter jokes.  Anyway, what were you
doing with F10 in your screenset?  Are you just trying to activate the
menu bar, and it is not working on the subsequent screens?  Or, are
you running through some of your own dialog?  Where are you placing
the logic -- in global or window dialog?  The reason I ask, is I
played a little with what Brian gave me, but not enough to get it to
work, so if you are capturing the event on the main screen in global,
I would be curious what your dialog looks like.

Mike

-- About life being serious - what if you seriously messed up your
life?  :-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
