[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Multiple programs in one source

_69 messages · 18 participants · 1999-07_

---

### Multiple programs in one source

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37932F22.A4751958@NOSPAMhome.com>`

```
I'm a mainframe programmer who has never worked in a location which has
more than one COBOL program in one source member.

When we have called programs, it is because several programs will be
doing the calling.

I suppose the called program can be in a copy library, but I also
haven't worked where compile time calls were standard.

The one place I can see a use for this is if only one program does the
call, and a perform won't work because the called program and calling
program use different subschemata.  (having fun with that word -
schemata is a dictionary plural for schema!!)

What am I overlooking?  What are the shops I have worked in overlooked?
```

#### ↳ Re: Multiple programs in one source

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UVJk3.971$ng2.5648@news2.mia>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com>`

```
Using separate programs (in one source file) provides better isolation
of function and data than does using PERFORM.
```

##### ↳ ↳ Re: Multiple programs in one source

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37937B17.2E9B2D6A@NOSPAMhome.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia>`

```
OK.  So when do you want this better isolation badly enough to get drop
the simplicity of PERFORM?  When the program isn't debugged?

Obviously you wouldn't call a sub program to replace a simple
computation.  What type of function do you consider creating this
isolation in a non-OO program?

Judson McClendon wrote:
> 
> Using separate programs (in one source file) provides better isolation
…[22 more quoted lines elided]…
> >What am I overlooking?  What are the shops I have worked in overlooked?
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r0%k3.2575$_f5.26236@news3.mia>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com>`

```
Howard Brazee wrote:
>OK.  So when do you want this better isolation badly enough to get
>drop the simplicity of PERFORM?  When the program isn't debugged?
…[3 more quoted lines elided]…
>isolation in a non-OO program?

I don't normally use same-source multiple programs myself, preferring
to independently compile them.  Conceptually, there is no difference,
but compiling them all in the same source will usually create only
one executable, which may be an advantage in some cases.  There are
two main reasons that I use sub programs.

One is to create isolated 'black box' routines where the inputs and
outputs are well defined.  This also facilitates using the subroutine
program unchanged in other applications.

The second is to cleanly break a large program into smaller parts.
A good example is a menu-driven application, where the user selects
a menu item, causing a small menu program to call the appropriate
sub program.

Actually, using separate programs can make testing easier, because
they can often be tested individually.  And because they are very
isolated, the chance of their internal logic affecting the calling
program is low.

This seems pretty elementary Howard, am I missing something? :-)
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3794999A.5413BFD2@NOSPAMhome.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia>`

```
Judson McClendon wrote:
> 
> Howard Brazee wrote:
…[27 more quoted lines elided]…
> This seems pretty elementary Howard, am I missing something? :-)

No.  I guess my environment is different enough that nobody has created
any examples of multiple programs in one source, so I was looking for an
example where I could do so where the advantage is clear enough to move
past any inertia in the standards/migration team approval.  We don't use
COBOL for anything except pure batch, our on-line uses ADS/O.   We do
use sub programs, but these are shared and linked separately.  Nobody
has attempted any OO Cobol (and an isolated OO Cobol program doesn't
make sense anyway), and we don't do any PC Cobol.

What I'm looking for is a good excuse - or at least some convincing
criteria to look for to allow me to move us in that direction.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 5)_

- **From:** Jared Thomas <jared@techie.com>
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37966671.731DDB7B@techie.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <3794999A.5413BFD2@NOSPAMhome.com>`

```
Howard Brazee wrote:
{snip}
> 
> What I'm looking for is a good excuse - or at least some convincing
> criteria to look for to allow me to move us in that direction.

I wrote one the other day to get a bunch of statistics.  I defined
a zillion buckets with several similar counters in each bucket
(like count, average, split by accounts) and used the same COPY
book repeatedly for each bucket.  Next I wrote a few inner
programs that took a bucket as one of the parameters.  They
tallied, printed, rolled up, rolled over, initialized, etc.  

Then I went into an existing program that ran through the files
and stuck CALLs in everywhere I found something I wanted to
count.  At the end I had another inner program (not strictly
needed) that looped through the buckets to print them.

. . .

In another case, a program was processing character strings,
substituting variables.  (Turn "you owe xxxx by yyyy" into smooth
text for a letter.  They did trims and squishes on buffers of 20K
bytes.  There was a lot of:
   MOVE BUFFER-1 TO PARM-IN-BUFFER
   PERFORM TRIM-IT
   MOVE PARM-OUT-BUFFER to BUFFER-1
In short, the program spend 70% of it's time moving characters
around.

I changed the TRIM-IT and SQUISH-IT and a couple of other
performed paragraphs (sections) into inner programs (20 lines
each?) passing BUFFER-1 as a parameter all the time.  Things
speeded up; that's how I got the 70% figure above.  Your mileage
may vary.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 5)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990720210030.23400.00000148@ngol07.aol.com>`
- **References:** `<3794999A.5413BFD2@NOSPAMhome.com>`

```
In article <3794999A.5413BFD2@NOSPAMhome.com>, Howard Brazee
<brazee@NOSPAMhome.com> writes:

>
>No.  I guess my environment is different enough that nobody has created
…[10 more quoted lines elided]…
>

I'm not sure of what the orignal intent of your request was, but I have found 
a couple of uses for the multiple programs in one source on an MVS mainframe.
Mainly it has to do with reducing memory requirements for Lookup tables.

Our environment has some canned aassembly language table access routines that
permit accessing flat files as binary search tables.  The downside to these
routines is that they load the entire table into memory and have a record
length limit of 256-bytes.  

Recently we came across development requirements of accessing files that were
1000-bytes wide and 100k deep.  An additonal requirement was to access multiple
such tables at once.  Our alternative was to create COBOL ISAM files on the fly
in the sub programs to handle the file access and the main program simply makes
a CALL to the sub program to get its data (kind of like having an external file
handler).   Each of the sub-programs is coded into a separate member and in the
compile of the main program , each of the sub program source members is
concatentated to the end of the main program separted by 'End Program.' cards.

This has worked extremely well for us making the runtime program operate within
a 9M region as opposed to requiring some 850M to table all the files into
memory at once.

I suppose that canned functions could be bound together in this manner or the
individual sub-programs compiled into executables that would then have to be
added to the LinkEdit list as additional Include members for the MainCalling
Programs.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37949F1E.602548B9@home.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia>`

```
Judson McClendon wrote:
> 
> Howard Brazee wrote:
…[6 more quoted lines elided]…
> program unchanged in other applications. 

A rose by another name; OO independent classes and proven methods.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i83l3.3060$_f5.30095@news3.mia>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com>`

```
James J. Gavan wrote:
>Judson McClendon wrote:
>> Howard Brazee wrote:
…[8 more quoted lines elided]…
>A rose by another name; OO independent classes and proven methods.

Ah, but done so much more simply, easily and intuitively! :-)
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3794D221.15FF9397@home.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia>`

```
Judson McClendon wrote:
> James J. Gavan wrote:
> >> One is to create isolated 'black box' routines where the inputs and
…[5 more quoted lines elided]…
> Ah, but done so much more simply, easily and intuitively! :-)

Want to put money on it ? In the long term mine will prove to be the
sweeter smelling rose, and as for longevity my rose wont fade - it will
continue to be enhanced, (VERY EASILY), in all its glorious colours.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TNkl3.4715$Kk.39268@news2.mia>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com>`

```
James J. Gavan wrote:
>Judson McClendon wrote:
>> James J. Gavan wrote:
…[10 more quoted lines elided]…
>continue to be enhanced, (VERY EASILY), in all its glorious colours.

Much of the industry is indeed betting the bank on OO.  It is clear
to me, at least, that the jury is still out at best, particularly as
to how cost and time effective OO will prove.  Time will tell. :-)
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379654EC.FD57917B@home.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia>`

```
Judson McClendon wrote:
> 
> Much of the industry is indeed betting the bank on OO.  It is clear
> to me, at least, that the jury is still out at best, particularly as
> to how cost and time effective OO will prove.  Time will tell. :-)

You're right about the jury still being out. You might be interested in
my own observations using OO. 

(a) Windowing/GUIs all that front-end HTML etc jazz, is just too damn 
complicated regardless of the tools you use - and OO GUI classes are
just a pig-in-the-poke like other GUI toolkits - Mr. Microsoft 'demands'
we learn Windows. (And how I love him for deciding the default button
will be 'Enter' and I have to refer to his SDK and find he puts in three
suggestions to put the 'Enter' back as I, AND THE USER, always used it).

As soon as you enter :-

	invoke MyDialog "show" 

Windows is in control and then your OO Dialog-program can jump all over
the place depending upon the control the user clicked on. Not the fault
of OO, but a gentleman named Bill - not the very dedicated contributor
to this NG.

(b) 'Straight' OO - like I used in my file-handling examples - is a
snip. After a one or two-day course, (to get the overall 'feel') anybody
could program using this aspect of OO. Much of it is replacing Paragraph
Names with Method Names 'invoke <method-name>' instead of 'perform
<para-name>' and the attractiveness of local variables as opposed to
global variables must be obvious to anyone.

