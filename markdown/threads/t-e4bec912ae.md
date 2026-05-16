[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL subscript range checking

_67 messages · 17 participants · 2007-08_

---

### COBOL subscript range checking

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-08T10:19:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46B998BE.6F0F.0085.0@efirstbank.com>`

```
I am wondering what philosophy other shops out there have with regard to
COBOL, CICS, and subscript range checking.  We currently have the CHECK LE
runtime option turned ON, but our compiler is set with NOSSRANGE.  This
means that the code for range checking is not compiled in to the
executables, and therefore range checking is not done, even though it's set
to ON at the runtime level.

A few weeks ago we started having some problems with a program writing of
ECDSA.  As you can imagine this was not a good thing.  Based on the names of
the programs being written to the console I took a guess at which program it
was.  I recompiled the program with the SSRANGE option set and voila, that
was it.  Of course this didn't actually make the program itself work, but it
did 1) show us where the problem was and 2) stop it from writing over
storage unexpectedly.

So the question is, is range checking in production (especially production
CICS) programs a good idea?  What type of performance hit can be expected if
we turn it on?

Just for the heck of it, I turned on SSRANGE for a program I implemented
yesterday.  For better of for worse, the program started abending with
reason 1006, which corresponds to COBOL error IGZ0006S (The reference to
table <name> by verb number <number> on line <number> addressed an area
outside the region of the table.)  This was bad in that it caused the
program to stop working (under certain circumstances), but it was good in
that we can now eliminate a bug.  (Yes, I did fix the problem prior to
posting this message!  <g>)

My thought is to, at the very least, have the test compile job set the
SSRANGE option.  We'll certainly come upon more subscript overflows.  But I
don't we'd find all of them.  At some point I'm thinking that perhaps we'd
also want to do this in production, but there are definitely down sides.

So what does everyone think?

Thanks,
Frank
```

#### ↳ Re: COBOL subscript range checking

- **From:** Robert Jones <rjones0@hotmail.com>
- **Date:** 2007-08-08T11:17:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1186597027.503910.121050@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<46B998BE.6F0F.0085.0@efirstbank.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com>`

```
On Aug 8, 5:19 pm, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
wrote:
> I am wondering what philosophy other shops out there have with regard to
> COBOL, CICS, and subscript range checking.  We currently have the CHECK LE
…[41 more quoted lines elided]…
> (303) 235-1403

SSRANGE involves a serious performance hit, I seem to remember that
the programmers guide gave some guidance.  Having said that, a
mishehaving program can also cause serious performance probloms that
are more likely if it hasn't been tested adequately.  Perhaps a useful
compromise would be to run programs in production with it on for the
first week or month, then recompile with it off once you are
reasonably confident, with the option to turn it on again if
circumstances indicate a potential problem.  It's probably a good idea
to always use it when testing, except perhaps when doing performnce
analysis.  You should be wary of using it with old programs, which may
deliberately go out of range for specific reasons, such as trying to
read the leading record descriptor on a variable length record.  I
think it would be advisable to test old programs with SSRANGE on
before applying it in production.

HTH Robert
```

#### ↳ Re: COBOL subscript range checking

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-08T12:27:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ig2kb39ft92i2tjqhp36bm01fh36ntf95a@4ax.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com>`

```
On Wed, 8 Aug 2007 10:19:42 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>My thought is to, at the very least, have the test compile job set the
>SSRANGE option.  We'll certainly come upon more subscript overflows.  But I
>don't we'd find all of them.  At some point I'm thinking that perhaps we'd
>also want to do this in production, but there are definitely down sides.

Many shops still have standards created decades ago by persons long
gone that include turning off "expensive" options such as SSRANGE.
What's funny is that many of those shops allowed languages such as
PL/I that didn't give us the option of turning range checking off -
citing the advantage of such languages' checking.

(Use Java vs C++ for a modern version of this argument).

It shouldn't be so hard to change obsolete standards.     I got our
shop to put SSRANGE in the TEST proc (although lots of programmers
in-line that proc).   But I was unable to get it into the production
compiler.
```

#### ↳ Re: COBOL subscript range checking

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-08-08T16:51:31-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kj7kb3hjvt3dhngqjsmfjku2dsn570up8u@4ax.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com>`

```
On Wed, 8 Aug 2007 10:19:42 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>I am wondering what philosophy other shops out there have with regard to
>COBOL, CICS, and subscript range checking.  We currently have the CHECK LE
…[31 more quoted lines elided]…
>So what does everyone think?
Have you reviewed the generated code to see what is added by turning
on the check?
>
>Thanks,
>Frank
```

##### ↳ ↳ Re: COBOL subscript range checking

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-08T16:40:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46B9F207.6F0F.0085.0@efirstbank.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <kj7kb3hjvt3dhngqjsmfjku2dsn570up8u@4ax.com>`

```
>>> On 8/8/2007 at 1:51 PM, in message
<kj7kb3hjvt3dhngqjsmfjku2dsn570up8u@4ax.com>, Clark F
Morris<cfmpublic@ns.sympatico.ca> wrote:
> On Wed, 8 Aug 2007 10:19:42 -0600, "Frank Swarbrick"
> <Frank.Swarbrick@efirstbank.com> wrote:
…[11 more quoted lines elided]…
>>ECDSA.  As you can imagine this was not a good thing.  Based on the names

> of
>>the programs being written to the console I took a guess at which program

> it
>>was.  I recompiled the program with the SSRANGE option set and voila, 
> that
>>was it.  Of course this didn't actually make the program itself work, but

> it
>>did 1) show us where the problem was and 2) stop it from writing over
…[4 more quoted lines elided]…
>>CICS) programs a good idea?  What type of performance hit can be expected

> if
>>we turn it on?
…[11 more quoted lines elided]…
>>SSRANGE option.  We'll certainly come upon more subscript overflows.  But

> I
>>don't we'd find all of them.  At some point I'm thinking that perhaps 
…[5 more quoted lines elided]…
> on the check?

No, but it does make the executable quite a bit larger.
I may do this when I have some time.  (I have time to post here but no time
to do this research.  <g>)

Frank
```

#### ↳ Re: COBOL subscript range checking

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-08T20:53:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6oKdnVh3eOlIHCfbnZ2dnUVZ_q_inZ2d@comcast.com>`
- **In-Reply-To:** `<46B998BE.6F0F.0085.0@efirstbank.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com>`

```
Frank Swarbrick wrote:
> I am wondering what philosophy other shops out there have with regard to
> COBOL, CICS, and subscript range checking.

Well, we weren't IBM, so we didn't have CICS.  But, we didn't do range 
checking in production.  We did occasionally turn it on during 
development and debugging (especially if we had a hunch).  The overhead 
was "significant" according to the manual, but in practice, we never ran 
it long enough to get concrete numbers on the performance penalty.
```

#### ↳ Re: COBOL subscript range checking

- **From:** foodman123@gmail.com
- **Date:** 2007-08-09T06:05:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1186664714.481032.142460@d55g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<46B998BE.6F0F.0085.0@efirstbank.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com>`

```
On Aug 8, 12:19?pm, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
wrote:
> I am wondering what philosophy other shops out there have with regard to
> COBOL, CICS, and subscript range checking.  We currently have the CHECK LE
> runtime option turned ON, but our compiler is set with NOSSRANGE.  

Any programmer not coding specific end-of-range tests within the
application program should be fired.

Depending on the OS to detect errors is amateurish.


Tony Dilworth
```

##### ↳ ↳ Re: COBOL subscript range checking

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-08-09T09:35:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13bm9g5tphsgl74@news.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com>`

```
foodman123@gmail.com wrote:
> On Aug 8, 12:19?pm, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
> wrote:
…[8 more quoted lines elided]…
> Depending on the OS to detect errors is amateurish.

We once had a chap try to feed a pumpkin into the card reader. I don't know 
how the software could have tested for that...
```

##### ↳ ↳ Re: COBOL subscript range checking

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-09T08:54:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ffamb354ppdu4i82hg3lpv5lcg1ds4jtib@4ax.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com>`

```
On Thu, 09 Aug 2007 06:05:14 -0700, foodman123@gmail.com wrote:

>Any programmer not coding specific end-of-range tests within the
>application program should be fired.

Programmers mess up - look at all of the memory overflow problems
there are in applications and operating systems written in languages
that don't check for it.

>Depending on the OS to detect errors is amateurish.

OS?

Using a compiler that provides suspenders to supplement your belt is
professional.
```

##### ↳ ↳ Re: COBOL subscript range checking

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-09T17:00:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46BB4831.6F0F.0085.0@efirstbank.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com>`

```
>>> On 8/9/2007 at 7:05 AM, in message
<1186664714.481032.142460@d55g2000hsg.googlegroups.com>,
<foodman123@gmail.com> wrote:
> On Aug 8, 12:19?pm, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
> wrote:
…[8 more quoted lines elided]…
> Depending on the OS to detect errors is amateurish.

Yes, but that assumes the end-of-range checking is correct.  For instance,
this helped me find a bug I had with this regard just the other day.


Relevant field definitions:

 01  OBI-INFO.                             
     05  OBI-INFO-TEXT       OCCURS 6 TIMES
                             PIC X(35).    
     05  OBI-INFO-LINE       OCCURS 3 TIMES
                             PIC X(71).    

 01  WIREMNT.
     05  WIREMNT-FREE-FORM.                                
         10  WIREMNT-FREE-FORM-INFO        OCCURS 14 TIMES 
                                           PIC X(39).      
     05  REDEFINES WIREMNT-FREE-FORM.                      
         10                                OCCURS 14 TIMES.
             15  WIREMNT-FREE-FORM-TYPE    PIC X(4).       
             15  WIREMNT-FREE-FORM-TEXT    PIC X(35).      

Original code:

MOVE ZERO                   TO FF-SUB2
PERFORM VARYING FF-SUB1 FROM 1 BY 1            
          UNTIL FF-SUB1 > 14                   
             OR FF-SUB2 > 6                    
    IF WIREMNT-FREE-FORM-TYPE (FF-SUB1) = 'OBI'
                                       OR 'SVC'
        ADD +1 TO FF-SUB2                      
        MOVE WIREMNT-FREE-FORM-TEXT (FF-SUB1)  
          TO OBI-INFO-TEXT (FF-SUB2)           
    END-IF                                     
END-PERFORM                                    

Fixed code:

MOVE ZERO                   TO FF-SUB2
PERFORM VARYING FF-SUB1 FROM 1 BY 1            
          UNTIL FF-SUB1 > 14                   
             OR FF-SUB2 = 6                    
    IF WIREMNT-FREE-FORM-TYPE (FF-SUB1) = 'OBI'
                                       OR 'SVC'
        ADD +1 TO FF-SUB2                      
        MOVE WIREMNT-FREE-FORM-TEXT (FF-SUB1)  
          TO OBI-INFO-TEXT (FF-SUB2)           
    END-IF                                     
END-PERFORM                                    

This code has been for two years and never noticed until I just happened to
turn on SSRANGE.
And yes, I did code the original, buggy code.  No one's perfect.  Most
'modern' languages already do subscript range checking (among other things!)
at run-time.

Frank
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-10T09:51:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com>`

```
On Thu, 9 Aug 2007 17:00:33 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>This code has been for two years and never noticed until I just happened to
>turn on SSRANGE.

I like to have all of those type of comparisons with ">" instead of
"=", so I can see that mistake.

I often make my subscript sizes into "constants", to make it easier
for maintenance programmers to catch that they need to be changed when
they change table sizes.   I suppose I could be paranoid and code in a
check to see if the table is the size I think it is - but I have only
done that with database records.


I just thought of another reason why the old standard was not to have
the compiler do table size checking.    Until recently, we had code to
get around table size limits - with fillers after the table which held
the rest of the table.    That was subject to having an optimizer
break the code, but it never was any problem in real life.    That
said, I was very glad when we were able to get rid of that construct.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 4)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-10T10:35:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46BC3F84.6F0F.0085.0@efirstbank.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com>`

