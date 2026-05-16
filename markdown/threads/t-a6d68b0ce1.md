[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Write not happening?

_12 messages · 4 participants · 2002-04_

---

### Write not happening?

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-10T01:52:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jVMs8.31382$4L4.1174571@typhoon.austin.rr.com>`

```
under OS/390, Cobol 1.2.2, the following code is simply failing. 
No indication of why, it simply doesn't write to the VSAM file it is supposed to 
be writing to. 

I'm in the middle of one of those marathon coding sessions right now, so I am probably too
tired to really see what is going on. Anyone have any advice on this one? All this little segment
of the application is doing is loading some records from a sequential file. 

Thanks 
-Paul

000150              WRITE SMDR-RECORD                                        
000151                INVALID KEY                                            
000152                  DISPLAY '(1) ' WS-USER-COUNT1 ': FAILED RECORD'      
000153                  DISPLAY '(F) ' SMDRIN-RECORD                         
000154                  DISPLAY '(L) ' WS-LAST-SMDR-RECORD                   
000155                  DISPLAY ' '                                          
000156                  ADD 1 TO WS-USER-COUNT2                              
000157                NOT INVALID KEY                                        
000158                  MOVE SMDRIN-RECORD TO WS-LAST-SMDR-RECORD            
000159                  ADD 1 TO WS-USER-COUNT3                              
000160                  DISPLAY 'SMDRWRITE: ' SMDR-RECORD                    
000161                END-WRITE                                              
000162              READ SMDRIN NEXT RECORD                                  


I put display statements just before and after the write, so I am sure the code is being hit. 
I also displayed the SMDR-RECORD and it is being loaded correctly. 
TKU! -Paul
```

#### ↳ Re: Write not happening?

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-10T01:56:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RYMs8.31384$4L4.1175807@typhoon.austin.rr.com>`
- **References:** `<jVMs8.31382$4L4.1174571@typhoon.austin.rr.com>`

```
I mean, I displayed it BEFORE the write. The displays in that code are usually not there. 
   
  I also displayed the SMDR-RECORD and it is being loaded correctly. 
  TKU! -Paul
```

#### ↳ Re: Write not happening?

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2002-04-09T21:16:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a90795$fhf$1@suaar1aa.prod.compuserve.com>`
- **References:** `<jVMs8.31382$4L4.1174571@typhoon.austin.rr.com>`

```
I would suggest you put a file status in the select statement and
check its value after the write (and open). Invalid key does not catch
all the possible failure conditions. Let us know what happens.

===================================================================== 
  "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:jVMs8.31382$4L4.1174571@typhoon.austin.rr.com...
  under OS/390, Cobol 1.2.2, the following code is simply failing. 
  No indication of why, it simply doesn't write to the VSAM file it is supposed to 
  be writing to. 

  I'm in the middle of one of those marathon coding sessions right now, so I am probably too
  tired to really see what is going on. Anyone have any advice on this one? All this little segment
  of the application is doing is loading some records from a sequential file. 

  Thanks 
  -Paul

  000150              WRITE SMDR-RECORD                                        
  000151                INVALID KEY                                            
  000152                  DISPLAY '(1) ' WS-USER-COUNT1 ': FAILED RECORD'      
  000153                  DISPLAY '(F) ' SMDRIN-RECORD                         
  000154                  DISPLAY '(L) ' WS-LAST-SMDR-RECORD                   
  000155                  DISPLAY ' '                                          
  000156                  ADD 1 TO WS-USER-COUNT2                              
  000157                NOT INVALID KEY                                        
  000158                  MOVE SMDRIN-RECORD TO WS-LAST-SMDR-RECORD            
  000159                  ADD 1 TO WS-USER-COUNT3                              
  000160                  DISPLAY 'SMDRWRITE: ' SMDR-RECORD                    
  000161                END-WRITE                                              
  000162              READ SMDRIN NEXT RECORD                                  


  I put display statements just before and after the write, so I am sure the code is being hit. 
  I also displayed the SMDR-RECORD and it is being loaded correctly. 
  TKU! -Paul
```

##### ↳ ↳ Re: Write not happening?

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-10T02:47:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oJNs8.31397$4L4.1187353@typhoon.austin.rr.com>`
- **References:** `<jVMs8.31382$4L4.1174571@typhoon.austin.rr.com> <a90795$fhf$1@suaar1aa.prod.compuserve.com>`

```
Boy- I am tired. The file opens with a status of 00, but each write it getting a status of 90. 
90? 

Thanks 
-Paul

  "Ron" <NoSoy@swbell.net> wrote in message news:a90795$fhf$1@suaar1aa.prod.compuserve.com...
  I would suggest you put a file status in the select statement and
  check its value after the write (and open). Invalid key does not catch
  all the possible failure conditions. Let us know what happens.

  ===================================================================== 
    "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:jVMs8.31382$4L4.1174571@typhoon.austin.rr.com...
    under OS/390, Cobol 1.2.2, the following code is simply failing. 
    No indication of why, it simply doesn't write to the VSAM file it is supposed to 
    be writing to. 

    I'm in the middle of one of those marathon coding sessions right now, so I am probably too
    tired to really see what is going on. Anyone have any advice on this one? All this little segment
    of the application is doing is loading some records from a sequential file. 

    Thanks 
    -Paul

    000150              WRITE SMDR-RECORD                                        
    000151                INVALID KEY                                            
    000152                  DISPLAY '(1) ' WS-USER-COUNT1 ': FAILED RECORD'      
    000153                  DISPLAY '(F) ' SMDRIN-RECORD                         
    000154                  DISPLAY '(L) ' WS-LAST-SMDR-RECORD                   
    000155                  DISPLAY ' '                                          
    000156                  ADD 1 TO WS-USER-COUNT2                              
    000157                NOT INVALID KEY                                        
    000158                  MOVE SMDRIN-RECORD TO WS-LAST-SMDR-RECORD            
    000159                  ADD 1 TO WS-USER-COUNT3                              
    000160                  DISPLAY 'SMDRWRITE: ' SMDR-RECORD                    
    000161                END-WRITE                                              
    000162              READ SMDRIN NEXT RECORD                                  


    I put display statements just before and after the write, so I am sure the code is being hit. 
    I also displayed the SMDR-RECORD and it is being loaded correctly. 
    TKU! -Paul
```

###### ↳ ↳ ↳ Re: Write not happening?

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2002-04-09T23:41:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a90fq3$qol$1@suaar1ac.prod.compuserve.com>`
- **References:** `<jVMs8.31382$4L4.1174571@typhoon.austin.rr.com> <a90795$fhf$1@suaar1aa.prod.compuserve.com> <oJNs8.31397$4L4.1187353@typhoon.austin.rr.com>`

```
Oh great. File status 90 is one of those lovely codes defined as "No further
information". Are there any messages on the job log that might give the 
exact VSAM error? If not, you will have to go the next step and get the vsam 
return codes as well, like this: 

file status is vsam-status vsam-return.

01  vsam-return-area.
    05 vsam-status pic xx. 
    05 vsam-return. 
        10 vsam-return-code pic 9(2) comp. 
        10 vsam-function-code pic 9(1) comp. 
        10 vsam-feedback-code pic 9(3) comp.  

Then, oh joy, you have to go to the assembler vsam macro reference to interpret these 
codes. Move these values to some usage display field and display them and let us know.
I'll check in the morning. Does this file have any alternate indexes? I can't really tell
beyond that without seeing the job, the program, jcl and cluster definition.

    
  "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:oJNs8.31397$4L4.1187353@typhoon.austin.rr.com...
  Boy- I am tired. The file opens with a status of 00, but each write it getting a status of 90. 
  90? 

  Thanks 
  -Paul

    "Ron" <NoSoy@swbell.net> wrote in message news:a90795$fhf$1@suaar1aa.prod.compuserve.com...
    I would suggest you put a file status in the select statement and
    check its value after the write (and open). Invalid key does not catch
    all the possible failure conditions. Let us know what happens.

    ===================================================================== 
      "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:jVMs8.31382$4L4.1174571@typhoon.austin.rr.com...
      under OS/390, Cobol 1.2.2, the following code is simply failing. 
      No indication of why, it simply doesn't write to the VSAM file it is supposed to 
      be writing to. 

      I'm in the middle of one of those marathon coding sessions right now, so I am probably too
      tired to really see what is going on. Anyone have any advice on this one? All this little segment
      of the application is doing is loading some records from a sequential file. 

      Thanks 
      -Paul

      000150              WRITE SMDR-RECORD                                        
      000151                INVALID KEY                                            
      000152                  DISPLAY '(1) ' WS-USER-COUNT1 ': FAILED RECORD'      
      000153                  DISPLAY '(F) ' SMDRIN-RECORD                         
      000154                  DISPLAY '(L) ' WS-LAST-SMDR-RECORD                   
      000155                  DISPLAY ' '                                          
      000156                  ADD 1 TO WS-USER-COUNT2                              
      000157                NOT INVALID KEY                                        
      000158                  MOVE SMDRIN-RECORD TO WS-LAST-SMDR-RECORD            
      000159                  ADD 1 TO WS-USER-COUNT3                              
      000160                  DISPLAY 'SMDRWRITE: ' SMDR-RECORD                    
      000161                END-WRITE                                              
      000162              READ SMDRIN NEXT RECORD                                  


      I put display statements just before and after the write, so I am sure the code is being hit. 
      I also displayed the SMDR-RECORD and it is being loaded correctly. 
      TKU! -Paul
```

###### ↳ ↳ ↳ Re: Write not happening?

_(reply depth: 4)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2002-04-10T17:11:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0204101611.443dda07@posting.google.com>`
- **References:** `<jVMs8.31382$4L4.1174571@typhoon.austin.rr.com> <a90795$fhf$1@suaar1aa.prod.compuserve.com> <oJNs8.31397$4L4.1187353@typhoon.austin.rr.com> <a90fq3$qol$1@suaar1ac.prod.compuserve.com>`

```
Hi Ron,

You didn't show your select or FD stmts. The LE cobols have a runtime
option that masks the abend and leaves you with an empty file. I
misspelled the DDNAME, and it happened. You might want to check that.

Jack 


"Ron" <NoSoy@swbell.net> wrote in message news:<a90fq3$qol$1@suaar1ac.prod.compuserve.com>...
> Oh great. File status 90 is one of those lovely codes defined as "No 
> further
…[96 more quoted lines elided]…
> --
```

###### ↳ ↳ ↳ Re: Write not happening?

_(reply depth: 4)_

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-11T00:11:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ex4t8.34396$ud6.1295775@typhoon.austin.rr.com>`
- **References:** `<jVMs8.31382$4L4.1174571@typhoon.austin.rr.com> <a90795$fhf$1@suaar1aa.prod.compuserve.com> <oJNs8.31397$4L4.1187353@typhoon.austin.rr.com> <a90fq3$qol$1@suaar1ac.prod.compuserve.com>`

```
Sorry I didn't reply this morning - I kind of crashed hard last night. :) 
As you suspected, there is some wierdness going on.  THe closest guess
I can get to this is that it thinks the VSAM file is an ESDS vice a KSDS
file. Huh...

Now  light begins to dawn... someone had replaced this file with a new version - 
naturally enough, they didn't tell anyone. (*sigh*) This leads me to some vauge
memory that you have to access empty VSAM files differently than you do a 
file that doesn't have any records. If that a false memory, or am I really remembering
something here? :) 


