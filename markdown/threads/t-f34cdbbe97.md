[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Panvalet

_8 messages · 3 participants · 1998-09_

---

### Panvalet

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-rJJwtDTd4vZW@Dwight_Miller.iix.com>`

```

Yeah, I've heard it before - but seriously - NO MANUALS to be found.  
I'm working on a remote site that use Panvalet, and I need to export 
an ENTIRE Panvalet library to a PDS - anyone know the util? Pan#1? or 
the control statements?

Thanks.
```

#### ↳ Re: Panvalet

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zOeJ1.329$Lk3.2665348@storm.twcol.com>`
- **References:** `<Jl0PnHJ5PvPd-pn2-rJJwtDTd4vZW@Dwight_Miller.iix.com>`

```
Here is one:

<<JOBCARD HERE>>

//STEP01 EXEC  PGM=PAN#1
//PANDD1   DD  DSN=<<source panvalet library>>,DISP=SHR
//PANDD2   DD  SYSOUT=*
//SYSPRINT DD  SYSOUT=*
//SYSPUNCH DD  SYSOUT=*
//* WRITE TO WORK WITH NO OTHER CONTROL STATEMENTS EXPANDS INCLUDES
//* WRITES TO DDNAME PANDD2
//SYSIN    DD  *
++WRITE WORK,<<panvalet member name>>
//

where <<JOBCARD HERE>> is your jobcard.
where <<source panvalet library>> is the panvalet library you need to copy
from
where <<panvalet member name>> is the panvalet member name you need to copy
Set PANDD2 to the fully qualified PDS and member name you wish to write to.
I may have others, I will post them when I find them. If you know REXX I can
give you some nice examples which can be run from batch or foreground.


Thane Hubbell wrote in message ...
>
>Yeah, I've heard it before - but seriously - NO MANUALS to be found.
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Panvalet

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-Xg8GZxwWEUyd@Dwight_Miller.iix.com>`
- **References:** `<Jl0PnHJ5PvPd-pn2-rJJwtDTd4vZW@Dwight_Miller.iix.com> <zOeJ1.329$Lk3.2665348@storm.twcol.com>`

```
On Tue, 8 Sep 1998 18:34:12, "Jeff" <a@a.com> wrote:

> where <<JOBCARD HERE>> is your jobcard.
> where <<source panvalet library>> is the panvalet library you need to copy
…[4 more quoted lines elided]…
> give you some nice examples which can be run from batch or foreground.

Thanks Jeff - I actually have this one working, but will it accept 
wild cards?  I want to do the ENTIRE panlib in one fell swoop, not 
member by member.

Have something like that?
```

###### ↳ ↳ ↳ Re: Panvalet

- **From:** tmj <spam@spam.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F858ED.63E9@spam.com>`
- **References:** `<Jl0PnHJ5PvPd-pn2-rJJwtDTd4vZW@Dwight_Miller.iix.com> <zOeJ1.329$Lk3.2665348@storm.twcol.com> <Jl0PnHJ5PvPd-pn2-Xg8GZxwWEUyd@Dwight_Miller.iix.com>`

```
If you have version 14.3 of PANVALET you can use wildcards (*) as
follows:

//PAN    EXEC  PGM=PAN#1                              
//STEPLIB  DD  DSN=yadayada.PANVALET.LINKLIB,DISP=SHR 
//PANDD1   DD  DSN=yadayada.PANVALET.TESTLIB,DISP=SHR 
//PANDD4   DD  DSN=yadayada.PANVALET.PRODLIB,DISP=SHR  
//PANDD2   DD DUMMY,DCB=BLKSIZE=3600                  
//SYSPRINT DD SYSOUT=*                                
//SYSPUNCH DD DSN=yadayada.THANE.COBOL,  
//           etc
//SYSIN    DD *                                                          
++WRITE PUNCH,PREFIX=THANE*                                            N 
//*                                     PUT "N" HERE------------------>* 

The "N" says don't expand ++INCLUDE, put an "E" there if you want them.

It put all the THANE programs into the one file.  I haven't figured out
how to put each PANVALET member into a seperate PDS member yet.  I think
that's what you wanted to do originally.


Thane Hubbell wrote:
> 
> On Tue, 8 Sep 1998 18:34:12, "Jeff" <a@a.com> wrote:
…[13 more quoted lines elided]…
> Have something like that?
```

###### ↳ ↳ ↳ Re: Panvalet

_(reply depth: 4)_

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-09-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%b%J1.32$4E6.304947@storm.twcol.com>`
- **References:** `<Jl0PnHJ5PvPd-pn2-rJJwtDTd4vZW@Dwight_Miller.iix.com> <zOeJ1.329$Lk3.2665348@storm.twcol.com> <Jl0PnHJ5PvPd-pn2-Xg8GZxwWEUyd@Dwight_Miller.iix.com> <35F858ED.63E9@spam.com>`

```
good answer. wish I'd figured that one out a few months ago when I needed
it. writing to PUNCH I believe expands the ++INCLUDE. Writing to WORK does
not expand the ++INCLUDE statements. There are several ways to do it, but it
looks like Thane figured it out.

>++WRITE PUNCH,PREFIX=THANE*                                            N


Is there a way to get a list of the members?
```

###### ↳ ↳ ↳ Re: Panvalet

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-GkOrTdMKcJpI@Dwight_Miller.iix.com>`
- **References:** `<Jl0PnHJ5PvPd-pn2-rJJwtDTd4vZW@Dwight_Miller.iix.com> <zOeJ1.329$Lk3.2665348@storm.twcol.com> <Jl0PnHJ5PvPd-pn2-Xg8GZxwWEUyd@Dwight_Miller.iix.com> <35F858ED.63E9@spam.com> <%b%J1.32$4E6.304947@storm.twcol.com>`

```
On Fri, 11 Sep 1998 01:38:13, "Jeff" <a@a.com> wrote:

> good answer. wish I'd figured that one out a few months ago when I needed
> it. writing to PUNCH I believe expands the ++INCLUDE. Writing to WORK does
…[7 more quoted lines elided]…
> 

Wasn't me who figured it out.  It's a solution, but not the one I want
yet.  If I can punch a single member to a single member of a PDS why 
can't I punch them all to individual members????  

What I want to end up with is a straight PDS copy of the panlib.
```

##### ↳ ↳ Re: Panvalet

- **From:** mixxerdw@eye_eye_echs.com
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1tGZ16mMk7i4-pn2-G6bfYNdv5Lij@dsm4merlin.iix.com>`
- **References:** `<Jl0PnHJ5PvPd-pn2-rJJwtDTd4vZW@Dwight_Miller.iix.com> <zOeJ1.329$Lk3.2665348@storm.twcol.com>`

```
On Tue, 8 Sep 1998 18:34:12, "Jeff" <a@a.com> wrote:

>  If you know REXX I can
> give you some nice examples which can be run from batch or foreground.
> 


A REXX-Panvalet interface?  Kewl!  Show us how!

(What Thane wants to do is not just a ++WRITE of a single member to a 
PDS, but to write the whole PANLIB.  I know I used to do that (e.g. 
maintained my PROCLIB in Panvalet, loading the entire PDS in one job 
after significant updates such as global DSN replacement) but I don't 
have any old JCL around to refresh my memory.)

=Dwight=
X1=L, X2=L & the domain is phonetic
```

#### ↳ Re: Panvalet

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-tFVJ6V5WSnh8@Dwight_Miller.iix.com>`
- **References:** `<Jl0PnHJ5PvPd-pn2-rJJwtDTd4vZW@Dwight_Miller.iix.com>`

```
On Tue, 8 Sep 1998 14:45:33, redsky@ibm.net (Thane Hubbell) wrote:

> 
> Yeah, I've heard it before - but seriously - NO MANUALS to be found.  
…[5 more quoted lines elided]…
> 

Someone (Tjones) was nice enough to e-mail me the answer to this 
problem, and it worked!  If anyone else needs to know how to do this, 
let me know and I'll be glad to pass on the instructions.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
