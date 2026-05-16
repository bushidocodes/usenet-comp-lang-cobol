[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM Mainframe Calling Java from Cobol via JCL Batch STDOUT Issues

_7 messages · 3 participants · 2009-05_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### IBM Mainframe Calling Java from Cobol via JCL Batch STDOUT Issues

- **From:** sjhesse@gmail.com
- **Date:** 2009-05-07T02:17:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f3a8cf29-db73-4fc3-ab4d-c0a013d37acf@l5g2000vbc.googlegroups.com>`

```
Hi all,

I have a legacy cobol main program in here. I want to call a java
program from this code, so I wrote an (Enterprise) OO cobol wrapper
for the jvm, which calls an object method. So far so good.
In the legacy cobol I'm calling the entrypoint of the oo cobol.
If I only have the oo cobol program without any call to java, I see my
"Display", which is in the oo program.
But when I add the call to the jvm to the oo cobol code, I do not get
any Displays in the sysout from that moment. But the program seems to
return correctly, because MAX RC in jcl is 4.
I'm calling that cobol tool from jcl, so I use  PGM=IKJEFT01 for the
execution.
The cobol program itself is compiled and linked via
PARM='RENT,LIST,LET,MAP,XREF,CASE(MIXED),DYNAM(DLL),RMODE(ANY)'

I also compiled my oo cobol as a mainprogram, which I run through
BPXBATCH - this program works fine, including the call to the jvm.

Has anyone any hint for me?

Thanks in advance and regards

Sascha

Here is some code:

oo cobol:
cbl dll,thread
Identification division.
Program-id. "TSTHELLO" recursive.
Environment division.
Configuration section.
Repository.
Class HelloJ is "HelloJ".
Data Division.
Procedure division.
            Display "COBOL program TSTHELLO entered".
           Invoke HelloJ "sayHello"
           Display "Returned from Java".
           Goback.
End program "TSTHELLO".

JCL:

//STEP004  EXEC PGM=IKJEFT1B,DYNAMNBR=20,COND=(4,LT)
//SYSABEND DD SYSOUT=*
//SYSOUT   DD SYSOUT=*
//SYSTSPRT DD SYSOUT=*
//SYSPRINT DD SYSOUT=*
//SYSTSIN  DD *
DSN SYSTEM(DSNP)
RUN  PROGRAM(T064JAVA) PLAN(T064JAVA)
END
//CEEOPTS  DD *
  XPLIN(ON)
  ENVAR(LIBPATH=/usr/lpp/java/J6.0/bin/classic/,
        CLASSPATH=/vwb/P10745/ootest/tsthello/)
  RPTOPTS(ON)
/*
//STDOUT   DD SYSOUT=*,DCB=(RECFM=VB)
//STDERR   DD SYSOUT=*,DCB=(RECFM=VB)
//PROTOK   DD DSN=SE.T064.PROTO(+1),
//            DISP=(NEW,CATLG,DELETE),
//            DATACLAS=DCSE0100,
//            MGMTCLAS=MCSEDFLT
//FEHLER   DD DSN=SE.T064.FEHLER(+1),
//            DISP=(NEW,CATLG,DELETE),
//            DATACLAS=DCSE0100,
//            MGMTCLAS=MCSEDFLT
//TVDCAT   DD DSN=RZVSAM.TVDCAT,DISP=SHR
//TVDP05   DD DSN=RZVSAM.TVDP05,DISP=SHR
//TVDP08   DD DSN=RZVSAM.TVDP08,DISP=SHR
//VTECHKU  DD DSN=RZVSAM.GTECHKU,DISP=SHR,AMP='BUFND=3,BUFNI=20'
//INKGDV   DD DSN=RZVSAM.INKGDV,DISP=SHR,AMP='BUFND=3,BUFNI=20'
//*   OG84IN   DD DSN=SE.T064.GDVAEND.SEQ(-1),DISP=SHR
//OG84IN   DD DSN=RZ.GDV08000.GDV.BEST(0),DISP=SHR
//*    //OG84IN   DD DSN=RZ.GDV08000.GDV.AEND(0),DISP=SHR
//DISKOU   DD DSN=SE.T064.GDVBEST.SEQ(+1),
 //*   DISKOU   DD DSN=SE.T064.VPDATL(+1),
 //            DISP=(NEW,CATLG,DELETE),
 //            DATACLAS=DCSE0100,
 //            MGMTCLAS=MCSEDFLT
 //SYSIN    DD *
 SQLPSNA xxx
 SQLPSNA xxx
 SQLPSNA xxx
 SQLPSNA xxx
 DLIPROD xxx             D
 /*
```

#### ↳ Re: IBM Mainframe Calling Java from Cobol via JCL Batch STDOUT Issues

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-05-07T22:47:50+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76fsioF1coj3kU1@mid.individual.net>`
- **References:** `<f3a8cf29-db73-4fc3-ab4d-c0a013d37acf@l5g2000vbc.googlegroups.com>`

```
sjhesse@gmail.com wrote:
> Hi all,
>
…[87 more quoted lines elided]…
> /*

I'm confused as to what is Java and what is COBOL here (I haven't used 
Enterprise OO COBOL).

Presumably "HelloJ" is a Java Class?  Or is it an OO COBOL Class that 
"wraps" Java?

And the "sayHello" method is in Java, and writes a Hello message to SYSOUT?

Have you tried calling "sayHello" from Java to make sure it works properly?

Work from the ground up. Get the Java Class working, then invoke it from 
COBOL, using whatever mechanism the system uses to communicate between Java 
and COBOL. I note your repository use but I'm not sure if you can include 
Java Classes directly in the repository or not. You mentioned "wrapping" the 
JVM. Is that necessary? It seems a bit drastic to me. I would expect that if 
you have identified the Java Class in the repository and you have the 
CLASSLIB path defined, the OO COBOL compiler would recognise the Methods and 
properties of that Java Class without having to do anything else, but I may 
be completely mistaken about this. It may be that the repository can only 
recognise OO COBOL Classes.

Can you clarify, please?

Pete.
```

##### ↳ ↳ Re: IBM Mainframe Calling Java from Cobol via JCL Batch STDOUT Issues

- **From:** sjhesse@gmail.com
- **Date:** 2009-05-07T04:18:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<06458d6e-21c3-4812-b3bb-a0292349c3d3@21g2000vbk.googlegroups.com>`
- **References:** `<f3a8cf29-db73-4fc3-ab4d-c0a013d37acf@l5g2000vbc.googlegroups.com> <76fsioF1coj3kU1@mid.individual.net>`

```
Hi Pete,

thanks for you reply

> Presumably "HelloJ" is a Java Class?  
You're right, this ist HelloJ:
public class HelloJ {
	public static void sayHello(){
		System.out.println("Hello World!");
	}
}

> Have you tried calling "sayHello" from Java to make sure it works properly?
I veryfied this class and also checked, that it is working properly
when invoked by oo cobol. The problem only occurs when

cobol   ------->  oo cobol   ----------->      java
          call                   invoke

I veryfied

cobol   ------->  oo cobol
          call

and also

oo cobol   ----------->      java
             invoke

which are working like I expected

> I note your repository use but I'm not sure if you can include
> Java Classes directly in the repository or not.
It is recommended to that this way. You have to include your java
classes in the repo.

> You mentioned "wrapping" the JVM. Is that necessary? It seems a bit drastic to me. I would expect that if
I think you're right, wrapping may the the wrong term. The oo cobol
uses a shared library to execute the code, I'm not sure if there'll be
a "real" jvm process
```

###### ↳ ↳ ↳ Re: IBM Mainframe Calling Java from Cobol via JCL Batch STDOUT Issues

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-05-08T12:25:35+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76hcg1F1d0h6pU1@mid.individual.net>`
- **References:** `<f3a8cf29-db73-4fc3-ab4d-c0a013d37acf@l5g2000vbc.googlegroups.com> <76fsioF1coj3kU1@mid.individual.net> <06458d6e-21c3-4812-b3bb-a0292349c3d3@21g2000vbk.googlegroups.com>`

```
sjhesse@gmail.com wrote:
> Hi Pete,
>
…[28 more quoted lines elided]…
> which are working like I expected

Excellent clarification. Thanks.

So the only problem really is CALLing OO COBOL from COBOL...

cobol   ------->  oo cobol   ----------->      java
           call                   invoke

What happens if you do this?

 cobol   ------->  oo cobol   ----------->      java
           INVOKE                  invoke

It may be that the mechanism used to link to a Class is different from the 
mechanism used to link to a module...

>
>> I note your repository use but I'm not sure if you can include
>> Java Classes directly in the repository or not.
> It is recommended to that this way. You have to include your java
> classes in the repo.

OK. What if you are using late binding? Repository is required for early 
binding so that references can be resolved at compile time and compliance 
and conformity can be checked. Late binding doesn't normally require it; you 
just invoke the fully qualified method of the Class you want. Maybe, in the 
Enterprise environment late binding is not an option, or it requires a 
repository entry for other reasons.
>
>> You mentioned "wrapping" the JVM. Is that necessary? It seems a bit
…[3 more quoted lines elided]…
> a "real" jvm process

Let us know how you get on. This is an interesting problem.

Pete.
```

###### ↳ ↳ ↳ Re: IBM Mainframe Calling Java from Cobol via JCL Batch STDOUT Issues

_(reply depth: 4)_

- **From:** Sascha John Hesse <sjhesse@gmail.com>
- **Date:** 2009-05-08T03:58:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2cf7cca3-1a12-4a1f-9693-b2f2356bfce6@e24g2000vbe.googlegroups.com>`
- **References:** `<f3a8cf29-db73-4fc3-ab4d-c0a013d37acf@l5g2000vbc.googlegroups.com> <76fsioF1coj3kU1@mid.individual.net> <06458d6e-21c3-4812-b3bb-a0292349c3d3@21g2000vbk.googlegroups.com> <76hcg1F1d0h6pU1@mid.individual.net>`

```
Hi Pete,
> What happens if you do this?
>
>  cobol   ------->  oo cobol   ----------->      java
>            INVOKE                  invoke
I'll do that the next week, because I've some administration to do
right now. Thanks for this hint.
What I started right today in the morning is to make the legacy cobol
an oo cobol, so I won't have the call - just the invokation...

> Maybe, in the
> Enterprise environment late binding is not an option, or it requires a
> repository entry for other reasons.
I'll check that late binding out.
>

> Let us know how you get on. This is an interesting problem.
I'll keep you informed. Today I heard, that we'll have someone from
Big Blue here the next friday, who seems to be familiar with Java/
Cobol batch things.
I also posted this to the cobol café, but there was no reply until
now.

Have a nice weekend!

Sascha
```

#### ↳ Re: IBM Mainframe Calling Java from Cobol via JCL Batch STDOUT Issues

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-07T07:19:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NlAMl.289610$UQ6.210907@en-nntp-03.dc1.easynews.com>`
- **References:** `<f3a8cf29-db73-4fc3-ab4d-c0a013d37acf@l5g2000vbc.googlegroups.com>`

```
This looks like a good question for the (relatively) new  IBM COBOL Cafe.

Check out:
  http://www-949.ibm.com/software/rational/cafe/community/cobol

P.S.  You may confuse people when you say,
  "I want to call a java  program from this code"

What I think you mean (and have coded) is,
  "I want to invoke a java method from this COBOL code"
```

#### ↳ Re: IBM Mainframe Calling Java from Cobol via JCL Batch STDOUT Issues

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-11T02:30:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_tQNl.275205$Yx2.198796@en-nntp-06.dc1.easynews.com>`
- **References:** `<f3a8cf29-db73-4fc3-ab4d-c0a013d37acf@l5g2000vbc.googlegroups.com>`

```
to comp.lang.cobol

I just posted a couple of replies in the IBM COBOL Cafe.  I am also posting them 
here (in case anyone has additional information).  Also, the advantage of CLC, 
is that if the OP wants to contact me "off-list" they can.

Here's what I put in the IBM COBOL Cafe:

   * * * * * *
I still think you will get an answer (or 2) via this forum. HOWEVER, if you have 
an "end-of-May" deadline for getting something working AND you think you are 
following what the current IBM documentation tells you to do but not getting 
expected results. then the fastest/most reliable way to get a "solution" is via 
the IBM support center.



Even if you think you are on the right track but have a deadline in a couple of 
weeks, I would certainly recommend that you (or whoever does this in your job) 
contact the IBM support center and create a "PMR".


FYI,


I am still not certain why you need the Java "subroutine". If the this is new 
logic or "separate" logic from your existing legacy COBOL program, then I would 
certainly go with (almost any other) solution, e.g. a regular COBOL subprogram. 
My best guess is that going with a mixed COBOL/Java application is going to end 
up with something that



  a.. is hard to maintain
  b.. uses LOTS more storage at run-time
  c.. probably has significant performance hits


Certainly IBM supports mixed COBOL/Java applications, but these are rare enough 
and sufficiently "out of the mainstream" that I would be hesitant to try this 
just because you have ONE Java subroutine (method) that you want to use. 
ESPECIALLY as you are trying to introduce this new technology under a time 
constraint, I really wonder if this is the best way to go.


One final note (if you are going this way), Have you looked at:


http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igy3pg40/2.3.1.4.2


and in particular, the use of COBJVMINITOPTIONS environment variable? This might 
well be usable for setting the STDOUT location (for Java).

   * * * * * * * * *


One other thing. I just noticed that your original note said (for the case where 
you have non-OO COBOL calling OO),

"I'm calling that cobol tool from jcl, so I use PGM=IKJEFT01 for the
execution."


However, that is NOT what the IBM documentation says to do if your main program 
is procedural code calling OO code. At:


http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igy3pg40/2.3.1.4.2


it explicitly says,


"If the first routine of a mixed COBOL and Java application is a COBOL program, 
run the application by specifying the program name at the command prompt. If a 
JVM is not already running in the process of the COBOL program, the COBOL run 
time automatically initializes a JVM"


that might be you entire problem for the non-OO main situation..


Have you rad:


http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igy3pg40/2.3.2.2


where it says,


"Use DD statements to specify files in the HFS for the standard input, output, 
and error streams for Java:



  a.. JAVAIN DD for the input from statements such as c=System.in.read();
  b.. JAVAOUT DD for the output from statements such as 
System.out.println(+string+);
  c.. JAVAERR DD for the output from statements such as 
System.err.println(+string+);


  a.. * * *

Your original JCL makes this look as if the original code was a DB2 program (to 
which you are adding Java). This almost certainly adds an enitre other layer of 
complexity. I found some documentation on mixing Java, COBOL, and DB2. If this 
is what you are trying to do, then make certain that this is clear to everyone 
you talk to about this. If you are NOT using DB2, then I think your entire 
original JCL needs to be reconsidered. At

http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igy3pg40/6.1


It says,


"COBOL class definitions and methods cannot contain EXEC SQL statements and 
cannot be compiled using the SQL compiler option. "


* * * *


Final note. Your original note said tha tyou used "static" calls from your main 
(non-OO COBOL) program to your OO wraper. But the JCL you showed uses 
DYNAM(DLL). This means that you are NOT using static calls.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
