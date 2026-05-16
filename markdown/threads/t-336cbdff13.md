[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol (Coding problem)

_21 messages · 10 participants · 2005-01_

---

### Cobol (Coding problem)

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-01-22T14:42:01+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cssq0a$95o$1@reader01.singnet.com.sg>`

```
Hi,
I have got some coding problem and appreciate someone could help advise
on how it should be done. Quite complicated though.Tks in advance.


Scenario (1)
============
1) If there is only 1 record only with version 00,
   then if date1 field = non-current date
   and date2 field = current date, o/p to file(B)

   In short, record pattern is  :
                    verno    date1                  date2
   xxx xxx xxx   00    non-current date   current date      => o/p to 
file(B)


Scenario(2)
============
2) However If there are multiple records(same key) with
   version 00, 01, 02 etc, have to check that
   if it is ver00 and date(1) field = non-current date
   and date(2) field = current date, o/p to file(B)

   For the rest of the record with same key (ie version 01,02 etc)
   if date(1) field = current date or that date(2) field is
   current or non-current date, o/p to file(A)


   In short, record pattern is :
                verno  date1              date2
   xxx xxx xxx   00    non-current date   current date     => o/p to file(B)
   xxx xxx xxx   01    current date       current date     => o/p to file(A)
   xxx xxx xxx   02    current date       non-current date => o/p to file(A)


(P/S: For o/p to file(B), only allow for version 00 records only)



How should I code for something that is able to perform the above??

I have some coding and towards the end, I coded like

If group-change      => group change refer to the group of any xxx field 
above
   if date(2) field = current date
      o/p to file(B)
   end-if
end-if

** It work for scenario(1) only but got bug in scenario(2). Can advise
how the coding should be done ??

** I thought of coding to check that if version no. not = spaces, then 
perform
something, but if you had ver00 or version01,02,etc, all these are consider 
not
= spaces.They are suppose to perform different things for version that is 
00,
and the rest of the version 01,02 etc.Not sure how I should code it.
```

#### ↳ Re: Cobol (Coding problem)

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-22T09:18:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9PKJzgN9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg>`

```
.    On  22.01.05
  wrote  leng1@bigfoot.com (Rick)
     on  /COMP/LANG/COBOL
     in  cssq0a$95o$1@reader01.singnet.com.sg
  about  Cobol (Coding problem)


   I allow myself to rearrange the quoted descriptions a little bit


l> Scenario(1)
l> ============
l> 1) If there is only 1 record only with version 00,
l>    then
l>       if date1 field = non-current date
l>          and date2 field = current date,
         THEN
l>          o/p to file(B)


l> Scenario(2)
l> ============
l> 2) However If there are multiple records(same key) with
l>    version 00, 01, 02 etc, have to check that

l>    if it is ver00
l>      and date(1) field = non-current date
l>      and date(2) field = current date,
      THEN
l>      o/p to file(B)


   Frankly, I do not see any difference between the two scenarios,  
unless you say that the in the case of _multiple_ occurences of  
Version 00 the second and subsequent records with Version ï¿½ï¿½ have to  
be treated differently.

   You can use the same conditional for both scenarios, as coded above  
by yourself (well, some syntactic accomodations, like "Date1 NOT =  
Current-Date", e.g.).

   You might of course try something more fancy, and use EVALUATE:



 EVALUATE
   Version, ALSO Date1 = Current-Date, ALSO Date2 = Current-Date

      WHEN '00', ALSO FALSE, ALSO TRUE
         WRITE File-B-Record FROM INput-File-Record
      OTHERWISE
         WRITE File-A-Record FROM Input-File-Record
  END-EVALUATE


  But for a binary choice, you might as well use IF .. THEN .. ELSE..  
END-IF.


HAve fun!
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Die Superklugheit ist eine der verï¿½chtlichsten Arten von Unklugheit. -G.C.Lichtenberg
```

##### ↳ ↳ Re: Cobol (Coding problem)

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-01-23T01:13:04+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cstuvh$afc$1@reader01.singnet.com.sg>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <9PKJzgN9flB@jpberlin-l.willms.jpberlin.de>`

```
Hi,
There is different for 2nd scenario

