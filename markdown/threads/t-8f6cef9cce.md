[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dinosaur Alert - Error Issue

_34 messages · 11 participants · 2012-03_

**Topics:** [`COBOL's future, legacy, and obsolescence`](../topics.md#future)

---

### Dinosaur Alert - Error Issue

- **From:** "Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au>
- **Date:** 2012-03-16T23:12:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au>`

```
I have a program which compiles correctly and runs fine using Net
Express.

As the program is a MS-DOS/Screen Section/ADIS app I tried to compile
it for MS-DOS in MicroFocus 3.1.54 but receive a Fatal error.

I'm creating a dynamic table and populating it with records read from a
file:

*--- dynamic table                                      
 linkage section.                                       
 01 dataList occurs 1 to 250 depending on artist-cnt    
             ascending key is tblArtistRef              
             indexed by tbl-index.                      
    03 tblartist-rec.                                   
       05 tblArtistRef          pic x(6).               
       05 tblArtistTitle        pic x(35). 
..........             
             
The error occurs when the compiler parses the populating code: 
                                           
populate-memory-table.         *> read file and add records to   
 move eof-false to eof-status  *> memory table                   
 set tbl-index to 0            *> ERROR HERE <<<<<<

 perform artist-cnt times                                        
   read artist-file next                                         
   set tbl-index up by 1                                         
   move  artist-rec to tblartist-rec(tbl-index)                  
 end-perform                                                     
 set tbl-index to 1.           *> reset index for display start  


Error display:

"set tbl-index to 0
 ------------------
 Wrong combination of data types

 MFHXX Error 166
 Recursive Cobol Call is illegal"

Any ideas why my old COBOL compiler produces these errors and the
'modern' one doesn't? Can I recode this to avoid the error?

This is a personal hobby/interest project so I'd appreciate not
receiving admonishments for 'living in the past' etc :-)

TIA
```

#### ↳ Re: Dinosaur Alert - Error Issue

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2012-03-16T22:56:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8>`
- **In-Reply-To:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au>`

```
On Saturday, March 17, 2012 12:12:33 AM UTC-4, Paul Richards wrote:
> I have a program which compiles correctly and runs fine using Net
> Express.
…[41 more quoted lines elided]…
> 'modern' one doesn't? Can I recode this to avoid the error?

'SET index-name TO 0' is invalid in COBOL 85. however
COBOL 02 was changed to allow the statement. I suggest
the combination

    set tbl-index to 1
    set tbl-index down by 1

You have not supplied any code for recursion. If
recursion is intended, add a LOCAL-STORAGE SECTION
in WORKING-STORAGE. If recursion was not intended,
correct the SET statement and see what happens.


> This is a personal hobby/interest project so I'd appreciate not
> receiving admonishments for 'living in the past' etc :-)
…[6 more quoted lines elided]…
> Melbourne,  Australia
```

##### ↳ ↳ Re: Dinosaur Alert - Error Issue

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2012-03-16T23:16:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19485622.1987.1331964986354.JavaMail.geo-discussion-forums@vbbfw10>`
- **In-Reply-To:** `<10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8>`

```
On Saturday, March 17, 2012 1:56:33 AM UTC-4, Rick Smith wrote:

[snip]

> You have not supplied any code for recursion. If
> recursion is intended, add a LOCAL-STORAGE SECTION
> in WORKING-STORAGE. If recursion was not intended,
> correct the SET statement and see what happens.

My apologies. That should have been 'add a LOCAL-STORAGE
SECTION _after_ WORKING-STORAGE.
```

##### ↳ ↳ Re: Dinosaur Alert - Error Issue

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2012-03-17T12:37:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8>`

```
On Mar 17, 6:56 pm, Rick Smith <rs847...@gmail.com> wrote:
> On Saturday, March 17, 2012 12:12:33 AM UTC-4, Paul Richards wrote:>

> 'SET index-name TO 0' is invalid in COBOL 85.

That is not true AFAIK.

> however
> COBOL 02 was changed to allow the statement. I suggest
…[8 more quoted lines elided]…
> correct the SET statement and see what happens.
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2012-03-20T12:04:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11>`
- **In-Reply-To:** `<85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com>`

```
On Saturday, March 17, 2012 3:37:27 PM UTC-4, Richard wrote:
> On Mar 17, 6:56 pm, Rick Smith <rs847...@gmail.com> wrote:
[snip] 

> > 'SET index-name TO 0' is invalid in COBOL 85.
> 
> That is not true AFAIK.

With COBOL 85 flagging in place I get an error.
=====
* Micro Focus COBOL Version 3.2.50   L2.5 revision 000 20-Mar-12 13:14 Page   1
*                      C:\DOCUME~1\RICHARD\MYDOCU~1\CBL-CHAL\IDX1.cbl
* Options: anim ensuite(2) wb errq editor(mf) noosvs nodosvs novsc2 nocobol370
*          ans85    csi confirm
     1$set ans85 flag"ans85" flagas"s"
     2 identification division.
     3 program-id. idx1.
     4 data division.
     5 working-storage section.
     6 1 table1.
     7  2 occurs 10 indexed by idx.
     8   3 elem pic x.
     9 procedure division.
    10 begin.
    11     set idx to 0.
