[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Acessing "RETURN-CODE" register

_10 messages · 7 participants · 2001-09_

---

### Acessing "RETURN-CODE" register

- **From:** mshetty@mail.com (mshetty)
- **Date:** 2001-09-15T05:50:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfbb8fd4.0109150450.375d8cc4@posting.google.com>`

```
Hi,

I am invoking a COBOL subprogram in my C prog. I am able to access the
value of "RETURN-CODE" if the COBOL prog terminates normally.

But if my COBOL prog throws a DIVDE BY ZERO error, the control does
not return to the calling C program.

Following is the error thrown by COBOL
**********************************************************************
KCCB0002R-S(1)
A divide exception occurred in a numeric item.
Program-name = CBL_QUERYBOOKNAME
Line number / column = 000012/09

**********************************************************************

Please let me know if there is a way to return control to the calling
C prog so, that appropriate action can be taken.

My COBOL sub-program ends with an -EXIT PROGRAM statement.

Thanks and Regards,
M Shetty
```

#### ↳ Re: Acessing "RETURN-CODE" register

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2001-09-15T15:32:36+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3vl6qt4c9krfole3gf4culhpl82ltq0790@4ax.com>`
- **References:** `<bfbb8fd4.0109150450.375d8cc4@posting.google.com>`

```
On 15 Sep 2001 05:50:26 -0700, mshetty@mail.com (mshetty) wrote:

>Hi,
>
…[12 more quoted lines elided]…
>M Shetty


In the sub-program:

IF DIVISOR =0 THEN
   MOVE 12 TO RETURN-CODE
   GOBACK
ELSE
   COMPUTE My-result = Divident / Divisor
END-IF


                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      God does not play dice with the universe.
      
        (Another Wisdom from my fortune cookie jar)         
______________________________________________________________________________
Posted Via Binaries.net = SPEED+RETENTION+COMPLETION = http://www.binaries.net
```

#### ↳ Re: Acessing "RETURN-CODE" register

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2001-09-15T15:36:44+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n7m6qt4ttfnbg4mgd16ose1slqhjqb4ne3@4ax.com>`
- **References:** `<bfbb8fd4.0109150450.375d8cc4@posting.google.com>`

```
Another option (in the sub-program)

COMPUTE My-result = Dividend / Divisor
   ON SIZE ERROR
      MOVE 12 TO RETURN-CODE
      DISPLAY ' There was a division by zero
      GOBACK
END-COMPUTE


On 15 Sep 2001 05:50:26 -0700, mshetty@mail.com (mshetty) wrote:

>Hi,
>
…[12 more quoted lines elided]…
>M Shetty


                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      You are secretive in your dealings but never to the extent of trickery.
      
        (Another Wisdom from my fortune cookie jar)         
______________________________________________________________________________
Posted Via Binaries.net = SPEED+RETENTION+COMPLETION = http://www.binaries.net
```

#### ↳ Re: Acessing "RETURN-CODE" register

- **From:** "JerryP" <news@bisusa.com>
- **Date:** 2001-09-15T14:29:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EBJo7.297688$VV1.21911935@bin1.nnrp.aus1.giganews.com>`
- **References:** `<bfbb8fd4.0109150450.375d8cc4@posting.google.com>`

```
IF MY-DIVISOR = 0
    MOVE 999 TO RETURN-CODE
   EXIT PROGRAM.


"mshetty" <mshetty@mail.com> wrote in message
news:bfbb8fd4.0109150450.375d8cc4@posting.google.com...
> Hi,
>
…[22 more quoted lines elided]…
>
```

#### ↳ Re: Acessing "RETURN-CODE" register

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-09-15T17:02:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wQLo7.518$QO1.92157@dfiatx1-snr1.gtei.net>`
- **References:** `<bfbb8fd4.0109150450.375d8cc4@posting.google.com>`

```
mshetty <mshetty@mail.com> wrote in message
news:bfbb8fd4.0109150450.375d8cc4@posting.google.com...
> Hi,
>
…[7 more quoted lines elided]…
> C prog so, that appropriate action can be taken.


    DIVIDE X INTO Y
        ON SIZE ERROR
           MOVE 1234 TO RETURN-CODE
           EXIT PROGRAM
    END-DIVIDE

MCM
```

#### ↳ Re: Acessing "RETURN-CODE" register

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2001-09-16T00:13:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9o1c10$ad6ja$1@ID-39920.news.dfncis.de>`
- **References:** `<bfbb8fd4.0109150450.375d8cc4@posting.google.com>`

```

mshetty <mshetty@mail.com> wrote in message
news:bfbb8fd4.0109150450.375d8cc4@posting.google.com...
> Hi,
>
…[21 more quoted lines elided]…
> M Shetty

You have to catch it before the ABEND.  You can do this several ways, but
the easiest is to either check your divisor (if statement) or use ON SIZE
ERROR on the DIVIDE/COMPUTE statement.  Either way, you will have to set a
return code for you calling program to find.

1)  IF divisor = ZERO
        MOVE number TO RETURN-CODE
        GOBACK
     END-IF.
     DIVIDE field-a BY divisor .....

2)  DIVIDE field-a BY divisor
         ON SIZE ERROR
              MOVE number TO RETURN-CODE
              GOBACK.
     ..........


Hope this helps,
Dave
```

##### ↳ ↳ Re: Acessing "RETURN-CODE" register

- **From:** mshetty@mail.com (mshetty)
- **Date:** 2001-09-20T06:37:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfbb8fd4.0109200537.8daa020@posting.google.com>`
- **References:** `<bfbb8fd4.0109150450.375d8cc4@posting.google.com> <9o1c10$ad6ja$1@ID-39920.news.dfncis.de>`

```
"DBuck" <dbuck@prairieinet.net> wrote in message news:<9o1c10$ad6ja$1@ID-39920.news.dfncis.de>...
> mshetty <mshetty@mail.com> wrote in message
> news:bfbb8fd4.0109150450.375d8cc4@posting.google.com...
…[44 more quoted lines elided]…
> Dave

Can I access the "RETURN-CODE" register in a shell script of UNIX ??
```

#### ↳ Re: Acessing "RETURN-CODE" register

- **From:** "Rick Price" <rick@hpdsoftware.com>
- **Date:** 2001-09-17T15:51:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9o52ek$ar3oq$1@ID-39799.news.dfncis.de>`
- **References:** `<bfbb8fd4.0109150450.375d8cc4@posting.google.com>`

```
One possible technique if you only have one good exit is to make that return
a specific non zero RETURN-CODE.  Then that value can be used to show a good
return and anything else (including zero) means there was an error.

mshetty <mshetty@mail.com> wrote in message
news:bfbb8fd4.0109150450.375d8cc4@posting.google.com...
> Hi,
>
…[21 more quoted lines elided]…
> M Shetty
```

##### ↳ ↳ Re: Acessing "RETURN-CODE" register

- **From:** "Rick Price" <rick@hpdsoftware.com>
- **Date:** 2001-09-17T16:14:49+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9o53q4$b5l0v$1@ID-39799.news.dfncis.de>`
- **References:** `<bfbb8fd4.0109150450.375d8cc4@posting.google.com> <9o52ek$ar3oq$1@ID-39799.news.dfncis.de>`

```
Whoops! You say that your calling C program doesn't get control after the
error, so this won't work.  I'll have to learn to read.  Sorry!

Rick Price <rick@hpdsoftware.com> wrote in message
news:9o52ek$ar3oq$1@ID-39799.news.dfncis.de...
> One possible technique if you only have one good exit is to make that
return
> a specific non zero RETURN-CODE.  Then that value can be used to show a
good
> return and anything else (including zero) means there was an error.
>
…[27 more quoted lines elided]…
>
```

#### ↳ Re: Acessing

- **From:** Daniel Jacot<daniel.jacot@winterthur.ch>
- **Date:** 2001-09-18T07:17:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<byCp7.3857$p77.11319@www.newsranger.com>`
- **References:** `<bfbb8fd4.0109150450.375d8cc4@posting.google.com>`

```
Hi M,

I am not aware on which platform you are programming and what versions of C and
COBOL you are using. Please have a look in your current COBOL programming guide.
I'd guess that you are allowed to use the 'ON SIZE ERROR' phrase in your DIVIDE
statements:

Try the following little program on your system which obviously makes no sense,
but should run and give you a return-code of 111 instead of an abort:

IDENTIFICATION DIVISION.                     
PROGRAM-ID. DIVIDE-ERROR.                  
DATA DIVISION.                               
WORKING-STORAGE SECTION.                    
01 DIVISOR  PIC S9(5) COMP-3 VALUE ZERO.   
01 DIVIDEND PIC S9(5) COMP-3 VALUE ZERO.   
01 RESULT   PIC S9(5) COMP-3 VALUE ZERO.   
PROCEDURE DIVISION.                          
MAIN SECTION.                                
DIVIDE DIVIDEND BY DIVISOR GIVING RESULT 
ON SIZE ERROR PERFORM S10-DIVIDE-ERROR  
NOT ON SIZE ERROR CONTINUE              
END-DIVIDE                               
GOBACK.                                  
S10-DIVIDE-ERROR SECTION.                    
MOVE 111 TO RETURN-CODE               
GOBACK.                                  
END PROGRAM DIVIDE-ERROR.                    

On 15 Sep 2001 05:50:26 -0700, in article
<bfbb8fd4.0109150450.375d8cc4@posting.google.com>, mshetty stated...
>
>Hi,
…[22 more quoted lines elided]…
>M Shetty

-------------------------------------------------
With kind regards
Daniel Jacot
-------------------------------------------------
visit us at: http://www.winterthur.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
