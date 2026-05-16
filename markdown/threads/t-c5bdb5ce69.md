[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# abortive exiting

_42 messages · 8 participants · 2006-05_

---

### abortive exiting

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-15T13:11:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4cs23aF17bpukU1@individual.net>`

```
New obsession....

With the following program, compiled using COBOL for VSE 1.1.1, I get the
following warnings:

PP 5686-068 IBM COBOL FOR VSE/ESA 1.1.1                        FSTEST   
DATE 05/15/2006  TIME 13:04:25   PAGE    12                
                                                                            
                                                       
LINEID  MESSAGE CODE  MESSAGE TEXT                                          
                                                       
                                                                            
                                                       
    31  IGYOP3094-W   THERE MAY BE A LOOP FROM THE "PERFORM" STATEMENT AT
"PERFORM (LINE 31.01)" TO ITSELF.  "PERFORM" STATEMENT    
                      OPTIMIZATION WAS NOT ATTEMPTED.                       
                                                       
                                                                            
                                                       
    32  IGYOP3094-W   THERE MAY BE A LOOP FROM THE "PERFORM" STATEMENT AT
"PERFORM (LINE 32.01)" TO ITSELF.  "PERFORM" STATEMENT    
                      OPTIMIZATION WAS NOT ATTEMPTED.                       
                                                       
                                                                            
                                                       
    35  IGYOP3094-W   THERE MAY BE A LOOP FROM THE "PERFORM" STATEMENT AT
"PERFORM (LINE 35.01)" TO ITSELF.  "PERFORM" STATEMENT    
                      OPTIMIZATION WAS NOT ATTEMPTED.                       
                                                       

000001 ID DIVISION.
000002 PROGRAM-ID. FSTEST.
000003 ENVIRONMENT DIVISION.
000004 INPUT-OUTPUT SECTION.
000005 FILE-CONTROL.
000006     SELECT MY-FILE
000007       ACCESS SEQUENTIAL
000008       FILE STATUS FILE-STATUS
000009       ASSIGN TO MYFILE.
000010 DATA DIVISION.
000011 FILE SECTION.
000012 FD  MY-FILE
000013     RECORDING MODE F.
000014 01  MY-RECORD                   PIC X(80).
000015 WORKING-STORAGE SECTION.
000016 01  FILE-STATUS.
000017     88  FILE-AT-END                 VALUE '10'.
000018     05                          PIC X.
000019         88  FILE-SUCCESSFUL         VALUE '0'.
000020     05                          PIC X.
000021
000022 LINKAGE SECTION.
000023 01  FIELD-1  PIC X(80).
000024 PROCEDURE DIVISION USING FIELD-1.
000025 MAINLINE SECTION.
000026     PERFORM NESTED1
000027     EXIT PROGRAM.
000028
000029 NESTED1 SECTION.
000030     DISPLAY FIELD-1
000031     PERFORM OPEN-FILE
000032     PERFORM READ-RECORD
000033     PERFORM UNTIL FILE-AT-END
000034         PERFORM HANDLE-RECORD
000035         PERFORM READ-RECORD
000036     END-PERFORM
000037     PERFORM CLOSE-FILE
000038     GO TO NESTED1-EXIT.
000039
000040 HANDLE-RECORD.
000041     DISPLAY MY-RECORD
000042     .
000043
000044 OPEN-FILE.
000045     OPEN INPUT MY-FILE
000046     IF NOT FILE-SUCCESSFUL
000047         DISPLAY 'ERROR OPENING MYFILE, STATUS: ' FILE-STATUS
000048           UPON CONSOLE
000049         GO TO NESTED1-EXIT
000050     END-IF
000051     .
000052
000053 READ-RECORD.
000054     READ MY-FILE
000055     IF NOT FILE-SUCCESSFUL
000056         DISPLAY 'ERROR READING MYFILE, STATUS: ' FILE-STATUS
000057           UPON CONSOLE
000058         GO TO NESTED1-EXIT
000059     END-IF
000060     .
000061
000062 CLOSE-FILE.
000063     CLOSE MY-FILE
000064     .
000065
000066 NESTED1-EXIT. EXIT.
000067
000068 END PROGRAM FSTEST.

I'm probably just missing something totally obvious, but just exactly what
code is causing these warnings?  If I get rid of the GO TOs in OPEN-FILE and
READ-RECORD then the warnings go away, but of course the program does not
function as intended.

Please no comments about how the program should be recoded using flags and
other things.  This is just a trivial program solely intended to illustrate
the issue at hand.  I, in fact, discovered it when using a nested program
and using "EXIT PROGRAM" instead of the "GO TO"s.  I had thought it had
something to do with my use of nested programs, but that does not appear to
be the case.

Any thoughts?  Oh, and it does go away if I use NOOPT instead of OPT, for
the obvious reason...

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

#### ↳ Re: abortive exiting

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-05-15T20:39:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<relh62pt7nslhvcdlgnqb910fco6mggqgb@4ax.com>`
- **References:** `<4cs23aF17bpukU1@individual.net>`

```
On Mon, 15 May 2006 13:11:35 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>New obsession....
>
…[100 more quoted lines elided]…
>Frank
Bad coding is the only thing I can think of when I see this type of
coding. But this is only my personal opinion.


The following will probably not issue the error.
       NESTED1 SECTION.
       NESTED1-START.               *> ALWAYS CODE PARAGRAPHS names.
           DISPLAY FIELD-1
           PERFORM OPEN-FILE
           IF NOT FILE-SUCCESSFUL
               GO TO NESTED1-EXIT
           END-IF
           PERFORM READ-RECORD
           PERFORM UNTIL FILE-AT-END
                OR NOT FILE-SUCESSEFUL  *> new code
               PERFORM HANDLE-RECORD
               PERFORM READ-RECORD
           END-PERFORM
           PERFORM CLOSE-FILE
           GO TO NESTED1-EXIT.
      
       HANDLE-RECORD.   *> Even this paragraph should be moved to
                        *> a section of its own.
                        *> I am almost sure that if you add a .
                        *> "GO TO NESTED1-EXIT" here that the warning
                        *> will occur also.
           DISPLAY MY-RECORD
           .
      
       CLOSE-FILE.      *> Same here as above.
           CLOSE MY-FILE
           .
      
       NESTED1-EXIT. EXIT.


      *> Moved code to sections.
       OPEN-FILE SECTION.
       OPEN-FILE-START.
           OPEN INPUT MY-FILE
           IF NOT FILE-SUCCESSFUL
               DISPLAY 'ERROR OPENING MYFILE, STATUS: ' FILE-STATUS
                 UPON CONSOLE
             *> Eventually here go to a exit program section.
           END-IF
           .
       OPEN-FILE-EXIT.
           EXIT.
      
       READ-RECORD SECTION.
       READ-RECORD-START.
           READ MY-FILE
           IF NOT FILE-SUCCESSFUL
               DISPLAY 'ERROR READING MYFILE, STATUS: ' FILE-STATUS
                 UPON CONSOLE
             *> Eventually here go to a exit program section.
           END-IF
           .
       READ-RECORD-EXIt.
           EXIT.
      


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: abortive exiting

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-15T14:03:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147726984.177002.214700@y43g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<4cs23aF17bpukU1@individual.net>`
- **References:** `<4cs23aF17bpukU1@individual.net>`

```
> If I get rid of the GO TOs in OPEN-FILE and
> READ-RECORD then the warnings go away, but of course the program
> does not function as intended.

It seems to me that it does not 'function as intended' at the moment.

I would suggest that you do not mix the performing of sections with the
performing of paragraphs. Choose one and stick to it. You may like to
consider that the _only_ reason for performing sections that have
several paragraph names (or perform thru) is to cater for gotos.

> 000032     PERFORM READ-RECORD
> 000033     PERFORM UNTIL FILE-AT-END
…[3 more quoted lines elided]…
> 000037     PERFORM CLOSE-FILE

This perform does not terminate.  Instead you are bypassing the close
by jumping straight out of the read when the '10' status occurs.

> 000053 READ-RECORD.
> 000054     READ MY-FILE
                     IF File-At-End
                           CONTINUE
                     ELSE
> 000055     IF NOT FILE-SUCCESSFUL
> 000056         DISPLAY 'ERROR READING MYFILE, STATUS: ' > FILE-STATUS
> 000057           UPON CONSOLE
> 000058         GO TO NESTED1-EXIT
> 000059     END-IF
                     END-IF
> 000060     .
```

#### ↳ Re: abortive exiting

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-15T15:03:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147730631.407547.23210@j33g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<4cs23aF17bpukU1@individual.net>`
- **References:** `<4cs23aF17bpukU1@individual.net>`

```


       IDENTIFICATION DIVISION.
       PROGRAM-ID. FSTEST.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT MY-FILE
               ACCESS SEQUENTIAL
               FILE STATUS FILE-STATUS
               ASSIGN TO MYFILE.
       DATA DIVISION.
       FILE SECTION.
       FD  MY-FILE
           RECORDING MODE F.
       01  MY-RECORD                   PIC X(80).
       WORKING-STORAGE SECTION.
       01  FILE-STATUS.
           88  FILE-AT-END                 VALUE '10'.
           05                          PIC X.
               88  FILE-SUCCESSFUL         VALUE '0'.
           05                          PIC X.

       LINKAGE SECTION.
       01  FIELD-1  PIC X(80).
       PROCEDURE DIVISION USING FIELD-1.
       MAINLINE.
           PERFORM Process-File
           EXIT PROGRAM.

       Process-File.
           DISPLAY FIELD-1
           OPEN INPUT MY-FILE
           IF ( NOT File-Successful )
               DISPLAY 'ERROR OPENING MYFILE, STATUS: ' FILE-STATUS
                             UPON CONSOLE
           ELSE
                    PERFORM READ-RECORD
                    PERFORM UNTIL NOT File-Successful
                        PERFORM HANDLE-RECORD
                        PERFORM READ-RECORD
                    END-PERFORM
                    CLOSE My-File
       END-IF

       HANDLE-RECORD.
           DISPLAY MY-RECORD
           .
      READ-RECORD.
           READ MY-FILE
               AT END
                       CONTINUE
               NOT AT END
               IF NOT FILE-SUCCESSFUL
                   DISPLAY 'ERROR READING MYFILE, STATUS: ' FILE-STATUS
                                  UPON CONSOLE
               END-IF
           END-READ
            .
       END PROGRAM FSTEST.
```

#### ↳ Re: abortive exiting

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-15T18:20:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4csk72F17mlq3U1@individual.net>`
- **References:** `<4cs23aF17bpukU1@individual.net>`

```
I guess I didn't make myself clear.  I'm not looking for a solution, per se.
 I can think of several other ways to get the job done.  I'm simply not
happy with them, for various reasons.
All I really want to know, at this point, is why am I getting this warning.

Anyway, take a look at the following.  This is more like what caused me to
bring up the issue.  I removed the "EXIT PROGRAM" logic from the subordinate
paragraphs and added additional checking to after the perform of OPEN-FILE. 
But I don't like it.  It clutters up the main logic of the program.  If
there is an exceptional condition, one that generally should not occur, I
don't like to have to put code all over the place to recover from it.  So my
thought here was I could use EXIT PROGRAM to immediately quit out of NESTED1
and then, in the main program, I could check for RETURN-CODE > ZERO and exit
after the call, if necessary.  (Not shown here...)   Even that I'm not fond
of, but at least its just in one place.

And yes, it's quite possible that I am just being stubborn!

000001 ID DIVISION.                                   
000002 PROGRAM-ID. OUTERPGM.                          
000003 ENVIRONMENT DIVISION.                          
000004 INPUT-OUTPUT SECTION.                          
000005 FILE-CONTROL.                                  
000006     SELECT MY-FILE                             
000007       ACCESS SEQUENTIAL                        
000008       FILE STATUS FILE-STATUS                  
000009       ASSIGN TO MYFILE.                        
000010 DATA DIVISION.                                 
000011 FILE SECTION.                                  
000012 FD  MY-FILE                     IS GLOBAL      
000013     RECORDING MODE F.                          
000014 01  MY-RECORD                   PIC X(80).     
000015 WORKING-STORAGE SECTION.                       
000016 01  FILE-STATUS                 IS GLOBAL.     
000017     88  FILE-AT-END                 VALUE '10'.
000018     05                          PIC X.         
000019         88  FILE-SUCCESSFUL         VALUE '0'. 
000020     05                          PIC X.         
000021                                                
000022 LINKAGE SECTION.                               
000023 01  FIELD-1  PIC X(80) GLOBAL.          
000024 PROCEDURE DIVISION USING FIELD-1.       
000025     CALL 'NESTED1'                      
000026     EXIT PROGRAM.                       
000027                                         
000028 ID DIVISION.                            
000029 PROGRAM-ID. 'NESTED1'.                  
000030 PROCEDURE DIVISION.                     
000031     MOVE ZERO TO RETURN-CODE            
000032     DISPLAY FIELD-1                     
000033     PERFORM OPEN-FILE                   
000034     IF RETURN-CODE > ZERO               
000035         EXIT PROGRAM                    
000036     END-IF                              
000037     PERFORM READ-RECORD                 
000038     PERFORM UNTIL NOT FILE-SUCCESSFUL   
000039         PERFORM HANDLE-RECORD           
000040         PERFORM READ-RECORD             
000041     END-PERFORM                         
000042     PERFORM CLOSE-FILE                  
000043     EXIT PROGRAM.                       
000044                                         
000045 HANDLE-RECORD.                                              
000046     DISPLAY MY-RECORD                                       
000047     .                                                       
000048                                                             
000049 OPEN-FILE.                                                  
000050     OPEN INPUT MY-FILE                                      
000051     IF NOT FILE-SUCCESSFUL                                  
000052         DISPLAY 'ERROR OPENING MYFILE, STATUS: ' FILE-STATUS
000053           UPON CONSOLE                                      
000054         MOVE 16 TO RETURN-CODE                              
000055     END-IF                                                  
000056     .                                                       
000057                                                             
000058 READ-RECORD.                                                
000059     READ MY-FILE                                            
000060     IF FILE-SUCCESSFUL OR FILE-AT-END                       
000061         CONTINUE                                            
000062     ELSE                                                    
000063         DISPLAY 'ERROR READING MYFILE, STATUS: ' FILE-STATUS
000064           UPON CONSOLE                                      
000065         MOVE 16 TO RETURN-CODE                              
000066     END-IF                                                  
000067     .                 
000068                       
000069 CLOSE-FILE.           
000070     CLOSE MY-FILE     
000071     .                 
000072                       
000073 END PROGRAM 'NESTED1'.
000074                       
000075 END PROGRAM OUTERPGM. 

Oh, and FWIW, none of this code has actually been run.  I have only compiled
it just to see when I get the warning and when I don't.


Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

##### ↳ ↳ Re: abortive exiting

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-15T19:03:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147745025.262982.91960@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<4csk72F17mlq3U1@individual.net>`
- **References:** `<4cs23aF17bpukU1@individual.net> <4csk72F17mlq3U1@individual.net>`

```
> All I really want to know, at this point, is why am I getting this warning.

The warning is that the optimization is not being done because there is
a goto within the scope of the perform.  It does not analyse the code
sufficiently to know whether or not the gotos would affect the
optimizer, it just doesn't optimize.  To get rid of the warning either
code the program 'better' or use a compiler option to turn off the
optimizer.

BTW, I don't see that the later version as being 'better' for several
reasons, one of which is that it complexifies the problem.  For example
you have introduced several GLOBALs (which are generally considered
bad) in order to use line 35 EXIT PROGRAM when it could be same effect
can be easily done with an ELSE in a paragraph that is performed:

000034     IF RETURN-CODE > ZERO
000035         CONTINUE
000036     ELSE
000037         PERFORM READ-RECORD
000038         PERFORM UNTIL NOT FILE-SUCCESSFUL
000039             PERFORM HANDLE-RECORD
000040             PERFORM READ-RECORD
000041         END-PERFORM
000042         PERFORM CLOSE-FILE
000043     END-IF.
```

###### ↳ ↳ ↳ Re: abortive exiting

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-15T19:20:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147746007.962678.238540@i40g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1147745025.262982.91960@u72g2000cwu.googlegroups.com>`
- **References:** `<4csk72F17mlq3U1@individual.net> <4cs23aF17bpukU1@individual.net> <1147745025.262982.91960@u72g2000cwu.googlegroups.com>`

```

Richard wrote:

> when it could be same effect
> can be easily done with an ELSE in a paragraph that is performed:

Or more easily with:

> 000034     IF File-Successful
> 000037         PERFORM READ-RECORD
…[5 more quoted lines elided]…
> 000043     END-IF.
```

#### ↳ Re: abortive exiting

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-05-16T08:09:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com>`
- **References:** `<4cs23aF17bpukU1@individual.net>`

```
New version of my previous posting.
Without sections or gotos, but with a style of perform I dont like
either, but that is very common also.

       LINKAGE SECTION.
       01  FIELD-1  PIC X(80).
       PROCEDURE DIVISION USING FIELD-1.
       MAINLINE SECTION.       
       NESTED1-START.
           DISPLAY FIELD-1
           PERFORM OPEN-FILE
           PERFORM READ-RECORD
           PERFORM UNTIL FILE-AT-END
               PERFORM HANDLE-RECORD
               PERFORM READ-RECORD
           END-PERFORM
           PERFORM CLOSE-FILE
           .
       EXIT-PROGRAM.
           GOBACK.  *>or exit program if your compiler does 
                    *>not support this
      
       HANDLE-RECORD.
           DISPLAY MY-RECORD
           .
      
       CLOSE-FILE.
           CLOSE MY-FILE
           .
      

      *> Moved code to sections.
       OPEN-FILE
           OPEN INPUT MY-FILE
           IF NOT FILE-SUCCESSFUL
               DISPLAY 'ERROR OPENING MYFILE, STATUS: ' FILE-STATUS
                 UPON CONSOLE
               PERFORM EXIT-PROGRAM
           END-IF
           .
      
       READ-RECORD.
           READ MY-FILE
           IF  NOT FILE-SUCCESSFUL
           AND NOT FILE-AT-END
               DISPLAY 'ERROR READING MYFILE, STATUS: ' FILE-STATUS
                 UPON CONSOLE
               PERFORM EXIT-PROGRAM
           END-IF
           .


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: abortive exiting

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-05-16T08:50:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<126jm4jf05o9jdd@news.supernews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com>`

```
Frederico Fonseca wrote:
> New version of my previous posting.
> Without sections or gotos, but with a style of perform I dont like
…[46 more quoted lines elided]…
>           END-IF

Suggest changing PERFORM EXIT-PROGRAM to Move "Yes" to FILE-AT-END (or 
whatever the flag might be) else the program exits without going through the 
file close routine. The compiler may automatically close the files and 
release locks upon exit, but maybe not.
```

###### ↳ ↳ ↳ Re: abortive exiting

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-16T12:12:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147806753.408990.179740@j33g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<126jm4jf05o9jdd@news.supernews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com>`

```

> Move "Yes" to FILE-AT-END (or whatever the flag might be)

Actually that is not required at all as the READ will set the
File-At-End condition true automatically, which you should have noticed
had you been paying attention.

> The compiler may automatically close the files and
> release locks upon exit, but maybe not.

Actually COBOL specifies exactly when the file will be closed
automatically and when it will not be, so there is no 'maybe' about
this.

But you get a 2 out of 10 for noticing that the program won't go
through the CLOSE when there is a failure on the READ.
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 4)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-05-17T09:58:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<126mef5iqdfm9fc@news.supernews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <1147806753.408990.179740@j33g2000cwa.googlegroups.com>`

```
Richard wrote:
>> Move "Yes" to FILE-AT-END (or whatever the flag might be)
>
> Actually that is not required at all as the READ will set the
> File-At-End condition true automatically, which you should have
> noticed had you been paying attention.

I do pay attention to that which deserves attention. Mostly. Well, at least 
often.

>
>> The compiler may automatically close the files and
…[4 more quoted lines elided]…
> this.

Yes COBOL does. But that doesn't alter the fact that THIS code may or may 
not result in a closed file. COBOL (generally) closes files upon exit of the 
run unit. We have no intimation that this code snippet is a complete run 
unit, therefore, upon exit of this code, the status of the file is 
problematic.

Just so you'll know, and for future reference, COBOL doesn't close files 
(generally) upon exit from a subprogram.

>
> But you get a 2 out of 10 for noticing that the program won't go
> through the CLOSE when there is a failure on the READ.
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-17T12:41:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147894910.042887.291600@j33g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<126mef5iqdfm9fc@news.supernews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <1147806753.408990.179740@j33g2000cwa.googlegroups.com> <126mef5iqdfm9fc@news.supernews.com>`

```

HeyBub wrote:

> >> The compiler may automatically close the files and
> >> release locks upon exit, but maybe not.
…[9 more quoted lines elided]…
> problematic.

It is only problematic, in this case, if the routine is CALLed again
within the same run-unit after it has had a failure on reading.  In
that case the CLOSE had not been done and the OPEN will fail. If the
code is a run unit then COBOL is required to CLOSE the file
automatically when the run unit completes.

> Just so you'll know, and for future reference, COBOL doesn't close files
> (generally) upon exit from a subprogram.

Exactly, there is no 'maybe' about it, COBOL specifies that it does if
there is an implicit CANCEL such as end of run unit or the routine was
explicitly 'IS INITIAL', otherwise not. An explicit CANCEL after the
CALL will do so too.
```

###### ↳ ↳ ↳ Re: abortive exiting

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-05-17T01:13:53+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com>`

```
On Tue, 16 May 2006 08:50:32 -0500, "HeyBub" <heybubNOSPAM@gmail.com>
wrote:

>Frederico Fonseca wrote:
>> New version of my previous posting.
…[52 more quoted lines elided]…
>release locks upon exit, but maybe not. 

Flag is set automatically. Look at the original post to see how it is
defined.

As for closing the files, the compiler may or not close it, but the
whole point of this code was to have it behaving exactly like the
original code (apart from the optimization error). As such I am
exiting the program on the same circumstances.

To be even more correct, and to avoid further errors, we should set a
flag stating if there had been an sucessefull open of the file(s), and
at the very end, close any openeds files. This this it not required to
add to the program, and should be left as an exercise to the less
knowledgeable on how to implement.


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 4)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-16T20:26:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147836398.445675.149560@j55g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com>`

```
> As for closing the files, the compiler may or not close it, but the
> whole point of this code was to have it behaving exactly like the
> original code (apart from the optimization error). As such I am
> exiting the program on the same circumstances.