Record pattern is :
                      verno     date1                     date2
   xxx xxx xxx   00       non-current date    current date         => o/p to 
file(B)
   xxx xxx xxx   01       current date           current date         => o/p 
to file(A)
   xxx xxx xxx   02       current date            non-current date => o/p to 
file(A)

For ver00, date2 must be current date, then o/p to file(B)
For all other version of the SAME group(xxx), so long date1 is current date, 
o/p to file(A)
Of course, I do not know how may version there will be so may need to use 
'PERFORM... UNTIL'
to write out all the records of the same group (ver01,02,03 etc) to file(A) 
so long date1 field
is current date but not sure how to go about coding it using PERFORM.... 
UNTIL



"Lueko Willms" <l.willms@jpberlin.de> wrote in message 
news:9PKJzgN9flB@jpberlin-l.willms.jpberlin.de...
>.    On  22.01.05
>  wrote  leng1@bigfoot.com (Rick)
…[33 more quoted lines elided]…
> be treated differently.
==> Yes, they are supposed to be treated differently


>
>   You can use the same conditional for both scenarios, as coded above
…[26 more quoted lines elided]…
> Unklugheit. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-22T19:43:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9PKO$z7eflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <9PKJzgN9flB@jpberlin-l.willms.jpberlin.de> <cstuvh$afc$1@reader01.singnet.com.sg>`

```
.    On  23.01.05
  wrote  leng1@bigfoot.com (Rick)
     on  /COMP/LANG/COBOL
     in  cstuvh$afc$1@reader01.singnet.com.sg
  about  Re: Cobol (Coding problem)


l> There is different for 2nd scenario

   according to what you explained in your original message, I do not  
see the slightest difference, and what you advance here, does it  
neither.

l>
l> Record pattern is :
l>                       verno     date1                     date2
l>    xxx xxx xxx   00       non-current date    current date         =>
l> o/p to file(B)
l>    xxx xxx xxx   01       current date           current date
l> => o/p to file(A)
l>    xxx xxx xxx   02       current date            non-current date =>
l> o/p to file(A)
l>
l> For ver00, date2 must be current date, then o/p to file(B)
l> For all other version of the SAME group(xxx), so long date1 is current
l> date, o/p to file(A)

   You have three conditions for the record being copied to file_B  
instead of file_A:

        Version = '00'
    AND date1 NOT = current-date
    AND date2     = current-date

    all input-records which do not fulfill these conditions are being  
copied to file_A.

    Did I miss something? Then explain.

    The only loop you have to code is the one over the valid records  
of the input file; the decision for copying is done via a simple
IF ... THEN ... ELSE ... END-IF


    The whole program (well, the procedural part) could go like this:



--------- schnipp -----------------------------------------
 PROCEDURE DIVISION.
 DECLARATIVES.

   *> event handlers for unrecoverable errors
   *> on input or output files go here

 END-DECLARATIVES.

 MAIN SECTION.
 BEGIN.
    OPEN INPUT input-file
    IF is-not-present-file in status-input-file
    THEN                                  *> minor filestat = '5'
      DISPLAY "input-file is not present"
    ELSE
      MOVE FUNCTION(CURRENT-DATE) TO My-Current-Date
      READ input-file
      IF has-reached-EOF in status-input-file
      THEN                                *> Major filestat = '1'
        DISPLAY "input-file is empty"
      ELSE
        OPEN OUTPUT output-file-A, output-file-B
        PERFORM WITH TEST AFTER
                UNTIL has-reached-EOF in status-input-file
          *> we now surely do have a valid record from input-file
          IF Version OF input-file-record = '00'
            AND date-1 OF input-file-record NOT = My-Current-Date
            AND date-2 OF input-file-record = My-Current-Date
          THEN
            WRITE output-file-B-record FROM input-file-record
          ELSE
            WRITE outpuf-file-A-record FROM input-file-record
          END-IF
          READ input-file
        END-PERFORM
        CLOSE output-file-A, output-file-B
      END-IF
      CLOSE input-file
    END-IF
    .
 END-IT.
    STOP RUN
    .
------------------ schnapp --------------------------------

   You would need the three preceding DIVISIONs with all the necessary  
