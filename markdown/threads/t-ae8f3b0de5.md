[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# So here he goes again!

_4 messages · 3 participants · 2007-08_

---

### So here he goes again!

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-15T14:43:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46C31127.6F0F.0085.0@efirstbank.com>`

```
So here he goes again!

Below are two snippets of code.  The first is how it is now and the second
is the new one.

     PERFORM REPOSITION-ACCOUNT                               
     IF NOT-RELATED-CUSTOMER                                      
        IF WS-HOLD-DATE-LAST-MTCE GREATER THAN +99999999          
           CONTINUE                                               
        ELSE                                                      
           ADD +100000000 TO WS-HOLD-DATE-LAST-MTCE               
        END-IF                                                    
        MOVE UMA1-ADDR-KEY            TO WS-HOLD-CUST-ADDR-KEY    
        IF UPDATE-MAIL-CODE                                       
           MOVE MAIL-CODE-TC          TO MR-TC                    
           MOVE HOLD-OLD-MAIL-CODE    TO MRO-X                    
           MOVE HOLD-NEW-MAIL-CODE    TO MRN-X                    
           PERFORM WRITE-ACCT-MAINTENANCE                     
        END-IF                                                    
        PERFORM UPDATE-ACCT-MSTR                              
     ELSE                                                         
        IF WS-HOLD-DATE-LAST-MTCE GREATER THAN +99999999          
           IF UPDATE-MAIL-CODE                                    
              MOVE MAIL-CODE-TC       TO MR-TC                    
              MOVE HOLD-OLD-MAIL-CODE TO MRO-X                    
              MOVE HOLD-NEW-MAIL-CODE TO MRN-X                    
              PERFORM WRITE-ACCT-MAINTENANCE                  
              PERFORM UPDATE-ACCT-MSTR                      
           END-IF                                               
        ELSE                                                    
           ADD +100000000 TO WS-HOLD-DATE-LAST-MTCE             
           IF UPDATE-MAIL-CODE                                  
              MOVE MAIL-CODE-TC       TO MR-TC                  
              MOVE HOLD-OLD-MAIL-CODE TO MRO-X                  
              MOVE HOLD-NEW-MAIL-CODE TO MRN-X                  
              PERFORM WRITE-ACCT-MAINTENANCE                
           END-IF                                               
           PERFORM UPDATE-ACCT-MSTR                         
        END-IF                                                  
        MOVE UMA1-CUST-NBR           TO WS-SSA-Q-D-RELN-CUST-NBR
        MOVE WS-HOLD-SEQ-NBR         TO WS-SSA-Q-D-RELN-SEQ     
        PERFORM REPOSITION-ACCT-RELN                        
        MOVE UMA1-ADDR-KEY           TO D-RELN-USE-ADDR-KEY     
        PERFORM UPDATE-ACCT-RELN                            
     END-IF.                                                    
--------------------------------------------------------------------
     PERFORM REPOSITION-ACCOUNT                             
     IF NOT-RELATED-CUSTOMER                                    
        IF WS-HOLD-DATE-LAST-MTCE GREATER THAN +99999999        
           CONTINUE                                             
        ELSE                                                    
           ADD +100000000 TO WS-HOLD-DATE-LAST-MTCE             
        END-IF                                                  
        MOVE UMA1-ADDR-KEY            TO WS-HOLD-CUST-ADDR-KEY  
        PERFORM HANDLE-MAIL-CODE                            
        PERFORM UPDATE-ACCT-MSTR                            
     ELSE                                                       
        IF WS-HOLD-DATE-LAST-MTCE GREATER THAN +99999999        
           PERFORM HANDLE-MAIL-CODE                         
           IF UPDATE-MAIL-CODE                                  
              PERFORM UPDATE-ACCT-MSTR                      
           END-IF                                               
        ELSE                                                    
           ADD +100000000 TO WS-HOLD-DATE-LAST-MTCE             
           PERFORM HANDLE-MAIL-CODE                         
           PERFORM UPDATE-ACCT-MSTR                         
        END-IF                                                  
        MOVE UMA1-CUST-NBR           TO WS-SSA-Q-D-RELN-CUST-NBR
        MOVE WS-HOLD-SEQ-NBR         TO WS-SSA-Q-D-RELN-SEQ     
        PERFORM REPOSITION-ACCT-RELN                   
        MOVE UMA1-ADDR-KEY           TO D-RELN-USE-ADDR-KEY
        PERFORM UPDATE-ACCT-RELN                       
     END-IF.                                               

 HANDLE-MAIL-CODE.                   
    IF UPDATE-MAIL-CODE                  
       MOVE MAIL-CODE-TC       TO MR-TC  
       MOVE HOLD-OLD-MAIL-CODE TO MRO-X  
       MOVE HOLD-NEW-MAIL-CODE TO MRN-X  
       PERFORM WRITE-ACCT-MAINTENANCE
    END-IF.

Obviously I re-did it to refactor redundant code in to a single procedure.
This is all well and good, in that the redundant code is fairly small and I
am comfortable placing it within the IF statement in the new procedure.

My question, is, what would you do if the code that is to be performed is
many lines long, including perhaps other conditional logic.  Would you:

1) Keep it like it is, putting the code within the IF statement?

