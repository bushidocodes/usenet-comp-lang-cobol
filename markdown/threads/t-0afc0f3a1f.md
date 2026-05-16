[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OpenCOBOL problem

_38 messages · 10 participants · 2010-11_

**Topics:** [`Open-source COBOL (GnuCOBOL, OpenCOBOL, TinyCOBOL)`](../topics.md#open-source)

---

### OpenCOBOL problem

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-11T18:36:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k2rckFpfU1@mid.individual.net>`

```
Anybody here doing stuff with OpenCOBOL?  I have a problem that one
would think would be easy to fix.  I can't seem to open a file for
input.

Here is my test program.

-----------------------------------------------

       Identification Division.

       Program-ID.    Tfile.
       Author.        Bill Gunshannon.
       Date-Written.  10 November 2010.
       Date-Compiled.

 
       Environment Division.
 
       Configuration Section.

       Source-Computer.  FreeBSD.
       Object-Computer.  FreeBSD.
 
       Input-Output Section.

       File-Control.
           Select Datafile Assign To 'datafile'.


       Data Division.
 
       File Section.
       FD  Datafile
           Data Record Is In-Record.

       01  In-Record  Pic X(9).

 
 
       Working-Storage Section.

       Linkage Section.

       Procedure Division.

       000-Init.
           Display "Open File".
           Open Input Datafile.
           Display "Close File".
           Close Datafile
           Display "Exit Program".
           Stop Run.

-----------------------------------------------

Here is the output under TinyCOBOL.


Open File
Close File
Exit Program
Open File

And here is the output from the exact same program under OpenCOBOL.

libcob: Permanent file error (STATUS = 30) File : 'datafile'


What am I misreading in the users manual?
I would really like to move to OpenCOBOL from TinyCOBOL but this is
a real showstopper.

bill
```

#### ↳ Re: OpenCOBOL problem

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-11-11T12:02:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2c3bc554-85f3-410d-a3e0-c969f49d0f2d@f16g2000prj.googlegroups.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net>`

```
On Nov 12, 7:36 am, billg...@cs.uofs.edu (Bill Gunshannon) wrote:


Scraping your source code to my system as open30.cbl gives:

[riplin@azonic testcobc]$ ./runopen30
Open File
/home/riplin/cobol/testcobc/open30.cbl:0: libcob: File does not exist
(STATUS = 35) File : 'datafile'

[riplin@azonic testcobc]$ touch datafile

[riplin@azonic testcobc]$ ./runopen30
Open File
Close File
Exit Program

runopen30 is:

#!/bin/sh
LD_LIBRARY_PATH=${COBOLITDIR}/lib
export LD_LIBRARY_PATH
DB_HOME=./locks
COB_SYNC=P
export DB_HOME COB_SYNC
cobc -x open30.cbl
./open30
```

##### ↳ ↳ Re: OpenCOBOL problem

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-11T20:39:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k32j7FpfU4@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <2c3bc554-85f3-410d-a3e0-c969f49d0f2d@f16g2000prj.googlegroups.com>`

```
In article <2c3bc554-85f3-410d-a3e0-c969f49d0f2d@f16g2000prj.googlegroups.com>,
	Richard <riplin@Azonic.co.nz> writes:
> On Nov 12, 7:36ï¿½am, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> Scraping your source code to my system as open30.cbl gives:
…[17 more quoted lines elided]…
> ./open30

What the hell is all that?  Somehow, I can't see the average user
jumping thru those kinda hoops to run a program.  Why do I suddenly
have the feeling OpenCOBOL is not ready for primetime?

bill
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-11-11T13:19:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d781bf38-0931-4168-8f6c-e585521480fd@w38g2000pri.googlegroups.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <2c3bc554-85f3-410d-a3e0-c969f49d0f2d@f16g2000prj.googlegroups.com> <8k32j7FpfU4@mid.individual.net>`

```
On Nov 12, 9:39 am, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> In article <2c3bc554-85f3-410d-a3e0-c969f49d0...@f16g2000prj.googlegroups.com>,
>         Richard <rip...@Azonic.co.nz> writes:
…[26 more quoted lines elided]…
> have the feeling OpenCOBOL is not ready for primetime?

I don't see 'the average user' writing the COBOL source code either so
what is your point ?

The 'runopen30' is a shell script that ensure the correct environment
variables point to the right places for the compile, compile the
program and then run it.

The first run found that 'datafile' did not exist and was not optional
(error 35). 'touch datafile' created an empty file. The second run
executed the program which ran to completion.

Here is a run without the 'confusing' compilation gubbins:

[riplin@azonic testcobc]$ ./open30
Open File
Close File
Exit Program
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 4)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-11T23:22:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k3c69FpfU6@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <2c3bc554-85f3-410d-a3e0-c969f49d0f2d@f16g2000prj.googlegroups.com> <8k32j7FpfU4@mid.individual.net> <d781bf38-0931-4168-8f6c-e585521480fd@w38g2000pri.googlegroups.com>`

```
In article <d781bf38-0931-4168-8f6c-e585521480fd@w38g2000pri.googlegroups.com>,
	Richard <riplin@Azonic.co.nz> writes:
> On Nov 12, 9:39ï¿½am, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
>> In article <2c3bc554-85f3-410d-a3e0-c969f49d0...@f16g2000prj.googlegroups.com>,
…[40 more quoted lines elided]…
> Exit Program

And the $64,000 question is why didn't the install procedure set all this
up in the first place?  

bill
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-11-11T13:32:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<927bb100-93f7-4a57-a6c8-19e671807bfc@g20g2000prg.googlegroups.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <2c3bc554-85f3-410d-a3e0-c969f49d0f2d@f16g2000prj.googlegroups.com> <8k32j7FpfU4@mid.individual.net>`

```
On Nov 12, 9:39 am, billg...@cs.uofs.edu (Bill Gunshannon) wrote:

>
> What the hell is all that?  Somehow, I can't see the average user
> jumping thru those kinda hoops to run a program.  Why do I suddenly
> have the feeling OpenCOBOL is not ready for primetime?

What version of OpenCobol are you using ?  What OS ?  Which file
system is it set for.

Does the 'datafile' exist and what created it, does it have
appropriate permissions ?
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 4)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-11T23:30:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k3cjuFpfU7@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <2c3bc554-85f3-410d-a3e0-c969f49d0f2d@f16g2000prj.googlegroups.com> <8k32j7FpfU4@mid.individual.net> <927bb100-93f7-4a57-a6c8-19e671807bfc@g20g2000prg.googlegroups.com>`

```
In article <927bb100-93f7-4a57-a6c8-19e671807bfc@g20g2000prg.googlegroups.com>,
	Richard <riplin@Azonic.co.nz> writes:
> On Nov 12, 9:39ï¿½am, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
>>
…[3 more quoted lines elided]…
> What version of OpenCobol are you using ?  

Different versions from 0.72 up to 1.1.

>                                            What OS ?  

BSD and Linux.

>                                                       Which file
> system is it set for.

Huh?  The native one, obviously.

> Does the 'datafile' exist 

"File not found" is Status: 35, not 30.

>                            and what created it, 

One created with cat.  One created with vi.  And one created by opening
a file for output from an OpenCOBOL program (which worked just fine.)

>                                                  does it have
> appropriate permissions ?

Take your pick.  Default was rw-r--r-- and tried everything up to
rwxrwxrwx.

And all of this misses the fact that on the same systems the same
program worked with TinyCOBOL without jumping thru hoops.  Based
on another posting, it looks like OpenCOBOL does not do all it
needs to when it installs.

bill
```

#### ↳ Re: OpenCOBOL problem

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-11-11T13:26:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4kYCo.14565$Ou2.11691@newsfe20.iad>`
- **In-Reply-To:** `<8k2rckFpfU1@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net>`

```
On 11/11/2010 11:36 AM, Bill Gunshannon wrote:

TOP POST only

Not a problem I run into (in my compiler) because within OO classes I 
pass the External file name to the File-Class.

I think the problem must be related to your use of the word 'datafile', 
you are doing the equivalent of :-

Select Datafile Assign To 'datafile',

which is like writing :-

Select CustomerFile Assign To 'customerfile'

See if this works :-

Select Data-File Assign To 'datafile',

Jimmy

> Anybody here doing stuff with OpenCOBOL?  I have a problem that one
> would think would be easy to fix.  I can't seem to open a file for
…[71 more quoted lines elided]…
>
```

##### ↳ ↳ Re: OpenCOBOL problem

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-11T20:36:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k32f3FpfU3@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <4kYCo.14565$Ou2.11691@newsfe20.iad>`

```
In article <4kYCo.14565$Ou2.11691@newsfe20.iad>,
	James Gavan <jgavan@shaw.ca> writes:
> On 11/11/2010 11:36 AM, Bill Gunshannon wrote:
> 
…[16 more quoted lines elided]…
> Select Data-File Assign To 'datafile',

Tried it with a lot of different filenames.  No difference.
And, remember, it works with the other Open Source COBOL Compiler
so the COBOL is most likely valid (actually, I know it is as I
have been doing COBOL a pretty long time.)

This is definitely something unique to OpenCOBOL.

bill
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-11-12T12:00:21+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k3as7Fa25U1@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <4kYCo.14565$Ou2.11691@newsfe20.iad> <8k32f3FpfU3@mid.individual.net>`

```
Bill Gunshannon wrote:
> In article <4kYCo.14565$Ou2.11691@newsfe20.iad>,
> James Gavan <jgavan@shaw.ca> writes:
…[27 more quoted lines elided]…
> bill

Bill,

your code is fine.

The problem is that you aren't checking for exceptions.

The first Open causes an exception if the file doesn't exist. Try running 
the same code having created the file. I'm betting it works as expected.

At the risk of teaching Granma' to suck eggs, you could create the file 
easily in a step before running the program, with the following DOS command:

ECHO 123456789 > datafile

Then run it.

You should really add a FILE STATUS to the FD and check it.

HTH,

Pete.
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 4)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-11T23:45:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k3dg0FpfU9@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <4kYCo.14565$Ou2.11691@newsfe20.iad> <8k32f3FpfU3@mid.individual.net> <8k3as7Fa25U1@mid.individual.net>`

```
In article <8k3as7Fa25U1@mid.individual.net>,
	"Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
> Bill Gunshannon wrote:
>> In article <4kYCo.14565$Ou2.11691@newsfe20.iad>,
…[36 more quoted lines elided]…
> The first Open causes an exception if the file doesn't exist. 

The file does exist.  Why would people here think I would try to open
a non-existant file for input?  And, the error for a non-existant file
is 30, not 35.