```
>>> On 8/10/2007 at 9:51 AM, in message
<h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com>, Howard
Brazee<howard@brazee.net> wrote:
> On Thu, 9 Aug 2007 17:00:33 -0600, "Frank Swarbrick"
> <Frank.Swarbrick@efirstbank.com> wrote:
…[6 more quoted lines elided]…
> "=", so I can see that mistake.

Yeah, I could have restructured it a bit to get this:

MOVE 1                      TO FF-SUB2
PERFORM VARYING FF-SUB1 FROM 1 BY 1            
          UNTIL FF-SUB1 > 14                   
             OR FF-SUB2 > 6                    
    IF WIREMNT-FREE-FORM-TYPE (FF-SUB1) = 'OBI'
                                       OR 'SVC'
        MOVE WIREMNT-FREE-FORM-TEXT (FF-SUB1)  
          TO OBI-INFO-TEXT (FF-SUB2)           
        ADD +1 TO FF-SUB2                      
    END-IF                                     
END-PERFORM                                    

But I decided to change just one line instead of two.
 
> I often make my subscript sizes into "constants", to make it easier
> for maintenance programmers to catch that they need to be changed when
> they change table sizes.   I suppose I could be paranoid and code in a
> check to see if the table is the size I think it is - but I have only
> done that with database records.

I do this sometimes.  Occasionally even do calculation by dividing the
length of the table by the length of a single occurrence.  That's the
safest, since you don't have to remember to change anything else when you
change the number of occurrences.

What I usually do now, though obviously not when I wrote the program above,
is something like:

REPLACE ==:ME-MAX:== BY ==10==.

01  MY-TABLE.
    05  MY-ENTRIES              OCCURS :ME-MAX: TIMES
                                INDEXED BY ME-IDX.
        10  ME-SOMETHING        PIC X.
        10  ME-SOMETHING-ELSE   PIC X(10).

PERFORM VARYING ME-IDX FROM 1 BY 1 UNTIL ME-IDX > :ME-MAX:
    ...
END-PERFORM

Hmm, I think we discussed exactly this just a few months ago.  :-)

Frank
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 5)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-08-11T14:16:39+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f9k9bd$k8t$03$1@news.t-online.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com>`

```
But don't we miss the 78 level in the standard :-)
(Yes, it can be done in other ways)
78  MAX-OCCS  VALUE 6.

....    OCCURS MAX-OCCS ....

IF  .. > MAX-OCCS

One place to change; no code checking necessary
(except if you screewed the IF)

Roger
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-11T23:43:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7Qrvi.500038$%85.343235@fe05.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com>`

```
Of course 78-levels are not part of "Standard COBOL" - and the OP was talking 
about IBM Enterprise COBOL (or VSE COBOL) where there are not
  - 78 levels
  - '02 Standard Constants
      or
  - the (old) Constant Section
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 6)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-13T09:42:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46C027A1.6F0F.0085.0@efirstbank.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com>`

```
>>> On 8/11/2007 at 6:16 AM, in message
<f9k9bd$k8t$03$1@news.t-online.com>,
Roger While<simrw@sim-basis.de> wrote:
> But don't we miss the 78 level in the standard :-)
> (Yes, it can be done in other ways)
…[7 more quoted lines elided]…
> (except if you screewed the IF)

Yep, except my compiler does not support that.

I believe the standard offers something similar.

01  MAX-OCCS CONSTANT AS 6.

Of course my compiler does not support that either...

Does remind me of an OpenCobol program I wrote recently, where I still had
to resort to a REPLACE statement:

program-id. x937cvt.
environment division.
replace ==:MAX-LEN:== by ==100000==.

input-output section.
file-control.
    select x937in-file
        organization sequential
        assign to x937in-file-name.

    select x937out-file
        organization sequential
        assign to x937out-file-name.

data division.
file section.
fd  x937in-file
    record varying from 1 to :MAX-LEN:
           depending on inreclen.
01  x937inrec.
    05  pic x occurs 1 to :MAX-LEN: times
              depending on inreclen.
01  x937inrec-fixed-area.
    05  x937inrec-type 
                      pic x(2).
    05                pic x(78).

fd  x937out-file
    record varying from 1 to :MAX-LEN:
           depending on outreclen.
01  x937outrec.
    05  pic x occurs 1 to :MAX-LEN: times
              depending on outreclen.

working-storage section.
78  MAX-LEN             value :MAX-LEN:.
78  MAX-SAVE            value 6.
77  x937in-file-name    pic x(80).
77  x937out-file-name   pic x(80).
77  inreclen            binary-long unsigned.
77  outreclen           binary-long unsigned.
77  rec-in-count        binary-long unsigned.
77                      pic x value 'N'.
    88  at-end                value 'Y'
                              false 'N'.
77  in-rectype          pic x(2).
    88  file-header           value '01'.
    88  bundle-header         value '20'.
    88  debit-detail          value '25'.
    88  credit-detail         value '61'.
    88  bundle-control        value '70'.
77                      pic x value 'N'.
    88  save-credits          value 'Y'
                              false 'N'.
77  out-rectype         pic x(2).

01  saved-items-table.
    05  saved-item-cnt  binary-long value zero.
    05  saved-item      occurs MAX-SAVE times
                        indexed by sidx.
        10  saved-item-len
                        binary-long unsigned.
        10  saved-item-rec.
            15  saved-item-rectype
                        pic x(2).
            15          pic x(MAX-LEN).

The constants are defined in working-storage and therefore (I assume) can
not be used in the file section.

[...minutes later...]

Just tried something, a little funky, but seems to work:

program-id. x937cvt.
environment division.
input-output section.
file-control.
    select dummy-file assign to dummy.

    select x937in-file
        organization sequential
        assign to x937in-file-name.

    select x937out-file
        organization sequential
        assign to x937out-file-name.

data division.
file section.
*  dummy-file declared only so some constant entries 
*  can be defined in the file section.
fd  dummy-file.
78  MAX-LEN             value 100000.
78  MAX-SAVE            value 6.

fd  x937in-file
    record varying from 1 to MAX-LEN
           depending on inreclen.
01  x937inrec.
    05  pic x occurs 1 to MAX-LEN times
              depending on inreclen.
01  x937inrec-fixed-area.
    05  x937inrec-type 
                      pic x(2).
    05                pic x(78).

fd  x937out-file
    record varying from 1 to MAX-LEN
           depending on outreclen.
01  x937outrec.
    05  pic x occurs 1 to MAX-LEN times
              depending on outreclen.

Too bad that the constant can't be defined outside of a file description
entry, but the standard seems to have this restriction as well.

Frank
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-13T12:46:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13c12vgjujfrc9@corp.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
news:46C027A1.6F0F.0085.0@efirstbank.com...
[snip]
> Just tried something, a little funky, but seems to work:
[snip]
> data division.
> file section.
…[25 more quoted lines elided]…
> entry, but the standard seems to have this restriction as well.

What was done in the standard is very inconvenient for
the programmer; but it is not, unfortunately, a material
defect. The same problem exists for both constant-entries
and typedefs. Even the DEFINE directive is of no help.

I think it is past time to restore the CONSTANT
SECTION as the location of choice for global constants
and typedefs.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-13T11:10:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b341c3t9mdt72jnfi7vvlbs58l2g23pobl@4ax.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com>`

```
On Mon, 13 Aug 2007 12:46:47 -0400, "Rick Smith" <ricksmith@mfi.net>
wrote:

>I think it is past time to restore the CONSTANT
>SECTION as the location of choice for global constants
>and typedefs.

And allow those constants to be used in the OCCURS clause.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 8)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-13T11:57:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46C04743.6F0F.0085.0@efirstbank.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com>`

```
>>> On 8/13/2007 at 10:46 AM, in message
<13c12vgjujfrc9@corp.supernews.com>,
Rick Smith<ricksmith@mfi.net> wrote:

> "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
> news:46C027A1.6F0F.0085.0@efirstbank.com...
…[39 more quoted lines elided]…
> and typedefs.

I'd never even heard of the "CONSTANT SECTION" before Bill Klein mentioned
it, but it sounds like a good idea to me!  Anyone know why it went away in
the first place?  I assume this was prior to the 1974 standard, since I
don't think the 1974 era mainframe compilers even supported it.\

What was the format of this section, anyway?

Frank
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 9)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-13T14:46:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13c19vgrto2dv9d@corp.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <46C04743.6F0F.0085.0@efirstbank.com>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
news:46C04743.6F0F.0085.0@efirstbank.com...
> >>> On 8/13/2007 at 10:46 AM, in message
> <13c12vgjujfrc9@corp.supernews.com>,
> Rick Smith<ricksmith@mfi.net> wrote:
[snip]
> > I think it is past time to restore the CONSTANT
> > SECTION as the location of choice for global constants
…[5 more quoted lines elided]…
> don't think the 1974 era mainframe compilers even supported it.\

According to an article on CODASYL COBOL, the
recommendation for deletion of the CONSTANT
SECTION was made in 1969; but this may have been
because it was never included in ANSI COBOL 68.

> What was the format of this section, anyway?

I don't know, never having seen it in a program.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-14T21:16:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ida6uF3ofalfU1@mid.individual.net>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <46C04743.6F0F.0085.0@efirstbank.com> <13c19vgrto2dv9d@corp.supernews.com>`

```


"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:13c19vgrto2dv9d@corp.supernews.com...
>
> "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
…[24 more quoted lines elided]…
>

It was very simple...

following WORKING-STORAGE...

CONSTANT SECTION.

01 some-constant pic <whatever, exactly as in WS>
77 some-other-constant pic <whatever, exactly as in WS>

I used it quite a bit just to document fields that did not get changed by 
the program (READ-ONLY, if you like.)

As the facilities in it were also available through WS, it was considered 
redundant and removed.

I don't think anyone was thinking in terms of typedefs at the time...:-)

I agree with you, it would be nice to see it back, especially if 78 levels 
were implemented.

(Don't hold your breath... :-))

Pete.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 11)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-08-14T12:14:58-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jkh3c3lkpiuig4o4tioo46k613vgeelj9q@4ax.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <46C04743.6F0F.0085.0@efirstbank.com> <13c19vgrto2dv9d@corp.supernews.com> <5ida6uF3ofalfU1@mid.individual.net>`

