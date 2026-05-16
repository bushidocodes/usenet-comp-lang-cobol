[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CALL X ON OVERFLOW

_6 messages · 4 participants · 2000-01_

---

### CALL X ON OVERFLOW

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387E23A1.5C6AD0A7@NOSPAMwebaccess.net>`

```
Is the only difference between

CALL 'MYPROG' USING MYFIELDS
    ON OVERFLOW  PERFORM MYROUTINE
END-CALL
and
CALL 'MYPROG' USING MYFIELDS
    ON EXCEPTION  PERFORM MYROUTINE
END-CALL

that the second call can have a NOT ON EXCEPTION ??

If so, why?
```

#### ↳ Re: CALL X ON OVERFLOW

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85l9v4$o5m$1@nntp4.atl.mindspring.net>`
- **References:** `<387E23A1.5C6AD0A7@NOSPAMwebaccess.net>`

```
There is a "NOT ON EXCEPTION" phrase - there is not a "NOT ON OVERFLOW"
phrase.  Furthermore, "ON OVERFLOW" is being made "archaic" in the next
Standard.

As for whether or not there is any difference between "ON OVERFLOW" and "ON
EXCEPTION" - this depends on your specific COBOL.  The reason that the '85
Standard "added" the "<not> ON EXCEPTION" was that the rules for when an "ON
OVERFLOW" were pretty "obscure" and not all vendors treated it the same.  In
you case, Howard, as I recall you are an "OS/390" type person.  I believe
that IBM treats the two as identical (i.e. the same things that cause an "ON
EXCEPTION" also cause an "ON OVERFLOW" and vice versa.  However, this isn't
true with every implementation.

The bottom-line: is that you (everyone) SHOULD be moving to "ON EXCEPTION" -
and reading your manual on exactly what can cause this.  However, this
PROBABLY isn't a change that will actually change run-time behavior.

Does this answer the question?
```

##### ↳ ↳ Re: CALL X ON OVERFLOW

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387E5968.6750A6FD@NOSPAMwebaccess.net>`
- **References:** `<387E23A1.5C6AD0A7@NOSPAMwebaccess.net> <85l9v4$o5m$1@nntp4.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 

> The bottom-line: is that you (everyone) SHOULD be moving to "ON EXCEPTION" -
> and reading your manual on exactly what can cause this.  However, this
…[3 more quoted lines elided]…
> 

Yep.

Thanks
```

##### ↳ ↳ Re: CALL X ON OVERFLOW

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000113224816.12140.00000193@ng-cr1.aol.com>`
- **References:** `<85l9v4$o5m$1@nntp4.atl.mindspring.net>`

```
Bill covered it mostly, yet let me add two very esoteric specifics (which
probably do not matter).

ON OVERFLOW can be made to behave differently under CMPR2 versus NOCMPR2. You
can not make a semantic difference for the newer ON EXCEPTION clause with the
old regression parm.

There is one other twist, and this is strange (all these comments apply to IBM
mainframe).  A _NOT_ ON EXCEPTION clause will be ignored in the absence of an
ON EXCEPTION clause!

The presence of an ON EXCEPTION clause will active the _NOT_ ON EXCEPTION
clause; the ON OVERFLOW clause will probably not do that. :-)

So if you are adding a _NOT_ clause to an old program with an ON OVERFLOW,
change the error dection to ON EXCEPTION.

I would expect diagnostics to motivate this anyway.

In a nutshell, the two clauses ON OVERFLOW and ON EXCEPTION are semantically
identical in that they both behave identically in the unusual condition in
which they behave at all. But they have a syntactic difference, in that a
successful CALL will not invoke _NOT_ ON EXCEPTION if it is only paired
syntactically with ON OVERFLOW.

I think that means, when you see this code, change the 'OVERFLOW' to
'EXCEPTION' (be careful, though, there are other OVERFLOW keywords in COBOL
(the STRING verb :-) ).

Best Wishes,

Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: CALL X ON OVERFLOW

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85m96c$rcb$1@nntp2.atl.mindspring.net>`
- **References:** `<85l9v4$o5m$1@nntp4.atl.mindspring.net> <20000113224816.12140.00000193@ng-cr1.aol.com>`

```
Robert,
  Are you saying that some release of IBM mainframe COBOL accepts (as valid
syntax - no error message):

    CALL ABC
         On overflow
              Display "1"
         Not On Exception
               Display "2"
            .

That SHOULD get a compiler error (with IBM COBOL - or any other compiler that
I know of) - but I don't have easy access to IBM COBOL for OS/390 & VM to
test it out.
```

###### ↳ ↳ ↳ Re: CALL X ON OVERFLOW

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6yKf4.1293$Lm3.13589@dfiatx1-snr1.gtei.net>`
- **References:** `<85l9v4$o5m$1@nntp4.atl.mindspring.net> <20000113224816.12140.00000193@ng-cr1.aol.com>`

```
RKRayhawk wrote in message <20000113224816.12140.00000193@ng-cr1.aol.com>...
>Bill covered it mostly, yet let me add two very esoteric specifics (which
>probably do not matter).
>
>There is one other twist, and this is strange (all these comments apply to
IBM
>mainframe).  A _NOT_ ON EXCEPTION clause will be ignored in the absence of
an
>ON EXCEPTION clause!


Does the code after NOT ON EXCEPTION execute? It should, as if there _is_ an
exception, with no ON EXCEPTION clause your program is no longer running
anyway (806 (?) abend).

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