*  41-S****************                                                (   0)**
**    ZERO is an invalid value for an index-name
    12     stop run.
    13 end program idx1.
* Micro Focus COBOL Version 3.2.50   L2.5 revision 000
* Last message on page: 1
*
* Total Messages:     1
* Unrecoverable :     0                    Severe  :     1
* Errors        :     0                    Warnings:     0
* Informational :     0                    Flags   :     0
* Data:         516     Code:          68
=====

Without flagging I get the same error.

> > however
> > COBOL 02 was changed to allow the statement.

=====
ISO/IEC 1989:2002(E)
Substantive changes not affecting existing programs

121) SET index-name. The result of setting an index can be
outside of the range of the associated table. Also, the
setting of an index in the TO phrase does not have to be
within the range of the associated table.
=====

Note the specific reference to the "TO phrase", which
implies that COBOL 85 had stricter requirements;
i.e., 0 was not permitted since it could never be
within the range of a table.
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-03-21T18:11:20+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9st67qFr1lU1@mid.individual.net>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11>`

```
Rick Smith wrote:
> On Saturday, March 17, 2012 3:37:27 PM UTC-4, Richard wrote:
>> On Mar 17, 6:56 pm, Rick Smith <rs847...@gmail.com> wrote:
…[15 more quoted lines elided]…
> within the range of a table.

COBOL is the ONLY language I know of where zero is NOT in the range of a 
table.

So, COBOL '85 doesn't allow it (which gels with my own experience) and COBOL 
2002 allows it, but that standard has little credibility and has never been 
fully implemented.

Conclusion: Best avoided. Don't set indexes or subscripts to zero if they 
are referencing anything. (I have sometimes set an index to 1, then set it 
down by 1 in an initialization routine, before it is used. (The loop code 
would increment it before using it)  But mostly I let PERFORM control them 
and they start at 1...)

Pete.
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2012-03-21T13:40:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<akbkm7t423a67skl3jpsv616ka61dfjr8h@4ax.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11> <9st67qFr1lU1@mid.individual.net>`

```
On Wed, 21 Mar 2012 18:11:20 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>COBOL is the ONLY language I know of where zero is NOT in the range of a 
>table.

It's the only computer language I know that way.   But languages
designed to mimic reality (such as English) don't generally have an
address of zero, in a warehouse nor elsewhere.
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 6)_

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2012-03-22T02:10:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20397526.3587.1332407443019.JavaMail.geo-discussion-forums@ynjl17>`
- **In-Reply-To:** `<akbkm7t423a67skl3jpsv616ka61dfjr8h@4ax.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11> <9st67qFr1lU1@mid.individual.net> <akbkm7t423a67skl3jpsv616ka61dfjr8h@4ax.com>`

```
On Wednesday, March 21, 2012 3:40:55 PM UTC-4, Howard Brazee wrote:
[snip]
> But languages
> designed to mimic reality (such as English) don't generally have an
> address of zero, in a warehouse nor elsewhere.

=====
< http://en.wikipedia.org/wiki/Array_data_type >

The 0-based/1-based debate is not limited to just
programming languages. For example, the elevator
button for the ground-floor of a building is
labeled "0" in France and many other countries,
but "1" in the USA.
=====

Unless French is not "designed to mimic reality". <g>
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 7)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2012-03-22T03:19:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3925883.4258.1332411545323.JavaMail.geo-discussion-forums@vbai14>`
- **In-Reply-To:** `<20397526.3587.1332407443019.JavaMail.geo-discussion-forums@ynjl17>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11> <9st67qFr1lU1@mid.individual.net> <akbkm7t423a67skl3jpsv616ka61dfjr8h@4ax.com> <20397526.3587.1332407443019.JavaMail.geo-discussion-forums@ynjl17>`

```
On Thursday, 22 March 2012 09:10:42 UTC, Rick Smith  wrote:
> On Wednesday, March 21, 2012 3:40:55 PM UTC-4, Howard Brazee wrote:
> [snip]
…[14 more quoted lines elided]…
> Unless French is not "designed to mimic reality". <g>

At a guess the reality is that the US refers to STOREYS and everywhere else uses FLOORS.
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2012-03-21T13:55:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<15e61487-d881-4637-9df0-deec6533f346@qg3g2000pbc.googlegroups.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11> <9st67qFr1lU1@mid.individual.net>`

```
On Mar 21, 6:11 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:

> COBOL is the ONLY language I know of where zero is NOT in the range of a
> table.

That seems to be a limitation of your 'know' rather than a limitation
of programming languages.