>                                                               Try running 
> the same code having created the file. I'm betting it works as expected.

You would have lost that bet.

> 
> At the risk of teaching Granma' to suck eggs, you could create the file 
> easily in a step before running the program, with the following DOS command:

Not using DOS!!

> 
> ECHO 123456789 > datafile
…[3 more quoted lines elided]…
> You should really add a FILE STATUS to the FD and check it.

Why?  It is printing the File Status out just fine: 35.
Now, if I was going to try to continue to run I might try capturing the
Status, but if it can't open the input file there really is little reason
for continuing.


bill 
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-11-12T13:41:09+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k3gp5F9mvU1@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <4kYCo.14565$Ou2.11691@newsfe20.iad> <8k32f3FpfU3@mid.individual.net> <8k3as7Fa25U1@mid.individual.net> <8k3dg0FpfU9@mid.individual.net>`

```
Bill Gunshannon wrote:
> In article <8k3as7Fa25U1@mid.individual.net>,
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
…[70 more quoted lines elided]…
> bill

OK. Sorry the suggestion was no help.

Pete.
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 6)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-12T14:15:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k50g3FagkU2@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <4kYCo.14565$Ou2.11691@newsfe20.iad> <8k32f3FpfU3@mid.individual.net> <8k3as7Fa25U1@mid.individual.net> <8k3dg0FpfU9@mid.individual.net> <8k3gp5F9mvU1@mid.individual.net>`

```
In article <8k3gp5F9mvU1@mid.individual.net>,
	"Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
> Bill Gunshannon wrote:
>> In article <8k3as7Fa25U1@mid.individual.net>,
…[73 more quoted lines elided]…
> OK. Sorry the suggestion was no help.

Actually, Richard had the answer.  It's just not one anyone would want
to see.  The install on both BSD and Linux appears to be very incomplete
leaving out a lot of environment stuff that is necessary for it to work.
Of course, his little script (which is also unacceptable in a production
environment, at least in mine) is installation specific so having no idea
what any of that means I could not duplicate any of it for my systems
beyond the LD_LIBRARY.  I will look into this further now that I know
the problem is with the install and maybe fix it.  Or maybe I should be
be taking a look at the recent OpenSource COBOL from france.  I just know
that TinyCOBOL isn't cutting it any more and I need a replacement.

bill
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-11-13T03:43:00+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k523kFpqsU1@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <4kYCo.14565$Ou2.11691@newsfe20.iad> <8k32f3FpfU3@mid.individual.net> <8k3as7Fa25U1@mid.individual.net> <8k3dg0FpfU9@mid.individual.net> <8k3gp5F9mvU1@mid.individual.net> <8k50g3FagkU2@mid.individual.net>`

```
Bill Gunshannon wrote:
> In article <8k3gp5F9mvU1@mid.individual.net>,
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
…[89 more quoted lines elided]…
> bill

I'm glad you at least found out what was wrong.

Open COBOL seems to be a pretty good product. Bill Klein  had a go at 
installing it under Windows and wrote up his experience here:

http://primacomputing.co.nz/cobol21/opencobol.aspx


I know you're not using Windows but the process he went through might jog 
something or suggest something for a re-install. Failing that, the OC forum 
at: http://www.opencobol.org/

...is pretty lively. (and helpful...)

I'm glad it turned out to be an install problem because your code looked 
fine to me.

It wasn't clear (to me, at least... although I maybe could have looked 
closer...) that you had actually created the file, but once that was 
established, and there were still problems, it was likely to be an 
environment problem.  Richard has good experience with the environment you 
are using and was the right person to assist you.

Thanks for letting us know the current status.

Pete.
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-11-12T15:24:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ibjm73$2sr$3@reader1.panix.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <8k32f3FpfU3@mid.individual.net> <8k3as7Fa25U1@mid.individual.net> <8k3dg0FpfU9@mid.individual.net>`

```
In article <8k3dg0FpfU9@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:

[snip]

>The file does exist.  Why would people here think I would try to open
>a non-existant file for input?

I barely know why *I* think anything, Mr Gunshannon, let alone anyone 
else... but it might be, possibly, that people responding here have enough 
experience under their belts to have made that very mistake themselves.

(It may be Hardware Troubleshooting, granted, but no matter *who* says 'I 
have a problem with (device)' a frequently-encountered response is 'Is it 
plugged in?')

DD
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 6)_

- **From:** PR <paul.raulerson@gmail.com>
- **Date:** 2010-11-16T13:48:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<06f5c3b1-ffda-41aa-bba8-6fb7b26844ed@p11g2000vbn.googlegroups.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <8k32f3FpfU3@mid.individual.net> <8k3as7Fa25U1@mid.individual.net> <8k3dg0FpfU9@mid.individual.net> <ibjm73$2sr$3@reader1.panix.com>`

```
I'm still trying to puzzle out what the original problem might have
been. I cut and pasted the sample code and compiled and ran it on
three systems (Linux x64, Linux x32, and z/Linux64) with no issues.
Other than I had to create a data file of course.

-Paul


