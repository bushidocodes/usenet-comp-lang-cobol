[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Printing to a HP4 laserjet

_5 messages · 4 participants · 1998-05_

---

### Printing to a HP4 laserjet

- **From:** "jerri schrijver" <ua-author-17075449@usenetarchives.gap>
- **Date:** 1998-05-05T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd78c5$33fe82d0$491e00c0@jerri>`

```

Goodmorning,

We have a MicroFocus Cobol programm running under DOS on a Win95 system.
Currently it is using a matrix printer to print to (NEC).
In waiting on a new windows programm we like to start printing to a HP
Laserjet 4.
I tried to print to the HP but it doesn't generate the correct output.
How do I do this?

TIA,

Jerri
(je··.@mi··t.nl)
```

#### ↳ Re: Printing to a HP4 laserjet

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-05T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6391bbbf4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd78c5$33fe82d0$491e00c0@jerri>`
- **References:** `<01bd78c5$33fe82d0$491e00c0@jerri>`

```

› We have a MicroFocus Cobol programm running under DOS on a Win95 system.
› Currently it is using a matrix printer to print to (NEC).
…[3 more quoted lines elided]…
› How do I do this?

You do not say what you do get ... the printer maybe just set to
the wrong font. Try powering it up and down.

Another thing to keep in mind is that a laser does not print until
a formfeed is issued. To do that in Cobol, you have to print
after/before PAGE.

An interesting thing you can do with that set-up is output a page, then
before giving the formfeed, home the cursor and overlay forms,
pictures, etc. In effect, a laser behaves like a screen. You paint onto
the laser memory, then when complete, give the formfeed.
```

#### ↳ Re: Printing to a HP4 laserjet

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-05-05T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6391bbbf4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bd78c5$33fe82d0$491e00c0@jerri>`
- **References:** `<01bd78c5$33fe82d0$491e00c0@jerri>`

```

Jerri,

It sounds like you are migrating your application from DOS to Windows -
is this correct? If so, then you should look at the PC_WIN_PRINTER
call-by-name routines which support printing through the Windows
Print Manager.

Hope this helps.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus International.

Jerri Schrijver wrote in message <01bd78c5$33fe82d0$491e00c0@jerri>...
› Goodmorning,
› 
…[11 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Printing to a HP4 laserjet

- **From:** "jerri schrijver" <ua-author-17075449@usenetarchives.gap>
- **Date:** 1998-05-05T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6391bbbf4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6391bbbf4-p3@usenetarchives.gap>`
- **References:** `<01bd78c5$33fe82d0$491e00c0@jerri> <gap-a6391bbbf4-p3@usenetarchives.gap>`

```

Hi Paddy,

Thanks for your reply. I am not sure I understand your answer. We have a
Win95 OS and we still use a dos based cobol accounting programm. Instead of
letting this programm print to a matrix printer we want it to connect to
the HP printer.
Because of the driver used by this programm is specially written to support
NEC it is
messing up the HP print results.

And yes, we are trying to rewrite it in Delphi because the company that
sold the
programm no longer exists. Perhaps i may be so bold to ask you if there is
a utility
available to convert the *.dat files to csv or paradox.

Thanks again hope you can help,

Jerri
(je··.@mi··t.nl)
```

#### ↳ Re: Printing to a HP4 laserjet

- **From:** "nop0..." <ua-author-471015@usenetarchives.gap>
- **Date:** 1998-05-05T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6391bbbf4-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bd78c5$33fe82d0$491e00c0@jerri>`
- **References:** `<01bd78c5$33fe82d0$491e00c0@jerri>`

```

On 6 May 1998 08:01:45 GMT, "Jerri Schrijver" wrote:

› Goodmorning,
› 
…[10 more quoted lines elided]…
› (je··.@mi··t.nl)
go to www.flexus.com and try winprint.
It is great for windows printing

best
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
