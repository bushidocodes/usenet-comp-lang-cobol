[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# error...

_4 messages · 4 participants · 1999-03_

---

### error...

- **From:** "cyberon01" <cyberon01@infonie.be>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<920918614.688053@eole>`

```
what does means this statement :
STATISTICS: HIGHEST SEVERITY CODE=I, PROGRAM UNIT=1
?
i have that when i compile with fujitsu cobol 85
```

#### ↳ Re: error...

- **From:** "Donald Tees" <donald@wilmack.com>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c1p4q$7m7$1@news.igs.net>`
- **References:** `<920918614.688053@eole>`

```
It means it compiled with no fatal errors.

cyberon01 wrote in message <920918614.688053@eole>...
>what does means this statement :
>STATISTICS: HIGHEST SEVERITY CODE=I, PROGRAM UNIT=1
…[3 more quoted lines elided]…
>
```

#### ↳ Re: error...

- **From:** Ed.Stevens@nmm.nissan-usa.com
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c1biv$mgt$1@nnrp1.dejanews.com>`
- **References:** `<920918614.688053@eole>`

```
In article <920918614.688053@eole>,
  "cyberon01" <cyberon01@infonie.be> wrote:
> what does means this statement :
> STATISTICS: HIGHEST SEVERITY CODE=I, PROGRAM UNIT=1
…[3 more quoted lines elided]…
>

It means that the "HIGHEST SEVERITY CODE" returned (while compiling the
program) was of severity level "I"

Severity level "I" - "Informational"
Severity level "W" - "Warning"
Severity level "E" - "Error"
Severity level "D" - "Disaster"

Ed Stevens

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: error...

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-Sdk5ZX6FXkfC@Dwight_Miller.iix.com>`
- **References:** `<920918614.688053@eole>`

```
On Mon, 8 Mar 1999 18:45:34, "cyberon01" <cyberon01@infonie.be> wrote:

> what does means this statement :
> STATISTICS: HIGHEST SEVERITY CODE=I, PROGRAM UNIT=1
…[3 more quoted lines elided]…
> 

It means that the highest leve of error in your program is I - 
Informational - you have a clean compile.  The Program Unit=1?  I 
dunno?  Gary?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