You could call it overkill, but I have the following Class (Data is
stored Imperial, but can be displayed/entered in Imperial/Metric).
Just like 'structured' I have to get a handle to this 'sub-program' with
my Method-id "new'. But OO is not grabbing memory for all subsequent
OBECT SECTION methods, just pulling them in as required, and dropping
them when finished, (the runtime may well have some cacheing system for
'popular' methods - I don't know) :-

------------------- convert.cbl ---------------------------------
                                                                 
*> Converts Imperial values to Metric and vice versa             
                                                                 
CLASS-ID.          ConvertValues                                 
                   inherits from Base.                           
                                                                 
CLASS-CONTROL.     ConvertValues       is class "convert"        
                   .                                             
                                                                
*>---------------------------------------------------------------
FACTORY.                                                         
*>---------------------------------------------------------------
Method-id. "new".                                                
*>-------------------------------------------------------------- 
Linkage Section.                                                 
01 lnk-self                  object reference.                   
Procedure Division returning lnk-self.                           
  invoke super "new" returning lnk-self                          
End Method "new".                                                
*>------------------------------------------------------------   
END FACTORY.                                                     
*>------------------------------------------------------------   
OBJECT.                                                          
*>------------------------------------------------------------   
Method-id. "imp-to-met".                                         
*>-------------------------------------------------------------  
Linkage section.                                                 
01 lnk-inches                   pic 9(03)v9(03) comp-3.          
01 lnk-mms                      pic 9(03)v9(02) comp-3.          
                                                                 
Procedure Division using     lnk-inches                          
                   returning lnk-mms.                            
                                                                 
   if  lnk-inches <> zeroes                                      
       compute lnk-mms rounded = lnk-inches * 25.4               
                                                                 
   else move zeroes to lnk-mms                                   
   End-if                                                        
                                                                 
End Method "imp-to-met".                                         
*>-------------------------------------------------------------  
Method-id. "met-to-imp".                                         
*>-------------------------------------------------------------  
Linkage section.                                                 
01 lnk-mms                      pic 9(03)v9(02) comp-3.          
01 lnk-inches                   pic 9(03)v9(03) comp-3.          
                                                                 
Procedure Division using     lnk-mms                             
                   returning lnk-inches.                         
                                                                 
   if    lnk-mms <> zeroes                                       
         compute lnk-inches rounded = lnk-mms * 0.03937          
                                                                 
   else  move zeroes to lnk-inches                               
   End-if                                                        
End Method "met-to-imp".                                         
*>-------------------------------------------------------------  
Method-id. "c-to-f".                                             
*>-------------------------------------------------------------  
Linkage section.                                                 
01 lnk-celsius                   pic s9(04) comp-3.              
01 lnk-fahrenheit                pic s9(04) comp-3.              
                                                                 
Procedure Division using     lnk-celsius                         
                   returning lnk-fahrenheit.                     
                                                                 
if    lnk-celsius <> zeroes                                      
      compute lnk-fahrenheit rounded = (lnk-celsius * 1.8) + 32  
                                                                 
else  move zeroes to lnk-fahrenheit                              
End-if                                                           
End Method "c-to-f".                                             
*>-------------------------------------------------------------  
Method-id. "f-to-c".                                             
*>-------------------------------------------------------------  
Linkage section.                                                 
01 lnk-fahrenheit                pic s9(04) comp-3.              
01 lnk-celsius                   pic s9(04) comp-3.              
                                                                 
Procedure Division using     lnk-fahrenheit                      
                   returning lnk-celsius.                        
                                                                 
if   lnk-fahrenheit <> zeroes                                    
     compute lnk-celsius rounded = (lnk-fahrenheit - 32) * 0.555 
                                                                 
else move zeroes to lnk-celsius                                  
End-if                                                           
End Method "f-to-c".                                             
*>-------------------------------------------------------------  
Method-id. "kpa-to-psi".                                         
*>-------------------------------------------------------------  
Linkage section.                                                 
01 lnk-kpa                       pic 9(05) comp-3.               
01 lnk-psi                       pic 9(05) comp-3.               
                                                                 
*>78 ls-convert                  value 0.1450326.                
                                                                 
Procedure Division using    lnk-kpa                              
                  returning lnk-psi.                             
                                                                 
  if lnk-kpa <> zeroes                                           
     compute lnk-psi rounded = lnk-kpa * 0.145                   
                                                                 
  else move zeroes to lnk-psi                                    
  End-if                                                         
                                                                 
End Method "kpa-to-psi".                                         
*>-------------------------------------------------------------  
Method-id. "psi-to-kpa".                                         
*>-------------------------------------------------------------  
Linkage section.                                                 
01 lnk-psi                       pic 9(05) comp-3.               
01 lnk-kpa                       pic 9(05) comp-3.               
                                                                 
Procedure Division using    lnk-psi                              
                  returning lnk-kpa.                             
                                                                 
  if lnk-psi <> zeroes                                           
     compute lnk-kpa rounded = lnk-psi * 6.8948                  
                                                                 
  else move zeroes to lnk-kpa                                    
  End-if                                                         
                                                                 
End Method "psi-to-kpa".                                         
*>-------------------------------------------------------------  
                                                                 
END OBJECT.                                                      
END CLASS ConvertValues.                                         
*>-------------------------------------------------------------  

You could argue that the above are 'one-liners' why not include them in
your 'paragraph'. But once I've got it right I don't have to bother
about them again. And of course the routines are not just being used for
data-entry/display, but also for printing programs. (So far haven't
needed to worry about Litres and Gallons(US/Imperial).

As a speed observation, I haven't noticed any sluggishness in
performance using OO - but I haven't done any benchmark tests either.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-07-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mCGl3.2309$xN4.21583@news3.mia>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com>`

```
James J. Gavan wrote:
>
>You could call it overkill, but I have the following Class (Data is
>stored Imperial, but can be displayed/entered in Imperial/Metric).

I would call it 'massive overkill'. ;-)

My question is simply this: Why complicate the issue with OO, when
all the essential goals can be much more simply and intuitively
implemented with good structured design?  I just don't see the
concept of 'objects' being necessary.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37975FB9.ACD87343@home.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia>`

```
Judson McClendon wrote:
> 
> James J. Gavan wrote:
…[9 more quoted lines elided]…
> concept of 'objects' being necessary.

Wont pursue this one any further at this stage - other than you say,
"simply, intuitively'. Other than I show a separate Class, which just
doesn't turn you on, where does it lack simplicity or intuition. Lots of
extraneous typing agreed, heading-up and finishing a method, but better
that than those bloody awful :-

	{
			}

What's the significant difference between :-

Working-Storage section.
01 DataValue			pic 9(03)v9(03) comp-3.
01 ImpValue			pic 9(03)v9(03) comp-3.
01 MetValue			pic 9(02)v9(03) comp-3.

	If   Imperial
	     continue

	else Perform GetMetricReadingValue
	End-if

as opposed to :-

Local-storage section.
01 DataValue			pic 9(03)v9(03) comp-3.
01 ImpValue			pic 9(03)v9(03) comp-3.
01 MetValue			pic 9(02)v9(03) comp-3.

	If   Imperial
	     continue

	else invoke os-Convert "imp-to-met"
	            using DataValue
		    returning MetValue
	End-if

See the separate quote I've included under this thread about OO machine 
performance.

(No, this is not me getting on the defensive because the 'critic' is 
slamming the "artist's" work :) ).

Good, be a 'disbeliever' - where would we be with COBOL if we all
slavishly followed the same track. That's the exciting aspect I find in
this NewsGroup - just as others have confirmed my suspicions about all
the clever stuff using Internet, (i.e. only use inter-netting when it is
cost-justifiable for the application).

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 11)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 1999-07-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n7sga$juq$1@mail.pl.unisys.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37975FB9.ACD87343@home.com>`

```
One of the advantages nested programs (and IPC as a whole, for that matter,
of which it is a subset) has over objects is that nested programs are called
for by ANSI X3.23-1985 and thus represent a part of a current standard.

The OO features of COBOL have not, so far as I know, been standardized as
yet, and in any case the user of such features is limited to compilers (and
associated platforms) that provide them.

Features mandated by standards are more likely to have broader application
than proposals, features included only in a draft of a future standard, or
proprietary extensions.

And performance conclusions based on one compiler vendor's implementation of
OOCOBOL on a given platform might not necessarily be applicable to another
compiler vendor's product, or another platform  when used with a compiler
from either vendor.

       -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 12)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379780FC.A873E9A2@home.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37975FB9.ACD87343@home.com> <7n7sga$juq$1@mail.pl.unisys.com>`

```
Chuck Stevens wrote:
> 
> The OO features of COBOL have not, so far as I know, been standardized as
> yet, and in any case the user of such features is limited to compilers (and
> associated platforms) that provide them.

Do I infer from the above that Unisys is saying 'Thanks. But no thanks",
to OO ?
 
> And performance conclusions based on one compiler vendor's implementation of
> OOCOBOL on a given platform might not necessarily be applicable to another
> compiler vendor's product, or another platform  when used with a compiler
> from either vendor.

Please ! I did say no discussion. It was meant to be informative for
those interested - not a plug for a vendor, nor have I drawn performance
conclusions from same, only a comparison between Structured and OO
SOLELY within NetExpress. (I'll plug it like hell if they give me a
whopping discount on my next purchase - like cost price = $0).

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 13)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 1999-07-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n8aj9$6io$1@mail.pl.unisys.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37975FB9.ACD87343@home.com> <7n7sga$juq$1@mail.pl.unisys.com> <379780FC.A873E9A2@home.com>`

```

James J. Gavan wrote in message <379780FC.A873E9A2@home.com>...
>Chuck Stevens wrote:
>>
>> The OO features of COBOL have not, so far as I know, been standardized as
>> yet, and in any case the user of such features is limited to compilers
(and
>> associated platforms) that provide them.
>
>Do I infer from the above that Unisys is saying 'Thanks. But no thanks",
>to OO ?

I can't say whether you do or don't; that only you can determine!  ;-)
Seriously, I haven't a clue what Unisys product planners have in mind; I can
say with little fear of contradiction that I believe it exceedingly unlikely
for Unisys to decide to add OO extensions to its A Series COBOL(68) or
COBOL74 compilers (products with which I am intimately familiar).

As to A Series COBOL85, I don't know, but so long as the draft standards are
still being refined in the area of OOCOBOL I'd find it unlikely for Unisys
to release a product intended to be compliant with a standard that hadn't
been completely established.  The risk, if and when that standard changes,
is too great, both for Unisys and for its existing A Series customers
(particularly those hypothetical ones that would have made use of the
feature only to have its behavior change underneath them in some way).

>
>> And performance conclusions based on one compiler vendor's implementation
of
>> OOCOBOL on a given platform might not necessarily be applicable to
another
>> compiler vendor's product, or another platform  when used with a compiler
>> from either vendor.
…[5 more quoted lines elided]…
>whopping discount on my next purchase - like cost price = $0).


I didn't find it clear that your entries applied only within the confines of
NetExpress; that precisely was my point.   They seemed to be worded more uni
versally than that.  I have no doubt that OO techniques can indeed use fewer
resources at execution time than more traditional techniques in some
environments and circumstances, but I am not convinced that there is
something inherent about OO programming (as distinct from structured
programming) that gives it a speed/resource advantage at execution time.
The primary architectural advantages and strengths of OO programming  -- and
they are by no means negligible -- lie in areas other than execution-time
performance and resource consumption, as I see it.

Whether a given program is faster in its OO instantiation than in an
equivalent structured version is a byproduct of the particular
implementation, not of the fact that the former is object oriented.
Whichever one in that particular implementation has the less resource
"baggage" to drag around will most likely win the race, and that's dependent
on the architects of each implementation, not so much on the rules or
philosophies that the architects are following.  Moreover, any
execution-time difference is as likely to be the result of a poor
implementation of the more resource-intensive environment -- whichever one
that happens to be -- as it is a good implementation of the less
resource-intensive one.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 14)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3797F1E5.46F0C819@home.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37975FB9.ACD87343@home.com> <7n7sga$juq$1@mail.pl.unisys.com> <379780FC.A873E9A2@home.com> <7n8aj9$6io$1@mail.pl.unisys.com>`

```
Chuck Stevens wrote:
> 
> James J. Gavan wrote in message <379780FC.A873E9A2@home.com>...
…[5 more quoted lines elided]…
> > As to A Series COBOL85.......

Your answer was fair. But I'm intrigued, bearing in mind I haven't been
near a mainframe in 24 years and I'm used to the grandfather, father,
son approach with compilers on PCs.

You refer to 68, 74 and 85. You don't keep on upgrading these
individually for the fun of it. Is it, say,  that your '68 was written
for a particular machine architecture and you just can't include later
COBOL implementations because they conflict with the architecture ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 15)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 1999-07-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nageh$38a$1@mail.pl.unisys.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37975FB9.ACD87343@home.com> <7n7sga$juq$1@mail.pl.unisys.com> <379780FC.A873E9A2@home.com> <7n8aj9$6io$1@mail.pl.unisys.com> <3797F1E5.46F0C819@home.com>`

```
<<You refer to 68, 74 and 85. You don't keep on upgrading these individually
for the fun of it.>>

The Unisys A Series COBOL74 and COBOL85 compilers were both built, first and
foremost, in response to marketplace requirements, primarily the requirement
by some of our customers (in particular the federal government) that any
systems obtained by them have COBOL compilers available that were compliant
with the then-current ANSI standards for COBOL.  In each case, ANSI
compliance was the first goal of the developers, and only later were
Unisys-specific enhancements added to these products.

COBOL(68) was introduced with, or very soon after, the Burroughs B6700, for
which it was written.

At the present time, COBOL85 (written *de novo*, not an "upgrade" of either
the A Series COBOL(68) or COBOL74 compilers, or any other COBOL compiler,
for that matter) would have to be regarded as our "flagship" COBOL compiler.
Significant new features destined for COBOL are most likely here.

Significant feature enhancements are unlikely in COBOL74, though it is still
an extremely popular product with a very large base of very loyal customers.
Their programs work.  Why should they change them?

COBOL(68) has been dropped from general release and is supported only for a
handful  of customers who have contracted explicitly for continued support.

<< Is it, say,  that your '68 was written for a particular machine
architecture and you just can't include later COBOL implementations because
they conflict with the architecture ?>>

No, that's not the case.  There's always a programmatic way around anything
that might be perceived as an architectural (system or programmatic)
problem, presuming that there's a requirement for the feature in the first
place, and providing that the user is willing to accept any potential
drawbacks or inefficiencies that might be entailed.   In the particular
environment that started this discussion, I do not personally see the Unisys
A Series platform as architecturally incompatible with, or in any way
inappropriate for, OOP, be that programming in COBOL or any other A Series
language.

If there are architectural limitations to, for example, COBOL(68) and
COBOL74, they would most likely take the form of limitations *within the
compiler* that increase the cost of implementing such new features.  There
are some internal limitations remaining in those compilers that have their
*origins* in earlier platforms, but these architectural limitations no
longer obtain for the hardware, only internally within the compilers.  There
is nothing that "just can't" be done; there are things that we do not feel
it is appropriate to do at this time (and we reserve the right to change our
minds!).

One such limitation affects COBOL74, for example.  No elementary item in a
record can occur more than 65,535 "units" from the beginning of that record
(units may be digits, bytes or words depending on the USAGE of the field).
The reasons for this limitation date back to the requirements of a machine
instruction that is no longer used, and no longer apply.  We could increase
this limit, but it would be costly to do so as it pervades a number of
internal structures, and that pervasion carries some destabilization risk.
For the time being, then, for those users who find this particular limit
unduly onerous, I would personally suggest migration to COBOL85, to which
the limit does not apply.

Similarly, we could at least in theory implement nested programs and
de-editing as ANSI-85-compliant features of COBOL74.  But why should we
enhance our "trailing-edge-technology" compilers to provide these
features -- and risk reliability degradation or even increased resource
consumption --  for users who are not interested in these features, given
that we already have a compiler that supports them in the form of our
COBOL85?  Why go to all that trouble to provide a capability we're already
providing, and in a product defined as containing it in the first place?

As it stands now, there is no *standard* that has been promulgated for COBOL
beyond ANSI X3.23-1985 as amended by ANSI X3.23a-1989.  So far as I know,
the Unisys A Series COBOL85 compiler is completely compliant with those
standards.

What "later implementations" are there to implement until such time as a
draft standard is finally approved for that implementation?  Are there
approved amendments beyond ANSI X3.23a-1989?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 16)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3798CD70.DFAA7DD2@home.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37975FB9.ACD87343@home.com> <7n7sga$juq$1@mail.pl.unisys.com> <379780FC.A873E9A2@home.com> <7n8aj9$6io$1@mail.pl.unisys.com> <3797F1E5.46F0C819@home.com> <7nageh$38a$1@mail.pl.unisys.com>`

```
Chuck Stevens wrote:
> 
> The Unisys A Series COBOL74 and COBOL85 compilers were both built, first and
> foremost, in response to marketplace requirements, primarily the requirement.....

Chuck, thanks for helping bring this old guy up-to-date.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 16)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nb01g$f60@dfw-ixnews10.ix.netcom.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37975FB9.ACD87343@home.com> <7n7sga$juq$1@mail.pl.unisys.com> <379780FC.A873E9A2@home.com> <7n8aj9$6io$1@mail.pl.unisys.com> <3797F1E5.46F0C819@home.com> <7nageh$38a$1@mail.pl.unisys.com>`

```
Chuck Stevens <charles.stevens@unisys.com> wrote in message
news:7nageh$38a$1@mail.pl.unisys.com...
  <much snippage>
>
> As it stands now, there is no *standard* that has been promulgated for
COBOL
> beyond ANSI X3.23-1985 as amended by ANSI X3.23a-1989.  So far as I know,
> the Unisys A Series COBOL85 compiler is completely compliant with those
…[8 more quoted lines elided]…
>

Nothing to do with the majority of Chuck's post (for which I have
insufficient information to comment - except that it is relatively
consistent with how most other vendors have handled upgrades in both the
Standard and user requirements),
   BUT

Yes, there is an amendment that supercedes (sort-of includes) ANSI
X3.23a-1989 - it is ANSI X3.23b-1991 (as is indicated in the last digits, it
was approved in 1991).  It corresponds (or more accurately is reflected in)
FIPS-21-4 - and also has an ISO variation.

It is "commonly" known as the "Correction Amendment" - which is a little
misleading as it does include a FEW "substantive changes" from the previous
Amendment - and a few others that reflect "enhanced" understandings of
substantive changes that were first introduced in the '85 Standard and the
'89 Amendment.

If you need information on getting copies, let me know - or contact ANSI -
or your "local national body" - or FIPS.

I won't make too many comments about at least PART of UNISYS not knowing
this - as I do know quite well that UNISYS is represented on J4 and that I
am positive that its representative there is WELL aware of the '91
Amendment.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 17)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ni51a$nc1$1@mail.pl.unisys.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37975FB9.ACD87343@home.com> <7n7sga$juq$1@mail.pl.unisys.com> <379780FC.A873E9A2@home.com> <7n8aj9$6io$1@mail.pl.unisys.com> <3797F1E5.46F0C819@home.com> <7nageh$38a$1@mail.pl.unisys.com> <7nb01g$f60@dfw-ixnews10.ix.netcom.com>`

```
On 23 July 1999 at 5:08PM, William M. Klein wrote:

>Yes, there is an amendment that supercedes (sort-of includes) ANSI
>X3.23a-1989 - it is ANSI X3.23b-1991 (as is indicated in the last digits,
it
>was approved in 1991).  It corresponds (or more accurately is reflected in)
>FIPS-21-4 - and also has an ISO variation.

>It is "commonly" known as the "Correction Amendment" - which is a little
>misleading as it does include a FEW "substantive changes" from the previous
>Amendment - and a few others that reflect "enhanced" understandings of
>substantive changes that were first introduced in the '85 Standard and the
>'89 Amendment.

Thanks for the clarification, Bill, and my apologies to the list.  I should
have written "I am not aware of any standard ...".

>I won't make too many comments about at least PART of UNISYS not knowing
>this - as I do know quite well that UNISYS is represented on J4 and that I
>am positive that its representative there is WELL aware of the '91
>Amendment.


And I'm sure the folks who work on the A Series COBOL85 compiler are
intimately familiar with it as well!  ;-)  Yes, Unisys is indeed represented
on J4.  Remember that my primary focus is on keeping the "trailing-edge"
COBOL compilers running smoothly.

But from your description I would have to surmise that the '91 amendment
doesn't include significant enhancements intended to support OOP; if that
surmise is correct,  then my original point still obtains.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 16)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-07-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37994684.1710703@news1.ibm.net>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37975FB9.ACD87343@home.com> <7n7sga$juq$1@mail.pl.unisys.com> <379780FC.A873E9A2@home.com> <7n8aj9$6io$1@mail.pl.unisys.com> <3797F1E5.46F0C819@home.com> <7nageh$38a$1@mail.pl.unisys.com>`

```
On Fri, 23 Jul 1999 12:40:45 -0700, "Chuck Stevens"
<charles.stevens@unisys.com> wrote:

I'm taking a free ride on your thread Charles.....


I have looked closely at nested programs.  However, I have a strong
DISTASTE for them.  I see nothing that can be accomplished that is not
more clearly accomplished by separate subprograms in separate source
members.  

I had a nested program system dumped on me for examination for
conversion.   I declined, but it was because it was IMPOSSIBLE to
understand.  Copybooks embedded in the source, which program was the
main, how did it interact with the others, it was hard to follow even
with the animator.  I have no use for nested programs, ONLY because
from a maintenance standpoint, they are a nightmare.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 17)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379C66D3.DA75A38A@NOSPAMhome.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37975FB9.ACD87343@home.com> <7n7sga$juq$1@mail.pl.unisys.com> <379780FC.A873E9A2@home.com> <7n8aj9$6io$1@mail.pl.unisys.com> <3797F1E5.46F0C819@home.com> <7nageh$38a$1@mail.pl.unisys.com> <37994684.1710703@news1.ibm.net>`

```
Thane Hubbell wrote:

> I have looked closely at nested programs.  However, I have a strong
> DISTASTE for them.  I see nothing that can be accomplished that is not
…[8 more quoted lines elided]…
> from a maintenance standpoint, they are a nightmare.

I started this thread asking for good reasons to nest subprograms.  I am
halfway convinced by a couple of arguments, but not enough to persuade
the standards committee to accept one.  However, before I asked, I
thought of one reason which may be useful in our environment.  If I need
to write a single program/entity which needs two subschemata, I would
have to break it out into a program and a subprogram.  This would be a
candidate for considering a nested program.

I suspect things are different in PC land.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 18)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379d3783.260052939@news1.ibm.net>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37975FB9.ACD87343@home.com> <7n7sga$juq$1@mail.pl.unisys.com> <379780FC.A873E9A2@home.com> <7n8aj9$6io$1@mail.pl.unisys.com> <3797F1E5.46F0C819@home.com> <7nageh$38a$1@mail.pl.unisys.com> <37994684.1710703@news1.ibm.net> <379C66D3.DA75A38A@NOSPAMhome.com>`

```
On Mon, 26 Jul 1999 07:46:59 -0600, Howard Brazee
<brazee@NOSPAMhome.com> wrote:

>I started this thread asking for good reasons to nest subprograms.  I am
>halfway convinced by a couple of arguments, but not enough to persuade
…[6 more quoted lines elided]…
>I suspect things are different in PC land.

Not really. I live in both worlds.  What if you want to reuse the
subprogram.  If nested, you are linking in the whole shebang or
re-including it in a new program. So now you have nested programs that
are --- copybooks.  What a nightmare.  No thanks!
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 16)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-07-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Vl_n3.39828$K65.105190@news2.mia>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37975FB9.ACD87343@home.com> <7n7sga$juq$1@mail.pl.unisys.com> <379780FC.A873E9A2@home.com> <7n8aj9$6io$1@mail.pl.unisys.com> <3797F1E5.46F0C819@home.com> <7nageh$38a$1@mail.pl.unisys.com>`

```
Good post Chuck, Thanks!

I have a question that I started to send to you by e-mail, but thought
some other C.L.C readers might be interested.  My clients who use Unisys
A Series all still use COBOL74 almost exclusively, because of the longer
compile times with COBOL85, and partly from inertia.  Could you tell us
exactly what the reason for the speed difference is, how significant it
is, and if we can expect any relief in that area?  If my clients could
expect comparable compile times, I might convince them to overcome the
inertia.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 10)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-07-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37997EBB.9F638EC7@zip.com.au>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia>`

```
Judson McClendon wrote:
> 
> James J. Gavan wrote:
…[9 more quoted lines elided]…
> concept of 'objects' being necessary.

Judson,

I have been struggling with this question.  I believe in the concept
of OO but it is really difficult to 'convert' from procedural.

I believe the OO is the wave of the future, not due to written
efficiency (which ultimately will be better) or execution speed but
better design.

Take where I work:

	Customer has:
   Phones   Internet   rebill   ...

The would be better stated as

    Customer has services

Services have various types phones, internet, rebill, etc.

You could/should build you system this way but ultimately it is easier
to add more and more code and not reconstruct the original design. If
it is OO you can use polymorphism to rebuild the design after it is
built with something different in mind.

ken
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 11)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-07-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ncemp$n8g$1@news.hitter.net>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au>`

```

Ken Foskey wrote in message <37997EBB.9F638EC7@zip.com.au>...
>Judson McClendon wrote:
>>
…[10 more quoted lines elided]…
>> concept of 'objects' being necessary.

Ahh! But not all of us are Judsons! ;-)

I find that thinking about objects helps to clarify both the structure
of the data and procedures. IOW, OOD helps me to make better
design choices for modular programs. However, I do question the
viability of OOP for most COBOL programming tasks.

Consider the following psuedocode:

For each (Customer, Employee, Transaction, etc.)
    Process the data

The OOP approach will have some overhead at the beginning
of the loop to allocate memory for the object (data) and to fill that
object from one or more records. It will also have overhead
at the end of the loop to free the memory.

An SD/MP approach uses statically allocated memory.

Both execute the same code at the lowest level.

This means that an OOP solution will require more time to
execute than the corresponding SD/MP program. In fact, if
the process time is the same as the OOP overhead, the program
will run twice as long. For batch and transaction processing, it
does not make sense to use "half-fast" OOP! :-)

OTOH, for the following psuedocode:

Load all the data
While not done
    Do whatever is required
Save the results

The OOD/OOP approach will almost certainly prove to be
superior. This is because the general statement more closely
matches the types of problems for which OOP was designed;
that is, modeling and simulation. Though it applies equally well
to interactive tasks such as, word processing, spreadsheets,
graphics, drawing, etc.

>Judson,
>
…[21 more quoted lines elided]…
>built with something different in mind.

The concept of data abstraction is not solely the province of OOP.
It may be accomplished easily in COBOL by using REDEFINES.
Consider the following:

01 Customer-Record.
   03 .... Some general customer data
   03 Customer-Services. *> this is the data abstraction place holder
        05 Customer-Services-Type Pic X.
            88 Customer-Phone-Services Value "A".
            88 Customer-Internet-Services Value "B".
            88 .... Other services Value ?
        05 Customer-Services-Data Pic X(??).
        05 Customer-Phone-Data
                    REDEFINES Customer-Services-Data.
            07 ... Whatever data is required
        05 ... Other services data
                    REDEFINES Customer-Services-Data.
    03 ... Other data abstractions

Does this meet the data requirements of your Services abstraction?

Polymorphism is one of those OO words whose concept is far
more confusing than clarifying. That is because the concept is
explained in terms of an OOPL rather than the simpler concepts of
SD/MP. Consider calculating the pay for employees who have
different pay classifications. OOP requires that you first create an
abstract class with a method, say, "calculatePay". Then for each
sub class, you provide the data definitions used by that sub class
and override the "calculatePay" method to provide the calculations
for the concrete sub class. Ultimately, you include the abstract class
as a 'contained' class within the definition of the employee class.

[For a SD/MP implementation, the method for including the pay class
data in the employee record was given above.]

The SD/MP polymorphic "methods" solution is quite simple.

    ...
    Call "calculatePay" using Employee-Record, Pay-Record
    ...

program-id. calculatePay. *> this is the method
...
procedure division using Employee-Record, Pay-Record.
    Evaluate true *> this is an implementation of Polymorphism
        When Salaried
            Perform calculateSalariedPay
        When Hourly
            Perform calculateHourlyPay
        When Commisiioned
            Perfornm calculateCommisionedPay
        When other
            *> Flag the pay record with an error and reason code
    End-Evaluate
    Exit Program
    .

*> These paragraphs have the code that would be in the methods
*> of the individual sub classes
calculateSalariedPay.
    ....
calculateHourlyPay.
    ....
calculateCommisiionedPay.
    ....

OO advocates claim that is easier to add new types in an OOPL
than in SD/MP. Is it clear that adding a Tip pay class to the above
code (and to the Employee-Record) would be relatively painless?
Perhaps even less painful than adding the same pay class
to OO COBOL?

Not everything about OOPLs is negative. One of the good features
of OOPLs is enforced encapsulation. In the above examples, the
Customer and Employee records are exposed everywhere.
There are cases where some data may need protection. Placing
that data in a CLASS with PROPERTY methods to control access
may be a necessary and wise precaution. This also could be
accomplished using SD/MP but would require more work than
is required by OO COBOL.

The bottom line is that OO is not the wave of the future. It is simply
another means for solving problems. What OOD provides is a
means for looking at those problems in a different light and for
simplifying the understanding of certain classes of complex
problems. Whether to implement the solution in an OOPL is a
decision best left to the implementor; but one must not choose
OOP based upon hype nor dismiss it out-of-hand. However, for
most COBOL solutions, I think OOP is unnecessary.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 12)_

- **From:** "Warren Simmons" <w.g.simmons@worldnet.att.net>
- **Date:** 1999-07-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ncutf$qki$1@bgtnsc01.worldnet.att.net>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net>`

```
Thanks, Rick.  I knew if I waited long enough someone would explain
OOP/OO/OOPL in a manner I could begin to grasp.  All of those $10 words keep
confusing me.  You've done a great service. However, now I need to decipher
SD/MS or what ever that was.<G>

Warren Simmons

Rick Smith <ricksmith@aiservices.com> wrote in message
news:7ncemp$n8g$1@news.hitter.net...
>
> Ken Foskey wrote in message <37997EBB.9F638EC7@zip.com.au>...
…[5 more quoted lines elided]…
> >> >stored Imperial, but can be displayed/entered in Imperial/Metric).

------------------------cliped most so it will not be repeated
here.---------------------

> Consider the following psuedocode:
>
…[3 more quoted lines elided]…
> The OOP approach will have some overhead at the
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 13)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379A270D.A801207A@home.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <7ncutf$qki$1@bgtnsc01.worldnet.att.net>`

```
Warren Simmons wrote:
> 
> Thanks, Rick.  I knew if I waited long enough someone would explain
> OOP/OO/OOPL in a manner I could begin to grasp.  All of those $10 words keep
> confusing me.  You've done a great service. However, now I need to decipher
> SD/MS or what ever that was.<G>

Nicely put Warren. Was a time when us two fuddy-duddies could buy a bar
of chocolate for a penny. Just to bring your $10 words up-to-date - this
zinger was thrown at me the other day - so I asked for explanation.

Quote : UML is "Unified Modelling Language" - an OO Design and Analysis
tool which tries to display various graphs of an OO application (use
cases, timelines etc.) It's actually quite useful, if you treat it as
one of many tools. "UML Distilled - Applying the Standard Object
Modelling Language" by Fowler (with Scott), published by Addison-Wesley.
End Quote :

Rick Smith wrote :

>..decision best left to the implementor; but one must not choose
>OOP based upon hype nor dismiss it out-of-hand. However, for
> most COBOL solutions, I think OOP is unnecessary.

Rick, I concur with Warren. Nicely put with the pros and cons - having
made your deliberations you then conclude - not for me at current time.
In dollars and cents, had I known they were going to jack the price up 
from VISOC to NetExpress, I would have gone with Fujitsu and to hell
with OO.

You might recall I said earlier "you can go ape over OO technology,
taken to its extremes" and you show this in your examples. Armed only
with the tools then available within VISOC I followed the OO/GUI route.
Agreed, much of what I'm doing could be done in structured. But purely
for a consistent programming style I've stuck with the OO framework as
the Imperial/Metric source shows. (Looking at others' code for N/E it is
a grab-bag of styles, structured, entry points, OO, Dialog System).
Thinking in one writing style makes it much easier to have a consistent
approach and get the results you want.

I'll concede Judson one point, overall it is not intuitive - you have
got to take your head and jerk it 180 degrees. It is a different
thinking process. Get beyond the initial process, then individual
classes and methods can be simplistic. (Didn't occur to me, until after
I sent it - did anyone observe that I don't use working-storage or
local-storage variables in the example source ?)

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 13)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-07-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ncql5$1111$1@news.hitter.net>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <7ncutf$qki$1@bgtnsc01.worldnet.att.net>`

```

Warren Simmons wrote in message <7ncutf$qki$1@bgtnsc01.worldnet.att.net>...
>Thanks, Rick.  I knew if I waited long enough someone would explain
>OOP/OO/OOPL in a manner I could begin to grasp.  All of those $10 words
keep
>confusing me.  You've done a great service. However, now I need to decipher
>SD/MS or what ever that was.<G>

SD/MP - Structured Design / Modular Programming

Both are very familiar terms.

Many would call it SD/SP; but a few weeks ago, I gave my
explanation as to the differences between Modular Programming
and Structured Programming. I happen to think that, in most cases,
MP is the more correct phrase.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 12)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379C6CAF.97BB9A4E@NOSPAMhome.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net>`

```
Rick Smith wrote:

> This means that an OOP solution will require more time to
> execute than the corresponding SD/MP program. In fact, if
> the process time is the same as the OOP overhead, the program
> will run twice as long. For batch and transaction processing, it
> does not make sense to use "half-fast" OOP! :-)


I'm not worried about such efficiency in a new methodology.  Pure power
is getting cheaper and cheaper.

> 
> OTOH, for the following psuedocode:
…[11 more quoted lines elided]…
> graphics, drawing, etc.

Insufficient.  Just because a tool was designed to match a problem
closer than other tools, does not mean that that tool is the best tool
for that problem.

> The bottom line is that OO is not the wave of the future. It is simply
> another means for solving problems. What OOD provides is a
…[7 more quoted lines elided]…
> Rick Smith

It is really useful to plug into other OO elements of a system.

My big objection to OO in an enterprise environment is that I want each
and every "word" in my program to work exactly the same way each time I
use it.  I want a guarantee that it's debugged and won't change on me.  
A library based language is hard in that there are an infinite amount of
"words" to learn, and one with "live" libraries is one where my critical
programs need to be tested and retested every time some changes are
made.  (I know OO advocates claim otherwise - but I'm not ready to pass
my critical systems on their unit testing).

A smaller objection is that layered commands within non-linear objects
can be hard to find and debug.  Of course, they're bug free, right!?!?
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 13)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nimtb$76l$1@news.hitter.net>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com>`

```

Howard Brazee wrote in message <379C6CAF.97BB9A4E@NOSPAMhome.com>...
>Rick Smith wrote:
>
>> This means that an OOP solution will require more time to
>> execute than the corresponding SD/MP program.
[...]
>I'm not worried about such efficiency in a new methodology.  Pure power
>is getting cheaper and cheaper.

About two weeks ago, there was a discussion in comp.lang.c
concerning a hashing algorithm in Kernighan's new book,
Software Practice. The alogorithm was given in both C and
C++/OOP. The C++/OOP version was 35 times slower than
the C version. Some C++ users lowered the figure to only 40%
slower than C. [The preceding is from memory; but the
important stuff is accurate.]

Now, 10%, 20%, even 40% slower may be tolerable under
some conditions; but it is possible that naive OOP
implementations may run multiples of times slower.

Is that tolerable?

How many organizations are prepared to double or triple
their processing power to use OOP? How many believe
that it may be required?

[...]
>> ... This is because the general statement more closely
>> matches the types of problems for which OOP was designed;
>> that is, modeling and simulation. Though it applies equally well
>> to interactive tasks such as, word processing, spreadsheets,
>> graphics, drawing, etc.

>Insufficient.  Just because a tool was designed to match a problem
>closer than other tools, does not mean that that tool is the best tool
>for that problem.

Perhaps you could clarify your statement.

Languages are tools; but OO is a technology that can be
applied to languages. Where one combines a technology
with a tool, one should have a better tool for solving those
classes of problems where the technology fits.

It seems to me that you are saying that "a better tool is not
necessarily the best tool" and this is confusing to me.

[...]
>It is really useful to plug into other OO elements of a system.
>
…[10 more quoted lines elided]…
>can be hard to find and debug.  Of course, they're bug free, right!?!?

I have always had a big problem with class design issues.

The brief examples given in texts are easily broken in real
applications and the examples of real applications are
easily broken when extended.

I think I may have found a solution for unbreakable classes
in one special case; but I need to test the solution for other
cases.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 14)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379D20DB.F1C0A612@home.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <7nimtb$76l$1@news.hitter.net>`

```
Rick Smith wrote:
> 
> The C++/OOP version was 35 times slower than
…[13 more quoted lines elided]…
> 
The simple answer is a big NO! Possibly 20% is the most tolerable figure
one should accept. (Don't want to keep plugging MicroFocus, but to
reiterate, their IDE is 90% OO/GUI - and they aren't thinking of
changing it. It is just too damn good a tool).

I'm not into the C languages, so how were the two examples written.
Quite simply OO is another tool. As Michael Mattias said once , "It's
the artist, not the paintbrush", although I'll expand that to "It's the
artist with a good set of paintbrushes".

Example - simple structured program updating the General Ledger.
Extremely well-written and documented by a very junior programmer. Took
over two hours to run on a mainframe. Give the problem to a seasoned
programmer to look at; with about four lines of code change he reduced
it to a runtime of one hour.

If there were benchmarks for OO COBOL it may well prove that there are
deficiencies in the OO approach - but until there are, it remains
conjecture. Having established OO "canned-routines" that definitely work
- I can sleep well at night. 

We see examples of people saying this program is "large" or this table
is "large" - as a Systems Manager I can assure you I would have said,
"Go away and have a re-think guys - not too happy with your word
'large'". OO design has to be just as practical as Structured design and
the efficiencies/deficiencies of a particular tool must be weighed
against the application and machine being used.

There is no 'right' way, but many 'good' ways.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 15)_

- **From:** "Warren Simmons" <w.g.simmons@worldnet.att.net>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7njcic$cjd$1@bgtnsc01.worldnet.att.net>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <7nimtb$76l$1@news.hitter.net> <379D20DB.F1C0A612@home.com>`

```
And, we used to say, "there is always a better way."

Warren Simmons
James J. Gavan <jjgavan@home.com> wrote in message
news:379D20DB.F1C0A612@home.com...
> Rick Smith wrote:
> >
…[45 more quoted lines elided]…
> Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 15)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nk26a$4k4$2@news.hitter.net>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <7nimtb$76l$1@news.hitter.net> <379D20DB.F1C0A612@home.com>`

```

James J. Gavan wrote in message <379D20DB.F1C0A612@home.com>...
>Rick Smith wrote:
>>
…[4 more quoted lines elided]…
>>
[...]
>I'm not into the C languages, so how were the two examples written.

I never saw the code for either solution; but it is likely that
the Kernighan example placed the data in a class that was
frequently instantiated and destroyed causing a lot of
memory allocation overhead. The solution likely involved
moving the object data into static structures. In C++ all
structures are classes. This would eliminate the memory
allocation overhead allowing the algorithm to run much faster.

Relating this to OO COBOL, we could imagine a program
with three nested loops. Both the outer and middle loops
might cost 20%, a tight inner loop could cost 100% giving
an overall loss of 144% or running 2.44 times longer. By
eliminating objects from the tight inner loop, the overall loss
drops to 44%. But, if the outer loop selects a small number
of objects to be processed in the middle and inner loops,
the overall loss approaches 20%.

How and where objects are used is the problem. One who
is trained to create everything as classes ("gung ho OO") is
more likely to create slow running OO programs.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 16)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nkprd$peg$1@news.hitter.net>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <7nimtb$76l$1@news.hitter.net> <379D20DB.F1C0A612@home.com> <7nk26a$4k4$2@news.hitter.net>`

```
I should have checked my multiplication.

Rick Smith wrote in message <7nk26a$4k4$2@news.hitter.net>...
[...]
>Relating this to OO COBOL, we could imagine a program
>with three nested loops. Both the outer and middle loops
>might cost 20%, a tight inner loop could cost 100% giving
>an overall loss of 144% or running 2.44 times longer.

This should read "an overall loss of 188% or 2.88 times longer."
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 14)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379DBAAF.A673663D@NOSPAMhome.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <7nimtb$76l$1@news.hitter.net>`

```
Rick Smith wrote:

> >> ... This is because the general statement more closely
> >> matches the types of problems for which OOP was designed;
…[16 more quoted lines elided]…
> necessarily the best tool" and this is confusing to me.

What I'm saying is that even if the intention of the tool is to match a
problem more closely than other tools do - it may not be the best tool
for solving that problem.  Reasons:  
The implementation of that intention may be lacking.
A problem as defined is never (well hardly ever) isolated.  Other issues
such as efficiency and maintenance effect which tool is better even if
you main issue is "modeling".
Other tools may better simply because their users are more competent
with them.
I could go on, but I think you understand my point.

A mountain bike is a tool designed to take someone over a mountain.
A pick-up truck isn't designed so specifically.  But sometimes, I would
prefer to use a pick-up truck to get me over that mountain.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 15)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nkdst$f24$1@news.hitter.net>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <7nimtb$76l$1@news.hitter.net> <379DBAAF.A673663D@NOSPAMhome.com>`

```

Howard Brazee wrote in message <379DBAAF.A673663D@NOSPAMhome.com>...
[...]
>I could go on, but I think you understand my point.

Fair enough!

>A mountain bike is a tool designed to take someone over a mountain.
>A pick-up truck isn't designed so specifically.  But sometimes, I would
>prefer to use a pick-up truck to get me over that mountain.

Hmmm! I haven't seen a mountain, up close and personal, for
over twenty years. So I guess my mountain bike is really an
off-road bike. But I haven't even used for that since the
incident with the rather steep decline into sand. I kept my
balance and made it through without injury -- I just don't ever
want to repeat the experience.

[For those who have never ridden a mountain bike in such
terrain. Imagine, if you will, the profile of a person riding over
the edge of a flat surface on to a sharp decline. To prevent
being thrown over the handlebars during the descent and
also to prevent planting the front tire in the sand, one must
move the center of gravity well back and as low as possible.
For me, this meant moving my pelvis to a position behind
and below the seat. There is no fender to prevent contact
between one's clothing (or that which the clothing covers)
and the knobby surface of the rotating rear tire.]

Even when tools, such as programming languages, are used
as designed; there is no assurance that the results will be
satisfactory; that much is a given. There is also no assurance
that technologically enhanced tools will provide more satisfactory
results. Like the technological enhancements that allow mountain
bikes to do more than regular bikes; OO COBOL may simply
allow one to get into that much more trouble.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 13)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379C9AE3.E9EA0995@home.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> I'm not worried about such efficiency in a new methodology.  Pure power is getting cheaper and cheaper.

I can't argue for or against OO speed. But I buy into your comment
regardless of whether it is mainframe or PC. I'm prepared to sacrifice a
'little' speed given the incremental power of each new phase of EDP
technology. Besides which, if it becomes apparent that a number-cruncher
program is taking two hours instead of one - the application can be
fine-tuned - and perhaps different methodology added for that specific
program). Regardless of speed, I am adamant in my thoughts that file
data should be stored in the most economical way. 
 
> My big objection to OO in an enterprise environment is that I want each
> and every "word" in my program to work exactly the same way each time I
…[6 more quoted lines elided]…
>
A very valid comment, which is why I think it is so very important to
have compiler developers on the same wavelength when organizing their
class structures and what the classes do. They can use different coding
within a method, but they must return the same results - exactly the
same result you and I expect from compute a = b + c, regardless of
compiler. 

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 14)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379CA768.67F1B445@NOSPAMhome.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <379C9AE3.E9EA0995@home.com>`

```
James J. Gavan wrote:

> > My big objection to OO in an enterprise environment is that I want each
> > and every "word" in my program to work exactly the same way each time I
…[14 more quoted lines elided]…
> Jimmy, Calgary AB

What's hard is that it's ALWAYS possible to enhance class libraries. 
MicroSoft went for a lowest common denominator, Sun is more ambitious,
but we have had multiple "standard" ways for standard objects to work. 
Let's say you want to work with more vendors supplying objects than the
standard makers.  Things will break.

Of course compiled languages also break when compute a = b + c when the
new compiler handles signs or overflows differently, but this seems
easier to find to me.

Today I was looking at a S9(8) COMP field which I displayed in COBOL for
MVS.  This was a db-key and when I used a tool to look for that database
record, the number didn't make sense.  The DISPLAY command truncated the
high-order bytes.  The compiler should have been smart enough to make
its required fields large enough to hold the largest number which a
S9(8) COMP could hold.  It had the overflow error, not me.
```

###### ↳ ↳ ↳ Truncation of COMP fields was Re: Multiple programs in one source

_(reply depth: 15)_

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379CCF76.A2D3E556@nbnet.nb.ca>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <379C9AE3.E9EA0995@home.com> <379CA768.67F1B445@NOSPAMhome.com>`

```
Howard:

Check your compile options.  The truncation you describe is required if
the option is TRUNC(STD) to conform to the standard.  It also is
implemented that way if you specify TRUNC(OPT) which conforms to the
standard for everything except BINARY to BINARY and literal to BINARY
with no Packed decimal and no usage DISPLAY operands.  If you had
specified TRUNC(BIN), the DISPLAY verb would have shown 10 digits. 
There are some interesting work-arounds to give you that with TRUNC(OPT)
involving use of double word S9(10) BINARY fields.

Clark Morris, CFM Technical Programming Services morrisc@nbnet.nb.ca 

Howard Brazee wrote:
> 
> James J. Gavan wrote:
…[11 more quoted lines elided]…
> S9(8) COMP could hold.  It had the overflow error, not me.
```

###### ↳ ↳ ↳ Re: Truncation of COMP fields was Re: Multiple programs in one source

_(reply depth: 16)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379CD3A3.2794BF19@NOSPAMhome.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <379C9AE3.E9EA0995@home.com> <379CA768.67F1B445@NOSPAMhome.com> <379CCF76.A2D3E556@nbnet.nb.ca>`

```
I was guessing I could fix the problem, if I were allowed to change my
compile options, you seem to confirm my guess.  I did a work-around, but
since the compiler picks the work fields for a display, the compiler
should be smart enough to pick work fields large enough to handle the
fields being displayed.  Period.  

Let me worry about the fields I pick to make sure they fit my compiler
options.  But the compiler should handle about the fields it picks.

Clark Morris wrote:
> 
> Howard:
…[26 more quoted lines elided]…
> > S9(8) COMP could hold.  It had the overflow error, not me.
```

###### ↳ ↳ ↳ Re: Truncation of COMP fields was Re: Multiple programs in one source

_(reply depth: 17)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nimcv$e31@dfw-ixnews10.ix.netcom.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <379C9AE3.E9EA0995@home.com> <379CA768.67F1B445@NOSPAMhome.com> <379CCF76.A2D3E556@nbnet.nb.ca> <379CD3A3.2794BF19@NOSPAMhome.com>`

```
Howard Brazee <brazee@NOSPAMhome.com> wrote in message
news:379CD3A3.2794BF19@NOSPAMhome.com...
> I was guessing I could fix the problem, if I were allowed to change my
> compile options, you seem to confirm my guess.  I did a work-around, but
…[5 more quoted lines elided]…
> options.  But the compiler should handle about the fields it picks.

This is one that I disagree with you completely on.  The entire "theory" of
the PICTURE clause in COBOL is that you *know and mean* what you say.  If
you say that something is

  Picture S9(08)

Then the compiler is not just justified - but is EXPECTED (by the ANSI/ISO
Standard) to believe you.  The only numbers that it should "believe" are
those last 8 (base-10) digits, not the binary "stuff" that fits into the
allocated space. The fact that you are using COMP (not USAGE BINARY) does
mean that you are in an "implementor-defined" part of COBOL, but I really,
REALLY, do not want the compiler to start "ignoring" your PICTURE clause and
start believing its own internals.  This is why the new USAGES (for "true
binary") explicitly do NOT have (allow) the use of a PICTURE clause.
Instead, there are separate USAGEs for each "storage size" of such fields.
```

###### ↳ ↳ ↳ Re: Truncation of COMP fields was Re: Multiple programs in one source

_(reply depth: 18)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379DBE28.A49F0C3B@NOSPAMhome.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <379C9AE3.E9EA0995@home.com> <379CA768.67F1B445@NOSPAMhome.com> <379CCF76.A2D3E556@nbnet.nb.ca> <379CD3A3.2794BF19@NOSPAMhome.com> <7nimcv$e31@dfw-ixnews10.ix.netcom.com>`

```
William M. Klein wrote:
> 
> Howard Brazee <brazee@NOSPAMhome.com> wrote in message
…[28 more quoted lines elided]…
>     wmklein <at> ix dot netcom dot com

You're absolutely right.  In this case it is Cullinane which was the
user which called it S9(8) COMP.  (Now owned by CA), but I should have
realized that they were using a larger number than what they stated.
```

###### ↳ ↳ ↳ Re: Truncation of COMP fields was Re: Multiple programs in one source

_(reply depth: 16)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nm46a$qjo@dfw-ixnews7.ix.netcom.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <379C9AE3.E9EA0995@home.com> <379CA768.67F1B445@NOSPAMhome.com> <379CCF76.A2D3E556@nbnet.nb.ca>`

```
I wasn't certain about this - but my initial reading of Clark's
understanding of TRUNC(OPT) was that it was "close" but not quite right.  I
don't have absolute confirmation on this (yet), but I do have the following
from one of my "usually reliable sources",

" I do not believe that Clark is right...the rules for TRUNC(OPT) are that
we
generate the most efficient code, regardless of whether truncation is
required
by the Standard or not.  We never generate extra code to truncate for
TRUNC(OPT)."
```

###### ↳ ↳ ↳ TRUNC (was Multiple programs in one source

_(reply depth: 15)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nildo$dl0@dfw-ixnews10.ix.netcom.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <379C9AE3.E9EA0995@home.com> <379CA768.67F1B445@NOSPAMhome.com>`

```
> James J. Gavan wrote:
>
  <much snippage>
>
> Today I was looking at a S9(8) COMP field which I displayed in COBOL for
…[4 more quoted lines elided]…
> S9(8) COMP could hold.  It had the overflow error, not me.

This compiler is indeed smart enough to do that - but you need to tell it
the CORRECT value for the TRUNC compiler option.   If you really want it to
*guarantee* that a COMP (binary) field will always be capable of holding the
largest value that will fit in the allocated storage make certain that you
compile with TRUNC(BINARY).  This option violates the ANSI Standard for
"binary behavior" - but does give you what you want.  You should be aware,
however, that IBM says that this is a "dog" for performance - but does
guarantee what you want (or say you want).

P.S.  This note explicitly applies to IBM COBOL for MVS & VM (or IBM COBOL
for OS/390 & VM) - but almost every COBOL implementation that I know of has
its own variation of "TRUNC(BINARY)".  Also FYI, the next Standard will
include new datatypes that will provide "true binary" support so that the
contents will be dependent upon the storage allocated rather than any
PICTURE that the programmers specifies.
```

###### ↳ ↳ ↳ Re: TRUNC (was Multiple programs in one source

_(reply depth: 16)_

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C8D540A5B5A6E754.5080EF4D8306F56C.C48BA9F2B875EF46@lp.airnews.net>`
- **References:** `<37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net> <379C6CAF.97BB9A4E@NOSPAMhome.com> <379C9AE3.E9EA0995@home.com> <379CA768.67F1B445@NOSPAMhome.com> <7nildo$dl0@dfw-ixnews10.ix.netcom.com>`

```
On Mon, 26 Jul 1999 16:56:12 -0500, "William M. Klein"
<wmklein@nospam.netcom.com> enlightened us:

>> James J. Gavan wrote:
>>
…[23 more quoted lines elided]…
>PICTURE that the programmers specifies.

I'm wondering if the previous discussion is relevant to a problem I
recently encountered in a CICS Cobol (OS/390 MVS) program.  

I needed to set the length field of a temp storage READQ statement.
CICS requires this field to be a half-word (PIC 9(04) COMP).  The
length of the queue in decimal was 14,400 or 3840 in hex.  In
Working-Storage I defined a field thus:

05  WS-QUEUE-LENGTH     PIC 9(04)  COMP  VALUE 14400.

Now if I remember correctly I got a compiler error on the field.  I
worked around it by defining the following:

05  WS-QUEUE-LENGTH-DBL   PIC S9(08)  COMP  VALUE 14400.
05  WS-QUEUE-LENGTH-FIELDS  REDEFINES  WS-QUEUE-LENGTH-DBL.
      10   FILLER                           PIC S9(04)  COMP.
      10  WS-QUEUE-LENGTH-HALF  PIC S9(08)  COMP.

I then used WS-QUEUE-LENGTH-HALF as my length field in the CICS
command to read the temp storage queue.  

It seems rather awkward that even though 14400 would in hex fit nicely
into a PIC 9(04) COMP field, the compiler wasn't smart enough to
figure that out.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Some days your the dog.  Some days your the hydrant.


 Steve
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 12)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2g_m3.404$K65.4533@news2.mia>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia> <37949F1E.602548B9@home.com> <i83l3.3060$_f5.30095@news3.mia> <3794D221.15FF9397@home.com> <TNkl3.4715$Kk.39268@news2.mia> <379654EC.FD57917B@home.com> <mCGl3.2309$xN4.21583@news3.mia> <37997EBB.9F638EC7@zip.com.au> <7ncemp$n8g$1@news.hitter.net>`

```
Rick, that is a very good post, thanks.  Your last paragraph sums up
my opinion of OO very well.  It also explains why some people think
it is the greatest thing since sliced bread, while others think it
stinks, and why many attempts at OO based projects fell flat.  OO is,
like any other tool ever devised by man, good for some things, and
not so good for others.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 4)_

- **From:** Jared Thomas <jared@techie.com>
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3796639D.E3E58E40@techie.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <r0%k3.2575$_f5.26236@news3.mia>`

```
One tiny detail about COBOL internal subroutines.  Some, but not
*all* can be compiled externally.  The difference is if variables
are exposed in the calling program (GLOBAL clause) or not.  The
compile of the inner program fails when compiled standalone
because the definitions in the outer program are not available.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n2o56$5l3$1@mail.pl.unisys.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com>`

```
Howard Brazee wrote in message <37937B17.2E9B2D6A@NOSPAMhome.com>...

>OK.  So when do you want this better isolation badly enough to get drop
>the simplicity of PERFORM?  When the program isn't debugged?


I've seen monolithic COBOL programs with 500,000 source lines and COBOL's
traditional "planar" data storage.  It would indeed make such a program
easier both to debug and to maintain if the data were  "cospatial" with the
code, and is considered immaterial (or even nonexistent) if it's not
required to be "persistent" between procedure calls.

Also, on some machines, the amount of information that can be maintained
current has some limit, based perhaps on some memory allocation scheme.
Having data spaces associated automatically with subsections of the program
by the system software (including the compiler) drastically reduces these
resource requirements.

ALGOL, and its descendant Pascal, and even to some degree PL/1, demonstrated
that this approach to program design has much to recommend it, particularly
for very complex programs.

Consider, for example, a hypothetical COBOL compiler itself written in
COBOL.  Is there any particular necessity for the compiler variables
associated with PICTURE clause parsing to be "hanging around" while
generating code for a COMPUTE statement?  Would it not make debugging or
maintenance of such a hypothetical COBOL compiler easier if the maintenance
programmer didn't have to wade through all (or even any of)  the data
related to the last PICTURE clause that was parsed in order to find his
COMPUTE code generation problem?

Such are the mechanisms provided by "nested programs" introduced with the
1985 standard for COBOL, in response to the requests of those who had been
exposed to "block-structured" languages and found the benefits of such an
*automatic* association of data with code appropriate to the COBOL
environment.

        -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3794F514.18707BAB@home.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <7n2o56$5l3$1@mail.pl.unisys.com>`

```
Chuck Stevens wrote:
> 
> 
> Consider, for example, a hypothetical COBOL compiler itself written in
> COBOL.  Is there any particular necessity for the compiler variables
> .........

Why keep it hypothetical ? Isn't it about time we had a COBOL compiler
with our own COBOL virtual machine.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n2v8n$lq4@dfw-ixnews5.ix.netcom.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <7n2o56$5l3$1@mail.pl.unisys.com> <3794F514.18707BAB@home.com>`

```

James J. Gavan <jjgavan@home.com> wrote in message
news:3794F514.18707BAB@home.com...
> Chuck Stevens wrote:
> >
…[8 more quoted lines elided]…
> Jimmy, Calgary AB


As often pointed out (in and out of this NG), the Micro Focus COBOL compiler
*is* written in COBOL (and has been for a long LONG time).
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3795CD41.E65E9399@NOSPAMhome.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <7n2o56$5l3$1@mail.pl.unisys.com> <3794F514.18707BAB@home.com>`

```
> > Consider, for example, a hypothetical COBOL compiler itself written in
> > COBOL.  Is there any particular necessity for the compiler variables
…[5 more quoted lines elided]…
> Jimmy, Calgary AB

Why?  Who would buy this or put in a COBOL virtual machine?   COBOL is a
compiled language anyway.

There IS a version of COBOL which compiles into Java bytes.  Pretty soon
Java virtual machines will be ubiquitous.  IBM plans to have them on all
of their machines.  Go with the standard and let your COBOL objects
interface with everybody else's objects.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-07-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37972C34.86429137@zip.com.au>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <7n2o56$5l3$1@mail.pl.unisys.com> <3794F514.18707BAB@home.com> <3795CD41.E65E9399@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> > > Consider, for example, a hypothetical COBOL compiler itself
…[15 more quoted lines elided]…
> objects interface with everybody else's objects.

I think the point of having a open compiler is that new technology can
be developed without waiting for the compiler vendors to prove it is
possible.  This will effectively force the vendors to follow the real
users (us).

The point of having it in cobol source is that anyone that uses the
compiler will be able to modify the compiler to do what they want.

I believe that the simplest way (in the short term) is to have a cobol
precompiler (of sorts) that takes in 'GNU' Cobol and outputs to
whatever dialect your compiler supports.  Eventually this could create
actual run time code but that is a long way off IMHO.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37974FEB.53BF7CDF@home.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <7n2o56$5l3$1@mail.pl.unisys.com> <3794F514.18707BAB@home.com> <3795CD41.E65E9399@NOSPAMhome.com> <37972C34.86429137@zip.com.au>`

```
Ken Foskey wrote:
> 
> Howard Brazee wrote:
…[7 more quoted lines elided]…
> > a compiled language anyway.

Howard,

Sorry to be T-H-I-C-K, (what do you expect from a former systems
analyst), but please clarify for me where you say 'COBOL is a compiled
language anyway'. From my limited knowledge BASIC was an interpretative
language - aren't all the others compiled (use a different word for
'compiled' if you wish).