```
On Tue, 14 Aug 2007 21:16:12 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>
…[43 more quoted lines elided]…
>redundant and removed.

At the time I agreed with the removal not even having a clue about the
concept of reentrant code and the initialization savings a CONSTANT
SECTION would allow.
>
>I don't think anyone was thinking in terms of typedefs at the time...:-)
…[6 more quoted lines elided]…
>Pete.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-13T19:40:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dt2wi.205221$ss3.140750@fe01.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:13c12vgjujfrc9@corp.supernews.com...
>
> "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
> news:46C027A1.6F0F.0085.0@efirstbank.com...
<snip>
>
> I think it is past time to restore the CONSTANT
> SECTION as the location of choice for global constants
> and typedefs.
>

Rick,
  Not that I think what is and is not in the Standard has much impact on anyone, 
can you tell me what you think is bad about the DRAFT Standard definition for 
Constants?  This allows for "elementary" items or records to be defined as 
constants.  (See the CONSTANT RECORD clause in WD 1.7)
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 9)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-13T20:31:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13c1u70s8s3gvfc@corp.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:dt2wi.205221$ss3.140750@fe01.news.easynews.com...
> "Rick Smith" <ricksmith@mfi.net> wrote in message
> news:13c12vgjujfrc9@corp.supernews.com...
…[7 more quoted lines elided]…
>   Not that I think what is and is not in the Standard has much impact on
anyone,
> can you tell me what you think is bad about the DRAFT Standard definition
for
> Constants?  This allows for "elementary" items or records to be defined as
> constants.  (See the CONSTANT RECORD clause in WD 1.7)

With respect to the definition of constants, nothing, I
know of, is bad and the problem is unrelated to the
CONSTANT RECORD clause.

The problem occurs when including application-wide
constants and typedefs in every program, function,
method, and class definition that uses them. When
these constants and typedefs are copied into the source,
the only "safe" place, to put the COPY statement, is prior
to the record definition for the first file in the file section,
unless there are no files. A CONSTANT SECTION,
immediately following the DATA DIVISION header,
would provide a "safe", consistent and well-understood
place for such a COPY statement.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-14T04:23:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N6awi.448183$LL7.77458@fe08.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com>`

```
Rick,
  Is there some place that prohibits "forward references" to constant-names in 
either the '02 Standard or the draft of the next one?  This is a serious 
question - as I was wondering about it for an interpretation that I did.  As far 
as I can tell (when I looked - and I haven't looked again) you can define a 
Constant in the Working-Storage section and use that name in the Special-Names 
paragraph.   There are rules about "circular" references, but I don't remember 
finding any "forward reference" prohibitions.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-14T04:28:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sbawi.212706$u82.113159@fe09.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com>`

```
(replying to myself)

I should have mentioned that I *know* that the '02 Standard has places where you 
need "forward references".  For example, the SELECT/USING structure.   Also, I 
am almost positive that TYPEDEFs do not need appear physically in the source 
code before they are used.

Now, if the question of whether this is "good" (easy to maintain) coding is 
another question.  I suspect that having a CONSTANT SECTION  where all of this 
"scuff" is together would be more (maintenance)  programmer friendly - and that 
may have been what you were saying and I just missed it.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 12)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-14T07:25:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13c34ih2h8d0m9b@corp.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:sbawi.212706$u82.113159@fe09.news.easynews.com...
> (replying to myself)
>
> I should have mentioned that I *know* that the '02 Standard has places
where you
> need "forward references".  For example, the SELECT/USING structure.
Also, I
> am almost positive that TYPEDEFs do not need appear physically in the
source
> code before they are used.
>
> Now, if the question of whether this is "good" (easy to maintain) coding
is
> another question.  I suspect that having a CONSTANT SECTION  where all of
this
> "scuff" is together would be more (maintenance)  programmer friendly - and
that
> may have been what you were saying and I just missed it.
>
…[6 more quoted lines elided]…
> >  Is there some place that prohibits "forward references" to
constant-names in
> > either the '02 Standard or the draft of the next one?  This is a serious
> > question - as I was wondering about it for an interpretation that I did.
As
> > far as I can tell (when I looked - and I haven't looked again) you can
define
> > a Constant in the Working-Storage section and use that name in the
> > Special-Names paragraph.   There are rules about "circular" references,
but I
> > don't remember finding any "forward reference" prohibitions.

[snip]

FDIS ISO/IEC 1989:2002, page 1, 1 Scope,
"This International Standard does not specify:

- The means whereby a compilation group written in
     COBOL is compiled into code executable by a
     processor.
..."

--, page 29, 7 Compiler directing facility,
"The compilation stage completes the compilation
process utilizing the structured compilation group."

There is nothing in the respective sections of the
standard that prohibits forward references for at least
these three items: constant-names, typedefs, and the
object of a SAME AS clause. [These are not mere
references; but affect the size of the item containing
the reference.]

The question is: Are such forward references permitted?

The answer is: No.

Forward references, for the above items, require a
non-sequential "means" for processing the "structured
compilation group". Requiring a particular "means" is not
within the scope of the standard.

Requiring the above items to be defined before they are
referenced, has no apparent effect on the "means whereby
a compilation group written in COBOL is compiled ...."

At least, that's how I see it!
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-22T05:28:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2QPyi.2107$fh4.476@fe01.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com>`

```
Rick,
  I remember discussion (during the '02 Standard development) about "single pass 
compilers".  My memory is that there is no requirement in the current standard 
that such be "supported" (or even allowed).  If you really cared, you could 
submit an interpretation request, but I certainly do think that those who have 
"constants" now (any format) allow forward references - and I am also 99% 
certain that MF (for example) allows forward references for typedefs.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 14)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-23T04:26:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13cqhb08ttqa331@corp.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:2QPyi.2107$fh4.476@fe01.news.easynews.com...
> Rick,
>   I remember discussion (during the '02 Standard development) about
"single pass
> compilers".  My memory is that there is no requirement in the current
standard
> that such be "supported" (or even allowed).  If you really cared, you
could
> submit an interpretation request, but I certainly do think that those who
have
> "constants" now (any format) allow forward references - and I am also 99%
> certain that MF (for example) allows forward references for typedefs.
…[19 more quoted lines elided]…
> >> Now, if the question of whether this is "good" (easy to maintain)
coding
> > is
> >> another question.  I suspect that having a CONSTANT SECTION  where all
of
> > this
> >> "scuff" is together would be more (maintenance)  programmer friendly -
and
> > that
> >> may have been what you were saying and I just missed it.
…[9 more quoted lines elided]…
> >> > either the '02 Standard or the draft of the next one?  This is a
serious
> >> > question - as I was wondering about it for an interpretation that I
did.
> > As
> >> > far as I can tell (when I looked - and I haven't looked again) you
can
> > define
> >> > a Constant in the Working-Storage section and use that name in the
> >> > Special-Names paragraph.   There are rules about "circular"
references,
> > but I
> >> > don't remember finding any "forward reference" prohibitions.
…[35 more quoted lines elided]…
> > At least, that's how I see it!


Given the following code (numbered lines have forward
references):

       01 A.
           02 D PIC X.
1          02 E SAME AS E OF B.
       01 B.
           02 D PIC 9.
2          02 E TYPE TO C.
3      01 C TYPEDEF PIC X(PIC-SIZE).
       01 PIC-SIZE CONSTANT 9.

The errors I would expect for each is a message indicating
that the referenced items: E OF B, C, and PIC-SIZE,
respectively, are undefined; because the compiler can not
apply the appropriate rules. Note that in each case, the rules
that apply are general rules, not syntax rules; that is, rules that
specify the action required by the compiler when it encounters
the respective elements: the SAME AS clause, TYPE clause,
and constant-name. [For comparison, it is the general rules in
the COPY statement and the REPLACE statement that
specify actions to be taken by the compiler.]

Reverse the sequence of the level-number 1 items and the
problem goes away.

Note, also, that references in the environment division to
data-names use syntax rules that do not apply until the
data-name is defined (or need not be applied until the end
of the data division).
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 15)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-25T05:59:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<izPzi.6595$SB3.5422@fe03.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com>`

```
Rick,
  You may expect such messages (or the possibility of such messages), but I do 
not believe that the designers of the '02 Standard would consider a compiler 
issuing such messages to be "conforming".  Again, this is MY understanding (and 
the lack of any explicit syntax rule seems to confirm it).  If you disagree, you 
certainly could submit an interpretation request - or wait until there is a 
compiler claiming to conform to the '02 Standard.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 16)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-25T08:09:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13d0772t303f405@corp.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:izPzi.6595$SB3.5422@fe03.news.easynews.com...
> Rick,
>   You may expect such messages (or the possibility of such messages), but
I do
> not believe that the designers of the '02 Standard would consider a
compiler
> issuing such messages to be "conforming".  Again, this is MY understanding
(and
> the lack of any explicit syntax rule seems to confirm it).  If you
disagree, you
> certainly could submit an interpretation request - or wait until there is
a
> compiler claiming to conform to the '02 Standard.

-----
FDIS ISO/IEC 1989:2002, page 3, 3.1.1 Acceptance
of standard language elements,
"An implementation shall accept the syntax and provide
the functionality for all standard language elements required
by this International Standard and the optional or
processor-dependent language elements for which support
is claimed.

An implementation shall provide a warning mechanism that
optionally can be invoked by the user at compile time to
indicate violations of the general formats and the explicit
syntax rules of standard COBOL. This warning mechanism
shall provide a suboption for selection or suppression of
checking for violations of the set of conformance rules
specified in 14.7, Conformance for parameters and returning
items, and in 9.3.7.1.2, Conformance between interfaces.

There are rules in standard COBOL that are not identified
as general formats or syntax rules, but nevertheless specify
elements that are syntactically distinguishable. This warning
mechanism shall indicate violations of such rules. For elements
not specified in general formats or in explicit syntax rules, it is
left to the implementor's judgement to determine what is
syntactically distinguishable.

There are general rules in standard COBOL that could have
been classified as syntax rules. These rules are classified as
general rules for the purpose of avoiding syntax checking,
and do not reflect errors in standard COBOL. An
implementation may, but is not required to, flag violations of
such rules."
-----

With specific reference to the last sentence of the third
paragraph, above; in my judgement, the use of a
constant-name is not "syntactically distinguishable" until its
constant-entry is defined. This is a direct consequence of
the explicit general rules for 13.9, Constant entry.
Furthermore, as a consequence of the second sentence
of the third paragraph, above, I not only expect a warning
message; but, were I an implementor, I would be obligated
to provide it!

In other words, the lack of an explicit syntax rule (or rules)
"requiring" forward references for constant-names, means the
implementor's judgement prevails; not interpretation based on
belief in intent. If you disagree, you could submit a defect
report to add such an explicit syntax rule. <G>
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 17)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-26T09:32:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oMbAi.152024$sR4.54373@fe08.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com>`