If the file is left OPEN then a subsequent CALL will have its OPEN fail
because it is already open.  It is probably not an issue with this
routine but if a routine is used to process a series of files, for
example the CALL passes a filename, then one failure (read gives not
successful file-status) will result in all subsequent CALLs failing on
'file already open'.

Not a happy thing at 2am.

> we should set a
> flag stating if there had been an sucessefull open of the file(s),
> and at the very end, close any openeds files

I suppose you _could_ do it that way, or you could ensure that the
logic path is done correctly in the first place and then avoid having
to patch in a nasty little fix using flags.

What is wrong with using gotos is not the gotos themselves at all, they
are perfectly easy to see what happens. What is wrong is that they are
used to 'short cut' the program logic, which can also be done with such
tricks as performing an exit program, or using exit paragraph, or even
more nastiness as next sentence with end-if.

The problem with gotos is where the target of the goto lies, the
paragraph label.  It is not obvious when looking at the label where all
the logic paths may be.  It is necessary to examine the _whole_ program
to see where all the paths are. In the case of your code it is only a
few lines yet there is still a goto/short-cut trap in that the PERFORM
Read-Record does not necessarily return to the correct place and thus
the CLOSE does not happen.

While it may be that the bug remains as it was in the original you have
merely substituted the GOTOs with some other code that is just as bad.
You might as well have left it as GO TO Exit-Program, at least that
would honestly admit that you haven't actually changed to being
goto-less and writing the correct logic for the problem.