declarations, of course.

   Errors with OPEN or CLOSE or other unrecoverable errors are dealt  
with in the event-handlers in the DECLARATIVES.


   Where is the problem?

   I could not discern any other conditions from your explanations.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Er liebte hauptsï¿½chlich die Wï¿½rter, die nicht in Wï¿½rterbï¿½chern vorzukommen pflegen. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-01-22T20:46:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10v63v947i6g071@news.supernews.com>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <9PKJzgN9flB@jpberlin-l.willms.jpberlin.de> <cstuvh$afc$1@reader01.singnet.com.sg> <9PKO$z7eflB@jpberlin-l.willms.jpberlin.de>`

```
Lueko Willms wrote:
> .    On  23.01.05
>  wrote  leng1@bigfoot.com (Rick)
…[91 more quoted lines elided]…
>    STOP RUN

The above code will inspire a beginner to take up hog farming.

How about:

Open INPUT Input-file.
READ Input-File.
PERFORM until Input-FS not = '00'
  IF File-1-Input-Date ....
  ....
  END-IF
  IF File-1-Input-Date...
  ...
  END-IF
  If File-1-Input-Date...
  ...
  END-IF
  Read Input-file
  END-PERFORM

CLOSE Input-File OutputA-File OutputB-File.

No compound IFs or qualified data names.
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

_(reply depth: 5)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-23T09:31:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9PORNwpuflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <9PKO$z7eflB@jpberlin-l.willms.jpberlin.de> <10v63v947i6g071@news.supernews.com>`

```
.    On  22.01.05
  wrote  nospam@bisusa.com (JerryMouse)
     on  /COMP/LANG/COBOL
     in  10v63v947i6g071@news.supernews.com
  about  Re: Cobol (Coding problem)


n> The above code will inspire a beginner to take up hog farming.

   which can be a rewarding job, and which requires the ability to  
attend a lot of detail, the overall look at the herd, the detailed  
look at the individual animals, taking care of input and output, and  
this all at the same time.

   Writing a program to process a sequence of data items is child play  
compared to that.


n>
n> How about:
n>
n> Open INPUT Input-file.

   where are the two output files?

n> READ Input-File.
n> PERFORM until Input-FS not = '00'

   a minor status not equal to zero can accompany the major status of  
zero, indicating SUCCESSFUL COMPLETION. Therefore I only use the major  
status. The data names for the various conditions do come, of course,  
from a COPY element.

n>   IF File-1-Input-Date ....
n>   ....
n>   END-IF
n>   IF File-1-Input-Date...
n>   ...
n>   END-IF
n>   If File-1-Input-Date...
n>   ...
n>   END-IF

   Why three consecutive conditional executions? Is that just a lapse  
of cut-and-paste, or a generalisation, or deliberate?
   There is only one choice (as far as Rick has told us to solve his  
problem).

n>   Read Input-file
n>   END-PERFORM
n>
n> CLOSE Input-File OutputA-File OutputB-File.


n> No compound IFs or qualified data names.


   I have just filled my template for sequential processing with the  
details of Rick's question.

   The rest is the same for every processing of sequentially accessed  
data items of unknown quantity.

   It allows the input file being OPTIONAL, and then not present:
      (which is not necessary in all cases, but for my simplicity,
      I maintain only one template; also non-presence of the file
      is a frequent error, which is reported in a 'soft' way
      by the program itself instead of a crash by the OS);
   it allows the input file to be empty, and tells the user about it,
      making a difference between some processing error
      and an empty file;
   it cares about output files only when there is input
      to be processed, avoiding useless work
   it is simple :-)


   Also I assume the same data description for the input file and the  
two output files which it is split into, so the data items have to be  
qualified, to make it simple, and the code to be understood without  
any research in other parts of the program or external documentation.

   Do we want to start another outgrowth of a thread on a concrete  
question to a generalist debate about programming principles?


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Es regnete so stark, daï¿½ alle Schweine rein und alle Menschen dreckig  
wurden. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

