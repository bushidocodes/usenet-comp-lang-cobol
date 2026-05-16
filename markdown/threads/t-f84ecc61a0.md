[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# another new problem

_8 messages · 8 participants · 2001-04_

---

### another new problem

- **From:** "Onder OZ" <kucuk_calik@yahoo.com>
- **Date:** 2001-04-18T09:55:26+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9bja5d$b041@baran22.ttnet.net.tr>`

```
Hi,
After solving prior issues, i came to another problem that i couldn't solve.

LINKAGE SECTION.
01 PAKET-REC.
   02 A PIC X.
   02 B PIC X.
01 PAKFIR-REC.
   02 C PIC X.
   02 D PIC X.

PROCEDURE DIVISION USING PAKET-REC PAKFIR-REC.
PROC-START.
        DISPLAY A.
        DISPLAY B.
        END PROGRAM.

And the compilation generates following errors:

chs.cbl 107: JMN3399I-S  'A' OF DISPLAY STATEMENT MUST BE DEFINED IN
WORKING-STORAGE SECTION.
chs.cbl 107: JMN3399I-S  'B' OF DISPLAY STATEMENT MUST BE DEFINED IN
WORKING-STORAGE SECTION.


How can i solve this???

Best regards & TY
Onder OZ
```

#### ↳ Re: another new problem

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-04-19T06:54:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ADEE013.451EF7D@brazee.net>`
- **References:** `<9bja5d$b041@baran22.ttnet.net.tr>`

```
Onder OZ wrote:

> Hi,
> After solving prior issues, i came to another problem that i couldn't solve.
…[22 more quoted lines elided]…
> How can i solve this???

Interesting.  I wonder if that is particular to your compiler - I don't know if
I have ever tried to display something from the LINKAGE SECTION, I would guess
yes, but I don't know.

So the compiler is telling you that what it needs to display has to be in
WORKING-STORAGE, you have it in LINKAGE.   I would believe the compiler and copy
it to WORKING-STORAGE before displaying.
```

#### ↳ Re: another new problem

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2001-04-19T09:07:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fiCD6.4102$rk3.167897@news1.atl>`
- **References:** `<9bja5d$b041@baran22.ttnet.net.tr>`

```
"Onder OZ" <kucuk_calik@yahoo.com> wrote:
> Hi,
> After solving prior issues, i came to another problem that i couldn't solve.
…[20 more quoted lines elided]…
> WORKING-STORAGE SECTION.

1. Check the CALL statement in the calling program to be sure the
   arguments are being passed for PAKET-REC and PAKFIR-REC, and that
   they are the correct size and type.

2. Check for a qualification problem in the called program.

3. Your compiler may simply not be able to DISPLAY from the Linkage
   Section, though that sounds peculiar.  I regularly use items in
   the Linkage Section for screen DISPLAY/ACCEPT in Net Express.
```

#### ↳ Re: another new problem

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-04-19T14:08:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gjCD6.692508$JT5.18431302@news20.bellglobal.com>`
- **References:** `<9bja5d$b041@baran22.ttnet.net.tr>`

```

"Onder OZ" <kucuk_calik@yahoo.com> wrote in message
news:9bja5d$b041@baran22.ttnet.net.tr...
> Hi,
> After solving prior issues, i came to another problem that i couldn't
solve.

WORKING-STORAGE SECTION.
       02 E PIC X.
       02 F PIC X.

> LINKAGE SECTION.
> 01 PAKET-REC.
…[7 more quoted lines elided]…
> PROC-START.
        MOVE A TO E.
        DISPLAY E.
        MOVE B TO F.
        DISPLAY F.
*******>         DISPLAY A.
*******>         DISPLAY B.
>         END PROGRAM.
>
> And the compilation generates following errors:
>

It tells you what to do.  You just have to read it.

> chs.cbl 107: JMN3399I-S  'A' OF DISPLAY STATEMENT MUST BE DEFINED IN
> WORKING-STORAGE SECTION.
…[10 more quoted lines elided]…
>
```

#### ↳ Re: another new problem

- **From:** "mikman" <mikman@home.com>
- **Date:** 2001-04-20T02:28:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q9ND6.19939$L7.169553@news1.sshe1.sk.home.com>`
- **References:** `<9bja5d$b041@baran22.ttnet.net.tr>`

```
so why not just define to new variables in the workign storage and move A
and B to those and display those?

Mike

"Onder OZ" <kucuk_calik@yahoo.com> wrote in message
news:9bja5d$b041@baran22.ttnet.net.tr...
> Hi,
> After solving prior issues, i came to another problem that i couldn't
solve.
>
> LINKAGE SECTION.
…[27 more quoted lines elided]…
>
```

##### ↳ ↳ Re: another new problem

- **From:** John H Sleight Jr <John_member@newsranger.com>
- **Date:** 2001-04-20T04:16:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EKOD6.3861$D4.385829@www.newsranger.com>`
- **References:** `<9bja5d$b041@baran22.ttnet.net.tr> <q9ND6.19939$L7.169553@news1.sshe1.sk.home.com>`

```
Hi,

In a mainframe environment, if you're accepting parm info from the exec JCL, you
need a parm len field - pic s9(004) comp. Also, it's better to code the LS:

01  lk-parm-info.
05  lk-parm-len pic     s9(004) comp.
05  lk-paket-rec.
10  lk-a        pic  x(001). 
10  lk-b        pic  x(001). 

05  lk-pakfir-rec.
10  lk-c        pic  x(001). 
10  lk-d        pic  x(001). 


In article <q9ND6.19939$L7.169553@news1.sshe1.sk.home.com>, mikman says...
>
>so why not just define to new variables in the workign storage and move A
…[40 more quoted lines elided]…
>
```

#### ↳ Re: another new problem

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-04-20T06:53:05+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ADFCEC1.AF5B8490@Azonic.co.nz>`
- **References:** `<9bja5d$b041@baran22.ttnet.net.tr>`

```
Onder OZ wrote:
> 
> Hi,
…[14 more quoted lines elided]…
>         END PROGRAM.
 
Ignoring your 'errors':

This should be a CALLed routine (it will fail if it is tun stand
alone).  What do you expect to happen after the displays ?  What do you
expect 'END PROGRAM' to do ?  What does the manual say that it does ?
```

#### ↳ Re: another new problem

- **From:** awkisall <awkisall@qwest.net>
- **Date:** 2001-04-21T00:20:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AE134A9.FF2C7815@qwest.net>`
- **References:** `<9bja5d$b041@baran22.ttnet.net.tr>`

```
Your compiler was unusually specific and to the point.

Move A to WS-DISPLAY-A
Move B to WS-DISPLAY-B

DISPLAY WS-DISPLAY-A
DISPLAY WS-DISPLAY-B.

predicated upon Working-Storage fields set up according to the properties of A
and B
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