SDMR-STATUS      : 90                                               
SMDR-RETURN-CODE : 08                                               
SMDR-FUNCTION-CD : 0                                                
SMDR-FEEDBACK-CD : 072                                              
SMDR-RECORD      : 000000000103260346 000058 T038 006               
SMDRIN-REC       :  03/26 03:46  00:00:58 T038  006                 
                                                                    
-------------------------                                           
SDMR-STATUS      : 90                                               
SMDR-RETURN-CODE : 08                                               
SMDR-FUNCTION-CD : 0                                                
SMDR-FEEDBACK-CD : 072                                              
SMDR-RECORD      : 000000000203260349 000217 T038 006               
SMDRIN-REC       :  03/26 03:49  00:02:17 T038  006                 
                                                                    
-------------------------                                           
SDMR-STATUS      : 90                                               


[ IDCAMS job that created a test dataset to use for this  ] 

000020  DEFINE CLUSTER (NAME(PRAUL.PERM.JAZZ)                         - 
000021                  OWNER(PRAUL)                                  - 
000022                  INDEXED                                       - 
000023                  RECORDSIZE(88 88)                             - 
000024                  KEYS(10 0)                                    - 
000025                  VOLUMES(CICS01)                               - 
000029                  SHAREOPTIONS(2 3)                             - 
000031                  IMBED )                                       - 
000037         DATA    (NAME(PRAUL.PERM.JAZZ.DATA)                    - 
000038                  CYLINDERS(40 40)                              - 
000039                  CISZ(2048)                                    - 
000040                  )                                             - 
000049         INDEX   (NAME(PRAUL.PERM.JAZZ.INDEX)                   - 
000060                  )                                               


