[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dumb Question Time: Qualification of data items

_6 messages · 4 participants · 2004-06 → 2004-08_

---

### Dumb Question Time: Qualification of data items

- **From:** "PAUL RAULERSON" <pkraulerson@verizon.net>
- **Date:** 2004-06-23T02:25:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XS5Cc.23889$a61.17636@nwrddc01.gnilink.net>`

```
I am not sure if I am mixing COBOL and Assembler, or Ada (or some other
language) up,
but isn't there a way to qualify a set of data items within a block
statement?

Something like:

    USING A-RECORD
       MOVE 'A' TO ITEM-1
       MOVE 2   TO ITEM-2
       END-USING

    USING B-RECORD
        MOVE 'B' TO ITEM-1
        MOVE 3   TO ITEM-2
        END-USING

  RATHER THAN

       MOVE 'A' TO ITEM-1 OF A-RECORD
       MOVE 2   TO ITEM-2 OF A-RECORD
       MOVE 'B' TO ITEM-1 OF B-RECORD
       MOVE 3   TO ITEM-2 OF B-RECORD

I swear, I thought this existed at least in IBM COBOL somewhere,
but I can not find anything like this at all in the reference manuals.

-Paul
```

#### ↳ Re: Dumb Question Time: Qualification of data items

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-06-22T22:34:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-B1DE6D.22344322062004@corp.supernews.com>`
- **References:** `<XS5Cc.23889$a61.17636@nwrddc01.gnilink.net>`

```
In article <XS5Cc.23889$a61.17636@nwrddc01.gnilink.net>,
 "PAUL RAULERSON" <pkraulerson@verizon.net> wrote:

> I am not sure if I am mixing COBOL and Assembler, or Ada (or some other
> language) up,
…[26 more quoted lines elided]…
> 

I think you might be mixing in the ADA.  But wasn't it called "WITH 
record DO" or is that the Pascal word?

The new assembler supports this something similar -- you can label a 
DSECT and then refer to the label.fieldname to resolve an offset rather 
than do an explicit using.

I wish there were such a notation for Cobol, as it would be a very cool  
time saving feature.
```

##### ↳ ↳ Re: Dumb Question Time: Qualification of data items

- **From:** "PAUL RAULERSON" <pkraulerson@verizon.net>
- **Date:** 2004-06-23T02:38:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m26Cc.23923$a61.16961@nwrddc01.gnilink.net>`
- **References:** `<XS5Cc.23889$a61.17636@nwrddc01.gnilink.net> <joe_zitzelberger-B1DE6D.22344322062004@corp.supernews.com>`

```
Thanks Joe - I sure wish it were there too. I could fix some really annoying
code I did not write much easier.
I love the new Assembler syntax. I have to check with the Dignus guys to
make sure we can use it. :)

-Paul


"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message
news:joe_zitzelberger-B1DE6D.22344322062004@corp.supernews.com...
> In article <XS5Cc.23889$a61.17636@nwrddc01.gnilink.net>,
>  "PAUL RAULERSON" <pkraulerson@verizon.net> wrote:
…[39 more quoted lines elided]…
> time saving feature.
```

#### ↳ Re: Dumb Question Time: Qualification of data items

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2004-06-23T02:19:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0406230119.304a3cd2@posting.google.com>`
- **References:** `<XS5Cc.23889$a61.17636@nwrddc01.gnilink.net>`

