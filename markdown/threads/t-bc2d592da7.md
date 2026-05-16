[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# help centering string1 into string2

_9 messages · 5 participants · 2000-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### help centering string1 into string2

- **From:** goble@gtech (David. E. Goble)
- **Date:** 2000-11-25T01:23:30+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3a1f1334.22166110@news.adelaide.on.net>`

```
Hi all;

I have screen field display-action Pic x(80).

how can I move the text field action Pic x(?), so that action is
centered inside display-action.

ie display-action [bbbbbbbb]  blanks
               action [ xxxx ]
                result [bbxxxxbb]

I know I need some way to find the length of each string

I tried 

	function length display-action to lenB
	function length action to lenA
But I think my syntax is wrong.

I then 
	compute center=(lenB - lenA) / 2

How do I then position action into display-action.

I thought of something like

string display-action(1:center)  delimited by size
         action delimited by size
into display-action.

But this might be wrong too.

Can anyone point me in the right direction. 

I am using microfocus personal cobol.
--Regards       David. E. Goble
             goble [AT] kin.net.au
          http://www.kin.net.au/goble
Po Box 648 Kingscote, Kangaroo Island, SA 5223
```

#### ↳ Re: help centering string1 into string2

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-11-24T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8vn7i00q01@enews3.newsguy.com>`
- **References:** `<3a1f1334.22166110@news.adelaide.on.net>`

```
Warning: untested code ahead...

ENVIRONMENT DIVISION.
DATA DIVISION.
WORKING-STORAGE SECTION.

01  FILLER.
    05  DISPLAY-ACTION    PIC X(80).
    05  FILLER  REDEFINES DISPLAY-ACTION.
        10  DISPLAY-ACTION-ELE PIC X(1) OCCURS 80.
    05  HOLD-ACTION       PIC X(80).
    05  FILLER  REDEFINES HOLD-ACTION.
        10  HOLD-ACTION-ELE    PIC X(1) OCCURS 80.

01  FILLER.
    05  TBL-SUB           PIC S9(4) COMP.
    05  ACTION-SUB        PIC S9(4) COMP.
    05  LIT-COMP-1        PIC S9(1) COMP-3 VALUE +1.
    05  LIT-COMP-2        PIC S9(1) COMP-3 VALUE +2.
    05  LIT-COMP-80       PIC S9(3) COMP-3 VALUE +80.
    05  HOLD-LENGTH       PIC S9(3) COMP-3.
    05  HOLD-OFFSET       PIC S9(3) COMP-3.

01 FILLER.
    05  FILLER            PIC X(1).
        88  LENGTH-FOUND            VALUE 'Y'.
        88  NOT-LENGTH-FOUND        VALUE 'N'.


PROCEDURE DIVISION.
    MOVE <default-values> TO DISPLAY-ACTION.
    MOVE <action>         TO HOLD-ACTION.
    SET NOT-LENGTH-FOUND  TO TRUE.
    MOVE LIT-COMP-80      TO TBL-SUB.
    PERFORM UNTIL ( ( TBL-SUB < LIT-COMP-1 )
               OR   ( LENGTH-FOUND ) )
       IF ( HOLD-ACTION-ELE ( TBL-SUB ) =
                             SPACE OR LOW-VALUE )
           SUBTRACT LIT-COMP-1 FROM TBL-SUB
       ELSE
           SET LENGTH-FOUND TO TRUE
           MOVE TBL-SUB TO HOLD-LENGTH
       END-IF
    END-PERFORM.
    IF ( LENGTH-FOUND )
       MOVE LIT-COMP-80      TO HOLD-OFFSET
       SUBTRACT HOLD-LENGTH  FROM HOLD-OFFSET
       DIVIDE LIT-COMP-2     INTO HOLD-OFFSET
       MOVE LIT-COMP-1       TO TBL-SUB
                                ACTION-SUB
       PERFORM HOLD-OFFSET TIMES
          ADD LIT-COMP-1 TO ACTION-SUB
       END-PERFORM
       PERFORM HOLD-LENGTH TIMES
          MOVE HOLD-ACTION-ELE ( TBL-SUB )
                     TO DISPLAY-ACTION-ELE ( ACTION-SUB )
          ADD LIT-COMP-1   TO TBL-SUB
                              ACTION-SUB
       END-PERFORM
    END-IF.


That should do it.

Jeff


----------
In article <3a1f1334.22166110@news.adelaide.on.net>, goble@gtech (David. E.
Goble) wrote:


> Hi all;
>
…[36 more quoted lines elided]…
> Po Box 648 Kingscote, Kangaroo Island, SA 5223
```

#### ↳ Re: help centering string1 into string2

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2000-11-26T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8vqtuf$5bcvq$1@ID-39920.news.dfncis.de>`
- **References:** `<3a1f1334.22166110@news.adelaide.on.net>`

```
There are lots of ways to do this.  Probably the easiest, code wise, is
this:

01    SPACE-CNT        PIC S9(4) COMP.
01    STRT                    PIC S9(4) COMP.
01    LEN                      PIC S9(4) COMP.
01    T-ACTION           PIC X(80).
01    D-ACTION          PIC X(80).

MOVE ZERO TO SPACE-CNT
                              STRT
                              LEN.
MOVE SPACES TO D-ACTION.
INSPECT FUNCTION REVERSE (T-ACTION) TALLYING SPACE-CNT
             FOR LEADING SPACES.
***COMPUTE STRT = ((80 - (80 - SPACE-CNT)) / 2) + 1.
COMPUTE LEN = 80 - SPACE-CNT.
COMPUTE STRT = ((80 - LEN) / 2) + 1.
MOVE T-ACTION TO D-ACTION (STRT:).

This assumes that T-ACTION is you test action field.  Since you did not
specify the max length, I assumed 80.  D-ACTION is your display action
field.

The INSPECT counts your trailing spaces within your test action field.  I
showed you the calculation in two different ways.  The first (commented
out), skips using the intermediate determination of the length (LEN) of the
text in text action.  The second is shown just to make it easier to
understand.

The idea behind it is this:  by subtracting the number of trailing spaces
from the maximum available space (assuming the text begins in position 1),
we get the length of the text within text action.  By subtracting the length
of the actual text from the maximum length of the display field, then
dividing by 2, we get the number of spaces we want to skip (rounded down).
Adding one gives us the start position we want...



David. E. Goble <goble@gtech> wrote in message
news:3a1f1334.22166110@news.adelaide.on.net...
> Hi all;
>
…[36 more quoted lines elided]…
> Po Box 648 Kingscote, Kangaroo Island, SA 5223
```

##### ↳ ↳ Re: help centering string1 into string2

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-11-26T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3a2128b5.47655251@207.126.101.100>`
- **References:** `<3a1f1334.22166110@news.adelaide.on.net> <8vqtuf$5bcvq$1@ID-39920.news.dfncis.de>`

```
Did you try to compile this?  I don't think (soon yes, but not now)
that you can inspect a function like this.  If it works when you
compile it, please tell us what compiler you are using.  This
certainly is supported in the draft standard.

On Sun, 26 Nov 2000 06:01:28 -0600, "DBuck" <dbuck@prairieinet.net>
wrote:

>There are lots of ways to do this.  Probably the easiest, code wise, is
>this:
…[79 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: help centering string1 into string2

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2000-11-26T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8vrc5h$5fk0v$1@ID-39920.news.dfncis.de>`
- **References:** `<3a1f1334.22166110@news.adelaide.on.net> <8vqtuf$5bcvq$1@ID-39920.news.dfncis.de> <3a2128b5.47655251@207.126.101.100>`

```

Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:3a2128b5.47655251@207.126.101.100...
> Did you try to compile this?  I don't think (soon yes, but not now)
> that you can inspect a function like this.  If it works when you
> compile it, please tell us what compiler you are using.  This
> certainly is supported in the draft standard.
>

While I didn't compile this particular piece of code, I have used
(extensively) all parts illustrated on an IBM390 using COBOL for MVS -
especially the FUNCTION REVERSE and the reference modication - which is
pretty much all there is to this little example....

Since IBM usually sits pretty much with the standard, I had assumed (perhaps
making an a$$ out of you and me, or at least me) that this was pretty
universal with the newer releases.  The COBOL for MVS that we are using is
from the early 90's.

Here is another example, using the same principle but not using the FUNCTION
REVERSE:

01    SPACE-CNT        PIC S9(4) COMP.
01    STRT                    PIC S9(4) COMP.
01    LEN                      PIC S9(4) COMP.
01    T-ACTION           PIC X(80).
01    D-ACTION          PIC X(80).

MOVE ZERO TO STRT
                              LEN.
MOVE SPACES TO D-ACTION.
PERFORM VARYING SPACE-CNT FROM 80 BY -1 UNTIL SPACE-CNT < 1
                                                        OR T-ACTION
(SPACE-CNT:1) NOT = SPACES
   CONTINUE
END-PERFORM.
***COMPUTE STRT = ((80 - (80 - SPACE-CNT)) / 2) + 1.
COMPUTE LEN = 80 - SPACE-CNT.
COMPUTE STRT = ((80 - LEN) / 2) + 1.
MOVE T-ACTION TO D-ACTION (STRT:).

Sorry if this is causing any confusion (although everyone is getting to see
several different ways to do this)....

Dave


> On Sun, 26 Nov 2000 06:01:28 -0600, "DBuck" <dbuck@prairieinet.net>
> wrote:
…[27 more quoted lines elided]…
> >out), skips using the intermediate determination of the length (LEN) of
the
> >text in text action.  The second is shown just to make it easier to
> >understand.
> >
> >The idea behind it is this:  by subtracting the number of trailing spaces
> >from the maximum available space (assuming the text begins in position
1),
> >we get the length of the text within text action.  By subtracting the
length
> >of the actual text from the maximum length of the display field, then
> >dividing by 2, we get the number of spaces we want to skip (rounded
down).
> >Adding one gives us the start position we want...
> >
…[48 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: help centering string1 into string2

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-11-27T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3a22cbe1.94141647@207.126.101.100>`
- **References:** `<3a1f1334.22166110@news.adelaide.on.net> <8vqtuf$5bcvq$1@ID-39920.news.dfncis.de> <3a2128b5.47655251@207.126.101.100> <8vrc5h$5fk0v$1@ID-39920.news.dfncis.de>`

```
It wasn't the function ITSELF I was questioning, but rather the use of
it in an INSPECT statement.  I don't think you can yet INSPECT a
function.


On Sun, 26 Nov 2000 10:04:10 -0600, "DBuck" <dbuck@prairieinet.net>
wrote:

>
>Thane Hubbell <thaneH@softwaresimple.com> wrote in message
…[139 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: help centering string1 into string2

_(reply depth: 5)_

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2000-11-27T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8vv2hq$5mkbe$1@ID-39920.news.dfncis.de>`
- **References:** `<3a1f1334.22166110@news.adelaide.on.net> <8vqtuf$5bcvq$1@ID-39920.news.dfncis.de> <3a2128b5.47655251@207.126.101.100> <8vrc5h$5fk0v$1@ID-39920.news.dfncis.de> <3a22cbe1.94141647@207.126.101.100>`

```

Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:3a22cbe1.94141647@207.126.101.100...
> It wasn't the function ITSELF I was questioning, but rather the use of
> it in an INSPECT statement.  I don't think you can yet INSPECT a
> function.
>
Well, I know for a fact that you can do so in COBOL for MVS.  I have several
programs in production that do so.  Past that, I can't make any promises...


>
> On Sun, 26 Nov 2000 10:04:10 -0600, "DBuck" <dbuck@prairieinet.net>
…[16 more quoted lines elided]…
> >Since IBM usually sits pretty much with the standard, I had assumed
(perhaps
> >making an a$$ out of you and me, or at least me) that this was pretty
> >universal with the newer releases.  The COBOL for MVS that we are using
is
> >from the early 90's.
> >
> >Here is another example, using the same principle but not using the
FUNCTION
> >REVERSE:
> >
…[19 more quoted lines elided]…
> >Sorry if this is causing any confusion (although everyone is getting to
see
> >several different ways to do this)....
> >
…[6 more quoted lines elided]…
> >> >There are lots of ways to do this.  Probably the easiest, code wise,
is
> >> >this:
> >> >
…[17 more quoted lines elided]…
> >> >This assumes that T-ACTION is you test action field.  Since you did
not
> >> >specify the max length, I assumed 80.  D-ACTION is your display action
> >> >field.
> >> >
> >> >The INSPECT counts your trailing spaces within your test action field.
I
> >> >showed you the calculation in two different ways.  The first
(commented
> >> >out), skips using the intermediate determination of the length (LEN)
of
> >the
> >> >text in text action.  The second is shown just to make it easier to
> >> >understand.
> >> >
> >> >The idea behind it is this:  by subtracting the number of trailing
spaces
> >> >from the maximum available space (assuming the text begins in position
> >1),
…[62 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: help centering string1 into string2

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2000-11-26T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<o5bU5.75$OL4.7326@nnrp2.sbc.net>`
- **References:** `<3a1f1334.22166110@news.adelaide.on.net> <8vqtuf$5bcvq$1@ID-39920.news.dfncis.de> <3a2128b5.47655251@207.126.101.100>`

```
Inspect function reverse....  works with the tallying feature.
I do this routinely to change trailing spaces to low-values to
make data compatible with goofy C stuff.

MOVE ZERO TO TALLY-FIELD.
INSPECT FUNCTION REVERSE (SOME-DATA)
  TALLYING TALLY-FIELD FOR LEADING SPACES.
MOVE LOW-VALUES TO SOME-DATA
            ( LENGTH OF SOME-DATA - TALLY-FIELD + 1 : TALLY-FIELD).

This works on OS/390 as well as Micro-Focus.

The obvious thought someone will have is why not do:
INSPECT FUNCTION REVERSE (SOME-DATA)
  REPLACING LEADING SPACES BY LOW-VALUES.
But this does not work. On OS/390 it will not compile. On Micro-Focus
it compiles but evidently the reversing action takes place in some work
area and the replacing action then takes place in the same work area
leaving SOME-DATA unchanged.
```

#### ↳ Re: help centering string1 into string2

- **From:** "Jason P. Hudson" <jason@44sycamore.freeserve.co.uk>
- **Date:** 2000-11-26T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8vrjlr$kts$1@newsg3.svr.pol.co.uk>`
- **References:** `<3a1f1334.22166110@news.adelaide.on.net>`

```
Hi David

I see you also use microfocus cobol.

A quick solution would be

77 WS-DISP-ACTION               PIC X(80).
            i would assume that ws-text is less than 80 chars long say 75
77 WS-ACTION                    PIC X(75).
77 WS-LEN                       PIC 9(02).
77 WS-OFFSET                    PIC 9(02).
.....
..
..
    *         get length of action text field and store value in ws-len
         PERFORM
            VARYING WS-LEN FROM 75 BY -1
            UNTIL   WS-LEN < 1
                 OR WS-ACTION(WS-LEN:1) NOT = SPACE
         END-PERFORM.
    *
    *            get offset - 80 been the length of ws-disp-action
         COMPUTE WS-OFFSET = (80 - WS-LEN)/2.
    *
    *            initialise the display field
         MOVE SPACES    TO WS-DISP-ACT.
    *
    *            move your action text to display starting at offset
         MOVE WS-ACTION TO WS-DISP-ACT(WS-OFFSET:).

I hope this solves your problem.
The use of refential access of individual charaters within a string ie with
the bracket + colon at the end of an identifier, simplifies character/string
manipulation and has been implemented in Microfocus Cobol.

Regards

Jason
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
