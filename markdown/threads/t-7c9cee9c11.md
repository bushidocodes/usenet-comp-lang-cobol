[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT: ISPF Question

_10 messages · 6 participants · 2004-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Off-topic and spam`](../topics.md#spam)

---

### OT: ISPF Question

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2004-03-10T13:14:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6emu40lpa35431uritr83501vv38bfn31q@4ax.com>`

```
This is a question for you mainframers who do your COBOL programming
in ISPF.  In all of the years that I've used it, there has always been
one annoying thing about the editing environment (well there are a
lot, but this is post is only about 1).  When you enter the line
command COLS, you get a nice scale on the line right after the
command.  But once you page forward, that scale is gone.

Does anyone know of a way in ISPF to have a scale, say on line 1 and
have it stay there even when paging forward or backward?

Thanks.


          ////
         (o o)
-oOO--(_)--OOo-


"Once in Africa I lost the corkscrew and we were
forced to live on food and water for weeks."
-- Ernest Hemingway
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: OT: ISPF Question

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2004-03-10T21:10:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rQMJBjC+Q4TAFwmq@ld50macca.demon.co.uk>`
- **References:** `<6emu40lpa35431uritr83501vv38bfn31q@4ax.com>`

```
Er....no. But the columns applicable to the screen are listed in the top 
right corner. You could always use BOUNDS to set the columns on view to 
those you need to see.

In message <6emu40lpa35431uritr83501vv38bfn31q@4ax.com>, SkippyPB 
<swiegand@neo.rr.NOSPAM.com> writes
>This is a question for you mainframers who do your COBOL programming

> When you enter the line
>command COLS, you get a nice scale on the line right after the
…[20 more quoted lines elided]…
>Steve
```

#### ↳ Re: OT: ISPF Question

- **From:** Bill TB <thunderbox@hotmail.com>
- **Date:** 2004-03-11T12:05:13+11:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2P3c.3174$KS1.167372@nasal.pacific.net.au>`
- **In-Reply-To:** `<6emu40lpa35431uritr83501vv38bfn31q@4ax.com>`
- **References:** `<6emu40lpa35431uritr83501vv38bfn31q@4ax.com>`

```
No, but you could set an Fkey up for that rather than typing it in all 
the time. Of course, you gotta find a slot not used !

Bill

SkippyPB wrote:
> This is a question for you mainframers who do your COBOL programming
> in ISPF.  In all of the years that I've used it, there has always been
…[23 more quoted lines elided]…
> Steve
```

#### ↳ Re: OT: ISPF Question

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-03-10T21:31:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-EF8BC2.21313810032004@corp.supernews.com>`
- **References:** `<6emu40lpa35431uritr83501vv38bfn31q@4ax.com>`

```
In article <6emu40lpa35431uritr83501vv38bfn31q@4ax.com>,
 SkippyPB <swiegand@neo.rr.NOSPAM.com> wrote:

> This is a question for you mainframers who do your COBOL programming
> in ISPF.  In all of the years that I've used it, there has always been
…[6 more quoted lines elided]…
> have it stay there even when paging forward or backward?

Yes, but it is an ugly way.

You can change the panel for the edit screen.  On your customized panel, 
you can make the last static line before the data lines the ruler.

If you concatenate your personal panel ahead of the default system edit 
panel the edit program will use your panel.

This solution might break every time your shop upgrades ISPF versions.
```

#### ↳ Re: OT: ISPF Question

- **From:** Joseph Katnic <usrr@post.no.mail>
- **Date:** 2004-03-11T20:38:38+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<110320042038382425%usrr@post.no.mail>`
- **References:** `<6emu40lpa35431uritr83501vv38bfn31q@4ax.com>`

```

Why would you want to.
Thats what intelligent tabbing is for.
You set your tabs up once (e.g. for COBOL) and the editor remembers
them forever - well almost.


In article <6emu40lpa35431uritr83501vv38bfn31q@4ax.com>, SkippyPB
<swiegand@neo.rr.NOSPAM.com> wrote:

> This is a question for you mainframers who do your COBOL programming
> in ISPF.  In all of the years that I've used it, there has always been
…[7 more quoted lines elided]…
>
```

#### ↳ Re: OT: ISPF Question

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2004-03-11T17:01:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040311.17013341@rechner12.lerch.home>`
- **References:** `<6emu40lpa35431uritr83501vv38bfn31q@4ax.com>`

```

>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 10.03.04, 18:14:06, schrieb SkippyPB <swiegand@neo.rr.NOSPAM.com> zum 
Thema OT: ISPF Question:


> This is a question for you mainframers who do your COBOL programming
> in ISPF.  In all of the years that I've used it, there has always been
…[3 more quoted lines elided]…
> command.  But once you page forward, that scale is gone.

hello

Why you do not use tab

enter prof 99 on Command ==> and you will see all of the profile lines
then you can fill the tabs line like this:

000001 
----+----1----+----2----+----3----+----4----+----5----+----6----+----
7-
=TABS#       *   *             *                 *           *         
      *
=MASK#
=BNDS# <
000002        01                filler            pic x(08)   value 
spaces,
''''''            05            test              pic 9(04)   value 
zeroes.

Then: 
tabs on
on command ==> line and tabs will work.

Every time you use the tab-key (forward / backward) your cursor is 
moved one byte after the *
if you use - as a tab character enter moves to the next - 

if you want to enter a character over the attrib-byte you must 
posistioning then cursor at the unvisibil position attrib-byte - press 
enter and you can overtype all tabs position in that line.

another way to set off tab-positions is to erase the line-number - 
press enter - and all lines with no line number are full editing

if you trimm your tab-positions quit well most lines can be insertet 
without (temp) delete of attrib byte.

One point. Every type dsn A.B.CBL A.B.TMP will have his own 
profile-set (Maximum ist defined in the undergrounds of ISPF) an the 
profile which is used comes on the first line of the Prof command:

=PROF# ....TMP (DATA - 80)

this means -->
Last Qual of the dsn is TMP
the recordsize is 80 bytes (i dont know FB/VB is another differenz 
indicator....)
if the recordsize is the same you can use PROF CBL to switch to the 
Cobol profile.

Take some time to read the sections TABS and PROFILE in ISPF - and 
other very usefull things like overlay picture strings and and and

and you will do your job in half the time :-)

I use ispf myself since 1982/83 and on my pc i use SPF/2 (ISPF for 
OS/2) full function with REXX EDIT macro and so on....

Have a nice day - an good luck

Andreas
```

##### ↳ ↳ Re: OT: ISPF Question

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2004-03-13T11:02:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2c650ljgau4lkjtlao5rrkuvdbh5u07ie@4ax.com>`
- **References:** `<6emu40lpa35431uritr83501vv38bfn31q@4ax.com> <20040311.17013341@rechner12.lerch.home>`

```
On Thu, 11 Mar 2004 17:01:33 GMT, Andreas Lerch
<andreas@andreas-lerch.de> enlightened us:

>
>>>>>>>>>>>>>>>>>>> Ursprï¿½ngliche Nachricht <<<<<<<<<<<<<<<<<<
…[74 more quoted lines elided]…
>

Thanks for the tips.  I had forgotten about Tabs and in fact I tried
to get them to work but I wasn't having much success.  Your
explanation shows me where I erred.  But I am a visual person and I
still like have a scale at the top :)  