(Granted you have removed the mix of section and paragraph).
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 5)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-17T07:50:00+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4edih$hkp$01$1@news.t-online.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com>`

```
What's wrong with using DECLARATIVES and the
USE AFTER ERROR syntax ?
No GO TO's and you can do what you want there.
(Including closing the file, doing an EXIT PROGRAM or STOP RUN)

Roger

> The problem with gotos is where the target of the goto lies, the
> paragraph label.  It is not obvious when looking at the label where all
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 6)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-17T10:04:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d0vt3F17n36iU1@individual.net>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com>`

```
I've never used DECLARATIVES in production code, but I was fooling around
with them a few weeks ago at home using, yes, OpenCobol!  I found them
interesting, but rather limiting actually.  It appears you can assign a
declarative at either the file level (one per file) or at the file mode type
(one per file mode: INPUT, OUTPUT, I-O, EXTEND).  But neither one is generic
enough to do what I would like.

Let's say you define one for each file.  When an error occurs and the
declarative section is performed you know what file has an error and what
the error status is, but you aren't told what file action (OPEN, READ,
WRITE, REWRITE, CLOSE) was just performed that caused the error.  I suppose
you could *assume*, based on the fact that you'd never get a, say, EOF
condition on an open or a write, but are there not cases where the status
code alone might be ambiguous in this sense?  Perhaps not.

