[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# pattern for an error

_25 messages · 10 participants · 2008-05 → 2008-06_

---

### pattern for an error

- **From:** mario <mmc_vw1200@hotmail.com>
- **Date:** 2008-05-28T02:31:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com>`

```
hi everyone,
i have to redesign a peace of code with a lot of GOTOs
looks like that

start.
   perform something
   perform something_else
   perform anything
   perform anything_else
   ...
   .

something.
   do_something
   if (x>10)
       error occurs
       go to error
    end-if
    do_something_else
       if (y=z)
       error occurs
       go to error
    end-if
    .

error.
   write error msg
     .
 ende.
   exit program.


so as u maybe see in any paragraph there are exit conditions when the
program should stop and write error massage
my problem now: is there any style guide or pattern to make that in a
clean way WITHOUT goto because i have to transfair it into an acu code
without goto.
the only way i´m thinking is to give a intern retern key after any
paragraph  but code would look very confusing right??

kind regards
```

#### ↳ Re: pattern for an error

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-28T06:35:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1jgq34l2bgsm7jagjb40ehjnvq9uvo12uf@4ax.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com>`

```
On Wed, 28 May 2008 02:31:57 -0700 (PDT), mario <mmc_vw1200@hotmail.com> wrote:

>hi everyone,
>i have to redesign a peace of code with a lot of GOTOs
…[36 more quoted lines elided]…
>paragraph  but code would look very confusing right??

Change 'go to error' into 'perform error' (where error includes exit program), or write an
inline 'exit program returning 1234'. Every program should pass back a return code: 0 for
success, non-zero for error. You can do it by moving the value to 'return-code' or with
the returning clause.
```

##### ↳ ↳ Re: pattern for an error

- **From:** mario <mmc_vw1200@hotmail.com>
- **Date:** 2008-05-28T04:41:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<af17cd6e-a738-4718-80f6-c1c4376446a6@59g2000hsb.googlegroups.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <1jgq34l2bgsm7jagjb40ehjnvq9uvo12uf@4ax.com>`

```
i already tried but "exit program"  does no exit

for example

gogogo.
   display "hi"
   perform error_occurs
   display "hi after error"

     .

error_occurs
    exit program
     .


i come back to the second display "hi after error" so the "EXIT
PROGRAM" does not realy that what it sould right???
```

###### ↳ ↳ ↳ Re: pattern for an error

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-05-28T12:52:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mAc%j.864436$us.423112@fe04.news.easynews.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <1jgq34l2bgsm7jagjb40ehjnvq9uvo12uf@4ax.com> <af17cd6e-a738-4718-80f6-c1c4376446a6@59g2000hsb.googlegroups.com>`

```
You should only return from the PERFORM of a routine with an EXIT PROGRAM, if 
the executing program is a MAIN program.  If you don't leave from a sub-program, 
then there is a bug - or something else you aren't telling us.

Depending on the compiler, you might want to replace EXIT PROGRAM with GOBACK. 
When available (it was an extension to the '85 Standard - but a common one that 
is now Standard), you will "go up a level" from a subprogram and will "stop run" 
from a main program.

If you STILL get to the DISPLAY, then there must be something going on that you 
haven't told us about.
```

#### ↳ Re: pattern for an error

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-05-28T07:50:41-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com>`

```
On Wed, 28 May 2008 02:31:57 -0700 (PDT), mario
<mmc_vw1200@hotmail.com> wrote:

>so as u maybe see in any paragraph there are exit conditions when the
>program should stop and write error massage
…[4 more quoted lines elided]…
>paragraph  but code would look very confusing right??

In my case, I don't have the option of EXIT PERFORM, so if I wanted to
convert an old CoBOL program to eliminate GO TOs, I would have to
write code.

What compiler do you use, do you have the option of EXIT PERFORM?
```

##### ↳ ↳ Re: pattern for an error

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-05-28T09:06:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com>`

```
"Howard Brazee" <howard@brazee.net> wrote in message 
news:rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com...
> On Wed, 28 May 2008 02:31:57 -0700 (PDT), mario
> <mmc_vw1200@hotmail.com> wrote:
…[3 more quoted lines elided]…
> write code.

PERFORM UNTIL  some-condition
   .....
[END-PERFORM]

??
```

###### ↳ ↳ ↳ Re: pattern for an error

- **From:** mario <mmc_vw1200@hotmail.com>
- **Date:** 2008-05-28T07:53:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5459f81a-6d4d-4c9d-b0e9-582334d0a4c9@k37g2000hsf.googlegroups.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com>`

```
TKS for ur quick and helpful answers, i think i have to reexplain my
problem

forexample my big program is perform-ing a lot of deeper layer
paragraphs, now my problem is that in one of those an error occurs,
for example the Number was not found in Database or some user imput
error ...

the case now is that at this point there is a GoTo end = finish
program
what i need is now a design pattern to handle those errors so that the
first layer paragraph knows that deep down something has gone wrong
and stops executing
for example

start.
  perform prog_layer2.

   do some other things
    ...
   .

 prog_layer2
   perform prog_layer3
   keep doing other stuff
   .

prog_layer3
   perform prog_layer4
   now here an error occurs!!!!
   .


my program looks now like that:

start.
  perform prog_layer2.

   do some other things
    ...
   .

 prog_layer2
   perform prog_layer3
   keep doing other stuff
   .

prog_layer3
   perform prog_layer4
   now here an error occurs!!!!  ->  GOTO END
   .


END
  exit program
   .  (finished)





my solution i am now working at is looking like that:

start.
  perform prog_layer2.
  if error = 1
    exit program
    and dont do the other things


   do some other things
    ...

   goto end
   .

 prog_layer2
   perform prog_layer3
   if error = 1
      exit program
      and DONT do the other stuff below

   keep doing other stuff
   .

prog_layer3
   perform prog_layer4
   now here an error occurs!!!!  ->
   move 1 to error
   exit program

END
  exit program
   .  (finished)



so far i think its not that clean that solution and if those lower
layers get called often the hole thing gets VERY unclear and is full
with "if error..."
so is there any design pattern that u know for example like in java
exception handling so that i can handle my errors in a clear program
flow??

i hope now my problem is more transparent to you
and thank u all for helping me!!!

mario
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-05-28T15:03:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wve%j.317444$3k2.34030@fe10.news.easynews.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <5459f81a-6d4d-4c9d-b0e9-582334d0a4c9@k37g2000hsf.googlegroups.com>`

```
If you ALWAYS want to stop the entire process once the error condition occurs 
but don't want to use an EXPLICIT "GO TO".  Then perform your "error routine" 
where you discover the problem and at the end of the error routine use STOP RUN 
and not EXIT PROGRAM.

Stay with EXIT PROGRAM (or better use GOBACK - if you can) if you want to return 
to a CALLing program (but NOT to a PERFORMing section of the same program).

If you want to return to part of the same program, then you should PERFORM the 
error routine and "set some flag" or other indicator that you have been in the 
error routine.

I was still not clear from your explanation below exactly which of the above (or 
some other logic) you want to do.  If none of the above is what you are trying 
to accomplish, please explain further.

It needs to be clear whether your "layers" are sections of the same program or 
separate programs.
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 4)_