[






  "Ron" <NoSoy@swbell.net> wrote in message news:a90fq3$qol$1@suaar1ac.prod.compuserve.com...
  Oh great. File status 90 is one of those lovely codes defined as "No further
  information". Are there any messages on the job log that might give the 
  exact VSAM error? If not, you will have to go the next step and get the vsam 
  return codes as well, like this: 

  file status is vsam-status vsam-return.

  01  vsam-return-area.
      05 vsam-status pic xx. 
      05 vsam-return. 
          10 vsam-return-code pic 9(2) comp. 
          10 vsam-function-code pic 9(1) comp. 
          10 vsam-feedback-code pic 9(3) comp.  

  Then, oh joy, you have to go to the assembler vsam macro reference to interpret these 
  codes. Move these values to some usage display field and display them and let us know.
  I'll check in the morning. Does this file have any alternate indexes? I can't really tell
  beyond that without seeing the job, the program, jcl and cluster definition.

      
    "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:oJNs8.31397$4L4.1187353@typhoon.austin.rr.com...
    Boy- I am tired. The file opens with a status of 00, but each write it getting a status of 90. 
    90? 

    Thanks 
    -Paul

      "Ron" <NoSoy@swbell.net> wrote in message news:a90795$fhf$1@suaar1aa.prod.compuserve.com...
      I would suggest you put a file status in the select statement and
      check its value after the write (and open). Invalid key does not catch
      all the possible failure conditions. Let us know what happens.

      ===================================================================== 
        "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:jVMs8.31382$4L4.1174571@typhoon.austin.rr.com...
        under OS/390, Cobol 1.2.2, the following code is simply failing. 
        No indication of why, it simply doesn't write to the VSAM file it is supposed to 
        be writing to. 

        I'm in the middle of one of those marathon coding sessions right now, so I am probably too
        tired to really see what is going on. Anyone have any advice on this one? All this little segment
        of the application is doing is loading some records from a sequential file. 

        Thanks 
        -Paul

        000150              WRITE SMDR-RECORD                                        
        000151                INVALID KEY                                            
        000152                  DISPLAY '(1) ' WS-USER-COUNT1 ': FAILED RECORD'      
        000153                  DISPLAY '(F) ' SMDRIN-RECORD                         
        000154                  DISPLAY '(L) ' WS-LAST-SMDR-RECORD                   
        000155                  DISPLAY ' '                                          
        000156                  ADD 1 TO WS-USER-COUNT2                              
        000157                NOT INVALID KEY                                        
        000158                  MOVE SMDRIN-RECORD TO WS-LAST-SMDR-RECORD            
        000159                  ADD 1 TO WS-USER-COUNT3                              
        000160                  DISPLAY 'SMDRWRITE: ' SMDR-RECORD                    
        000161                END-WRITE                                              
        000162              READ SMDRIN NEXT RECORD                                  


        I put display statements just before and after the write, so I am sure the code is being hit. 
        I also displayed the SMDR-RECORD and it is being loaded correctly. 
        TKU! -Paul
```

###### ↳ ↳ ↳ Re: Write not happening?

_(reply depth: 5)_

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2002-04-10T22:15:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a92v4c$c7v$1@suaar1aa.prod.compuserve.com>`
- **References:** `<jVMs8.31382$4L4.1174571@typhoon.austin.rr.com> <a90795$fhf$1@suaar1aa.prod.compuserve.com> <oJNs8.31397$4L4.1187353@typhoon.austin.rr.com> <a90fq3$qol$1@suaar1ac.prod.compuserve.com> <ex4t8.34396$ud6.1295775@typhoon.austin.rr.com>`

```
This does seem like a very weird error. The manual gives this description: 
"You made a keyed request for access to an entry-sequenced data set.  Or,
you issued a GETIX or PUTIX to an entry-sequenced data set or fixed-length 
RRDS." 

It sounds like you just ran the idcams delete/define. You are right that 
vsam files in that state must be handled differently. If the file has just
been defined, in COBOL you can only ONLY open the file OUTPUT (NOT I-O). 
I suspect this is what is wrong. VSAM expects that the file will be loaded with
REPRO or with a program. If that's the case the error message would kind of
make sense because no index exists as yet. Once there is data in the file you
can open it I-O and do random updates. You cannot open a file for OUTPUT if 
data is already in it UNLESS it is defined with REUSE, in which case it would
write over the file. So if you have a freshly defined file and you're opening
I-O you need to put a record in it first with File-Aid or something. I usually
put a record with all low-values in the key.  

Now a few suggestions. If you need to initialize an empty file with a lot of data,
do it in load mode (OUTPUT). Sort the data in key sequence and load the file using
repro or sort or a program. It saves tons of time. Opening I-O and doing inserts
is dog slow. But, of course if what you're testing is random updates you can't do
that. I would also specifically allocate some index space CYLINDERS (5 2). I am not
sure of the default allocation and I just feel better knowing exactly what index is
going to be.      

Good Luck,
Ron
                                                

  "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:ex4t8.34396$ud6.1295775@typhoon.austin.rr.com...
  Sorry I didn't reply this morning - I kind of crashed hard last night. :) 
  As you suspected, there is some wierdness going on.  THe closest guess
  I can get to this is that it thinks the VSAM file is an ESDS vice a KSDS
  file. Huh...

  Now  light begins to dawn... someone had replaced this file with a new version - 
  naturally enough, they didn't tell anyone. (*sigh*) This leads me to some vauge
  memory that you have to access empty VSAM files differently than you do a 
  file that doesn't have any records. If that a false memory, or am I really remembering
  something here? :) 


  SDMR-STATUS      : 90                                               
  SMDR-RETURN-CODE : 08                                               
  SMDR-FUNCTION-CD : 0                                                
  SMDR-FEEDBACK-CD : 072                                              
  SMDR-RECORD      : 000000000103260346 000058 T038 006               
  SMDRIN-REC       :  03/26 03:46  00:00:58 T038  006                 
                                                                      
  -------------------------                                           
  SDMR-STATUS      : 90                                               
  SMDR-RETURN-CODE : 08                                               
  SMDR-FUNCTION-CD : 0                                                
  SMDR-FEEDBACK-CD : 072                                              
  SMDR-RECORD      : 000000000203260349 000217 T038 006               
  SMDRIN-REC       :  03/26 03:49  00:02:17 T038  006                 
                                                                      
  -------------------------                                           
  SDMR-STATUS      : 90                                               


  [ IDCAMS job that created a test dataset to use for this  ] 

  000020  DEFINE CLUSTER (NAME(PRAUL.PERM.JAZZ)                         - 
  000021                  OWNER(PRAUL)                                  - 
  000022                  INDEXED                                       - 
  000023                  RECORDSIZE(88 88)                             - 
  000024                  KEYS(10 0)                                    - 
  000025                  VOLUMES(CICS01)                               - 
  000029                  SHAREOPTIONS(2 3)                             - 
  000031                  IMBED )                                       - 
  000037         DATA    (NAME(PRAUL.PERM.JAZZ.DATA)                    - 
  000038                  CYLINDERS(40 40)                              - 
  000039                  CISZ(2048)                                    - 
  000040                  )                                             - 
  000049         INDEX   (NAME(PRAUL.PERM.JAZZ.INDEX)                   - 
  000060                  )                                               


  [






    "Ron" <NoSoy@swbell.net> wrote in message news:a90fq3$qol$1@suaar1ac.prod.compuserve.com...
    Oh great. File status 90 is one of those lovely codes defined as "No further
    information". Are there any messages on the job log that might give the 
    exact VSAM error? If not, you will have to go the next step and get the vsam 
    return codes as well, like this: 

    file status is vsam-status vsam-return.

    01  vsam-return-area.
        05 vsam-status pic xx. 
        05 vsam-return. 
            10 vsam-return-code pic 9(2) comp. 
            10 vsam-function-code pic 9(1) comp. 
            10 vsam-feedback-code pic 9(3) comp.  

    Then, oh joy, you have to go to the assembler vsam macro reference to interpret these 
    codes. Move these values to some usage display field and display them and let us know.
    I'll check in the morning. Does this file have any alternate indexes? I can't really tell
    beyond that without seeing the job, the program, jcl and cluster definition.

        
      "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:oJNs8.31397$4L4.1187353@typhoon.austin.rr.com...
      Boy- I am tired. The file opens with a status of 00, but each write it getting a status of 90. 
      90? 

      Thanks 
      -Paul

        "Ron" <NoSoy@swbell.net> wrote in message news:a90795$fhf$1@suaar1aa.prod.compuserve.com...
        I would suggest you put a file status in the select statement and
        check its value after the write (and open). Invalid key does not catch
        all the possible failure conditions. Let us know what happens.

        ===================================================================== 
          "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:jVMs8.31382$4L4.1174571@typhoon.austin.rr.com...
          under OS/390, Cobol 1.2.2, the following code is simply failing. 
          No indication of why, it simply doesn't write to the VSAM file it is supposed to 
          be writing to. 

          I'm in the middle of one of those marathon coding sessions right now, so I am probably too
          tired to really see what is going on. Anyone have any advice on this one? All this little segment
          of the application is doing is loading some records from a sequential file. 

          Thanks 
          -Paul

          000150              WRITE SMDR-RECORD                                        
          000151                INVALID KEY                                            
          000152                  DISPLAY '(1) ' WS-USER-COUNT1 ': FAILED RECORD'      
          000153                  DISPLAY '(F) ' SMDRIN-RECORD                         
          000154                  DISPLAY '(L) ' WS-LAST-SMDR-RECORD                   
          000155                  DISPLAY ' '                                          
          000156                  ADD 1 TO WS-USER-COUNT2                              
          000157                NOT INVALID KEY                                        
          000158                  MOVE SMDRIN-RECORD TO WS-LAST-SMDR-RECORD            
          000159                  ADD 1 TO WS-USER-COUNT3                              
          000160                  DISPLAY 'SMDRWRITE: ' SMDR-RECORD                    
          000161                END-WRITE                                              
          000162              READ SMDRIN NEXT RECORD                                  


          I put display statements just before and after the write, so I am sure the code is being hit. 
          I also displayed the SMDR-RECORD and it is being loaded correctly. 
          TKU! -Paul
```

###### ↳ ↳ ↳ Re: Write not happening?

_(reply depth: 6)_

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-11T03:27:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Bo7t8.35656$ud6.1380194@typhoon.austin.rr.com>`
- **References:** `<jVMs8.31382$4L4.1174571@typhoon.austin.rr.com> <a90795$fhf$1@suaar1aa.prod.compuserve.com> <oJNs8.31397$4L4.1187353@typhoon.austin.rr.com> <a90fq3$qol$1@suaar1ac.prod.compuserve.com> <ex4t8.34396$ud6.1295775@typhoon.austin.rr.com> <a92v4c$c7v$1@suaar1aa.prod.compuserve.com>`

```
And that is pretty much exactly what the issue was. OUTPUT worked on the test file, so I deleted and 
recreated the production file, and it loaded just fine. (*sigh*) Boy, I feel pretty stupid sometimes. 
Guess it comes from switching languages and platforms 5-6 times per day. 

Thanks for the help, I really appreciate it. :) :) :) 