As for DECLARATIVES for file mode, this is even worse as you don't even know
what file is having a problem unless you do something like MOVE "FILE1" TO
CURRENT-FILE before each file action.  Seems to me to not be worth it. 
What'd I'd like to see is something like the following:

PROCEDURE DIVISION.
DECLARATIVES.
    USE AFTER EXCEPTION PROCEDURE ON ALL.
    DISPLAY "ERROR ON" FILE-ACTION " FOR FILE " FILE-NAME ", STATUS = "
FILE-STATUS
*   do some more stuff here to allow the operator to either retry or abort.
END DECLARITIVES.

FILE-ACTION and FILE-NAME would be "special registers" containing, well, the
action performed and the name of the file.  FILE-STATUS is, of course, the
FILE-STATUS defined in the SELECT statement.

What could be more simple?  One small section of code to handle all file
errors the same.  You could, of course, get more granular for specific
situations where this generic exception handler would not suffice.

I just can't imagine how the current usage of DECLARATIVES came about...  Am
I just (as usual) missing something obvious?

I will do a bit more fooling around using the "ON filename1, filename2,
filename3" to see if I can make this fairly useful by defining my own
FILE-ACTION and FILE-NAME fields and moving the appropriate values to them. 
It just seems to me that these are things you'd obviously want, so shouldn't
COBOL set them implicitly?  Ah well...

Frank

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> Roger While<simrw@sim-basis.de> 05/16/06 11:50 PM >>>
What's wrong with using DECLARATIVES and the
USE AFTER ERROR syntax ?
No GO TO's and you can do what you want there.
(Including closing the file, doing an EXIT PROGRAM or STOP RUN)

Roger

> The problem with gotos is where the target of the goto lies, the
> paragraph label.  It is not obvious when looking at the label where all
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-17T19:12:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7AKag.90258$E46.5142@fe09.news.easynews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com> <4d0vt3F17n36iU1@individual.net>`

```
Roger,
   any plans for OpenCOBOL to implement the following 2002 Intrinsic Functions:

- EXCEPTION-FILE
- EXCEPTION-STATEMENT
- EXCEPTION-STATUS

These would give Frank exactly what he is looking for (to make a "generic" 
declarative)
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 8)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-17T22:30:15+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4g14s$sjn$03$1@news.t-online.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com> <4d0vt3F17n36iU1@individual.net> <7AKag.90258$E46.5142@fe09.news.easynews.com>`

```
Actually, those shouldn't be too difficult.
I'll take a look over the weekend.

Roger

"William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
news:7AKag.90258$E46.5142@fe09.news.easynews.com...
> Roger,
>   any plans for OpenCOBOL to implement the following 2002 Intrinsic 
…[106 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 9)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-18T11:42:31+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4hfib$3vs$01$1@news.t-online.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com> <4d0vt3F17n36iU1@individual.net> <7AKag.90258$E46.5142@fe09.news.easynews.com> <e4g14s$sjn$03$1@news.t-online.com>`

```
Well, how about this for EXCEPTION-FILE
just now built in to OpenCOBOL  :-)
(EXCEPTION-STATUS coming soon)

       IDENTIFICATION DIVISION.
       PROGRAM-ID. MINIPROG.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER.  LINUX.
       OBJECT-COMPUTER.  LINUX.
       SPECIAL-NAMES.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT PRINTFILE ASSIGN TO "XXRXWXX"
             FILE STATUS RXWSTAT.
       DATA DIVISION.
       FILE SECTION.
       FD  PRINTFILE.
       01  PRINTREC         PIC X(132).
       WORKING-STORAGE SECTION.
       01  RXWSTAT          PIC XX.
       PROCEDURE DIVISION.
       A00-MAIN SECTION.
       001-MAIN-PROCEDURE.
           OPEN INPUT PRINTFILE.
           DISPLAY "File Status    " RXWSTAT.
           DISPLAY "EXCEPTION-FILE " FUNCTION EXCEPTION-FILE.
           DISPLAY "Return Length  "
                   FUNCTION LENGTH (FUNCTION EXCEPTION-FILE).
           STOP RUN.

When file does not exist :

File Status    35
EXCEPTION-FILE 35PRINTFILE
Return Length  00000011

When file exists :

File Status    00
EXCEPTION-FILE 00
Return Length  00000002
WARNING - Implicit CLOSE of XXRXWXX

Roger

"Roger While" <simrw@sim-basis.de> schrieb im Newsbeitrag 
news:e4g14s$sjn$03$1@news.t-online.com...
> Actually, those shouldn't be too difficult.
> I'll take a look over the weekend.
…[118 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 10)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-18T12:24:41+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4hi1c$vjm$02$1@news.t-online.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com> <4d0vt3F17n36iU1@individual.net> <7AKag.90258$E46.5142@fe09.news.easynews.com> <e4g14s$sjn$03$1@news.t-online.com> <e4hfib$3vs$01$1@news.t-online.com>`

```
EXCEPTION-STATUS is in :-)
Same prog as in first post with Proc Div -
           OPEN INPUT PRINTFILE.
           DISPLAY "File Status      " RXWSTAT.
           DISPLAY "EXCEPTION-FILE   " FUNCTION EXCEPTION-FILE.
           DISPLAY "Return Length    "
                   FUNCTION LENGTH (FUNCTION EXCEPTION-FILE).
           DISPLAY "EXCEPTION-STATUS " FUNCTION EXCEPTION-STATUS.
           STRING "TOOLONG" DELIMITED SIZE INTO RXWSTAT.
           DISPLAY "EXCEPTION-STATUS " FUNCTION EXCEPTION-STATUS.


File Status      35
EXCEPTION-FILE   35PRINTFILE
Return Length    00000011
EXCEPTION-STATUS EC-I-O-PERMANENT-ERROR
EXCEPTION-STATUS EC-OVERFLOW-STRING

Roger


"Roger While" <simrw@sim-basis.de> schrieb im Newsbeitrag 
news:e4hfib$3vs$01$1@news.t-online.com...
> Well, how about this for EXCEPTION-FILE
> just now built in to OpenCOBOL  :-)
…[172 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 11)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-18T14:13:57+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4hoe9$sgk$00$1@news.t-online.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com> <4d0vt3F17n36iU1@individual.net> <7AKag.90258$E46.5142@fe09.news.easynews.com> <e4g14s$sjn$03$1@news.t-online.com> <e4hfib$3vs$01$1@news.t-online.com> <e4hi1c$vjm$02$1@news.t-online.com>`

```
And EXCEPTION-STATEMENT is in :-)
(Note - prog must be compiled with debug option)
Same prog as last post with Proc Div -

           OPEN INPUT PRINTFILE.
           DISPLAY "File Status         " RXWSTAT.
           DISPLAY "EXCEPTION-FILE      " FUNCTION EXCEPTION-FILE.
           DISPLAY "Return Length       "
                   FUNCTION LENGTH (FUNCTION EXCEPTION-FILE).
           DISPLAY "EXCEPTION-STATUS    " FUNCTION EXCEPTION-STATUS.
           DISPLAY "EXCEPTION-STATEMENT " FUNCTION EXCEPTION-STATEMENT.
           STRING "TOOLONG" DELIMITED SIZE INTO RXWSTAT.
           DISPLAY "EXCEPTION-STATUS    " FUNCTION EXCEPTION-STATUS.
           DISPLAY "EXCEPTION-STATEMENT " FUNCTION EXCEPTION-STATEMENT.

