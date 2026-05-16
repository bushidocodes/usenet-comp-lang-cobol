[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP

_17 messages · 8 participants · 2001-10_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### HELP

- **From:** JONESEY <mrjones_101@hotmail.com>
- **Date:** 2001-10-22T00:32:30+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com>`

```
So Im pretty new to cobol!! My problem is that I am reading records from one file carrying out calculations and writing the new data to a sequential
output file. Im using fillers to line up the titles and the main problem I have is that it outputs like this:-

?Pï¿½ï¿½ï¿½Xï¿½
 ï¿½ï¿½ï¿½:ï¿½uï¿½ï¿½ ï¿½GROSS      N.I.   TAX    PENSION NETPAY
?Pï¿½ï¿½ï¿½Xï¿½
 ï¿½ï¿½ï¿½:ï¿½uï¿½ï¿½ ï¿½---------------------------------------
Ms   Elizabeth Wilson  1076.17    43.05 132.01  64.57  ï¿½836.54
Mr   John McMordie      560.92    22.44 167.31   0.00  ï¿½306.59
Mrs  Emma Keers         708.33    28.33  47.41  42.49  ï¿½590.10
Mr   Robert Gillespie  1931.83    70.00  98.81 115.90 ï¿½1639.85
Mrs  Sharon Murray      359.75    14.39   0.00   0.00  ï¿½229.46
Miss Lynda Creighton   1799.67    70.00  68.42   0.00 ï¿½1543.36
Mr   William Sloan      600.00    24.00  22.50  36.00  ï¿½517.50
Mr   William Sloan      600.00***  END OF FILE  ***

The first two lines and the last line have rubbish info (william sloan and 600 on ht ebootm line). THe fillers have been decalred as part of record
like this:-

          02 FILLER             PIC X(30).

Any help would be appreciated

J
```

#### ↳ Re: HELP

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-10-21T17:05:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD362B4.3995@paralynx.com>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com>`

```
JONESEY wrote:
> 
> So Im pretty new to cobol!! My problem is that I am reading records from one file carrying out calculations and writing the new data to a sequential
…[20 more quoted lines elided]…
> Any help would be appreciated

Only use FILLER where you don't care what the field contains.  To pad out either give 
the empty bits real names and fill them with spaces or else move spaces to a 
redefinition of your 01 level.

Your last line probably results from recognising EOF in the wrong place in your code. 
You printed a line after you hit EOF and some of the data from the previous operation 
was left in it.
```

#### ↳ Re: HELP

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-10-22T03:52:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bKMA7.37823$ev2.44313@www.newsranger.com>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com>`

```
Hi Jonesey,

Filler can be coded 2 ways:

0x Filler      PIC X(5). 
This form just reserves space for data moved into it, at a higher level. For
example, if the Filler is an 05 level, the Filler is part of the 01 level
receiving the moved data. That is the only way the field can be populated. If a
move isn't performed, the contents of the field are unpredictable.

0x Filler      PIC X(5) VALUE 'GROSS'. 
This form fills the space w/the chars 'GROSS' and no move of data is required.
This is a way to initialize data fields, especially useful in crating report
headings and field titles. The existing data (GROSS) can be overlaid with other
data by a move to a higher level as above (sometimes by mistake).

HTH, Jack 


In article <5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com>, JONESEY says...
>
>So Im pretty new to cobol!! My problem is that I am reading records from one file carrying out calculations and writing the new data to a sequential
…[22 more quoted lines elided]…
>J
```

#### ↳ Re: HELP

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-10-22T07:42:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qwTA7.6290$ET.734319@news20.bellglobal.com>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com>`

```
From the looks of it, you are attempting to line up text printed in a
proportional font. Change the printer font to a mono spaced type, and try
the code that way.


"JONESEY" <mrjones_101@hotmail.com> wrote in message
news:5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com...
> So Im pretty new to cobol!! My problem is that I am reading records from
one file carrying out calculations and writing the new data to a sequential
> output file. Im using fillers to line up the titles and the main problem I
have is that it outputs like this:-
>
> ?P���X�
…[12 more quoted lines elided]…
> The first two lines and the last line have rubbish info (william sloan and
600 on ht ebootm line). THe fillers have been decalred as part of record
> like this:-
>
…[4 more quoted lines elided]…
> J
```

##### ↳ ↳ Re: HELP

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-10-22T16:42:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD44E07.F9EF501@home.com>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com> <qwTA7.6290$ET.734319@news20.bellglobal.com>`

```


Donald Tees wrote:

> From the looks of it, you are attempting to line up text printed in a
> proportional font. Change the printer font to a mono spaced type, and try
…[30 more quoted lines elided]…
> > J

It *might* give you a quick solution - try specifying your fillers as follows :-

         02 FILLER             PIC X(30) value spaces..

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: HELP

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-10-22T12:50:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<X1YA7.6596$ET.875233@news20.bellglobal.com>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com> <qwTA7.6290$ET.734319@news20.bellglobal.com> <3BD44E07.F9EF501@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message
news:3BD44E07.F9EF501@home.com...
>
>
…[3 more quoted lines elided]…
> > proportional font. Change the printer font to a mono spaced type, and
try
> > the code that way.
> >
> > "JONESEY" <mrjones_101@hotmail.com> wrote in message
> > news:5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com...
> > > So Im pretty new to cobol!! My problem is that I am reading records
from
> > one file carrying out calculations and writing the new data to a
sequential
> > > output file. Im using fillers to line up the titles and the main
problem I
> > have is that it outputs like this:-
> > >
…[13 more quoted lines elided]…
> > > The first two lines and the last line have rubbish info (william sloan
and
> > 600 on ht ebootm line). THe fillers have been decalred as part of record
> > > like this:-
…[7 more quoted lines elided]…
> It *might* give you a quick solution - try specifying your fillers as
follows :-
>
>          02 FILLER             PIC X(30) value spaces..
>
> Jimmy, Calgary AB
>

that too, that too.

;<)
```

#### ↳ Re: HELP

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-10-22T16:30:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lQXA7.38363$ev2.45016@www.newsranger.com>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com>`

