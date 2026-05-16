[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# first conversion program: disaster

_66 messages · 22 participants · 2001-12 → 2002-01_

---

### first conversion program: disaster

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-22T23:34:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c250264.895577@news.libero.it>`

```
I have studied Cobol the whole day.

My purpose is to write a conversion routine that will trasform weird
COMP-3 records in plain old ASCII data.

As I have no idea how to write COMP-3 data, I began doing the
opposite, i.e. converting ASCII numbers into their COMP-3
counterpart.

The result is disappointing to say the least.

Starting data (in 1.dat) was:

123456789
123456789
123456789
123456789
123456789

what I got is:

12345
9    
12345
9    
12345
9    
12345
9    
12345
9    
12345
9    

I assume I did something wrong... :)

Any help  ? (the code is attached...)

Thank you

Duilio Foschi


 IDENTIFICATION DIVISION.
 PROGRAM-ID.    CONVERT-DATA.
 AUTHOR.        DUILIO FOSCHI.

 ENVIRONMENT DIVISION.
 INPUT-OUTPUT SECTION.
 FILE-CONTROL.

        SELECT IN-FILE ASSIGN TO '1.DAT'
           ORGANIZATION IS LINE SEQUENTIAL.
        SELECT OUT-FILE ASSIGN TO '2.DAT'
           ORGANIZATION IS LINE SEQUENTIAL.

 DATA DIVISION.
 FILE SECTION.

 FD  IN-FILE.

 01  IN-REC.
     03  QTA        pic 9(9).

 FD  OUT-FILE.

 01  OUT-REC.
     03  QTA        pic 9(9) COMP-3.


 WORKING-STORAGE SECTION.
 01 EOF-FLAG PIC X.
      88 END-OF-FILE VALUE 'Y'.


*****************************************************

 PROCEDURE DIVISION.
 MAIN-PARA.
     OPEN INPUT IN-FILE
        OUTPUT OUT-FILE
     PERFORM UNTIL END-OF-FILE
        READ IN-FILE
          AT END MOVE 'Y' TO EOF-FLAG
          NOT AT END
            MOVE IN-REC TO OUT-REC
            WRITE OUT-REC
        END-READ
     END-PERFORM
     CLOSE OUT-FILE IN-FILE
     STOP RUN.
```

#### ↳ Re: first conversion program: disaster

- **From:** "JerryMouse" <news@bisusa.com>
- **Date:** 2001-12-23T01:01:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com>`
- **References:** `<3c250264.895577@news.libero.it>`

```

"Duilio Foschi" <dedalus@yifan.net> wrote in message
news:3c250264.895577@news.libero.it...
> I have studied Cobol the whole day.
>
…[88 more quoted lines elided]…
>      STOP RUN.

The program is perfect except for one small detail: All group moves (MOVE
IN-REC TO OUT-REC) are alphanumeric. That is, the move is done without
conversions of any kind - as if both groups were defined as PIC X(...).

So, change that one line to read MOVE QTA OF IN-REC TO QTA OF OUT-REC and
you should be good to go.

Couple of observations:

1. My suggestion makes use of 'Qualified' data names. If you have two
different data elements of the same name, they must be 'Qualified' by using
the "OF" phrase - otherwise how would the compiler know which you mean? A
better (and MUCH more common) method of naming data is:

01  IN-REC.
   02  IN-QTA...

01  OUT-REC.
  02  OUT-QTA...

Then you MOVE IN-QTA TO OUT-QTA and don't have to fool with the "OF" stuff.

2. COMP-3 data are not that 'weird when viewed in historical perspective.
Computers were first deployed to solve commercial problems plus memory was
expensive. On the original mainframes, there existed circuitry to do decimal
arithmetic (as opposed to binary) very efficiently. COMP-3 minimizes storage
of decimal numbers (used in commercial applications) and COMP-3 numbers are
processed directly - without conversion - by decimal instructions/circuits
in the computer. This is much more efficient, both in terms of storage and
speed, and yields greater precision, than other forms of data
representation. No other common language of which I am aware can handle the
precision built into COBOL (18+ decimal digits of precision).

3. Oh, and once you perfect your program, you won't be able to view the
result with an ASCII viewer (like NOTEPAD) because the result won't be in
ASCII format. You'll have to use a hex viewer.
```

##### ↳ ↳ Re: first conversion program: disaster

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-23T10:47:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c25b061.3688907@news.libero.it>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com>`

```
>The program is perfect 

:)


>except for one small detail: All group moves (MOVE
>IN-REC TO OUT-REC) are alphanumeric. 

ARGHH

I should have known it: I read this thing in the tutorial (then I
forgot it).

>2. COMP-3 data are not that 'weird when viewed in historical perspective.

ok. But why is there any sense in using that format now ? 

>So, change that one line to read MOVE QTA OF IN-REC TO QTA OF OUT-REC and
>you should be good to go.

at first there was some avoc: 

the output file was _bigger_ than the input file.

After some head-scratching I realized that the input file was 72 bytes
long, while the expected size was 66 bytes (9 bytes for '123456789' +
1 byte for 0D + 1 byte for 0A).

Further inspection revealed that I had written

1234556789

in every line, instead of 

123456789

ARGHHHH!

Now everything works as expected.

I am happy.

Thanks a lot and merry Xmas

Duilio
```

##### ↳ ↳ Re: first conversion program: disaster

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-23T11:05:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c25b8b0.5816643@news.libero.it>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com>`

```
>1. My suggestion makes use of 'Qualified' data names. 


I tried the syntax 

            MOVE CORRESPONDING IN-REC TO OUT-REC

and it works, too (in the sense that it does format convertion).

This is useful in my case, as the record is made of several fields and
this will be a quick and dirty conversion routine..

>3. Oh, and once you perfect your program, you won't be able to view the
>result with an ASCII viewer (like NOTEPAD) because the result won't be in
>ASCII format. You'll have to use a hex viewer.

I used tdump (of Borland) to see the result and I had a nice glimpse
of how COMP-3 number are written:

Turbo Dump  Version 4.1 Copyright (c) 1988, 1994 Borland International
                       Display of File 2.DAT

000000: 12 34 56 78 9F 0D 0A 12  34 56 78 9F 0D 0A 12 34 
000010: 56 78 9F 0D 0A 12 34 56  78 9F 0D 0A 12 34 56 78 
000020: 9F 0D 0A 12 34 56 78 9F  0D 0A 00 00 00 00 00 00 


do you see ?

My ASCII numbers '123456789'  where converted to 
hex 

12 34 56 78 9F

where every digit now takes a nibble.

(The last nibble F must be a filler)

A reduction of roughly 50% in space.

Very interesting

Thanks a lot

Duilio
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

- **From:** "JerryMouse" <news@bisusa.com>
- **Date:** 2001-12-24T05:11:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it>`

```

"Duilio Foschi" <dedalus@yifan.net> wrote in message
news:3c25b8b0.5816643@news.libero.it...
> >1. My suggestion makes use of 'Qualified' data names.
>
…[5 more quoted lines elided]…
> and it works, too (in the sense that it does format convertion).

## Yes. I didn't mention MOVE CORRESPONDING because imbedding the record
name is more common - and for good reasons. In thirty years, I have never
seen MOVE CORRESPONDING actually used anywhere. (I know, I know, there are
those out there who've seen, or even used, MOVE CORRESPONDING. I've just
never run into such a program.)

>
> This is useful in my case, as the record is made of several fields and
…[26 more quoted lines elided]…
> (The last nibble F must be a filler)

## No, it's not a filler. The last nibble is the algebraic sign. It is
always a letter (A-F) and here's an easy way to remember: FACE (or CAFE) are
positive, B & D are negative.

>
> A reduction of roughly 50% in space.

## And to answer yout question about why COMP-3 is still used, this day in
age, what with electric lights and indoor plumbing, there are two answers:
1. There are still decimal arithmetic circuits in use, so COMP-3 is more
efficient than other renditions, and
2. There hundreds of billions of records and billions of lines of code that
use it every day (and I'm not exaggerating).
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 4)_

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-24T09:42:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c26f565.467666@news.libero.it>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com>`

```

>2. There hundreds of billions of records and billions of lines of code that
>use it every day 

gulp.

I have a further question:

One of the file I want to convert (and of which I have the FD) has the
following instructiorns in the source program:

      select ITEMS-EXTENDED assign to Path-Articoli-Extended
                       organization is indexed
                       access mode is dynamic
                       lock mode is automatic
                       record key is Io001-Key
                       file status is Stato-Rec.

Can I still access it sequentially ?

I suspect that the access mode is something that depends on the way I
want to open a file and not on the internal organization of the file.

In other words I guess I can access a file in different ways according
to my convenience and I am not compelled to use one way.

Is that right ?

Thank you

Duilio
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 5)_

- **From:** leclaire <leclaire@rr.com>
- **Date:** 2001-12-24T12:28:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C271EAA.720C8D02@rr.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it>`

```
Yes, that's right.  "Access Dynamic" means that the file may be accessed
either randomly (direct read by key) or sequentially, and usually both,
within the same program.  In fact, modern file systems typically default
to dynamic access, and I think I've even encountered a compiler or two
in which the "access mode" clause is optional.

Duilio Foschi wrote:
> 
> Can I still access it sequentially ?
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 6)_

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-24T13:46:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c27305a.15562477@news.libero.it>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com>`

```
>Yes, that's right.  

very good.

Thanks for the quick reply

Duilio
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-12-25T08:43:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C283C35.5F2A90D1@Azonic.co.nz>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com>`

```
leclaire wrote:
> 
> In fact, modern file systems typically default
> to dynamic access, and I think I've even encountered a compiler or two
> in which the "access mode" clause is optional.

In the Cobol Language ('85), and thus in all conforming compilers,
'ACCESS MODE' is optional and defaults to SEQUENTIAL if not specified.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 7)_

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2001-12-24T14:52:22-09:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C27BFB6.D9A673B1@dced.state.ak.us>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz>`

```
Richard Plinston wrote:

> leclaire wrote:
> >
…[5 more quoted lines elided]…
> 'ACCESS MODE' is optional and defaults to SEQUENTIAL if not specified.

Which I believe is different from what leclaire was talking about. Taken in
context, leclaire seems to be saying that some compilers default ACCESS MODE
to DYNAMIC. IMO that default makes a lot more sense than defaulting to
SEQUENTIAL.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 8)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2001-12-25T03:31:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hqSV7.2497$tp6.605228099@newssvr16.news.prodigy.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C27BFB6.D9A673B1@dced.state.ak.us>`

```
    I think I read somewhere that with mainframe COBOLs, there's a lot more
overhead involved with DYNAMIC ACCESS than SEQUENTIAL and one should choose
between the two based upon the predominant access used in the program.  If
that's true, I can understand defaulting to SEQUENTIAL.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-12-25T18:37:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C28C77D.A092E8AC@Azonic.co.nz>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz>`

```
> > leclaire wrote:
> > >
…[7 more quoted lines elided]…
> Which I believe is different from what leclaire was talking about. 

In what way ?

> Taken in context, 

The context is the Cobol language and its compilers, is leclaire's
context different ? 

> leclaire seems to be saying that some compilers default ACCESS MODE
> to DYNAMIC. 

Which would make them non-conforming.  _All_ compilers should have
ACCESS MODE as optional with the default as SEQUENTIAL.  If there is a
compiler that defaults to DYNAMIC then name it.

What leclaire _seems_ to be saying is that it will 'default to dynamic
access' even if the ACCESS MODE clause is not optional.  What ?

> IMO that default makes a lot more sense than defaulting to SEQUENTIAL.

If the ORGANISATION is SEQUENTIAL then it makes sense to default the
ACCESS MODE to SEQUENTIAL as that is the _only_ valid option.  If ACCESS
MODE were to have a default of DYNAMIC in _some_ cases then there must
be a rule under which it defaults sometimes to one thing and other times
to another.

What actually makes sense is having a consistent default, as it in does
in fact have.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 8)_

- **From:** leclaire <leclaire@rr.com>
- **Date:** 2001-12-25T16:08:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C28A3C5.990BC44A@rr.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C28C77D.A092E8AC@Azonic.co.nz>`

