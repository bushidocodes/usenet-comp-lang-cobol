[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL & Unix Envir. Vars.

_4 messages · 4 participants · 1996-01 → 1996-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL & Unix Envir. Vars.

- **From:** "dbma..." <ua-author-1810562@usenetarchives.gap>
- **Date:** 1996-01-31T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4erjbk$n43@news.onramp.net>`

```
I am looking for a way to access Environment vars, eg. those defined by
SETENVR, from inside a MF cobol program. The manuals are very unclear
how to perform this action. Could someone give me an idea/example??

Thanks.
```

#### ↳ Re: MF COBOL & Unix Envir. Vars.

- **From:** "dwayne...." <ua-author-17086750@usenetarchives.gap>
- **Date:** 1996-02-01T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3aa0ef7e48-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4erjbk$n43@news.onramp.net>`
- **References:** `<4erjbk$n43@news.onramp.net>`

```
In article <4erjbk$n.··.@new··p.net>,
dbm··.@onr··p.net (david martin) wrote:
› 
› I am looking for a way to access Environment vars, eg. those defined by 
…[3 more quoted lines elided]…
› Thanks.

Please post to the net... I would be very interested also.

Thanks!


**********************************************************************
Dwayne Williams
Project Director
Georgia Tech Research Institute Work: (404) 894-1458
Atlanta GA 30332 Fax: (404) 894-6211
**********************************************************************

```

##### ↳ ↳ Re: MF COBOL & Unix Envir. Vars.

- **From:** "ken..." <ua-author-17086105@usenetarchives.gap>
- **Date:** 1996-02-01T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3aa0ef7e48-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3aa0ef7e48-p2@usenetarchives.gap>`
- **References:** `<4erjbk$n43@news.onramp.net> <gap-3aa0ef7e48-p2@usenetarchives.gap>`

```
› In article <4erjbk$n.··.@new··p.net>,
›   dbm··.@onr··p.net (david martin) wrote:
…[4 more quoted lines elided]…
›› 

The following program will get & display the value of the HOME
environment variable. For any others, replace HOME with the desired
variable name.

Ken Row

----------

$set rtncode-size(4)
WORKING-STORAGE SECTION.
01 cobdir pic x(100) value spaces.
01 env-name pic x(100) value spaces.

LINKAGE SECTION.
01 namebuf pic x(100).
01 return-code2.
05 return-pointer usage is pointer.
PROCEDURE DIVISION.
START-OF-PROGRAM.
set address of return-code2 to address of return-code.
string "HOME", low-values delimited by size into env-name.
call "cobgetenv" using env-name.
if return-code = 0
display "Something went wrong."
STOP RUN.

set address of namebuf to return-pointer.
string namebuf delimited by low-values into cobdir.
display "The value of $HOME is " cobdir.
stop-run.
```

##### ↳ ↳ Re: MF COBOL & Unix Envir. Vars.

- **From:** "janna wemekamp" <ua-author-17086264@usenetarchives.gap>
- **Date:** 1996-02-04T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3aa0ef7e48-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3aa0ef7e48-p2@usenetarchives.gap>`
- **References:** `<4erjbk$n43@news.onramp.net> <gap-3aa0ef7e48-p2@usenetarchives.gap>`

```
dwa··.@gtr··h.edu (Dwayne Williams) wrote:
› In article <4erjbk$n.··.@new··p.net>,
›   dbm··.@onr··p.net (david martin) wrote:
…[8 more quoted lines elided]…
› 

There's an easy way:

First,
Configuration Section.
Special-Names.
Environment-Value is env-value
Environment-Name is env-name.

Where env-value and env-name are defined as pic x(255), for example,
in working storage.

Then, when you wish to read the value of an environment variable such as
$LOGIN:

display "LOGIN" upon env-name
accept login-name from env-value.

where login-name would be defined as pic x(8) on most Unices.

My thanks to someone who posted this solution some time ago; I've lost the
posting so can't acknowledge by name.



Janna Wemekamp
tol··.@tol··m.au                                  Tel. +61 6 258 8330
TOLDARK PTY. LIMITED                                    Fax. +61 6 258 8183
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