FORTRAN, SASL, Algol, Algol68R, Pascal* and derivatives, some BASICs
(eg BBC BASIC).



* Pascal can define the range of subscripts allowed for an array, such
as A(100..199) but zero is not allowed in the Pascals that I used
(decades ago).
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-03-22T14:02:07+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9svc0rFd4iU1@mid.individual.net>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11> <9st67qFr1lU1@mid.individual.net> <15e61487-d881-4637-9df0-deec6533f346@qg3g2000pbc.googlegroups.com>`

```
Richard wrote:
> On Mar 21, 6:11 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[10 more quoted lines elided]…
>
Fortran 77 indexes from anything you like, including zero, and negative 
numbers.

It is only a CONVENTION that 1 is used.

I tend to be unconventional... :-)

Algol, I don't know about and will take your word

I understood Pascal could define array bounds (as you noted). I believe that 
definition can include zero, much as for Fortran.

It is a long time since I wrote BASIC but Microsoft Basic (and Visual Basic) 
certainly allow array(0).

Not that I care, you understand :-)...

Pete.
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 7)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2012-03-21T20:52:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f20lm7hlvv7493s9hofnunm2h2ml215acu@4ax.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11> <9st67qFr1lU1@mid.individual.net> <15e61487-d881-4637-9df0-deec6533f346@qg3g2000pbc.googlegroups.com> <9svc0rFd4iU1@mid.individual.net>`

```
On Thu, 22 Mar 2012 14:02:07 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Richard wrote:
>> On Mar 21, 6:11 pm, "Pete Dashwood"
…[27 more quoted lines elided]…
>Not that I care, you understand :-)...


Basic originally certainly did not.  MS implementations have long
supported "OPTION BASE".  IIRC, all IBM PC versions defaulted to 0,
but (at least some) other earlier MS implementations defaulted to 1.
And other implementations never had the option, and were always 1
(Applesoft Basic on the Apple II  - which is MS - was always 1, for
example).  HP-2000 Basic was always 1.  The original Dartmouth Basic
was not.

And I think you may be misremembering about F77.  Arrays were
definitely (only) base 1 in older standards (FIV, for example).  In
(at least) F90 and later you could specify array ranges Pascal style
(IOW, "REAL, DIMENSION(-5:14)"), but I'm 98% certain that was *not* in
F77.  In any event, the default is still base 1 (IOW, if you
"DIMENSION B(100)", accessing B(0) *is* an error).

Obviously particular implementations may have had various extensions.

But the debate between base 0 and base 1 arrays is ancient, and was
often a distinction between "application" and "system" languages.  And
is the basis of one of my favorite CS quotes:

"Should array indices start at 0 or 1? My compromise of 0.5 was
rejected without, I thought, proper consideration." - Stan
Kelly-Bootle
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 8)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2012-03-21T19:02:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e70b0c24-0158-4cda-bf99-0749e8563187@pz2g2000pbc.googlegroups.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11> <9st67qFr1lU1@mid.individual.net> <15e61487-d881-4637-9df0-deec6533f346@qg3g2000pbc.googlegroups.com> <9svc0rFd4iU1@mid.individual.net> <f20lm7hlvv7493s9hofnunm2h2ml215acu@4ax.com>`

```
On Mar 22, 2:52 pm, Robert Wessel <robertwess...@yahoo.com> wrote:
> On Thu, 22 Mar 2012 14:02:07 +1300, "Pete Dashwood"
>
…[52 more quoted lines elided]…
> "DIMENSION B(100)", accessing B(0) *is* an error).

Sorry, but the 2% has the correct answer. According to Balfour and
Marwick 'Programming in Standard FORTRAN 77', 1979 (another in my
overflowing library), it did have specifying the range of subscripts
for an array. You are correct that if only one value is given then the
lower value is 1, as in [real] FORTRAN.

> Obviously particular implementations may have had various extensions.
>
…[6 more quoted lines elided]…
> Kelly-Bootle
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 9)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2012-03-21T21:28:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<la3lm7pq0smceso3lmk4a9ipfaqn1lh699@4ax.com>`
- **References:** `<10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11> <9st67qFr1lU1@mid.individual.net> <15e61487-d881-4637-9df0-deec6533f346@qg3g2000pbc.googlegroups.com> <9svc0rFd4iU1@mid.individual.net> <f20lm7hlvv7493s9hofnunm2h2ml215acu@4ax.com> <e70b0c24-0158-4cda-bf99-0749e8563187@pz2g2000pbc.googlegroups.com>`

```
On Wed, 21 Mar 2012 19:02:47 -0700 (PDT), Richard
<riplin@Azonic.co.nz> wrote:

>On Mar 22, 2:52ï¿½pm, Robert Wessel <robertwess...@yahoo.com> wrote:
>> On Thu, 22 Mar 2012 14:02:07 +1300, "Pete Dashwood"
…[59 more quoted lines elided]…
>lower value is 1, as in [real] FORTRAN.


