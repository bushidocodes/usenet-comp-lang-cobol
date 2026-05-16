[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SP2 ---- HELP!!!!!!!!!

_5 messages · 3 participants · 2001-06_

---

### SP2 ---- HELP!!!!!!!!!

- **From:** "J MacRae" <jmacrae1@mbox.rrc.mb.ca>
- **Date:** 2001-06-26T16:10:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iu2_6.649$K7.19304@news2.mts.net>`

```
Hi, I am new to sp2 and am having some trouble.
What I need to do is display an Inquiry Screen to get criteria from the user
and after retrieving the data redisplay the screen.
The user enters criteria and presses FIND, control is returned  to the COBOL
program in order to retrieve the record and move the data into the panel
fields.  The problem is that once the data is retrieved I cannot redisplay
the updated window.

I tried this:

CALL "SP2" USING SP2-DISPLAY-WINDOW SP2-NULL-PARM.

but no luck.

Any suggestions?  Thanks.
Jason.
```

#### ↳ Re: SP2 ---- HELP!!!!!!!!!

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-26T13:53:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0106261253.55e4382b@posting.google.com>`
- **References:** `<iu2_6.649$K7.19304@news2.mts.net>`

```
I think Bob already answered you, but what you do is:

Call "Sp2" using sp2-converse-panel xxxxx-converse-data

and you will do the I/O on the panel.  Display doesn't "Get" any data.

"J MacRae" <jmacrae1@mbox.rrc.mb.ca> wrote in message news:<iu2_6.649$K7.19304@news2.mts.net>...
> Hi, I am new to sp2 and am having some trouble.
> What I need to do is display an Inquiry Screen to get criteria from the user
…[13 more quoted lines elided]…
> Jason.
```

##### ↳ ↳ Re: SP2 ---- HELP!!!!!!!!!

- **From:** "J MacRae" <jmacrae1@mbox.rrc.mb.ca>
- **Date:** 2001-06-27T20:01:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AYq_6.673$K7.19852@news2.mts.net>`
- **References:** `<iu2_6.649$K7.19304@news2.mts.net> <bfdfc3e8.0106261253.55e4382b@posting.google.com>`

```
Yeah, it would be nice if it were that easy, but it didn't work so something
else must be jiggered.
The window is shown the first time and I can show other panels, but it won't
refresh the one I want.
Maybe I'm just a doink, but I'm not having fun.


"Thane Hubbell" <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0106261253.55e4382b@posting.google.com...
> I think Bob already answered you, but what you do is:
>
…[4 more quoted lines elided]…
> "J MacRae" <jmacrae1@mbox.rrc.mb.ca> wrote in message
news:<iu2_6.649$K7.19304@news2.mts.net>...
> > Hi, I am new to sp2 and am having some trouble.
> > What I need to do is display an Inquiry Screen to get criteria from the
user
> > and after retrieving the data redisplay the screen.
> > The user enters criteria and presses FIND, control is returned  to the
COBOL
> > program in order to retrieve the record and move the data into the panel
> > fields.  The problem is that once the data is retrieved I cannot
redisplay
> > the updated window.
> >
…[7 more quoted lines elided]…
> > Jason.
```

###### ↳ ↳ ↳ Re: SP2 ---- HELP!!!!!!!!!

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-27T19:00:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0106271800.58e54b98@posting.google.com>`
- **References:** `<iu2_6.649$K7.19304@news2.mts.net> <bfdfc3e8.0106261253.55e4382b@posting.google.com> <AYq_6.673$K7.19852@news2.mts.net>`

```
Send me a private email and I'll give you a hand.  Most probably cause
- the xxxx-next-panel is not set to the name of he panel you want to
converse.  Just a guess, but if you send me a private note I'll give
you a hand.


"J MacRae" <jmacrae1@mbox.rrc.mb.ca> wrote in message news:<AYq_6.673$K7.19852@news2.mts.net>...
> Yeah, it would be nice if it were that easy, but it didn't work so something
> else must be jiggered.
…[33 more quoted lines elided]…
> > > Jason.
```

#### ↳ Re: SP2 ---- HELP!!!!!!!!!

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 2001-06-27T01:37:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010626213735.29044.00000975@ng-bg1.aol.com>`
- **References:** `<iu2_6.649$K7.19304@news2.mts.net>`

```
Hi Jason,

If you are still having problems with this you could send me your panel and I
could write a little program to work with it as an example.  

Bob Hennessey
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
