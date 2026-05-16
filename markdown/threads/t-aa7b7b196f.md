[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF-Cobol function length ()

_7 messages · 5 participants · 2000-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF-Cobol function length ()

- **From:** Manfred Friedrich <mfriedrich@excite.com>
- **Date:** 2000-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3953F957.FCFACA0E@excite.com>`

```
Hello,

I have a question regarding transfer of length
information from a calling Cobol program to a
called C program. Is it possible apply the
MF-Cobol Function length () in the following
form:

CALL "c_program to call" USING
                    PIC-X-VARIABLE
                    FUNCTION LENGTH (PIC-X-VARIABLE)

Is it sure that the length information is submited
in the native integer format of the plattform,
i.e. COMP-5 in MF-Cobol or is it necessary to use
a intermediate variable?

My plattform is DigitalUnix.

Thanks.

Manfred
```

#### ↳ Re: MF-Cobol function length ()

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-06-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8j0tvt$j4d$1@news.igs.net>`
- **References:** `<3953F957.FCFACA0E@excite.com>`

```
You have to put the data in a specific place and format.

Manfred Friedrich wrote in message <3953F957.FCFACA0E@excite.com>...
>Hello,
>
…[19 more quoted lines elided]…
>Manfred
```

#### ↳ Re: MF-Cobol function length ()

- **From:** "Lucas, Todd" <Todd.Lucas@C-Cubed.net>
- **Date:** 2000-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8j5826$vtg$1@news.chatlink.com>`
- **References:** `<3953F957.FCFACA0E@excite.com>`

```
I do alot of VB to Micro Focus Cobol mixed-language programming, and
these are the methods I use.  Not saying that they are the best, but
they have worked for me for the past 5 years with no coding changes.  I
develop on a Windows NT/9.x platform, as well as (used to) an OS/2
platform.

* Define a signed Long Integer (4 bytes):
01  PICX-LENGTH  PIC S9(9) COMP-5.

* Move the length to the long integer:
MOVE LENGTH OF PIC-X-VARIABLE TO PICX-LENGTH

* Call the C program:
CALL "c_program to call" USING
                    PIC-X-VARIABLE
                    PICX-LENGTH

Also, I have always had better luck passing all integer and long numeric
data before string data.  Hope it helps ...

Todd Lucas
E-Mail:  Todd.Lucas@C-Cubed.net
Web:   http://www.c-cubed.net


Manfred Friedrich <mfriedrich@excite.com> wrote in message
news:3953F957.FCFACA0E@excite.com...
> Hello,
>
…[19 more quoted lines elided]…
> Manfred
```

##### ↳ ↳ Re: MF-Cobol function length ()

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39564797.A7F27E6F@home.com>`
- **References:** `<3953F957.FCFACA0E@excite.com> <8j5826$vtg$1@news.chatlink.com>`

```


"Lucas, Todd" wrote:
> 
> I do alot of VB to Micro Focus Cobol mixed-language programming, and
…[18 more quoted lines elided]…
> 
The only caveat on the above is that I think MOVE LENGTH OF.... is Micro
Focus specific; I don't see any reference to it in the draft Standard.

Like you I use MOVE LENGTH OF...., but for source code portability, it
might be better to use the LENGTH FUNCTION.

Jimmy
```

###### ↳ ↳ ↳ Re: MF-Cobol function length ()

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8j5q7c$9jq$1@slb6.atl.mindspring.net>`
- **References:** `<3953F957.FCFACA0E@excite.com> <8j5826$vtg$1@news.chatlink.com> <39564797.A7F27E6F@home.com>`

```
Jimmy - well "yes and no",

It is true that the "LENGTH" special register is a Micro Focus (well
originally IBM) extension - which will *not* be part of the next COBOL
Standard.  *HOWEVER*, the next Standard *will* allow the omission of the
"noise" word FUNCTION before any of the intrinsic function names - IF AND
ONLY IF - you declare in your (new) repository paragraph that you haven't
used them as "user-defined words".

FYI,
  You may also specify certain functions that are used this way - while
others still require the word "function".  You may also "declare"
user-defined functions to be used this way as well.  The word "function"
remains required as the default - but not in all case.

FYI2,
  Of course the use of COMP-5 already takes the program out of being
Standard-conforming in this - or the next Standard.  To  make this "standard
conforming" today, you would need to use "FUNCTION LENGTH" *and* USAGE COMP
with the COMP-5 (as I recall) directive to turn COMP into COMP-5.
```

###### ↳ ↳ ↳ Re: MF-Cobol function length ()

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3956939A.85FB5153@home.com>`
- **References:** `<3953F957.FCFACA0E@excite.com> <8j5826$vtg$1@news.chatlink.com> <39564797.A7F27E6F@home.com> <8j5q7c$9jq$1@slb6.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> Jimmy - well "yes and no",
…[18 more quoted lines elided]…
> with the COMP-5 (as I recall) directive to turn COMP into COMP-5.
 
Thanks for the clarifications Bill - but I think the solutions you offer
make the whole thing even more bloody complicated ! (Says to himself,
"What about the Comp-5 which is used EXTENSIVELY when invoking Micro
Focus OO classes ??????).

I just wonder - can we ever get to a truly portable COBOL ? The short
answer seems to be "Yes" if you restrict yourself to '68/'74 features.
Currently going back to DOS and changing RM/COBOL programs (V2) which
use ANSI '74 - believe me, it's a real pain in the butt without the
features I now have in M/F COBOL '97++.

Jimmy
```

###### ↳ ↳ ↳ Re: MF-Cobol function length ()

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8j6jcs$eep$1@slb2.atl.mindspring.net>`
- **References:** `<3953F957.FCFACA0E@excite.com> <8j5826$vtg$1@news.chatlink.com> <39564797.A7F27E6F@home.com> <8j5q7c$9jq$1@slb6.atl.mindspring.net> <3956939A.85FB5153@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message
 <snip>
>
> Thanks for the clarifications Bill - but I think the solutions you offer
…[3 more quoted lines elided]…
>

If you want to use "ANSI/ISO conforming binary fields" that are in intel
"little-endian" format, then define them with COMP (not COMP-5) as the
usage - and use the COMP-5 (I think) Micro Focus directive.  The only problem
that you would have is if you ALSO are getting some fields in "big-endian"
format (say from an IBM mainframe) into the same application at the same
time.  There is a "solution" to even that problem, but it is a "little
obscure" and I won't go into it, unless someone really cares.

My guess is that if you compile your existing COBOL code with the FLAGSTD
directive you would be AMAZED at how much "non-standard" code you have.  This
is true for NON-OO code, much less OO code - and true for any implementor who
is FIPS compiliant (and includes a "FIPS flagging" mechanism).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