Indeed.  I found a copy of the F77 standard online:

http://www.fortran.com/F77_std/rjcnf.html

Apparently dimension declarators were added in F77.
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-03-22T22:40:14+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9t0ac0FikmU1@mid.individual.net>`
- **References:** `<10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11> <9st67qFr1lU1@mid.individual.net> <15e61487-d881-4637-9df0-deec6533f346@qg3g2000pbc.googlegroups.com> <9svc0rFd4iU1@mid.individual.net> <f20lm7hlvv7493s9hofnunm2h2ml215acu@4ax.com> <e70b0c24-0158-4cda-bf99-0749e8563187@pz2g2000pbc.googlegroups.com> <la3lm7pq0smceso3lmk4a9ipfaqn1lh699@4ax.com>`

```
Robert Wessel wrote:
> On Wed, 21 Mar 2012 19:02:47 -0700 (PDT), Richard
> <riplin@Azonic.co.nz> wrote:
…[69 more quoted lines elided]…
> Apparently dimension declarators were added in F77.

So, I WASN'T "misremembering"?

Thanks.

When you get to my age, that becomes important... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 7)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2012-03-21T18:52:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0dbea021-279d-4d2e-a69e-3c9032618d2c@lf20g2000pbb.googlegroups.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11> <9st67qFr1lU1@mid.individual.net> <15e61487-d881-4637-9df0-deec6533f346@qg3g2000pbc.googlegroups.com> <9svc0rFd4iU1@mid.individual.net>`

```
On Mar 22, 2:02 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Richard wrote:
> > On Mar 21, 6:11 pm, "Pete Dashwood"
…[14 more quoted lines elided]…
> It is only a CONVENTION that 1 is used.

That is true of Fortran 77, a different language, but FORTRAN in the
previous two decades had the first array item as 1.

> I tend to be unconventional... :-)
>
> Algol, I don't know about and will take your word

I can photocopy a page of the manual if required.

> I understood Pascal could define array bounds (as you noted). I believe that
> definition can include zero, much as for Fortran.

You mean 'much as in Fortran _77_'.

ISO Pascal does allow any subscript range, including negative, but
that is a different language from 'Pascal' as created by Wirth.

> It is a long time since I wrote BASIC but Microsoft Basic (and Visual Basic)
> certainly allow array(0).

'BASIC' is not one language but is a class of, often quite different,
languages that have vague similarities. Which is why I said 'some'.

Some versions of MS BASIC and DRI Personal BASIC have an 'OPTION BASE'
statement which can set the minimum subscript to 0 or 1 as required.

JEAN is another language with subscripts starting at 1. This was an
interactive language for ICL 1900 series and GEORGE* III from the
1960s (or possibly, like the other George III, from the 1760s). Yes, I
still have a manual for that too, alongside my PLAN and PERT manuals.



* General ORGanizational Environment.

> Not that I care, you understand :-)...
>
> Pete.
> --
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 7)_

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2012-03-22T13:18:09+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4f6b1876$0$284$14726298@news.sunsite.dk>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11> <9st67qFr1lU1@mid.individual.net> <15e61487-d881-4637-9df0-deec6533f346@qg3g2000pbc.googlegroups.com> <9svc0rFd4iU1@mid.individual.net>`

```
Pete Dashwood wrote:

> Richard wrote:
>> On Mar 21, 6:11 pm, "Pete Dashwood"
…[19 more quoted lines elided]…
> Algol, I don't know about and will take your word

I still remebers the Algol 60 course in 1971 on an ELX-8 computer where
array structures were shows like 
  array s [-2:10] ;
a construct at that time not possible with the to me available Fortran
compiler (like Algol also available on a Siemens 4004/150).
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 7)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2012-03-22T10:27:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2gdmm7psr8srlm9uu1toh7b875f3p54i0i@4ax.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11> <9st67qFr1lU1@mid.individual.net> <15e61487-d881-4637-9df0-deec6533f346@qg3g2000pbc.googlegroups.com> <9svc0rFd4iU1@mid.individual.net>`

```
On Thu, 22 Mar 2012 14:02:07 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Richard wrote:
>> On Mar 21, 6:11 pm, "Pete Dashwood"
…[29 more quoted lines elided]…
>Pete.

Here's another wrinkle.  I sometimes need to use DYL280 to generate
reports or other things.  When using a tabled area, to see the first
occurrence you must set the index field to 0.  In Easytrieve, which I
also use at time, the first occurrence is index 1.

To me zero makes more sense but that's because I started life as an
IBM Assembler programmer and the first position, first occurrence just
about first anything is 0.

Regards,
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