2) Move the code in to a separate paragraph (WRITE-MAIL-CODE-MAINT), and
perform that paragraph from within the HANDLE-MAIL-CODE IF statement?

3) Rename HANDLE-MAIL-CODE itself to WRITE-MAIL-CODE-MAINT and put the IF
statements in the main procedure above (doing the test each of the three
times before performing the new paragraph).

4) Escape out of HANDLE-MAIL-CODE immediately if UPDATE-MAIL-CODE is not
true (using EXIT PARAGRAPH, if available; otherwise necessitating the
restructure of the logic to allow for a useful GO TO EXIT, either by using
SECTIONs or PERFORM...THRU (argh, I know!))

5) Put it in a subroutine which you would exit (EXIT PROGRAM) if
UPDATE-MAIL-CODE was not true?

6) Something else entirely?

 HANDLE-MAIL-CODE.                   
    IF NOT UPDATE-MAIL-CODE
        EXIT PARAGRAPH.

    MOVE MAIL-CODE-TC       TO MR-TC  
    MOVE HOLD-OLD-MAIL-CODE TO MRO-X  
    MOVE HOLD-NEW-MAIL-CODE TO MRN-X  
    PERFORM WRITE-ACCT-MAINTENANCE
    .

My preference is number 6.  :-)

Anyway, since there are only a few statements I'm going to code it as I have
above, but I'm always looking for a better way.  Not that I ever take
anyone's advice <g>, but I still like to hear it.

Frank
```

#### ↳ Re: So here he goes again!

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-08-16T08:25:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1187277927.096249.184150@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<46C31127.6F0F.0085.0@efirstbank.com>`
- **References:** `<46C31127.6F0F.0085.0@efirstbank.com>`

```
On 15 Aug, 21:43, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
wrote:
> So here he goes again!
>
> 2) Move the code in to a separate paragraph (WRITE-MAIL-CODE-MAINT), and
> perform that paragraph from within the HANDLE-MAIL-CODE IF statement?
>

At the risk of upsetting some people, I would:

Move the code to a separate SECTION and perform that SECTION from
within the Handle-Mail-Code statement.

;-P
```

#### ↳ Re: So here he goes again!

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-22T21:35:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<J_1zi.122238$sR4.36482@fe08.news.easynews.com>`
- **References:** `<46C31127.6F0F.0085.0@efirstbank.com>`

```
<JUST JOKING>

Put the redundant code into a COPY member and COPY it in (in the appropriate 
places - using REPLACING if any cases differ).  "Single sourced" routines 
(common logic) are easier to "maintain" when a change occurs.
```

##### ↳ ↳ Re: So here he goes again!

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-22T16:35:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46CC65EB.6F0F.0085.0@efirstbank.com>`
- **References:** `<46C31127.6F0F.0085.0@efirstbank.com> <J_1zi.122238$sR4.36482@fe08.news.easynews.com>`

```
Great idea, Bill!

:-)

n 8/22/2007 at 3:35 PM, in message
<J_1zi.122238$sR4.36482@fe08.news.easynews.com>, William M.
Klein<wmklein@nospam.netcom.com> wrote:
<> JUST JOKING>
> 
> Put the redundant code into a COPY member and COPY it in (in the 
> appropriate 
> places - using REPLACING if any cases differ).  "Single sourced" routines

> 
> (common logic) are easier to "maintain" when a change occurs.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