```
On Mon, 22 Oct 2001 00:32:30 +0100, in article
<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com>, JONESEY stated 
>
>So Im pretty new to cobol!! My problem is that I am reading records from one file carrying out calculations and writing the new data to a sequential
>output file. Im using fillers to line up the titles and the main problem I have is that it outputs like this:-

Looks like you are putting something in a storage location then printing it;
then when you go to print it again it is still there.  

Initially it might be nice to move spaces to fields to start out with; otherwise
the printline's memory location may already have something at that location to
start with.  Then, as you print lines, you may need to move spaces to it to
blank it out. If nothing is moved to that location, whatever was moved there
last time may still be there. 

A lot depends on how you describe the fillers. 
>
>?P���X�
…[15 more quoted lines elided]…
>          02 FILLER             PIC X(30).

Try this:

02 FILLER             PIC X(30) VALUE SPACES.
(This will initially blank it out.) 

A lot depends on how you do the printing of the lines.  Usually I use a blank
print line like this.

01 PRINT-LINE                   PIC X(80) VALUE SPACES.

Then use the command:

WRITE PRINT-LINE FROM SOME-OTHER-LINE AFTER 1 LINE.

If you have fields you reuse, you may have to reinitialize them by moving spaces
to that field.

This is a pretty common problem, that I have dealt with before.  Sometimes
things like this occur even though I think I have prevented it from happening.

>
>Any help would be appreciated
>
>J
```

#### ↳ Re: HELP

- **From:** JONESEY <mrjones_101@hotmail.com>
- **Date:** 2001-10-22T21:08:27+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k5v8ttooo29dti912ivp2g762ljtvi6r6c@4ax.com>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com>`

```
OK so the compiler keeps throwing up an error everytime I have tried to use value spaces

On Mon, 22 Oct 2001 00:32:30 +0100, JONESEY <mrjones_101@hotmail.com> wrote:

>So Im pretty new to cobol!! My problem is that I am reading records from one file carrying out calculations and writing the new data to a sequential
>output file. Im using fillers to line up the titles and the main problem I have is that it outputs like this:-
…[21 more quoted lines elided]…
>J
```

##### ↳ ↳ Re: HELP

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-22T15:31:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r1vq2$v9g$1@slb6.atl.mindspring.net>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com> <k5v8ttooo29dti912ivp2g762ljtvi6r6c@4ax.com>`

```
Show us the source code and the compiler error.

HINT: Any chance that you have added this VALUE statement under the FD - and
not in Working-Storage section?  If so, you need to use the VALUE clause in
WS - and then either do a WRITE FROM or a MOVE to get the value from WS to
your file "buffer".

P.S. Some compilers accept VALUE clauses in the file-section (and linkage
section) - and this will be legal in the next COBOL Standard, but NO
compiler "uses" such clauses for storage initialization.
```

###### ↳ ↳ ↳ Re: HELP

- **From:** JONESEY <mrjones_101@hotmail.com>
- **Date:** 2001-10-22T21:41:58+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dt09ttsrvojpoc78u8tc03bdtnqlattund@4ax.com>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com> <k5v8ttooo29dti912ivp2g762ljtvi6r6c@4ax.com> <9r1vq2$v9g$1@slb6.atl.mindspring.net>`

```
OK it is declared above the WS section. It is part of record.... I tried moveing another variable(decalared in WS) but still no!!


GRRRRRRR


On Mon, 22 Oct 2001 15:31:14 -0500, "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:

>Show us the source code and the compiler error.
>
…[7 more quoted lines elided]…
>compiler "uses" such clauses for storage initialization.
```

###### ↳ ↳ ↳ Re: HELP

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-10-22T21:03:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD48B4C.FFBBC49A@home.com>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com> <k5v8ttooo29dti912ivp2g762ljtvi6r6c@4ax.com> <9r1vq2$v9g$1@slb6.atl.mindspring.net> <dt09ttsrvojpoc78u8tc03bdtnqlattund@4ax.com>`

```


JONESEY wrote:

> OK it is declared above the WS section. It is part of record.... I tried moveing another variable(decalared in WS) but still no!!
>
> GRRRRRRR
>

If you are still having problems, tell us Operating System, compiler, and as Bill suggested, post the source code.

Jimmy
```

###### ↳ ↳ ↳ Re: HELP

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-22T16:32:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r23dg$btn$1@slb2.atl.mindspring.net>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com> <k5v8ttooo29dti912ivp2g762ljtvi6r6c@4ax.com> <9r1vq2$v9g$1@slb6.atl.mindspring.net> <dt09ttsrvojpoc78u8tc03bdtnqlattund@4ax.com>`

```
Everyone in comp.lang.cobol knows that I tend to offer "complex" answers -
more than students want.  My guess is that you are (as you indicated in your
first note) pretty new to COBOL and don't know some of the ways to avoid
this type of problem - that would be used in "real world" applications.
Therefore, let me try and outline a solution that should work with beginning
homework assignments.

Assume your code has the following parts (along with everything else).

FD  MyFile ...
01 Print-Line.
   05  Somefield  Pic XXX.
   05  Filler Pic X(10).
   05  AnotherField  Pic 999.
   05  Filler  Pic X(10).

   ...
Procedure Division.
* These may be paragraphs or in your mainline.

  Open Input MyFile
  Perform until EOF
    Read AnotherFile
      At end
          Set EOF to true
      Not At end
        Move InputField to Somefield
        Move AnotherInput to AnotherField
        Write Print-Line
       End-Read
 End-Perform
 Close MyFile

***
Now the TRICK to "clearing out" garbage in the first line of your output is
to do a
  Move SPACES to Print-Line
*right after* you do an OPEN of MyFile