_(reply depth: 5)_

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2012-03-22T02:27:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33441847.2465.1332408476774.JavaMail.geo-discussion-forums@ynlt15>`
- **In-Reply-To:** `<9st67qFr1lU1@mid.individual.net>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <10973219.2055.1331963793982.JavaMail.geo-discussion-forums@yncd8> <85da5c37-415d-4d46-a73f-4770265517d6@n9g2000pbb.googlegroups.com> <18057858.1422.1332270259317.JavaMail.geo-discussion-forums@ynv11> <9st67qFr1lU1@mid.individual.net>`

```
On Wednesday, March 21, 2012 1:11:20 AM UTC-4, Pete Dashwood wrote:
[snip]
> COBOL is the ONLY language I know of where zero is NOT in the range of a 
> table.

< http://en.wikipedia.org/wiki/Comparison_of_programming_languages_(array) >
provides information on a number of languages,
including COBOL. I found the page a couple weeks
ago and, as is so often the case, the information
for COBOL is incomplete or erroneous.

In the "Array system cross-reference list":
Specifiable index type should be 'no'
Multidimensional should be 'array of array'
Vectorized operations should be 'some using Intrinsic Functions'
```

#### ↳ Re: Dinosaur Alert - Error Issue

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2012-03-17T02:47:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y5Kdnbwsl4Th3PnSnZ2dnUVZ5hydnZ2d@giganews.com>`
- **In-Reply-To:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au>`

```
On 3/16/2012 11:12 PM, Paul Richards wrote:
> I have a program which compiles correctly and runs fine using Net
> Express.
…[48 more quoted lines elided]…
>

If it were me, I would try deleting the line that sets tbl-index to zero 
and then recoding the loop as follows:

  perform varying tbl-index from 1 by 1
          until   tbl-index > artist-cnt
    read artist-file next
    set tbl-index up by 1
    move  artist-rec to tblartist-rec(tbl-index)
  end-perform
  set tbl-index to 1.

I think that might work in both compilers.
```

##### ↳ ↳ Re: Dinosaur Alert - Error Issue

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2012-03-17T12:40:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf7c8584-930b-407d-a8e7-d93e1c7bd37f@pg6g2000pbb.googlegroups.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <y5Kdnbwsl4Th3PnSnZ2dnUVZ5hydnZ2d@giganews.com>`

```
On Mar 17, 8:47 pm, Arnold Trembley <arnold.tremb...@att.net> wrote:
> On 3/16/2012 11:12 PM, Paul Richards wrote:
>
…[62 more quoted lines elided]…
>     read artist-file next
          AT END ...

          NOT AT END
>             set tbl-index up by 1

              this will double step as the PERFORM will also
              increment BY 1

>             move  artist-rec to tblartist-rec(tbl-index)
      END-READ
>   end-perform
>   set tbl-index to 1.
…[3 more quoted lines elided]…
> --http://www.arnoldtrembley.com/
```

#### ↳ Re: Dinosaur Alert - Error Issue

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-03-18T02:21:29+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9sjherFuv1U1@mid.individual.net>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au>`

```
Paul Richards wrote:
<snip>>
> *--- dynamic table
> linkage section.
…[6 more quoted lines elided]…
> ..........
<snip>

Apart from the very sound advice you have already received about recursion 
and NOT setting an index to zero, there was something else that struck me 
about this code.

I seem to recall more than one flavour of COBOL not allowing OCCURS at an 01 
level.

Even if your particular flavour DOES allow it, it might be best to avoid 
it...

Pete.
```

#### ↳ Re: Dinosaur Alert - Error Issue

- **From:** Doug Miller <doug_at_milmac_dot_com@example.com>
- **Date:** 2012-03-17T14:15:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XnsA019686761C10dougmilmaccom@88.198.244.100>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au>`

```
"Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au> wrote in 
news:Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au:

> I have a program which compiles correctly and runs fine using Net
> Express.
…[21 more quoted lines elided]…
>  set tbl-index to 0            *> ERROR HERE <<<<<<

I have no experience with this particular compiler, but it looks to me as though it wants the 
value of an index to be a positive integer.
> 
>  perform artist-cnt times                                        
…[4 more quoted lines elided]…
>  set tbl-index to 1.           *> reset index for display start  

Try this instead:

populate-memory-table.         
 move eof-false to eof-status 
 set tbl-index to 1    	    	*> Note set to 1 instead of 0
 
 perform artist-cnt times                                        
   read artist-file next                                         
   move  artist-rec to tblartist-rec(tbl-index)   *> Note order of these two
   set tbl-index up by 1                                         *> statements is reversed
 end-perform                                                     
 set tbl-index to 1.
```

##### ↳ ↳ Re: Dinosaur Alert - Error Issue

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2012-03-17T12:43:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9d72c19-343a-49ea-bfe0-5fbfb24501b3@gj7g2000pbc.googlegroups.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <XnsA019686761C10dougmilmaccom@88.198.244.100>`

```
On Mar 18, 3:15 am, Doug Miller <doug_at_milmac_dot_...@example.com>
wrote:
> "Paul Richards" <paulricha...@XXXNOSPAMiinet.net.au> wrote innews:Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au:
>
…[54 more quoted lines elided]…
>    set tbl-index up by 1                *> statements is reversed