In this thread and others, reference OO, I've been saying "I guess", "I
don't know". And in a message to Judson I said in effect, "I hadn't
noticed any degradation in performance using OO". Well I went to the
source, (Newbury) and this is the answer from the horse's mouth (purely
provided for info - not discussion) :-

I wrote that with OO you establish an object reference handle to a
class, then I 'guessed' there were pointers to the methods, and as a 
wild thought, suggested there might be caching.

> .....
> Can't give away too many secrets about how the run-time is 
…[10 more quoted lines elided]…
> code should be faster than multiple CALLs.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37977739.4AA803E8@NOSPAMhome.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <7n2o56$5l3$1@mail.pl.unisys.com> <3794F514.18707BAB@home.com> <3795CD41.E65E9399@NOSPAMhome.com> <37972C34.86429137@zip.com.au> <37974FEB.53BF7CDF@home.com>`

```
James J. Gavan wrote:

> > > Why?  Who would buy this or put in a COBOL virtual machine?   COBOL is
> > > a compiled language anyway.
…[7 more quoted lines elided]…
> 'compiled' if you wish).

Well, Rexx is interpreted, Pascal uses P-code, and Java uses a more
advanced kind of p-code.  The JVM understands Java Bytes and translates
them into machine language at run time.  A compiled language translates
its commands into machine language at compile time.  I know terms get
confusing as the technologies merge and separate, but this old
terminology is what I was meaning.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