- **From:** amir <ahsharif@gmail.com>
- **Date:** 2008-05-31T22:33:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fdea64f9-34e3-4284-a591-f8108df54ea4@f36g2000hsa.googlegroups.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <5459f81a-6d4d-4c9d-b0e9-582334d0a4c9@k37g2000hsf.googlegroups.com>`

```
On May 28, 5:53 pm, mario <mmc_vw1...@hotmail.com> wrote:
> TKS for ur quick and helpful answers, i think i have to reexplain my
> problem
…[96 more quoted lines elided]…
> mario

If you draw your program structure and architecture, you can see your
problem better.
I suggest you to:
1- separate layers in sections
2- in each section you can redesign the layer structure.
3- exception handling is nothing but a GO TO, you can not escape it.
just organize it as:
+ use declaratives for file exception handling.
+ use file status check and ON Overflow, AT End and ... for known
exceptions.
+ cluster your other exceptions(exit conditions) in each layer and
make different paragraphs to handle it(something like: exit-normal,
except-math, except-...)
+ also create a Data-Group for return status between layers, like:
01 Exception-Result
  05 Code	pic 9999.
  05 Message	pic X(50).
Initialize it at any function (paragraph) startup and check it after
call to handle exceptions between layers.

I used the mechanism like this to implement an exception handling in
my code.
I hope be useful and will appreciated for any idea.
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-01T05:52:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m1t444hpct7vgnepgjurfu7glf6phtqbo5@4ax.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <5459f81a-6d4d-4c9d-b0e9-582334d0a4c9@k37g2000hsf.googlegroups.com> <fdea64f9-34e3-4284-a591-f8108df54ea4@f36g2000hsa.googlegroups.com>`

```
On Sat, 31 May 2008 22:33:05 -0700 (PDT), amir <ahsharif@gmail.com> wrote:


>+ also create a Data-Group for return status between layers, like:
>01 Exception-Result
>  05 Code	pic 9999.
>  05 Message	pic X(50).

Use the Standard mechanism rather than inventing your own. Cobol calls it "return-code".

One of the nice things about return-code is that it cascades. For example, A calls B, B
calls C, C encounters an error,  moves a non-zero to return-code and exits. B sees that
return-code is non-zero and simply exits. A gets the return-code set by C. When A exits,
the operating system/command shell gets the return-code set by C.  If C is written in
another language, the return mechanism works the same way. 

Embedded SQL does not follow the convention. You must 'move sqlcode to return-code.'

>Initialize it at any function (paragraph) startup and check it after
>call to handle exceptions between layers.

PERFORM does not pass parameters nor a return code; paragraphs cannot have private
variables (working-storage). It is Better to  use CALL rather than PERFORM and nested
programs rather than paragraphs.
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 6)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-06-01T18:19:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e927c0ca-9c5d-41ae-a922-707ee238d238@a32g2000prf.googlegroups.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <5459f81a-6d4d-4c9d-b0e9-582334d0a4c9@k37g2000hsf.googlegroups.com> <fdea64f9-34e3-4284-a591-f8108df54ea4@f36g2000hsa.googlegroups.com> <m1t444hpct7vgnepgjurfu7glf6phtqbo5@4ax.com>`

```
On Jun 1, 10:52 pm, Robert <n...@e.mail> wrote:
> On Sat, 31 May 2008 22:33:05 -0700 (PDT), amir <ahsha...@gmail.com> wrote:
> >+ also create a Data-Group for return status between layers, like:
…[4 more quoted lines elided]…
> Use the Standard mechanism rather than inventing your own. Cobol calls it "return-code".

It is _NOT_ a standard in Cobol-85.  CALL ... RETURNING and EXIT
PROGRAM RETURNING are MF extensions in '85.

RETURN-CODE is an extension in Fujitsu Cobol, as is PROCEDURE
DIVISION .... RETURNING ...

If you have an '02 compiler then you should look up what that does.

> One of the nice things about return-code is that it cascades. For example, A calls B, B
> calls C, C encounters an error,  moves a non-zero to return-code and exits. B sees that
…[11 more quoted lines elided]…
> programs rather than paragraphs.
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-01T21:08:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6bk644579pkvi4h5fq5lfdc862g22m0ilf@4ax.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <5459f81a-6d4d-4c9d-b0e9-582334d0a4c9@k37g2000hsf.googlegroups.com> <fdea64f9-34e3-4284-a591-f8108df54ea4@f36g2000hsa.googlegroups.com> <m1t444hpct7vgnepgjurfu7glf6phtqbo5@4ax.com> <e927c0ca-9c5d-41ae-a922-707ee238d238@a32g2000prf.googlegroups.com>`

```
On Sun, 1 Jun 2008 18:19:41 -0700 (PDT), Richard <riplin@azonic.co.nz> wrote:

>On Jun 1, 10:52ï¿½pm, Robert <n...@e.mail> wrote:
>> On Sat, 31 May 2008 22:33:05 -0700 (PDT), amir <ahsha...@gmail.com> wrote:
…[11 more quoted lines elided]…
>DIVISION .... RETURNING ...

RETURN-CODE began as an IBM extension to Cobol 74 in the days of OS/VS. It has been
supported by Micro Focus, Fujitsu and Realia for at least 20 years. It is a de facto
standard.

The traditional syntax is MOVE nnn TO RETURN-CODE followed by GOBACK, EXIT PROGRAM or STOP
RUN. 

