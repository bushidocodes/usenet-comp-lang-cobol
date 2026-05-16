[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# rexx script won't work in batch

_6 messages · 5 participants · 2004-09 → 2004-10_

---

### rexx script won't work in batch

- **From:** user99@austin.rr.com (user99)
- **Date:** 2004-09-22T09:15:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a16bd472.0409220815.2b9e93fb@posting.google.com>`

```
tried this script in batch and I get the following error:

   ZSERVER                                              
      6 *-* "VPUT (CNT, TP)"                            
        +++ RC(-3) +++                                  
      7 *-* "EDIT DATASET('USER99.SPF.JCL($)')         
        +++ RC(-3) +++                                  
 READY                                                  
   END                                                  
 READY                         

my rexx script (ZSERVER):

/* REXX */                                 
                                           
CNT = 1                                    
TP = 12345678911                           
ADDRESS ISPEXEC                            
"VPUT (CNT, TP)"                           
"EDIT DATASET('USER99.SPF.JCL($)')        
       MACRO(TSERVERM)"                    
RETURN                                     


my job:
//TSERVER  JOB (280000,AAO,T21),MSGCLASS=0        
//*MAIN  CLASS=T                                  
//TSOBATCH EXEC PGM=IKJEFT01                      
//SYSEXEC  DD  DSN=USER99.SPF.REXX,DISP=SHR      
//SYSTSPRT DD  SYSOUT=*                           
//SYSTSIN  DD  *                                  
  ZSERVER                                         
  END                                                

ideas??????
```

#### ↳ Re: rexx script won't work in batch

- **From:** N Benson <nigel@lbenny1.demon.co.uk>
- **Date:** 2004-09-22T23:11:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ktt3l0dei0v4o1nm0549s2n5jb147ealgk@4ax.com>`
- **References:** `<a16bd472.0409220815.2b9e93fb@posting.google.com>`

```
User99

This is a mainly friendly newsgroup -please post with your name...

REXX questions should really be posted to COMP.LANG.REXX.

But the real answer to your question probably lies in the JCL used to run you
REXX. Look at the library allocations you should have to invoke ISPF services...

If you're still having difficulties please let us know.

Regards

Nigel







On 22 Sep 2004 09:15:04 -0700, user99@austin.rr.com (user99) wrote:

>tried this script in batch and I get the following error:
>
…[32 more quoted lines elided]…
>ideas??????
```

##### ↳ ↳ Re: rexx script won't work in batch

- **From:** alex ortiz <user99@austin.rr.com>
- **Date:** 2004-09-23T00:15:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OAo4d.25116$1d6.19861@fe1.texas.rr.com>`
- **In-Reply-To:** `<ktt3l0dei0v4o1nm0549s2n5jb147ealgk@4ax.com>`
- **References:** `<a16bd472.0409220815.2b9e93fb@posting.google.com> <ktt3l0dei0v4o1nm0549s2n5jb147ealgk@4ax.com>`

```
geez, thanks a lot.  checked out comp.lang.rexx and nobody's posting!

N Benson wrote:

> User99
> 
…[58 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: rexx script won't work in batch

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2004-09-22T20:29:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8No4d.20078$pA.1365686@news20.bellglobal.com>`
- **References:** `<a16bd472.0409220815.2b9e93fb@posting.google.com> <ktt3l0dei0v4o1nm0549s2n5jb147ealgk@4ax.com> <OAo4d.25116$1d6.19861@fe1.texas.rr.com>`

```
Try bit.listserv.tsorexx or bit.listserv.ispf-l  The latter one is 
particularly 'on point' in your case.

"alex ortiz" <user99@austin.rr.com> wrote in message 
news:OAo4d.25116$1d6.19861@fe1.texas.rr.com...
> geez, thanks a lot.  checked out comp.lang.rexx and nobody's posting!
>
…[50 more quoted lines elided]…
>>
```

###### ↳ ↳ ↳ Re: rexx script won't work in batch

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-09-23T07:12:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9HPwdP9uflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<a16bd472.0409220815.2b9e93fb@posting.google.com> <ktt3l0dei0v4o1nm0549s2n5jb147ealgk@4ax.com> <OAo4d.25116$1d6.19861@fe1.texas.rr.com>`

```
.    Am  23.09.04
schrieb  user99@austin.rr.com (alex ortiz)
    auf  /COMP/LANG/COBOL
     in  OAo4d.25116$1d6.19861@fe1.texas.rr.com
  ueber  Re: rexx script won't work in batch

ao> geez, thanks a lot.  checked out comp.lang.rexx and nobody's posting!

   I have six messages in comp.lang.rexx for September 22.


Yours,
Lï¿½ko Willms                                     http://www.mlwerke.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

"Das Volk, das ein anderes Volk unterjocht, schmiedet seine eigenen
Ketten."                         - Karl Marx           (1. Januar 1870)
```

#### ↳ Re: rexx script won't work in batch

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2004-10-03T17:10:49+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mg50m0l7mhakcq9t426snguob00dbgd2i0@4ax.com>`
- **References:** `<a16bd472.0409220815.2b9e93fb@posting.google.com>`

```
On 22 Sep 2004 09:15:04 -0700 user99@austin.rr.com (user99) wrote:

:>tried this script in batch and I get the following error:

:>   ZSERVER                                              
:>      6 *-* "VPUT (CNT, TP)"                            
:>        +++ RC(-3) +++                                  
:>      7 *-* "EDIT DATASET('USER99.SPF.JCL($)')         
:>        +++ RC(-3) +++                                  
:> READY                                                  
:>   END                                                  
:> READY                         

:>my rexx script (ZSERVER):

:>/* REXX */                                 
                                           
:>CNT = 1                                    
:>TP = 12345678911                           
:>ADDRESS ISPEXEC                            
:>"VPUT (CNT, TP)"                           
:>"EDIT DATASET('USER99.SPF.JCL($)')        
:>       MACRO(TSERVERM)"                    
:>RETURN                                     


:>my job:
:>//TSERVER  JOB (280000,AAO,T21),MSGCLASS=0        
:>//*MAIN  CLASS=T                                  
:>//TSOBATCH EXEC PGM=IKJEFT01                      
:>//SYSEXEC  DD  DSN=USER99.SPF.REXX,DISP=SHR      
:>//SYSTSPRT DD  SYSOUT=*                           
:>//SYSTSIN  DD  *                                  
:>  ZSERVER                                         
:>  END                                                

:>ideas??????

In the event that you have not yet received an answer:

   ISPF CMD(ZSERVER)

Of course, you will then get error messages about your missing allocations.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
