[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CONTINUE in a search

_15 messages · 8 participants · 2000-01_

---

### CONTINUE in a search

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3885EBD5.5403951B@NOSPAMwebaccess.net>`

```
What is the cleanest way of doing the following invalid code?:
     IF C-OLD-REC-KEY > BC-REC-KEY
         SEARCH NEW-KEY-RECORD
            VARYING NEW-KEY-INDEX
              AT END
                  DISPLAY 'at-end of table with no luck'
              WHEN 'XX12345'  = NEW-KEY-RECORD (NEW-KEY-INDEX)
                  continue
         END-SEARCH
         imperative-command-1
         imperative-command-2
     END-IF.
```

#### ↳ Re: CONTINUE in a search

- **From:** Joseph Kohler <joe_kohler@yahoo.com>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38861C7C.CBE4BC53@yahoo.com>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net>`

```
How about coding PERFORM NO-OP which is an empty paragraph and
essentially does nothing.  This way your subscript is pointing to the
record you want.  If you weren't in a IF...END-IF sequence I imagine you
would have coded NEXT SENTENCE but an empty paragraph should do the
trick.  

Joe

Howard Brazee wrote:
> 
> What is the cleanest way of doing the following invalid code?:
…[10 more quoted lines elided]…
>      END-IF.
```

##### ↳ ↳ Re: CONTINUE in a search

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38871D8B.96B3F989@NOSPAMwebaccess.net>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net> <38861C7C.CBE4BC53@yahoo.com>`

```


Joseph Kohler wrote:
> 
> How about coding PERFORM NO-OP which is an empty paragraph and
…[5 more quoted lines elided]…
> Joe

Hadn't thought of that.  I ended up pulling the SEARCH into its own
paragraph so that NEXT SENTENCE would work.
```

#### ↳ Re: CONTINUE in a search

- **From:** "Glenn Gordon" <ggordon@dimensional.com>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N3vh4.482$x3.799@wormhole.dimensional.com>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net>`

```
Well, the code isn't exactly invalid, although the logic is suspect.
Assuming that the NEW-KEY-INDEX is set at an appropriate value prior to the
search (inferred from the names), there is the problem of
imperative-command-1 and -2 still being executed when the search fails.  It
is unlikely you would want to do the same thing regardless of the search
result.  CONTINUE is a valid statement, it will not continue the search, but
will drop you to the first statement following the END-SEARCH.

Without more information about what you are trying to accomplish there
really isn't a way for me to provide an opinion of what way is cleanest.
Your 'invalid' code does not adequately explain your intentions.

Glenn


"Howard Brazee" <brazee@NOSPAMwebaccess.net> wrote in message
news:3885EBD5.5403951B@NOSPAMwebaccess.net...
> What is the cleanest way of doing the following invalid code?:
>      IF C-OLD-REC-KEY > BC-REC-KEY
…[9 more quoted lines elided]…
>      END-IF.
```

##### ↳ ↳ Re: CONTINUE in a search

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38871C37.BBC6C6C2@NOSPAMwebaccess.net>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net> <N3vh4.482$x3.799@wormhole.dimensional.com>`

```


Glenn Gordon wrote:
> 
> Well, the code isn't exactly invalid, although the logic is suspect.
…[5 more quoted lines elided]…
> will drop you to the first statement following the END-SEARCH.

CONTINUE didn't work for me, it wouldn't compile cleanly.  Maybe that's
a problem with my COBOL for MVS compiler.  NEXT SENTENCE was listed as
an IBM extension.  If I want to do that, however, I need to remove the
search from within the IF statement and put it into its own paragraph.


> Without more information about what you are trying to accomplish there
> really isn't a way for me to provide an opinion of what way is cleanest.
> Your 'invalid' code does not adequately explain your intentions.

My intention is to display a message if there is no match - but to
continue processing anyway, just the same as if there was a match.
 
> Glenn
> 
…[13 more quoted lines elided]…
> >      END-IF.
```

###### ↳ ↳ ↳ Re: CONTINUE in a search

- **From:** thaneH@softwaresimple.com
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<867ilv$dha$1@nnrp1.deja.com>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net> <N3vh4.482$x3.799@wormhole.dimensional.com> <38871C37.BBC6C6C2@NOSPAMwebaccess.net>`

```

> My intention is to display a message if there is no match - but to
> continue processing anyway, just the same as if there was a match.
>

Then try this:


      IF C-OLD-REC-KEY > BC-REC-KEY
          SEARCH NEW-KEY-RECORD
             VARYING NEW-KEY-INDEX
               AT END
                   DISPLAY 'at-end of table with no luck'
                   Perform Next-Step
               WHEN 'XX12345'  = NEW-KEY-RECORD (NEW-KEY-INDEX)
                   Perform Next-Step
          END-SEARCH
      END-IF.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: CONTINUE in a search

- **From:** "Glenn Gordon" <ggordon@dimensional.com>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hN9i4.541$x3.901@wormhole.dimensional.com>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net> <N3vh4.482$x3.799@wormhole.dimensional.com> <38871C37.BBC6C6C2@NOSPAMwebaccess.net>`

```
Hmmm...  You say your compiler chokes on the CONTINUE in the WHEN clause?  I
work with IBM MVS COBOL a lot, and I am pretty sure I have used a CONTINUE
in this manner!  I'll make a note to double-check on Monday at the office,
the only difference is I have always done it with multiple WHENs on the
search.  My use was inserting unique keys into a small table to accumulate
field values for the key values of selected records, something to the effect
of:

IF data-flag
    SET ndx TO +1
    SEARCH table VARYING ndx
        AT END
            error logic here, unique item but table is full
        WHEN ndx = next-free-ndx
            MOVE data-key to table-key(next-free-ndx)
            ADD +1 TO next-free-ndx
        WHEN table-key(ndx) = search-key
            CONTINUE
    END-SEARCH
    ADD data-value TO table-value(ndx)
END-IF

which looks an awful lot like what you had.  I'll double-check at the office
Monday just how I coded it.  Are you sure the problem was not related to
your index being out of range?  For a sequential search the index value
starts wherever it happens to be to facilitate skip-sequential processing.


Glenn


"Howard Brazee" <brazee@NOSPAMwebaccess.net> wrote in message
news:38871C37.BBC6C6C2@NOSPAMwebaccess.net...
> My intention is to display a message if there is no match - but to
> continue processing anyway, just the same as if there was a match.
```

###### ↳ ↳ ↳ Re: CONTINUE in a search

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388C6418.14603E80@NOSPAMwebaccess.net>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net> <N3vh4.482$x3.799@wormhole.dimensional.com> <38871C37.BBC6C6C2@NOSPAMwebaccess.net> <hN9i4.541$x3.901@wormhole.dimensional.com>`

```
I just double checked, and it did NOT choke.  I wonder what happened
last week.

Glenn Gordon wrote:
> 
> Hmmm...  You say your compiler chokes on the CONTINUE in the WHEN clause?  I
> work with IBM MVS COBOL a lot, and I am pretty sure I have used a CONTINUE
> in this manner!
```

#### ↳ Re: CONTINUE in a search

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8663bb01930@enews3.newsguy.com>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net>`

```
  01  FILLER               PIC X.
      88  TABLE-REC-FOUND         VALUE 'Y'.
      88  TABLE-REC-NOT-FOUND     VALUE 'N'.
```

##### ↳ ↳ Re: CONTINUE in a search

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38871D21.EDBDF76F@NOSPAMwebaccess.net>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net> <8663bb01930@enews3.newsguy.com>`

```


Jeff Baynard wrote:
> 
>   01  FILLER               PIC X.
…[18 more quoted lines elided]…
>       END-IF.

I have used this type of logic, but I like to avoid switches.  I guess
sometimes I can't.  Too bad I can't use CONTINUE.
 
> OR
> 
…[17 more quoted lines elided]…
> Is this what you meant?

As much as I dislike GO TOs, they are better than switches.  But in this
case, it doesn't do what I want.  In each case imperative-commands
should be run.  With my compiler, CONTINUE was marked as invalid.

> In article <3885EBD5.5403951B@NOSPAMwebaccess.net>, Howard Brazee
> <brazee@NOSPAMwebaccess.net> wrote:
…[12 more quoted lines elided]…
> >      END-IF.
```

#### ↳ Re: CONTINUE in a search

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eZsh4.1398$xZ3.25558@dfiatx1-snr1.gtei.net>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net>`

```
What I usually do is set an explicit flag when I find something...

IF Whatever
   MOVE 'N'  TO ITEM-FOUND-SW
   SEARCH   TABLE-NAME
     AT END
      CONTINUE
    WHEN...
      SET ITEM-FOUND TO TRUE
   END-SEARCH
   IF ITEM-FOUND....
   ...
   END-IF
END-IF

MCM
```

##### ↳ ↳ Re: CONTINUE in a search

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3887169D.E4688288@NOSPAMwebaccess.net>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net> <eZsh4.1398$xZ3.25558@dfiatx1-snr1.gtei.net>`

```
I've tried that some times, but I hate flags.  Also, on an IBM
mainframe, NEXT SENTENCE is allowed, so I have pulled the SEARCH from
within the IF and put it in its own paragraph.

But there should be a better way.

Since yours is the first reply I have seen, I doubt if there is.  I
wonder why CONTINUE isn't allowed here.

Michael Mattias wrote:
> 
> What I usually do is set an explicit flag when I find something...
…[35 more quoted lines elided]…
> >     END-IF.
```

#### ↳ Re: CONTINUE in a search

- **From:** Volker Bandke <vbandke@ibm.net>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r4id8s8fbo6gfd7oikh6rsk5up2f2qjvmc@4ax.com>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net>`

```
On Wed, 19 Jan 2000 09:52:37 -0700, Howard Brazee <brazee@NOSPAMwebaccess.net> wrote:

>What is the cleanest way of doing the following invalid code?:
>     IF C-OLD-REC-KEY > BC-REC-KEY
…[9 more quoted lines elided]…
>     END-IF.


Make a new variable

01	Misc-Flag	PIC X	VALUE 'N'.
	88  Found-it		VAlue 'Y'.

and instead of the "continue" code

	SET found-it TO TRUE
```

##### ↳ ↳ Re: CONTINUE in a search

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86tvg8$mbn$1@nntp5.atl.mindspring.net>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net> <r4id8s8fbo6gfd7oikh6rsk5up2f2qjvmc@4ax.com>`

```
Having been away from the NG, did someone verify that CONTINUE is completely
VALID within a SEARCH Statement (where IBM allows - as an extension - a NEXT
SENTENCE - which means something else).

If you (anyone) is still getting a compiler error on a CONTINUE in a SEARCH
statement, please re-post the source code - and include the exact compiler
message.
```

###### ↳ ↳ ↳ Re: CONTINUE in a search

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38959CE5.DB21A936@NOSPAMwebaccess.net>`
- **References:** `<3885EBD5.5403951B@NOSPAMwebaccess.net> <r4id8s8fbo6gfd7oikh6rsk5up2f2qjvmc@4ax.com> <86tvg8$mbn$1@nntp5.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> Having been away from the NG, did someone verify that CONTINUE is completely
…[5 more quoted lines elided]…
> message.

I thought I was getting a compiler error, but I no longer have it.  When
I tried to duplicate the problem, it did not occur.  Maybe I did
something different, maybe I was completely wrong to begin with.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