```
You still have NOT provided any rule that is not marked as a syntax rule or 
general rule that explicitly prohibts "forward references".  General Rules are 
*NEVER* supposed to be "detected" at compile-time. (Well a vendor MAY detect a 
logically invalid construct but is not required to).

Rick,
 I think you are just trying to turn the Standard into saying something that it 
simply doesn't.  Have you tried Micro Focus' TYPEDEFs?  (I have NOT).  My guess 
is that they allow foward references.

It doesn't sond (to me) as if I will convince you of either the INTENT (to allow 
foward refences) or the rules of the '02 Standard. I *might* submit my own 
interpretation request, but as I still see minimal signs of any implementor 
actually IMPLEMENTING a fully conforming (to the '02 Standard) compiler, I don't 
know what this would get either of us.

If you plan on submitting public review comments when the draft of the next 
Standard comes out, you might want to mention this.

SR(1) of the CONSTANT entry seems pretty clear to me when it states,

"Constant-name-1 may be used anywhere that a format specifies a literal of the 
class and category of constant-name-
1."

This is where I would expect a rule to exist that says, "previously defined in 
the current source element" - if that was what was meant or intended.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 18)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-26T08:11:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13d2rm6ho25no66@corp.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:oMbAi.152024$sR4.54373@fe08.news.easynews.com...
> You still have NOT provided any rule that is not marked as a syntax rule
or
> general rule that explicitly prohibts "forward references".  General Rules
are
> *NEVER* supposed to be "detected" at compile-time. (Well a vendor MAY
detect a
> logically invalid construct but is not required to).

Yet, the items: SAME AS clause, TYPEDEF clause,
and contant-entry; have general rules but no runtime
behavior!

> Rick,
>  I think you are just trying to turn the Standard into saying something
that it
> simply doesn't.  Have you tried Micro Focus' TYPEDEFs?  (I have NOT).  My
guess
> is that they allow foward references.

Micro Focus COBOL 3.2 does not allow forward
references; but that version is from 1994. I don't
know what is done currently, though I suspect and
hope it is the same.
-----
* Micro Focus COBOL Version 3.2.24 [...] 26-Aug-07 06:35 Page   1
*                                  C:\CBL-CHAL\A27B17.CBL
* Options: WB ERRQ EDITOR(MF) LIST() NOOSVS ANS85
     1 program-id. A27B17.
     2 data division.
     3 01 item-1 pic x(pic-size).
* 230-S************************* [...] (   0)**
**    PICTURE string has illegal precedence or illegal character
     4 78 pic-size value 20.
     5
     6 01 item-2 uint.
* 233-S************** [...] (   1)**
**    Unknown data description qualifier
     7 01 uint typedef pic 9(9) comp-5.
     8
     9 01 item-3 pic x(pic-size).
    10
    11 01 item-4 uint.
* Micro Focus COBOL Version 3.2.24   L2.5 revision 000
* Last message on page: 1
*
* Total Messages:     2
* Unrecoverable :     0                    Severe  :     2
* Errors        :     0                    Warnings:     0
* Informational :     0                    Flags   :     0
* Data:         524     Code:          57
-----

> It doesn't sond (to me) as if I will convince you of either the INTENT (to
allow
> foward refences) or the rules of the '02 Standard. I *might* submit my own
> interpretation request, but as I still see minimal signs of any
implementor
> actually IMPLEMENTING a fully conforming (to the '02 Standard) compiler, I
don't
> know what this would get either of us.

I have had the unfortunate experience of leaning too
late that errors of omission do occur with intellegent,
well-educated, knowledgeable, and sincere people.
In this case, conformance is to the written standard;
not to unstated intent; thus, intent (or belief in intent)
has no weight, while the result of an interpretation
request would have weight if, and only if, it reveals
an error of omission.

> If you plan on submitting public review comments when the draft of the
next
> Standard comes out, you might want to mention this.
>
> SR(1) of the CONSTANT entry seems pretty clear to me when it states,
>
> "Constant-name-1 may be used anywhere that a format specifies a literal of
the
> class and category of constant-name-
> 1."
>
> This is where I would expect a rule to exist that says, "previously
defined in
> the current source element" - if that was what was meant or intended.

This is where I would expect a note (statement of intent)
to the effect that the rule permits forward references.
But, I am relying on GR(1),

"If literal-1 or compilation-variable-name-1 is specified,
the effect of specifying constant-name-1 in other than
this entry is as if literal-1 or the text represented by
compilation-variable-name-1 were written where
constant-name-1 is written."

And, the fact that it can not be applied until after the
constant-entry occurs in the source unit, as was
demonstrated in the program posted above.
```

###### ↳ ↳ ↳ "forward" references (was: COBOL subscript range checking

_(reply depth: 19)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-27T00:18:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PLoAi.162805$jE4.61866@fe12.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:13d2rm6ho25no66@corp.supernews.com...
>
> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message
> news:oMbAi.152024$sR4.54373@fe08.news.easynews.com...
<snip>
>>
>> SR(1) of the CONSTANT entry seems pretty clear to me when it states,
…[23 more quoted lines elided]…
>

The syntax rule says that they may be used anywhere and the GR tells HOW it is 
"used" wherever that might be.  The GR never says ANYTHING about *how* the 
compiler does what it is required to do.  I think the SR and GR work quite well 
together to tell what must be supported (use anywhere a literal of that category 
can be use) and the GR tell that you do a substitution (but does NOT tell you 
how or what the compiler needs to do to do this).  Your assumption that a 
"single pass" (or a use of only previously defined "stuff") is required is 
simply not supported by the rules as they exist.

SR rule is quite clear that a conforming compiler MUST support use of a 
constant-name wherever such a literal is supported (including in Special-Names, 
earlier in the Data Division, or wherever).  I would expect a compiler with 
"limited" passes to find a user-defined word where a literal is required (or 
allowed) to search forward in the text until it finds the appropriate 
"definition".  Same requirement for TYPEDEF and SAME AS.

The constant entry SR doesn't need to make "intent" clear; instead it provides a 
simple REQUIREMENT for all conforming compilers that they allow constant-names 
wherever such literals appear in the format.
```

###### ↳ ↳ ↳ Re: "forward" references (was: COBOL subscript range checking

_(reply depth: 20)_

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2007-08-27T14:43:01+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<faugsm$q0c$1@nntp.fujitsu-siemens.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
news:PLoAi.162805$jE4.61866@fe12.news.easynews.com...
> The syntax rule says that they may be used anywhere and the GR tells HOW 
> it is "used" wherever that might be.  The GR never says ANYTHING about 
…[14 more quoted lines elided]…
> AS.

Bill,
that is just the problem: which text should be searched? The program text 
can be manipulated using directives, which again may use literals, which 
again may be represented by user-defined words defined as constants which 
are not necessarily known at the time, when the source text manipulation 
must make the decisions!
Consider for example a combination like this:
  >>DEFINE var AS PARAMETER
  ...
  >>IF var = const
    ...
    01 const CONSTANT "a".
    ...
  >>ELSE
   ...
   01 const CONSTANT "b".
   ...
  >>END-IF
in this case, a look ahead might help (if the actual value for var is not 
"a" and not "b"), but in general a compiler must expect and be able to 
handle various combinations and nesting of such directives, which means - as 
far as i can see - a compiler must assume values for the unknown constants 
and start to expand in parallel all possible sources and then check 
consitency of the assumed values for each expansion with the constant 
definitions eventually found in the expanded source; and additionally.
All thogether, i think the definition of constants in STD2002 is not 
implementable - at least not with adequate usage of resources!

K. Kiesel
Fujitsu Siemens Computers, M�nchen
```

###### ↳ ↳ ↳ "forward" references (was: COBOL subscript range checking

_(reply depth: 21)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-27T17:29:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CRDAi.175098$jE4.100287@fe12.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com>`

```
(Karl raised the issue of whether the current definition is - or is not - 
implementable.  He didn't seem to disagree with me on what the '02 Standard 
says).

I posted, the following question to the J4 distribution list

"
This has been a discussion in the comp.lang.cobol forum and I *think* that I 
remember correctly, but was wondering if anyone else either remembers 
differently or can point me to better places to look for a "definitive" answer.

The question is about "forward" references for things like CONSTANT Entries, 
TYPEDEF/TYPE, and SAME AS.
It is my memory that when this was discussed (during the development of the '02 
Standard) it was INTENTIONALLY decided that a conforming program could have 
"forward" references, e.g.

 - use of a constant-name in Special-Names paragraph - with CONSTANT entry in 
data division
 - Use of TYPE pointing to a TYPEDEF defined later in the program
 - SAME AS referring to record later in the data division

It was thought (???) that the rules DO prohibit "circularity" of references, but 
that "forward" references were INTENTIONALLY allowed.

Without submitting an interpretation request (that I MIGHT end up doing), can 
others tell me what they think was INTENDED and ALLOWED?"

  ***

Sp far, I have received 3 replies, i.e

"** Reply 1

"My recollection is the same as Bill's."

*** Reply 2

" I wasn't there for this part of the development, but I can say that how to 
deal with "forward references" is an mplementation detail.  From a 
compiler-design standpoint such issues are pretty much moot if two passes are 
made against the source or an encoded version of it.  Nested programs as 
introduced in '85 complicates the implementation, but doesn't change the point 
that it's the implementor's job to resolve the references, and I believe the 
rules are clear as to how to resolve them (or determine that they are ambiguous 
and take appropriate action).

Moreover, forward references exist in the '74 standard -- SELECT ... RECORD KEY 
... being but one example.

My opinion is that the resolution of references -- be they forward or 
backward -- is one of the things the implementor is expected to provide for at 
compilation time, and is not something the end user is supposed to be concerned 
about so long as the references can be resolved unambiguously.  "

*** Reply 3

""Forward" references are allowed and were intentionally allowed. Why is this a 
problem (it is a problem for the implementors, not the  users)? No 
interpretation is needed since it is quite clear."

* * * * * * * * * * * *

I don't think that these will change Rick's mind (on either what was intended or 
stated), but I did think that I would share these.
```

###### ↳ ↳ ↳ Re: "forward" references (was: COBOL subscript range checking

_(reply depth: 22)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-27T15:39:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13d6a9qgvelti4b@corp.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <CRDAi.175098$jE4.100287@fe12.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:CRDAi.175098$jE4.100287@fe12.news.easynews.com...
> (Karl raised the issue of whether the current definition is - or is not -
> implementable.  He didn't seem to disagree with me on what the '02
Standard
> says).
>
…[3 more quoted lines elided]…
> This has been a discussion in the comp.lang.cobol forum and I *think* that
I
> remember correctly, but was wondering if anyone else either remembers
> differently or can point me to better places to look for a "definitive"
answer.
>
> The question is about "forward" references for things like CONSTANT
Entries,
> TYPEDEF/TYPE, and SAME AS.
> It is my memory that when this was discussed (during the development of
the '02
> Standard) it was INTENTIONALLY decided that a conforming program could
have
> "forward" references, e.g.
>
>  - use of a constant-name in Special-Names paragraph - with CONSTANT entry
in
> data division
>  - Use of TYPE pointing to a TYPEDEF defined later in the program
>  - SAME AS referring to record later in the data division
>
> It was thought (???) that the rules DO prohibit "circularity" of
references, but
> that "forward" references were INTENTIONALLY allowed.
>
> Without submitting an interpretation request (that I MIGHT end up doing),
can
> others tell me what they think was INTENDED and ALLOWED?"
>
…[10 more quoted lines elided]…
> " I wasn't there for this part of the development, but I can say that how
to
> deal with "forward references" is an mplementation detail.  From a
> compiler-design standpoint such issues are pretty much moot if two passes
are
> made against the source or an encoded version of it.  Nested programs as
> introduced in '85 complicates the implementation, but doesn't change the
point
> that it's the implementor's job to resolve the references, and I believe
the
> rules are clear as to how to resolve them (or determine that they are
ambiguous
> and take appropriate action).
>
> Moreover, forward references exist in the '74 standard -- SELECT ...
RECORD KEY
> ... being but one example.
>
> My opinion is that the resolution of references -- be they forward or
> backward -- is one of the things the implementor is expected to provide
for at
> compilation time, and is not something the end user is supposed to be
concerned
> about so long as the references can be resolved unambiguously.  "
>
> *** Reply 3
>
> ""Forward" references are allowed and were intentionally allowed. Why is
this a
> problem (it is a problem for the implementors, not the  users)? No
> interpretation is needed since it is quite clear."
…[3 more quoted lines elided]…
> I don't think that these will change Rick's mind (on either what was
intended or
> stated), but I did think that I would share these.

These replies seem to be non-responsive to the "real"
question. I agree with what was said by both 2 and 3;
but neither addressed conformance with respect to
substitution ("as if"/"as though" ...) with elements defined
later in source text. This is particularly evident in 2 by
referring to the 74 and 85 standards when the "real"
question doesn't arise until the 2002 standard. 1's reply
contains nothing to show that the "real" question was
being addressed; rather, it does nothing more than agree
with a potentially faulty recollection.

The bottom-line is that there is nothing in these replies
to serve as reason for my changing my mind!
```

###### ↳ ↳ ↳ Re: "forward" references (was: COBOL subscript range checking