```
  To clarify what was said regarding the "Access Mode" clause, let me
say that *all* of the above responses are correct.  For the sake of
*brevity* (I am, after all, a programmer) I omitted certain details.
However, I meant to imply that Access Dynamic *should* be the default. 

  That is, any modern file system should be capable of allowing (or
prepared to provide) both random and sequential access within a program
without requiring that the programmer make a determination beforehand to
*exclude* either one mode or the other. This especilly given the strong
likelihood that somewhere down the road there will be certain
modifications made to the program, and most likely be made by someone
other than the original author and who may spend agonizing hours trying
to figure out why the modifications aren't working until he/she
"happens" to review a listing which includes the copylib and notice the
offending Access Mode clause (unless the platform provides clear and
relavent error messages, but how often does THAT happen).

  Therefore, personally in practice, I *always* code "access dynamic" in
the select statement.  If the operating environment has performance
issues regarding access mode then I feel that the complier should
automatically optimize the code accordingly (please hear me out on
this).  It is my belief that specifying access mode is another largely
unnecessary throwback to legacy COBOL and represents a mere formality in
order to accomodate existing rigid (dare I say antiquated) systems, such
as being forced to honor the sacred A and B margins, or coping with
compliers which error out because there is no Label Records clause (or
error out because said clause was included).

  However, I also recognize that the widespread existence of such rigid
and unprogressive systems are largely responsible for the perpetuation
of this marvelous language, and therefore my livelihood as well.  (Try
as I may, I have not been able to develop any adequately useful systems
utilizing VB or any incarnation of C/C++/C#/u-name-it or
hobbled-together Java or Perl or whatever ... at least, not any systems
that I would want to put my name on ... rant off).  So if mainframe
vendors (ahem) and the standards groups which accomodate them determine
that access mode should default to sequential unless otherwise
specified, then so be it.

  To end this discussion, in my earlier post I meant to say this: that
at some time I may have noticed while reviewing the language reference
manual for some implementation of COBOL that the Access Mode cluase was
not required.  That particular implementation *may* have defaulted to
Dynamic mode (which I feel it should *in an ideal world*), but I would
have included an Access Mode Dynamic clause anyway, from force of
habit.  If there is in fact a standard, and that standard is to default
to sequential access, then in my view it is a good habit to maintain.

  That's my thoughts. Your thoughts and opinions are welcome.
  Merry Christmas to all and seasons greetings to everyone else!
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 9)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-12-25T16:16:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d2uh2uc0gv2evfh5vdma4797di4haclhfo@4ax.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C28C77D.A092E8AC@Azonic.co.nz> <3C28A3C5.990BC44A@rr.com>`

```
On Tue, 25 Dec 2001 16:08:18 GMT leclaire <leclaire@rr.com> wrote:

:>  To clarify what was said regarding the "Access Mode" clause, let me
:>say that *all* of the above responses are correct.  For the sake of
:>*brevity* (I am, after all, a programmer) I omitted certain details.
:>However, I meant to imply that Access Dynamic *should* be the default. 

Certainly an argument for bloatware.

:>  That is, any modern file system should be capable of allowing (or
:>prepared to provide) both random and sequential access within a program
:>without requiring that the programmer make a determination beforehand to
:>*exclude* either one mode or the other. 

They do.

Just like a modern operating system should be capable of allowing (or prepared
to provide) a program to do pretty much about anything without requiring that
the programmer make a determination beforehand.

:>                                        This especilly given the strong
:>likelihood that somewhere down the road there will be certain
:>modifications made to the program, and most likely be made by someone
:>other than the original author and who may spend agonizing hours trying
:>to figure out why the modifications aren't working until he/she
:>"happens" to review a listing which includes the copylib and notice the
:>offending Access Mode clause (unless the platform provides clear and
:>relavent error messages, but how often does THAT happen).

If the attempted access does not match the access mode one certainly should
expect compilation errors. 

Which compiler did you find that did not do that?

:>  Therefore, personally in practice, I *always* code "access dynamic" in
:>the select statement.  If the operating environment has performance
:>issues regarding access mode then I feel that the complier should
:>automatically optimize the code accordingly (please hear me out on
:>this).  It is my belief that specifying access mode is another largely
:>unnecessary throwback to legacy COBOL and represents a mere formality in
:>order to accomodate existing rigid (dare I say antiquated) systems, such
:>as being forced to honor the sacred A and B margins, or coping with
:>compliers which error out because there is no Label Records clause (or
:>error out because said clause was included).

A bloatware argument.

The code should more appropriately be optimized to the general case (good old
80/20 rule). If you lie to the compiler or chooses an inefficient way to code
something expect poor results.

:>  However, I also recognize that the widespread existence of such rigid
:>and unprogressive systems are largely responsible for the perpetuation
:>of this marvelous language, and therefore my livelihood as well.  (Try
:>as I may, I have not been able to develop any adequately useful systems
:>utilizing VB or any incarnation of C/C++/C#/u-name-it or
:>hobbled-together Java or Perl or whatever ... at least, not any systems
:>that I would want to put my name on ... rant off).  So if mainframe
:>vendors (ahem) and the standards groups which accomodate them determine
:>that access mode should default to sequential unless otherwise
:>specified, then so be it.

Reducing program size and speeding up processing for the general case.

   [ snipped ]
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 9)_

- **From:** "JerryMouse" <news@bisusa.com>
- **Date:** 2001-12-26T00:10:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2A8W7.389135$8q.33697501@bin2.nnrp.aus1.giganews.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C28C77D.A092E8AC@Azonic.co.nz> <3C28A3C5.990BC44A@rr.com>`

```

"leclaire" <leclaire@rr.com> wrote in message
news:3C28A3C5.990BC44A@rr.com...

>   Therefore, personally in practice, I *always* code "access dynamic" in
> the select statement.  If the operating environment has performance
> issues regarding access mode then I feel that the complier should
> automatically optimize the code accordingly (please hear me out on
> this).

I ran a test. There are no performance issues.

The time for dynamic/sequential reads is exactly the same as it is for
sequential/sequential reads. Writing too.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-12-26T11:25:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C29B3B0.F131AFA2@Azonic.co.nz>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C28C77D.A092E8AC@Azonic.co.nz> <3C28A3C5.990BC44A@rr.com>`

```
leclaire wrote:

> For the sake of
> *brevity* (I am, after all, a programmer) I omitted certain details.

Cobol programmers should not abbreviate nor should they omit details 
;-)

> However, I meant to imply that Access Dynamic *should* be the default.

And I disagreed, as previously indicated, defaulting to SEQUENTIAL is
sensible because there are file organizations for which ACCESS
SEQUENTIAL is the only option.

Besides which changing the default would break a lot of programs.

>   That is, any modern file system should be capable of allowing (or
> prepared to provide) both random and sequential access within a program
> without requiring that the programmer make a determination beforehand to
> *exclude* either one mode or the other. 

It is nothing to do with 'modern file systems', I was using machines in
the 60s that provided sequential and/or random access, but I had to do
these with subroutine calls. Indexed and Relative files were introduced
in ANS74 which also allowed ACCESS DYNAMIC clause.  The programmer only
had to pre-determine what he meant when he wrote 'READ file' and specify
that.  There was no need at all to ever 'exclude' anything.

> This especilly given the strong
> likelihood that somewhere down the road there will be certain
…[5 more quoted lines elided]…
> relavent error messages, but how often does THAT happen).

You are only arguing about changes that may take place in one specific
situation and are ignoring the equally agonising problems associated
with other situations.  One programmer is completely stumped for hours
when his 'READ file' unexpectedly gets the next record because access is
sequential.  Another fumbles for half a day because 'READ file' fails to
read the next record but just rereads the same one due to access
dynamic.

>   Therefore, personally in practice, I *always* code "access dynamic" in
> the select statement. 

Presumably your *always* actually excludes the cases when it is
inappropriate, such as for printers or 'sysin/sysout' or all the other
cases where you don't specify dynamic.  Or is your compiler lax enough
that it just doesn't report the errors in these cases ?

> If the operating environment has performance
> issues regarding access mode then I feel that the complier should
> automatically optimize the code accordingly 

I did work on one system where access dynamic was required to implement
record locking (which was/is non-standard anyway) on the ISAM files. 
Sequential files or access, or random, gave exclusive file lock for OPEN
I-O and OUTPUT and shared for OPEN INPUT.

> It is my belief that specifying access mode is another largely
> unnecessary throwback 

Throwback, yes.  Unnecessary, no.  Changing from access sequential to
access dynamic requires that NEXT be added to READ to give the same
results.  The default means that files can be changed from organisation
sequential to organisation indexed and the only change to existing
programs would be the organisation clause in the select and recompile to
have them continue working the same way.

> So if mainframe
> vendors (ahem) and the standards groups which accomodate them determine
> that access mode should default to sequential unless otherwise
> specified, then so be it.

It has nothing to do with mainframe vendors or 'accomodating' them, it
is about consistency in programming.

>   To end this discussion, in my earlier post I meant to say this: that
> at some time I may have noticed while reviewing the language reference
> manual for some implementation of COBOL that the Access Mode cluase was
> not required.  That particular implementation *may* have defaulted to
> Dynamic mode 

I very much doubt that it would have.

> (which I feel it should *in an ideal world*), 

I think that you should revise your ideas about what should be 'ideal'
for all the printers, text files, console and other sequential files for
which many wouldn't bother using an access clause, the default being
absolutely perfect for these needs.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 10)_

- **From:** leclaire <leclaire@rr.com>
- **Date:** 2001-12-26T00:49:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C291DEA.B1C37C02@rr.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C28C77D.A092E8AC@Azonic.co.nz> <3C28A3C5.990BC44A@rr.com> <3C29B3B0.F131AFA2@Azonic.co.nz>`

```


Richard Plinston wrote:
> 
> I think that you should revise your ideas about what should be 'ideal'
> for all the printers, text files, console and other sequential files for
> which many wouldn't bother using an access clause, the default being
> absolutely perfect for these needs.

I've not encontered a printer or text file with an index, so the access 
mode really has no bearing.  Please realize that I was replying to 
Foschi's question regarding the select for an indexed file:

" select ITEMS-EXTENDED assign to Path-Articoli-Extended
                       organization is indexed
                       access mode is dynamic
                       lock mode is automatic
                       record key is Io001-Key
                       file status is Stato-Rec.
 Can I still access it sequentially ?"

And I wasn't suggesting that anyone retrofit existing code or change
any standards.  As sequential access is the default then we may continue
to specify dynamic mode in the environment division and 'read next' for
sequential access.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 10)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-12-27T20:35:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C2B8606.67A295B3@Azonic.co.nz>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C28C77D.A092E8AC@Azonic.co.nz> <3C28A3C5.990BC44A@rr.com> <3C29B3B0.F131AFA2@Azonic.co.nz>`

```
Calvin Crumrine wrote:

> As mentioned above, I don't know of any compilers that do this. 

I very much doubt of the existence of any.

> > What leclaire _seems_ to be saying is that it will 'default to dynamic
> > access' even if the ACCESS MODE clause is not optional.  What ?
> 
> What? How can something 'default' if a specific selection is required, i.e.
> non-optional? 

Exactly, that is why I questioned what he seemed to be saying with my
'What?'.

> I was pointing
> out that your response to leclaire indicated a misunderstanding-either you or I
> misunderstood what leclaire was saying.

I didn't misunderstand anything about what leclaire wrote, My response
was initially pointing out what leclaire misunderstood about Cobol.

>  I *will* stand by my
> statement that a compiler that defaults to ACCESS MODE DYNAMIC when appropriate
> (ORGANIZATION INDEXED, ACCESS MODE not specified) would be better (IMO) that the
> conforming compilers that default to ACCESS MODE SEQUENTIAL in such
> circumstances.

You seem to define 'better' as 'saving two words being keyed into what
is most likely a copybook (and thus saving nothing in each program)'.

Of course if you actually type in those two words for each indexed file
in each program, or even into copybooks, then I would suggest that you
get better development tools and a better methodology. Ever heard of
skeleton code files ? keyboard macros ?  inserting file into current
being edited ?

For the same point I would define 'worse' as 'breaking large quantities
of existing programs that use the default, forcing programmers to add
'access sequential' to make them work again'.

Note that where sequential access is specified or defaulted to (and for
sequential files) it is only necessary to use 'READ file' for a
sequential read.  When access dynamic is used a sequential read requires
a NEXT RECORD clause and 'READ file' works in a completely different
way.

BTW, what do you think should be the default for 'ORGANISATION RELATIVE'
?

> Obviously I didn't think this thru.

I think that makes a very good summary of your entire position.

Now what I think leclaire may have _wanted_ to have said is that
_programmers_ (rather than compilers) should default to _specifying_
ACCESS DYNAMIC, as he does, wherever possible.  I would be tempted to 
agree with that.  But it ain't what he said.
```

###### ↳ ↳ ↳ Re: In Conclusion ... first conversion

_(reply depth: 11)_

- **From:** leclaire <leclaire@rr.com>
- **Date:** 2001-12-27T22:14:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C2B9C80.92D5A328@rr.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C28C77D.A092E8AC@Azonic.co.nz> <3C28A3C5.990BC44A@rr.com> <3C29B3B0.F131AFA2@Azonic.co.nz> <3C2B8606.67A295B3@Azonic.co.nz>`

```
First, thank you Richard for detailing the mechanics of the Cobol
Multiply/Divide statements.  It makes perfect sense now, and I
for one will likely never again head for the manual for syntax.

And finally, regarding dynamic access of indexed files ...

Richard Plinston wrote:
> 
> Now what I think leclaire may have _wanted_ to have said is that
> _programmers_ (rather than compilers) should default to _specifying_
> ACCESS DYNAMIC, as he does, wherever possible.  I would be tempted to
> agree with that.  But it ain't what he said.

