[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Looking for unix editor for COBOL students

_7 messages · 5 participants · 1995-02_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Looking for unix editor for COBOL students

- **From:** "m...." <ua-author-10347546@usenetarchives.gap>
- **Date:** 1995-02-07T09:27:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ua-fallback-mVHMVPcDpMM@usenetarchives.gap>`

```
This year we have abandoned our Mainframe COBOL (IBM COBOL II), for teaching
purposes and moved to a RISC6000 series box using an IBM badged unix-based
MicroFocus COBOL compiler. However with the move to unix I look it looks as
if my students will have to suffer (sic?) "vi" or "emacs" as the MicroFocus
compiler does not appear to have its own editor. (Students will be using
MicroFocus Personal COBOL on their PCs for development at home).

Can anyone suggest a (free?), simple, intuitive unix-based programmers editor
similar to the sort of offerings of Microsoft / Borland on the PC that my
students could use?

Thanks

Michael
m.··.@uws··u.au




Michael Turk
m.··.@uws··u.au

University of Western Sydney, Macarthur
Visit Camden, at the rural edge of Sydney, Australia
```

#### ↳ Re: Looking for unix editor for COBOL students

- **From:** "horo..." <ua-author-15202268@usenetarchives.gap>
- **Date:** 1995-02-07T09:52:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1af253fed0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-mVHMVPcDpMM@usenetarchives.gap>`
- **References:** `<ua-fallback-mVHMVPcDpMM@usenetarchives.gap>`

```
In article M.··.@uws··U.AU (Michael Turk) writes:
› From: M.··.@uws··U.AU (Michael Turk)
› Subject: Looking for unix editor for COBOL students
› Date: Tue, 7 Feb 1995 14:27:00
 
› This year we have abandoned our Mainframe COBOL (IBM COBOL II), for teaching 
› purposes and moved to a RISC6000 series box using an IBM badged unix-based 
…[3 more quoted lines elided]…
› MicroFocus Personal COBOL on their PCs for development at home).

I had a similiar problem, on a smaller scale. I used to be involved with a
software consulting business that work exclusively with Wang VS. When Wang
started to have problems, we started to look for other platforms. It was my
job to scout out the new platforms, and train the programming staff on how to
use the tools on the new system. When I started with Unix, I was *very*
concerned with vi. I thought that it would be a serious drawback to COBOL
development on Unix platforms. The major problem was, as consultants I needed
a replacement that I could port over several platforms (we were using AIX and
SCO in our office) and also licence on the wide range of boxes that our client
base would use. I came back to vi. It was an editor that was always going to
be available on every machine our people worked on.

So, I started to learn vi. I created a cheat sheet of commands, and after a
few days (weeks maybe) I started to like it. It is rich with features, once
you figure out how to use them.

Anyway, IMHO, If you want to teach people how to develop software on a Unix
(open systems) platform. Use the tools that are common to all platforms.

David
```

#### ↳ Re: Looking for unix editor for COBOL students

- **From:** "dbr..." <ua-author-535048@usenetarchives.gap>
- **Date:** 1995-02-08T00:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1af253fed0-p3@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-mVHMVPcDpMM@usenetarchives.gap>`
- **References:** `<ua-fallback-mVHMVPcDpMM@usenetarchives.gap>`

```
M.··.@uws··U.AU (Michael Turk) writes:

› This year we have abandoned our Mainframe COBOL (IBM COBOL II), for teaching 
› purposes and moved to a RISC6000 series box using an IBM badged unix-based 
…[3 more quoted lines elided]…
› MicroFocus Personal COBOL on their PCs for development at home).

If your RS/6000 has the pine e-mailer then it should have
the pico editor. They come as a set.
```

#### ↳ Re: Looking for unix editor for COBOL students

- **From:** "c..." <ua-author-17087649@usenetarchives.gap>
- **Date:** 1995-02-10T03:11:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1af253fed0-p4@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-mVHMVPcDpMM@usenetarchives.gap>`
- **References:** `<ua-fallback-mVHMVPcDpMM@usenetarchives.gap>`