_(reply depth: 23)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-28T01:06:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MyKAi.175961$jE4.165723@fe12.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <CRDAi.175098$jE4.100287@fe12.news.easynews.com> <13d6a9qgvelti4b@corp.supernews.com>`

```
Certainly, when/if there is a conforming '02 Standard compiler, there is nothing 
that says that any programmer will be required to uses forward references. 
Furthermore, I think that even if there ever is a conforming compiler, I doubt 
that there will ever be any conformance tests.

Therefore, I don't think you (or I) will be impacted by this. As others in J4 
agree, the rules are clear (to us) and do require a conforming compiler to 
provide this functionality.  When a syntax rule says that something can be used 
anywhere (with certain restrictions) then those are simply the ONLY valid 
restrictions that a conforming compiler can put on it.

You won't be forced to use it, but "implementors" (such as Roger with OC) will 
need to provide the feature - or not claim to be conforming.
```

###### ↳ ↳ ↳ Re: "forward" references (was: COBOL subscript range checking

_(reply depth: 21)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-27T17:44:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4EAi.169153$Bo7.88986@fe07.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com>`

```
Karl,
  For what is is worth, Page 29 of the '02 Standard explicitly states that the 
 >>IF, - >>ELSE, and  >>DEFINE directives are handled during the "Text 
manipulation" and not the later "comiilation stage".  Therefore (to me) I would 
expect only one CONSTANT ENTRY to be "known" by the time you get to the 
compilation stage (when this information would be needed).

My original comment about "searching ahead" was assuming (possibly erroneously) 
that the entire text manipulation stage had been completed before this all need 
to be handled.
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 22)_

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2007-08-28T13:33:16+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fb115t$6kc$1@nntp.fujitsu-siemens.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com>`

```
"William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
news:e4EAi.169153$Bo7.88986@fe07.news.easynews.com...
> Karl,
>  For what is is worth, Page 29 of the '02 Standard explicitly states that 
…[9 more quoted lines elided]…
>
Bill,
that is just the problem I see here! The STD2002 defines a sequence of 
separate stages of compilation (see chapter 7) but the earlier stage (text 
manipulation) may need information that can only be obtained from the later 
stage (compilation): expressions within >>IF and >>EVALUATE directives may 
be formed using literals (for example see STD2002 7.2.7.1 syntax rule 1) and 
i did not find any rule, that forbids using a constant in place of a literal 
in these expressions. Therefore, to complete the text manipulation stage, a 
compiler must be able to evaluate constant conditional expressions in 
directives, but this is impossible, if a constant is involved, beause 
processing (ie recognition and especially determining the value) of such a 
constant entry is definitely part of the later stage - but this stage can 
not be entered unless the previous stage has been completed! In this sense, 
using constants within directives is a form of 'forward reference'; If the 
concept of stages within the STD2002 is to be kept - and I would not like to 
give it up! - constant entries are a problem that make implementaion rather 
hard, if not impossible.

Karl Kiesel
Fujitsu Siemens Computers
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 23)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-08-28T17:06:49+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fb1dmk$at6$01$1@news.t-online.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com> <fb115t$6kc$1@nntp.fujitsu-siemens.com>`

```

"Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com> schrieb im Newsbeitrag 
news:fb115t$6kc$1@nntp.fujitsu-siemens.com...
> "William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
> news:e4EAi.169153$Bo7.88986@fe07.news.easynews.com...
…[33 more quoted lines elided]…
>

Geez, you beat me to it. I had studied the standard for the last
x hours/days. I had come to the conclusion as you did.
I was still trying to find the reverse arguments.

Incidentally a GLOBAL CONSTANT is somewhat different
in that it has to abide by the GLOBAL constraint.
ie. This is only possible to refernce backwards.

Roger

Roger
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 23)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-29T12:13:48+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jjs1vF3ua30hU1@mid.individual.net>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com> <fb115t$6kc$1@nntp.fujitsu-siemens.com>`

```


Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com> wrote in message 
news:fb115t$6kc$1@nntp.fujitsu-siemens.com...
> "William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
> news:e4EAi.169153$Bo7.88986@fe07.news.easynews.com...
…[10 more quoted lines elided]…
>> before this all need to be handled.

I have followed most of this stuff with bewilderment. Perhaps someone can 
explain in simple, clear, terms (I know that's proven very difficult for J4 
people in the past, but, please do try...I'm not stupid, and you have my 
full attention :-)) exactly what the problem is here?

I've only ever worked on one COBOL compiler but I can assure you that 
forward references are NOT a problem. The "text manipulation" phase you 
refer to is the parsing phase and this is normally an extraction of 
simplexes ("simple expressions", usually in a tokenized or coded form) from 
COBOL source. If forward references are encountered, a placeholder is 
inserted and the second pass of the parser updates the simplexes, with what 
were previously forward references but have now been tokenized and stored. 
In the third pass, addresses are assigned to simplex constants and 
variables. No problem.

So is it that the 2002 standard requires a particular approach? Why would 
it? Implementation should be left to implementors. Having constants in a 
Constant Section or having literals embedded in code should not be 
problematic to a compiler writer.

As for the "vicious circle" that Karl describes where the "text 
manipulation" cannot be complete until information from subsequent passes is 
obtained, that's the bit I am having difficulty with. Why would an 
implementor paint himself into a corner? In my experience, they don't.

>>
> Bill,
> that is just the problem I see here! The STD2002 defines a sequence of 
> separate stages of compilation (see chapter 7)

Why does it?

I confess, I haven't read the standard, but if that is the case, why would a 
Standards committee close down the options of an implementor? Why should the 
standard even be talking about "phases of compilation" that have no bearing 
on an end user and are properly the province only of the implementor?

Is this where the problem is arising?

I can't speak for others, but if I was still in the business of writing and 
maintaining COBOL compilers, and I found something in a standard that 
curtailed my options, I'd simply ignore it. Risk non-compliance? How is it 
non-compliant if everything required to be implemented, is achieved? (HOW it 
is achieved is no business of the Standards committee...)

End users don't care (especially if it is the only compliant compiler 
available :-)) how many passes the compiler takes as long as their code is 
compiled correctly. Do you seriously think anyone would eschew a 2002 
implementation because it didn't follow the compilation phases "required" by 
the standard (which, in my opinion, shouldn't even be addressing compilation 
phases anyway)?

There seems to be some serious confusion here between WHAT (definitely the 
province of the Standards committee) and HOW, (definitely the province of 
the implementor). Or am I just missing something?



 but the earlier stage (text
> manipulation) may need information that can only be obtained from the 
> later stage (compilation): expressions within >>IF and >>EVALUATE 
…[8 more quoted lines elided]…
> has been completed!

This is blatant nonsense.  If that's in the standard then no-one in their 
right mind would try and implement it as written. (Funny, 2002 compliant 
COBOL compilers are not exactly thick on the ground...).

A vendor who was seriously committed to producing such a compiler would 
simply not use this approach. Why can the later stage not be entered until 
the earlier stage is complete? Of course it can. That's what multiple 
passes, placeholders, and cleanup phases are all about.


> In this sense, using constants within directives is a form of 'forward 
> reference'; If the concept of stages within the STD2002 is to be kept - 
> and I would not like to give it up! - constant entries are a problem that 
> make implementaion rather hard, if not impossible.

Ah, maybe Karl has offered a clue in the above.

"If the concept of stages within the STD2002 is to be kept - and I would not 
like to
give it up! "

Maybe that's what I am missing. Perhaps a quick summary of what these stages 
are, and what benefits accrue from implementing according to them, might 
shed some light on what this thread is discussing.  I have enough respect 
for Karl to recognise that if he is reluctant to give them up, there are 
probably good reasons; I'd just like some instances as to what those reasons 
might be...

If a documented approach in a standard means that implementors won't 
implement the product, then the Standard needs to change.

My contention is that it should never have documented or mandated 
implementation approaches  in the first place. Perhaps an Appendix of 
suggestions for implementors, but no way a mandated Standard. (Unless there 
is some really important benefit from this approach, that I am missing.)

BOTTOM LINE:

As far as I can see (unfettered by any mandated approach in the Standard) 
there is no technical difficulty with implementing anything that has been 
discussed here, forward references, dependent phases, CONSTANTS, Globals or 
not.

So what exactly is the problem?

Pete.
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 24)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-29T02:24:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ON4Bi.258300$rk4.112517@fe09.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com> <fb115t$6kc$1@nntp.fujitsu-siemens.com> <5jjs1vF3ua30hU1@mid.individual.net>`