_(reply depth: 4)_

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3794F418.33644953@nbnet.nb.ca>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <UVJk3.971$ng2.5648@news2.mia> <37937B17.2E9B2D6A@NOSPAMhome.com> <7n2o56$5l3$1@mail.pl.unisys.com>`

```
One use that we have of nested programs at my current client is the
design of our callable date routine such that the source code for the
program is in a copybook in the copy library.  The "source library"
member is just a COPY datertn.  The normally batch use is as a
separately compiled and linked program.  The use in CICS is as a nested
program where the last two statements of the program are "COPY datertn."
followed by "END-PROGRAM calling-program-name".  If for performance
reasons we wanted to change a batch program to have this routine
embedded in it would be to add those two statements to the program and
recompile.  The difference in overhead between the intra-module call and
the dynamic call on IBM MVS had a fairly large per executed call
component (as opposed to the overhead for the initial establishment of
linkage).    

Chuck Stevens wrote:
> 
> Howard Brazee wrote in message <37937B17.2E9B2D6A@NOSPAMhome.com>...
…[9 more quoted lines elided]…
> snip
Clark Morris, CFM Technical Programming Services.
```

#### ↳ Re: Multiple programs in one source

- **From:** "Carlo Hogeveen" <hyphen@xs4all.nl>
- **Date:** 1999-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n027o$dic$1@news1.xs4all.nl>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com>`

