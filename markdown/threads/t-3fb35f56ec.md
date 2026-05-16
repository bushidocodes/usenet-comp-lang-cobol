[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu v5 CALL problem

_7 messages · 4 participants · 2000-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu v5 CALL problem

- **From:** B W Spoor <bwspoor@fridaycs.co.uk>
- **Date:** 2000-05-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392A8011.AA366AC8@fridaycs.co.uk>`

```
Hi,

I've just started evaluating the Fujitsu cobol as a replacement for MF
and have encountered a problem with CALL when moving code over.

The code fragment:-

    05  nm-prog-curr   pic x(8).
    05  nm-prog-next   pic x(8).

    move "NMINIT" to nm-prog-next.
    perform until nm-prog-next = spaces
        move nm-prog-next to nm-prog-curr
        move "NMQUICK"    to nm-prog-next
        call nm-prog-curr using nmlink-area
                          on exception move spaces to nm-prog-next
        end-call
    end-perform.

results in the "on exception" action being taken, if I remove the clause
I then get an error 0x485 cannot call program NMINIT.

However the code fragment:-

    call "NMINIT" using nmlink-area.

works okay.

As my programs work around the first sequence, this is a major problem
for me. NMMENU/NMQUICK return the next program module required by the
user into nm-prog-next.

I haven't been able to find the error codes in the online documentation
- where should I look?

Anybody any ides?

Thanks,

Brian
```

#### ↳ Re: Fujitsu v5 CALL problem

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-05-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qXxW4.4104$X9.56212@typhoon.austin.rr.com>`
- **References:** `<392A8011.AA366AC8@fridaycs.co.uk>`

```
>         call nm-prog-curr using nmlink-area
>                           on exception move spaces to nm-prog-next
…[12 more quoted lines elided]…
> user into nm-prog-next.

Maybe others can help you. If on the other hand it turns out that
you cannot call dynamically, you can always (on any platform)
do the following:

move "NMINIT" to prog
if prog = "ABC"
     call  "ABC" using
else
if prog = "KLM"
     call  "KLM" using
else
if prog = "NMINIT"
     call  "NMINIT" using
else
if prog = "XYZ"
     call  "XYZ" using
else
etc. etc.
```

##### ↳ ↳ Re: Fujitsu v5 CALL problem

- **From:** B W Spoor <bwspoor@fridaycs.co.uk>
- **Date:** 2000-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392AE547.4DF500A1@fridaycs.co.uk>`
- **References:** `<392A8011.AA366AC8@fridaycs.co.uk> <qXxW4.4104$X9.56212@typhoon.austin.rr.com>`

```
Thanks, I've used an EVALUATE to do what you have suggested and it works
fine, but in the long term will mean having to change the main program
whenever I add an additional module.

I would prefer to use dynamic in the long term (after I have hte
conversion sorted).

Regrads,

Brian


Leif Svalgaard wrote:
> 
> >         call nm-prog-curr using nmlink-area
…[32 more quoted lines elided]…
> etc. etc.
```

###### ↳ ↳ ↳ Re: Fujitsu v5 CALL problem

- **From:** B W Spoor <bwspoor@fridaycs.co.uk>
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392D9290.9D9B1E9F@fridaycs.co.uk>`
- **References:** `<392A8011.AA366AC8@fridaycs.co.uk> <qXxW4.4104$X9.56212@typhoon.austin.rr.com> <392AE547.4DF500A1@fridaycs.co.uk>`

```
B W Spoor wrote:
 
Thanks to those who replied to this problem.

With the help of Lee at Fujitsu support, I've got the initial modules of
the system compiling and running just as I wanted in dynamic load mode.

Now I'm into debugging the differences between MF and Fujitsu (system
calls), everything else seems to be fine.

Almost time to bring in the Flexus GUI screens (adn reports).
 
Regards,

Brian
```

#### ↳ Re: Fujitsu v5 CALL problem

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392aad0c.150331158@news.cox-internet.com>`
- **References:** `<392A8011.AA366AC8@fridaycs.co.uk>`

```
You are making Dynamic vs Static calls when you use the variable name
vs the literal.  

Fujitsu COBOL follows Windows "Rules" to the letter.  When Windows
loads a mainline EXE it also loads all of the supporting DLL's into
memory.  (1 level down).  When you call one of these DLL's before it
runs windows loads in all the DLL's that it calls directly.  If one of
these DLL files is missing you get the "cannot call" message.  I
suspect that one of the DLL's called by NMINIT or NMQUICK 
 is missing.

On Tue, 23 May 2000 11:50:36 GMT, B W Spoor <bwspoor@fridaycs.co.uk>
wrote:

>Hi,
>
…[37 more quoted lines elided]…
>Brian
```

##### ↳ ↳ Re: Fujitsu v5 CALL problem

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-05-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gf17l$g43$1@news.cerf.net>`
- **References:** `<392A8011.AA366AC8@fridaycs.co.uk> <392aad0c.150331158@news.cox-internet.com>`

```
"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:392aad0c.150331158@news.cox-internet.com...
> You are making Dynamic vs Static calls when you use the variable name
> vs the literal.
…[3 more quoted lines elided]…
> memory.  (1 level down).

This is not necessarily true, there is a technique called late binding,
which if they use it, will leave the DLLs on the disk until they are
actually called. This technique is particularly useful for DLLs like
winspool32.drv and netapi32.dll as they have a lot of overhead in their
initialization.

If this technique is used properly, worst case environments actually can
mean a load time improvement of several seconds.

Cheesle.
```

###### ↳ ↳ ↳ Re: Fujitsu v5 CALL problem

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392bfaf2.235822172@news.cox-internet.com>`
- **References:** `<392A8011.AA366AC8@fridaycs.co.uk> <392aad0c.150331158@news.cox-internet.com> <8gf17l$g43$1@news.cerf.net>`

```
On Tue, 23 May 2000 15:37:36 -0700, "Cheesle"
<cheesle@online.NoSpamPlease.no> wrote:

>This is not necessarily true, there is a technique called late binding,
>which if they use it, will leave the DLLs on the disk until they are
…[6 more quoted lines elided]…
>

Fujitsu does support late binding, but tells you to look at your
linker manual to figure out how.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
