[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ACUCOBOL 85

_2 messages · 2 participants · 1997-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### ACUCOBOL 85

- **From:** "dben..." <ua-author-758965@usenetarchives.gap>
- **Date:** 1997-10-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19971017171100.NAA24536@ladder01.news.aol.com>`

```

I am trying to learn COBOL with this Acucobol85 starter kit using my notepad as
the editor. The manual will not be out until 12/97. Has anyone had experience
with this. I can't seem to get anything to compile.
```

#### ↳ Re: ACUCOBOL 85

- **From:** "james h. zisch" <ua-author-6588870@usenetarchives.gap>
- **Date:** 1997-10-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aaa0c081ad-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19971017171100.NAA24536@ladder01.news.aol.com>`
- **References:** `<19971017171100.NAA24536@ladder01.news.aol.com>`

```

DBens8888 wrote:
›
› I am trying to learn COBOL with this Acucobol85 starter kit using my notepad as
› the editor. The manual will not be out until 12/97. Has anyone had experience
› with this. I can't seem to get anything to compile.

Having responded to your account directly, wanted to post a response
here as well so that others can benefit from the information:

Hello DBens8888,

Pleased to see you've discovered Acucobol. Here's how to get started,
in three simple steps:

1. Setup:

Since you mentioned using NotePad, let's presume you're using Windows,
Windows 95 or Windows NT...

Assure your PATH contains the sub-directory to the ACUCOBOL BIN
directory. If it does not, add its path to your AUTOEXEC.BAT file and
restart (re-boot).

2. Compiling:

Compile your source using the compiler; named CCBLxx.exe, where "xx"
is either 16 (16 bit for DOS and Win 3.x) or 32 (32 bit for Win 95 and
NT). Syntax:

CCBL32 source-filename.ext (resulting compiled object filename defaults
to CBL.OUT)

(You may use a series of compile switches or define environment
variable CBLFLAGS to contain your compiler switches.)

Recommend using:

CCBL32 -Zds -v -Lo @.lst -o @.obj source-filename.ext

Where "Zds" causes souce & symbolic level debugging, "V" is verbose
listing, "Lo" is output listing (as opposed to terminal output), "@.lst"
is the listing filename (the @ "at" sign is a wildcard for the filename
w/o extension), "o" is object filename, "@.obj" is the object filename
(overrides the default of CBL.OUT). "source-filename.ext" is obvious,
the name of your COBOL source file (NOTE: there are many sample programs
in the "SAMPLE" directory.

3. Running:

The output of the compiler is a portable program object. Portable to
any platform you have a runtime for. Syntax:

WRUN32

(if you compiled without switches and no CBLFLAGS containing switches,
then the default object filename is assumed; otherwise,...)

In Debug mode -

WRUN32 -dle @.err object-filename.ext

Where "dle" means debug (d) mode with a error listing (le), hence
"dle", "@.err" is your runtime error listing (as opposed to on-screen),
and of course the program object name.

Within the Debugger, use "s" for step, "g" for go, "d" for display,
etc.. There is application help within the debugger, plus much of the
debug function is available from the pull-down menus.

---
TIPS:

- Compile debugged programs without the -zds switch and run without the
-dle switch.

- You can have one program call another program using the CALL
"program-name", and pass parameters to the called program with the CALL
USING statement.

- Check our website http://www.acucobol.com/ for lots of information
about our products, as well as additional sample programs.

Best of luck to you learning COBOL...I trust you'll soon learn it to be
a wise decision, if you haven't already. And, ACUCOBOL-GT provides you
with the ability to develope GUI applications using COBOL, without using
external third party API products...you can do it all within COBOL. Any
you can write and compile once, and run on more than 600 supported
platforms, sound familiar? We been doing this for more than eight years
and have an installed user base of over one million users. Cool, huh?

If I can be of any further assistance, please do not hesitate to contact
us at sys··.@acu··l.com .

Sincerely,
Jim Zisch


----------------------------------------------------------
James H. Zisch, Systems Engineer
Acucobol, Inc.                    http://www.acucobol.com/
tel: (888) 767 0670 (in USA)
or:  +1 619 689 7129	          fax: +1 619 689 7251
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