```
Pete,
   For example,

The '02 Standard allows for
   COPY "literal-name".  *> previously this was an extension

Suppose you had

   Copy XYZ.

And within a member LMN, you had
   01  XYZ Constant Value "LMN".

but you didn't have any copy member XYZ.

As the '02 Standard currently stands (and *if* you allow constants to be used in 
the text manipulation stage), then it APPEARS that the Standard would require an 
implement to copy in the member "LMN" *before* it could know that "XYZ" was 
actually a constant name with the value "LMN".

Does this help you understand what this problem is?
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 25)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-30T01:18:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jla0pF4srfU1@mid.individual.net>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com> <fb115t$6kc$1@nntp.fujitsu-siemens.com> <5jjs1vF3ua30hU1@mid.individual.net> <ON4Bi.258300$rk4.112517@fe09.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:ON4Bi.258300$rk4.112517@fe09.news.easynews.com...
> Pete,
>   For example,
…[18 more quoted lines elided]…
> Does this help you understand what this problem is?

Yes, I think so, but I can't believe this is problematic. The old circular 
reference trick... Surely the Standard doesn't allow that?

The fact that LMN contains a constant called XYZ has no bearing whatsoever 
on the statement to COPY XYZ. (Which occurs in source ABC, say...) Why would 
it?

That is simply an illegal (circular) indirect reference. How can a source 
possibly know what is in all other sources that might be copied? It can't, 
and neither does it need to. If the action you actually want is to "COPY 
LMN", then XYZ would need to be defined as a constant with a value of "LMN" 
in the program where the COPY statement is made (ABC in my example), not in 
some other book that MIGHT be COPYed, or even in one that IS COPYed.

No one could reasonably expect such a circular reference to work, and if the 
standard allows it then that is probably an oversight. Seems to me that all 
that is required is for the Standard to state explicitly that circular 
references caused by using constants, or from any other cause, are coded at 
the programmer's own risk, and results are implementor defined. (Caveat 
emptor...)

In the example you're citing, the source can never be COPYed because there 
is no XYZ, and it can't just KNOW that LMN was the intended COPYbook.

I would expect, and I think most people would agree, that it will throw a 
compiler error of "COPYbook not found."
(I'd be perfectly happy with that; it would draw my attention to the 
problem...)

If your argument is that COPY using the constant might occur in source 
before the constant has been defined, thus requiring a forward reference, 
yes, I agree, it needs a forward reference. But that isn't the end of the 
world. Forward references can be dealt with easily by established techniques 
in a multipass compiler.

Now, how many angels CAN stand on a pinhead...? :-)

Pete.
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 26)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-29T10:59:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13db2kuoft2919a@corp.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com> <fb115t$6kc$1@nntp.fujitsu-siemens.com> <5jjs1vF3ua30hU1@mid.individual.net> <ON4Bi.258300$rk4.112517@fe09.news.easynews.com> <5jla0pF4srfU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:5jla0pF4srfU1@mid.individual.net...
[snip]
> If your argument is that COPY using the constant might occur in source
> before the constant has been defined, thus requiring a forward reference,
> yes, I agree, it needs a forward reference. But that isn't the end of the
> world. Forward references can be dealt with easily by established
techniques
> in a multipass compiler.

Forward reference is a misnomer.  It is an indirect reference;
to a literal (constant-entry), or to a data-description-entry
or record-description (typedef and object of SAME AS
clause). Many common languages use indirect backward
references; but I am not aware of any that permit indirect
forward references. The latter being the case, whence do
these "established techniques" come?

Furthermore, some uses of the SAME AS and TYPE
clauses and constant-entries will result in chains of indirect
references. Resolving these chains is analogous to creating
an indented list of parts from a product structure file (or table).
Relatively easy to do when the components and assemblies
are known (indirect backward references); but not so easy
when they are not yet known (indirect forward reference).

In other words, it is possible to accommodate indirect
forward references; but doing so adds an unprecedented
level of complexity to COBOL compiler development
with, in my opinion, no significant benefit.
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 27)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-29T18:34:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9%iBi.22098$1J4.81@fe06.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com> <fb115t$6kc$1@nntp.fujitsu-siemens.com> <5jjs1vF3ua30hU1@mid.individual.net> <ON4Bi.258300$rk4.112517@fe09.news.easynews.com> <5jla0pF4srfU1@mid.individual.net> <13db2kuoft2919a@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:13db2kuoft2919a@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
> news:5jla0pF4srfU1@mid.individual.net...
> [snip]
<more snip>
>
> In other words, it is possible to accommodate indirect
…[3 more quoted lines elided]…
>

Now, when we get away from these references in the "text manipulation stage" - 
which I think everyone agrees SHOULD be prohibited, we then get to the "more 
resources required to figuour out what is required" issue, that Rick mentions 
here. I think it is clear that the '02 Standard *does* place such a requirement 
on the implementer - and as far as I can tell everyone in J4 and Karl also agree 
this requirement is placed on the implementer.  This *CAN* be done and a 
conforming compiler must do it.

As someone who both helped develop the '02 Standard and eventually expressed my 
opposition to its final approval, I can safely state that this standard places 
MANY "very expensive" requirements on the implementer (many of which would 
provide minimal pay-back to the eventual user).  This is why the current 
direction is to make some new '02 fetures OPTIONAL in the next revision (if 
any).  Consider the Exception Handling RESUME statement and STANDARD ARITHMETIC 
(using an arbitrary intermediate data type that doesn't exist in the language) 
as prime examples.

There is (to me) a major difference between (obvious?) defect in the 
specification (like the COPY constant-name one) and "difficult but not 
impossible to implement" requirements like using TYPE statements before the 
corresponding TYPEDEF.
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 28)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-30T12:24:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jmh1rFbc90U1@mid.individual.net>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com> <fb115t$6kc$1@nntp.fujitsu-siemens.com> <5jjs1vF3ua30hU1@mid.individual.net> <ON4Bi.258300$rk4.112517@fe09.news.easynews.com> <5jla0pF4srfU1@mid.individual.net> <13db2kuoft2919a@corp.supernews.com> <9%iBi.22098$1J4.81@fe06.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:9%iBi.22098$1J4.81@fe06.news.easynews.com...
> "Rick Smith" <ricksmith@mfi.net> wrote in message 
> news:13db2kuoft2919a@corp.supernews.com...
…[18 more quoted lines elided]…
> implementer.  This *CAN* be done and a conforming compiler must do it.

The requirement that is placed on the implementor is that the function 
described be implemented as specified. (That's what a "standard" is for.) A 
fair corollary to this is that it should be POSSIBLE to implement as 
specified. (No one said it has to be easy...although that is obviously 
desirable.)
 What you're saying above seems to bear this out, so there shouldn't be a 
problem.

What I see happening here is people straying into second guessing what an 
implementor needs to do in order to comply.

This is presumptuous and pointless. There may exist an implementor somewhere 
who has techniques and approaches that are not in general use, may even take 
an entirely different approach that renders the whole issue a non-issue. 
Just because something is a "problem" to one operson doesn't mean it is a 
"problem" to "everyone".

(I have made considerable amounts of money by doing what was considered 
"impossible" by some... so I am very wary about putting this label on 
anything. More often than not, when computer people describe something as 
"not possible" what they are really saying is: "I don't know how to do it.". 
It is only impossible if the reason why it is impossible can be shown (as 
with a circular reference) and even then, caution is required. (It MIGHT be 
possible to solve even this by a different approach...)

<aside...skip this if you don't like anecdotes>

In my impetuous youth I realised that sometimes programming problems can be 
solved by adopting completely different and unexpected strategies.  De Bono 
calls it "lateral thinking" but it really doesn't matter what you call it... 
After having a few successes in this area I became persuaded that "nothing 
was impossible". I had a Scottish friend who had a wicked sense of humour 
and was also very insightful. After excitedly explaining my latest triumph 
to him he sat back and sipped his whisky. "So you think nothing is 
impossible?" I again launched into an exposition about attitude, and the 
power of Human ability to overcome all obstacles etc. etc. When I paused he 
looked at me and said: "Hang your arse out the window, then go down the road 
and throw stones at it." That was 40 years ago and I remember it like it was 
yesterday. :-)

</aside...skip this if you don't like anecdotes>

The Standard should confine itself to defining requirement. If, by accident 
or design it has strayed from that, then it should be set straight.

If it hasn't, then it simply needs to be clarified.


> As someone who both helped develop the '02 Standard and eventually 
> expressed my opposition to its final approval, I can safely state that 
…[10 more quoted lines elided]…
> the corresponding TYPEDEF.

That makes complete sense to me.

Thanks for that, Bill.

Pete.
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 27)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-30T11:50:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jmf1nFb2q4U1@mid.individual.net>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com> <fb115t$6kc$1@nntp.fujitsu-siemens.com> <5jjs1vF3ua30hU1@mid.individual.net> <ON4Bi.258300$rk4.112517@fe09.news.easynews.com> <5jla0pF4srfU1@mid.individual.net> <13db2kuoft2919a@corp.supernews.com>`

```


"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:13db2kuoft2919a@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[12 more quoted lines elided]…
> clause).

I referred to it as: "That is simply an illegal (circular) indirect 
reference."

However, whatever you call it has no bearing on what it does.

The issue here is with functionality, not nomenclature.


>Many common languages use indirect backward
> references; but I am not aware of any that permit indirect
> forward references. The latter being the case, whence do
> these "established techniques" come?

I can't believe this, Rick. I never said there were techniques for dealing 
with "indirect forward references"; on the contrary I suggested that such 
would be illegal due to circularity. As usual,  you are much more interested 
in having an argument, or parading your book learning, than solving a 
problem.

Does the standard require that circular references be permitted or does it 
not?

How would you address this?

I already made my suggestion.
>
> Furthermore, some uses of the SAME AS and TYPE
…[6 more quoted lines elided]…
>
So you won't be writing a 2002 compliant compiler any time soon, then?

> In other words, it is possible to accommodate indirect
> forward references; but doing so adds an unprecedented
> level of complexity to COBOL compiler development
> with, in my opinion, no significant benefit.

Well, that's your opinion and perfectly valid as such.

Others may disagree.

Pete.
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 27)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-29T21:39:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13dc83o19ril2a8@corp.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com> <fb115t$6kc$1@nntp.fujitsu-siemens.com> <5jjs1vF3ua30hU1@mid.individual.net> <ON4Bi.258300$rk4.112517@fe09.news.easynews.com> <5jla0pF4srfU1@mid.individual.net> <13db2kuoft2919a@corp.supernews.com>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:5jmf1nFb2q4U1@mid.individual.net...
>
>
…[7 more quoted lines elided]…
> >> before the constant has been defined, thus requiring a forward
reference,
> >> yes, I agree, it needs a forward reference. But that isn't the end of
the
> >> world. Forward references can be dealt with easily by established
> > techniques
…[22 more quoted lines elided]…
> would be illegal due to circularity. As usual,  you are much more
interested
> in having an argument, or parading your book learning, than solving a
> problem.
…[31 more quoted lines elided]…
>

It is not clear to me exactly how the total absence of
personal pronouns in my comments should be construed
as personal; however, let me clarify.

I took one paragraph completely out of context because
its words stimulated some thoughts. I then wrote and
posted those thoughts for interested readers to consider.

Nothing more than that was intended.
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 28)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-30T15:42:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jmsl6FbvmpU1@mid.individual.net>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com> <fb115t$6kc$1@nntp.fujitsu-siemens.com> <5jjs1vF3ua30hU1@mid.individual.net> <ON4Bi.258300$rk4.112517@fe09.news.easynews.com> <5jla0pF4srfU1@mid.individual.net> <13db2kuoft2919a@corp.supernews.com> <5jmf1nFb2q4U1@mid.individual.net> <13dc83o19ril2a8@corp.supernews.com>`

```


"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:13dc83o19ril2a8@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[86 more quoted lines elided]…
>
OK. I 've let it go.

You might consider that when you respond in a thread to a specifc post, the 
person postng it has reason to believe you are responding to them. If what 
you say then appears to dispute what has already been said, then there will 
be a reaction. It doesn't require personal pronouns :-)

I have nothing more to say on this thread anyway.

Pete.
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 23)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-29T02:15:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GE4Bi.188127$jE4.178252@fe12.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com> <fb115t$6kc$1@nntp.fujitsu-siemens.com>`

```
Karl and Roger,
  OK - I see your problem.  There is the IMPLICATION that literals in the "text 
manipulation stage" may not be constants, but it certainly isn't explict.  (I am 
more than happy to do a "defect report" on this - if neither of you do.)

The IMPLICATION is on page 31 where it is describing "text words" (what the text 
manipulation stage deals with) where it says,

"2) an alphanumeric, boolean, or national literal including the opening and 
closing delimiters that bound the literal;"

Therefore, (unlike numeric literals) I would INFER that something without 
literal delimiters is NOT a "valid" literal in the text manipulation stage.

I believe that rule 10 on page 40 should be "expanded" to exclude 
constant-names - and the same restriction should be applied to COPY and REPLACE 
statements.
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 24)_

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2007-08-29T10:01:47+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fb395c$jjg$1@nntp.fujitsu-siemens.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com> <fb115t$6kc$1@nntp.fujitsu-siemens.com> <GE4Bi.188127$jE4.178252@fe12.news.easynews.com>`

```
"William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
news:GE4Bi.188127$jE4.178252@fe12.news.easynews.com...
> Karl and Roger,
>  OK - I see your problem.  There is the IMPLICATION that literals in the 
…[16 more quoted lines elided]…
> REPLACE statements.

Bill, Roger and all others, please accept my excuses to have troubled you 
all with the directives + constants problem - someone has already tackeled 
it: my colleague Susanne Hinz found, that in the WD1.7 for the next 
standard, syntax rule 2 of the constant entry has been refined to:
"Constant-name-1 may be used anywhere, EXCEPT IN A COMPILER DIRECTIVE, that 
a format specifies a literal of the class and category of constant-name-1"
This solves the problem at least partly, but I fully agree with Bill, that 
the same restriction should be applied to COPY!

Pete, for understanding the problem, I can offer my personal interpretation 
of the standard: the standard defines only 2 stages of compilation, the 
'text manipulation' followed by the 'compilation' - but these are not 
bindingly for a compiler, but rather a means for description of the COBOL 
language and a basis for the various rules. Nevertheless for me they define 
a natural separation:

1) the very first thing, before starting the real compilation, is to 
establish the source that is to be compiled; this is the only task of the 
'text manipulation', especially selecting parts that are to be excluded from 
compilation due to directives, including/resolving COPY elements and 
performing the various replacements.

2) afterwards the real compilation can start working on this source and may 
be structured as various steps/passes beginning with a lexical analysis, 
followed by syntax analysis and so on - just as described in the 'dragon 
book'.

Even though similar tasks are to be performed in both stages (some sort of 
lexical and  syntax analysis is needed in the text manipulation stage in 
order to recognize directives, COPY and REPLACE statements), I think it is 
helpful to keep these stages separated, for instance to reduce complexity of 
tasks - but the standard does not force this separation upon a compiler!

Karl Kiesel
Fujitsu Siemens Computers, M�nchen
```

