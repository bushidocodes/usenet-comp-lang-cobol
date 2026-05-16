[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# interesting bug

_13 messages · 5 participants · 1999-07 → 1999-08_

---

### interesting bug

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nngcl$n9a$1@news.igs.net>`

```
Found the following under Fujitsu 4.0 today.


    the statement

        PERFORM OPEN-THE-FILE UNTIL
                FILE-STATUS-WORD IS EQUAL TO "00".

        OPEN-THE-FILE.
                OPEN OUTPUT REPORT-FILE.
                IF FILE-STATUS-WORD (is correctable)
                        (fix the error)
                ELSE
                        (sit in loop showing error).

Craps out the *second* time it runs with a "divide by zero!" error. Not the
open statement itself, but the perform. I was able to fix it by changing the
UNTIL to a flag check, and setting the flag in the IF statement of the
OPEN-THE-FILE paragraph, but a divide by zero error on a PERFORM/UNTIL
through me off for about an hour.
```

#### ↳ Re: interesting bug

- **From:** walterm@rose.hp.com (Walter Murray)
- **Date:** 1999-07-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nqgv3$kam$1@ocean.cup.hp.com>`
- **References:** `<7nngcl$n9a$1@news.igs.net>`

```
donald tees (donald@willmack.com) wrote:
: Found the following under Fujitsu 4.0 today.
:     the statement
:         PERFORM OPEN-THE-FILE UNTIL
:                 FILE-STATUS-WORD IS EQUAL TO "00".
:         OPEN-THE-FILE.
:                 OPEN OUTPUT REPORT-FILE.
:                 IF FILE-STATUS-WORD (is correctable)
:                         (fix the error)
:                 ELSE
:                         (sit in loop showing error).

: Craps out the *second* time it runs with a "divide by zero!" error. 
: [snip]

This looks mildly suspicious.  Your PERFORM statement doesn't include
a TEST AFTER phrase, so will not execute OPEN-THE-FILE if 
FILE-STATUS-WORD happens to be 00 initially.  Are you setting
FILE-STATUS-WORD to a non-zero value somewhere in order to force
OPEN-THE-FILE to be executed?

Disclaimer:  I know nothing about Fujitsu COBOL.

Walter Murray
```

##### ↳ ↳ Re: interesting bug

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-07-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ns470$lmt$1@news.igs.net>`
- **References:** `<7nngcl$n9a$1@news.igs.net> <7nqgv3$kam$1@ocean.cup.hp.com>`

```
Yes.

Walter Murray wrote in message <7nqgv3$kam$1@ocean.cup.hp.com>...
>donald tees (donald@willmack.com) wrote:
>: Found the following under Fujitsu 4.0 today.
…[21 more quoted lines elided]…
>Walter Murray
```

###### ↳ ↳ ↳ Re: interesting bug

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<933620429.16048.0.nnrp-06.c1edc1b5@news.demon.co.uk>`
- **References:** `<7nngcl$n9a$1@news.igs.net> <7nqgv3$kam$1@ocean.cup.hp.com> <7ns470$lmt$1@news.igs.net>`

```
Use Micro Focus Cobol, I never have any probs using them.

Simon R Hart
donald tees <donald@willmack.com> wrote in message
news:7ns470$lmt$1@news.igs.net...
> Yes.
>
…[26 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: interesting bug

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37A5EEC9.F51552BB@home.com>`
- **References:** `<7nngcl$n9a$1@news.igs.net> <7nqgv3$kam$1@ocean.cup.hp.com> <7ns470$lmt$1@news.igs.net> <933620429.16048.0.nnrp-06.c1edc1b5@news.demon.co.uk>`

```
Simon R Hart wrote:
> 
> Use Micro Focus Cobol, I never have any probs using them.
> 
Naughty of you Simon. Donald might just start using OO if he did that.
<G>

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: interesting bug

_(reply depth: 5)_

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<933703154.19502.0.nnrp-10.c1edc1b5@news.demon.co.uk>`
- **References:** `<7nngcl$n9a$1@news.igs.net> <7nqgv3$kam$1@ocean.cup.hp.com> <7ns470$lmt$1@news.igs.net> <933620429.16048.0.nnrp-06.c1edc1b5@news.demon.co.uk> <37A5EEC9.F51552BB@home.com>`

```

James J. Gavan <jjgavan@home.com> wrote in message
news:37A5EEC9.F51552BB@home.com...
> Simon R Hart wrote:
> >
…[5 more quoted lines elided]…
> Jimmy, Calgary AB

Why not, hey, Donald could be the second person to get the brass ring in
developing a comercial "real life" OO system ;>)


Simon R Hart
Eaton.
```

###### ↳ ↳ ↳ Re: interesting bug

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7o836g$6t6$1@news.igs.net>`
- **References:** `<7nngcl$n9a$1@news.igs.net> <7nqgv3$kam$1@ocean.cup.hp.com> <7ns470$lmt$1@news.igs.net> <933620429.16048.0.nnrp-06.c1edc1b5@news.demon.co.uk> <37A5EEC9.F51552BB@home.com> <933703154.19502.0.nnrp-10.c1edc1b5@news.demon.co.uk>`

```
You mean I could get to say "oops"?

Simon R Hart wrote in message
<933703154.19502.0.nnrp-10.c1edc1b5@news.demon.co.uk>...
>
>James J. Gavan <jjgavan@home.com> wrote in message
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: interesting bug

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7o81eq$5q4$2@news.igs.net>`
- **References:** `<7nngcl$n9a$1@news.igs.net> <7nqgv3$kam$1@ocean.cup.hp.com> <7ns470$lmt$1@news.igs.net> <933620429.16048.0.nnrp-06.c1edc1b5@news.demon.co.uk>`

```
You cannot have written much code then ...

Simon R Hart wrote in message
<933620429.16048.0.nnrp-06.c1edc1b5@news.demon.co.uk>...
>Use Micro Focus Cobol, I never have any probs using them.
>
…[33 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: interesting bug

_(reply depth: 5)_

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-08-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<933785432.21472.0.nnrp-01.c1edc1b5@news.demon.co.uk>`
- **References:** `<7nngcl$n9a$1@news.igs.net> <7nqgv3$kam$1@ocean.cup.hp.com> <7ns470$lmt$1@news.igs.net> <933620429.16048.0.nnrp-06.c1edc1b5@news.demon.co.uk> <7o81eq$5q4$2@news.igs.net>`

```

donald tees <donald@willmack.com> wrote in message
news:7o81eq$5q4$2@news.igs.net...
> You cannot have written much code then ...

Why??

> Simon R Hart wrote in message
> <933620429.16048.0.nnrp-06.c1edc1b5@news.demon.co.uk>...
…[37 more quoted lines elided]…
>
```

#### ↳ Re: interesting bug

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37A075B5.B5E421E6@home.com>`
- **References:** `<7nngcl$n9a$1@news.igs.net>`

```
donald tees wrote:
> 
> Found the following under Fujitsu 4.0 today.
…[17 more quoted lines elided]…
> through me off for about an hour.

Donald,

I think your example illustrates very well the benefit of using 88s to
determine end-of-routine and making file-status a separate check :-

	set FileNotFinished to true
	perform Open-the-file until FileFinished

	Open-the-File.
	   open output Report-File
	   if file-status <> "00"
              set FileFinished to true
	   else ......
	   End-if

	 ... and as a result of the file-status error do something else
```

##### ↳ ↳ Re: interesting bug

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-07-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nq8hl$f3e$2@news.igs.net>`
- **References:** `<7nngcl$n9a$1@news.igs.net> <37A075B5.B5E421E6@home.com>`

```
Well, I agree, but syntactically the two are the very same ... i.e.-I would
suspect the same bug would crop up.

James J. Gavan wrote in message <37A075B5.B5E421E6@home.com>...
>donald tees wrote:
>>
…[14 more quoted lines elided]…
>> Craps out the *second* time it runs with a "divide by zero!" error. Not
the
>> open statement itself, but the perform. I was able to fix it by changing
the
>> UNTIL to a flag check, and setting the flag in the IF statement of the
>> OPEN-THE-FILE paragraph, but a divide by zero error on a PERFORM/UNTIL
…[17 more quoted lines elided]…
> ... and as a result of the file-status error do something else
```

#### ↳ Re: interesting bug

- **From:** allenmc@my-deja.com
- **Date:** 1999-08-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ocn4e$oso$1@nnrp1.deja.com>`
- **References:** `<7nngcl$n9a$1@news.igs.net>`

```
In article <7nngcl$n9a$1@news.igs.net>,
  "donald tees" <donald@willmack.com> wrote:
> Found the following under Fujitsu 4.0 today.
>
…[12 more quoted lines elided]…
> Craps out the *second* time it runs with a "divide by zero!" error.
Not the
> open statement itself, but the perform. I was able to fix it by
changing the
> UNTIL to a flag check, and setting the flag in the IF statement of the
> OPEN-THE-FILE paragraph, but a divide by zero error on a PERFORM/UNTIL
> through me off for about an hour.
>
>


I'm gonna skip all the digs about the different COBOL's and try to stay
with your point.  I agree with Walter, you're best bet would be to use
a "WITH TEST AFTER" clause in this type of logic.  I typically
incorporate the use of a 88's and declaratives with it.   Here is an
example:


       01  OK-SW    PIC X(01).
           88  OK       VALUE "Y".
           88  FAILURE  VALUE "SPACE".

                  :

       PROCEDURE DIVISION
       DECLARATIVES
       OUTPUT-FILE-ERROR SECTION.
            USE AFTER STANDARD ERROR PROCEDURE ON OUTPUT
       OUTPUT-FILE-ERROR-ROUTINE.
            SET FAILURE TO TRUE.
  ***  GET YOUR EXTENDED FILE STATUS IN THIS AREA.
       END DECLARATIVES.

       PERFORM OPEN-THE-FILE THRU
               OPEN-THE-FILE-EXIT
               WITH TEST AFTER
               UNTIL OK.


   OPEN-THE-FILE.
       SET OK TO TRUE.
       MOVE "00" TO FILE-STATUS.
       OPEN OUTPUT REPORT-FILE.
       IF FAILURE
  ***     DO WHATEVER YOU HAVE TO HERE TO FIX THE ERROR
       END-IF.
   OPEN-THE-FILE-EXIT.
       EXIT.

In this example you can get any extended error code such as RM/COBOL's
errors via C$RERR or the 9/xxx errors in Micro Focus.  I've got
Fujitsu's version 3.0 but havn't had time to see how they get their
extended codes but I hope you have the idea here.


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

##### ↳ ↳ Re: interesting bug

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-08-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37A9EA42.B5E93F4C@home.com>`
- **References:** `<7nngcl$n9a$1@news.igs.net> <7ocn4e$oso$1@nnrp1.deja.com>`

```
allenmc@my-deja.com wrote:
> 
> In article <7nngcl$n9a$1@news.igs.net>,
>   "donald tees" <donald@willmack.com> wrote:
> > Found the following under Fujitsu 4.0 today.

> I'm gonna skip all the digs about the different COBOL's and try to stay
> with your point.  I agree with Walter, you're best bet would be to use
…[33 more quoted lines elided]…
>
Agree with you for 'structured'. That Declaratives bit is about the only
piece of source code that appeared with RM V 2. It works on the system I
wrote back in early '80s and still does the job to-day.

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