_(reply depth: 6)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2005-01-23T22:26:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10v8u702s8mlcde@news.supernews.com>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <9PKO$z7eflB@jpberlin-l.willms.jpberlin.de> <10v63v947i6g071@news.supernews.com> <9PORNwpuflB@jpberlin-l.willms.jpberlin.de>`

```
Lueko Willms wrote:
> .    On  22.01.05
>  wrote  nospam@bisusa.com (JerryMouse)
…[21 more quoted lines elided]…
>   where are the two output files?

Output is left to the user.

>
> n> READ Input-File.
…[5 more quoted lines elided]…
> from a COPY element.

Yes it can. I, however, in over thirty years have never seen it Neither will 
a beginner with a single input file that's simply trying to split the file. 
There is no reason to comple a beginner to fuss with a COPY statement.

>
> n>   IF File-1-Input-Date ....
…[10 more quoted lines elided]…
> of cut-and-paste, or a generalisation, or deliberate?

It is deliberate in the sense that it avoids a compound IF.

>   There is only one choice (as far as Rick has told us to solve his
> problem).
…[11 more quoted lines elided]…
> details of Rick's question.

Rick doesn't have a template. Rick doesn't want a template. Rick may not 
even know what a template is. Nor do I. Exactly.

>
>   The rest is the same for every processing of sequentially accessed
…[12 more quoted lines elided]…
>   it is simple :-)

It is not simple. It is convoluted, complex, and over-kill. It is the worst 
of all worlds for a beginner. He's GOT the file; it can never be missing. 
Likewise, this one-off program does NOT have an empty file. There's two 
unnecessary excursions right there.

>
>
…[3 more quoted lines elided]…
> any research in other parts of the program or external documentation.

Where'd you get the idea that qualified data names are simple? In this 
example, since the ouput files never reference their data fields, why should 
the input file's data names be qualified other than to feed the construct 
forced by using a standardized "template?"
>
>   Do we want to start another outgrowth of a thread on a concrete
> question to a generalist debate about programming principles?

Uh, isn't that what you did?
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

_(reply depth: 7)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2005-01-24T10:25:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41F5217B.39272D4D@mb.sympatico.ca>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <9PKO$z7eflB@jpberlin-l.willms.jpberlin.de> <10v63v947i6g071@news.supernews.com> <9PORNwpuflB@jpberlin-l.willms.jpberlin.de> <10v8u702s8mlcde@news.supernews.com>`

```
JerryMouse wrote:
> 
> 
…[4 more quoted lines elided]…
> 
  

Correction:  "There's" is short for "There is".  So you're saying "There
is two unnecessary ...".

This causes me extreme anguish!

PL
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-01-24T09:42:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ct3c0e$10lk$1@si05.rsvl.unisys.com>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <9PKO$z7eflB@jpberlin-l.willms.jpberlin.de> <10v63v947i6g071@news.supernews.com> <9PORNwpuflB@jpberlin-l.willms.jpberlin.de> <10v8u702s8mlcde@news.supernews.com> <41F5217B.39272D4D@mb.sympatico.ca>`

```
Well, since we seem to be into criticisms of the English grammar of others,
I would have to make the argument that "There's" points back to the previous
text (singular).  He could equally reasonably have written "That's" (which
would probably have been my preference). How many places can one (verbal)
index finger point at a given instant?        ;-)

As my sainted mother used to say:  Never try to teach your grandmother how
to milk ducks ...

    -Chuck Stevens


"Peter Lacey" <lacey@mb.sympatico.ca> wrote in message
news:41F5217B.39272D4D@mb.sympatico.ca...
> JerryMouse wrote:
> >
> >
> > It is not simple. It is convoluted, complex, and over-kill. It is the
worst
> > of all worlds for a beginner. He's GOT the file; it can never be
missing.
> > Likewise, this one-off program does NOT have an empty file. There's two
> > unnecessary excursions right there.
…[8 more quoted lines elided]…
> PL
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-01-24T18:31:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ct3f0n$b4k$1@peabody.colorado.edu>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <9PKO$z7eflB@jpberlin-l.willms.jpberlin.de> <10v63v947i6g071@news.supernews.com> <9PORNwpuflB@jpberlin-l.willms.jpberlin.de> <10v8u702s8mlcde@news.supernews.com> <41F5217B.39272D4D@mb.sympatico.ca> <ct3c0e$10lk$1@si05.rsvl.unisys.com>`

```