I accept full blame for my cavalier remark alluding to some unspecified 
compiler possibly defaulting to Dynamic access.  Your statement above 
is most accurate.  I hope everyone has enjoyed this little exercise in
group dynamics <g>.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 11)_

- **From:** jamesc7460@aol.com (JamesC7460)
- **Date:** 2001-12-31T02:53:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20011230215326.06350.00002690@mb-mq.aol.com>`
- **References:** `<3C2B8606.67A295B3@Azonic.co.nz>`

```
>  I *will* stand by my  statement that a compiler that defaults to 
> ACCESS MODE DYNAMIC when appropriate  (ORGANIZATION 
> INDEXED, ACCESS MODE not specified) would be better (IMO) that > the 
conforming compilers that default to ACCESS MODE 
> SEQUENTIAL in such  circumstances.

That would be quite unfortunate for us if they did.  First understand that
there is no such thing as a dynamic access method there are only ones for
sequential and random.  When a file is declared as DYNAMIC two file handle
opens are issued:  one for random access,  another for sequential and it would
be detrimental to the system's performance if every file open request came with
double the baggage as even modern *progressive* file systems have a limit to
the number of such things that can be active at any time.  The only reasonable
default, as Mr. Plinston pointed out, is SEQUENTIAL as it still (probably)
accounts for 90% of all file access in the *real* world.

Cheers and pass the eggnog,
Jim Castro
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 8)_

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2001-12-26T08:18:58-09:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C2A0682.165E4F6B@dced.state.ak.us>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C28C77D.A092E8AC@Azonic.co.nz>`

```


Richard Plinston wrote:

> > > leclaire wrote:
> > > >
…[9 more quoted lines elided]…
> In what way ?

as expained in my original message just a sentence or so after this response.
Did you read the entire message?

> > Taken in context,
>
> The context is the Cobol language and its compilers, is leclaire's
> context different ?

I take leclaire's context to be ACCESS MODE DYNAMIC.

> > leclaire seems to be saying that some compilers default ACCESS MODE
> > to DYNAMIC.
…[3 more quoted lines elided]…
> compiler that defaults to DYNAMIC then name it.

*I* don't know of any. I was simply pointing out that leclaire's statement seems
to say that he/she does. Leclaire? Can you name it?

> What leclaire _seems_ to be saying is that it will 'default to dynamic
> access' even if the ACCESS MODE clause is not optional.  What ?

What? How can something 'default' if a specific selection is required, i.e.
non-optional? I think leclaire is saying that (on some compilers anyway) the
ACCESS MODE is optional and if it's missing then the default is DYNAMIC. Your
statement that the ACCESS MODE is *always* optional (on conforming compilers)
doesn't conflict, but your statement that the default is SEQUENTIAL does.
(Except for the qualifier that the compiler conform to the standard, which
qualification leclaire didn't make.)

> > IMO that default makes a lot more sense than defaulting to SEQUENTIAL.
>
…[4 more quoted lines elided]…
> to another.

Good point. Obviously I didn't think this thru.

> What actually makes sense is having a consistent default, as it in does
> in fact have.

Well, I don't see any problem with a default that varies depending on the
circumstances. It's called intelligence. (Or at least that's what I call it.) Of
course this variation should follow a consistent rule & it should be documented,
but I don't see any problem with the variation itself.

As mentioned above, I don't know of any compilers that do this. I was pointing
out that your response to leclaire indicated a misunderstanding-either you or I
misunderstood what leclaire was saying. Since leclaire hasn't responded, that
I've seen, possibly the misunderstanding was mine. I *will* stand by my
statement that a compiler that defaults to ACCESS MODE DYNAMIC when appropriate
(ORGANIZATION INDEXED, ACCESS MODE not specified) would be better (IMO) that the
conforming compilers that default to ACCESS MODE SEQUENTIAL in such
circumstances. OTOH I've seen many 'better' ideas fail because they were
non-conforming & possibly this is another such. In any case, I don't know of a
compiler that actually does this, whether it's actually a better idea or not, so
until somebody comes up with one I suppose the question is moot.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 9)_

- **From:** leclaire <leclaire@rr.com>
- **Date:** 2001-12-27T00:48:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C2A6F33.C9D07CBD@rr.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C28C77D.A092E8AC@Azonic.co.nz> <3C2A0682.165E4F6B@dced.state.ak.us>`

```

Calvin Crumrine wrote:
> > 
> I *will* stand by my
…[3 more quoted lines elided]…
> circumstances. 

Well put, and thank you, I fully agree.  The point of my original reply
was basicly that Access Dynamic is the equivalent of "no particular
access mode was specified" and therefore the file may be accessed 
in any manner.

> OTOH I've seen many 'better' ideas fail because they were
> non-conforming & possibly this is another such. In any case, I don't know of a
> compiler that actually does this, whether it's actually a better idea or not, so
> until somebody comes up with one I suppose the question is moot.

No particular compiler came to mind at the time, but it seemed to me
that if there is no need to specify either random or sequential access
then there may as well not be any requirement to include the access mode
clause at all.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 10)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-12-27T17:54:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c2aa9ee_5@Usenet.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C28C77D.A092E8AC@Azonic.co.nz> <3C2A0682.165E4F6B@dced.state.ak.us> <3C2A6F33.C9D07CBD@rr.com>`

```

leclaire <leclaire@rr.com> wrote in message news:3C2A6F33.C9D07CBD@rr.com...
>
<big snipperoonie on something that really isn't worth debating.>
>
> No particular compiler came to mind at the time, but it seemed to me
> that if there is no need to specify either random or sequential access
> then there may as well not be any requirement to include the access mode
> clause at all.

IF there is no need to specify either Random or Sequential access your point
is well taken. However, this is NOT the case.

What happens when in one program I want pure random access, in another I
want skip sequential access (position to a point in the file, then read
sequentially for a while, until I skip to the next random point, and in yet
another program I just want to read sequentially from start to end?

COBOL originally supported sequential and random access. The ACCESS MODE
DYNAMIC was put in it to support the skip sequential access described above.
It is very powerful and most people use it, so it is natural that you might
expect or hope that THAT would be the default. However COBOL has
consistently had a history of trying to be SIMPLE. The defaults for most
COBOL constructs are the SIMPLEST ones. If you wish to introduce
"complexity" you must "spell it out"...

What is the SIMPLEST form of file access?

Yep...SEQUENTIAL. THAT's why it is the default.

Your bitching about  it won't change it, so deal with it and let's move
on...<G>

(I can be confident it won't be changed for the following reasons:

1. There is too huge an investment in existing code to allow a fundamental
change to something which isn't broken.

2. It complies with the "philosophy of COBOL" which makes the simplest
options the default.

3. There is no way the existing standards setup could accommodate doing this
before 2020 (and there's no reason why they should); they are much too busy
getting the 1989 standard out before 2003...

Now, you could argue that the MOST USED option should always be the default,
and many people (including myself) could be sympathetic to your argument.
But it still won't change it.(And besides, then we'd sit in CLC arguing
about which is the MOST USED option with no one being able to quantify
it...so it would just rattle on into another pointless argument.)

That's the way it is. SEQUENTIAL is the default in conforming compilers (as
I think Richard pointed out).

There are many things which newcomers to COBOL will consider "odd".
Nevertheless, they have served the COBOL community well over many years and
they are NOT broken. (Things like why we READ a FILE but WRITE a RECORD; a
major source of confusion to many COBOL newbies... The original syntax of
ADD and DIVIDE (now made more "forgiving" by vendor extension so we can say
"DIVIDE...BY" (instead of the original "DIVIDE... INTO") and a host of other
"inelegancies" and "inconsistencies".)

The general use of Indexed files is a nail in COBOL's coffin anyway. (No,
I'm not saying they should NEVER be used. I AM saying they should be used
only when it is particularly appropriate and there is no doubt that the data
on them will NEVER need to be shared with any other system, and they should
NOT be the "First Choice" for systems requiring random or dynamic access...)

Let it go...<G>

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 11)_

- **From:** leclaire <leclaire@rr.com>
- **Date:** 2001-12-27T05:59:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C2AB827.32538389@rr.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C28C77D.A092E8AC@Azonic.co.nz> <3C2A0682.165E4F6B@dced.state.ak.us> <3C2A6F33.C9D07CBD@rr.com> <3c2aa9ee_5@Usenet.com>`

```

"Peter E. C. Dashwood" wrote:
>  
> Your bitching about  it won't change it, so deal with it and let's move
…[5 more quoted lines elided]…
> 

Just to reiterate my point a couple posts up in this thread:
at no point did I ever advocate nor even make reference to
either changing the standard nor modifying any existing code.

I only replied to the original poster that Access Dynamic
pretty much allows any type of access one would need.

*Now* we can drop it. This has probably gone much too far
and we're all "preaching to the choir".