-Paul

  "Ron" <NoSoy@swbell.net> wrote in message news:a92v4c$c7v$1@suaar1aa.prod.compuserve.com...
  This does seem like a very weird error. The manual gives this description: 
  "You made a keyed request for access to an entry-sequenced data set.  Or,
  you issued a GETIX or PUTIX to an entry-sequenced data set or fixed-length 
  RRDS." 

  It sounds like you just ran the idcams delete/define. You are right that 
  vsam files in that state must be handled differently. If the file has just
  been defined, in COBOL you can only ONLY open the file OUTPUT (NOT I-O). 
  I suspect this is what is wrong. VSAM expects that the file will be loaded with
  REPRO or with a program. If that's the case the error message would kind of
  make sense because no index exists as yet. Once there is data in the file you
  can open it I-O and do random updates. You cannot open a file for OUTPUT if 
  data is already in it UNLESS it is defined with REUSE, in which case it would
  write over the file. So if you have a freshly defined file and you're opening
  I-O you need to put a record in it first with File-Aid or something. I usually
  put a record with all low-values in the key.  

  Now a few suggestions. If you need to initialize an empty file with a lot of data,
  do it in load mode (OUTPUT). Sort the data in key sequence and load the file using
  repro or sort or a program. It saves tons of time. Opening I-O and doing inserts
  is dog slow. But, of course if what you're testing is random updates you can't do
  that. I would also specifically allocate some index space CYLINDERS (5 2). I am not
  sure of the default allocation and I just feel better knowing exactly what index is
  going to be.      

  Good Luck,
  Ron
                                                  

    "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:ex4t8.34396$ud6.1295775@typhoon.austin.rr.com...
    Sorry I didn't reply this morning - I kind of crashed hard last night. :) 
    As you suspected, there is some wierdness going on.  THe closest guess
    I can get to this is that it thinks the VSAM file is an ESDS vice a KSDS
    file. Huh...

    Now  light begins to dawn... someone had replaced this file with a new version - 
    naturally enough, they didn't tell anyone. (*sigh*) This leads me to some vauge
    memory that you have to access empty VSAM files differently than you do a 
    file that doesn't have any records. If that a false memory, or am I really remembering
    something here? :) 


    SDMR-STATUS      : 90                                               
    SMDR-RETURN-CODE : 08                                               
    SMDR-FUNCTION-CD : 0                                                
    SMDR-FEEDBACK-CD : 072                                              
    SMDR-RECORD      : 000000000103260346 000058 T038 006               
    SMDRIN-REC       :  03/26 03:46  00:00:58 T038  006                 
                                                                        
    -------------------------                                           
    SDMR-STATUS      : 90                                               
    SMDR-RETURN-CODE : 08                                               
    SMDR-FUNCTION-CD : 0                                                
    SMDR-FEEDBACK-CD : 072                                              
    SMDR-RECORD      : 000000000203260349 000217 T038 006               
    SMDRIN-REC       :  03/26 03:49  00:02:17 T038  006                 
                                                                        
    -------------------------                                           
    SDMR-STATUS      : 90                                               


    [ IDCAMS job that created a test dataset to use for this  ] 

    000020  DEFINE CLUSTER (NAME(PRAUL.PERM.JAZZ)                         - 
    000021                  OWNER(PRAUL)                                  - 
    000022                  INDEXED                                       - 
    000023                  RECORDSIZE(88 88)                             - 
    000024                  KEYS(10 0)                                    - 
    000025                  VOLUMES(CICS01)                               - 
    000029                  SHAREOPTIONS(2 3)                             - 
    000031                  IMBED )                                       - 
    000037         DATA    (NAME(PRAUL.PERM.JAZZ.DATA)                    - 
    000038                  CYLINDERS(40 40)                              - 
    000039                  CISZ(2048)                                    - 
    000040                  )                                             - 
    000049         INDEX   (NAME(PRAUL.PERM.JAZZ.INDEX)                   - 
    000060                  )                                               


    [






      "Ron" <NoSoy@swbell.net> wrote in message news:a90fq3$qol$1@suaar1ac.prod.compuserve.com...
      Oh great. File status 90 is one of those lovely codes defined as "No further
      information". Are there any messages on the job log that might give the 
      exact VSAM error? If not, you will have to go the next step and get the vsam 
      return codes as well, like this: 

      file status is vsam-status vsam-return.

      01  vsam-return-area.
          05 vsam-status pic xx. 
          05 vsam-return. 
              10 vsam-return-code pic 9(2) comp. 
              10 vsam-function-code pic 9(1) comp. 
              10 vsam-feedback-code pic 9(3) comp.  

      Then, oh joy, you have to go to the assembler vsam macro reference to interpret these 
      codes. Move these values to some usage display field and display them and let us know.
      I'll check in the morning. Does this file have any alternate indexes? I can't really tell
      beyond that without seeing the job, the program, jcl and cluster definition.

          
        "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:oJNs8.31397$4L4.1187353@typhoon.austin.rr.com...
        Boy- I am tired. The file opens with a status of 00, but each write it getting a status of 90. 
        90? 

        Thanks 
        -Paul

          "Ron" <NoSoy@swbell.net> wrote in message news:a90795$fhf$1@suaar1aa.prod.compuserve.com...
          I would suggest you put a file status in the select statement and
          check its value after the write (and open). Invalid key does not catch
          all the possible failure conditions. Let us know what happens.

          ===================================================================== 
            "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:jVMs8.31382$4L4.1174571@typhoon.austin.rr.com...
            under OS/390, Cobol 1.2.2, the following code is simply failing. 
            No indication of why, it simply doesn't write to the VSAM file it is supposed to 
            be writing to. 

            I'm in the middle of one of those marathon coding sessions right now, so I am probably too
            tired to really see what is going on. Anyone have any advice on this one? All this little segment
            of the application is doing is loading some records from a sequential file. 

            Thanks 
            -Paul

            000150              WRITE SMDR-RECORD                                        
            000151                INVALID KEY                                            
            000152                  DISPLAY '(1) ' WS-USER-COUNT1 ': FAILED RECORD'      
            000153                  DISPLAY '(F) ' SMDRIN-RECORD                         
            000154                  DISPLAY '(L) ' WS-LAST-SMDR-RECORD                   
            000155                  DISPLAY ' '                                          
            000156                  ADD 1 TO WS-USER-COUNT2                              
            000157                NOT INVALID KEY                                        
            000158                  MOVE SMDRIN-RECORD TO WS-LAST-SMDR-RECORD            
            000159                  ADD 1 TO WS-USER-COUNT3                              
            000160                  DISPLAY 'SMDRWRITE: ' SMDR-RECORD                    
            000161                END-WRITE                                              
            000162              READ SMDRIN NEXT RECORD                                  


            I put display statements just before and after the write, so I am sure the code is being hit. 
            I also displayed the SMDR-RECORD and it is being loaded correctly. 
            TKU! -Paul
```

###### ↳ ↳ ↳ Re: Write not happening?

_(reply depth: 7)_

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2002-04-11T12:43:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a94i06$eo4$1@suaar1ac.prod.compuserve.com>`
- **References:** `<jVMs8.31382$4L4.1174571@typhoon.austin.rr.com> <a90795$fhf$1@suaar1aa.prod.compuserve.com> <oJNs8.31397$4L4.1187353@typhoon.austin.rr.com> <a90fq3$qol$1@suaar1ac.prod.compuserve.com> <ex4t8.34396$ud6.1295775@typhoon.austin.rr.com> <a92v4c$c7v$1@suaar1aa.prod.compuserve.com> <Bo7t8.35656$ud6.1380194@typhoon.austin.rr.com>`

```
You are welcome. I am glad you found the answer. 

Ron
  "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:Bo7t8.35656$ud6.1380194@typhoon.austin.rr.com...
  And that is pretty much exactly what the issue was. OUTPUT worked on the test file, so I deleted and 
  recreated the production file, and it loaded just fine. (*sigh*) Boy, I feel pretty stupid sometimes. 
  Guess it comes from switching languages and platforms 5-6 times per day. 

  Thanks for the help, I really appreciate it. :) :) :) 

  -Paul

    "Ron" <NoSoy@swbell.net> wrote in message news:a92v4c$c7v$1@suaar1aa.prod.compuserve.com...
    This does seem like a very weird error. The manual gives this description: 
    "You made a keyed request for access to an entry-sequenced data set.  Or,
    you issued a GETIX or PUTIX to an entry-sequenced data set or fixed-length 
    RRDS." 

    It sounds like you just ran the idcams delete/define. You are right that 
    vsam files in that state must be handled differently. If the file has just
    been defined, in COBOL you can only ONLY open the file OUTPUT (NOT I-O). 
    I suspect this is what is wrong. VSAM expects that the file will be loaded with
    REPRO or with a program. If that's the case the error message would kind of
    make sense because no index exists as yet. Once there is data in the file you
    can open it I-O and do random updates. You cannot open a file for OUTPUT if 
    data is already in it UNLESS it is defined with REUSE, in which case it would
    write over the file. So if you have a freshly defined file and you're opening
    I-O you need to put a record in it first with File-Aid or something. I usually
    put a record with all low-values in the key.  

    Now a few suggestions. If you need to initialize an empty file with a lot of data,
    do it in load mode (OUTPUT). Sort the data in key sequence and load the file using
    repro or sort or a program. It saves tons of time. Opening I-O and doing inserts
    is dog slow. But, of course if what you're testing is random updates you can't do
    that. I would also specifically allocate some index space CYLINDERS (5 2). I am not
    sure of the default allocation and I just feel better knowing exactly what index is
    going to be.      

    Good Luck,
    Ron
                                                    

      "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:ex4t8.34396$ud6.1295775@typhoon.austin.rr.com...
      Sorry I didn't reply this morning - I kind of crashed hard last night. :) 
      As you suspected, there is some wierdness going on.  THe closest guess
      I can get to this is that it thinks the VSAM file is an ESDS vice a KSDS
      file. Huh...

      Now  light begins to dawn... someone had replaced this file with a new version - 
      naturally enough, they didn't tell anyone. (*sigh*) This leads me to some vauge
      memory that you have to access empty VSAM files differently than you do a 
      file that doesn't have any records. If that a false memory, or am I really remembering
      something here? :) 


      SDMR-STATUS      : 90                                               
      SMDR-RETURN-CODE : 08                                               
      SMDR-FUNCTION-CD : 0                                                
      SMDR-FEEDBACK-CD : 072                                              
      SMDR-RECORD      : 000000000103260346 000058 T038 006               
      SMDRIN-REC       :  03/26 03:46  00:00:58 T038  006                 
                                                                          
      -------------------------                                           
      SDMR-STATUS      : 90                                               
      SMDR-RETURN-CODE : 08                                               
      SMDR-FUNCTION-CD : 0                                                
      SMDR-FEEDBACK-CD : 072                                              
      SMDR-RECORD      : 000000000203260349 000217 T038 006               
      SMDRIN-REC       :  03/26 03:49  00:02:17 T038  006                 
                                                                          
      -------------------------                                           
      SDMR-STATUS      : 90                                               


      [ IDCAMS job that created a test dataset to use for this  ] 

      000020  DEFINE CLUSTER (NAME(PRAUL.PERM.JAZZ)                         - 
      000021                  OWNER(PRAUL)                                  - 
      000022                  INDEXED                                       - 
      000023                  RECORDSIZE(88 88)                             - 
      000024                  KEYS(10 0)                                    - 
      000025                  VOLUMES(CICS01)                               - 
      000029                  SHAREOPTIONS(2 3)                             - 
      000031                  IMBED )                                       - 
      000037         DATA    (NAME(PRAUL.PERM.JAZZ.DATA)                    - 
      000038                  CYLINDERS(40 40)                              - 
      000039                  CISZ(2048)                                    - 
      000040                  )                                             - 
      000049         INDEX   (NAME(PRAUL.PERM.JAZZ.INDEX)                   - 
      000060                  )                                               


      [






        "Ron" <NoSoy@swbell.net> wrote in message news:a90fq3$qol$1@suaar1ac.prod.compuserve.com...
        Oh great. File status 90 is one of those lovely codes defined as "No further
        information". Are there any messages on the job log that might give the 
        exact VSAM error? If not, you will have to go the next step and get the vsam 
        return codes as well, like this: 

        file status is vsam-status vsam-return.

        01  vsam-return-area.
            05 vsam-status pic xx. 
            05 vsam-return. 
                10 vsam-return-code pic 9(2) comp. 
                10 vsam-function-code pic 9(1) comp. 
                10 vsam-feedback-code pic 9(3) comp.  

        Then, oh joy, you have to go to the assembler vsam macro reference to interpret these 
        codes. Move these values to some usage display field and display them and let us know.
        I'll check in the morning. Does this file have any alternate indexes? I can't really tell
        beyond that without seeing the job, the program, jcl and cluster definition.

            
          "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:oJNs8.31397$4L4.1187353@typhoon.austin.rr.com...
          Boy- I am tired. The file opens with a status of 00, but each write it getting a status of 90. 
          90? 

          Thanks 
          -Paul

            "Ron" <NoSoy@swbell.net> wrote in message news:a90795$fhf$1@suaar1aa.prod.compuserve.com...
            I would suggest you put a file status in the select statement and
            check its value after the write (and open). Invalid key does not catch
            all the possible failure conditions. Let us know what happens.

            ===================================================================== 
              "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com> wrote in message news:jVMs8.31382$4L4.1174571@typhoon.austin.rr.com...
              under OS/390, Cobol 1.2.2, the following code is simply failing. 
              No indication of why, it simply doesn't write to the VSAM file it is supposed to 
              be writing to. 

              I'm in the middle of one of those marathon coding sessions right now, so I am probably too
              tired to really see what is going on. Anyone have any advice on this one? All this little segment
              of the application is doing is loading some records from a sequential file. 

              Thanks 
              -Paul

              000150              WRITE SMDR-RECORD                                        
              000151                INVALID KEY                                            
              000152                  DISPLAY '(1) ' WS-USER-COUNT1 ': FAILED RECORD'      
              000153                  DISPLAY '(F) ' SMDRIN-RECORD                         
              000154                  DISPLAY '(L) ' WS-LAST-SMDR-RECORD                   
              000155                  DISPLAY ' '                                          
              000156                  ADD 1 TO WS-USER-COUNT2                              
              000157                NOT INVALID KEY                                        
              000158                  MOVE SMDRIN-RECORD TO WS-LAST-SMDR-RECORD            
              000159                  ADD 1 TO WS-USER-COUNT3                              
              000160                  DISPLAY 'SMDRWRITE: ' SMDR-RECORD                    
              000161                END-WRITE                                              
              000162              READ SMDRIN NEXT RECORD                                  


              I put display statements just before and after the write, so I am sure the code is being hit. 
              I also displayed the SMDR-RECORD and it is being loaded correctly. 
              TKU! -Paul
```

###### ↳ ↳ ↳ Re: Write not happening?

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-04-11T11:52:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GNet8.3672$w31.447@nwrddc01.gnilink.net>`
- **References:** `<jVMs8.31382$4L4.1174571@typhoon.austin.rr.com> <a90795$fhf$1@suaar1aa.prod.compuserve.com> <oJNs8.31397$4L4.1187353@typhoon.austin.rr.com> <a90fq3$qol$1@suaar1ac.prod.compuserve.com> <ex4t8.34396$ud6.1295775@typhoon.austin.rr.com> <a92v4c$c7v$1@suaar1aa.prod.compuserve.com>`

```
Ron <NoSoy@swbell.net> wrote in message
news:a92v4c$c7v$1@suaar1aa.prod.compuserve.com...
>It sounds like you just ran the idcams delete/define. You are right that
>vsam files in that state must be handled differently. If the file has just
>been defined, in COBOL you can only ONLY open the file OUTPUT (NOT I-O).

What I do when I am working with VSAM files subject to periodic
DELETE/DEFINE (which is darn near any VSAM file from which DELETEs are done)
is OPEN the file I-O and interrogate the status. If the open fails, I open
it OUTPUT, CLOSE it, then OPEN it I-O.

If OPEN fails now, the problem is *NOT*  a 'virgin'  status and I give up.
If the OPEN succeeds the second time, all is well.

Why screw around with File-Aid or REPRO when you can handle it in your COBOL
code?

MCM
```

###### ↳ ↳ ↳ Re: Write not happening?

_(reply depth: 7)_

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2002-04-11T12:46:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a94i65$39g$1@suaar1ab.prod.compuserve.com>`
- **References:** `<jVMs8.31382$4L4.1174571@typhoon.austin.rr.com> <a90795$fhf$1@suaar1aa.prod.compuserve.com> <oJNs8.31397$4L4.1187353@typhoon.austin.rr.com> <a90fq3$qol$1@suaar1ac.prod.compuserve.com> <ex4t8.34396$ud6.1295775@typhoon.austin.rr.com> <a92v4c$c7v$1@suaar1aa.prod.compuserve.com> <GNet8.3672$w31.447@nwrddc01.gnilink.net>`

```
You are right. That is a good solution in a production environment. I was
specifically referring to using File-Aid or REPRO in a one-time or testing/debugging
situation to facilitate locating the problem we were discussing.



"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:GNet8.3672$w31.447@nwrddc01.gnilink.net...
> Ron <NoSoy@swbell.net> wrote in message
> news:a92v4c$c7v$1@suaar1aa.prod.compuserve.com...
…[20 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
