[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# (MicroFocus) DISPLAY statements to stdout ?

_3 messages · 3 participants · 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax)

---

### (MicroFocus) DISPLAY statements to stdout ?

- **From:** "Jacques Vidal" <syster.soft@wanadoo.fr>
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vm9rh$goh$1@wanadoo.fr>`

```
Hi,

Does anybody know how to redirect DISPLAY statements to
standard output with Win32 MicroFocus COBOL? I've tried
DISPLAY ... UPON SYSOUT and other things, but am still
unable to redirect DISPLAYed messages to a file. I guess
DISPLAYs default to display memory. How can I change this
behaviour?

TIA,

Jacques Vidal
```

#### ↳ Re: (MicroFocus) DISPLAY statements to stdout ?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381F3F50.8DAA4FFF@home.com>`
- **References:** `<7vm9rh$goh$1@wanadoo.fr>`

```


Jacques Vidal wrote:
> 
> Hi,
…[6 more quoted lines elided]…
> behaviour?

Not sure if this helps, but this is the NetExpress syntax :-

Formatï¿½1 (Line at a Time)

DISPLAY identifier-1 identifier-2 ...
        iteral-1     literal-2    
        UPON mnemonic-name  [ WITH NO ADVANCING ]
            function-name 
              [ON EXCEPTION imperative-statement-1]
              [NOT ON EXCEPTION imperative-statement-2]
              [END-DISPLAY]

(Allowing you to specify mnemonic/function in SPECIAL NAMES). The
mnemonic-name must be associated with a function-name in the
SPECIAL-NAMES paragraph in the Environment Division. For a list of valid
function-names, see the general rules of the SPECIAL-NAMES paragraph.
The mnemonic-name can have the following compiler-defined values, which
are specified in detail in the general rules.
	COMMAND-LINE
	ARGUMENT-NAME
	ARGUMENT-NUMBER
	ENVIRONMENT-VALUE
	ENVIRONMENT-NAME
	SYSERR

A bit of a half-baked approach, but if you are wanting to get it to a
file - from Windows, set printer to write to disk, then "DISPLAY UPON
PRINTER" ????

Jimmy, Calgary AB
```

#### ↳ Re: (MicroFocus) DISPLAY statements to stdout ?

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vmd6k$hbp$1@ssauraac-i-1.production.compuserve.com>`
- **References:** `<7vm9rh$goh$1@wanadoo.fr>`

```
    Assuming plain, ordinary displays without the AT clause (they roll the
screen when they reach the bottom of the screen), set COBSW=+S5.  The color
will change (if you are using ansi.sys, and have set a default color).  Then
all plain displays will redirect.  Note that this includes trace messages.
If you use display AT for normal program use (who would use a plain
display), then the screen will look normal when redirection is active.  Note
that trace output can create long files.



Jacques Vidal <syster.soft@wanadoo.fr> wrote in message
news:7vm9rh$goh$1@wanadoo.fr...
> Hi,
>
…[12 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