On Nov 12, 9:24 am, docdw...@panix.com () wrote:
> In article <8k3dg0Fp...@mid.individual.net>,
>
…[15 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 7)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-17T00:18:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kgl9vFlfcU1@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <8k32f3FpfU3@mid.individual.net> <8k3as7Fa25U1@mid.individual.net> <8k3dg0FpfU9@mid.individual.net> <ibjm73$2sr$3@reader1.panix.com> <06f5c3b1-ffda-41aa-bba8-6fb7b26844ed@p11g2000vbn.googlegroups.com>`

```
In article <06f5c3b1-ffda-41aa-bba8-6fb7b26844ed@p11g2000vbn.googlegroups.com>,
	PR <paul.raulerson@gmail.com> writes:
> I'm still trying to puzzle out what the original problem might have
> been. I cut and pasted the sample code and compiled and ran it on
> three systems (Linux x64, Linux x32, and z/Linux64) with no issues.
> Other than I had to create a data file of course.

The problem appears to be in the build/install scripts provided for 
both BSD and Linux.  Wether or not I have the time or inclination to
try and fix it remains to be seen.  In the meantime I have to go back
to using TinyCOBOL which I already know will not work for some of my
near-term projects.

bill
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 8)_

- **From:** PR <paul.raulerson@gmail.com>
- **Date:** 2010-11-18T11:09:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<729416b6-0569-4516-a61f-3bd92f162aff@p1g2000yqm.googlegroups.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <8k32f3FpfU3@mid.individual.net> <8k3as7Fa25U1@mid.individual.net> <8k3dg0FpfU9@mid.individual.net> <ibjm73$2sr$3@reader1.panix.com> <06f5c3b1-ffda-41aa-bba8-6fb7b26844ed@p11g2000vbn.googlegroups.com> <8kgl9vFlfcU1@mid.individual.net>`

```
On Nov 16, 6:18 pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> In article <06f5c3b1-ffda-41aa-bba8-6fb7b2684...@p11g2000vbn.googlegroups.com>,
>         PR <paul.rauler...@gmail.com> writes:
…[18 more quoted lines elided]…
> Scranton, Pennsylvania   |         #include <std.disclaimer.h>  

What platform are you building on? It works just fine on everything I
have tried it on, from MacOS to z/Linux.
You do have to have the pre-requisites installed, but the ./configure
step should catch all of those for you.

I don't use OpenCOBOL for production projects unless I use the Oracle
branded version of BerkeleyDB, but other than that, I
have not found many problems with it.

-Paul
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 9)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-18T20:05:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8klf7qF150U2@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <8k32f3FpfU3@mid.individual.net> <8k3as7Fa25U1@mid.individual.net> <8k3dg0FpfU9@mid.individual.net> <ibjm73$2sr$3@reader1.panix.com> <06f5c3b1-ffda-41aa-bba8-6fb7b26844ed@p11g2000vbn.googlegroups.com> <8kgl9vFlfcU1@mid.individual.net> <729416b6-0569-4516-a61f-3bd92f162aff@p1g2000yqm.googlegroups.com>`

```
In article <729416b6-0569-4516-a61f-3bd92f162aff@p1g2000yqm.googlegroups.com>,
	PR <paul.raulerson@gmail.com> writes:
> On Nov 16, 6:18ï¿½pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
>> In article <06f5c3b1-ffda-41aa-bba8-6fb7b2684...@p11g2000vbn.googlegroups.com>,
…[14 more quoted lines elided]…
> have tried it on, from MacOS to z/Linux.

FreeBSD 7.x and 8.x and RedHat (specifically Scientific Linux)

> You do have to have the pre-requisites installed, but the ./configure
> step should catch all of those for you.

You would think that.  :-)

> I don't use OpenCOBOL for production projects unless I use the Oracle
> branded version of BerkeleyDB, but other than that, I
> have not found many problems with it.

There must be installs somewhere that work.  I can't believe everyone
would be having this problem, fixing it themselves and not telling
anyone.

bill
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 10)_

- **From:** Paul <paul-nospamatall.raulerson@mac.com>
- **Date:** 2010-11-22T22:21:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ceb4141$0$14799$bbae4d71@news.suddenlink.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <ibjm73$2sr$3@reader1.panix.com> <06f5c3b1-ffda-41aa-bba8-6fb7b26844ed@p11g2000vbn.googlegroups.com> <8kgl9vFlfcU1@mid.individual.net> <729416b6-0569-4516-a61f-3bd92f162aff@p1g2000yqm.googlegroups.com> <8klf7qF150U2@mid.individual.net>`

```
On 2010-11-18 14:05:15 -0600, Bill Gunshannon said:

Well, I just installed SL 5.5 x86_64 in a VMWare instance and built 
OpenCobol with only a few little issues, like having to install GMP.

Your code compiles and operates correctly, so I think you may have 
something else wrong.

I tend to prefer SuSE Linux distributions myself, as they are 
marginally more complete, and have YAST.

-Paul



> In article <729416b6-0569-4516-a61f-3bd92f162aff@p1g2000yqm.googlegroups.com>,
> 	PR <paul.raulerson@gmail.com> writes:
…[33 more quoted lines elided]…
> bill
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 11)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-23T13:18:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8l1t89F3i5U1@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <ibjm73$2sr$3@reader1.panix.com> <06f5c3b1-ffda-41aa-bba8-6fb7b26844ed@p11g2000vbn.googlegroups.com> <8kgl9vFlfcU1@mid.individual.net> <729416b6-0569-4516-a61f-3bd92f162aff@p1g2000yqm.googlegroups.com> <8klf7qF150U2@mid.individual.net> <4ceb4141$0$14799$bbae4d71@news.suddenlink.net>`

```
In article <4ceb4141$0$14799$bbae4d71@news.suddenlink.net>,
	Paul <paul-nospamatall.raulerson@mac.com> writes:
> On 2010-11-18 14:05:15 -0600, Bill Gunshannon said:
> 
…[4 more quoted lines elided]…
> something else wrong.

As I had said.  It is intereting that I grabbed a new copy of the 1.1
distribution yesterday and it installed cleanly and worked perfectly
with my test program on the same Linux Distro that had failed 2-3 weeks
ago.

> 
> I tend to prefer SuSE Linux distributions myself, as they are 
> marginally more complete, and have YAST.

I chose Scientific Linux as a read of their info showed it to be
targetted at the academic type environment.  So far, OpenCOBOL was
the only problem I have had and I don't anticipate any others.

bill
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 5)_

- **From:** PR <paul.raulerson@gmail.com>
- **Date:** 2010-11-16T13:49:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9b62d32b-b179-44b2-940a-b37786a2c89f@l32g2000yqc.googlegroups.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <4kYCo.14565$Ou2.11691@newsfe20.iad> <8k32f3FpfU3@mid.individual.net> <8k3as7Fa25U1@mid.individual.net> <8k3dg0FpfU9@mid.individual.net>`

```
On Nov 11, 5:45 pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> In article <8k3as7Fa2...@mid.individual.net>,
>         "Pete Dashwood" <dashw...@removethis.enternet.co.nz> writes:
…[80 more quoted lines elided]…
> Scranton, Pennsylvania   |         #include <std.disclaimer.h>
```

#### ↳ Re: OpenCOBOL problem

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-11-11T14:26:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_bZCo.15684$Mk2.7824@newsfe13.iad>`
- **In-Reply-To:** `<8k2rckFpfU1@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net>`

```
On 11/11/2010 11:36 AM, Bill Gunshannon wrote:
> Anybody here doing stuff with OpenCOBOL?  I have a problem that one
> would think would be easy to fix.  I can't seem to open a file for
> input.
>
> Here is my test program.

Ahhh Richard's reply was the giveaway :-

 From my class that has the M/F file-status error codes :-

05 pic x(L2) value "30I-O error/Data check parity err.".
05 pic x(L2) value "34Boundary violation              ".
05 pic x(L2) value "35Open IO/INPUT/EXTEND non-optionl".

Here's your program using M/F Net Express :-

--------------------------------------------------

Program-ID.    Tfile.
Author.        Bill Gunshannon.

File-Control.
     Select Datafile Assign To 'datafile'.

Data Division.

File Section.
FD  Datafile
     Data Record Is In-Record.

01  In-Record  Pic X(9).

Procedure Division.

Open Output DataFile       *> Add these two lines
Close DataFile             *>  ..   ..  ..  ..
Display "Open File".
Open Input Datafile.
Display "Close File".
Close Datafile
Display "Exit Program".
Stop Run.

I didn't invoke my File Status class, just Procedural to see what would 
happen. First time around, tried it without my two additional lines. 
Surprisingly, never seen it before, but M/F came back with their own 
Message - Error 13 File doesn't exist

Don't know whether Open Source has used some of the PC-based CBL_ 
routines available in Fujitsu or Micro Focus, but I use :-

Call CBL_CHECK_FILE_EXISTS using filename returning Result

if Result is incorrect then you need an Open-New-File routine, those 
first two lines.

Did you test TinyCOBOL against an EXISTING file - ????

Got caught years ago. Wrote part of an application where I used M/F 
Directives to compress records. Worked fine. Looked at it some eight 
months later testing it and it went belly-up.

Famous "Well it used to work". Contacted M/F Forum they were helpful but 
no joy. Some further six months went by - and then it clicked.
On the re-vamp, I had excluded the compress Directive. Without the 
directive the new version couldn't expand records to their true length !

Jimmy
```

##### ↳ ↳ Re: OpenCOBOL problem

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-11T23:35:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k3cu7FpfU8@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <_bZCo.15684$Mk2.7824@newsfe13.iad>`

```
In article <_bZCo.15684$Mk2.7824@newsfe13.iad>,
	James Gavan <jgavan@shaw.ca> writes:
> On 11/11/2010 11:36 AM, Bill Gunshannon wrote:
>> Anybody here doing stuff with OpenCOBOL?  I have a problem that one
…[11 more quoted lines elided]…
> 05 pic x(L2) value "35Open IO/INPUT/EXTEND non-optionl".

Actually, everything I  found says 35 is a "boundry violation", whatever
that is.

> 
> Here's your program using M/F Net Express :-
…[19 more quoted lines elided]…
> Open Output DataFile       *> Add these two lines

Why would I open an input datafile for output?  Wouldn't that basicly
truncate the file making it empty?

> Close DataFile             *>  ..   ..  ..  ..
> Display "Open File".
…[19 more quoted lines elided]…
> Did you test TinyCOBOL against an EXISTING file - ????

I tested tjhis program against an existing file.  That's what
input files tend to be.  If the file doesn't exist TinyCOBOL
fails, too, but for 30 - File Not Found, not 35.

> 
> Got caught years ago. Wrote part of an application where I used M/F 
…[7 more quoted lines elided]…
> 

All of which is irrelevant to this problem.