RETURNING used on EXIT PROGRAM, CALL and PROCEDURE DIVISION are relatively recent
additions.
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-06-02T03:13:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pzJ0k.352199$3k2.30220@fe10.news.easynews.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <5459f81a-6d4d-4c9d-b0e9-582334d0a4c9@k37g2000hsf.googlegroups.com> <fdea64f9-34e3-4284-a591-f8108df54ea4@f36g2000hsa.googlegroups.com> <m1t444hpct7vgnepgjurfu7glf6phtqbo5@4ax.com> <e927c0ca-9c5d-41ae-a922-707ee238d238@a32g2000prf.googlegroups.com> <6bk644579pkvi4h5fq5lfdc862g22m0ilf@4ax.com>`

```
Interestingly enough ....

Once MIGHT say that "Return-Code" is a COBOL Standard - if you mean the X/Open 
rather than an ANSI or ISO Standard.

I also think it WELL pre-dates OS/VS COBOL for IBM mainframe compilers.  I can 
almost guarantee that it was in "ANS COBOL V2" which was a '68 ONLY compiler 
(not '74 stuff).  I also believe that it was in all the DOS/VS COBOL although 
that included a COMREG which was never in OS/VS COBOL so I am not certain.

Personally, I think that the RETURNING (in one form or another) is much more 
common in NEW programs, but the "return-code" fits in with the z/OS operating 
system, so its use there is still meaningful in a "special way".
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 8)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-06-01T21:48:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1c0a771f-032f-4ac0-8687-addf46b6510e@b5g2000pri.googlegroups.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <5459f81a-6d4d-4c9d-b0e9-582334d0a4c9@k37g2000hsf.googlegroups.com> <fdea64f9-34e3-4284-a591-f8108df54ea4@f36g2000hsa.googlegroups.com> <m1t444hpct7vgnepgjurfu7glf6phtqbo5@4ax.com> <e927c0ca-9c5d-41ae-a922-707ee238d238@a32g2000prf.googlegroups.com> <6bk644579pkvi4h5fq5lfdc862g22m0ilf@4ax.com>`

```
On Jun 2, 2:08 pm, Robert <n...@e.mail> wrote:
> On Sun, 1 Jun 2008 18:19:41 -0700 (PDT), Richard <rip...@azonic.co.nz> wrote:
> >On Jun 1, 10:52 pm, Robert <n...@e.mail> wrote:
…[22 more quoted lines elided]…
> additions.

Interestingly, RETURN-CODE is a GLOBAL special register item and yet
you advocate it in spite of your claim that global is Bad.

'relatively recent' is, like, a quarter century.

As these are implemented differently in different compilers they don't
count as 'standard'.
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 6)_

- **From:** amir <ahsharif@gmail.com>
- **Date:** 2008-06-01T23:54:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13bfeef4-c511-4041-bc25-8439b07f8231@i76g2000hsf.googlegroups.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <5459f81a-6d4d-4c9d-b0e9-582334d0a4c9@k37g2000hsf.googlegroups.com> <fdea64f9-34e3-4284-a591-f8108df54ea4@f36g2000hsa.googlegroups.com> <m1t444hpct7vgnepgjurfu7glf6phtqbo5@4ax.com>`

```
On Jun 1, 1:52 pm, Robert <n...@e.mail> wrote:
> On Sat, 31 May 2008 22:33:05 -0700 (PDT), amir <ahsha...@gmail.com> wrote:
> >+ also create a Data-Group for return status between layers, like:
…[10 more quoted lines elided]…
> another language, the return mechanism works the same way.

Classification and more information passing requirement, cause to use
this structure. Also, using RETURN CODE is very good for general
result checking.
e.g.
code = 0025 ->File open error
message = 'Account File Problem'

> Embedded SQL does not follow the convention. You must 'move sqlcode to return-code.'
Also, mechanism I told can help to unify all exception and error
handling mechanisms.

> >Initialize it at any function (paragraph) startup and check it after
> >call to handle exceptions between layers.
…[3 more quoted lines elided]…
> programs rather than paragraphs.

