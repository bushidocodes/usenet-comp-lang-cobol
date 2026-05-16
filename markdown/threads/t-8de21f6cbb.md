[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# what if COBOL had closures

_2 messages · 2 participants · 2006-05 → 2006-06_

---

### what if COBOL had closures

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-05-22T15:20:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4deo8qF19o412U1@individual.net>`

```
For anyone who understands closures, do this look like how it might look if
COBOL supported them?
Now that I have a "hard example" I think I finally understand what they are,
at least somewhat.

The thing that's really nice is that BROWSE-CARD-HISTORY is simply a generic
routine that reads (backwards) each card-history record and passes (yields)
the record back to the "block" (closure) to do whatever unique processing is
necessary.  So as long as the block you are passing is something that
utilizes the CHR-MTCE-HISTORY record, the BROWSE-CARD-HISTORY function can
be used over and over to do different types of CMH record processing.
Very elegant.  If only....  :-)  

Something similar could probably be done simular to a C program "callback",
using a PROGRAM-POINTER, but since my COBOL does not support that...

 ID DIVISION.
 PROGRAM-ID. MAIN.
*   more stuff goes here
 PROCEDURE DIVISION USING CARD-NUMBER.
 BROWSE-HISTORY.
     FUNCTION BROWSE-CARD-HISTORY(CARD-NUMBER) DOBLOCK | CHR-MTCE-HISTORY |
         MOVE SPACE                  TO RESULTS           
         MOVE CHR-MH-DATE            TO MSC-JULDATE       
         CALL 'CVASJULD'  USING  MSC-DATES                
         MOVE MSC-MODYYR             TO NNBNNBNN          
         MOVE '/'                    TO NNBNNBNN (3:1)    
                                        NNBNNBNN (6:1)    
         MOVE NNBNNBNN               TO DT                
         MOVE CHR-MH-TIME            TO NNBNN             
         MOVE ':'                    TO NNBNN (3:1)       
         MOVE NNBNN                  TO TM                
         CALL 'GET-DESCR-FOR-FIELD' USING CHR-MH-FIELD-NBR
                                          DESCR           
         MOVE CHR-MH-FIELD-BEFORE    TO BEFOR             
         MOVE CHR-MH-FIELD-AFTER     TO AFTR              
         MOVE SPACES TO BANK-BRANCH-LOOKUP-FIELDS            
         MOVE CHR-MH-TERMID          TO BBLF-TERMINAL-PREFIX 
         CALL BBLF-PROGRAM USING BANK-BRANCH-LOOKUP-FIELDS   
         IF BBLF-NEW-BRANCH-NBR = 999                        
             MOVE CHR-MH-TERMID      TO BRCH                 
         ELSE                                                
             MOVE BBLF-BRANCH-NAME   TO BRCH                 
         END-IF                                              
         MOVE CHR-MH-OP-ID           TO USER                 
         PERFORM CALL-XML-ROUTINE                         
     END-DOBLOCK                                                         
     EXIT PROGRAM.                                               
 END PROGRAM MAIN.
***********************************************************************

 ID DIVISION.
 FUNCTION-ID. BROWSE-CARD-HISTORY.
 LINKAGE SECTION.
 01  CARD-NBR                    PIC S9(17) COMP-3.
 PROCEDURE DIVISION USING CARD-NUMBER.
 BCH-MAIN.
     PERFORM START-CARD-HISTORY                               
     IF MORE-RECORDS                                          
         PERFORM POSITION-CARD-HISTORY                        
         PERFORM UNTIL NO-MORE-RECORDS                        
                    OR CHR-MH-CARD-NBR NOT = CARD-NBR         
             YIELD CHR-MTCE-HISTORY                            
             PERFORM PREV-CARD-HISTORY-REC                    
         END-PERFORM                                          
         PERFORM END-CARD-HISTORY                             
     END-IF                                                   
     .                                                    
                                                              
 START-CARD-HISTORY.                                     
     MOVE HIGH-VALUES            TO CHR-MTCE-HISTORY     
     MOVE CARD-NBR               TO CHR-MH-CARD-NBR      
     EXEC CICS IGNORE CONDITION                          
         NOTFND                                          
     END-EXEC                                            
     EXEC CICS STARTBR                                   
         FILE (CARD-MAINT-HIST-FILE)                     
         RIDFLD (CHR-MH-KEY)                             
         KEYLENGTH (LENGTH OF CHR-MH-KEY)                
     END-EXEC                                   
     EVALUATE EIBRESP                           
     WHEN DFHRESP(NORMAL)                       
         SET MORE-RECORDS TO TRUE               
     WHEN OTHER                                 
         SET NO-MORE-RECORDS TO TRUE            
     END-EVALUATE                               
     EXEC CICS IGNORE CONDITION                 
     END-EXEC                                   
     .                                      
                                                