Regards,

          ////
         (o o)
-oOO--(_)--OOo-


"Once in Africa I lost the corkscrew and we were
forced to live on food and water for weeks."
-- Ernest Hemingway
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: ISPF Question

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2004-03-14T12:47:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040314.12472779@rechner12.lerch.home>`
- **References:** `<6emu40lpa35431uritr83501vv38bfn31q@4ax.com> <20040311.17013341@rechner12.lerch.home> <f2c650ljgau4lkjtlao5rrkuvdbh5u07ie@4ax.com>`

```


>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 13.03.04, 16:02:55, schrieb SkippyPB <swiegand@neo.rr.NOSPAM.com> zum 
Thema Re: OT: ISPF Question:

Hello

> Thanks for the tips.  I had forgotten about Tabs and in fact I tried
> to get them to work but I wasn't having much success.  Your
> explanation shows me where I erred.  But I am a visual person and I
> still like have a scale at the top :)

I am a visual person too :-)

You can modify the edit-panel (ISREDIT in ispplib) if you know how 
EDSET will work.

i.e. One line below the Commandline you can put your scale line
and with a command (Scale on/Scale off) modify the visibility.

or you can take the ultimative hardware-solution - cut a scale out of 
paper - and glue it at the top of your screen :-) on real hardware 
3270-5 i do this to see the 24 line limit of a 3270-2.

