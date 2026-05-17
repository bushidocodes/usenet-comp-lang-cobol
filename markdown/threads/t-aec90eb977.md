[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Trimming Fields

_12 messages · 10 participants · 1999-06_

---

### Trimming Fields

- **From:** elmo_lover13@hotmail.com (Martina Dick)
- **Date:** 1999-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r1493.1763$S7.880732@WReNphoon3>`

```
Does anybody know how to trim fields?

I've to transfer name details and need to lose the spaces between first name
and surname.

The first name is a field of 15 characters and the surname is 20 characters.
I need to make the new field be a concatenation of both with extra spaces
inbetween..

Example
First Name 'James          '
Surname 'Brown                    '

New Field 'James Brown'

Thanks!



   -**** Posted from RemarQ, http://www.remarq.com/?a ****-
 Search and Read Usenet Discussions in your Browser - FREE -
```

#### ↳ Re: Trimming Fields

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3Wi93.13277$hh1.3814@news1.mia>`
- **References:** `<r1493.1763$S7.880732@WReNphoon3>`

```
String Name-1 delimited by SPACES
           ' ' delimited by SIZE
           Name-2 delimited by SPACES
into FULL-NAME.

Martina Dick wrote in message ...
>Does anybody know how to trim fields?
>
>I've to transfer name details and need to lose the spaces between first
name
>and surname.
>
>The first name is a field of 15 characters and the surname is 20
characters.
>I need to make the new field be a concatenation of both with extra spaces
>inbetween..
…[12 more quoted lines elided]…
> Search and Read Usenet Discussions in your Browser - FREE -
```

#### ↳ Re: Trimming Fields

- **From:** "Jerry Peacock" <bismail@bisusa.com>
- **Date:** 1999-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mgj93.353$7G6.113431@typhoon01.swbell.net>`
- **References:** `<r1493.1763$S7.880732@WReNphoon3>`

```

Martina Dick <elmo_lover13@hotmail.com> wrote in message
news:r1493.1763$S7.880732@WReNphoon3...

I like:

MOVE SPACES TO NAMES.
UNSTRING FIRST-NAME DELIMITED ALL ' ' INTO
     NAME(1)
     NAME(2)
     NAME(3)
     NAME(4) etc to as many given-names as is possible, then

STRING NAME(1) DELIMITED SPACE
     ' ' DELIMITED SIZE
     NAME(2) DELIMITED ' '
    ' ' DELIMITED SIZE
     etc
     LAST-NAME DELIMITED SIZE INTO FINAL-OUTPUT.

P.S.
Glad to see you're doing your homework.
```

#### ↳ Re: Trimming Fields

- **From:** Rolf Klemenz <rolf.klemenz@ubs.com>
- **Date:** 1999-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3764D3C1.2AEB9EFC@ubs.com>`
- **References:** `<r1493.1763$S7.880732@WReNphoon3>`

```
Hi

Try STRING  NAME SURNAME 
	    DELIMITED BY ' ' 
 	    INTO NEWFIELD

Not shure, but should work.

Rolf

Martina Dick wrote:
> 
> Does anybody know how to trim fields?
…[19 more quoted lines elided]…
>  Search and Read Usenet Discussions in your Browser - FREE -
```

##### ↳ ↳ Re: Trimming Fields

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3764EB93.2AD2EC40@zip.com.au>`
- **References:** `<r1493.1763$S7.880732@WReNphoon3> <3764D3C1.2AEB9EFC@ubs.com>`

```
Rolf Klemenz wrote:
> 
> Hi
> 
> Try STRING  first-NAME 
                 delimited by '  '
	      SURNAME
>             DELIMITED BY '  '
>             INTO NEWFIELD
> 

Always use two spaces as there is probably more than a single
name.  It will fail sometimes if the user enters two spaces
between names but is a good easy solution.

For a thorough job consider unstring into multiple character
arrays pulling the length of each field into a number variable. 
You can then peice together as many names as you have got without
any errors and guarantee a single space between every word.

	STRING word(1)(1:len-1) delimited by size
               ' ' delimited by size
               word(2) (1:len-2) delimited by size
               ......

Happy RTFM
Ken
```

##### ↳ ↳ Re: Trimming Fields

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7k2tf6$nt8$1@nnrp1.deja.com>`
- **References:** `<r1493.1763$S7.880732@WReNphoon3> <3764D3C1.2AEB9EFC@ubs.com>`

```
An what about 'Jean Francis de la Plata' or 'Peter J. Brown Miller'.
Just 'Jean de' or 'Peter Brown'?
I'd search from the right to the left until first non-blank character:

PERFORM VARYING WS-IND1 FROM 20 BY -1 UNTIL
   SURNAME(WS-IND1:1) NOT = SPACES OR WS-IND1 = ZERO
END-PERFORM
...
STRING SURNAME(1:WS-IND1) DELIMITED BY SIZE,
       NAME(1:WS-IND2)    DELIMITED BY SIZE
  INTO FULL-NAME
END-STRING
...

(Left some details apart, don't want to make ALL of your homework ;-)

In article <3764D3C1.2AEB9EFC@ubs.com>,
  rolf.klemenz@ubs.com wrote:
> Hi
>
…[12 more quoted lines elided]…
> > I've to transfer name details and need to lose the spaces between
first name
> > and surname.
> >
> > The first name is a field of 15 characters and the surname is 20
characters.
> > I need to make the new field be a concatenation of both with extra
spaces
> > inbetween..
> >
…[12 more quoted lines elided]…
>
```

#### ↳ Re: Trimming Fields

- **From:** docdwarf@clark.net ()
- **Date:** 1999-06-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Kb893.670$S2.41968@iad-read.news.verio.net>`
- **References:** `<r1493.1763$S7.880732@WReNphoon3>`

```
In article <r1493.1763$S7.880732@WReNphoon3>,
Martina Dick <elmo_lover13@hotmail.com> wrote:
>Does anybody know how to trim fields?
>
>I've to transfer name details and need to lose the spaces between first name
>and surname.

Please do your own homework.

DD
```

#### ↳ Re: Trimming Fields

- **From:** Alex Romaniuk <ales.romaniuk@zag.si>
- **Date:** 1999-06-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37666339.1E66@zag.si>`
- **References:** `<r1493.1763$S7.880732@WReNphoon3>`

```
Martina Dick wrote:
> 
> Does anybody know how to trim fields?
…[19 more quoted lines elided]…
>  Search and Read Usenet Discussions in your Browser - FREE -
Check my HP
```

#### ↳ Re: Trimming Fields

- **From:** "Jonathan Robert" <jroberts@globalserve.net>
- **Date:** 1999-06-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37666bf2$0$20691@fountain.mindlink.net>`
- **References:** `<r1493.1763$S7.880732@WReNphoon3>`

```
This bit of code takes f1 "James", f2 "Smith"
and makes it into "Smith, James".
Kinda similiar to what you want.

           Initialize Xx Yy Zz.
           Perform Test After Varying Xx from 1 By 1 Until Xx = 15
                   If Init-Lname (Xx:) = Space
                      Add 1 To Yy
                   End-If
           End-Perform
           Compute Zz = 15 - Yy
           Move Init-Lname (1:Zz) To Ws-Name(1:)
           Add 1 To Zz
           Move "," To Ws-Name(Zz:)
           Add 2 To Zz.
           Move Init-Fname To Ws-Name(Zz:).
           Move Ws-Name    To Main-EF-43-Value.
           Display Main-Ef-43-Screen.

Regards.

RBA

Martina Dick <elmo_lover13@hotmail.com> wrote in message
news:r1493.1763$S7.880732@WReNphoon3...
> Does anybody know how to trim fields?
>
> I've to transfer name details and need to lose the spaces between first
name
> and surname.
>
> The first name is a field of 15 characters and the surname is 20
characters.
> I need to make the new field be a concatenation of both with extra spaces
> inbetween..
…[12 more quoted lines elided]…
>  Search and Read Usenet Discussions in your Browser - FREE -
```

#### ↳ Re: Trimming Fields

- **From:** Bill Thompson <wthompson@my-deja.com>
- **Date:** 1999-06-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7k61od$rvg$1@nnrp1.deja.com>`
- **References:** `<r1493.1763$S7.880732@WReNphoon3>`

```
Nobody has hit on the simple compress-in-place perform.

Redefine the data area as an indexed array and scan the array moving
each non-blank byte foward as needed (after encountering the first blank
byte).

Great for relief from "gas" pressure...(grin)...

In article <r1493.1763$S7.880732@WReNphoon3>,
  elmo_lover13@hotmail.com (Martina Dick) wrote:
> Does anybody know how to trim fields?
>
> I've to transfer name details and need to lose the spaces between
first name
> and surname.
>
> The first name is a field of 15 characters and the surname is 20
characters.
> I need to make the new field be a concatenation of both with extra
spaces
> inbetween..
>
…[10 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: Trimming Fields

- **From:** elmo_lover13@hotmail.com (Martina Dick)
- **Date:** 1999-06-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ZJ93.2195$S7.1157363@WReNphoon3>`
- **References:** `<7k61od$rvg$1@nnrp1.deja.com> <r1493.1763$S7.880732@WReNphoon3>`

```
Thanks everyone -  I got this to work.

Martina



   -**** Posted from RemarQ, http://www.remarq.com/?a ****-
 Search and Read Usenet Discussions in your Browser - FREE -
```

#### ↳ Re: Trimming Fields

- **From:** elmo_lover13@hotmail.com (Martina Dick)
- **Date:** 1999-06-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eRP93.472$e9.183860@WReNphoon3>`
- **References:** `<7k61od$rvg$1@nnrp1.deja.com> <r1493.1763$S7.880732@WReNphoon3>`

```
Thanks Everyone.
I got it to work.

Martina



   -**** Posted from RemarQ, http://www.remarq.com/?a ****-
 Search and Read Usenet Discussions in your Browser - FREE -
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