```
M.··.@uws··U.AU (Michael Turk) writes:

› This year we have abandoned our Mainframe COBOL (IBM COBOL II), for teaching 
› purposes and moved to a RISC6000 series box using an IBM badged unix-based 
…[3 more quoted lines elided]…
› MicroFocus Personal COBOL on their PCs for development at home).

I use emacs 19 as my programming-environment and I do not *suffer*. I have
implemented some kind of cobol-mode that allows to edit cobol-programs with
respect to all the cobol-needs (writing in col's 8 - 72, no tab-chars, etc.).

It even allows you to compile your programs in a separate window and to jump
to the location of compilation-errors in the sourcefiles even accross multiple
COPY's.

Another nice feature is a key to jump to a corresponding word
(PERFORM <-> END-PERFORM, etc.) or to the place, where a variable or a
paragraph is defined.

And, last not least, programming e-lisp can be a good training, even for
cobol-programmers :-).

› Can anyone suggest a (free?), simple, intuitive unix-based programmers editor
› similar to the sort of offerings of Microsoft / Borland on the PC that my
› students could use?

Of course, emacs is free.

----------------------------------------------------------------------
Christian A. Lademann EMail:
--------------------- speaking from, not for: ------------------------
ZLS Software GmbH Tel.: (+49) 6195 900500
D-65779 Kelkheim Fax: (+49) 6195 900600
----------------------------------------------------------------------
```

#### ↳ Re: Looking for unix editor for COBOL students

- **From:** "def..." <ua-author-4572935@usenetarchives.gap>
- **Date:** 1995-02-12T12:56:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1af253fed0-p5@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-mVHMVPcDpMM@usenetarchives.gap>`
- **References:** `<ua-fallback-mVHMVPcDpMM@usenetarchives.gap>`

```
Robert Dewar (de··.@cs.··u.edu) wrote:
› I think introducing beginning students to Emacs is close to violating the
› punishment clause of the constitution. Yes, it is a wonderful took, but it
› is very complex for beginning students to get the hang of. Partly this is
› because there is, as far as I know, no really simply tutorial. 
 
› Try M-x info. There is a tutorial.
 
› I do not recommend teaching your beginning COBOL students to write Emacs
› E-Lisp macro programming :-)

Nor macro writing in vi. A beginning student only needs to know a couple of
keystrokes/commands to use any editor. Some to move around the screen, some to
delete and add text, file opening and saving etc. To me C-x C-f is
no more difficult to understand or remember then ":e ". Nor is M-d
more difficult than "dw". Students don't need to write E-Lisp to use Emacs,
that's for customization.
_________________________________________
/Andrew DeFaria (def··.@cup··p.com) ¥
|Hewlett Packard, California Language Lab |
|Phone: (408)-447-5741 |
|WWW: http://hpcll50.cup.hp.com/‾defaria |
¥_________________________________________/
```

#### ↳ Re: Looking for unix editor for COBOL students

- **From:** "def..." <ua-author-4572935@usenetarchives.gap>
- **Date:** 1995-02-12T22:50:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1af253fed0-p6@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-mVHMVPcDpMM@usenetarchives.gap>`
- **References:** `<ua-fallback-mVHMVPcDpMM@usenetarchives.gap>`

```
Michel BILLAUD (billaud@victor) wrote:
› For this reason I recommend MicroEmacs. Small version of emacs,
› loads quickly (I use it on my 8088 PC at 6Mhz), and so on.

Well I use an HP700 workstation most of the time. I've start Epoch (an emac
derivative that I happen to like) weeks ago and never exit it. Therefore I
don't have to worry about "loads quickly" - it doesn't have to load - it's
loaded already!
_________________________________________
/Andrew DeFaria (def··.@cup··p.com) ¥
|Hewlett Packard, California Language Lab |
|Phone: (408)-447-5741 |
|WWW: http://hpcll50.cup.hp.com/‾defaria |
¥_________________________________________/
```

#### ↳ Re: Looking for unix editor for COBOL students

- **From:** "def..." <ua-author-4572935@usenetarchives.gap>
- **Date:** 1995-02-21T20:10:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1af253fed0-p7@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-mVHMVPcDpMM@usenetarchives.gap>`
- **References:** `<ua-fallback-mVHMVPcDpMM@usenetarchives.gap>`

```
Dan Yates (ya··.@eag··n.edu) wrote:
› if you are looking for an editor that will run on a mini-computer that
› has an unix operating installed, may I suggest QEDIT from Robelle
…[3 more quoted lines elided]…
› this helps.

Both emacs and vi are full screen editors. The chances that vi will be on a
Unix system is 100%. The chances that emacs is on a Unix system are probably
80-90%. The chances that QEDIT is on a Unix system is probably close to zip.

Besides, in emacs I can easily insert the contains of a file located on a
machine across the country in a couple of keystrokes:

C-xi/def··a@mll··p.com/etc/group

And the /etc/group file from the machine mll.apollo.hp.com is magically sucked
into my current buffer. Try that in other editors!
_________________________________________
/Andrew DeFaria (def··.@cup··p.com) ¥
|Hewlett Packard, California Language Lab |
|Phone: (408)-447-5741 |
|WWW: http://hpcll50.cup.hp.com/‾defaria |
¥_________________________________________/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