It's my suggestion, if he do not want to change his file structure.
I agree with you.
Specially, if he could redesign the code, many exit points will
changed to loop conditions and he can make it more readable and
understandable.
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-06-02T07:26:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l6t74496o55oktoneiu2noqbbduq9onusc@4ax.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <5459f81a-6d4d-4c9d-b0e9-582334d0a4c9@k37g2000hsf.googlegroups.com> <fdea64f9-34e3-4284-a591-f8108df54ea4@f36g2000hsa.googlegroups.com> <m1t444hpct7vgnepgjurfu7glf6phtqbo5@4ax.com>`

```
On Sun, 01 Jun 2008 05:52:36 -0500, Robert <no@e.mail> wrote:

>Use the Standard mechanism rather than inventing your own. Cobol calls it "return-code".
>
…[4 more quoted lines elided]…
>another language, the return mechanism works the same way. 

Which CoBOL compilers have cascading return codes, which have
non-cascading return codes, and which have neither?
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 7)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-06-02T09:12:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RcT0k.6282$Ri.5672@flpi146.ffdc.sbc.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <5459f81a-6d4d-4c9d-b0e9-582334d0a4c9@k37g2000hsf.googlegroups.com> <fdea64f9-34e3-4284-a591-f8108df54ea4@f36g2000hsa.googlegroups.com> <m1t444hpct7vgnepgjurfu7glf6phtqbo5@4ax.com> <l6t74496o55oktoneiu2noqbbduq9onusc@4ax.com>`

```
"Howard Brazee" <howard@brazee.net> wrote in message 
news:l6t74496o55oktoneiu2noqbbduq9onusc@4ax.com...
> On Sun, 01 Jun 2008 05:52:36 -0500, Robert <no@e.mail> wrote:
>
…[14 more quoted lines elided]…
> non-cascading return codes, and which have neither?

Call me an old fuddy-duddy if you will... but it seems to me if  any one 
compiler does 'cascade' RCs and any one other compiler does not, "good 
practice" would be to never rely on it happening for you and that one should 
ALWAYS invest the  typing time required to write "MOVE x TO RETURN-CODE" (or 
equivalent for your compiler).

MCM
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-06-02T11:01:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iImdnbS1gevOltnVnZ2dnUVZ_vninZ2d@posted.mid-floridainternet>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <5459f81a-6d4d-4c9d-b0e9-582334d0a4c9@k37g2000hsf.googlegroups.com> <fdea64f9-34e3-4284-a591-f8108df54ea4@f36g2000hsa.googlegroups.com> <m1t444hpct7vgnepgjurfu7glf6phtqbo5@4ax.com> <l6t74496o55oktoneiu2noqbbduq9onusc@4ax.com> <RcT0k.6282$Ri.5672@flpi146.ffdc.sbc.com>`

```

"Michael Mattias" <mmattias@talsystems.com> wrote in message
news:RcT0k.6282$Ri.5672@flpi146.ffdc.sbc.com...
> "Howard Brazee" <howard@brazee.net> wrote in message
> news:l6t74496o55oktoneiu2noqbbduq9onusc@4ax.com...
> > On Sun, 01 Jun 2008 05:52:36 -0500, Robert <no@e.mail> wrote:
> >
> >>Use the Standard mechanism rather than inventing your own. Cobol calls
it
> >>"return-code".
> >>
> >>One of the nice things about return-code is that it cascades. For
example,
> >>A calls B, B
> >>calls C, C encounters an error,  moves a non-zero to return-code and
> >>exits. B sees that
> >>return-code is non-zero and simply exits. A gets the return-code set by
C.
> >>When A exits,
> >>the operating system/command shell gets the return-code set by C.  If C
is
> >>written in
> >>another language, the return mechanism works the same way.
…[6 more quoted lines elided]…
> practice" would be to never rely on it happening for you and that one
should
> ALWAYS invest the  typing time required to write "MOVE x TO RETURN-CODE"
(or
> equivalent for your compiler).

H'm! Then if program C does MOVE 16 TO RETURN-CODE,
programs B and A, in turn should do IF RETURN-CODE NOT
EQUAL ZERO, MOVE RETURN-CODE TO RETURN-CODE?

I think the rule here is that if a compiler implements a RETURN-CODE
special register, that register will be set to zero upon entry into
any program and will retain its value on exit to the calling program;
therefore, "cascading" through each program exit until another CALL
is encountered or control passes to the OS.
```

###### ↳ ↳ ↳ Re: pattern for an error

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-05-28T11:33:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l4sq341nooi4p1aflnpgdl8hufksr91qql@4ax.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com>`

