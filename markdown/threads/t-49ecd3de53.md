[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [o]: JCL question

_4 messages · 3 participants · 1999-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### [o]: JCL question

- **From:** "kennet" <kennet@post11.tele.dk>
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77oa0h$5qeq$1@news-inn.inet.tele.dk>`

```
I'm trying to write a procedure in JCL but I am having problems with the
parameters. Here's a simple example:

// write     proc line=''
// step1   exec db2ucaf,pgmname=writeit,param=&line
// etc.

Here the called procedure "db2ucaf" is our standard JCL for running load
modules, and writeit is just a PL/1 program that prints the content in
param. So the procedure can simply print a line of text.

Now, if I what to write "Hello" on the screen, I can just do this:

//  exec   write,line=hello

And it works fine. However, if I need to write "Hello, world", I'm having
problem with the comma. So I tried

//  exec   write,line='hello, world'

But this doesn't work. However triple-quotes works:

//  exec   write,line='''hello, world'''

But that's not the way I wanna do it! I also tried recoding the procedure as

// write     proc line=''
// step1   exec db2ucaf,pgmname=writeit,param='&line'
// etc.

but then &line is not recognised as a symbolic parameter, and the program
simply prints the string '&line'.
Is there a way to pass parameters with spaces and commas without having to
use triple-quotes?

Regards,
Kennet
```

#### ↳ Re: [o]: JCL question

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1999-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990116142026.25453.00001673@ng133.aol.com>`
- **References:** `<77oa0h$5qeq$1@news-inn.inet.tele.dk>`

```
I have another way of looking at this, as opposed to a proposed direct
solution.

Your problem is that your style involves a PROC invoking another PROC.  It
would not be correct to say that that is a no-no, but it is discouraged. 
The biggest reason does not relate directly to your current considerations with
resolving symbolics, but relates to the difficulty of specifying restarts.  A
step which has a stepname invokes a proc, the proc has a stepname, and if it
invokes a proc you have a proc-proc stepname to contend with. Restart syntax is
not flexible, it allows only for stepname and procstepname.  (and only the
stepname within the last proc can be referenced as the procstepname).

Thus specifying parm overrides or dd statement overrides is confusing, tough
and sometimes impossible when a proc invokes a proc. This problem is usually
faced when you can least afford it, an emmergency abend system down, in the wee
hours of the morning when there are few application programmers and few system
programmers available.

But really procs within a proc are just _almost_ a no-no. Because there are
shops that do it anyway, and some amelioration can be had by making the outer
proc single-stepped (a severe limitation). For example your proc as posted has
only one step in the outer proc, which may work for you, but provides very
limitted future flexibility.

JCL was invented long before recursive functional languages became all the
craze.  JCL is obtusedly flatlanded in cousciousness.
Getting parms from the top level of a job stream into a proc is straight
forward, passing them deeper is infact not what the language was intended for.
Yes folks do it to many layers deep, it's just that that is the wrong path with
this tool.

Some thoughts relating to simplifying this (that is flattening it).  

One approach is to proliferate the bottom level proc into each of its versions
(as opposed to dynamically generating it at proc execution time). Your initial
approach is more artistic, but in situations in which there are not realy too
many different basic low level procs, proliferating them as mostly hard coded
procs is a solution to the limitations of JCL.

If you have the right JES you can SET symbolics that could be used in a PROC
name in the high level job JCL to pick the correct proc for execution.

For example if you had a DB2UW PROC that executed your WRITEIT program, you
could code this:

// SET SPECXYZ=W 
//WRITE1 EXEC DB2U&SPECXYZ

this will execute proc DB2UW and that proc would have 

//WHATEVER EXEC WRITEIT

This should ease the specification of the text parameters.


Another way to look at this is that as you veer away from simplistic parm
values (only the complex ones engage the quoting issue), you are nolonger
dealing with parms but instead data.

In the situation you describe, many shops will not try to get the text in via
parms. Utilities like WRTIEIT are coded to access data files for headers, tags
or elaborate control parms. A prestep is needed to jam the text onto this
requisite file. This is controversial because everyone just wants a simple way
to do things and two steps is not desirable when one step ought to be enough.
But JCL does have limitations which bring these alternatives into view. 

There is a basic fact in your post. You know the text value up at the jobstream
level, and are having trouble getting it all the way down to the specific EXEC
that invokes the presenter WRITEIT.  What some shops will do is have you put
that text on a data card in the _job_ JCL lib, which is just JCL and can
therefore tollerate DD * input and /* input termination. (procs do not allow
that of course, but JCL does).

Atleast as far as your example is concerned, these text items are job specific,
not PROC specific. This distinction can be used powerfully. Job streams can
have SYSIN DD *, even if submitted from a PDS with a name like *.PROC or
*.PROCLIB.  It is the manner of invocation that makes the difference. A
corollary is that a proc invoked with EXEC PROCNAME or EXECUTE PROC=PROCNAME
cannot have DD* input even if brought in, via JCLLIB control from
GIZMO.NOTPROC.YOURNODE.
It is the manner of invocation that determines it.

Yet another possibility, is to fold all this back together, and, keeping your
PROCs one layer deep, simply insert a //utilddnm DD * to the correct step for
WRITEIT or whichever, and bring the text directly into the program.

Alternatively, if your text is not job specific, but application specific, then
place the text into parm file PDSes, and bring it in explicitly with a DD in
the proc just like the DD * approach. Obviously you could resolve the member
name, and all or parts of the PDS DSN with symbolics.

In short, another way to look at this is that the complex text has provided you
with a symptom of a problem.  Either you are trying to go too deep in your proc
layers, as JCL infact was not designed for this (it was designed for a flat
world, and has been extended strangely). Or your text interface, via parms, was
conceived for simple matter, and you are finding you want more; which will flow
better through data files or PDSes, than through parms.

Hope this helps even though it is not directly responsive.




"kennet" <kennet@post11.tele.dk>
On Fri, 15 Jan 1999 21:53:48 +0100
posted

<<
I'm trying to write a procedure in JCL but I am having problems with the
parameters. Here's a simple example:

// write     proc line=''
// step1   exec db2ucaf,pgmname=writeit,param=&line
// etc.

Here the called procedure "db2ucaf" is our standard JCL for running load
modules, and writeit is just a PL/1 program that prints the content in
param. So the procedure can simply print a line of text.

Now, if I what to write "Hello" on the screen, I can just do this:

//  exec   write,line=hello

And it works fine. However, if I need to write "Hello, world", I'm having
problem with the comma. So I tried

//  exec   write,line='hello, world'

But this doesn't work. However triple-quotes works:

//  exec   write,line='''hello, world'''

But that's not the way I wanna do it! I also tried recoding the procedure as

// write     proc line=''
// step1   exec db2ucaf,pgmname=writeit,param='&line'
// etc.

but then &line is not recognised as a symbolic parameter, and the program
simply prints the string '&line'.
Is there a way to pass parameters with spaces and commas without having to
use triple-quotes?

>>


Best Wishes,


Robert Rayhawk
RKRayhawk@aol.com
```

##### ↳ ↳ Re: [o]: JCL question

- **From:** "kennet" <kennet@post11.tele.dk>
- **Date:** 1999-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77qr4i$3o14$1@news-inn.inet.tele.dk>`
- **References:** `<77oa0h$5qeq$1@news-inn.inet.tele.dk> <19990116142026.25453.00001673@ng133.aol.com>`

```

RKRayhawk skrev i meddelelsen
<19990116142026.25453.00001673@ng133.aol.com>...
>[...a lot of good stuf...]
>Hope this helps even though it is not directly responsive.
>


Thank you very much for your answer. Indeed, it does help to
understand some of the background for JCL.
I've been a PC programmer so far, and have little knowledge
of the mainframe world, esp. the limitations. It does seem,
that I'm trying to do something with JCL that it is not really intended
for. I'll consider using another approach.

Thank you.
Kennet
```

#### ↳ Re: JCL question

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8oUo2.5793$hE2.23593709@storm.twcol.com>`
- **References:** `<77oa0h$5qeq$1@news-inn.inet.tele.dk>`

```
>Here the called procedure "db2ucaf" is our standard JCL for running load
>modules, and writeit is just a PL/1 program that prints the content in
>param. So the procedure can simply print a line of text.

Sounds more like a PROC used to execute DB2 programs. I don't usually use
these unless there is actually DB2 in the program you are trying to execute.
If there is no DB2, CICS, or IMS in the program you can run it by:

//STEP001  EXEC PGM=WRITEIT
//STEPLIB  DD DSN=TSO.PROD.LOADLIB,DISP=SHR
//*above dd contains load module WRITEIT
//SYSIN    DD *
Hello, world
/*
//SYSOUT   DD SYSOUT=*
//*sometimes you need the following in case of an abend
//SYSUDUMP DD SYSOUT=*
//SYSABEND DD SYSOUT=*

or

//STEP001  EXEC PGM=WRITEIT
//STEPLIB  DD DSN=TSO.PROD.LOADLIB,DISP=SHR
//*above dd contains load module WRITEIT
//*the following dsn contains your string "Hello, world"
//SYSIN    DD DSN=TSO.PROD.PARMLIB(LINE),DISP=SHR
//SYSOUT   DD SYSOUT=*
//*sometimes you need the following in case of an abend
//SYSUDUMP DD SYSOUT=*
//SYSABEND DD SYSOUT=*



>
>Now, if I what to write "Hello" on the screen, I can just do this:
…[4 more quoted lines elided]…
>problem with the comma. So I tried

The problem would be the comma tells jcl you are passing another parameter.
Thus if in your program you were expecting 2 vars X and Y then your parm
below would pass X='hello' Y='world'.

>
>//  exec   write,line='hello, world'
…[3 more quoted lines elided]…
>//  exec   write,line='''hello, world'''

The triple quotes tells JCL you physically want to pass a "'" as part of the
parameter and use the first "'" as a delimeter.


>// write     proc line=''
>// step1   exec db2ucaf,pgmname=writeit,param='&line'
…[5 more quoted lines elided]…
>use triple-quotes?

If you have to do this within a proc try using a file containing the string
you wish to pass down, typically stored in a PARM lib or a CONTROL lib:
// write     proc line=''
// step1   exec db2ucaf,pgmname=writeit,param='&line'
// sysin   dd dsn=tso.prod.parmlib(line),disp=shr

where the dsn tso.prod.parmlib(line) would contain any characters you need
to pass to your COBOL progrm. Then inside the program you can ACCEPT each
line in the SYSIN DD, in this case:
tso.prod.parmlib(line)
which would contain something like:
"JCL DOES NOT LIKE A ' CONTAINED ON A LINE OR A , CONFUSES IT."


If you assign the parm card to something else besides SYSIN you can OPEN it
and READ it like any other file.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