Don't do it before the OPEN, don't do it for every WRITE (in your loop) and
don't try and move it to the individual fields.
```

###### ↳ ↳ ↳ Re: HELP

_(reply depth: 5)_

- **From:** JONESEY <mrjones_101@hotmail.com>
- **Date:** 2001-10-22T22:42:49+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4k49ttkpcs2dpkeeq2uhemtg0l322hnv6v@4ax.com>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com> <k5v8ttooo29dti912ivp2g762ljtvi6r6c@4ax.com> <9r1vq2$v9g$1@slb6.atl.mindspring.net> <dt09ttsrvojpoc78u8tc03bdtnqlattund@4ax.com> <9r23dg$btn$1@slb2.atl.mindspring.net>`

```
THANK YOU ALL VERY MUCH....

thanks to that last message I got it sorted....just moved the "Move spaces"

THANKS

n Mon, 22 Oct 2001 16:32:12 -0500, "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:

>Everyone in comp.lang.cobol knows that I tend to offer "complex" answers -
>more than students want.  My guess is that you are (as you indicated in your
…[38 more quoted lines elided]…
>don't try and move it to the individual fields.
```

##### ↳ ↳ Re: HELP

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-10-22T13:42:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD484B0.27C1@paralynx.com>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com> <k5v8ttooo29dti912ivp2g762ljtvi6r6c@4ax.com>`

```
That shouldn't be a problem if you name the filler like a variable and move spaces to 
it.

JONESEY wrote:
> 
> OK so the compiler keeps throwing up an error everytime I have tried to use value spaces
…[26 more quoted lines elided]…
> >J
```

###### ↳ ↳ ↳ Re: HELP

- **From:** JONESEY <mrjones_101@hotmail.com>
- **Date:** 2001-10-22T21:51:57+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dh19tto7a3s1e28rkb2r7fqh63poqoavcl@4ax.com>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com> <k5v8ttooo29dti912ivp2g762ljtvi6r6c@4ax.com> <3BD484B0.27C1@paralynx.com>`

```
I tried exactly that!!!

On Mon, 22 Oct 2001 13:42:24 -0700, Ed Guy <ed_guy@paralynx.com> wrote:

>That shouldn't be a problem if you name the filler like a variable and move spaces to 
>it.
…[30 more quoted lines elided]…
>> >J
```

#### ↳ Re: HELP

- **From:** "Peter Klau���" <klauss@thales.de>
- **Date:** 2001-10-25T02:02:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gfs5r9.q3r.ln@parana.thales.de>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com>`

```

"JONESEY" <mrjones_101@hotmail.com> schrieb im Newsbeitrag
news:5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com...
> So Im pretty new to cobol!! My problem is that I am reading records from
one file carrying out calculations and writing the new data to a sequential
> output file. Im using fillers to line up the titles and the main problem I
have is that it outputs like this:-
>
> ?P���X�
…[3 more quoted lines elided]…
> Ms   Elizabeth Wilson  1076.17    43.05 132.01  64.57  �836.54

I suggest you have a level 01 Record like this:

01 TEST-RECORD.
    02 NAME    PIC ....
    02 FILLER   PIC ....
    02 GROSS   PIC ....
    etc.


Before filling the fields say:

initialize TEST-RECORD.

this will fill all Fields with spaces/zeroes according to their definition
as PIC X (alpha) or
PIC 9 (numeric).

hope this will solve your problem.
```

##### ↳ ↳ Re: HELP

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-10-25T19:47:23+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD85E3B.E567E8DD@Azonic.co.nz>`
- **References:** `<5hm6tt40k4idn5jpqkcni6be9na2jhrj4h@4ax.com> <gfs5r9.q3r.ln@parana.thales.de>`

```
Peter Klauï¿½ wrote:
> >
> > ?Pï¿½ï¿½X,
…[19 more quoted lines elided]…
> PIC 9 (numeric).

Wrong.  INITIALISE will only operate on NON-FILLER fields, that is ones
that have a name. The result of the INITIALISE will be the same as if it
had not been done (given that all named fields are specifically moved
to).  This was the subject of a discussion a short while ago.  It is
necessary to MOVE SPACES TO Test-Record prior to moving the fields in to
ensure that the junk data in the FILLERs is cleared to spaces.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