```
Paul,

if you have a large number of these qualified moves it might be worth
setting a PFK  or keystroke combination with SPF to produce " OF
A-RECORD" etc. At least that way it's one key depression...

Of course it is a pain to have to re-program the key for each new
record...

What about some global edits to change the names to something unique,
like A-REC-ITEM1, A-REC-ITEM2 etc.? If these are record layouts from
COPY books you could set this up at the time you COPY them in; REPLACE
the level number so: COPY A-RECORD REPLACING ' 03 ' BY ' 03 A-REC-' 
etc.

If it isn't a copy book, a quick cut and paste might do the
trick...(this can be modified to work for a COPY book as well, but it
is a bit more effort..)


01  A-RECORD.
    12 ITEM1      PIC ...
       ...
    12 ITEM53     PIC ...

Copy the above and paste it as a redefinition...

01  A-RECORD.
    12 ITEM1      PIC ...
       ...
    12 ITEM53     PIC ...
01  FILLER REDEFINES A-RECORD.
    12 ITEM1      PIC ...
       ...
    12 ITEM53     PIC ...

Edit the redefinition...

01  A-RECORD.
    12 ITEM1      PIC ...
       ...
    12 ITEM53     PIC ...
01  FILLER REDEFINES A-RECORD.
    12 $A-ITEM1      PIC ...
       ...
    12 $A-ITEM53     PIC ...

Do the same for the other records...

01  B-RECORD.
    12 ITEM1      PIC ...
       ...
    12 ITEM53     PIC ...
01  FILLER REDEFINES B-RECORD.
    12 $B-ITEM1      PIC ...
       ...
    12 $B-ITEM53     PIC ...

Now make your amendments using the redefined fields without
qualification...


MOVE 'A' to $A-ITEM1
MOVE 123 TO $C-ITEM23
MOVE $A-ITEM2 TO $B-ITEM2
...

When you are through, run global edits to replace $A with 'A-REC', $B
with 'B-REC' and so on.

The main advantage of doing this is that any existing qualified
references will still work OK, and you are gradually 'migrating' the
programs to the point where they don't require qualification.

The obvious downside is that if the ORIGINAL is modified, the
REDEFINITION must be also (that's why it isn't such a good idea for
COPY books, unless you can modify the COPY book original.)

I'm not claiming that any of the above are "elegant" solutions, but
looking at them may stimulate you to something appropriate for the
environment you are working in.

Visual Basic has the USING facility almost exactly as you posted.

I agree it would be a useful facility to see in COBOL. These days I
make sure record layouts are unique, but you are dealing with other
people's code...

Pete.

"PAUL RAULERSON" <pkraulerson@verizon.net> wrote in message news:<XS5Cc.23889$a61.17636@nwrddc01.gnilink.net>...
> I am not sure if I am mixing COBOL and Assembler, or Ada (or some other
> language) up,
…[25 more quoted lines elided]…
> -Paul
```

##### ↳ ↳ Qualification is matter of COBOL Theology was Re: Dumb Question Time: Qualification of data items

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2004-08-26T21:15:19-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2p7g3oFhvqasU2@uni-berlin.de>`
- **In-Reply-To:** `<b3638c46.0406230119.304a3cd2@posting.google.com>`
- **References:** `<XS5Cc.23889$a61.17636@nwrddc01.gnilink.net> <b3638c46.0406230119.304a3cd2@posting.google.com>`

```
Peter E. C. Dashwood wrote:
> Paul,
> 
> if you have a large number of these qualified moves it might be worth
> setting a PFK  or keystroke combination with SPF to produce " OF
> A-RECORD" etc. At least that way it's one key depression...

I have wanted to be able to code A-FILE.FIELD-1 instead of FIELD-1 OF
A-FILE for at least 20 - 30 years.  This would extend to include
A-FILE.B-RECORD.C-GROUP.FIELD-1 instead of
FIELD-1 OF C-GROUP OF B-RECORD OF A-FILE.  The notation is consistent 
with other languages and unambiguous.  The only case for it not working 
is if a site uses pure numeric section and paragraph names, something 
still allowed even if it makes no sense.  Since I have never used 
qualified paragraph names, I am willing to live with using the "." means 
of qualification only for data division items.  COPY REPLACING LEADING 
is an improvement that allows us to easily reuse the descriptions where 
the field names have a common prefix but at the expense of not being 
able to use MOVE CORRESPONDING and ADD CORRESPONDING.

> Of course it is a pain to have to re-program the key for each new
> record...
…[111 more quoted lines elided]…
>>-Paul
```

###### ↳ ↳ ↳ Re: Qualification is matter of COBOL Theology was Re: Dumb Question Time: Qualification of data items

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-26T23:14:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-42DB01.23140826082004@knology.usenetserver.com>`
- **References:** `<XS5Cc.23889$a61.17636@nwrddc01.gnilink.net> <b3638c46.0406230119.304a3cd2@posting.google.com> <2p7g3oFhvqasU2@uni-berlin.de>`

```
I wish I could do that as well.  

But there are those in the COBOL community that insist that it look like 
English -- regardless of the 4 - errr 5 -- decades of proof that English 
speaking ability is not corelated with programming skill.

Don't give up hope -- they gave use COMPUTE, maybe they will see the 
light...

In article <2p7g3oFhvqasU2@uni-berlin.de>,
 "Clark F. Morris, Jr." <cfmtech@istar.ca> wrote:

> Peter E. C. Dashwood wrote:
> > Paul,
…[139 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