This will increment tbl-index to be greater than artist-cnt and will
give a bound check error (if checking is on).

>  end-perform
>  set tbl-index to 1.
```

#### ↳ Re: Dinosaur Alert - Error Issue

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2012-03-17T12:12:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f690386-3f6f-42eb-b359-10927d1c102d@gj7g2000pbc.googlegroups.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au>`

```
On Mar 17, 5:12 pm, "Paul Richards"
<paulricha...@XXXNOSPAMiinet.net.au> wrote:
> I have a program which compiles correctly and runs fine using Net
> Express.
…[5 more quoted lines elided]…
> file:

No, you are not creating a dynamic table, at least not in MF 3.x.

An OCCURS 1 TO 250 will create a fixed memory array of 250 items. The
'depending on' will be used to set a limit for some operations such as
SEARCH and MOVE.

> *--- dynamic table
>  linkage section.
…[6 more quoted lines elided]…
> ..........

In LINKAGE SECTION no memory area will be created (in MF 3.1) by the
compiler. It is usual that another program will have an area in their
working-storage and will pass it to this program as a parameter to a
CALL. There may be other means of creating a memory area that this
will map to, such as using a system call to create a memory area then
using SET to point dataList at that. This is not valid '85 COBOL but
is a MF extension in this compiler.

An OCCURS on an 01 level is wrong. An 01 is a record area, OCCURS can
only be on a group or elementary item. Some compilers will process
this as if it were a group, others may not.

Both to comply and logically the OCCURS should be on tblArtist-rec.

That is to say you are not creating 250 '01 records', but are creating
one '01 array record' that contains 250 items.


> The error occurs when the compiler parses the populating code:
>
…[17 more quoted lines elided]…
>  Recursive Cobol Call is illegal"

Because it is in LINKAGE SECTION then it won't exist unless:

a) it has been passed as a CALL parameter from a program where it does
exist, and this is specified on the PROCEDURE DIVISION header.

or b) some other means has been used to create it, such as a system
call to create the memory area.

It is likely that tbl-index does not exist and thus the compiler
cannot determine what it is.

> Any ideas why my old COBOL compiler produces these errors and the
> 'modern' one doesn't? Can I recode this to avoid the error?

Newer compilers have more features. It may be that MF 3.1 DOS compiler
does not automatically create tbl-index because it is in LINKAGE but
later compilers 'fixed' this issue.


> This is a personal hobby/interest project so I'd appreciate not
> receiving admonishments for 'living in the past' etc :-)
```

#### ↳ Re: Dinosaur Alert - Error Issue

- **From:** "Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au>
- **Date:** 2012-03-17T20:45:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XqqdnR3e68CBo_jSnZ2dnUVZ_rqdnZ2d@westnet.com.au>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au>`

```
Gentlemen: thanks for your helpful comments.

As far as SETting tbl-index is concerned, both Rick's and Doug's
suggestions will allow the program to correctly compile without errors
under version 3.1.54 but I am then getting a run time error 163
'Illegal character in numeric field'.

Again, I am not getting this error when running the program via the IDE
in Net Express.

With respect to the general design and Richard's final comments, I used
this example to base my approach on

