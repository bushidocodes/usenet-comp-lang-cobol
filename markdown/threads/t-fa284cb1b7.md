[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# String Search in COBOL?

_6 messages · 5 participants · 2001-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### String Search in COBOL?

- **From:** "Fritz Sonnichsen" <sonnichs@berkshire.net>
- **Date:** 2001-12-15T21:29:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BCTS7.108382$lV4.16918958@e420r-atl1.usenetserver.com>`

```
It has been about 20 years since I wrote a lot of COBOL code, and I wondered
is someone can help here. I am using an IBM VSII compiler to write some
simple code, and I want to read a record, and make a conditional decision
based upon whether or not the record-buffer contains a certain substring.
  I have successfully written the code using 3  loops and 3 indexes, one
pointing to the character in the substring, one pointing to the character in
the record and one pointing to a starting point in the record, which 'walks'
across the whole record to scan it.
   Of course this works fine, but it seems somewhat verbose and inefficient.
I looked at the INSPECT and SEARCH commands, etc, but didn't really see any
simpler way.
    Did I overdo it here or is this the common acceptable technique for this
simple operation?
```

#### ↳ Re: String Search in COBOL?

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-12-16T15:59:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C1CC4D0.936164E8@Azonic.co.nz>`
- **References:** `<BCTS7.108382$lV4.16918958@e420r-atl1.usenetserver.com>`

```
Fritz Sonnichsen wrote:
> 
> It has been about 20 years since I wrote a lot of COBOL code, and I wondered
…[9 more quoted lines elided]…
> simpler way.


	MOVE ZERO      TO Substring-Count
        INSPECT Data-Record
            TALLYING Substring-Count FOR ALL "XYZ"
```

##### ↳ ↳ Re: String Search in COBOL?

- **From:** "ThatGuy" <thatguy@thatguy.net>
- **Date:** 2001-12-16T13:34:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xp1T7.17956$Z24.3571633@typhoon.jacksonville.mediaone.net>`
- **References:** `<BCTS7.108382$lV4.16918958@e420r-atl1.usenetserver.com> <3C1CC4D0.936164E8@Azonic.co.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3C1CC4D0.936164E8@Azonic.co.nz...
> Fritz Sonnichsen wrote:
> >
> > It has been about 20 years since I wrote a lot of COBOL code, and I
wondered
> > is someone can help here. I am using an IBM VSII compiler to write some
> > simple code, and I want to read a record, and make a conditional
decision
> > based upon whether or not the record-buffer contains a certain
substring.
> >   I have successfully written the code using 3  loops and 3 indexes, one
> > pointing to the character in the substring, one pointing to the
character in
> > the record and one pointing to a starting point in the record, which
'walks'
> > across the whole record to scan it.
> >    Of course this works fine, but it seems somewhat verbose and
inefficient.
> > I looked at the INSPECT and SEARCH commands, etc, but didn't really see
any
> > simpler way.
>
…[3 more quoted lines elided]…
>             TALLYING Substring-Count FOR ALL "XYZ"

Or you could try this:

MOVE SPACES TO WS-VAR-1 WS-VAR-2.
UNSTRING (Record)
  DELIMITED BY (Substring)
  INTO
    WS-VAR-1
    WS-VAR-2.

IF WS-VAR-2 NOT = SPACES  (You could 88-level this if you prefer)
  DO WHATEVER.

This only works as long as the substring you are searching for is not the
last part of the record searched.  It will also parse the record for you
which comes in handy in certain situations (splitting names separated by ' &
',  ' AND ', etc.)
```

###### ↳ ↳ ↳ Re: String Search in COBOL?

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-12-17T04:06:39+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c1dbef5_9@Usenet.com>`
- **References:** `<BCTS7.108382$lV4.16918958@e420r-atl1.usenetserver.com> <3C1CC4D0.936164E8@Azonic.co.nz> <xp1T7.17956$Z24.3571633@typhoon.jacksonville.mediaone.net>`

```
ThatGuy <thatguy@thatguy.net> wrote in message
news:xp1T7.17956$Z24.3571633@typhoon.jacksonville.mediaone.net...
>
> "Richard Plinston" <riplin@Azonic.co.nz> wrote in message
…[20 more quoted lines elided]…
> which comes in handy in certain situations (splitting names separated by '
&
> ',  ' AND ', etc.)
>
>

There is no comparison between doing this and the code Richard submitted.
(Of course, I WOULD say that because my code would have been identical to
Richard's...<G>).

If all you want to know is whether the record contains a given substring,
INSPECT is more appropriate than UNSTRING.

Why?

Because the UNSTRING  incurs the additional overhead of moving every
character to storage, whereas the INSPECT just looks... (and optionally
counts).

Note that BOTH these solutions will keep on scanning even after the target
string has been found.

To avoid this you COULD code:

MOVE ZERO      TO Substring-Count
         INSPECT Data-Record
            TALLYING Substring-Count FOR CHARACTERS
                                                          BEFORE "XYZ"

The disadvantage here is that you must then check the count against the
known length of the buffer in order to determine whether the target was
found...

IF Substring-Count = Buffer-Length   *> we have scanned the whole buffer
     SET NOT-found to TRUE
ELSE
     SET found-it to TRUE
END-IF

If the sub-string occurs consistently in an "early" part of the record, this
arguably less elegant solution would certainly be more efficient than either
of the above.

But I still wouldn't do it (It causes an "add" for every character looked at
before the target...this is nearly as bad as the "move" incurred with
UNSTRING, but it stops when the target is found)

Pete.




 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

##### ↳ ↳ Re: String Search in COBOL?

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-12-17T03:41:21+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c1cb62d$1_7@Usenet.com>`
- **References:** `<BCTS7.108382$lV4.16918958@e420r-atl1.usenetserver.com> <3C1CC4D0.936164E8@Azonic.co.nz>`

```

Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3C1CC4D0.936164E8@Azonic.co.nz...
>
> MOVE ZERO      TO Substring-Count
>         INSPECT Data-Record
>             TALLYING Substring-Count FOR ALL "XYZ"

Absolutely. (Nothing missed here...<G>).

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: String Search in COBOL?

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-12-17T15:47:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9vl3tp$l6q$1@peabody.colorado.edu>`
- **References:** `<BCTS7.108382$lV4.16918958@e420r-atl1.usenetserver.com>`

```

On 15-Dec-2001, "Fritz Sonnichsen" <sonnichs@berkshire.net> wrote:

> It has been about 20 years since I wrote a lot of COBOL code, and I
> wondered
…[16 more quoted lines elided]…
> simple operation?

If you don't want to use the INSPECT command, you might want to use
reference modification in your loop.  Since you last coded,  reference
modification has made this job easier:

A few new features of the language are illustrated below, but you should be
able to infer how they work:

COMPUTE STRING-LENGTH = FUNCTION LENGTH (MY-STRING)
COMPUTE START-POSITION = BUFFER-LENGTH - STRING-LENGTH.
PERFORM VARYING START-POINT FROM START-POSITION BY -1
                      UNTIL START-POINT < 1
                           OR SW-FOUND-ONE
       COMPUTE END-POSITION = START-POSITION + STRING-LENGTH
       IF MY-BUFFER (START-POSITION:END-POSITION) = MY-STRING
              SET SW-FOUND-ONE TO TRUE
       END-IF
END-PERFORM.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
