[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# TelCo "programming challenge" (update)

_9 messages · 6 participants · 2004-05_

---

### TelCo "programming challenge" (update)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-05-12T03:38:41+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<5%goc.16938$V97.10351@newsread1.news.pas.earthlink.net>`

```
I have finished my (initial?) fully functional test program in COBOL.  I would
be interested in input on how to "optimize" it. (What I did, has INCREDIBLY
"bad" mixtures of data types - but was "easy" for me to program on-the-fly).

The following is what I sent to the poster of the "challenge"

***

Mike,
The following are my current timing results (large test input file). I believe
it meets all the requirements in your "specification" at:

    http://www2.hursley.ibm.com/decimal/telco.html

These timings were created using the Fujitsu compiler. The same source code
would compile with Micro Focus compiler. It would require *minimal* changes
(mostly indentation and comment indicators) to compile with IBM's VisualAge
COBOL compiler (or even your Enterprise mainframe compiler).

Timing with calculations:
    Start-Time:22:18:39/64
    End-Time:22:19:02/72

Timings "skipping" calculations:
    Start-Time:22:22:52/62
    End-Time:22:23:00/93

***

The COBOL source code is available "online" at:

    http://home.netcom.com/~wmklein/dox/TELCO.txt

NOTE WELL:
    I have done ALMOST nothing to "optimize" this program. The "mixture" of
various numeric data formats is "bound" to cause performance degradation. It
could also be modified QUITE easily to handle the "binary" input file.

Please let me know if this is the type of information you want - or if you
want/need anything else.
```

#### ↳ Re: TelCo "programming challenge" (update)

- **From:** "David Frank" <dave_frank@hotmail.com>
- **Date:** 2004-05-12T12:48:38+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<G2poc.546673$B81.10316696@twister.tampabay.rr.com>`
- **References:** `<5%goc.16938$V97.10351@newsread1.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:5%goc.16938$V97.10351@newsread1.news.pas.earthlink.net...
>I have finished my (initial?) fully functional test program in COBOL.  I 
>would
…[50 more quoted lines elided]…
>

Interesting,  8.3 sec for file in/out without calculations.

I have some timings using the binary version of the million values file.
Below timings are for my 830Mhz pentium just reading the file,
(no file output yet)

totsec= 1.60 total= 0.00000000000000        no calculations
totsec= 1.64 total= 1011714.90549671568442   + dp calc        (no rounding)
totsec= 2.30 total= 1011714.90549560400000   + quad/decimal  calc     "

Some observations..

1. Time for double precision real calculations = .04 sec
2. Time for   quad precision real calculations  = .70 sec

It takes approx 16x longer to do calculations using quad precision.

I expect this ratio to stay about the same even if  rounding routines were
available for dp run and compared to the final version of my million call
program run which WILL have rounding added.

Below is my Fortran dp test program that produced outputs 1,2 above.
The quad test program is identical expect for dp declarations changed to
quad.

! ---------------------
PROGRAM Telco_Million_Calls
use Decimal
implicit none
real(8) :: brate = .0013d0
real(8) :: drate = .00894d0
real(8) :: btax  = .0675d0
real(8) :: dtax  = .0341d0
real(8) :: p, t
integer     :: ignore, time, time1(8), time2(8)
integer(1)  :: tb(4); equivalence (tb,time)
integer     :: i
real        :: totsec
character(50) :: stotal

open (1,file='expon180.1e6',form='binary')    ! 8-byte integers

call date_and_time (values=time1)   ! benchmark time start

t = 0.0
do                     !  input 1 big-endian 4 byte integer
   read (1,end=101,err=102) ignore, (tb(i),i=4,1,-1)

!!! cycle    ! find total time to read file, no processing

   if (iand(time,1) == 0) then      ! Local call
      p = time*brate
      t = t + p + p*btax
   else
      p = time*drate
      t = t + p + p*btax +p*dtax
   end if
end do

101 call date_and_time (values=time2)   ! benchmark time stop

totsec = (time2(6)*60 + time2(7) + time2(8)/1000.) & ! mm:ss.sss
       - (time1(6)*60 + time1(7) + time1(8)/1000.)

write (*,'(a,f0.2,a,f0.14)') 'totsec= ',totsec, ' total= ',t
stop

102 write (*,*) 'error reading data file' ; stop
END PROGRAM Telco_Million_Calls
```

##### ↳ ↳ Re: TelCo "programming challenge" (update)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-05-12T17:10:19+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<%Tsoc.17411$V97.4707@newsread1.news.pas.earthlink.net>`
- **References:** `<5%goc.16938$V97.10351@newsread1.news.pas.earthlink.net> <G2poc.546673$B81.10316696@twister.tampabay.rr.com>`

```
Just out of curiosity, on what platform were these timing results?  (Mine was
under Windows XP - with a Pentium processor).

And as I indicated earlier, my source code was NOT optimized for performance.
(I may or may not try to do that still).

FYI - the original specifications talk about "file buffering".  As far as I know
most (probably all) actual "telephone billing" applications run on systems with
excellent file buffering - which WindowsXP does NOT.  I would expect
SIGNIFICANTLY less I/O time in such environments.

P.S.  I would expect better calculation performance on WindowsXP if I switched
to "little-endian" binary - which I may (or may not) try.
```

###### ↳ ↳ ↳ Re: TelCo "programming challenge" (update)

- **From:** "David Frank" <dave_frank@hotmail.com>
- **Date:** 2004-05-12T17:57:56+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<EAtoc.547227$B81.10344603@twister.tampabay.rr.com>`
- **References:** `<5%goc.16938$V97.10351@newsread1.news.pas.earthlink.net> <G2poc.546673$B81.10316696@twister.tampabay.rr.com> <%Tsoc.17411$V97.4707@newsread1.news.pas.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:%Tsoc.17411$V97.4707@newsread1.news.pas.earthlink.net...
> Just out of curiosity, on what platform were these timing results?  (Mine 
> was
> under Windows XP - with a Pentium processor).
>

XP home  (with a OLD 833mhz pentium as I said.)
```

###### ↳ ↳ ↳ Re: TelCo "programming challenge" (update)

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-05-13T12:37:27+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<b_Joc.7026$eH1.3571644@newssvr28.news.prodigy.com>`
- **References:** `<5%goc.16938$V97.10351@newsread1.news.pas.earthlink.net> <G2poc.546673$B81.10316696@twister.tampabay.rr.com> <%Tsoc.17411$V97.4707@newsread1.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:%Tsoc.17411$V97.4707@newsread1.news.pas.earthlink.net...
> FYI - the original specifications talk about "file buffering".  As far as
I know
> most (probably all) actual "telephone billing" applications run on systems
with
> excellent file buffering - which WindowsXP does NOT.  I would expect
> SIGNIFICANTLY less I/O time in such environments.

Actually, all Windows versions offer excellent file buffering if you access
files using "memory-mapped file objects."

Not that it's necessary all that often because you can load entire files to
memory fairly easily since you get 2 Gb of virtual RAM per process.

Maybe when I do this challenge I'll do it three ways:
- One record at a time,  which will use whatever 'default' buffering is
available. (Although my BASIC compiler allows me to specify the equivalent
of "blocks" which will return multiple records per physical I-O; so maybe I
will make "block size" an option).
- Load entire file to memory and treat as a table
- Use memory-mapped files and access records by address.


MCM
```

###### ↳ ↳ ↳ Re: TelCo "programming challenge" (update)

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-05-13T12:18:13-07:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<217e491a.0405131118.f3c2896@posting.google.com>`
- **References:** `<5%goc.16938$V97.10351@newsread1.news.pas.earthlink.net> <G2poc.546673$B81.10316696@twister.tampabay.rr.com> <%Tsoc.17411$V97.4707@newsread1.news.pas.earthlink.net> <b_Joc.7026$eH1.3571644@newssvr28.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote

> Not that it's necessary all that often because you can load entire files to
> memory fairly easily since you get 2 Gb of virtual RAM per process.

Business systems are usually used by the whole business.  This means
that several people will have access to shared data.  Loading a file
into one machine's RAM for any purpose other than just reading it
means that it is no longer shared.
```

#### ↳ Re: TelCo "programming challenge" (update)

- **From:** "David Frank" <dave_frank@hotmail.com>
- **Date:** 2004-05-14T07:52:29+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<1V_oc.551141$B81.10513543@twister.tampabay.rr.com>`
- **References:** `<5%goc.16938$V97.10351@newsread1.news.pas.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:5%goc.16938$V97.10351@newsread1.news.pas.earthlink.net...
> The following is what I sent to the poster of the "challenge"
>
…[13 more quoted lines elided]…
>on-the-fly).

>The following is what I sent to the poster of the "challenge"

>Mike,
>The following are my current timing results (large test input file). I 
>believe
>it meets all the requirements in your "specification" at:

>   http://www2.hursley.ibm.com/decimal/telco.html

>These timings were created using the Fujitsu compiler. The same source code
>would compile with Micro Focus compiler. It would require *minimal* changes
>(mostly indentation and comment indicators) to compile with IBM's VisualAge
>COBOL compiler (or even your Enterprise mainframe compiler).

>Timing with calculations:
>    Start-Time:22:18:39/64
>    End-Time:22:19:02/72

>Timings "skipping" calculations:
>    Start-Time:22:22:52/62
>    End-Time:22:23:00/93

>The COBOL source code is available "online" at:

>    http://home.netcom.com/~wmklein/dox/TELCO.txt

>NOTE WELL:
>    I have done ALMOST nothing to "optimize" this program. The "mixture" of
>various numeric data formats is "bound" to cause performance degradation. 
>It
>could also be modified QUITE easily to handle the "binary" input file.

>Please let me know if this is the type of information you want - or if you
>want/need anything else.

>Bill Klein
> wmklein <at> ix.netcom.com

Well to chime in for my fav language Fortran, below is a scorecard
that needs more inputs from fav language adherents..

1. Fortran 25 statements   3  sec to execute
2. Cobol  83 statements  23  sec to execute
3. C           ?
4. C#         ?
5. Java       ?
6. C++       ?
7. PL/I       ?

! ---------------------
PROGRAM Telco_Million_Calls  ! from expon180.1e6 file
use DollarCents
real(8)    :: brate = 0.13d0,   drate = 0.894d0
real(8)    :: btax  = 0.0675d0, dtax  = 0.0341d0
integer(8) :: time, p, b, d, sumb, sumd, sumt
integer(1) :: tb(8); equivalence (tb,time)

open (1,file='expon180.1e6',form='binary')  ! 8-byte integers
sumb = 0.0 ; sumd = 0.0 ; sumt = 0.0
do
   read (1,end=101) (tb(i),i=8,1,-1) ! big-endian 8-byte integer
   if (iand(time,1) == 0) then                ! Local call
      p = Mul(time,brate,bankers) ; b = Mul(p,btax)
      sumb = sumb +b ; sumt = sumt+p+b
   else                                       ! Distance call
      p = Mul(time,drate,bankers) ; b = Mul(p,btax) ; sumb = sumb+b
      d = Mul(p,dtax) ; sumd = sumd +d ; sumt = sumt+p+b+d
   end if
end do
101 write (*,'(a,f10.2)') 'SumT = ', sumt/1D2, &
                          'SumB = ', sumb/1D2, &
                          'SumD = ', sumd/1D2
END PROGRAM Telco_Million_Calls
Outputs:
SumT = 1004737.58
SumB =   57628.30
SumD =   25042.17
```

##### ↳ ↳ Re: TelCo "programming challenge" (update)

- **From:** "Mike Cowlishaw" <mfc@uk.ibm.com>
- **Date:** 2004-05-14T11:15:22+01:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<c8267u$h1u$1@news.btv.ibm.com>`
- **References:** `<5%goc.16938$V97.10351@newsread1.news.pas.earthlink.net> <1V_oc.551141$B81.10513543@twister.tampabay.rr.com>`

```
David Frank wrote:

[sigh there seems to be an almost identical threads in c.l.fortran]

> Well to chime in for my fav language Fortran, below is a scorecard
> that needs more inputs from fav language adherents..
>
> 1. Fortran 25 statements   3  sec to execute

[so here's an almost identical answer.  sorry, readers...]

Hi .. yes, by using integers and manual scaling, it is easy to
write a special-purpose piece of code for this that is very
short and fast.

But that's missing the point of the benchmark  The benchmark
is intended to estimate the overhead of the calculations when
they are done in a straightforward and maintainable way.

The total speed is uninteresting, as is the size of the code
(and for readability Rexx probably wins).  As someone pointed
out, the full application would be more complex and work
on much larger quantities of data.  What the benchmark
does appear to do is match the behaviour of those large
real applications in the one respect it is intended to measure.

Mike
```

###### ↳ ↳ ↳ Re: TelCo "programming challenge" (update)

- **From:** "Bill Turner, WB4ALM" <Abracadabra-magic-wb4alm@arrl.net>
- **Date:** 2004-05-14T19:57:40+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<Uw9pc.545$SZ4.348@newsread2.news.pas.earthlink.net>`
- **In-Reply-To:** `<c8267u$h1u$1@news.btv.ibm.com>`
- **References:** `<5%goc.16938$V97.10351@newsread1.news.pas.earthlink.net> <1V_oc.551141$B81.10513543@twister.tampabay.rr.com> <c8267u$h1u$1@news.btv.ibm.com>`

```
Mike Cowlishaw wrote:
> David Frank wrote:
> 
…[28 more quoted lines elided]…
> 

"...The benchmark is intended to estimate the overhead of the
  calculations when they are done in a straightforward and
  maintainable way."

"...What the benchmark does appear to do is match the behaviour of those 
large real applications in the one respect it is intended to measure."

- - -

I like your statements, Mike - Over the years or my employment, I have 
observed many people not understanding what a benchmark is or does... 
...often with a frightening misuse of the results.

As part of a "challenge" of why you MUST understand what the benchmark 
is measuring, I allowed a vender once (many years ago) to make changes 
to a major benchmarking suite or programs that my employer used to 
verify the "actual" processing speed of mainframe systems handling OUR 
processing job mix.

The change was simple and did not change any of the processing modules 
in the test suite. (The file blocksizes were mearly upped from the 
previous standard of 8k blocking to a newer one of 27k (half-track 
blocking) --- which just happened to match our guideline for optimium 
disk file blocksizes.)

As a result of this minor external change, a non-IBM monolithic machine 
with one processing engine seemingly out-performed the 8-engine IBM 
top-of-the-line system that we were using at that time. In fact, the 
Non-IBM system was rated at 18 to 20 times faster than our fastest IBM 
systems --- something that we knew just couldn't be true...

As it turned out, the seemingly "innocent" change to the benchmark JCL 
caused some cache memory and an "instruction pipeline" to be constantly 
flushed on the IBM system, while the single engine system gained a hugh 
advantage because of the way it used its smaller cache memory with it's 
one processing engine.


Ever since then, I have been very careful before beleiving "my thingy
is bigger (or faster) then your thingy" type claims - especially in the 
Computer Industry.

Many computer hardware nuts are aware of the fisco that occurred a few 
years back, when one of the PC Video Card manufacturers modified the 
hardware on their Video Card to exploit the "standard" benchmark test,
by storing more of the "polygon" requests onboard while deciding how
to best perform the requested operations.   The modified card did run 
the benchmark tests far faster then all of it's competitors, but if I 
recall correctly, it did not really perform very well when doing real 
world gaming graphics....

As has been said often  "Ceteris paribus - Caveat venditor".

/s/ Bill Turner, wb4alm
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