```
On Wed, 28 May 2008 09:06:02 -0500, "Michael Mattias"
<mmattias@talsystems.com> wrote:

>> In my case, I don't have the option of EXIT PERFORM, so if I wanted to
>> convert an old CoBOL program to eliminate GO TOs, I would have to
…[4 more quoted lines elided]…
>[END-PERFORM]

There's a lot of old code that looks like this:
PERFORM AAAA THRU AAAA-EXIT UNTIL FILE-EOF.

AAAA.
       ...
       COMPUTE INVENTORY-TYPE = INPUT-TYPE + DATABASE-TYPE.
       IF INVENTORY-TYPE > 1212
              GO TO AAAA-EXIT
       ...
       READ MY-FILE.
       IF FILE-STATUS-OK
            CONTINUE
       ELSE
            GO TO BAD-FILE-STATUS
       END-IF.
AAAA-EXIT.
      EXIT.
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-05-28T17:36:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g1k57g$bpu$1@reader2.panix.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <l4sq341nooi4p1aflnpgdl8hufksr91qql@4ax.com>`

```
In article <l4sq341nooi4p1aflnpgdl8hufksr91qql@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:

[snip]

>There's a lot of old code that looks like this:

[snip]

>       IF FILE-STATUS-OK
>            CONTINUE
>       ELSE
>            GO TO BAD-FILE-STATUS
>       END-IF.

Wait a moment... how did IKFCBL00 compile that?

DD
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-05-28T12:45:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9v9r34li5gfth17dttv7mu7f62587uv7el@4ax.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <l4sq341nooi4p1aflnpgdl8hufksr91qql@4ax.com> <g1k57g$bpu$1@reader2.panix.com>`

```
On Wed, 28 May 2008 17:36:48 +0000 (UTC), docdwarf@panix.com () wrote:

>>       IF FILE-STATUS-OK
>>            CONTINUE
…[4 more quoted lines elided]…
>Wait a moment... how did IKFCBL00 compile that?

I don't know what IKFCBL00 is, but my IBM compiler will compile it.
But the people who code with Go To are also the people who don't use
END-IF.
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-05-28T19:10:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g1kam9$pc6$1@reader2.panix.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <l4sq341nooi4p1aflnpgdl8hufksr91qql@4ax.com> <g1k57g$bpu$1@reader2.panix.com> <9v9r34li5gfth17dttv7mu7f62587uv7el@4ax.com>`

```
In article <9v9r34li5gfth17dttv7mu7f62587uv7el@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Wed, 28 May 2008 17:36:48 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[8 more quoted lines elided]…
>I don't know what IKFCBL00 is, but my IBM compiler will compile it.

IKFCBL00 was the IBM mainframe's COBOL '74 compiler; scope delimiters did 
not appear until the 1985 standard.

DD
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 6)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-05-28T15:55:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pVj%j.1$t07.0@newsfe22.lga>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <l4sq341nooi4p1aflnpgdl8hufksr91qql@4ax.com> <g1k57g$bpu$1@reader2.panix.com> <9v9r34li5gfth17dttv7mu7f62587uv7el@4ax.com>`

```

Howard Brazee <howard@brazee.net> wrote in message
news:9v9r34li5gfth17dttv7mu7f62587uv7el@4ax.com...
> On Wed, 28 May 2008 17:36:48 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[10 more quoted lines elided]…
> END-IF.

A calumny, that, thou poltroon.

END-IF is too useful not to be used, even for the non-GOTO-challenged.

PL
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-05-28T22:09:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IKk%j.872839$Gl5.737087@fe02.news.easynews.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <rjoq345rnsr7tkls16ril9d30coqvsvu08@4ax.com> <REd%j.5494$Ri.4180@flpi146.ffdc.sbc.com> <l4sq341nooi4p1aflnpgdl8hufksr91qql@4ax.com> <g1k57g$bpu$1@reader2.panix.com> <9v9r34li5gfth17dttv7mu7f62587uv7el@4ax.com>`