bill
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-11-11T18:00:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<227e30b3-ee8c-4a99-b931-fc867826c528@g4g2000prj.googlegroups.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <_bZCo.15684$Mk2.7824@newsfe13.iad> <8k3cu7FpfU8@mid.individual.net>`

```
On Nov 12, 12:35 pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> In article <_bZCo.15684$Mk2.7...@newsfe13.iad>,


> Actually, everything I  found says 35 is a "boundry violation", whatever
> that is.

What 'everything' is that ?  34 is boundary violation. With ANS85 you
will get '35' for file not found, or '05' if it is not found and is
optional.

My run of your program give a 35 error.

Note that OpenCOBOL can work.

30 implies 'failed' and 'no extra information' which implies that the
file handler is not installed, or not found.

OpenCOBOL can use various file handlers including BerkelyDB or VBisam
(I think).

--with-db1        use Berkeley DB 1.85 (libdb-1.85)
--with-db         use Berkeley DB 3.0 or later (default)
--with-lfs64      use large file system for file I/O (default)

If it can't find the libraries then it may fail in ways that match
your results.
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 4)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-12T14:20:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k50omFagkU3@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <_bZCo.15684$Mk2.7824@newsfe13.iad> <8k3cu7FpfU8@mid.individual.net> <227e30b3-ee8c-4a99-b931-fc867826c528@g4g2000prj.googlegroups.com>`

```
In article <227e30b3-ee8c-4a99-b931-fc867826c528@g4g2000prj.googlegroups.com>,
	Richard <riplin@Azonic.co.nz> writes:
> On Nov 12, 12:35ï¿½pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
>> In article <_bZCo.15684$Mk2.7...@newsfe13.iad>,
…[5 more quoted lines elided]…
> My run of your program give a 35 error.

That was because you hadn't put a datafile there for it to try to open.

> Note that OpenCOBOL can work.
> 30 implies 'failed' and 'no extra information' which implies that the
…[7 more quoted lines elided]…
> your results.

And, why does the install not set all this up like other packages do?
I built it from source on both machines after successfully running
configure.  I find it hard to believe that anyone is using this package
if a normal install results in a non-operational compiler.

Maybe COBOL really is dead!!

bill
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-11-13T03:44:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k5279FqhaU1@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <_bZCo.15684$Mk2.7824@newsfe13.iad> <8k3cu7FpfU8@mid.individual.net> <227e30b3-ee8c-4a99-b931-fc867826c528@g4g2000prj.googlegroups.com> <8k50omFagkU3@mid.individual.net>`

```
Bill Gunshannon wrote:
> In article
> <227e30b3-ee8c-4a99-b931-fc867826c528@g4g2000prj.googlegroups.com>,
…[30 more quoted lines elided]…
> Maybe COBOL really is dead!!

Or maybe it's the people using it... :-)

Pete.
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 6)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-12T15:23:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k54feFagkU6@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <_bZCo.15684$Mk2.7824@newsfe13.iad> <8k3cu7FpfU8@mid.individual.net> <227e30b3-ee8c-4a99-b931-fc867826c528@g4g2000prj.googlegroups.com> <8k50omFagkU3@mid.individual.net> <8k5279FqhaU1@mid.individual.net>`

```
In article <8k5279FqhaU1@mid.individual.net>,
	"Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
> Bill Gunshannon wrote:
>> In article
…[34 more quoted lines elided]…
> 

Well, that was a little tongue-in-cheek but I do find it
very hard to believe that something like this cold actually
exist.  I will probably be able to fix it knowing that it
is apparently an install/environment problem but I know
from experience that there are very few people who might be
interested in taking a look at COBOL who could or would be
willing to put forth the effort if a normal install just
resulted in a broken compiler.  That tells me there is
probably a very, very small group of people actually using
it.

As someone who is still hoping to get back into full-time
COBOL programming (I have applications for two jobs being
considered right now) because of how much I always liked
the language it is very disheartening to know that giving
it a try is so hard compared to other much less adequate
languages.

bill
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-11-11T20:39:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7G2Do.29415$F77.6902@newsfe07.iad>`
- **In-Reply-To:** `<8k3cu7FpfU8@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <_bZCo.15684$Mk2.7824@newsfe13.iad> <8k3cu7FpfU8@mid.individual.net>`

```
On 11/11/2010 4:35 PM, Bill Gunshannon wrote:
> In article<_bZCo.15684$Mk2.7824@newsfe13.iad>,
> 	James Gavan<jgavan@shaw.ca>  writes:
…[85 more quoted lines elided]…
>
I was surprised when Pete backed off with a very polite apology for not 
producing useful information. I'm surprised he didn't tell you to Piss 
Off. You may take it I'm already pissed off at you, particularly the 
last sentence above.

OK go take a glass of water or something. Are you support programming 
staff at the University or are you an instructor. If you are a teacher, 
Christ help your students if you can lose your cool over something this 
trivial and condemn a compiler as being defective.

Now make the bloody effort to read the Open Source COBOL manual, which I 
did for the first time. References to your problem :-

4.7 		File Status Table
6.32 		OPEN
7.3.1.14 	CBL_CHECK_FILE_EXISTS
8.1. 		FileStat-Msgs.cpy  - 35 FILE NOT FOUND

The only thing wrong with my quote from my File-Status Table

05 pic x(L2) value "35Open IO/INPUT/EXTEND non-optionl".,