```

It is called structured programming!

Having been Cobol 74 programmers for so long, we have become
blind to the concept of procedures with local variables.

Instead we bicker about whether to perform sections or paragraphs :-)

Sections and paragraphs are procedures without parameters or local variables.

Subroutines are procedures with both parameters and local variables,
and we "know" that subroutines are only useful when called by more
than one program, because subroutines are external, so we design them
that way, and it becomes a selffulfilling truth.

Well, we have Cobol 85 (and extensions) now with INTERNAL subroutines,
and there is a new truth in town.

Alas :-) Cobol 85 is backwards compatible with Cobol 74, so we can program
the way we used to, and what 's the use of these internal subroutines anyway?

In my case it is both a mental and a design problem.

First the mental problem.

In any other programming language I know, I  learned to use procedures
with local variables from the start and I wouldn't dream of putting all variables
in one place: my teachers would have (verbally) hurt me!

And yet, when I start to design a structured Cobol program
I keep coming up with Cobol 74 chunks: variableless procedures.

The way I try to break through this wall, is by first imagining how I would
attack the problem in structured language X, and then translate it in
my head to Cobol 85 procedures.

And now for the design problem.

What if we don't know any structured languages, how would we
find good candidates for Cobol 85 's internal subroutines?

My first rule: look at the data!

Is there data we can attach it's own program-specific procedure to?
I think of this as internal I/O: chunks that communicate with each other.
(Yeah, nicely heading towards OO, that can't hurt.).

Is there a record that must be handled in a for this program particular way?
Interface: record in, nothing out. Side effect: processing.
Local variables for dissecting and otherwise processing the record!

Is there a field that must be calculated using a for this program specific formula?
Interface: a few fields in, a result out. Local variables for intermediate results!

Is there a report to be printed?
Interface: fields for one detail-line in, nothing out. Side effect: report is printed.
Local variables for editing the detail-line to be printed and possibly for
printing page headers and accumulating and printing totals.

Page headers and totals are possible candidates for their own
procedures too.

All of the above are examples of possible program-specific subroutines.
Once a record is read, no two programs might handle it the same way.
No two programs will print the same report.
No two programs will handle the same screen.
A formula might be specific to a program or to an external subroutine.

And in general, of course, just like with external subroutines, we keep
in mind to search for procedures with high cohesion and low coupling.

Having said all this, of course sections and paragraphs won't both
disappear: they will still outnumber internal subroutines.


There can be a totally different reason to use internal subroutines
instead of external subroutines: speed!

A call to an internal subroutine is much faster that a call to an external subroutine.

One of our Cobol guru's extended the Cobol preprocessor to replace the
call to our most heavily used external subroutine, by building in and
calling that subroutine internally, and got a significant speed increase.


Carlo





Howard Brazee wrote in message <37932F22.A4751958@NOSPAMhome.com>...
I'm a mainframe programmer who has never worked in a location which has
more than one COBOL program in one source member.

When we have called programs, it is because several programs will be
doing the calling.

I suppose the called program can be in a copy library, but I also
haven't worked where compile time calls were standard.

The one place I can see a use for this is if only one program does the
call, and a perform won't work because the called program and calling
program use different subschemata.  (having fun with that word -
schemata is a dictionary plural for schema!!)

What am I overlooking?  What are the shops I have worked in overlooked?
```