> 
> 3. There is no way the existing standards setup could accommodate doing this
> before 2020 (and there's no reason why they should); they are much too busy
> getting the 1989 standard out before 2003...
> 

(( grin ))  Hey, at least this language *HAS* standards.

> Now, you could argue that the MOST USED option should always be the default,
> and many people (including myself) could be sympathetic to your argument.

Hence I had qualified my original statement with "in an ideal world". 

> 
> There are many things which newcomers to COBOL will consider "odd" ...
> "DIVIDE...BY" (instead of the original "DIVIDE... INTO") ...

I occasionally reach for the quick reference card on that one myself,
as well as the ever perplexing "multiply LIT by ID".

> 
> The general use of Indexed files is a nail in COBOL's coffin anyway. (No,
> I'm not saying they should NEVER be used. I AM saying they should be used
> only when it is particularly appropriate ...

IMHO COBOL's built-in database is perhaps one of its most handy
features.

> Let it go...<G>
> 

'Nuff said.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 12)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-12-27T19:32:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C2B7755.5FB93F55@Azonic.co.nz>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C28C77D.A092E8AC@Azonic.co.nz> <3C2A0682.165E4F6B@dced.state.ak.us> <3C2A6F33.C9D07CBD@rr.com> <3c2aa9ee_5@Usenet.com> <3C2AB827.32538389@rr.com>`

```
leclaire wrote:

> > There are many things which newcomers to COBOL will consider "odd" ...
> > "DIVIDE...BY" (instead of the original "DIVIDE... INTO") ...
> 
> I occasionally reach for the quick reference card on that one myself,
> as well as the ever perplexing "multiply LIT by ID".

The rule was (before DIVIDE BY) that the result would be in the last
argument:

     ADD X          TO Y
     SUBTRACT X   FROM Y
     DIVIDE X     INTO Y
     MULTIPLY X     BY Y

The result is in 'Y'.  Of course if GIVING Z is added to any of these
then Z is the last argument and takes the result.
```

###### ↳ ↳ ↳ Comments on the File System, was : first conversion program: disaster

_(reply depth: 12)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-12-28T14:33:10+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c2bccc5_4@Usenet.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <3C271EAA.720C8D02@rr.com> <3C283C35.5F2A90D1@Azonic.co.nz> <3C28C77D.A092E8AC@Azonic.co.nz> <3C2A0682.165E4F6B@dced.state.ak.us> <3C2A6F33.C9D07CBD@rr.com> <3c2aa9ee_5@Usenet.com> <3C2AB827.32538389@rr.com>`

```

leclaire <leclaire@rr.com> wrote in message news:3C2AB827.32538389@rr.com...
>
>
> IMHO COBOL's built-in database is perhaps one of its most handy
> features.
>
Yes, I agree with that. In fact, its usefulness and simplicity is positively
seductive...<G>

For many years (when there was no alternative) it served us very well.

The trouble is that in those days COBOL was the ONLY game in town (at least
as far as commercial processing was concerned) so there was no need to
interface to other (non-COBOL) systems, and PCs weren't invented yet.

With the advent of random access in the mid/late sixties (see "Tales from
the BitBucket" on www.aboutlegacycoding.com this month...) the COBOL file
system was upgraded and it provided an excellent repository. But there was a
downside...

Files proliferated. There was not the body of knowledge regarding DB design
which can be tapped today.

Better ways to organise the most important resource in the Enterprise had to
be found, and they were. Hierarchic and Networked DB models made their
appearances and we all got stuck into IMS and IDBMS and ADABAS.

These systems were better in terms of data organisation and efficieny, but
they were a bit unwieldy to implement and the simplicity of the COBOL file
system made it retain its appeal. As late as 1979 I can remember fighting a
(successful) rearguard action to retain VSAM over IMS for a key project in a
major UK Corporation. Now, in hindsight (isn't it amazing how clear things
become when you look BACK at them...<G>), I realize my position was really
very wrong and I did the Company no great favour by maintaining
it...(fortunately, I did them no great harm either. The VSAM system we
designed served very well for several years until it was finally replaced by
IMS, but there would have been definite cost savings in "biting the bullet"
earlier, rather than later.)

Given the successful track record of the COBOL file system you might well
wonder why I am so anti.

Here are my arguments:

1. I am NOT anti-File System, per se. It is an excellent tool. If we were
developing COBOL systems in isolation (as we did prior to 1980) you wouldn't
hear a peep out of me... (well, I might suggest using the Relational Model
on pure data organizational grounds, but I certainly wouldn't be as vehement
as I am being.)

2. Data is a Corporate Resource. It is the most essential resource in the
Organization. If you store it with the COBOL file system you have to write
an interface or downstream feed for every non-COBOL system that wants to
access it.
(Of course, many IT departments see this as an excellent justification for
the retention of COBOL and believe that by doing this they are ensuring
COBOL's survival. History has shown that instead, the lesson learned by
Management is that anything written in COBOL is "locked up" and will require
an expensive conversion sooner or later. (Believe me, I have managed a
number of fairly major conversions like this and the general attitude is
"Bloody COBOL...the sooner we get rid of it the better...")

So the COBOL systems are relegated to "Legacy" and all new development is
forbidden to be done in COBOL.

On the other hand, systems that utilise an Open Database are very popular in
the organization because packages and Client /Server Languages can access
and share them. In fact, in today's culture, where the trend is towards
smaller "localised" applications in different Departments, nobody really
gives a rats arse what language is used for a specific application, as long
as the data from it is freely available to all, without problem. The COBOL
File System actually EXCLUDES COBOL from the "club"...

3. Having built the system using the COBOL File System, the users now want
to get information from it. They need to have a COBOL Program written for
every report and screen enquiry they want.

New requirements, new reports, new COBOL programs. (...and endless debates
in CLC about the relative merits of the COBOL Report Generator or how to
embed control codes into report programs for font and paper size...etc., ad
nauseum... It's time we trained users to accept reports as files, which they
can print through their Word Processor, ONLY if they really NEED to... That
way the trees last longer, the users have less stuff to push around their
desks and filing cabinets, and programmers have one thing less to worry
about...<G>)

Users suddenly find they are disenfranchised with no control over their own
data. They have to go cap in hand to IT and request a new report. The
psychological effect of this is enormous. The users of today are NOT the
users of 30 years ago (or even 10 years ago...). Today's user has a computer
at home which he runs his Wordprocessor and Spreadsheets on. He is familiar
with Wizards which allow him to "program" in a fundamental way and achieve
results. If he uses ACCESS he knows that getting information from a
Relational Database is a snap, even if he doesn't have a background in
Relational Set Theory and Boolean Algebra. So, when the IT department tell
him they'll do his report sometime next month, he gets very irritated and
bitches to his manager.

Who is seen as the culprit?

COBOL.

If the data wasn't locked into the COBOL file system, users could get it
themselves.

Many Corporations are becoming aware of what this is costing them. It is not
for nothing that COBOL is becoming "unfashionable".

And the sad thing is that COBOL is the "right" language for commercial
development.

While programmers argue about the intimate details of computer programming
and how COBOL does or does not meet the requirements of a "modern" language,
these academic arguments are being swamped by the visible effect on the
"shop floor" that using the COBOL file system is having. Frustration, anger,
and a feeling of powerlessness in the user base are not likely to win COBOL
friends.

4. Programmers in a forum such as this one, inevitably see the argument from
a programming perspective. The File System is simple to implement,
efficient, reliable, and I don't have to buy any add on products...

I am NOT arguing any of this (because I can't...I'd lose...<G>).

What I am suggesting is that there are things even more powerful than good
programming, which will affect the future of COBOL.

Organizational perception is the most compelling of these.

Whenever there are problems, if an individual's name keeps coming up, it
isn't too long before that individual is working somewhere else...

I believe that implementing closed systems with the COBOL File System is a
major contributor to the "bad press" COBOL is currently suffering from. In
Companies where the COBOL development is to a RDB which can be easily
imported/exported or even accessed directly from VB or Java or Crystal
Reports, using ODBC across platforms, you will hear much less criticism of
COBOL. In these circumstances it is accepted as the "mainframe language"
but, as it doesn't cause any problems, there is little or no antipathy to
it.

Finally:

1. I would urge you as a COBOL Programmer to consider carefully before
implementing any "public" systems with the File System. RDB will do the job
just as well (better if it is tuned properly, with the sole exception of
large volume sequential access) and it is Open.

2. Learn SQL. (It is MUCH easier than COBOL and you learned THAT OK...<G>)

3. Existing Indexed files can be converted to RDB fully automatically (and
for small system personal use, I'll give you the tools for free...) so you
can try with one of your existing systems and "get the hang of it". You will
still need to manually amend your code to access the new database (although
I am working on this and some progress is being made...). At the end of it,
you have a system which is more flexible, time proofed (the relational model
is here to stay, at least for the foreseeable future), and, best of all,
OPEN! You can run queries and reports from it WITHOUT having to write,
debug, and test COBOL programs, and it will interface easily and seamlessly
to any other RDB based system.

Pete.






 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 5)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-12-24T09:05:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QyGV7.5374$eo1.798992@news20.bellglobal.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it>`

```
That is correct, but for one thing ... it is the read statement that
determines whether you use the index or read it sequentially, not the open
statement.  If you are reading it either way, though, you should become
familiar with the locking mechanism.  You could end up locking out other
processes if you read and do not UNLOCK, REWRITE, or CLOSE. (Notice that
locking is set to automatic).

Donald

"Duilio Foschi" <dedalus@yifan.net> wrote in message
news:3c26f565.467666@news.libero.it...
>
> >2. There hundreds of billions of records and billions of lines of code
that
> >use it every day
>
…[28 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 6)_

- **From:** "JerryMouse" <news@bisusa.com>
- **Date:** 2001-12-24T15:08:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BxHV7.379518$8q.32666545@bin2.nnrp.aus1.giganews.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <QyGV7.5374$eo1.798992@news20.bellglobal.com>`

```

"Donald Tees" <donald_tees@sympatico.ca> wrote in message
news:QyGV7.5374$eo1.798992@news20.bellglobal.com...
> That is correct, but for one thing ... it is the read statement that
> determines whether you use the index or read it sequentially, not the open
…[3 more quoted lines elided]…
> locking is set to automatic).

1. "UNLOCK, REWRITE, or CLOSE." should read "UNLOCK, REWRITE, READ, WRITE,
or CLOSE."

2. With ACCESS IS DYNAMIC:

"READ MYFILE" implies random read (read based on a key) and demands a prior
statement along the lines of MOVE "WEASEL" TO MYKEY"

"READ MYFILE NEXT" implies sequential read.

3. How to read the first record whose key begins with "M" is an exercise
left to the reader (hint: see "START")
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 7)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-12-24T10:16:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eBHV7.5560$eo1.830216@news20.bellglobal.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <QyGV7.5374$eo1.798992@news20.bellglobal.com> <BxHV7.379518$8q.32666545@bin2.nnrp.aus1.giganews.com>`

```
Merry christmass, Jerry.
Donald
;<)

"JerryMouse" <news@bisusa.com> wrote in message
news:BxHV7.379518$8q.32666545@bin2.nnrp.aus1.giganews.com...
>
> "Donald Tees" <donald_tees@sympatico.ca> wrote in message
> news:QyGV7.5374$eo1.798992@news20.bellglobal.com...
> > That is correct, but for one thing ... it is the read statement that
> > determines whether you use the index or read it sequentially, not the
open
> > statement.  If you are reading it either way, though, you should become
> > familiar with the locking mechanism.  You could end up locking out other
…[8 more quoted lines elided]…
> "READ MYFILE" implies random read (read based on a key) and demands a
prior
> statement along the lines of MOVE "WEASEL" TO MYKEY"
>
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-12-25T18:52:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C28CAF6.44F2AFC2@Azonic.co.nz>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3c26f565.467666@news.libero.it> <QyGV7.5374$eo1.798992@news20.bellglobal.com> <BxHV7.379518$8q.32666545@bin2.nnrp.aus1.giganews.com>`

```
"Donald Tees" <donald_tees@sympatico.ca> wrote in message
> That is correct, but for one thing ... it is the read statement that
> determines whether you use the index or read it sequentially, not the open
…[3 more quoted lines elided]…
> locking is set to automatic).

What is even more relevant is the action that may be required in this
program if it encounters a record that is locked by another process. 
Depending on compiler maker, compiler options, run-time switches and/or
code in the program the program may repeat the same record without
moving the file pointer until the lock disappears (ensuring that the
record eventually gets read without a lock), or it may 'hang' until the
record becomes available, or it may move the file pointer on for the
next read.

Of course opening INPUT avoids the whole issue entirely as record locks
are not made or noticed.

Leaving the lock mode out may be a mistake as the system may default to
EXCLUSIVE (depending on .. etc) which may then fail to open the file if
it was opened by another user and/or would lock those other users out.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-12-24T18:03:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C276E31.95166413@shaw.ca>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com>`

```


JerryMouse wrote:

>
> ## Yes. I didn't mention MOVE CORRESPONDING because imbedding the record
…[4 more quoted lines elided]…
>

Agreed, I had never used it before - but here's a practical example. I give the
user three options for producing a Listbox (1) Default - by Name (2) By Key and
(3) If appropriate, by 'Another Code'. Initially I was 'leaping all over the
place' storing the positions (so I could use Reference Modification). to move
fields into list records depending upon sequence selected.

So my revised coding in OO is :-

       OBJECT-STORAGE SECTION. *> WORKING in COBOL 2002
       copy "collectn.cpy"   replacing ==(tag)== by ==ws==.
       copy "desListRec.cpy" replacing ==(tag)== by ==ws==.

       *> Listbox records :-

       01 Key-Record.
          05 Des-Code                     pic x(04).
          05 Tab1                         pic x.
          05 Des-Name                     pic x(40).
          05 Tab2                         pic x.
          05 Des-Other1                   pic x(10).
          05 Des-Other2                   pic x(10).

       01 Name-Record.
          05 Des-Name                     pic x(40).
          05 Tab1                         pic x.
          05 Des-Code                     pic x(04).
          05 Tab2                         pic x.
          05 Des-Other1                   pic x(10).
          05 Des-Other2                   pic x(10).

       01 Other-Record.
          05 Des-Other1                   pic x(10).
          05 Des-Other2                   pic x(10).
          05 Tab1                         pic x.
          05 Des-Name                     pic x(40).
          05 Tab2                         pic x.
          05 Des-Code                     pic x(04).

and the method :-

*>----------------------------------------------------------
Method-id. "makeListRecord".
*>----------------------------------------------------------
Local-storage section.
01 ls-length                     pic x(4) comp-5.
Linkage section.
01 lnk-string                    object reference.

Procedure division returning lnk-string.

move length of Name-record to ls-length

if TypeTabbed
    move x'09' to Tab1 of ws-DesListRecord
                  Tab2 of ws-DesListRecord
End-if

Evaluate true
  when ByName
    move CORR ws-DesListRecord to Name-record
    invoke CharacterArray "withLengthValue" using
       ls-length, Name-record returning lnk-string
  when ByKey
    move CORR ws-DesListRecord to Key-record
    invoke CharacterArray "withLengthValue" using
       ls-length, Key-record returning lnk-string
  when other
    move CORR ws-DesListRecord to Other-record
    invoke CharacterArray "withLengthValue" using
       ls-length, Other-record returning lnk-string
End-evaluate

End Method "makeListRecord".
*>----------------------------------------------------------

It does it, but I'm not too thrilled about all the qualification, e.g. MOVE ABC
of XYZRecord to DEF of PQR record, sometimes required elsewhere in a program.

Jimmy
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 4)_

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2001-12-24T14:47:38-09:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C27BE9A.47619AEA@dced.state.ak.us>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com>`

```
JerryMouse wrote:

> ## And to answer yout question about why COMP-3 is still used, this day in
> age, what with electric lights and indoor plumbing, there are two answers:
…[3 more quoted lines elided]…
> use it every day (and I'm not exaggerating).

As an example, I ported a system written in the late 70's from a mainframe to a
LAN. COMP-3 fields were a pain, so I (mostly) eliminated them in the port. But
that left 20 years worth of archive tapes which now had to be converted, too.
(They needed to be converted anyway-we could have 'institutionalized' the EBCDIC
to ASCII conversion process, but felt it was better to convert to new tapes &
get it over with.)

Anyway, we discovered that there were some undocumented changes in the record
formats back in the early 80's. Now I still have a half-dozen EBCDIC tapes on my
desk that I'm gradually converting to ASCII, and unpacking the COMP-3 fields in
the process. It's a good thing I worked on the system in the (late) 80's. The
programmers we're getting today wouldn't have a clue how to handle this problem.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 5)_

- **From:** "JerryMouse" <news@bisusa.com>
- **Date:** 2001-12-25T14:01:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KE%V7.227217$C8.15731770@bin4.nnrp.aus1.giganews.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3C27BE9A.47619AEA@dced.state.ak.us>`

```