File Status                              35
EXCEPTION-FILE               35PRINTFILE
Return Length                         00000011
EXCEPTION-STATUS         EC-I-O-PERMANENT-ERROR
EXCEPTION-STATEMENT OPEN
EXCEPTION-STATUS         EC-OVERFLOW-STRING
EXCEPTION-STATEMENT STRING

Roger

"Roger While" <simrw@sim-basis.de> schrieb im Newsbeitrag 
news:e4hi1c$vjm$02$1@news.t-online.com...
> EXCEPTION-STATUS is in :-)
> Same prog as in first post with Proc Div -
…[201 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 12)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-18T14:05:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d42d0F18jd2kU1@individual.net>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com> <4d0vt3F17n36iU1@individual.net> <7AKag.90258$E46.5142@fe09.news.easynews.com> <e4g14s$sjn$03$1@news.t-online.com> <e4hfib$3vs$01$1@news.t-online.com> <e4hi1c$vjm$02$1@news.t-online.com> <e4hoe9$sgk$00$1@news.t-online.com>`

```
All very cool!

So how about: FUNCTION EXCEPTION-LOCATION ?

:-)

I've really got to take a look at the source code for this compiler!

Frank

>>> Roger While<simrw@sim-basis.de> 05/18/06 6:13 AM >>>
And EXCEPTION-STATEMENT is in :-)
(Note - prog must be compiled with debug option)
Same prog as last post with Proc Div -

           OPEN INPUT PRINTFILE.
           DISPLAY "File Status         " RXWSTAT.
           DISPLAY "EXCEPTION-FILE      " FUNCTION EXCEPTION-FILE.
           DISPLAY "Return Length       "
                   FUNCTION LENGTH (FUNCTION EXCEPTION-FILE).
           DISPLAY "EXCEPTION-STATUS    " FUNCTION EXCEPTION-STATUS.
           DISPLAY "EXCEPTION-STATEMENT " FUNCTION EXCEPTION-STATEMENT.
           STRING "TOOLONG" DELIMITED SIZE INTO RXWSTAT.
           DISPLAY "EXCEPTION-STATUS    " FUNCTION EXCEPTION-STATUS.
           DISPLAY "EXCEPTION-STATEMENT " FUNCTION EXCEPTION-STATEMENT.

File Status                              35
EXCEPTION-FILE               35PRINTFILE
Return Length                         00000011
EXCEPTION-STATUS         EC-I-O-PERMANENT-ERROR
EXCEPTION-STATEMENT OPEN
EXCEPTION-STATUS         EC-OVERFLOW-STRING
EXCEPTION-STATEMENT STRING
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-19T03:49:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xfbbg.119788$Wl.97110@fe08.news.easynews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com> <4d0vt3F17n36iU1@individual.net> <7AKag.90258$E46.5142@fe09.news.easynews.com> <e4g14s$sjn$03$1@news.t-online.com> <e4hfib$3vs$01$1@news.t-online.com> <e4hi1c$vjm$02$1@news.t-online.com> <e4hoe9$sgk$00$1@news.t-online.com> <4d42d0F18jd2kU1@individual.net>`

```
I vote AGAINST <G> Exception-Location.   It is totally "up to the implementor" 
what that returns and whether it is useful or not is a real question (IMHO).
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 14)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-19T11:56:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d6f6gF197akbU1@individual.net>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com> <4d0vt3F17n36iU1@individual.net> <7AKag.90258$E46.5142@fe09.news.easynews.com> <e4g14s$sjn$03$1@news.t-online.com> <e4hfib$3vs$01$1@news.t-online.com> <e4hi1c$vjm$02$1@news.t-online.com> <e4hoe9$sgk$00$1@news.t-online.com> <4d42d0F18jd2kU1@individual.net> <xfbbg.119788$Wl.97110@fe08.news.easynews.com>`

```
Hmm, from what I read it looks useful.  Take the following code snippet:

000001 ID DIVISION.
000002 PROGRAM-ID. STUFF.
000003 PROCEDURE DIVISION.
000004 
000005 DECLARATIVES.
000006 HANDLER SECTION.
000007     USE AFTER EXCEPTION CONDITION EC-ALL.
000008 HANDLE-EXCEPTION.
000009     DISPLAY "ERROR: PROGRAM " FUNCTION EXCEPTION-LOCATION
000010     EXIT PROGRAM RAISING LAST EXCEPTION.
000011 END DECLARITIVES.
000012 
000013 MAINLINE SECTION.
000014 MAIN.
000015*  do something to cause an exception
000016     EXIT PROGRAM.
000017 END PROGRAM STUFF.


This should display

ERROR: PROGRAM STUFF: MAIN OF MAINLINE; 15

Seems pretty useful to me...


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> William M. Klein<wmklein@nospam.netcom.com> 05/18/06 9:49 PM >>>
I vote AGAINST <G> Exception-Location.   It is totally "up to the
implementor" 
what that returns and whether it is useful or not is a real question
(IMHO).
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 13)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-19T07:16:56+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4jkcf$dtm$02$1@news.t-online.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com> <4d0vt3F17n36iU1@individual.net> <7AKag.90258$E46.5142@fe09.news.easynews.com> <e4g14s$sjn$03$1@news.t-online.com> <e4hfib$3vs$01$1@news.t-online.com> <e4hi1c$vjm$02$1@news.t-online.com> <e4hoe9$sgk$00$1@news.t-online.com> <4d42d0F18jd2kU1@individual.net>`

```
Sure, coming up soon  :-)
Although, as Bill says in a later post, it's probably of
limited use. Some of this stuff anyway only gets activated when
debugging is enabled and there are usually then other specific
features which are more useful.
So ie. OC has a compile option which produces a trace of
section and paragraph names reached in the prog at run time
along with the prog-id when entered.

If you want to take a look -
I keep a snapshot tarball (AKA prerelease) of OpenCOBOL at :
http://www.sim-basis.de/open-cobol-0.33.tar.gz
This is at least CVS status and is usually ahead as it gets my
development stuff thrown in. (CVS as per status on the
OpenCOBOL project over at SourceForge)

Roger

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> schrieb im Newsbeitrag 
news:4d42d0F18jd2kU1@individual.net...
> All very cool!
>
…[31 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 14)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-19T10:07:34+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e4jucb$bqe$01$1@news.t-online.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com> <4d0vt3F17n36iU1@individual.net> <7AKag.90258$E46.5142@fe09.news.easynews.com> <e4g14s$sjn$03$1@news.t-online.com> <e4hfib$3vs$01$1@news.t-online.com> <e4hi1c$vjm$02$1@news.t-online.com> <e4hoe9$sgk$00$1@news.t-online.com> <4d42d0F18jd2kU1@individual.net> <e4jkcf$dtm$02$1@news.t-online.com>`

```
Here it is  :-)
Same prog as before with Proc Div
(compiled with debug option) -

       A00-MAIN SECTION.
       A01-MAIN-PROCEDURE.
           OPEN INPUT PRINTFILE.
           DISPLAY "File Status         " RXWSTAT.
           DISPLAY "EXCEPTION-FILE      " FUNCTION EXCEPTION-FILE.
           DISPLAY "Return Length       "
                   FUNCTION LENGTH (FUNCTION EXCEPTION-FILE).
           DISPLAY "EXCEPTION-STATUS    " FUNCTION EXCEPTION-STATUS.
           DISPLAY "EXCEPTION-STATEMENT " FUNCTION EXCEPTION-STATEMENT.
       A02-MAIN-PARA.
           DISPLAY "EXCEPTION-LOCATION  " FUNCTION EXCEPTION-LOCATION.
           STRING "TOOLONG" DELIMITED SIZE INTO RXWSTAT.
           DISPLAY "EXCEPTION-STATUS    " FUNCTION EXCEPTION-STATUS.
           DISPLAY "EXCEPTION-STATEMENT " FUNCTION EXCEPTION-STATEMENT.
       B00-MAIN SECTION.
       B01-MAIN-PROCEDURE.
           DISPLAY "EXCEPTION-LOCATION  " FUNCTION EXCEPTION-LOCATION.


