[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Difficulty using DFSORT with packed decimal fields

_3 messages · 3 participants · 2003-10_

---

### Difficulty using DFSORT with packed decimal fields

- **From:** gelewyc@nyct.com (george lewycky)
- **Date:** 2003-10-23T13:04:33-07:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<68aecc05.0310231204.5c660c8f@posting.google.com>`

```
I am having difficulty with the field   JOB-STATUS-DATE
which is a packed decimal field. 
Using DFSORT I am trying to select records greater than 37600


using file-aid I mapped a sample record

 File-AID - Browse - TC.BGLPROD.TABLES.CL --------
 COMMAND ===> show p(icture)                              
 RECORD: 19063                      JOB-RECORD    
 ---- FIELD LEVEL/NAME ------- PICTURE- ----+----1
   10 JOB-CONT-PHONE-EXCHANGE  999      243       
   10 JOB-CONT-PHONE-NUMBER    9(4)     3044      
 5 JOB-PROGRAM-DESCRIPTION     X(40)              
 5 JOB-BILLING-CRED-DATE       9(5)     37893     
 5 JOB-STATUS-DATE             9(5)     37767     
 5 JOB-DEFAULT-INDICATOR       X    
****************************** BOTTOM OF DATA **              

 File-AID - Browse - TC.BGLPROD.TABLES.CL -------
 COMMAND ===> show f(ormat)                                     
 RECORD: 19063                      JOB-RECORD   
 ---- FIELD LEVEL/NAME ------- -FORMAT- ----+----
   10 JOB-CONT-PHONE-EXCHANGE    3/NUM  243      
   10 JOB-CONT-PHONE-NUMBER      4/NUM  3044     
 5 JOB-PROGRAM-DESCRIPTION      40/AN            
 5 JOB-BILLING-CRED-DATE         3/P    37893    
 5 JOB-STATUS-DATE               3/P    37767    
 5 JOB-DEFAULT-INDICATOR         1/AN            
 ****************************** BOTTOM OF DATA **


 File-AID - Browse - TC.BGLPROD.TABLES.CL 
 COMMAND ===>                                              
----+----7----+----8----+----9----+----0----+----1----+----
82433044                                         i   @     
FFFFFFFF44444444444444444444444444444444444444443833774   <-------
37767C  82433044000000000000000000000000000000000000000079F76C0


Selecting the records using FILE-AID works correctly using 
this criteria: 

                                             
    AND                                      
Cmd /OR Position Length RO                   
--- --- -------- ------ -- ------------------
___      1              EQ T'job'            
___ AND  512            GT X'37600C'         


Below is the DFSORT card. The last condition is where I'm having 
difficulty. I've tried many variations but had no luck. Also
IBM, Quickref, etc dont have samples for the PACKED DECIMAL format


//SYSIN    DD  *                                                  
 SORT FIELDS=COPY                                                 
 INCLUDE COND=(1,3,CH,EQ,C'JOB',AND,88,1,CH,NE,C'C',AND,          
   (11,3,CH,NE,C'ADJ',OR,11,3,CH,NE,C'OMB'),AND,85,4,PD,GT,37600)
<=========
 OUTREC FIELDS=(1,7,C'","',11,5,C'","',28,40,C'",',20X)           


I've tried these variations with no success:

85,4,PD,GT,c'37600C'
85,4,PD,GT,x'37600C' 
85,4,PD,GT,p'37600C' 
85,4,PD,GT,p'37600' 
85,4,PD,GT,37600
85,5,PD,GT,37600 


If anyone has any sample JCL, suggestions, ideas I'd
really appreciate it

Thanks in Advance

George Lewycky
NY CITY TRANSIT
Brooklyn NY  USA
gelewyc@nyct.com
```

#### ↳ Re: Difficulty using DFSORT with packed decimal fields

- **From:** docdwarf@panix.com
- **Date:** 2003-10-23T16:48:09-04:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<bn9eq9$pfk$1@panix1.panix.com>`
- **References:** `<68aecc05.0310231204.5c660c8f@posting.google.com>`

```
In article <68aecc05.0310231204.5c660c8f@posting.google.com>,
george lewycky <gelewyc@nyct.com> wrote:
>I am having difficulty with the field   JOB-STATUS-DATE
>which is a packed decimal field. 

[snip]

>    AND                                      
>Cmd /OR Position Length RO                   
>--- --- -------- ------ -- ------------------
>___      1              EQ T'job'            
>___ AND  512            GT X'37600C'         

[snip]

>//SYSIN    DD  *                                                  
> SORT FIELDS=COPY                                                 
> INCLUDE COND=(1,3,CH,EQ,C'JOB',AND,88,1,CH,NE,C'C',AND,          
>   (11,3,CH,NE,C'ADJ',OR,11,3,CH,NE,C'OMB'),AND,85,4,PD,GT,37600)

Might it make a difference that in FileAid you are pointing to position 
512 and in SyncSort to position 85?

DD
```

#### ↳ Re: Difficulty using DFSORT with packed decimal fields

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-10-23T21:36:26+00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<uRXlb.12148$Ec1.1092878@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<68aecc05.0310231204.5c660c8f@posting.google.com>`

```

george lewycky <gelewyc@nyct.com> wrote in message news:68aecc05.0310231204.5c660c8f@posting.google.com...
> I am having difficulty with the field   JOB-STATUS-DATE
> which is a packed decimal field.
…[30 more quoted lines elided]…
> gelewyc@nyct.com

Try 85,3,PD,GT,+37600
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