On 24-Jan-2005, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> Well, since we seem to be into criticisms of the English grammar of others,
> I would have to make the argument that "There's" points back to the previous
> text (singular).  He could equally reasonably have written "That's" (which
> would probably have been my preference). How many places can one (verbal)
> index finger point at a given instant?        ;-)

I disagree.   It still means "There is two unnecessary excursions right there".
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-01-24T11:55:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ct3jq1$15rf$1@si05.rsvl.unisys.com>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <9PKO$z7eflB@jpberlin-l.willms.jpberlin.de> <10v63v947i6g071@news.supernews.com> <9PORNwpuflB@jpberlin-l.willms.jpberlin.de> <10v8u702s8mlcde@news.supernews.com> <41F5217B.39272D4D@mb.sympatico.ca> <ct3c0e$10lk$1@si05.rsvl.unisys.com> <ct3f0n$b4k$1@peabody.colorado.edu>`

```
I think it could also be a legitimate transformation of
    [Up] there is [an illustration of] two unnecessary excursions [, ] right
there.

I would personally have preferred
    That is [an illustration of] two unnecessary excursions [, ] right
there.

but I think Chomsky would have recognized the transforms that could be used
to lead to the first.

    -Chuck Stevens


"Howard Brazee" <howard@brazee.net> wrote in message
news:ct3f0n$b4k$1@peabody.colorado.edu...
>
> On 24-Jan-2005, "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
> > Well, since we seem to be into criticisms of the English grammar of
others,
> > I would have to make the argument that "There's" points back to the
previous
> > text (singular).  He could equally reasonably have written "That's"
(which
> > would probably have been my preference). How many places can one
(verbal)
> > index finger point at a given instant?        ;-)
>
> I disagree.   It still means "There is two unnecessary excursions right
there".
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

_(reply depth: 7)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-24T17:01:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9PSc57keflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <9PORNwpuflB@jpberlin-l.willms.jpberlin.de> <10v8u702s8mlcde@news.supernews.com>`

```
.    On  23.01.05
  wrote  nospam@bisusa.com (JerryMouse)
     on  /COMP/LANG/COBOL
     in  10v8u702s8mlcde@news.supernews.com
  about  Re: Cobol (Coding problem)

  on my template for processing sequences of objects serially:

n> It is not simple. It is convoluted, complex, and over-kill.

  it is appropriate to the task, and really simple. One can overlook  
it  easily since it will not strech beyond a page, neither printed nor  
displayed on screen (OK, not the Epson PX-8 I once had, with only 8  
lines).

n> It is the worst of all worlds for a beginner.

   Rick X. did not state that he is a beginner. How do you know?

   And even if he is, shouldn't a beginner begin with correct  
programs?

   I think he just got entangled in a specification which led him  
astray, not seeing the wood for the trees (as far as I can see based  
on the way he presented his problem).

n> He's GOT the file; it can never be missing.

   But maybe the program doesn't find it? Or the next cycle of  
execution fails to produce the output which should be the input-file  
for this step?


n> Likewise, this one-off program does NOT have an empty file.

   How do you know that this is a "one-off program"?

n> There's two unnecessary excursions right there.

   I am talking about safeguards against potential hazards.

>>   Also I assume the same data description for the input file and the
>> two output files which it is split into, so the data items have to be
>> qualified, to make it simple, and the code to be understood without
>> any research in other parts of the program or external documentation.

n> Where'd you get the idea that qualified data names are simple?

   In my experience. The qualification tells the reader right away  
what the program is talking about and dealing with: With items in the  
input-file-record.

n> In this example, since the ouput files never reference their data
n> fields,

   How do you know that?


n> why should the input file's data names be qualified other than to
n> feed the construct forced by using a standardized "template?"

   The qualification does not flow from the template, but from the  
ease of documentation, and avoiding separate and therefore potentially  
conflicting descriptions for the three files.

   If your assumption is correct, and the compiler allows it, the  
output file(s) could be declared with a record of ANY size, or  
something like that. But I don't know, and I do not want to act too  
much on assumptions which may be wrong.

>>   Do we want to start another outgrowth of a thread on a concrete
>> question to a generalist debate about programming principles?

