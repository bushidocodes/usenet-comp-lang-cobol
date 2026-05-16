[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# screen section ACCEPTing

_5 messages · 5 participants · 1998-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### screen section ACCEPTing

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36003E40.EF052863@mindspring.com>`

```
going thru the code i have so far, i see where i really need to
eliminate some go to's.  for instance, in my customer-info i-o screen i
would like to ACCEPT CUST-INFO-IN (CUST-INFO-IN being a screen section
definition), but i want <ENTER> to move to the next field instead of
terminating the ACCEPT.  i only want certain F-keys to terminate the
accept.  i tried to use CURSOR-POSITION (SPECIAL-NAMES, CURSOR IS
CURSOR-POSITION) to determine which field to go to when <ENTER> was
pressed but it didn't work.  do i have to have an ACCEPT for each
individual field?  how do you guys do it?
```

#### ↳ Re: screen section ACCEPTing

- **From:** "Paul Swartout" <pauls@ftmis5.demon.co.uk>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<905990982.20106.0.nnrp-03.c1eda680@news.demon.co.uk>`
- **References:** `<36003E40.EF052863@mindspring.com>`

```
As far as I know, you have to ACCEPT each field as it's own screen within
the screen section.

Cheers,

Paul.

skidmike wrote in message <36003E40.EF052863@mindspring.com>...
>going thru the code i have so far, i see where i really need to
>eliminate some go to's.  for instance, in my customer-info i-o screen i
..........
```

#### ↳ Re: screen section ACCEPTing

- **From:** "Gael Wilson" <gw@mfltd.co.uk>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tqekf$a38@hyperion.mfltd.co.uk>`
- **References:** `<36003E40.EF052863@mindspring.com>`

```

skidmike wrote in message <36003E40.EF052863@mindspring.com>...
>going thru the code i have so far, i see where i really need to
>eliminate some go to's.  for instance, in my customer-info i-o screen i
…[6 more quoted lines elided]…
>individual field?  how do you guys do it?

You haven't mentioned which compiler you are using, but if it is a Micro
Focus product you can program the action of the various function keys using
the ADISCF utility. This will allow you to set the enter key to move to the
next field as required.
```

#### ↳ Re: screen section ACCEPTing

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-tIH63KmldevS@Dwight_Miller.iix.com>`
- **References:** `<36003E40.EF052863@mindspring.com>`

```
On Wed, 16 Sep 1998 22:40:00, skidmike <skidmike@mindspring.com> 
wrote:

> going thru the code i have so far, i see where i really need to
> eliminate some go to's.  for instance, in my customer-info i-o screen i
…[6 more quoted lines elided]…
> individual field?  how do you guys do it?

Let's look at how you used cursor-position.  Because that works.

Heres one that works.  Every time you press enter it goes to the next 
field.  It's not pretty though.  (Like hard coded field positions).

000010 IDENTIFICATION DIVISION.                              
000020 PROGRAM-ID DEMO1.                                     
000030 ENVIRONMENT DIVISION.                                 
000040 CONFIGURATION SECTION.                                
000070 SPECIAL-NAMES.                                        
000071      CRT Status Is CRT-STATUS                         
000072      CURSOR IS CURSOR-POS.                            
000120 DATA DIVISION.                                        
000140 WORKING-STORAGE SECTION.                              
000150 01  Crt-Status      Value Spaces.                     
000160     03  Type-Accept Pic X.                            
000170     03  Key-Press   Pic X.                            
000171     03  Unused      Pic X.                            
000172 01  Cursor-Pos      Value "0109".                     
000174     03  Cursor-Row  Pic 99.                           
000175     03  Cursor-Column Pic 99.                         
000176 01  Field-1 Pic X(20) Value Spaces.                   
000177 01  Field-2 Pic X(20) Value Spaces.                   
000178 01  Field-3 Pic X(20) Value Spaces.                   
000179 01  Field-4 Pic X(20) Value Spaces.                   
000180 Screen Section.                                       
000181 01  The-Screen Blank Screen.                          
000182     03  Line 01 Column 01 Value "Field 1".            
000183     03  Line 01 Column 40 Value "Field 2".            
000184     03  Line 02 Column 01 Value "Field 3".            
000185     03  Line 02 Column 40 Value "Field 4".            
000186     03  Line 10 Column 20 Value "Press F3 to Exit".   
000187     03  Pic X(20) Line 01 Column 9  Using Field-1.    
000188     03  Pic X(20) Line 01 Column 49 Using Field-2.    
000189     03  Pic X(20) Line 02 Column 9  Using Field-3.    
000190     03  Pic X(20) Line 02 Column 49 Using Field-4.    
000191 PROCEDURE DIVISION.                                   
000200     Perform Until Key-Press = X"03"                   
000201        Display The-Screen                             
000202        Accept The-Screen                              
000203        Evaluate True                                  
000204           When Cursor-Pos < "0149"                    
000205                Move "0149" To Cursor-Pos              
000206           When Cursor-Pos < "0209"                    
000207                Move "0209" To Cursor-Pos              
000208           When Cursor-Pos < "0249"                    
000209                Move "0249" To Cursor-Pos              
000210           When Other                                  
000211                Move "0109" To Cursor-Pos              
000212        End-Evaluate                                   
000213     End-Perform                                       
000214     Stop Run                                          
000220     .
```

##### ↳ ↳ Re: screen section ACCEPTing

- **From:** jcj0347@aol.com (JCJ0347)
- **Date:** 1998-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980917225552.26460.00000982@ng-fd2.aol.com>`
- **References:** `<Jl0PnHJ5PvPd-pn2-tIH63KmldevS@Dwight_Miller.iix.com>`

```

>000071      CRT Status Is CRT-STATUS                         
>000072      CURSOR IS CURSOR-POS.                            
…[8 more quoted lines elided]…
>000175     03  Cursor-Column Pic 99.                         

Thane, is the cursor position returned to the field
CURSOR-POS after the accept statement?

I'm using Micro Focus 3.2.24 and am having trouble
getting the cursor position from the screen.  Although
my data names are different, I'm using the exact code
you present in this example.  CURSOR-ROW and
CURSOR-COLUMN contain zeros in my system after
an accept.   What am I missing?

I am successful in setting the cursor position to an exact
location before the display, however.  It's just that with my
particular application, it won't do me any good unless I know
where the cursor was after the ACCEPT.

Regards,
JC Jones.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