##### ↳ ↳ Re: Multiple programs in one source

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37939CFA.2E7EAC5D@NOSPAMhome.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <7n027o$dic$1@news1.xs4all.nl>`

```
> And now for the design problem.
> 
…[31 more quoted lines elided]…
> in mind to search for procedures with high cohesion and low coupling.

Thank-you.
 
> Having said all this, of course sections and paragraphs won't both
> disappear: they will still outnumber internal subroutines.
> 
> There can be a totally different reason to use internal subroutines
> instead of external subroutines: speed!

Yes, but I would expect that paragraphs have the same advantage over
internal subroutines.
 

I think the biggest difficulties in moving to internal sub-programs are:

1.  More coding = more work.
2.  The advantages haven't shown to be big enough to be worth while
doing things differently in the minds of people making standards or
expecting others do do maintenance.  Is this what the maintenance
programmers see as KISS?  It will be once it is widely accepted in your
shop, but not before.
3.  Documentation procedures were designed for paragraphs which don't
need documenting.
4.  Debugging procedures often work poorly with called programs, giving
errors at the wrong location.
5.  Nobody wants to be the first to test their pre-compiler when they
have a deadline to complete a program. 
6.  When you try to justify experimenting with this, people will ask
about speed effects.

On the other hand, once a few sub-programs have been written and
included, our desire to cut, paste, and modify will mean that the NEXT
report program will come much more quickly.
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