###### ↳ ↳ ↳ Re: CONSTANT ENTRY (was "forward" references (was: COBOL subscript range checking))

_(reply depth: 23)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-29T02:19:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gJ4Bi.190008$Bo7.179257@fe07.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com> <PLoAi.162805$jE4.61866@fe12.news.easynews.com> <faugsm$q0c$1@nntp.fujitsu-siemens.com> <e4EAi.169153$Bo7.88986@fe07.news.easynews.com> <fb115t$6kc$1@nntp.fujitsu-siemens.com>`

```
"Roger While" <simrw@sim-basis.de> wrote in message 
news:fb1dmk$at6$01$1@news.t-online.com...
<snip>
> Incidentally a GLOBAL CONSTANT is somewhat different
> in that it has to abide by the GLOBAL constraint.
…[5 more quoted lines elided]…
>
Roger,
  I see where a GLOBAL constant *MAY* be referenced after it is defined, but I 
don't see where it is prohibited from being used BEFORE it is defined (as long 
as it is defined at the "same" level of program nesting).

Can you show me where you think there is a constraint otherwise?
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 19)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-08-27T07:59:48+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fatp8r$seh$02$1@news.t-online.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <1186664714.481032.142460@d55g2000hsg.googlegroups.com> <46BB4831.6F0F.0085.0@efirstbank.com> <h02pb3psoiov1v33fi63o7s1l3fum2i390@4ax.com> <46BC3F84.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <izPzi.6595$SB3.5422@fe03.news.easynews.com> <13d0772t303f405@corp.supernews.com> <oMbAi.152024$sR4.54373@fe08.news.easynews.com> <13d2rm6ho25no66@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
news:13d2rm6ho25no66@corp.supernews.com...
>
> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message
…[24 more quoted lines elided]…
> hope it is the same.


MF SE up to and including 4.0 does the same.

Roger




> -----
> * Micro Focus COBOL Version 3.2.24 [...] 26-Aug-07 06:35 Page   1
…[79 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 15)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-25T06:08:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188047337.835940.89460@x35g2000prf.googlegroups.com>`
- **In-Reply-To:** `<13cqhb08ttqa331@corp.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com>`

```
On 23 Aug, 09:26, "Rick Smith" <ricksm...@mfi.net> wrote:
> "William M. Klein" <wmkl...@nospam.netcom.com> wrote in messagenews:2QPyi.2107$fh4.476@fe01.news.easynews.com...
>
…[118 more quoted lines elided]…
> apply the appropriate rules.

That would assume that the compiler is a single-pass compiler. IIRC,
even the S/370 Assembler takes two passes to assemble code correctly
and it would not be too much for a compiler to reach a forward
reference and READ FORWARD from that point to resolve the issue.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 16)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-25T12:23:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13d0m30mtmcv307@corp.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <f9k9bd$k8t$03$1@news.t-online.com> <46C027A1.6F0F.0085.0@efirstbank.com> <13c12vgjujfrc9@corp.supernews.com> <dt2wi.205221$ss3.140750@fe01.news.easynews.com> <13c1u70s8s3gvfc@corp.supernews.com> <N6awi.448183$LL7.77458@fe08.news.easynews.com> <sbawi.212706$u82.113159@fe09.news.easynews.com> <13c34ih2h8d0m9b@corp.supernews.com> <2QPyi.2107$fh4.476@fe01.news.easynews.com> <13cqhb08ttqa331@corp.supernews.com> <1188047337.835940.89460@x35g2000prf.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
news:1188047337.835940.89460@x35g2000prf.googlegroups.com...
> On 23 Aug, 09:26, "Rick Smith" <ricksm...@mfi.net> wrote:
> > "William M. Klein" <wmkl...@nospam.netcom.com> wrote in
messagenews:2QPyi.2107$fh4.476@fe01.news.easynews.com...
> >
> > > Rick,
…[6 more quoted lines elided]…
> > > submit an interpretation request, but I certainly do think that those
who
> > have
> > > "constants" now (any format) allow forward references - and I am also
99%
> > > certain that MF (for example) allows forward references for typedefs.

[snip]

> > Given the following code (numbered lines have forward
> > references):
…[18 more quoted lines elided]…
> reference and READ FORWARD from that point to resolve the issue.

I make no such assumption!

The following could be done:
Pass 1: Produce logically-converted compilation group
Pass 2: Produce expanded compilation group
Pass 3. Produce conditionally-processed compilation group
Pass 4: Produce structured compilation group
Pass 5: Produce intermediate code
Pass 6: Optimization
Pass 7: Produce object code
Pass 8: Produce source listing
Pass 9: Produce cross-reference listing
Pass 10: Produce assembler listing

It is during Pass 5 that syntax rules and those general rules
affecting compilation are applied. This is where the errors,
noted above, are recognized.

What you seem to be saying is that Pass 5, in this scenario,
could be written (i.e., "butchered" <g>) to accommodate
certain forward references, while I find no explicit requirement
to treat them as forward references.

I see the following as practical equivalents:

(1)
    01 item pic x(pic-size).
    replace ==pic-size== by ==20==.
(2)
    01 item pic x(pic-size).
    01 pic-size constant 20.

And, in both cases, I see it as an error. Reverse the sequences
and both are valid. While the general rules for the REPLACE
statement and the constant-entry are very different, their end is
the same. Neither has, as far as I can tell, any explicit rule(s)
regarding forward references. Thus, to treat the first as an error;
but claim the second is valid is illogical.
```

#### ↳ Re: COBOL subscript range checking

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2007-08-09T14:41:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20070809.14414997@rechner12.lerch.xl>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com>`

```


?? Ursprüngliche Nachricht

Am 08.08.07, 18:19:42, schrieb "Frank Swarbrick" 
<Frank.Swarbrick@efirstbank.com> zum Thema COBOL subscript range 
checking:

Hi Frank

> I am wondering what philosophy other shops out there have with regard 
to
> COBOL, CICS, and subscript range checking.  We currently have the 
CHECK LE
> runtime option turned ON, but our compiler is set with NOSSRANGE.  
This
> means that the code for range checking is not compiled in to the
> executables, and therefore range checking is not done, even though 
it's set
> to ON at the runtime level.

COBOL calculates the addresses relative to the beginning of a table or 
MOVE.
With SSR, COBOL add something like this code to the object code:

	IF POINTER BEFORE TABLE
	OR POITER AFTER TABLE
	  CALL IGZ??? --> to Abend
	END-IF

this code take about 6 to 8 or so instructions and can be 20 bytes 
long (or so)

The runtime option is only a marker to tell IGZ???: to do or not to do 
an abend....

> So the question is, is range checking in production (especially 
production
> CICS) programs a good idea?  What type of performance hit can be 
expected if
> we turn it on?

	YES - YOU MUST.
Sorry - there is no significant performance degration, even you have 
no haevy load on your transactions. I have done some experiances with 
SSR oan NOSSR, and my resulty are:

Load module --> SSR is some bytes larger than NOSSR --> irrelevant - 
modules are loaded once an in storage.
CPU-cost --> irrelevant --> one transaction ist running in 0,0001 or 
0,0015 cpu-seconds

I have no other degrations with SSR, bit I think: a PERFORM has more 
overhaed than SSR.

We use SSR since the implementation of COBOL-II (late 80th of the last 
century) and we have a small number, 2 or 3, of programms, that are 
compiled with NOSSR, to keep the runtime an cpu-load less, but these 
programms are called several million times in ONE process,(most batch)

more significant for a problem could this be:

	01 table1 occurs 10 indexed by index1.
	05 field-of-table1 pic x(10).
	01 table2 occurs 10 indexed by index2.
	05 field-of-table2 pic x(20).

With this commands:

	SET INDEX1 TO 3
	MOVE FIELD-OF-TABLE2 (INDEX1) TO ???

which bytes are moved?

Yes: 
COBOL calculates 3 x 10 and add the result to the beginning of table2, 
then the MOVEwill be done like following:

	MOVE TABLE2 (30:20) to ???

you can never find this mistake, with or without SSR....

The better way to reduce runtime and cpu-consuming ist to optimize 
your I/O - IMS, VSAM, more DB2. When we change from ESCON to FICON, 
our batch-runtimes are the half than before (german: halbiert see: 
LEO)

the most, we save, are accesses to DB2............

I am an experiance since 1980 with COBOL and Assembler on MVS and 
z/OS. I learned to read a systemdump of cobol backward to resolv the 
source field of a compute.

Einen schoenen Tag
Andreas Lerch
```

#### ↳ Re: COBOL subscript range checking

- **From:** CG <Carl.Gehr.ButNoSPAMStuff.4@MCGCG.Com>
- **Date:** 2007-08-09T12:08:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf20e$46bb3bf5$d06620ed$10913@FUSE.NET>`
- **In-Reply-To:** `<46B998BE.6F0F.0085.0@efirstbank.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com>`

```
Frank Swarbrick wrote:
> I am wondering what philosophy other shops out there have with regard to
> COBOL, CICS, and subscript range checking.  We currently have the CHECK LE
…[31 more quoted lines elided]…
> So what does everyone think?

Rather than speculating, I have pasted the results from the IBM COBOL 
Performance Tuning document below.  Note:  This was done with Enterprise 
COBOL V3.1, so it is a bit obsolete with V3.4 as the current product 
level.  OTOH, I don't believe there has been significant changes in this 
area.

I would also suggest that, the overhead would be less for the compiler 
doing the same number of tests versus hand coding the tests in the 
program.  As indicated below, testing all versus some of the subscript 
references should be your guide.

My experience is that, it is very common to compile with SSRANGE and run 
with CHECK(OFF).  It can significantly reduce problem determination time 
by not having to recompile.  And, in some shops, there are major 
impediments to recompiles, but a run-time option change is much easier 
to do, especially when the objective is fixing a production problem.

Here are the IBM results:
> SSRANGE or NOSSRANGE
> Using SSRANGE generates additional code to verify that all
…[21 more quoted lines elided]…
>    with a range of equivalent to 16% slower.

So, in the second, more recommended situation:  You may not have much 
penalty at all [equivalent] but the worst case is 9%.  So, I'd say other 
decision points:  How critical is the application?  How critical is the 
application's performance?  How important is it to get the application 
fixed if it does fail?  [YMMV...]

Carl
```

##### ↳ ↳ Re: COBOL subscript range checking

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-09T10:22:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1ffmb3tplbaec2csbe5c137tshlipn5gut@4ax.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <cf20e$46bb3bf5$d06620ed$10913@FUSE.NET>`

```
On Thu, 09 Aug 2007 12:08:18 -0400, CG
<Carl.Gehr.ButNoSPAMStuff.4@MCGCG.Com> wrote:

>I would also suggest that, the overhead would be less for the compiler 
>doing the same number of tests versus hand coding the tests in the 
>program.  As indicated below, testing all versus some of the subscript 
>references should be your guide.

That's something that always bothered me about any standard to turn
off an overflow check.    This doesn't mean we should save cycles by
not checking for overflow - it only means that we code the check by
hand.   How does that save cycles?    Especially since it is easier to
optimize code where the compiler understands exactly what is desired
than when it is guessing what is significant to the programmer.

Lots of coding would be more efficient with exception processing
rather than checking everything ahead of time.    This isn't always
part of the design of CoBOL - calling a function to find out whether
we can call a function is inefficient and ugly.
```