http://itsacobolworld.blogspot.com.au/2010/06/declarative-sorting-of-dyn
amically.html (although I'm not sorting the table contents)

and used the "CBL_ALLOC_MEM" routine as shown in the example, hence the
use of a Linkage section.

If what Richard is saying ("No, you are not creating a dynamic table,
at least not in MF 3.x.") is accurate then I might just as well code
for a fixed table since I am not dynamically claiming and then
releasing any memory.
```

##### ↳ ↳ Re: Dinosaur Alert - Error Issue

- **From:** "Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au>
- **Date:** 2012-03-17T21:22:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ErCdnQIQQfBq2_jSnZ2dnUVZ_omdnZ2d@westnet.com.au>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <XqqdnR3e68CBo_jSnZ2dnUVZ_rqdnZ2d@westnet.com.au>`

```
Paul Richards wrote:

> I am then getting a run time error 163
> 'Illegal character in numeric field'

I don't think this has anything to do with the tbl-index issue on
further reflection.
```

##### ↳ ↳ Re: Dinosaur Alert - Error Issue

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2012-03-17T21:08:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d1725d54-0fc8-43f6-9f5a-69265aef283d@qg3g2000pbc.googlegroups.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <XqqdnR3e68CBo_jSnZ2dnUVZ_rqdnZ2d@westnet.com.au>`

```
On Mar 18, 2:45 pm, "Paul Richards"
<paulricha...@XXXNOSPAMiinet.net.au> wrote:
> Gentlemen: thanks for your helpful comments.
>
…[3 more quoted lines elided]…
> 'Illegal character in numeric field'.

The error will give a location. Compile the program with REF and
COPYLIST to a .int (OPT(0)) and run this. If you are compiling to .gnt
or .exe then you will need to get an ASMLIST with source to relate the
location from the error line to the source in the ASM list.

> Again, I am not getting this error when running the program via the IDE
> in Net Express.
…[13 more quoted lines elided]…
> releasing any memory.

The OCCURS 1 TO 250 does not create a dynamic table when it is in
WORKING-STORAGE, it creates a fixed length table of 250.

However it is in LINKAGE-SECTION and the (MF only) CBL_ALLOC_MEM
(which you hadn't mentioned before) will create this at run-time, but
I don't think that tbl-index is being created.
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue

- **From:** "Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au>
- **Date:** 2012-03-18T00:30:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<asCdnZPSLOVD7_jSnZ2dnUVZ_t-dnZ2d@westnet.com.au>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <XqqdnR3e68CBo_jSnZ2dnUVZ_rqdnZ2d@westnet.com.au> <d1725d54-0fc8-43f6-9f5a-69265aef283d@qg3g2000pbc.googlegroups.com>`

```
Richard wrote:

> On Mar 18, 2:45ï¿½pm, "Paul Richards"
> <paulricha...@XXXNOSPAMiinet.net.au> wrote:
…[18 more quoted lines elided]…
> >
http://itsacobolworld.blogspot.com.au/2010/06/declarative-sorting-of-dyn
> > amically.html (although I'm not sorting the table contents)
> > 
…[13 more quoted lines elided]…
> I don't think that tbl-index is being created.

Richard: thanks for your feedback. Sorry for not mentioning
CBL_ALLOC_MEM ;-). I'll follow your suggestion re the REF/COPYLIST and
do some further analysis.
```

##### ↳ ↳ Re: Dinosaur Alert - Error Issue

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2012-03-19T22:12:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d638157a-c5cf-4d69-a669-be946595617f@o3g2000pbt.googlegroups.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <XqqdnR3e68CBo_jSnZ2dnUVZ_rqdnZ2d@westnet.com.au>`

```
On Mar 18, 2:45 pm, "Paul Richards"
<paulricha...@XXXNOSPAMiinet.net.au> wrote:
> Gentlemen: thanks for your helpful comments.

> With respect to the general design and Richard's final comments, I used
> this example to base my approach on
>
> http://itsacobolworld.blogspot.com.au/2010/06/declarative-sorting-of-dyn
> amically.html (although I'm not sorting the table contents)

I looked at that example and have these comments:

       01 variants occurs 1 to 1000 depending on variant-count
                   ascending key is sku
                   indexed   by jump-start-index.
           03 sku  binary-long.
           03 decr pic x(20).

In ANS'85 OCCURS is not allowed on 01 or 77 level. MF allow this as
[confusing] non-standard item.

In particular an 01 is a record area so one may expect it to unroll
as:

      01  variants(1).
          03 sku(1) ..
          03 decr(1) ...
      01  variants(2).
          03 sku(2) ..
          03 decr(2) ...
      01  ...

But there may be padding between 01 level items. Adding a 02 to take
the occurs makes it standard and more clear (IMHO).

       01 variants.
           02 SKU-Items occurs 1 to 1000 depending on variant-count
                   ascending key is sku
                   indexed   by jump-start-index.
             03 sku  binary-long.
             03 decr pic x(20).

Here is where confusion could occur:

           move 10 to variant-count
           set mem-ln to length of variants

Setting variant-count to 10 gives 10 sku and decr. Is the 'length of'
the data area of 'variants' refer to the total size of the table or of
one occurs ?  In fact in the original it does give 24, but I would
change this to:

           set mem-ln to length of SKU-Items(1)

to make this explicit. We see inconsistencies appear in:

           set address of variants(1) to mem-ptr

which is clearer as:

           set address of variants   to mem-ptr

The SORT also needs changing to SORT SKU-Items.
```

##### ↳ ↳ Re: Dinosaur Alert - Error Issue

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2012-03-19T23:20:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f7136c9-39ea-45c8-94f0-67761aec7458@oq7g2000pbb.googlegroups.com>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <XqqdnR3e68CBo_jSnZ2dnUVZ_rqdnZ2d@westnet.com.au>`

```
On Mar 18, 2:45 pm, "Paul Richards"
<paulricha...@XXXNOSPAMiinet.net.au> wrote:
> Gentlemen: thanks for your helpful comments.
>
…[6 more quoted lines elided]…
> in Net Express.

In MF 3.1 the default is that memory is initialized to spaces. The
SPZERO compiler option will cater for display numeric items containing
spaces to be treated as zero, _BUT_ this only works for 'native' code.
ie .gnt or .exe, compiled with OPT(1) or OPT(2). As this OPT() only
applies in the generate phase then it won't be used when running the
program from the editor or animator, or when the compiler output is
a .int or equivalent.

The Net Express version may well apply SPZERO, or some equivalent, all
the time.

You may be using a numeric data item when it has non-numeric
characters. This may be because you are, for example, ADDing to a W-S
item that does not have a VALUE clause nor has it been initialized.

Or you are reading a data item from a file that has non-numeric
characters in a numeric field. eg "   123456" instead of "000123456"
when the field is PIC S9(7)V99.

Ensure that W-S numeric fields have a VALUE clause or MOVE ZERO to
them before using them.

For all input use a IF NUMERIC test. It is necessary to do this on a
PIC X() redefines or group field - you can't do IF NUMERIC on a
NUMERIC field in ANS'85.

> With respect to the general design and Richard's final comments, I used
> this example to base my approach on
…[10 more quoted lines elided]…
> releasing any memory.

You are creating the table 'dynamically' in that you are creating it
at run-time rather than compile time, but it is not a 'dynamic table'
because it will not change the physical size by changing the value of
the depending on.  If you wanted it larger than the original size it
was created at you would have to CBL_FREE_MEM and then CBL_ALLOC_MEM
with a larger size, and that would lose all the data in it.
```

#### ↳ Re: Dinosaur Alert - Error Issue - SOLVED

- **From:** "Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au>
- **Date:** 2012-03-19T20:04:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HOydnYR8UOYCSvrSnZ2dnUVZ_qidnZ2d@westnet.com.au>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au>`

```
Paul Richards wrote:

> I have a program which compiles correctly and runs fine using Net
> Express.
…[46 more quoted lines elided]…
> TIA

I think the cause of this problem had nothing to do with the apparent
symptom. As is so often the case, the solution was straightforward. My
data and index files are in a WORK folder. I realised that the
Professional COBOL editor was defaulting to the MFCOBOL\EXEDLL folder.
Since I was running the prgram from within the editor, I guess that
when I was using the function that required the dynamic memory
allocation and reading of data from a file the program could not find
the file (since it must have been 'looking' in EXEDLL) and this sparked
off a series of strange conditions which the compiler attempted to
analyse and provide messages for. My analysis may, of course, be
totally off the mark but the solution below has solved the issue.

The solution was,in my batch file which sets up the PROCO environment,
to issue a final 'change directory' command to the WORK folder. After
this the program works as it should and there is, therefore, no
apparent conflict with the Net Express compilation.

It also means that 'set tbl-index to 0' is a valid statement in version
3.1.54 since I reverted to my original coding and produced the expected
results.

Thanks once again for the advice received earlier.
```

##### ↳ ↳ Re: Dinosaur Alert - Error Issue - SOLVED

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2012-03-20T16:09:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13711866.327.1332284940959.JavaMail.geo-discussion-forums@yneo2>`
- **In-Reply-To:** `<HOydnYR8UOYCSvrSnZ2dnUVZ_qidnZ2d@westnet.com.au>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <HOydnYR8UOYCSvrSnZ2dnUVZ_qidnZ2d@westnet.com.au>`

```
On Monday, March 19, 2012 9:04:31 PM UTC-4, Paul Richards wrote:
[snip]

> It also means that 'set tbl-index to 0' is a valid statement in version
> 3.1.54 since I reverted to my original coding and produced the expected
> results.

That is an invalid conclusion! As I demonstrated
elsewhere, Micro Focus 3.2 (with COBOL 85 flagging)
does flag such a statement as an error. In reaching
your conclusion, you failed to account for the
possibility that Micro Focus 3.1 was not in
conformance with standard COBOL for that variant
of the SET statement. 

IOW 'set tbl-index to 0' is invalid in COBOL 85
and the failure of any implementation (claiming
conformance to COBOL 85) to flag the statement
cannot make the statement valid.
```

###### ↳ ↳ ↳ Re: Dinosaur Alert - Error Issue - SOLVED

- **From:** "Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au>
- **Date:** 2012-03-21T01:46:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ku2dnd4f4rmq5PTSnZ2dnUVZ_rCdnZ2d@westnet.com.au>`
- **References:** `<Ad6dnfOqn9GskvnSnZ2dnUVZ_umdnZ2d@westnet.com.au> <HOydnYR8UOYCSvrSnZ2dnUVZ_qidnZ2d@westnet.com.au> <13711866.327.1332284940959.JavaMail.geo-discussion-forums@yneo2>`

```
Rick Smith wrote:

> On Monday, March 19, 2012 9:04:31 PM UTC-4, Paul Richards wrote:
> [snip]
…[16 more quoted lines elided]…
> cannot make the statement valid.

I stand corrected re ANS85. However as this is a personal hobby project
I am not really concerned if I use MF 'extensions' - the program now
works as I intended - and I am not concerned with portability.

Thanks.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