- **From:** Jared Thomas <jared@techie.com>
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379662EF.1E3945E3@techie.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <7n027o$dic$1@news1.xs4all.nl> <37939CFA.2E7EAC5D@NOSPAMhome.com>`

```
I only use COBOL because I have to.  (My present job is 75% COBOL,
25% ASM, so I have to...)  In the last two shops I've started
using internal subroutines.  And I got quite a battle.  Those who
have never programmed outside COBOL on one side, those who know
another language (Basic, C, Fortran, PL/I) on the other.

We examined the IBM VS COBOL compiler and the COBOL/390 (aka MVS
COBOL) compilers.  Looking at the generated code, you could not
see a calling sequence for an internal routine that was any worse
than a PERFORM.  In many cases, the compiler decided to "inline"
the subroutine to there was zero performance penalty.
```

##### ↳ ↳ Re: Multiple programs in one source

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n0god$aja@dfw-ixnews9.ix.netcom.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <7n027o$dic$1@news1.xs4all.nl>`

```

Carlo Hogeveen <hyphen@xs4all.nl> wrote in message
news:7n027o$dic$1@news1.xs4all.nl...
>
> It is called structured programming!
>

What did I miss?
   When did "structured programming" have ANYTHING to do with "local"
variables.

I understand the theory of "procedure independence" and whatever, but I have
never (before) heard it even VAGUELY tied into the concept of "structured"
programming.
```