*    THE FOLLOWING IS NEEDED BECAUSE OF THE STRANGE WAY THAT  
*    READPREV BEHAVES.  SEE CICS DOCUMENTATION FOR MORE INFO. 
 POSITION-CARD-HISTORY.                                       
     MOVE ZERO                   TO CNT                       
     PERFORM NEXT-CARD-HISTORY-REC                    
     PERFORM UNTIL (CNT = 2) OR NO-MORE-RECORDS       
         ADD 1                   TO CNT               
         PERFORM PREV-CARD-HISTORY-REC                
     END-PERFORM                                      
     .                                            
                                                      
 NEXT-CARD-HISTORY-REC.                         
     EXEC CICS READNEXT                         
         FILE  (CARD-MAINT-HIST-FILE)           
         RIDFLD (CHR-MH-KEY)                    
         KEYLENGTH (LENGTH OF CHR-MH-KEY)       
         INTO (CHR-MTCE-HISTORY)                
     END-EXEC                                   
     .                                      
                                                
 PREV-CARD-HISTORY-REC.                         
     EXEC CICS IGNORE CONDITION                 
         ENDFILE                                     
     END-EXEC                                        
     EXEC CICS READPREV                              
         FILE (CARD-MAINT-HIST-FILE)                 
         RIDFLD (CHR-MH-KEY)                         
         KEYLENGTH (LENGTH OF CHR-MH-KEY)            
         INTO (CHR-MTCE-HISTORY)                     
     END-EXEC                                        
     IF EIBRESP = DFHRESP(ENDFILE)                   
         SET NO-MORE-RECORDS TO TRUE                 
     END-IF                                          
     EXEC CICS IGNORE CONDITION                      
     END-EXEC                                        
     .                                           
                                                     
 END-CARD-HISTORY.                                   
     EXEC CICS ENDBR                                 
         FILE (CARD-MAINT-HIST-FILE)                 
     END-EXEC                                        
     .                                           

END PROGRAM BROWSE-CARD-HISTORY.


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA
```

#### ↳ Re: what if COBOL had closures

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-06-22T20:19:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7eu0d0s5q@news1.newsguy.com>`
- **References:** `<4deo8qF19o412U1@individual.net>`

```

[I apologize for replying to this a month late, but I haven't had time
for Usenet for a while, and I thought a couple of old articles merited
responses.]

In article <4deo8qF19o412U1@individual.net>, "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> writes:
> For anyone who understands closures, do this look like how it might look if
> COBOL supported them?

It's one possibility, using Ruby-style closures ("blocks").  Those are
somewhat different from closures in older functional languages such as
the Lisp and ML families, but I'd call them a form of closure, yes.

Basically, a closure is a piece of data that includes some code and
the "environment" (the current values of variables, loosely speaking)
in which the closure was created.  While a program is running, it can
create a closure, then later it can invoke that closure to execute
the enclosed code in the saved environment.  (Usually the code is a
function, ie it takes some parameters.)

In the Lisp and ML families, defining closures is straightforward;
you just use an operator (such as "lambda" in Lisp or "function" in
SML) that returns a new function, and it automatically includes the
current environment.

For example, in OCaml I might do:

   # let plusx = function x -> function y -> x + y;;

which says "Create a variable named plusx which is a function that
takes one parameter, x, and returns a function that takes one
parameter, y.  And that new function adds y to whatever x was when
the new function was created".

Now if I do:

   # let plus2 = plusx 2;;

I've created a new function, plus2, which takes one parameter and
adds 2 to it, returning the result:

   # plus2 3;;
   - : int = 5

The value 2 was the parameter to plusx, which became part of the
environment that was captured by the closure that I assigned to the
variable "plus2".  I could have made x a global variable rather than
a parameter, and it would have worked the same way: when plus2 was
defined, the current value of the global variable would have been
captured in the closure, and even if I changed the global variable
later, the function still would use the value 2 for it.

Ruby does things a bit differently, in its use of blocks.  The
simplest use of blocks in Ruby basically creates an unnamed closure
that can be passed as a hidden parameter to another piece of code
(in Ruby, that's a method, because everything in Ruby is an object).
The recipient doesn't call the block directly; instead, it uses the
"yield" keyword to call it.  That's what you've done in a COBOL-like
syntax in this note.

As you say, this is particularly nice for iteration.  You can create
a generic routine that just iterates over some collection of items -
elements of an array, records in a file, etc - and yields each one
as it encounters it.  Then you can call that routine with a block
that prints the item if you want to print the collection, or a block
that grabs one field and adds it to a running total, or whatever you
might want to do.

This is the "Visitor" pattern.  It can be done in a lot of ways (you
mentioned a callback, for example); the "block" idiom is just a nice
high-level way of coding it.

Ruby also supports creating blocks as objects, which creates more of
a Lisp-like closure - you can pass them around and so forth.

Anyway, thanks for the interesting post.  I've been kicking around
some ideas for a functional version of COBOL that has dynamic
functions, closures, recursive hierarchical environments, etc.
Really just an academic exercise (I don't think there's much of a
market for Functional COBOL), but it's fun.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