##### ↳ ↳ Re: COBOL subscript range checking

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-09T10:26:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<srfmb359lh1qn37kkiohoe5crmccmfm8c9@4ax.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <cf20e$46bb3bf5$d06620ed$10913@FUSE.NET>`

```
On Thu, 09 Aug 2007 12:08:18 -0400, CG
<Carl.Gehr.ButNoSPAMStuff.4@MCGCG.Com> wrote:

>So, in the second, more recommended situation:  You may not have much 
>penalty at all [equivalent] but the worst case is 9%.  So, I'd say other 
>decision points:  How critical is the application?  How critical is the 
>application's performance?  How important is it to get the application 
>fixed if it does fail?  [YMMV...]

And what are the alternatives to having the compiler check?   Options
include:

1.   Have the program check - that doesn't save cycles.
2.   Have the program abort with overflow.
3.   Have the program run - with unpredictable results.

I know, sometimes the design can mean that no checking is necessary -
until maintenance makes changes.    And we see lots of highly paid
programmers write critical applications with overflow vulnerabilities.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2007-08-09T21:15:52+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vcmmb3l7jkut1s0mhavotiukg8rm1cq9qr@4ax.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <cf20e$46bb3bf5$d06620ed$10913@FUSE.NET> <srfmb359lh1qn37kkiohoe5crmccmfm8c9@4ax.com>`

```
On Thu, 09 Aug 2007 10:26:12 -0600 Howard Brazee <howard@brazee.net> wrote:

:>On Thu, 09 Aug 2007 12:08:18 -0400, CG
:><Carl.Gehr.ButNoSPAMStuff.4@MCGCG.Com> wrote:

:>>So, in the second, more recommended situation:  You may not have much 
:>>penalty at all [equivalent] but the worst case is 9%.  So, I'd say other 
:>>decision points:  How critical is the application?  How critical is the 
:>>application's performance?  How important is it to get the application 
:>>fixed if it does fail?  [YMMV...]

:>And what are the alternatives to having the compiler check?   Options
:>include:

:>1.   Have the program check - that doesn't save cycles.

False.

The program does not need to check every reference, i.e., if SUB is used 20
times it need only check when it is set.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-08-09T18:30:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f9fmgp$33i$1@reader2.panix.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <cf20e$46bb3bf5$d06620ed$10913@FUSE.NET> <srfmb359lh1qn37kkiohoe5crmccmfm8c9@4ax.com> <vcmmb3l7jkut1s0mhavotiukg8rm1cq9qr@4ax.com>`

```
In article <vcmmb3l7jkut1s0mhavotiukg8rm1cq9qr@4ax.com>,
Binyamin Dissen  <postingid@dissensoftware.com> wrote:
>On Thu, 09 Aug 2007 10:26:12 -0600 Howard Brazee <howard@brazee.net> wrote:
>
…[17 more quoted lines elided]…
>times it need only check when it is set.

Well, in the Oldene Dayse I recall being taught that a subscript was 
supposed to be range-checked for every incrementing/decrementing... I 
posted some code here a while back where that was done and even included 
Classic Mistake Number (your choice) of checking the data-condition before 
the subscript's range.

DD
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 4)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-08-09T20:54:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13bnh9bp7e7dc95@news.supernews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <cf20e$46bb3bf5$d06620ed$10913@FUSE.NET> <srfmb359lh1qn37kkiohoe5crmccmfm8c9@4ax.com> <vcmmb3l7jkut1s0mhavotiukg8rm1cq9qr@4ax.com>`

```
Binyamin Dissen wrote:
>
>>> 1.   Have the program check - that doesn't save cycles.
…[4 more quoted lines elided]…
> used 20 times it need only check when it is set.

Ah, but the subscript could change without having been changed. For example:

01  MYSTUFF.
  02  MYNAME  OCCURS 5 PIC X(50).
  02  MYADDR   OCCURS 5 PIC X(60).
  ...
  02  MYINDX   PIC S9(7) COMP-5.
  02  MYOTHERTHING  OCCURS 5 PIC X(100).
  ...

PERFORM VARYING MYINDX FROM 1 BY 1 UNTIL MYINDX > 5
   ...
   IF (something-really-weird)
       MOVE SPACE TO MYSTUFF
   END-IF
   ...
   MOVE 'RESIDENT' TO MYNAME(MYINDX)
   ...

The subscript was not changed under program control - it was changed by a 
completely unrelated bug. Bounds checking would catch the error, manual 
checking would not.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 5)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2007-08-10T09:54:26+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8p2ob31gsi9dqtnm8ug0m5dvnngfkitlo9@4ax.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <cf20e$46bb3bf5$d06620ed$10913@FUSE.NET> <srfmb359lh1qn37kkiohoe5crmccmfm8c9@4ax.com> <vcmmb3l7jkut1s0mhavotiukg8rm1cq9qr@4ax.com> <13bnh9bp7e7dc95@news.supernews.com>`

```
On Thu, 9 Aug 2007 20:54:08 -0500 "HeyBub" <heybubNOSPAM@gmail.com> wrote:

:>Binyamin Dissen wrote:

:>>>> 1.   Have the program check - that doesn't save cycles.

:>> False.

:>> The program does not need to check every reference, i.e., if SUB is
:>> used 20 times it need only check when it is set.

:>Ah, but the subscript could change without having been changed. For example:

:>01  MYSTUFF.
:>  02  MYNAME  OCCURS 5 PIC X(50).
:>  02  MYADDR   OCCURS 5 PIC X(60).
:>  ...
:>  02  MYINDX   PIC S9(7) COMP-5.
:>  02  MYOTHERTHING  OCCURS 5 PIC X(100).
:>  ...

:>PERFORM VARYING MYINDX FROM 1 BY 1 UNTIL MYINDX > 5
:>   ...
:>   IF (something-really-weird)
:>       MOVE SPACE TO MYSTUFF
:>   END-IF
:>   ...
:>   MOVE 'RESIDENT' TO MYNAME(MYINDX)
:>   ...

:>The subscript was not changed under program control - 

It certainly was.

:>                                                      it was changed by a 
:>completely unrelated bug. Bounds checking would catch the error, manual 
:>checking would not. 

And the bounds checking would not provide any useful information.

Perhaps some folk need training wheels - a real programmer will do his own
bounds checking.
```

###### ↳ ↳ ↳ Re: COBOL subscript range checking

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-10T09:55:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<te2pb3tp9dqkp9e46nf04jg9pmi7o5tsha@4ax.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <cf20e$46bb3bf5$d06620ed$10913@FUSE.NET> <srfmb359lh1qn37kkiohoe5crmccmfm8c9@4ax.com> <vcmmb3l7jkut1s0mhavotiukg8rm1cq9qr@4ax.com> <13bnh9bp7e7dc95@news.supernews.com> <8p2ob31gsi9dqtnm8ug0m5dvnngfkitlo9@4ax.com>`

```
On Fri, 10 Aug 2007 09:54:26 +0300, Binyamin Dissen
<postingid@dissensoftware.com> wrote:

>Perhaps some folk need training wheels - a real programmer will do his own
>bounds checking.

In real life, memory leaks are a huge problem.    Requiring that all
programmers be "real programmers" is not a real solution.

I knew someone who was creating a class on debugging, and he purposely
created a bounds error - but got a data exception (SOC-7).   It seems
that his out-of-bounds change hit program memory instead of data
memory.
```

##### ↳ ↳ Re: COBOL subscript range checking

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-09T17:09:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46BB4A38.6F0F.0085.0@efirstbank.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <cf20e$46bb3bf5$d06620ed$10913@FUSE.NET>`

```
>>> On 8/9/2007 at 10:08 AM, in message
<cf20e$46bb3bf5$d06620ed$10913@FUSE.NET>,
CG<Carl.Gehr.ButNoSPAMStuff.4@MCGCG.Com> wrote:
> Frank Swarbrick wrote:
>> I am wondering what philosophy other shops out there have with regard to
…[78 more quoted lines elided]…
>> performance sensitive applications, NOSSRANGE is recommended.

That's kind of an odd comment.  Certainly they are not advocating a time
when you should *intentionally* note code your own range checks?  The
problem with explicit range checks is that, well, they may be wrong.  So, in
my way of thinking, SSRANGE gives you *two* types of range checking: the
explicitly coded one which will hopefully handle an out of range by doing
something sensible, and SSRANGE which will simply blow up if your explicit
range checking logic is faulty.

>> Performance considerations using SSRANGE:
>> *  On the average, SSRANGE with the run-time option CHECK(ON) was 
…[9 more quoted lines elided]…
>>    with a range of equivalent to 16% slower.

I'm afraid I don't understand what is meant by "...a range of equivalent
to...".
 
> So, in the second, more recommended situation:  You may not have much 
> penalty at all [equivalent] but the worst case is 9%.  So, I'd say other 
> decision points:  How critical is the application?  How critical is the 
> application's performance?  How important is it to get the application 
> fixed if it does fail?  [YMMV...]

Thanks for the info!

Frank
```

#### ↳ Re: COBOL subscript range checking

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-10T04:42:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S0Sui.144549$Zr1.94902@fe06.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com>`

```
(I have followed some - but not all - of this thread in both IBM-MAIN and 
comp.lang.cobol - but haven't replied yet).

As far as I can tell from the notes that I have read so far, no one has pointed 
to the performance paper comments on this.  It should be noted that Frank is 
usually interested in COBOL under VSE, so Enterprise COBOL *may* not be exactly 
the same.  However, if you look at the paper at:

 http://www-1.ibm.com/support/docview.wss?uid=swg27001475&aid=1

It has the following (exceprted) information:

"SSRANGE or NOSSRANGE

Using SSRANGE generates additional code to verify that all subscripts, indexes, 
and reference modification | expressions do not refer to data beyond the bounds 
of the subject data item. This in-line code occurs at every reference to a 
subscripted or variable-length data item, as well as at every reference 
modification expression, and it can result in some degradation at run time. In 
general, if you need to verify the subscripts only a few times in the 
application instead of at every reference, coding your own checks may be faster 
than using the SSRANGE option. For performance sensitive applications, NOSSRANGE 
is recommended.

Performance considerations using SSRANGE:

   On the average, SSRANGE with the run-time option CHECK(ON) was 1% slower than 
NOSSRANGE, with a range of equivalent to 27% slower.

   On the average, SSRANGE with the run-time option CHECK(OFF) was 1% slower 
than | NOSSRANGE, with a range of equivalent to 9% slower.

   On the average, SSRANGE with the run-time option CHECK(ON) was 1% slower than 
SSRANGE with the run-time option CHECK(OFF) with a range of equivalent to 16% 
slower.

 (COB PG: pp 313, 333, 545)"

   ***

My personal GENERAL rules-of-thumb are:

1) Have the default compiler option set to SSRANGE (for production and test)

2) Have the run-time option for test set to CHECK(ON)

3) Have the run-time option for production set to CHECK(OFF) - but know how to 
turn it on when symptoms indicate the need.

4) Make certain that VERY performance-sensitive applications that use many 
subscripts and reference modification, compile with NOSSRANGE (but document 
this)

In general, these rules apply to both batch and online applications. However, 
having the ned for NOSSRANGE for online may occur more often than for batch 
(depending upon system design).
```

##### ↳ ↳ Re: COBOL subscript range checking

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-10T04:46:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W4Sui.111452$Vy2.94915@fe10.news.easynews.com>`
- **References:** `<46B998BE.6F0F.0085.0@efirstbank.com> <S0Sui.144549$Zr1.94902@fe06.news.easynews.com>`

```
OOPS - I read further and found that the Performance Paper was quoted.  Sorry to 
repeat the input of others.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