#### ↳ Re: Multiple programs in one source

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n0bt8$rh8$3@news.igs.net>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com>`

```
The main reason that I have seen it used is for multi-threaded code,
particularly where the threads are event driven.  If you have, for example,
three windows all working together, it makes a lot of sense to write it as
three individual programs within one startup program.

Howard Brazee wrote in message <37932F22.A4751958@NOSPAMhome.com>...
>I'm a mainframe programmer who has never worked in a location which has
>more than one COBOL program in one source member.
…[12 more quoted lines elided]…
>What am I overlooking?  What are the shops I have worked in overlooked?
```

##### ↳ ↳ Re: Multiple programs in one source

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37947BBB.43F26A90@NOSPAMhome.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <7n0bt8$rh8$3@news.igs.net>`

```
donald tees wrote:
> 
> The main reason that I have seen it used is for multi-threaded code,
> particularly where the threads are event driven.  If you have, for example,
> three windows all working together, it makes a lot of sense to write it as
> three individual programs within one startup program.

That is something I have never looked for in a mainframe environment.  I
have had PC Java multi-threaded, and even REXX on OS/2, but never made
multi-threaded programs on a mainframe.  (and since my only experience
with PC Cobol was over a decade ago, I haven't done any multi-threaded
COBOL there either).
```

##### ↳ ↳ Re: Multiple programs in one source

- **From:** kthompsn <thompsonk@st-louis-exch01.army.mil>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n2jqe$6dd$1@nnrp1.deja.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <7n0bt8$rh8$3@news.igs.net>`

```
Thx! First reason/explanation i've seen that actually makes sense.

In article <7n0bt8$rh8$3@news.igs.net>,
  "donald tees" <donald@willmack.com> wrote:
> The main reason that I have seen it used is for multi-threaded code,
> particularly where the threads are event driven.  If you have, for
example,
> three windows all working together, it makes a lot of sense to write
it as
> three individual programs within one startup program.
>
> Howard Brazee wrote in message <37932F22.A4751958@NOSPAMhome.com>...
> >I'm a mainframe programmer who has never worked in a location which
has
> >more than one COBOL program in one source member.
> >
…[6 more quoted lines elided]…
> >The one place I can see a use for this is if only one program does
the
> >call, and a perform won't work because the called program and calling
> >program use different subschemata.  (having fun with that word -
> >schemata is a dictionary plural for schema!!)
> >
> >What am I overlooking?  What are the shops I have worked in
overlooked?
>
>


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: Multiple programs in one source

- **From:** "Ed Milne" <emilne@ford.com>
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n1vpv$o3p1@eccws1.dearborn.ford.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com>`

```
The easiest justification for using an internal program is when you have to
do the same process on multiple fields.  Instead of moving data back and
forth between common fields for processing, you can use multiple CALL
statements USING the different fields.

Ed Milne

Howard Brazee wrote in message <37932F22.A4751958@NOSPAMhome.com>...
>I'm a mainframe programmer who has never worked in a location which has
>more than one COBOL program in one source member.
…[12 more quoted lines elided]…
>What am I overlooking?  What are the shops I have worked in overlooked?
```

##### ↳ ↳ Re: Multiple programs in one source

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37962417.61685ECF@NOSPAMhome.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <7n1vpv$o3p1@eccws1.dearborn.ford.com>`

```
Ed Milne wrote:
> 
> The easiest justification for using an internal program is when you have to
…[4 more quoted lines elided]…
> Ed Milne

I don't see the selling point in changing a move to a call.  I increase
overhead, but what do I gain?  (besides a chance to play with internal
programs)
```

###### ↳ ↳ ↳ Re: Multiple programs in one source

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-07-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37972DAE.578BC6EF@zip.com.au>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com> <7n1vpv$o3p1@eccws1.dearborn.ford.com> <37962417.61685ECF@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> Ed Milne wrote:
…[10 more quoted lines elided]…
> internal programs)

current example:

Move screen-effective-date  to ws-validate-date
perform p100-validate-date
move ws-validate-return     to screen-effective-date

module example:

call 'validdt'  using screen-effective-date
                      screen-effective-date

cost nil: 'call' to 'perform' and it removes the move statements.
-  negative run time.
-  Once you are used to doing this it is actually clearer (less code)

Jarred's note implies that the cobol compiler may eliminate the
perform entirely making the call actually faster (if the source of
'validdt' is inside the same program.

Ken
```

#### ↳ Re: Multiple programs in one source

- **From:** Patrick <pwm@bellatlantic.net>
- **Date:** 1999-07-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<932827205.25922@www.remarq.com>`
- **References:** `<37932F22.A4751958@NOSPAMhome.com>`

```
Programs can be "nested" since 1985. A nested program could
be a copybook. The advantage of a separate program over a
section or paragraph that is performed is "abstraction." A
separate program is not limited to processing only the data
defined within the program, it is capable of processing any
data passed to it by the calling program, whatever program
that might be.



* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