was that I paraphrased it. The full M/F text for a 35 IS :-

35 An OPEN operation with the I-O, INPUT, or EXTEND phrases has been 
tried on a non-OPTIONAL file that is not present. (Take it as read - 
that is the ANSI definition).

If you aren't using File-Status checks with DECLARATIVES, (which I 
personally consider the pits), or preferably a routine that lets you 
call their File-Status message table, may I suggest that you should. If 
you are an Instructor, you aren't giving your students good advice. 
Prepare them for this problem, regardless of compiler showing literals 
for file errors. You will save them a lot of unnecessary aggravation in 
the early part of their careers.

You came here for FREE advice - and dished out your aggravation.

Jimmy
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 4)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-11-11T20:36:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d3038864-51c0-4115-9f6a-3cef6aef102b@f16g2000prj.googlegroups.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <_bZCo.15684$Mk2.7824@newsfe13.iad> <8k3cu7FpfU8@mid.individual.net> <7G2Do.29415$F77.6902@newsfe07.iad>`

```
On Nov 12, 4:39 pm, James Gavan <jga...@shaw.ca> wrote:
> On 11/11/2010 4:35 PM, Bill Gunshannon wrote:
>
…[88 more quoted lines elided]…
> last sentence above.

Well I think that he should tell you to 'piss off', you obviously do
not understand the problem.

* The file _does_ exist (in fact he tried several ways to create the
file) as he explained. Your suggestion to open output would indeed
truncate the existing file.

* The file status given by the program is '30'.

* MF's COMPRESS is irrelevant


Peter's answer was not helpful at all, and in fact was irrelevant.
Peter claimed the problem was caused by the program raising an
exception and a 'FILE STATUS IS ..' should be added. The default
action of any COBOL that I have worked with is to display the file
status code and terminate the program. There is no need to add a file
status clause or deal with the exception unless it is required for the
program to continue.

He, at least, recognised he wasn't being helpful.


> OK go take a glass of water or something. Are you support programming
> staff at the University or are you an instructor. If you are a teacher,
…[9 more quoted lines elided]…
> 8.1.            FileStat-Msgs.cpy  - 35 FILE NOT FOUND


You are idiot James. Instead of ranting actually read what his problem
is.



> The only thing wrong with my quote from my File-Status Table
>
…[18 more quoted lines elided]…
> Jimmy

The only aggravation I see is yours.
```

###### ↳ ↳ ↳ Re: OpenCOBOL problem

_(reply depth: 5)_

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-11-12T10:08:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5weDo.15732$Mk2.1873@newsfe13.iad>`
- **In-Reply-To:** `<d3038864-51c0-4115-9f6a-3cef6aef102b@f16g2000prj.googlegroups.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <_bZCo.15684$Mk2.7824@newsfe13.iad> <8k3cu7FpfU8@mid.individual.net> <7G2Do.29415$F77.6902@newsfe07.iad> <d3038864-51c0-4115-9f6a-3cef6aef102b@f16g2000prj.googlegroups.com>`

```
On 11/11/2010 9:36 PM, Richard wrote:
> On Nov 12, 4:39 pm, James Gavan<jga...@shaw.ca>  wrote:
>
I can see now what his problem was. Did he convey that initially. 
Something with different options should be read up FIRST, in detail, 
before you attempt it. Net Express handles Unix etc., most definitely I 
would have to read it up before I attempted it to establish any 
uniqueness there was.
>
> You are idiot James. Instead of ranting actually read what his problem
> is.

About some six months back somebody wrote to me, "Is he always like this 
?".  I made some trite reply. I should have written. "Very 
knowledgeable, but he can be a touchy arrogant arsehole when he chooses 
to be".
```

#### ↳ Re: OpenCOBOL problem

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-11-11T16:06:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<x4SdnRo0V4589UHRnZ2dnUVZ_t-dnZ2d@earthlink.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net>`

```
Bill Gunshannon wrote:
> Anybody here doing stuff with OpenCOBOL?  I have a problem that one
> would think would be easy to fix.  I can't seem to open a file for
…[69 more quoted lines elided]…
>

The contents of the File-Control paragraph are implementor-defined and vary 
across compilers. The default organization may be way different between 
compilers (SEQUENTIAL or something else). The "assign to" clause may 
reference a data-name defined in working storage, an external parameter, or 
be the actual name of the file itself.

And so on.

So, then, your "dataname" may be trying to reference a file that does not 
exist, cannot be found, is not defined, or whose attributes do not match the 
(implied) definition.

I suggest you review the definitions of the File-Control paragraph for the 
compiler(s) you are using. You will find marked differences in their syntax 
and implementation.

Or it could be something else altogether, possibly involving a jar of 
mayonnaise.
```

#### ↳ Re: OpenCOBOL problem

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-11-12T05:17:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2da67497-30b6-4974-8de6-06b504bb8a26@v12g2000vbh.googlegroups.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net>`

```
On Nov 11, 6:36 pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> Anybody here doing stuff with OpenCOBOL?  I have a problem that one
> would think would be easy to fix.  I can't seem to open a file for
…[63 more quoted lines elided]…
>

I wouldn't wish to pour oil on troubled waters but:

1. You show 'Open File' appears twice in the program output although
that display is only executed once in your program. I presume that is
the famous red herring (Clupea harengus rudis to biologists).

2. File status code 30 is an open error with no further information
available.
I don't know how clever TinyCobol and OpenCobol are but it may be for
any one of a host of reasons from file does not exist; to the file
being empty at time of opening; to the record contents being different
from the record description definition (if you have a record of three
characters long or a record that is variable in length) to ....   It
might help to show us the contents of the file.
```

