[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Screen Save in MFCOBOL under UNIX

_5 messages · 5 participants · 1999-01_

---

### Screen Save in MFCOBOL under UNIX

- **From:** shanmugam@my-dejanews.com
- **Date:** 1999-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<770th5$ghk$1@nnrp1.dejanews.com>`

```
Dear friends,

Can anybody tell me how to save snap shot of a screen and restore it back. I
am having a user interface COBOL program written using MFCOBOL DISPLAY/ACCEPT
statements (without any screen section). I want to do..  1) Save the screen
contents  2) Display another screen (say LookUp/HELP Screen)  3) Display back
the saved Screen. Basically I have want to provide field level help screens
using DISPLAY/ACCEPT statements.


-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Screen Save in MFCOBOL under UNIX

- **From:** Kevin Digweed <Kevin.Digweed@dial.pipex.com>
- **Date:** 1999-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3694A020.8AF06099@dial.pipex.com>`
- **References:** `<770th5$ghk$1@nnrp1.dejanews.com>`

```
shanmugam@my-dejanews.com wrote:
> Dear friends,
> 
> Can anybody tell me how to save snap shot of a screen and restore it back. I
> am having a user interface COBOL program written using MFCOBOL DISPLAY/ACCEPT
> statements (without any screen section).

Take a look at the "Call-by-name Routines" chapter of your
documentation. The relevant routines are in the CBL_READ_SCR_???? and
CBL_WRITE_SCR_???? family.

Cheers, Kev.
```

#### ↳ Re: Screen Save in MFCOBOL under UNIX

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_L2l2.4587$dS4.1818236@news2.mia>`
- **References:** `<770th5$ghk$1@nnrp1.dejanews.com>`

```
shanmugam@my-dejanews.com wrote
>
>Can anybody tell me how to save snap shot of a screen and restore it back. I
…[4 more quoted lines elided]…
>using DISPLAY/ACCEPT statements.

Put the code which displays the screen, and the code which displays
the help in separate paragraphs.  Perform the associated paragraph
whenever you want to display that screen.
```

#### ↳ Re: Screen Save in MFCOBOL under UNIX

- **From:** g1dlc@Radix.Net (David L. Craig)
- **Date:** 1999-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<772hh8$qc0$1@saltmine.radix.net>`
- **References:** `<770th5$ghk$1@nnrp1.dejanews.com>`

```
In article <770th5$ghk$1@nnrp1.dejanews.com>,
 <shanmugam@my-dejanews.com> wrote:
>
> Can anybody tell me how to save snap shot of a screen and
…[6 more quoted lines elided]…
> using DISPLAY/ACCEPT statements.

I would study the "Screen Section" documentation that
begins on page 4-155 of the "Micro Focus Object COBOL
and COBOL Language Reference" manual, Issue 15, May 1995.
This syntax is XOPEN compliant and facilitates everything
you mention.
```

#### ↳ Re: Screen Save in MFCOBOL under UNIX

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-n27nTRxC8tC4@Dwight_Miller.iix.com>`
- **References:** `<770th5$ghk$1@nnrp1.dejanews.com>`

```
On Thu, 7 Jan 1999 00:01:43, shanmugam@my-dejanews.com wrote:

> Dear friends,
> 
…[6 more quoted lines elided]…
>

Look up the Library Routines: CBL_READ_SCRCHRATTRS (from memory) and 
CBL_WRITE_SCRCHRATTRS
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