File Status                               35
EXCEPTION-FILE                35PRINTFILE
Return Length                          00000011
EXCEPTION-STATUS          EC-I-O-PERMANENT-ERROR
EXCEPTION-STATEMENT  OPEN
EXCEPTION-LOCATION    MINIPROG; A01-MAIN-PROCEDURE OF A00-MAIN; 21
EXCEPTION-STATUS          EC-OVERFLOW-STRING
EXCEPTION-STATEMENT  STRING
EXCEPTION-LOCATION    MINIPROG; A02-MAIN-PARA OF A00-MAIN; 30

(Yep, the prog-id is MINIPROG and the line numbers are correct)

Roger


"Roger While" <simrw@sim-basis.de> schrieb im Newsbeitrag 
news:e4jkcf$dtm$02$1@news.t-online.com...
> Sure, coming up soon  :-)
> Although, as Bill says in a later post, it's probably of
…[53 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 8)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-17T14:34:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d1fn3F188d0mU1@individual.net>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com> <4d0vt3F17n36iU1@individual.net> <7AKag.90258$E46.5142@fe09.news.easynews.com>`

```
Sounds cool.

Now to figure out a way to port OpenCobol to VSE!  :-)

Frank

>>> William M. Klein<wmklein@nospam.netcom.com> 05/17/06 1:12 PM >>>
Roger,
   any plans for OpenCOBOL to implement the following 2002 Intrinsic
Functions:

- EXCEPTION-FILE
- EXCEPTION-STATEMENT
- EXCEPTION-STATUS

These would give Frank exactly what he is looking for (to make a "generic" 
declarative)
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-05-17T22:07:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<09Nag.113114$OZ2.91384@fe01.news.easynews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com> <4d0vt3F17n36iU1@individual.net> <7AKag.90258$E46.5142@fe09.news.easynews.com> <4d1fn3F188d0mU1@individual.net>`

```
Given the existence of C and C-libraries, you probably could port to VSE.  The 
problem(s) would arise with things like ILC, Files, CICS, etc.
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 10)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-18T14:13:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d42rdF18jd2kU2@individual.net>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <e4edih$hkp$01$1@news.t-online.com> <4d0vt3F17n36iU1@individual.net> <7AKag.90258$E46.5142@fe09.news.easynews.com> <4d1fn3F188d0mU1@individual.net> <09Nag.113114$OZ2.91384@fe01.news.easynews.com>`

```
Too bad the C compiler costs money.  Plus I'm not sure that it has all of
the C libraries needed by OpenCobol.  Of course it wouldn't need ncurses,
because the screen section wouldn't be supported. It probably wouldn't need
Berkeley DB, but an interface to VSAM and regular sequential files would be
needed.  I would guess that GMP could be bypassed in favor of native decimal
arithmatic.  And I think dynamic calls would be fairly(?) simple.  So who
knows.  And I imagine that for CICS there'd be no reason that the existing
COBOL interface could not be used, though I imagine LE might make things
more difficult in that regard.

Certainly gets me thinking, but I can't imagine I could take time from doing
"real work" to work on it.  Ah well...

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> William M. Klein<wmklein@nospam.netcom.com> 05/17/06 4:07 PM >>>
Given the existence of C and C-libraries, you probably could port to VSE. 
The 
problem(s) would arise with things like ILC, Files, CICS, etc.
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-05-18T15:16:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<126pi2de5ul6860@corp.supernews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:1147836398.445675.149560@j55g2000cwa.googlegroups.com...
[snip]
> The problem with gotos is where the target of the goto lies, the
> paragraph label.  It is not obvious when looking at the label where all
> the logic paths may be.  It is necessary to examine the _whole_ program
> to see where all the paths are.

If the 'style' is that of using GO TO only within sections
then it *is not* 'necessary to examine the _whole_ program'.

The code snippet below is from a program that uses GO
TO only within sections, thus it is not necessary to examine
any other part of the program to understand every logic
path in this code. [The requirement (from a 'challenge' last
year) was for the highest possible execution speed. Using
structured programming just slows things down.]

-----
        01 char pic x.
        01 xchar redefines char pic x comp-x.

       get-word section.
       begin.
           move 0 to text-pos
           move 0 to hash-index
           move spaces to word-text
           if file-closed
               exit section
           end-if
           .
       loop-start.
           move buffer (buffer-pos:1) to char
           add 1 to buffer-pos
           go to ws ws ws ws ws ws ws ws ws ws ws ws ws ws ws
              ws ws ws ws ws ws ws ws ws ws ws ws ws ws ws ws
              ws ws ws ws ws ws ws ap ws ws ws ws ws ws ws ws
              ws ws ws ws ws ws ws ws ws ws ws ws ws ws ws ws
              ws uc uc uc uc uc uc uc uc uc uc uc uc uc uc uc
              uc uc uc uc uc uc uc uc uc uc uc ws ws ws ws ws
              ws lc lc lc lc lc lc lc lc lc lc lc lc lc lc lc
              lc lc lc lc lc lc lc lc lc lc lc ws ws ws ws ws
               depending on xchar
           if xchar > 127
               go to ws
           end-if
           go to end-of-block
           .
       end-of-block.
           perform get-block
           if file-closed
               go to loop-exit
           end-if
           go to loop-start
           .
       ap.
           go to loop-start
           .
       ws.
           if text-pos = 0
               go to loop-start
           end-if
           go to loop-exit
           .
       uc.
           add 32 to xchar
           go to lc
           .
       lc.
           multiply 17 by hash-index
           add xchar to hash-index
           add 1 to text-pos
           move char to word-text (text-pos:1)
           go to loop-start
           .
       loop-exit.
           exit
           .
-----
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-18T13:51:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<60kp62le0uv5mm0aqmb2vbssh3k6160i5l@4ax.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <126pi2de5ul6860@corp.supernews.com>`

```
On Thu, 18 May 2006 15:16:49 -0400, "Rick Smith" <ricksmith@mfi.net>
wrote:

>The code snippet below is from a program that uses GO
>TO only within sections, thus it is not necessary to examine
…[3 more quoted lines elided]…
>structured programming just slows things down.]

Not when the optimizer limits itself when it sees GOTOs.

 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 6)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-18T14:57:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147989432.559546.72730@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<126pi2de5ul6860@corp.supernews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <126pi2de5ul6860@corp.supernews.com>`

```

Rick Smith wrote:

> If the 'style' is that of using GO TO only within sections
> then it *is not* 'necessary to examine the _whole_ program'.

That may be true, if it could be guaranteed that the style was actually
correctly followed. For example Judson had a program that would check
all labels and labels to ensure that the only gotos were to an exit
that was the last label in a section. If a word 'SECTION' had been
accidentally ommitted, or a 'GO TO 8194-EXIT' was accidentally in the
'8149-PROCESSING SECTION'  then it would flag these as an error, the
compiler will not.

In the absense of any SECTION, GO TO, EXIT PARAGRAPH/SECTION, NEXT
SENTENCE or other positionally dependent code a simple grep will
guarantee these are absent, and so help to ensure that a 'perform
paragraph only' style has actually been used.

> The code snippet below is from a program that uses GO
> TO only within sections, thus it is not necessary to examine
> any other part of the program to understand every logic
> path in this code.

It may not be necessary for *you* because you wrote the code and
debugged it. However, if I was given this code and was required to
modify it I have no guarantee at all, except your word, that I don't
need to examine the whole program. The compiler won't tell me, text
tools won't tell me.

> [The requirement (from a 'challenge' last
> year) was for the highest possible execution speed. Using
> structured programming just slows things down.]

I recall that RW used to claim things as being 'faster' when an actual
test run showed that his claim was untrue.
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-05-18T21:24:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<126q7kn81mg5r3a@corp.supernews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <126pi2de5ul6860@corp.supernews.com> <1147989432.559546.72730@u72g2000cwu.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:1147989432.559546.72730@u72g2000cwu.googlegroups.com...
>
> Rick Smith wrote:
…[10 more quoted lines elided]…
> compiler will not.