"Calvin Crumrine" <Calvin_Crumrine@dced.state.ak.us> wrote in message
news:3C27BE9A.47619AEA@dced.state.ak.us...
> JerryMouse wrote:
>
> > ## And to answer yout question about why COMP-3 is still used, this day
in
> > age, what with electric lights and indoor plumbing, there are two
answers:
> > 1. There are still decimal arithmetic circuits in use, so COMP-3 is more
> > efficient than other renditions, and
> > 2. There hundreds of billions of records and billions of lines of code
that
> > use it every day (and I'm not exaggerating).
>
> As an example, I ported a system written in the late 70's from a mainframe
to a
> LAN. COMP-3 fields were a pain, so I (mostly) eliminated them in the port.
But
> that left 20 years worth of archive tapes which now had to be converted,
too.

Assuming 1 backup per day for 20 years = 7300 tapes. At 25 Mbytes/tape,
that's (mumble, mumble, ignore leap years, carry the two...) 182,500,000,000
bytes worth of data to be converted. At six minutes per tape, that's one
month of 24-hours days to perform the conversion. In one shop. For one
system. By one person. In addition to other duties.

Why not just ditch COMP-3 indeed!
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2001-12-25T09:13:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a0a1hl$c3s$1@panix3.panix.com>`
- **References:** `<3c250264.895577@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3C27BE9A.47619AEA@dced.state.ak.us> <KE%V7.227217$C8.15731770@bin4.nnrp.aus1.giganews.com>`

```
In article <KE%V7.227217$C8.15731770@bin4.nnrp.aus1.giganews.com>,
JerryMouse <news@bisusa.com> wrote:
>
>"Calvin Crumrine" <Calvin_Crumrine@dced.state.ak.us> wrote in message
>news:3C27BE9A.47619AEA@dced.state.ak.us...

[snippage]

>> As an example, I ported a system written in the late 70's from a mainframe to a
>> LAN. COMP-3 fields were a pain, so I (mostly) eliminated them in the port. But
…[8 more quoted lines elided]…
>Why not just ditch COMP-3 indeed!

How interesting... and here I was thinking that *I* was the only one who 
did this kind of time-analysis when it came to tasks.

You haven't happened to have read 'The Principles of Scientific 
Management' by Frederick Winslow Taylor, have you?  (although the logical 
end of this work is that of reducing Man to a machine there is much of 
value to be found along the way... I try to remember Vonnegut's 
description of beautiful roses being grown in pure cat excrement)

DD
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 7)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-12-25T09:46:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qf0W7.10611$u93.1217746@news20.bellglobal.com>`
- **References:** `<3c250264.895577@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3C27BE9A.47619AEA@dced.state.ak.us> <KE%V7.227217$C8.15731770@bin4.nnrp.aus1.giganews.com> <a0a1hl$c3s$1@panix3.panix.com>`

```
<docdwarf@panix.com> wrote in message news:a0a1hl$c3s$1@panix3.panix.com...
> In article <KE%V7.227217$C8.15731770@bin4.nnrp.aus1.giganews.com>,
> JerryMouse <news@bisusa.com> wrote:
…[6 more quoted lines elided]…
> >> As an example, I ported a system written in the late 70's from a
mainframe to a
> >> LAN. COMP-3 fields were a pain, so I (mostly) eliminated them in the
port. But
> >> that left 20 years worth of archive tapes which now had to be
converted, too.
> >
> >Assuming 1 backup per day for 20 years = 7300 tapes. At 25 Mbytes/tape,
> >that's (mumble, mumble, ignore leap years, carry the two...)
182,500,000,000
> >bytes worth of data to be converted. At six minutes per tape, that's one
> >month of 24-hours days to perform the conversion. In one shop. For one
…[13 more quoted lines elided]…
> DD


Just think, Doc.  They could have done all that backup to the net at 9600
baud, and saved themselves all the problem of reading tapes.<G>

Donald
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2001-12-25T10:53:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a0a7e1$icb$1@panix3.panix.com>`
- **References:** `<3c250264.895577@news.libero.it> <KE%V7.227217$C8.15731770@bin4.nnrp.aus1.giganews.com> <a0a1hl$c3s$1@panix3.panix.com> <qf0W7.10611$u93.1217746@news20.bellglobal.com>`

```
In article <qf0W7.10611$u93.1217746@news20.bellglobal.com>,
Donald Tees <donald_tees@sympatico.ca> wrote:
><docdwarf@panix.com> wrote in message news:a0a1hl$c3s$1@panix3.panix.com...
>> In article <KE%V7.227217$C8.15731770@bin4.nnrp.aus1.giganews.com>,
…[31 more quoted lines elided]…
>baud, and saved themselves all the problem of reading tapes.<G>

Where *did* you study DP, Mr Tees?  Disk has to be kept open for swap 
files; *everything else* goes to - and, as a result, comes from - tape, 
period.

What's next... telling me that the RESERVE nn AREAS isn't needed?  Granted 
it eats up a little core, sure, but you get a good SysJock in there to 
optimise IO and even for SORTs three... all right, *four* drives is all 
we'll ever need!

DD
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 9)_

- **From:** "JerryMouse" <news@bisusa.com>
- **Date:** 2001-12-25T23:47:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<se8W7.43742$m05.3615101@bin5.nnrp.aus1.giganews.com>`
- **References:** `<3c250264.895577@news.libero.it> <KE%V7.227217$C8.15731770@bin4.nnrp.aus1.giganews.com> <a0a1hl$c3s$1@panix3.panix.com> <qf0W7.10611$u93.1217746@news20.bellglobal.com> <a0a7e1$icb$1@panix3.panix.com>`

```

<docdwarf@panix.com>

> What's next... telling me that the RESERVE nn AREAS isn't needed?  Granted
> it eats up a little

"core,"      <how quaint, almost cuddly>

sure, but you get a good SysJock in there to
> optimise IO and even for SORTs three... all right, *four* drives is all
> we'll ever need!
>
> DD
>
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2001-12-25T20:07:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a0b7tf$5v3$1@panix3.panix.com>`
- **References:** `<3c250264.895577@news.libero.it> <qf0W7.10611$u93.1217746@news20.bellglobal.com> <a0a7e1$icb$1@panix3.panix.com> <se8W7.43742$m05.3615101@bin5.nnrp.aus1.giganews.com>`

```
In article <se8W7.43742$m05.3615101@bin5.nnrp.aus1.giganews.com>,
JerryMouse <news@bisusa.com> wrote:
>
><docdwarf@panix.com>
…[4 more quoted lines elided]…
>"core,"      <how quaint, almost cuddly>

Gosh... I'd blush, were I able to remember how.

DD
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 7)_

- **From:** "JerryMouse" <news@bisusa.com>
- **Date:** 2001-12-25T23:52:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2j8W7.336608$uB.34473609@bin3.nnrp.aus1.giganews.com>`
- **References:** `<3c250264.895577@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3C27BE9A.47619AEA@dced.state.ak.us> <KE%V7.227217$C8.15731770@bin4.nnrp.aus1.giganews.com> <a0a1hl$c3s$1@panix3.panix.com>`

```

<docdwarf@panix.com>
>
> How interesting... and here I was thinking that *I* was the only one who
> did this kind of time-analysis when it came to tasks.

Ah ha! I always thought you thought you were unique.

>
> You haven't happened to have read 'The Principles of Scientific
> Management' by Frederick Winslow Taylor, have you?

No, but I did have a math/physics teacher who pounded us to estimate the
answer before attempting to solve the problem - sort of 'back of the
envelope' solutions (which, as it turns out, are often good enough).
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2001-12-25T20:24:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a0b8rq$7f3$1@panix3.panix.com>`
- **References:** `<3c250264.895577@news.libero.it> <KE%V7.227217$C8.15731770@bin4.nnrp.aus1.giganews.com> <a0a1hl$c3s$1@panix3.panix.com> <2j8W7.336608$uB.34473609@bin3.nnrp.aus1.giganews.com>`

```
In article <2j8W7.336608$uB.34473609@bin3.nnrp.aus1.giganews.com>,
JerryMouse <news@bisusa.com> wrote:
>
><docdwarf@panix.com>
…[4 more quoted lines elided]…
>Ah ha! I always thought you thought you were unique.

Note the qualifier of 'when it came to tasks'... the situation is an 
unique one.

>
>>
…[5 more quoted lines elided]…
>envelope' solutions (which, as it turns out, are often good enough).

Aye... consider:

'It shouldn't take so long to...'

'Well, to do the task a single time takes (m) seconds... and there are (n) 
instances of the task... and there are 28,800 second in an 8-hr working 
day... so assuming no coffee breaks, no distractions and the ability to 
perform the same taks repeatedly with no degradation in time or quality it 
will take one person (m*n)/28,800 days.'

'That can't be right!'

'Those are the numbers and assumptions; if you - or anyone else - can use 
them to generate a different conclusion the I should *very* much like to 
see it.'

'You're not being very helpful.'

'I'm being factual... you want help, call some nuns.'

(side note - this same approach, when applied to the question of what 
salary it would take to get me to shift from consultant to employee in 
Manhattan, would generate slack-jawed amazement; I would base my figures 
on two facts and one assumption:

Fact: the Federal Housing Authority (FHA) recommends that housing ans 
associated expenses consume no more than 25% - 33% of one's income.

Fact: an average one-bedroom apartment in Manhattan costs (US$x).

Assumption: It is a Good and Proper Thing for a company to pay a skilled, 
technical employee enough to afford at *least* an average, one-bedroom in 
the town in which s/he is expected to work.)

DD
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 6)_

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2001-12-26T08:32:03-09:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C2A0993.339A6502@dced.state.ak.us>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3C27BE9A.47619AEA@dced.state.ak.us> <KE%V7.227217$C8.15731770@bin4.nnrp.aus1.giganews.com>`

```
JerryMouse wrote:

> Assuming 1 backup per day for 20 years = 7300 tapes. At 25 Mbytes/tape,
> that's (mumble, mumble, ignore leap years, carry the two...) 182,500,000,000
…[4 more quoted lines elided]…
> Why not just ditch COMP-3 indeed!

Yes, very time consuming. Would I have done it *just* to ditch COMP-3? No way!
But, as I pointed out, we needed to convert the tapes anyway due to the system
port so it was fairly easy to incorporate the conversion from COMP-3, and IMO it
made sense to do so. (BTW, we only kept daily backups for 2 weeks. Beyond that
it was monthly backups. Part of the reason for the port was to get better backup
retention without excessively increasing costs. I was just assigned the task of
doing the port, not of analyzing whether or not it was worthwhile.)
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 5)_

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-12-25T21:24:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C295EF9.2BBA@paralynx.com>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <3c25b8b0.5816643@news.libero.it> <0OyV7.313040$uB.33224317@bin3.nnrp.aus1.giganews.com> <3C27BE9A.47619AEA@dced.state.ak.us>`

```
Calvin Crumrine wrote:
> 
> JerryMouse wrote:
…[13 more quoted lines elided]…
> get it over with.)

I'm amazed that you still had a drive which could read them without wrecking them. The 
older tapes were usually of a softer "emulsion" and today's heads would probably 
seriously damage them.  (A few years ago an EDP audit group I managed did an audit of 
tape retention and found this one.)
```

##### ↳ ↳ Re: first conversion program: disaster

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 2001-12-23T22:10:55+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a05h9k$mnm$1@oslo-nntp.eunet.no>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com>`

```
"JerryMouse" <news@bisusa.com> wrote
> No other common language of which I am aware can handle the
> precision built into COBOL (18+ decimal digits of precision).

You might want to know that the latest Cobol compiler for IBM mainframe
(V2.2) will handle decimal numbers up to 31 digits, which is also the limit
of the hardware decimal instructions (has been so since S/360).

Gunnar.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-12-25T19:26:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a0b9i5$314$1@slb4.atl.mindspring.net>`
- **References:** `<3c250264.895577@news.libero.it> <l1aV7.86001$Zd.8193582@bin1.nnrp.aus1.giganews.com> <a05h9k$mnm$1@oslo-nntp.eunet.no>`

```
31 digits is ALSO the amount that will be required by the next COBOL
Standard (even for operating systems without such "built-in" support)
```

#### ↳ Re: first conversion program: disaster

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-12-22T18:54:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C254772.64A3@paralynx.com>`
- **References:** `<3c250264.895577@news.libero.it>`

```
Duilio Foschi wrote:
> 
> I have studied Cobol the whole day.
> 
> My purpose is to write a conversion routine that will trasform weird
> COMP-3 records in plain old ASCII data.