```
To use product names (rather than the PGM= name from JCL).

For the "MVS" environment (including OS/390, z/OS - but not VSE),

Any compiler from VS COBOL II, R1 and later will allow END-IF.  (VS COBOL II, 
R1, R1.2, and R2 were '74 Standard compilers.  VS COBOL II R3.0 and later 
support eh '85 Standard).  They also support - as an extension - NEXT SENTENCE 
in an IF that ends with END-IF.  Support for END-xxxx syntax is available even 
when CMPR2 is used to emulate a '74 Standard compiler - sort-of.

Any compiler from OS/VS COBOL or earlier will NOT support END-IF (or any other 
END-xxxx syntax).

  ***

 Most (but certainly NOT ALL) code with
    GO TO NNN-PARA-NAME-EXIT
syntax in it (especially if coded in all CAPS) was PROBABLY originally coded for 
OS/VS COBOL or someone who was trained on OS/VS COBOL (or earlier).  If that 
is/was the case, then you will NOT see

    GO TO NNN-PARA-NAME-EXIT

In an IF statement that is terminated by END-IF.  If you see the combination of 
that type of GO TO (especially in CAPS and END-IF), the changes are medium-good 
that you are looking at code that has been maintained (in the last 20 years) but 
never really "upgraded" to current coding techniques.

All of this is VAST generalizations and many exceptions do exist (on IBM 
mainframes and elsewhere).
```

###### ↳ ↳ ↳ Re: pattern for an error

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-05-29T01:14:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g1l02d$oo4$1@reader2.panix.com>`
- **References:** `<846f69cb-ff3f-4c47-bb1c-3c06ccbedc81@d1g2000hsg.googlegroups.com> <g1k57g$bpu$1@reader2.panix.com> <9v9r34li5gfth17dttv7mu7f62587uv7el@4ax.com> <IKk%j.872839$Gl5.737087@fe02.news.easynews.com>`

```
In article <IKk%j.872839$Gl5.737087@fe02.news.easynews.com>,
William M. Klein <wmklein@nospam.netcom.com> wrote:

[snip]

>In an IF statement that is terminated by END-IF.  If you see the combination of 
>that type of GO TO (especially in CAPS and END-IF), the changes are medium-good 
>that you are looking at code that has been maintained (in the last 20
>years) but 
>never really "upgraded" to current coding techniques.

Where is it... ahhhhh, wonderful thing, this Web... DejaNews... errrr, 
Google Groups shows something from almost half of the aforementioned 20 
years ago.  Posted 19 Mar 1999, found at 
<http://groups.google.com/group/comp.lang.rexx/msg/29d1b77320d7bfc7?dmode=source<

--begin quoted text:

>Other may prefer programming languages with more modern 
>constructs.

Others may, sure... but let them *try* to get some code past a review and
implemented into Prod!

'What is *this* stuff?  EVALUATE TRUE WHEN cond-1 imperative statement...
you call this COBOL?!?'

'Oh, please, Mr Standards-and-Practises Reviewmeister, it is exactly what
is allowed by the ANSI '85 Standard.'

'ANSI '85?  Crap, I *knew* things were goin' ta hell in a handbasket when
we allowed them fancy ANSI '74 constructs in a couple a' years back...
look, 1985 is only 14 years ago, we oughta wait until the technology is
Really Proven before we implement it.  Go back and rewrite this in *real*
COBOL, then try again.'

--end quoted text

Hmmmmm... come to think of it, the references go fill circle.  From that 
same posting, a few paragraphs earlier:

--begin quoted text:

>You might mull things over before snipping yourself, DD.  The TSO
>and Rexx overhead is only paid once.  Take a look at the "Address" 
>clause.  Once we pass control to native S/390 object code, we run at 
>native S/390 object code speeds.

TSO and Rexx overhead is one thing.. IO algorithms are another.  SyncSort,
for example, does things *much* more efficiently than, say, MVS BASIC and
I am assuming - rightfully or wrongly - that such a thing is at work when
IKJEFT01 moves faster than a COBOL program does.  Both are doing the same
thing - READ an inrec, INSERT it into a table-row, all IO, nothing more -
so I conclude that the IO subroutines included into the LM generated by
HEWL from the object code generated by IKFCBL00/IGYCRCTL are less
efficient than those used by IKJEFT01... if this assumption or conclusion,
based as both most obviously are, in conjecture, ignorance and overall
cogitative sloth, are incorrect, then be so kind as to point out where the
error was generated.

--end quoted text

(notice the fancy-pantsed and newfangled use of HEWL instead of IEWL, 
too!)

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