As I recall, Mr McClendon used 6 digit prefixes with
PERFORM THRU paragraphs; but I suppose I could
be mistaken.

> In the absense of any SECTION, GO TO, EXIT PARAGRAPH/SECTION, NEXT
> SENTENCE or other positionally dependent code a simple grep will
> guarantee these are absent, and so help to ensure that a 'perform
> paragraph only' style has actually been used.

Which seems entirely unrelated to 'using GO TO only
within sections'.

> > The code snippet below is from a program that uses GO
> > TO only within sections, thus it is not necessary to examine
…[7 more quoted lines elided]…
> tools won't tell me.

Micro Focus CSI tells me a lot of things other products
don't.

> > [The requirement (from a 'challenge' last
> > year) was for the highest possible execution speed. Using
…[3 more quoted lines elided]…
> test run showed that his claim was untrue.

I don't recall Mr Wagner making such a claim with reference
to structured programming; but in this case, I first developed
the program using structured techniques then changed that
one procedure to using GO TO when I realized that it would
be faster with GO TO DEPENDING. The other GO TO
statements completed the necessary control paths. That
'structured programming just slows things down' is based
on that experience as well as several others where actual
measurements of execution time showed improvement by
'unstructuring'.
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 8)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-18T19:11:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148004704.671781.116790@j73g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<126q7kn81mg5r3a@corp.supernews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <126pi2de5ul6860@corp.supernews.com> <1147989432.559546.72730@u72g2000cwu.googlegroups.com> <126q7kn81mg5r3a@corp.supernews.com>`

```

Rick Smith wrote:

> As I recall, Mr McClendon used 6 digit prefixes with
> PERFORM THRU paragraphs; but I suppose I could
> be mistaken.

That could well have been the case. Certainly the check seemed to rely
on checking prefixes of the labels (which I dislike, but nevermind).

> > In the absense of any SECTION, GO TO, EXIT PARAGRAPH/SECTION, NEXT
> > SENTENCE or other positionally dependent code a simple grep will
…[4 more quoted lines elided]…
> within sections'.

It was an contrasting example of a style where, unlike 'sections and
goto', it was easy to show that the style had been correctly adhered
to.

> Micro Focus CSI tells me a lot of things other products
> don't.

MF CSI doesn't tell me anything at all.

> I don't recall Mr Wagner making such a claim with reference
> to structured programming; but in this case, I first developed
…[7 more quoted lines elided]…
> 'unstructuring'.

I grant you that a table based go to depending on is faster than a
whole bunch of IFs or WHENs.

Howver, I just did a version without any GO TOs inside a single PERFORM
UNTIL that runs in 277ms versus your code in 272ms for a few million
iterations of simple fixed data. I'll try tuning it if I have time.
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 9)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-05-20T21:52:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<126vi11dqgg9113@corp.supernews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <126pi2de5ul6860@corp.supernews.com> <1147989432.559546.72730@u72g2000cwu.googlegroups.com> <126q7kn81mg5r3a@corp.supernews.com> <1148004704.671781.116790@j73g2000cwa.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:1148004704.671781.116790@j73g2000cwa.googlegroups.com...
[snip]
> Howver, I just did a version without any GO TOs inside a single PERFORM
> UNTIL that runs in 277ms versus your code in 272ms for a few million
> iterations of simple fixed data. I'll try tuning it if I have time.

Here is a tuned version that may be faster than GO TO
DEPENDING. [Preliminary tests show them to be about
the same; but those tests were done with other programs
running.] As may be seen, I duplicated some code and
separated the test for 'space' to move it closer to the
start of the EVALUATE. Execution counts are shown as
in-line comments and were generated by Micro Focus
Analyzer.

-----
       get-word section.
       begin.
           move 0 to text-pos *> 789782
           move 0 to hash-index
           move spaces to word-text
           if file-closed
               exit section *> -
           end-if
           set word-complete to false
           perform until word-complete
               move buffer (buffer-pos:1) to char *> 4833138
               add 1 to buffer-pos
               evaluate char
                 when "a" thru "z" *> 3107111
                   multiply 17 by hash-index
                   add xchar to hash-index
                   add 1 to text-pos
                   move char to word-text (text-pos:1)
                 when space *> 1152081
                   if text-pos = 0
                       continue *> 531555
                   else
                       set word-complete to true *> 620526
                   end-if
                 when "A" thru "Z" *> 116015
                   add 32 to xchar
                   multiply 17 by hash-index
                   add xchar to hash-index
                   add 1 to text-pos
                   move char to word-text (text-pos:1)
                 when "'" *> 2022
                   continue
                 when x"00" *> 197
                   perform get-block
                   if file-closed
                       set word-complete to true *> 1
                   end-if
                 when other *> 455712
                   if text-pos = 0
                       continue *> 286457
                   else
                       set word-complete to true *> 169255
                   end-if
               end-evaluate
           end-perform
           .
-----
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 10)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-21T13:36:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148243819.626161.149570@i40g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<126vi11dqgg9113@corp.supernews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <126pi2de5ul6860@corp.supernews.com> <1147989432.559546.72730@u72g2000cwu.googlegroups.com> <126q7kn81mg5r3a@corp.supernews.com> <1148004704.671781.116790@j73g2000cwa.googlegroups.com> <126vi11dqgg9113@corp.supernews.com>`

```
> Here is a tuned version that may be faster than GO TO DEPENDING.

I was working on a lookup table based solution where a table of 256
preset items had values for each character. a-z being zero, A-Z being
32, ' as -2 and the rest being -1. PERFORM UNTIL -1 and text-pos > 0.
Add the non-negative value before calculating the hash.

Maybe it wouldn't be faster that the evaluate, or perhaps the table
should be a translate table to save the add.
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-05-22T16:06:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12746h4fmfnmr85@corp.supernews.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <126pi2de5ul6860@corp.supernews.com>`

```

Mr Brazee, ever since your messages were "Posted Via
Usenet.com", they have not appeared when downloading
news:comp.lang.cobol newsgroup messages to my computer.
I happen to notice this one in Google Groups.

-----
On Thu, 18 May 2006 15:16:49 -0400, "Rick Smith" <ricksm...@mfi.net>
wrote:

>The code snippet below is from a program that uses GO
>TO only within sections, thus it is not necessary to examine
…[3 more quoted lines elided]…
>structured programming just slows things down.]

Not when the optimizer limits itself when it sees GOTOs.
-----

Mr Brazee, that would seem to depend entirely upon
what limits the 'optimizer' imposes on itself; but consider
that if an optimized, structured program is slower than
an non-optimized, unstructured program, then it might follow
that "[u]sing structured programming just slow[ed] things
down."
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-22T14:43:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6i84725hu49g9f4p1sp6jlana4mqals0jq@4ax.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <126pi2de5ul6860@corp.supernews.com> <12746h4fmfnmr85@corp.supernews.com>`

```
On Mon, 22 May 2006 16:06:42 -0400, "Rick Smith" <ricksmith@mfi.net>
wrote:

>Mr Brazee, that would seem to depend entirely upon
>what limits the 'optimizer' imposes on itself; but consider
…[3 more quoted lines elided]…
>down."

People in other newsgroups have said the same thing.   Usenet has
consistently told me:

*This is an automated message.  Please do not reply directly*

Below is the response our technical support team has issued regarding
your earlier inquiry.  
If this response resolves your issue no further action on your part is
necessary.  
If you require further assistance please use the link at the bottom of
this message or go to the members area.

In answer to your question:

Hello,

The issue isn't on our end, we can see the posts fine. Bob will need
to contact Supernews. We think its his usenet provider not allowing
him to see your posts correctly.

Thanks,
Usenet Tech Support

Your original message text:

Here's a message, with headers:
```

###### ↳ ↳ ↳ Re: abortive exiting

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-05-23T08:26:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tn667214mr167dvcoj289hbero8vlevrao@4ax.com>`
- **References:** `<4cs23aF17bpukU1@individual.net> <55ui62db8u7janashfmmgujqtu2qjgoaap@4ax.com> <126jm4jf05o9jdd@news.supernews.com> <scqk62d3hjc70fhtn3sjvq8fnpsfllm7a2@4ax.com> <1147836398.445675.149560@j55g2000cwa.googlegroups.com> <126pi2de5ul6860@corp.supernews.com> <12746h4fmfnmr85@corp.supernews.com> <6i84725hu49g9f4p1sp6jlana4mqals0jq@4ax.com>`