If all you want is to convert the data (not use it simply as an exercise to learn 
COBOL), why not just use an existing conversion program like ParseRat 
(http://www.parserat.com/) in its generic binary mode?
```

##### ↳ ↳ Re: first conversion program: disaster

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-23T10:18:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c25abb3.2491452@news.libero.it>`
- **References:** `<3c250264.895577@news.libero.it> <3C254772.64A3@paralynx.com>`

```
Ed,

>why not just use an existing conversion program like ParseRat 

for several reasons (mostly due to my ignorance of the product):

1. data is in SCO-Unix and have no idea if ParseRat will work on it

2. there is a working Microfocus compiler in the SCO-Unix box

3. ParseRat could be expensive 

4. ParseRat could be difficult to get 

5. ParseRat could be difficult to learn and I don't want to spend time
in learning a tool I won't use in the future

6. ParseRat could not work 

7. I already program in a number of languages, so I was not scared at
the idea of learning a bit of Cobol

8. I can reuse the time spent in learning a bit of Cobol

9. a number of people in this NG adviced me to take the road I took

Thank you 

Duilio
```

#### ↳ Re: first conversion program: disaster

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-12-23T11:37:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20011223063758.28453.00000521@mb-co.aol.com>`
- **References:** `<3c250264.895577@news.libero.it>`

```
In article <3c250264.895577@news.libero.it>, dedalus@yifan.net (Duilio Foschi)
writes:

>
>As I have no idea how to write COMP-3 data, I began doing the
>opposite, i.e. converting ASCII numbers into their COMP-3
>counterpart.
>

Your results are exactly as would be expected from a GROUP LEVEL
move, which acts like a character move.
The input record is defined as 9 char, but the output record is 
defined as only 5 char in size.  I am not at all sure how you manage to 
get the 9 on a separate record.
Try using an elementary level move and see if your results are more
in line with expectations.
```

#### ↳ Re: first conversion program: disaster

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2001-12-23T11:37:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a050nf$r7k$1@slb7.atl.mindspring.net>`
- **References:** `<3c250264.895577@news.libero.it>`

```
When you move group to group, there is no conversion. Instead, try the
following:

MOVE QTA OF IN-REC TO QTA OF OUT-REC.

This should solve your problem.

Happy Holidays,

Bill

< Rest Snipped>
```

#### ↳ Re: first conversion program: disaster

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-12-23T16:45:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8TnV7.8746$XC5.10013@www.newsranger.com>`
- **References:** `<3c250264.895577@news.libero.it>`

```
I know this might seem obvious - but you are half way there.  Why not use a
COBOL program like the one you wrote to read the records with COMP-3 data and
write them as PIC 99999999.99- (Use appropriate number of digits and decimals)
fields and be done with it?



In article <3c250264.895577@news.libero.it>, Duilio Foschi says...
>
>I have studied Cobol the whole day.
…[90 more quoted lines elided]…
>
```

##### ↳ ↳ Re: first conversion program: disaster

- **From:** stephenjspiro@mail.com (Stephen J Spiro)
- **Date:** 2001-12-23T13:27:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<928495c6.0112231327.635f0291@posting.google.com>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com>`

```
A warning:
"Packed" is NOT a standard format. That is, it's existence and
behavior is in the Standard (all genuflect), but the format is not
specified.  The format of packed data varies from processor to
processor.  What you have is NOT the same as IBM mainframe or NCR, for
instance.

Stephen J Spiro
Member, ANSI COBOL Standards Committee
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-23T22:20:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c265742.46416512@news.libero.it>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com>`

```
>all genuflect

LOL

>What you have is NOT the same as IBM mainframe or NCR, for instance.

ok, I got it

Thank you and merry XMas

Duilio
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-25T16:48:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c28aae0.32743857@news.libero.it>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com>`

```
>The format of packed data varies from processor to processor.  

can I expect that in the Intel world all packed data has the same
format ?

A Fujitsu 85 compiler and a Microfocus compiler seem to format data
differently.

The o.s. is different, the processor is Intel in both cases.

Or I could have messed up the code, of course :)

Thank you

Duilio Foschi
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 4)_

- **From:** "JerryMouse" <news@bisusa.com>
- **Date:** 2001-12-25T23:58:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ro8W7.231775$C8.16041244@bin4.nnrp.aus1.giganews.com>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com> <3c28aae0.32743857@news.libero.it>`

```

"Duilio Foschi" <dedalus@yifan.net> wrote in message
news:3c28aae0.32743857@news.libero.it...
> >The format of packed data varies from processor to processor.
>
> can I expect that in the Intel world all packed data has the same
> format ?

Probably not inasmuch as packed data make no intrinsic sense to an Intel
chip. It was the early mainframes that had circuitry to manipulate packed
data. For Intel machines, the compiler must generate code to convert packed
data into something else it can handle then convert the result back to the
pre-defined format. The Fujitsu and Realia compilers mimic IBM mainframe
renditions of COMP-3; I have no idea about the others.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 5)_

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 2001-12-27T23:47:05+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a0g8ea$kco$1@oslo-nntp.eunet.no>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com> <3c28aae0.32743857@news.libero.it> <Ro8W7.231775$C8.16041244@bin4.nnrp.aus1.giganews.com>`

```

"JerryMouse" <news@bisusa.com> wrote in message
news:Ro8W7.231775$C8.16041244@bin4.nnrp.aus1.giganews.com...
>
> "Duilio Foschi" <dedalus@yifan.net> wrote in message
…[8 more quoted lines elided]…
> data. For Intel machines, the compiler must generate code to convert
packed
> data into something else it can handle then convert the result back to the
> pre-defined format. The Fujitsu and Realia compilers mimic IBM mainframe
> renditions of COMP-3; I have no idea about the others.

Intel chips has had a native packed decimal format ever since the 8087.  It
is 10 bytes (80 bits): 1 bit sign, 7 unused bits (zero), and 18 4-bit
BCD-coded decimal digits.  This (18 digits) conforms to the Cobol standard
so far (coincidence?).  Two instructions (FBSTP and FBLD) can convert
between this format and extended precision float, but there are no
instructions for packed decimal computation (except an awkward add/subtract
plus adjust, one byte at a time).

The IBM S/360-370-390 and z900 packed decimal format is 1 to 16 bytes, which
contains up to 31 4-bit BCD-coded digits and a 4-bit sign code.  Several
instructions can compute in this format, or convert to/from binary or zoned
format.

The sequence of the digits is of course opposite, and the sign is on the
other end as well.

The compilers may of course use an other format, but to produce efficient
code they better use the native format, which they do in the IBM mainframe
case.  I know nothing about how Intel-based compilers treat packed decimal.

Gunnar.
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-12-26T13:32:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ckkW7.50$mq1.20752@dfiatx1-snr1.gtei.net>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com> <3c28aae0.32743857@news.libero.it>`

```
Duilio Foschi <dedalus@yifan.net> wrote in message
news:3c28aae0.32743857@news.libero.it...
> >The format of packed data varies from processor to processor.
>
> can I expect that in the Intel world all packed data has the same
> format ?

"Packed" data format is a function of the application (e.g., a compiler),
not a function of the chip.

COBOL binary data, for example, are stored MSB-LSB regardless of the
hardware.

COBOL COMP-3 or PACKED-DECIMAL data are stored based on the compiler
("implementor-defined").

So the answer to your question is "no."

For more info on data storage, see my free tutorials at:

http://www.flexus.com/downloads.html file COBDATA.ZIP is a text and graphics
tutorial covering bit patterns, etc.

http://www.flexus.com/ebd2asc.html is a "conversion" guide which includes
character set and COBOL-IEEE data type considerations.

(Sheesh, I really should update that first one, and then maybe combine the
two pieces into one? Comments, anyone?)
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-12-26T13:44:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WukW7.361$LY2.85189@paloalto-snr1.gtei.net>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com> <3c28aae0.32743857@news.libero.it> <ckkW7.50$mq1.20752@dfiatx1-snr1.gtei.net>`

```
Michael Mattias <michael.mattias@gte.net> wrote in message
news:ckkW7.50$mq1.20752@dfiatx1-snr1.gtei.net...
> For more info on data storage, see my free tutorials at:
>
> http://www.flexus.com/downloads.html file COBDATA.ZIP is a text and
graphics
> tutorial covering bit patterns, etc.

   CORRECT LINK IS http://www.flexus.com/download.html

MCM
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 6)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-12-27T12:54:22+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c2a661b_3@Usenet.com>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com> <3c28aae0.32743857@news.libero.it> <ckkW7.50$mq1.20752@dfiatx1-snr1.gtei.net> <WukW7.361$LY2.85189@paloalto-snr1.gtei.net>`

```
Michael,

as you have provided these files for free and I understand a number of
people have used them, I suggest the following:

1. Keep them as they are on your own download site so that anyone who wants
to can see the originals.

2. One rainy Sunday when you have nothing better to do, revise, condense,
and combine them into one download and give it to Bill for inclusion with
the COBOL FAQ. (Don't sweat it...)

The point is that you should not incur an onerous workload for something you
are doing out of the goodness of your heart.

As many new people are picking up COBOL and it is desirable that we should
all encourage them to do so, it is likely that we will see many further
requests for information about Packed, Binary, and even Floating point
formats in COBOL.

The formats can be easily described in a couple of paragraphs, but the
newbie needs code samples to really understand what is happening (Standards
writers, please take note...). A long time ago I remember spending an
afternoon writing a document describing these formats to Jimmy Gavan. It is
difficult for people (even good programmers like Jimmy) who have not had
mainframe exposure, to understand what, why, and how, things like packed
decimal work.

I believe there is really not much point in responding every time someone in
CLC asks the question. It is a true "Frequently  Asked" question and
properly belongs on a FAQ.

(Maybe we need a standard response like the one Doc uses when people post
Jobs that don't quote rates, something like: "Your request for COBOL
information is covered in the COBOL FAQ. Please go to [wherever Bill is
keeping it these days] and you will find answers and code samples to help
you. If you still have questions, post specific inquiries, along with a copy
of your code where appropriate, in this Newsgroup.")

In passing, I would suggest that we should actively promote the COBOL FAQ
and route people to it as a first point of contact, THEN discuss any
remaining questions in CLC.

That way we prevent the NG from stagnating. (Repetitive posts are one of the
quickest ways to kill interest in any forum...)

For myself, I will be happy to contribute documents and code to the FAQ if
it is not currently equipped to serve its intended purpose.

I would also like to see a downloadable on-line Help file or HTML document
with "quick answers" (summaries in plain English, with code samples, and
hyperlinked references to pertinent "See Also..."s ) for COBOL.

(This is something I have had on a "back burner" for some time; if anyone is
interested in helping with this, please contact me privately. I see
something that will be freely distributed as "Quick COBOL Help". Wherever
possible it will be non-platform specific, but examples that utilise a
particular platform could be colour coded. Different people could contribute
different samples. If we had 30 people contributing 3 hours a week to this,
for a couple of months, we could produce something very useful without
anyone being unduly burdened...If there is no support for it, I'll do it
myself as a retirement project <G>, but that means that you won't see it for
some years yet...)

Pete.

Michael Mattias <michael.mattias@gte.net> wrote in message
news:WukW7.361$LY2.85189@paloalto-snr1.gtei.net...
> Michael Mattias <michael.mattias@gte.net> wrote in message
> news:ckkW7.50$mq1.20752@dfiatx1-snr1.gtei.net...
…[11 more quoted lines elided]…
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 7)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-12-26T19:12:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uEtW7.16918$eo1.2080486@news20.bellglobal.com>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com> <3c28aae0.32743857@news.libero.it> <ckkW7.50$mq1.20752@dfiatx1-snr1.gtei.net> <WukW7.361$LY2.85189@paloalto-snr1.gtei.net> <3c2a661b_3@Usenet.com>`

```
Somewhat germaine to the below, does anybody have an ascii list of links for
some of the more common stuff?  Being able to post it into a message fast is
certainly an easy way of responding.

Donald

"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:3c2a661b_3@Usenet.com...
> Michael,
>
…[3 more quoted lines elided]…
> 1. Keep them as they are on your own download site so that anyone who
wants
> to can see the originals.
>
…[4 more quoted lines elided]…
> The point is that you should not incur an onerous workload for something
you
> are doing out of the goodness of your heart.
>
…[6 more quoted lines elided]…
> newbie needs code samples to really understand what is happening
(Standards
> writers, please take note...). A long time ago I remember spending an
> afternoon writing a document describing these formats to Jimmy Gavan. It
is
> difficult for people (even good programmers like Jimmy) who have not had
> mainframe exposure, to understand what, why, and how, things like packed
> decimal work.
>
> I believe there is really not much point in responding every time someone
in
> CLC asks the question. It is a true "Frequently  Asked" question and
> properly belongs on a FAQ.
…[5 more quoted lines elided]…
> you. If you still have questions, post specific inquiries, along with a
copy
> of your code where appropriate, in this Newsgroup.")
>
…[4 more quoted lines elided]…
> That way we prevent the NG from stagnating. (Repetitive posts are one of
the
> quickest ways to kill interest in any forum...)
>
…[7 more quoted lines elided]…
> (This is something I have had on a "back burner" for some time; if anyone
is
> interested in helping with this, please contact me privately. I see
> something that will be freely distributed as "Quick COBOL Help". Wherever
> possible it will be non-platform specific, but examples that utilise a
> particular platform could be colour coded. Different people could
contribute
> different samples. If we had 30 people contributing 3 hours a week to
this,
> for a couple of months, we could produce something very useful without
> anyone being unduly burdened...If there is no support for it, I'll do it
> myself as a retirement project <G>, but that means that you won't see it
for
> some years yet...)
>
…[25 more quoted lines elided]…
>                 http://www.usenet.com
```

###### ↳ ↳ ↳ Re: first conversion program: disaster

_(reply depth: 7)_

- **From:** "warren.simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2001-12-27T03:49:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BTwW7.199367$WW.11558073@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com> <3c28aae0.32743857@news.libero.it> <ckkW7.50$mq1.20752@dfiatx1-snr1.gtei.net> <WukW7.361$LY2.85189@paloalto-snr1.gtei.net> <3c2a661b_3@Usenet.com>`

```
Peter, Jimmy, and Others,

This is a great idea. In the TC project such a reference is badly needed as
well. A few of this
group have shown interest in that need. It seems that anything that could be
freely downloaded
could be considered as fodder for this kind of activity. Sections of the
200x document might
be good targets for inclusion as well when it modifys the current standard.
It might be possible
to illustrate the variations supported, and comment on the amount of effort
they place on
movement between compilers.  A lot of the questions have  been in this area.

Warren Simmons
warren.simmons@worldnet.att.net
warren@tinycobol.org

Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote in message
news:3c2a661b_3@Usenet.com...
> Michael,
>
…[3 more quoted lines elided]…
> 1. Keep them as they are on your own download site so that anyone who
wants
> to can see the originals.
>
…[4 more quoted lines elided]…
> The point is that you should not incur an onerous workload for something
you
> are doing out of the goodness of your heart.
>
…[6 more quoted lines elided]…
> newbie needs code samples to really understand what is happening
(Standards
> writers, please take note...). A long time ago I remember spending an
> afternoon writing a document describing these formats to Jimmy Gavan. It
is
> difficult for people (even good programmers like Jimmy) who have not had
> mainframe exposure, to understand what, why, and how, things like packed
> decimal work.
>
> I believe there is really not much point in responding every time someone
in
> CLC asks the question. It is a true "Frequently  Asked" question and
> properly belongs on a FAQ.
…[5 more quoted lines elided]…
> you. If you still have questions, post specific inquiries, along with a
copy
> of your code where appropriate, in this Newsgroup.")
>
…[4 more quoted lines elided]…
> That way we prevent the NG from stagnating. (Repetitive posts are one of
the
> quickest ways to kill interest in any forum...)
>
…[7 more quoted lines elided]…
> (This is something I have had on a "back burner" for some time; if anyone
is
> interested in helping with this, please contact me privately. I see
> something that will be freely distributed as "Quick COBOL Help". Wherever
> possible it will be non-platform specific, but examples that utilise a
> particular platform could be colour coded. Different people could
contribute
> different samples. If we had 30 people contributing 3 hours a week to
this,
> for a couple of months, we could produce something very useful without
> anyone being unduly burdened...If there is no support for it, I'll do it
> myself as a retirement project <G>, but that means that you won't see it
for
> some years yet...)
>
…[25 more quoted lines elided]…
>                 http://www.usenet.com
```

###### ↳ ↳ ↳ COBOl Examples WAS - Re: first conversion program: disaster

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-12-27T19:08:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C2B7250.D5747296@shaw.ca>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com> <3c28aae0.32743857@news.libero.it> <ckkW7.50$mq1.20752@dfiatx1-snr1.gtei.net> <WukW7.361$LY2.85189@paloalto-snr1.gtei.net> <3c2a661b_3@Usenet.com> <BTwW7.199367$WW.11558073@bgtnsc05-news.ops.worldnet.att.net>`

```
"Earwigo again" said the earwig as it fell off the wall <G>. We are back on my
favourite topic - COBOL examples. I think this to be an absolute MUST if we want
COBOL to survive.

"warren.simmons" wrote:

> Peter, Jimmy, and Others,
>
…[15 more quoted lines elided]…
>

-------------------------------------------------------------------------------
Warren,

Reminds me that a message I sent to you was undelivered. Here is a repeat and
others may care to comment :-

*>---------------------------------------------------------------------------------

subject:
        COBOL Users' Manual
   Date:
        Tue, 06 Nov 2001 22:35:44 -0700
   From:
        "James J. Gavan" <jjgavan@shaw.ca>
     To:
        Warren Simmons <warren@tinycobol.org>
    CC:
        "William M. Klein" <wmklein@ix.netcom.com>

Warren,

Care to spell out what you think you want to cover ? I'm including Bill
on this because he possibly has already communicated with you and may
want to add/change to what I put below. I don't know if you are aware
but J4 have accepted 'in principle' that there should be an 'Examples
Book'. But with the usual alacrity, I don't see it happening any time
soon !.

Attempting a DETAILED Users' Manual is a pretty tall order - so I would
suggest it should be a prï¿½cis mainly SUPPORTED by coding examples
illustrating all the features.

Contents - my contention - it should only acknowledge COBOL '97 and
later - it should be pointing at the newbies coming up, if we want COBOL to
survive. Bill knows I don't like the current J4 sequence of contents and I would
prefer to see it go by discrete topics.

1. Structure of a Program - contains all Divisional features. From
thereon in, like the Micro Focus concept, examples should ignore the red
tape where it isn't required to illustrate how you do something. All the
verbiage detracts from what you are trying to put across. (If you look
at the J4 examples for OO all the program syntax is there distracting
you from the real purpose of the examples).

2. Numbers/numerics - how we describe, use etc. Include the VERBS that
manipulate numbers - add/subtract/divide/compute etc... and
cross-reference to intrinsice below. (Or maybe it is the other way
around - incude the appropriate numeric intrinsics in here and cross
reference them under Intrinsics)..

3. Text - ditto. (Again possibly text intrinsics should appear here).

An example which fits under this one, which I wrote this last week, to
find out what MOVE CORRESPONDING does :-
-------------------------
Program-id. MoveCorr.

01 A-record.
   05 anItem1           pic x(03) value all "x".
   05 aKey              pic x(05) value 'A0635'.
   05 anItem2           pic x(03) value all ">>>".
   05 aName             pic x(20) value "John".
   05 anItem3           pic x(03) value "<<<".
   05 aDept             pic x(10) value "Marketing".
   05 anItem4           pic x(03) value all "***".

01 Key-record.
   05 aKey              pic x(05).
   05 aName             pic x(20).
   05 aDept             pic x(10).

01 Name-record.
   05 aName             pic x(20).
   05 aKey              pic x(05).
   05 aDept             pic x(10).

01 Dept-record.
   05 aDept             pic x(10).
   05 aName             pic x(20).
   05 aKey              pic x(05).

move corresponding a-record to Key-record
move corresponding a-record to Name-record
move corresponding a-record to Dept-record
display "Original :- " a-record
display "By Key   :- " Key-record
display "By Name  :- " Name-record
display "By Dept  :- " Dept-record

STOP RUN.
------------------

Note 'shorthand' above - No Divisions/Sections etc......

The above example is NOT exhaustive and additional examples need to
illustrate where you use packed numerics etc.

4. Screen Section - perhaps iffy, but newbies *might* find it useful for
very basic program construction.

5. File Section - just referred somebody to Limerick - check out the
examples at

    www.csis.ul.ie/COBOL/examples/

The author is Michael Coughlan. Should be able to get his permission to
include, plus also allowing you to 'change'. Limerick will be giving up
on COBOL within the next 12 months or less.

Would suggest ALL examples make use of file-status, showing, initially,
calling a File Error program - again, initially Standard File-status
codes, and perhaps later, vendor extensions.

By far and away File Section should be a real biggie.

5A. Printing - because it is associated with file handling.

5B. To keep Bill happy <G> - Report Writer.

6. Table and Subscript handling, indexing, SEARCHING etc.

7. Declaratives - not sure where this one goes as it has so many
possibilities - any thoughts Bill ?

8. Intrinsic functions - break these down into groups, e.g. date
functions, numeric, text handling and statistical functions etc. A good
source here would be Jerry Garfunkel - wrote some sample source quite a
while back, covering them all.

8. Wish List - put these on the back burner, you will have more than
enough to do at this stage :-

8(b) New COBOL 2002 features - like the VALIDATE verb.( Note - any
innovations in COBOL 2002 that affect the earlier categories should
include new 2002 syntax provided). (*** Late note - Gary de Ward Brown did an
article on  the new VALIDATE for cobolreport.com ***)

8(b) OO, CGI, HTML and all the other OLE and Web jazz. They are very
IMPORTANT - but not until you've done the groundwork on the above.
(Hopefully, by the time you have a semblance of Items 1 through 7, J4
will have firmed up on standard classes/collections - and then it allows
for examples to cover these).

Those are my initial thoughts - so how do they tie in with your thinking
?

Jimmy

*>----------------------------------------------------------------------------------

I can add other comments later. With refence to Pete's message to Michael, I
excpect he can dig out his paper on numeric usage - if not I can dig it out of
my archives. On further thoughts, an obvious area to add is a set of basic
examples for ESQL - couched in generalised syntax which makes the examples, (as
near as possible), apply to all flavours of DBs.

Jimmy, Calgary AB
..................

> Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote in message
> news:3c2a661b_3@Usenet.com...
…[100 more quoted lines elided]…
> >                 http://www.usenet.com
```

###### ↳ ↳ ↳ Re: COBOl Examples WAS - Re: first conversion program: disaster

_(reply depth: 9)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-12-28T12:44:27+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c2bb398_11@Usenet.com>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com> <3c28aae0.32743857@news.libero.it> <ckkW7.50$mq1.20752@dfiatx1-snr1.gtei.net> <WukW7.361$LY2.85189@paloalto-snr1.gtei.net> <3c2a661b_3@Usenet.com> <BTwW7.199367$WW.11558073@bgtnsc05-news.ops.worldnet.att.net> <3C2B7250.D5747296@shaw.ca>`

```
I think it's really important NOT to be too ambitious with this.

Try and imagine a newbie who wants an overview of how you do stuff and the
basic constructs that should work on ANY platform.

Think "COBOL Reference Card" rather than "COBOL User's Guide".

For the standard, by all means contribute detailed examples. As a matter of
principle I won't do this, but there is no reason why others shouldn't.

(I WOULD do it if there was no attempt to copyright the COBOL Standard, if
the Organisation concerned showed some readiness to review and improve its
internal procedures, if there was some answerability to the COBOL Community,
and if, instead of patting themselves on the back for the "great job" they
have done, they accepted responsibility for their failure and showed what
measures they are taking to ensure that it never happens again ... As this
seems to be too big an ask, don't expect contributions from me any time
soon...)

Given the above, I don't agree with COBOL 97 or the new 200x or whatever as
being the basis (although I understand and sympathise with your intentions,
Jimmy.) I think it needs to be BASIC, SIMPLE, and available on MOST
platforms. The particular "flavour" (year) is irrelevant.

I REALLY like the idea of hyperlink references to other sources you
described, but now we are coming to a Web Site rather than a downloadable
HELP file. Maybe that is the answer. In this age of connectivity, there is
no reason why we can't have a COBOL tutorial/quick reference on the Web that
anyone can refer to when they need to. Maybe BOTH a web site AND a
downloadable Win Help file would be valuable.

At this point I stopped and thought..."Somebody must have already done
this...". Ran a Google search on "COBOL Tutorial" and, sure enough, there
are dozens of 'em! I looked at four or five and was impressed.

Given the high standard of the material available, I think we would just be
"re-inventing the wheel".

At some point, a downloadable Quick Reference, in the form of  WinHELP or
HTML, with links to some of the existing tutorials and references, could be
of use, but I don't see it as "pressing", given the wide variety of what is
available from the Web.

I have been too busy to revamp my own Web Site (which has a page offering
COBOL help to students and through which 27 people have been helped in the
past 3 years - not a lot, but certainly better than nothing...) My plan is
to completely revise the whole Web Site (now that I have mastered Java and
JavaScript I can make it much more interesting and lively) and particularly
to expand the COBOL section. Unfortunately, I am still too mobile to set up
my own server, so I don't have control over SSI and CGI code which is the
key to a really good interactive web site, but within the next five years I
plan to be living at home so I'll do it then.

In the meantime, I believe the contribution of code examples to J4 may be a
"good thing", but I really have no right to suggest that, as I won't be
doing it myself...<G>

Pete.

James J. Gavan <jjgavan@shaw.ca> wrote in message
news:3C2B7250.D5747296@shaw.ca...
> "Earwigo again" said the earwig as it fell off the wall <G>. We are back
on my
> favourite topic - COBOL examples. I think this to be an absolute MUST if
we want
> COBOL to survive.
>
…[4 more quoted lines elided]…
> > This is a great idea. In the TC project such a reference is badly needed
as
> > well. A few of this
> > group have shown interest in that need. It seems that anything that
could be
> > freely downloaded
> > could be considered as fodder for this kind of activity. Sections of the
> > 200x document might
> > be good targets for inclusion as well when it modifys the current
standard.
> > It might be possible
> > to illustrate the variations supported, and comment on the amount of
effort
> > they place on
> > movement between compilers.  A lot of the questions have  been in this
area.
> >
> > Warren Simmons
…[4 more quoted lines elided]…
> --------------------------------------------------------------------------
-----
> Warren,
>
> Reminds me that a message I sent to you was undelivered. Here is a repeat
and
> others may care to comment :-
>
>
*>--------------------------------------------------------------------------
-------
>
> subject:
…[24 more quoted lines elided]…
> later - it should be pointing at the newbies coming up, if we want COBOL
to
> survive. Bill knows I don't like the current J4 sequence of contents and I
would
> prefer to see it go by discrete topics.
>
…[97 more quoted lines elided]…
> include new 2002 syntax provided). (*** Late note - Gary de Ward Brown did
an
> article on  the new VALIDATE for cobolreport.com ***)
>
…[11 more quoted lines elided]…
>
*>--------------------------------------------------------------------------
--------
>
> I can add other comments later. With refence to Pete's message to Michael,
I
> excpect he can dig out his paper on numeric usage - if not I can dig it
out of
> my archives. On further thoughts, an obvious area to add is a set of basic
> examples for ESQL - couched in generalised syntax which makes the
examples, (as
> near as possible), apply to all flavours of DBs.
>
…[14 more quoted lines elided]…
> > > 2. One rainy Sunday when you have nothing better to do, revise,
condense,
> > > and combine them into one download and give it to Bill for inclusion
with
> > > the COBOL FAQ. (Don't sweat it...)
> > >
> > > The point is that you should not incur an onerous workload for
something
> > you
> > > are doing out of the goodness of your heart.
> > >
> > > As many new people are picking up COBOL and it is desirable that we
should
> > > all encourage them to do so, it is likely that we will see many
further
> > > requests for information about Packed, Binary, and even Floating point
> > > formats in COBOL.
…[5 more quoted lines elided]…
> > > afternoon writing a document describing these formats to Jimmy Gavan.
It
> > is
> > > difficult for people (even good programmers like Jimmy) who have not
had
> > > mainframe exposure, to understand what, why, and how, things like
packed
> > > decimal work.
> > >
> > > I believe there is really not much point in responding every time
someone
> > in
> > > CLC asks the question. It is a true "Frequently  Asked" question and
> > > properly belongs on a FAQ.
> > >
> > > (Maybe we need a standard response like the one Doc uses when people
post
> > > Jobs that don't quote rates, something like: "Your request for COBOL
> > > information is covered in the COBOL FAQ. Please go to [wherever Bill
is
> > > keeping it these days] and you will find answers and code samples to
help
> > > you. If you still have questions, post specific inquiries, along with
a
> > copy
> > > of your code where appropriate, in this Newsgroup.")
> > >
> > > In passing, I would suggest that we should actively promote the COBOL
FAQ
> > > and route people to it as a first point of contact, THEN discuss any
> > > remaining questions in CLC.
> > >
> > > That way we prevent the NG from stagnating. (Repetitive posts are one
of
> > the
> > > quickest ways to kill interest in any forum...)
> > >
> > > For myself, I will be happy to contribute documents and code to the
FAQ if
> > > it is not currently equipped to serve its intended purpose.
> > >
> > > I would also like to see a downloadable on-line Help file or HTML
document
> > > with "quick answers" (summaries in plain English, with code samples,
and
> > > hyperlinked references to pertinent "See Also..."s ) for COBOL.
> > >
> > > (This is something I have had on a "back burner" for some time; if
anyone
> > is
> > > interested in helping with this, please contact me privately. I see
> > > something that will be freely distributed as "Quick COBOL Help".
Wherever
> > > possible it will be non-platform specific, but examples that utilise a
> > > particular platform could be colour coded. Different people could
…[4 more quoted lines elided]…
> > > anyone being unduly burdened...If there is no support for it, I'll do
it
> > > myself as a retirement project <G>, but that means that you won't see
it
> > for
> > > some years yet...)
…[9 more quoted lines elided]…
> > > > > http://www.flexus.com/downloads.html file COBDATA.ZIP is a text
and
> > > > graphics
> > > > > tutorial covering bit patterns, etc.
…[15 more quoted lines elided]…
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: COBOl Examples WAS - Re: first conversion program: disaster

_(reply depth: 9)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-12-28T12:22:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5C5F0B60F5A4D75A.91064A663AF68520.C98CC3A8A540C4FE@lp.airnews.net>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com> <3c28aae0.32743857@news.libero.it> <ckkW7.50$mq1.20752@dfiatx1-snr1.gtei.net> <WukW7.361$LY2.85189@paloalto-snr1.gtei.net> <3c2a661b_3@Usenet.com> <BTwW7.199367$WW.11558073@bgtnsc05-news.ops.worldnet.att.net> <3C2B7250.D5747296@shaw.ca>`

```
On Thu, 27 Dec 2001 19:08:09 GMT, "James J. Gavan" <jjgavan@shaw.ca>
enlightened us:

>"Earwigo again" said the earwig as it fell off the wall <G>. We are back on my
>favourite topic - COBOL examples. I think this to be an absolute MUST if we want
>COBOL to survive.
>

Isn't that why they write text books?  I can look through my old
college Cobol text book and find an "example" of just about anything
Cobol can do.  Thane's excellent book also has plenty of examples in
it.  

Bottom line, if a programmer or anyone wants to find examples of Cobol
code, all they need to do is a "little" research (translate that into
ambition) and plenty can already be found.


>"warren.simmons" wrote:
>
…[19 more quoted lines elided]…
>-------------------------------------------------------------------------------
<<much snippage>>

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

When you stop believing in Santa Claus is 
when you start getting clothes for Christmas!

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: COBOl Examples WAS - Re: first conversion program: disaster

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-12-28T19:29:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C2CC8F1.7342A216@shaw.ca>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com> <3c28aae0.32743857@news.libero.it> <ckkW7.50$mq1.20752@dfiatx1-snr1.gtei.net> <WukW7.361$LY2.85189@paloalto-snr1.gtei.net> <3c2a661b_3@Usenet.com> <BTwW7.199367$WW.11558073@bgtnsc05-news.ops.worldnet.att.net> <3C2B7250.D5747296@shaw.ca> <5C5F0B60F5A4D75A.91064A663AF68520.C98CC3A8A540C4FE@lp.airnews.net>`

```


SkippyPB wrote:

> On Thu, 27 Dec 2001 19:08:09 GMT, "James J. Gavan" <jjgavan@shaw.ca>
> enlightened us:
…[5 more quoted lines elided]…
>

I concur about Thane's book, (just checked to ensure he had MOVE CORRESPONDING <g>).

But it isn't just syntax you should be after but usefulness - for example where can
MOVE CORRESPONDING be used in a real world example. Further RENAMES, a feature I know
Pete Dashwood has used - but example(s) where it is applied in the real world.

I can recommend you to Will Price's book on Elements of OO COBOL - BUT - it is only a
starting point, which Will would admit. Then you have to develop from there. OO COBOL
(is/will be (?)) replete with methods for creating and using
collections/dictionaries. IF or WHEN you get into OO your immediate comments will be
"Collections/Dictionaries are fine, but show me examples of their practical
application......"

Back to 'basic'  COBOL - used a COBOL SORT for first time about three months ago. So
I go to Thane's book and read up on SORTS, plus I adapted one of his examples.
However, it would be more convenient if there was a COBOL on-line help  where I could
search on SORT and it immediately took me to say, ten SORT examples. I can probably
get all I would want from those examples, and reference the 'official' syntax text as
necessary.

I too can reference about five textbooks - but they are no damned good if I'm looking
for COBOL 97 +.  And your comment about 'researching' - why on earth have 3 million
(?) people, each doing their own research ?

>
> Bottom line, if a programmer or anyone wants to find examples of Cobol
> code, all they need to do is a "little" research (translate that into
> ambition) and plenty can already be found.
>

That one smacks a little of a saying associated with the British Trade Union
movement, "F... you Jack. I'm all right !".

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: COBOl Examples WAS - Re: first conversion program: disaster

_(reply depth: 10)_

- **From:** "warren.simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2001-12-28T23:46:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gv7X7.244487$3d2.12003683@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com> <928495c6.0112231327.635f0291@posting.google.com> <3c28aae0.32743857@news.libero.it> <ckkW7.50$mq1.20752@dfiatx1-snr1.gtei.net> <WukW7.361$LY2.85189@paloalto-snr1.gtei.net> <3c2a661b_3@Usenet.com> <BTwW7.199367$WW.11558073@bgtnsc05-news.ops.worldnet.att.net> <3C2B7250.D5747296@shaw.ca> <5C5F0B60F5A4D75A.91064A663AF68520.C98CC3A8A540C4FE@lp.airnews.net>`

```
SkippyPB, you are right, of course. I've made them up, read them in books,
found them on the
net. Yet, most of the readers here, first ask here for examples of something
they want to do.
Often, they are things for which the sources available do NOT include.

Put on top of that, an effort to create a public compiler by a group of
people who have not
used COBOL, or perhaps don't have ready access or the funds to obtain the
sources you spoke
of below. The TC group, for example is primarily made up of C programmers.
They use
examples that look like C. They often do not have the slightest idea of why
something is the
way it is in COBOL

And of course, all those students who come to this group with problems that
seemingly the
group serves do come to you (the royal you).

Then of course particapation is NOT required.  Some people do things because
they see a need,
and want to help in some way.  The project is not something anyone else is
doing including the
writers of books, or compilers.  While these efforts are a great help, is
that all someone supporting
COBOL can contribute?

While you appear to vote NO to such a project, would we see you contributing
something
should such a project begin?  More over,  anything you have contributed to
the readers of
CLC in the past might be useful in such a project and is  available for
taking.  Among the many
very bright people in this group, there are lots of ways to skin a cat, and
given a problem of
how to do something they  collectively have more experience than the author
of a book and
any one source.

To me that means the product of such a project could be the basis of all
future COBOL
specifications, and place that part of the developement into the hands of
USERS.

Warren Simmons

SkippyPB <swiegand@nospam.neo.rr.com> wrote in message
news:5C5F0B60F5A4D75A.91064A663AF68520.C98CC3A8A540C4FE@lp.airnews.net...
> On Thu, 27 Dec 2001 19:08:09 GMT, "James J. Gavan" <jjgavan@shaw.ca>
> enlightened us:
>
> >"Earwigo again" said the earwig as it fell off the wall <G>. We are back
on my
> >favourite topic - COBOL examples. I think this to be an absolute MUST if
we want
> >COBOL to survive.
> >
…[15 more quoted lines elided]…
> >> This is a great idea. In the TC project such a reference is badly
needed as
> >> well. A few of this
> >> group have shown interest in that need. It seems that anything that
could be
> >> freely downloaded
> >> could be considered as fodder for this kind of activity. Sections of
the
> >> 200x document might
> >> be good targets for inclusion as well when it modifys the current
standard.
> >> It might be possible
> >> to illustrate the variations supported, and comment on the amount of
effort
> >> they place on
> >> movement between compilers.  A lot of the questions have  been in this
area.
> >>
> >> Warren Simmons
…[5 more quoted lines elided]…
>---------------------------------------------------------------------------
----
> <<much snippage>>
>
…[13 more quoted lines elided]…
> Steve
```

##### ↳ ↳ Re: first conversion program: disaster

- **From:** dedalus@yifan.net (Duilio Foschi)
- **Date:** 2001-12-23T22:19:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c265665.46195941@news.libero.it>`
- **References:** `<3c250264.895577@news.libero.it> <8TnV7.8746$XC5.10013@www.newsranger.com>`

```
>Why not use a COBOL program like the one you wrote 

this is exactly my purpose.

As the data I have to convert are not here (they are at a customer's
site), I began doing the opposite convertion (i.e. from ASCII to
COM-3).

Thank you and merry Xmas

Duilio
```

#### ↳ Re: first conversion program: disaster

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2002-01-04T20:34:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6loZ7.4290$cD4.8197@www.newsranger.com>`
- **References:** `<3c250264.895577@news.libero.it>`

```
On Sat, 22 Dec 2001 23:34:58 GMT, in article <3c250264.895577@news.libero.it>,
Duilio Foschi stated 
>
>I have studied Cobol the whole day.
…[45 more quoted lines elided]…
>          NOT AT END

*            MOVE IN-REC TO OUT-REC
*This is a group move and nothing is changed 
*because it is moved as a large text field!!!!!
*This will unpack the field.
MOVE QTA-P TO QTA-9.
>            WRITE OUT-REC
>        END-READ
…[3 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