n> Uh, isn't that what you did?

    Only if there are takes. :-))

    Besides, I think that would be more appropriate for this  
newsgroup, than the talk about political issues. In the past weeks, I  
sometimes asked myself if COBOL is still on-topic here.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Gerade das Gegenteil tun heiï¿½t auch nachahmen, es heiï¿½t nï¿½mlich das  
Gegenteil nachahmen. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-01-24T09:51:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106589072.619700.103620@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<10v8u702s8mlcde@news.supernews.com>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <9PKO$z7eflB@jpberlin-l.willms.jpberlin.de> <10v63v947i6g071@news.supernews.com> <9PORNwpuflB@jpberlin-l.willms.jpberlin.de> <10v8u702s8mlcde@news.supernews.com>`

```
> He's GOT the file; it can never be missing.

What if he has mis-specified the file name ?  The file might be _there_
but he looks for it _here_.

> Likewise, this one-off program does NOT have an empty file.

Idioms are designed to cater for boundary conditions, such as empty
files.  It is important to teach beginners idioms which work rather
than dismissing problems which may occur.
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

_(reply depth: 4)_

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-01-23T14:03:12+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<csvc3f$et5$1@reader01.singnet.com.sg>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <9PKJzgN9flB@jpberlin-l.willms.jpberlin.de> <cstuvh$afc$1@reader01.singnet.com.sg> <9PKO$z7eflB@jpberlin-l.willms.jpberlin.de>`

```
Tks Lueko Willms for your advise :-)  I will go try it out and hopefully it 
will help resolve my issue :-)
Will updates through this newsgroup again.
As I also have to cater other conditions beside this in the pgm, hope 
everything go well.
As the records does not have indicator field to determine where the record 
should o/p to,
it's based on "record pattern" in the input file to determine, hence not so 
straight forward at times :-(


 <l.willms@jpberlin.de> wrote in message 
news:9PKO$z7eflB@jpberlin-l.willms.jpberlin.de...
>.    On  23.01.05
>  wrote  leng1@bigfoot.com (Rick)
…[109 more quoted lines elided]…
> pflegen. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

_(reply depth: 5)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-23T08:41:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9PORMmG9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <9PKO$z7eflB@jpberlin-l.willms.jpberlin.de> <csvc3f$et5$1@reader01.singnet.com.sg>`

```
.    On  23.01.05
  wrote  leng1@bigfoot.com (Rick)
     on  /COMP/LANG/COBOL
     in  csvc3f$et5$1@reader01.singnet.com.sg
  about  Re: Cobol (Coding problem)


l> As I also have to cater other conditions beside this in the pgm, hope
l> everything go well.

   Sure, I could only respond to the questions you asked. Good luck  
with the rest. How long have you been working in COBOL, and do you  
other tasks besides programming in COBOL?

l> As the records does not have indicator field to determine where the
l> record should o/p to, it's based on "record pattern" in the input
l> file to determine, hence not so straight forward at times :-(

   Well, you have described a clear cut, quite simple condition based  
on three data items, which can comfortably be described in one  
conditional expression.

   'Pattern matching' suggests something else; this is meant normally  
to search for patterns in one single string of text, not fixed fields  
which can be identified easily by their names.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Er liebte hauptsï¿½chlich die Wï¿½rter, die nicht in Wï¿½rterbï¿½chern vorzukommen pflegen. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

_(reply depth: 4)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2005-01-25T11:05:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9PWg-QTPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <cstuvh$afc$1@reader01.singnet.com.sg> <9PKO$z7eflB@jpberlin-l.willms.jpberlin.de>`

```
.    On  22.01.05
  wrote  L.Willms@JPBERLIN.de (Lueko Willms)
     on  /COMP/LANG/COBOL
     in  9PKO$z7eflB@jpberlin-l.willms.jpberlin.de
  about  Re: Cobol (Coding problem)

   A caveat to my proposal:

LW>       MOVE FUNCTION(CURRENT-DATE) TO My-Current-Date

   this can be a problem in this decision:

LW>           IF Version OF input-file-record = '00'
LW>             AND date-1 OF input-file-record NOT = My-Current-Date
LW>             AND date-2 OF input-file-record = My-Current-Date


   since FUNCTION(CURRENT-DATE) does return not only the date, but  
also the time of day in one structure, and the time of day will quite  
certainly not match the value given in the input-file. It does  
probably only carry a calendar date.

   So either My-Current-Date has to be a 8-character field, truncating  
the result of FUNCTION(CURRENT-DATE) to the date only, or one has to  
use  ACCEPT My-Current-Date FROM DATE or do possibly shuffle the year,  
month, and day parts, so that it corresponds to the form the date is  
represented in the file.

   Sorry about any confusion my proposal may have caused in this  
point.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Nach einem dreiï¿½igjï¿½hrigen Krieg mit sich selbst kam es endlich zu einem Vergleich, aber die Zeit war verloren. -G.C.Lichtenberg
```

#### ↳ Re: Cobol (Coding problem)

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-01-22T22:51:13+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35em0jF4in9cvU1@individual.net>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg>`

```

"Rick" <leng1@bigfoot.com> wrote in message
news:cssq0a$95o$1@reader01.singnet.com.sg...
> Hi,
> I have got some coding problem and appreciate someone could help advise
…[13 more quoted lines elided]…
>

I assume that if there is only 1 record with version 00, and date 1 field is
non-current, and date 2 field is also non-current,
then it goes to file A, right?
>
> Scenario(2)
…[14 more quoted lines elided]…
>    xxx xxx xxx   00    non-current date   current date     => o/p to
file(B)
>    xxx xxx xxx   01    current date       current date     => o/p to
file(A)
>    xxx xxx xxx   02    current date       non-current date => o/p to
file(A)
>
>
…[20 more quoted lines elided]…
> something, but if you had ver00 or version01,02,etc, all these are
consider
> not
> = spaces.They are suppose to perform different things for version that is
…[3 more quoted lines elided]…
>

It is an interesting problem, Rick and you have stated it well.

There are a number of red herrings and you were wise to build truth tables.

Ignoring what is not important, I believe the following should do it (unless
there are other conditions you haven't mentioned.)


WS

01  date-1-flag            pic x  value zero.
      88 date-1-current  value '1'.

01  date-2-flag            pic x  value zero.
      88 date-2-current  value '1'.

01  today.
      12 today-yyyy pic x(4).
      12 today-mm  pic xx.
      12 today-dd    pic xx.

PD
....
* set up the today field once in initialization, unless you are likely to
run
* this process overnight and date could change at midnight.
*
* If your compiler supports functions use function (CURRENT-DATE) otherwise
* you may need to accept TODAYS-DATE... check your COBOL manual to see what
works for you.
I
        move function (CURRENT-DATE) to today   *> may need some fiddling to
ensure formats match


*Apply the following code to ALL records in each key group as each record is
fetched...

*You might want to detect a group change for other reasons, but you don't
need to on the basis of what you told us.

        move zero to date-1-flag date-2-flag
        if date-1-field  = today
           set date-1-current  to TRUE
        end-if
        if date-2-field = today
           set date-2-current  to TRUE
        end-if
        if version = '00'
                    AND
            NOT date-1-current
                    AND
            date-2-current
                   output to file B
        else
            output to file A
        end-if

etc.

HTH,

Pete.
```

##### ↳ ↳ Re: Cobol (Coding problem)

- **From:** "Rick" <leng1@bigfoot.com>
- **Date:** 2005-01-23T01:24:48+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cstvlh$aft$1@reader01.singnet.com.sg>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <35em0jF4in9cvU1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:35em0jF4in9cvU1@individual.net...
>
> "Rick" <leng1@bigfoot.com> wrote in message
…[21 more quoted lines elided]…
> then it goes to file A, right?
===> No, basically, it will be ignored for these record. For only 1 record
          with version00, date2 field must be current date, then o/p to 
file(B).
          This is to ensure that I pick current day record but I need to
          determine base on the 2 date field to o/p to which file


>>
>> Scenario(2)
…[115 more quoted lines elided]…
> etc.
===> Hi, does the above code o/p for the rest of the version (for 
ver01,02,03 etc) of the same group
          to file(A).As I do not know how many version there will be, 
basically so long for version00
          and date2 field is current date, then o/p to file(B), all 
subsequent version (01,02,03 etc)
          of the same group, will need to o/p to file(A) so long date(1) 
field is current date.Guess, have to use
          "PERFORM... UNTIL" but not sure how to code. Can help ??
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2005-01-22T16:14:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106439268.461247.293200@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<cstvlh$aft$1@reader01.singnet.com.sg>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <35em0jF4in9cvU1@individual.net> <cstvlh$aft$1@reader01.singnet.com.sg>`

```
Hi Rick,

If I read your specs correctly, this pseudo code should work:
(Don't forget the Os and Cs)

W/S.
01  NEW-REC.
05 NEW-etc ...

01  PREV-REC.
05 PREV-etc ...

01  GRP-FIN-SW      PIC X VALUE 'R'.
88 RESET-GRP-FIN-SW   VALUE 'R'.
88 GRP-IS-FINISHED    VALUE 'F'.


PROC DIV.
Get the today's date
PERF READ-IP-REC
PERF PROCESS-GROUPS UNTIL EOF
STOP RUN
.
PROCESS-GROUPS.
You can add some statistical stuff here.
SET RESET-GRP-FIN-SW TO TRUE
PERF PROCESS-RECS UNTIL GRP-IS-FINISHED
You can add some statistical stuff here.
.
PROCESS-RECS.
EVAL NEW-VERNO
WHEN 0
IF NEW-DATE-1     = TODAYS-DATE
AND
NEW-DATE-2 NOT = TODAYS-DATE
WRITE FILE-B-REC FROM NEW-REC
END-IF
WHEN OTHER
IF NEW-DATE-1     = TODAYS-DATE
WRITE FILE-A-REC FROM NEW-REC
END-IF
END-EVAL
PERF READ-IP-REC
You can add some statistical stuff here too.
.
READ-IP-REC.
MOVE NEW-REC  TO PREV-REC
READ IP-REC INTO NEW-REC AT END
SET EOF  TO TRUE
END-READ
IF NEW-GROUP NOT = PREV-GROUP
SET GRP-IS-FINISHED TO TRUE
   END-IF
   .
```

###### ↳ ↳ ↳ Re: Cobol (Coding problem)

_(reply depth: 4)_

- **From:** "slade2" <jacksleight@hotmail.com>
- **Date:** 2005-01-22T16:26:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1106440014.561531.17850@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1106439268.461247.293200@c13g2000cwb.googlegroups.com>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg> <35em0jF4in9cvU1@individual.net> <cstvlh$aft$1@reader01.singnet.com.sg> <1106439268.461247.293200@c13g2000cwb.googlegroups.com>`

```
I knew I needed something else in that "AT END" clause.  Add this SET
stmt:

SET GRP-IS-FINISHED TO TRUE

Jack
```

#### ↳ Re: Cobol (Coding problem)

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-23T06:13:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e6v05qlarv8ja6red3ploe76ucpva2gm@4ax.com>`
- **References:** `<cssq0a$95o$1@reader01.singnet.com.sg>`

```
On Sat, 22 Jan 2005 14:42:01 +0800, "Rick" <leng1@bigfoot.com> wrote:

>Hi,
>I have got some coding problem and appreciate someone could help advise
…[12 more quoted lines elided]…
>file(B)

perform open-files   *> primes input with first record
perform until end-of-input
    evaluate verno also date1 also date2
        when '00'  also not = current-date also current-date
            perform write-to-b
    end-evaluate
    perform read-input
end-perform
perform close-files
stop run.

>Scenario(2)
>============
…[17 more quoted lines elided]…
>(P/S: For o/p to file(B), only allow for version 00 records only)

"Date(2) field is current or non-current" is always true. 

perform open-files   *> primes input with first record
perform until end-of-input
    evaluate verno also date1 also date2
        when '00'  also not = current-date also current-date
            perform write-to-b
        when other also current-date also any
            perform write-to-a
    end-evaluate
    perform read-input
end-perform
perform close-files
stop run.

>I have some coding and towards the end, I coded like
>
…[5 more quoted lines elided]…
>end-if

The problem does not require testing group change.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