have a nice day - Andreas
```

###### ↳ ↳ ↳ Re: OT: ISPF Question

_(reply depth: 4)_

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2004-03-14T13:22:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3m8950plcu85dp2uvmaekb0s10ish4jhoa@4ax.com>`
- **References:** `<6emu40lpa35431uritr83501vv38bfn31q@4ax.com> <20040311.17013341@rechner12.lerch.home> <f2c650ljgau4lkjtlao5rrkuvdbh5u07ie@4ax.com> <20040314.12472779@rechner12.lerch.home>`

```
On Sun, 14 Mar 2004 12:47:27 GMT, Andreas Lerch
<andreas@andreas-lerch.de> enlightened us:

>
>
…[23 more quoted lines elided]…
>

LOL!  I love low-tech solutions :)

>have a nice day - Andreas
>
>
Regards,

          ////
         (o o)
-oOO--(_)--OOo-


"Once in Africa I lost the corkscrew and we were
forced to live on food and water for weeks."
-- Ernest Hemingway
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: OT: ISPF Question

_(reply depth: 5)_

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2004-03-15T18:25:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040315.18253741@rechner12.lerch.home>`
- **References:** `<6emu40lpa35431uritr83501vv38bfn31q@4ax.com> <20040311.17013341@rechner12.lerch.home> <f2c650ljgau4lkjtlao5rrkuvdbh5u07ie@4ax.com> <20040314.12472779@rechner12.lerch.home> <3m8950plcu85dp2uvmaekb0s10ish4jhoa@4ax.com>`

```

> On Sun, 14 Mar 2004 12:47:27 GMT, Andreas Lerch
> <andreas@andreas-lerch.de> enlightened us:

hello

> >
> >I am a visual person too :-)
> >
> >You can modify the edit-panel (ISREDIT in ispplib) if you know how
> >EDSET will work.

Today - at work - i have a look on that - ispf (IBM) does a panel 
switch
ISREDIT2 <--> ISREDIT4 with the option EDSET

so you can only change these panels or invoke ISPEXEC EDIT 
PANEL(your_panel_name) . . . to resolve your problem - i.e. There is 
no way, else you would program yourself :-)

> >
> >or you can take the ultimative hardware-solution - cut a scale out of
> >paper - and glue it at the top of your screen :-) on real hardware
> >3270-5 i do this to see the 24 line limit of a 3270-2.
> >

> LOL!  I love low-tech solutions :)

oh 32 an 24 line thats true - i have designed a 25 line panel and --> 
error, error, error, error


this is the last message from me to this (ot)-theme. It's very 
interesting, because it shows me what difference of kind of work exist 
and what kind of solutions are requested.
ISPF/PDF is one of the gratest (yes) programming tool for (old and 
likely) languages that was ever builded. I work whit it since 1984 and 
I invest a lot, very lot, of time to produce useable tools under ispf. 
DBRC Command Interface, IMS generation Utility, some Edit tools like 
EDITC/BROWSEC (Cursor+PF selected invokation of ..) special menues 
with DB2 and a lot more

But, i can 'Only bring a Solution' if i can understand the usability 
and take a job (view by view - (wo)man to (wo)man) to resolve the 
problem and bring down, in a suitable area, the time to do our job,

Thank you, Steve, I have to do so much and to learn!

einen schoenen Tag - Andreas
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