##### ↳ ↳ Re: OpenCOBOL problem

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-12T14:26:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k5151FagkU4@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <2da67497-30b6-4974-8de6-06b504bb8a26@v12g2000vbh.googlegroups.com>`

```
In article <2da67497-30b6-4974-8de6-06b504bb8a26@v12g2000vbh.googlegroups.com>,
	Alistair Maclean <alistair.j.l.maclean@googlemail.com> writes:
> On Nov 11, 6:36ï¿½pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
>> Anybody here doing stuff with OpenCOBOL? ï¿½I have a problem that one
…[68 more quoted lines elided]…
> the famous red herring (Clupea harengus rudis to biologists).

Bad cut and paste.  The second Open File should be the first line of
the output from OpenCOBOL showing that the error occurs on the file
open attempt.  Sorry.

> 2. File status code 30 is an open error with no further information
> available.
…[5 more quoted lines elided]…
> might help to show us the contents of the file.

I have tried it with an empty file and with a file containing a few
lines of data.  It is Line Sequential so as long as the lines contain
an Unix Newline at the end of each record it should be fine (according
to the manual).  And emty file should not result in the program crashing
on the open as empty files are perfectly legitimate.

bill
```

##### ↳ ↳ Re: OpenCOBOL problem

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-11-12T09:21:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2784343-a8a2-4f69-8d64-78ed1c97abc4@r4g2000prj.googlegroups.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <2da67497-30b6-4974-8de6-06b504bb8a26@v12g2000vbh.googlegroups.com>`

```
On Nov 13, 2:17 am, Alistair Maclean
<alistair.j.l.macl...@googlemail.com> wrote:
> On Nov 11, 6:36 pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
>
…[72 more quoted lines elided]…
> the famous red herring (Clupea harengus rudis to biologists).

He ran tinyCobol which found and opened the file OK and then OpenCOBOL
which opened the file then borked with file status 30. The two 'open
file' are from the two runs, he seems to have added his comment after
the OpenCOBOL 'open file' rather than before it.

> 2. File status code 30 is an open error with no further information
> available.
…[5 more quoted lines elided]…
> might help to show us the contents of the file.

I had run his program using OpenCOBOL with no file (it gave 35
correctly), with an empty file and with a file with arbitrary data. It
didn't complain on the open.
```

#### ↳ Re: OpenCOBOL problem

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-11-12T05:19:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fdadfa3-41fc-4c42-a20b-5ea69271beaf@e20g2000vbn.googlegroups.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net>`

```
On Nov 11, 6:36 pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> Anybody here doing stuff with OpenCOBOL?  I have a problem that one
> would think would be easy to fix.  I can't seem to open a file for
…[70 more quoted lines elided]…
> Scranton, Pennsylvania   |         #include <std.disclaimer.h>  

Just a thought: Does anyone know whether either Cobol is case
sensitive on filenames?
```

##### ↳ ↳ Re: OpenCOBOL problem

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2010-11-12T14:28:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k517rFagkU5@mid.individual.net>`
- **References:** `<8k2rckFpfU1@mid.individual.net> <6fdadfa3-41fc-4c42-a20b-5ea69271beaf@e20g2000vbn.googlegroups.com>`

```
In article <6fdadfa3-41fc-4c42-a20b-5ea69271beaf@e20g2000vbn.googlegroups.com>,
	Alistair Maclean <alistair.j.l.maclean@googlemail.com> writes:
> On Nov 11, 6:36ï¿½pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
>> Anybody here doing stuff with OpenCOBOL? ï¿½I have a problem that one
…[73 more quoted lines elided]…
> sensitive on filenames?

The file name is a literal, even if contained in a variable, so, yes, it
would have to be case sensitive on a system that supported mixed case.

bill
```

#### ↳ Re: OpenCOBOL problem

- **From:** Brian Tiffin <btiffin@canada.com>
- **Date:** 2010-11-20T22:39:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6e23b0ce-2aee-401f-9a0f-eb9ad3ba650e@z19g2000yqb.googlegroups.com>`
- **References:** `<8k2rckFpfU1@mid.individual.net>`

```
On Nov 11, 1:36 pm, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> Anybody here doing stuff with OpenCOBOL?  I have a problem that one
> would think would be easy to fix.  I can't seem to open a file for
…[70 more quoted lines elided]…
> Scranton, Pennsylvania   |         #include <std.disclaimer.h>  

Just in case; see http://opencobol.add1tocobol.com/#assign as you may
have an environment variable in between you and your local file.
OpenCOBOL follows a configuration setting.

# If yes, file names are resolved at run time using
#   environment variables.
# For example, given ASSIGN TO "DATAFILE", the actual
#   file name will be
#  1. the value of environment variable 'DD_DATAFILE' or
#  2. the value of environment variable 'dd_DATAFILE' or
#  3. the value of environment variable 'DATAFILE' or
#  4. the literal "DATAFILE"
# If no, the value of the assign clause is the file name.
#
# Value: 'yes', 'no'
filename-mapping: yes

Umm, just in case.

Cheers,
Brian
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