```
On Mon, 22 May 2006 14:43:55 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Mon, 22 May 2006 16:06:42 -0400, "Rick Smith" <ricksmith@mfi.net>
>wrote:
…[6 more quoted lines elided]…
>>down."

New reply from Usenet:

Hello,

The users that are unable to see your messages all seem to be using
the SuperNews service. You will need to contact Supernews for more
information. 

Contact information: http://www.supernews.com/contact_info.html

Thanks,
Usenet Tech Support

Your original message text:

 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: abortive exiting

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-17T15:48:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d1k1eF18e7naU1@individual.net>`
- **References:** `<4cs23aF17bpukU1@individual.net>`

```
Me again.  Feel free to ignore me.

Take the following code:

 BROWSE-CARD-HISTORY.                         
     PERFORM START-BROWSE-CARD-HISTORY        
     IF NO-MORE-RECORDS                       
         CONTINUE                             
     ELSE                                     
         PERFORM NEXT-CARD-HISTORY-FILE       
         PERFORM PREV-CARD-HISTORY-FILE       
         PERFORM PREV-CARD-HISTORY-FILE       
         IF CHR-MH-CARD-NBR NOT = CARD-NBR    
             SET NO-MORE-RECORDS TO TRUE      
         END-IF                               
         PERFORM UNTIL NO-MORE-RECORDS        
             PERFORM HANDLE-RECORD            
             PERFORM CALL-XML-ROUTINE         
             PERFORM PREV-CARD-HISTORY-FILE   
             IF CHR-MH-CARD-NBR NOT = CARD-NBR
                 SET NO-MORE-RECORDS TO TRUE  
             END-IF                           
         END-PERFORM                          
         PERFORM END-BROWSE-CARD-HISTORY      
     END-IF                                   
     EXIT.                                    

Wouldn't it be nice if if there is any unexpected error in any of the
performed routines we could simply "jump" to the EXIT statement?  Again,
what I am trying to avoid is something like:

 BROWSE-CARD-HISTORY.                         
     PERFORM START-BROWSE-CARD-HISTORY        
     IF MORE-RECORDS                       
         PERFORM NEXT-CARD-HISTORY-FILE       
         IF MORE-RECORDS         
             PERFORM PREV-CARD-HISTORY-FILE       
             IF MORE-RECORDS         
                 PERFORM PREV-CARD-HISTORY-FILE       
                 IF MORE-RECORDS
                     IF CHR-MH-CARD-NBR NOT = CARD-NBR    
                         SET NO-MORE-RECORDS TO TRUE      
                     END-IF                               
                     PERFORM UNTIL NO-MORE-RECORDS        
                         PERFORM HANDLE-RECORD            
                         PERFORM CALL-XML-ROUTINE         
                         PERFORM PREV-CARD-HISTORY-FILE   
                         IF CHR-MH-CARD-NBR NOT = CARD-NBR
                             SET NO-MORE-RECORDS TO TRUE  
                         END-IF                           
                     END-PERFORM                          
         PERFORM END-BROWSE-CARD-HISTORY      
     END-IF                                   
     .                                    

Obviously, in START-BROWSE-CARD-HISTORY,NEXT-CARD-HISTORY-FILE, and
PREV-CARD-HISTORY-FILE I attempt the specified function and set MORE-RECORDS
to TRUE if successful and NO-MORE-RECORDS if not, or if there's an
unexpected result.

Now I won't get into the fact that I have to do one READNEXT followed by two
READPREVs to get the "first" record...

I hope that this makes more clear the reason for my obsession.
Seems to be in a language with nice exception handling I could do something
like:
 BROWSE-CARD-HISTORY.                         
     try
         PERFORM START-BROWSE-CARD-HISTORY        
         IF RECORD-FOUND
             try
                 PERFORM MAINLINE
             end-try
         END-IF
     catch EXCEPTION-ALL
*        do some error handling here
     end-try
     .                                    

MAINLINE.
     PERFORM NEXT-CARD-HISTORY-FILE       
     PERFORM PREV-CARD-HISTORY-FILE       
     PERFORM PREV-CARD-HISTORY-FILE       
     IF CHR-MH-CARD-NBR NOT = CARD-NBR    
         SET NO-MORE-RECORDS TO TRUE      
     END-IF                               
     PERFORM UNTIL NO-MORE-RECORDS        
          PERFORM HANDLE-RECORD            
          PERFORM CALL-XML-ROUTINE         
          PERFORM PREV-CARD-HISTORY-FILE   
          IF CHR-MH-CARD-NBR NOT = CARD-NBR
              SET NO-MORE-RECORDS TO TRUE  
          END-IF                           
      END-PERFORM                          
      PERFORM END-BROWSE-CARD-HISTORY      
      .

Here we would throw an exception for a non expected condition (basically
anything other than OK, not-found or EOF).

Stil a bit verbose, to be honest, but at least all of the error-handling
stuff is separated from the main code stream.


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

##### ↳ ↳ Re: abortive exiting

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-17T16:22:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1147908163.047556.236720@j55g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<4d1k1eF18e7naU1@individual.net>`
- **References:** `<4cs23aF17bpukU1@individual.net> <4d1k1eF18e7naU1@individual.net>`

```

Frank Swarbrick wrote:

> what I am trying to avoid is something like:
>
…[27 more quoted lines elided]…
> unexpected result.

One of the advantages of a style that eliminates all the GOTOs and the
pseudo-gotos is that code can be moved around without reference to any
positional dependencies.  For example if you had a go to ~-exit then
you would not be able to take a bunch of that code and just move it to
another paragraph. Well actually you could if you mixed performs of
paragraphs and sections but that leads to too many problems.  By
removing all code that is positionally dependent, such as goto, exit
something and next sentence, you remove the need to keep code in
particular places.

I would probably code this as something like:

  BROWSE-CARD-HISTORY.
       PERFORM START-CARD-HISTORY
       PERFORM
               UNTIL NO-MORE-RECORDS
                    OR CHR-MH-CARD-NBR NOT = CARD-NBR

               PERFORM HANDLE-RECORD
               PERFORM CALL-XML-ROUTINE
               PERFORM PREV-CARD-HISTORY-FILE
        END-PERFORM
        PERFORM END-BROWSE-CARD-HISTORY
        .

    START-CARD-HISTORY.
        PERFORM START-BROWSE-CARD-HISTORY
        IF MORE-RECORDS
            PERFORM  NEXT-CARD-HISTORY-FILE
            IF MORE-RECORDS
               PERFORM PREV-CARD-HISTORY-FILE
               IF MORE-RECORDS
                   PERFORM PREV-CARD-HISTORY-FILE
              END-IF
           END-IF
        END-IF
        .

This, IMHO, indicates that the start-next-prev-prev is a block of code
that can be reused and that it is a single irreducible block.

_Because_ there is no go to ~-exit or equivalent there is no need to
build large blocks of deeply nested code nor to 'short cut' to avoid
deep nesting, just rip the code out and create a new paragraph for it.
If the _only_ structure is perform paragraph then there will be no drop
thrus and thus the new paragraph can be put at the end of the current
one.
```

###### ↳ ↳ ↳ Re: abortive exiting

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-18T14:17:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d4325F18jd2kU3@individual.net>`
- **References:** `<4cs23aF17bpukU1@individual.net> <4d1k1eF18e7naU1@individual.net> <1147908163.047556.236720@j55g2000cwa.googlegroups.com>`

```
Richard<riplin@Azonic.co.nz> 05/17/06 5:22 PM >>>
>
>Frank Swarbrick wrote:
…[28 more quoted lines elided]…
>> PREV-CARD-HISTORY-FILE I attempt the specified function and set
MORE-RECORDS
>> to TRUE if successful and NO-MORE-RECORDS if not, or if there's an
>> unexpected result.
…[47 more quoted lines elided]…
>one.

True enough, and a very valid point.  I will try it on for size!
:-)

Thanks,
Frank
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
