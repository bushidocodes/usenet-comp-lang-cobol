[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Getting File Name from a ksh script

_8 messages · 4 participants · 2003-12_

---

### Getting File Name from a ksh script

- **From:** "Dan" <deacondan25@N.O.S.P.A.M.hotmail.com>
- **Date:** 2003-12-04T00:33:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vstl8o6jaibl11@corp.supernews.com>`

```
We're in the process of converting from Compaq Cobol to MF Cobol.

In Compaq Cobol I could assign a generic filename then override it in a ksh
script. I MF Cobol it doesn't like that and tries to use the file in the
Select/Assign.

Here's what I am doing:

FILE-CONTROL
        SELECT TRANFILE ASSIGN TO 'TRANFILE'
                       ORGANIZATION IS LINE SEQUENTIAL.
        SELECT TRANSRPT ASSIGN TO 'TRANSRPT'.


Here's the script

TRANFILE=tranfile.dat; export TRANFILE
TRANSRPT=transrpt.lis; export TRANSRPT
pgmname.exe

Is there a way to do the same thing in MF? We have some programs that are
used multiple times with various inputs/outputs plus it is easier to track
the files in the scripts.

Thanks,
Dan
```

#### ↳ Re: Getting File Name from a ksh script

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-04T02:55:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IdGzb.12025$yd.1680464@news20.bellglobal.com>`
- **In-Reply-To:** `<vstl8o6jaibl11@corp.supernews.com>`
- **References:** `<vstl8o6jaibl11@corp.supernews.com>`

```
Dan wrote:
> We're in the process of converting from Compaq Cobol to MF Cobol.
> 
…[25 more quoted lines elided]…
> 


Use a data name instead of a quoted variable, and then set the value 
appropriately before open/close.

Donald
```

#### ↳ Re: Getting File Name from a ksh script

- **From:** "Simon Tobias" <Simon.Tobias@nospam.MicroFocus.com>
- **Date:** 2003-12-04T11:02:34
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bqn549$tiu$1@hyperion.microfocus.com>`
- **References:** `<vstl8o6jaibl11@corp.supernews.com>`

```
Hi Dan.

Rather than use

> TRANFILE=tranfile.dat; export TRANFILE
> TRANSRPT=transrpt.lis; export TRANSRPT

Micro Focus COBOL supports Filename Mapping thus :

dd_TRANFILE=tranfile.dat ; export dd_TRANFILE
dd_TRANSRPT=transrpt.lis ; export dd_TRANSRPT

This will map the 'TRANFILE' and 'TRANSRPT' definitions in your program to
the appropriate filename.

See the Server Express File Handling manual, chapter 3, in the section
"Filename Mapping" for more details.

SimonT.
```

##### ↳ ↳ Re: Getting File Name from a ksh script

- **From:** "Dan" <deacondan25@N.O.S.P.A.M.hotmail.com>
- **Date:** 2003-12-04T09:03:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vsuj69263jna54@corp.supernews.com>`
- **References:** `<vstl8o6jaibl11@corp.supernews.com> <bqn549$tiu$1@hyperion.microfocus.com>`

```
Thanks

"Simon Tobias" <Simon.Tobias@nospam.MicroFocus.com> wrote in message
news:bqn549$tiu$1@hyperion.microfocus.com...
> Hi Dan.
>
…[18 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Getting File Name from a ksh script

- **From:** "Dan" <deacondan25@N.O.S.P.A.M.hotmail.com>
- **Date:** 2003-12-05T19:57:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vt2ds66mkcvec1@corp.supernews.com>`
- **References:** `<vstl8o6jaibl11@corp.supernews.com> <bqn549$tiu$1@hyperion.microfocus.com>`

```
Thanks! This does exactly what I want. Works great!

"Simon Tobias" <Simon.Tobias@nospam.MicroFocus.com> wrote in message
news:bqn549$tiu$1@hyperion.microfocus.com...
> Hi Dan.
>
…[18 more quoted lines elided]…
>
```

#### ↳ Re: Getting File Name from a ksh script

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-12-04T11:42:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FCF1B15.F6821427@shaw.ca>`
- **References:** `<vstl8o6jaibl11@corp.supernews.com>`

```


Dan wrote:

> We're in the process of converting from Compaq Cobol to MF Cobol.
>
…[22 more quoted lines elided]…
> Dan

I have no idea what a ksh script file is, plus I'm curious what the reference
is to the pgmname.exe in that file. I've been doing the following since Day One
using RM/COBOL, Microsoft COBOL and M/F DOS COBOL and Net Express. It must be
very close to what you want to do - see if it's adaptable.

Firstly I have two sets of ISAMs (very little use of Sequentials). :-

(a) General - data applicable to all the following (b) sets
(b) Files specific to a geographical location.

The application has a Default file - one record - so uses ws-RelativeKey = 1

01 Relative-Record.
   05 Client-Facility.
      10 ClientNumber pic x(05). *> e.g. "AM500'
      10 FacilitiyNumber pic 9(02) *> e.g. "23"
   05 ClientName pic x(30). *> e.g. Amoco Canada Ltd
   05 FacilityName pc x(30) *> e.g. Waterton Ethylene Plant
   05 other stuff..........

Application starts with a Master Menu and reads the Default file to see what is
the current Client/Facility setting. Uses Client/Facility with
CBL_CHECK_FILE_EXISTS. Even just using the old limit of 8 plus 3 for suffix
each file in a subset (b) can be identified :-

AM50023I.dat - "I" = Items
AM50023R.dat - "R" = Readings etc.....

If the FILE_EXISTS fails then there's a problem. If OK then you have the
filenames to pass to called programs :-

FILE-CONTROL.

     Select               Data-File
     assign               Data-filename
     organization         indexed
     access               dynamic
     record key           Data-PrimeKey
     file status          ws-FileStatus.

Data-Filename can be passed to the called program or each called program could
read the Default file to establish what it wants.

The Master Menu also allows :-

1 - Create new set of files - prompts for Client/Facility and then repeats
above opening a fresh set of files and putting the new ID in the Default File..

2. User might have finished with current set after two hours. Selects from Menu
to change current  ID. (Obviously close existing set). Prompt for new
Client/Facility ID which is put into the Default record and as above,
"CHECK_EXISTS" or prompt 'Do you want a new set ?'.

Even given a multi user situation the (Relative) Default File could have a
record per user - for ten users, records 1 through 10. Don't do something daft
like allocating a 3-digit user ID otherwise you finish up with unnecessary
empty space in your Relative file.

Any resemblance to what you want to do - if not come back with specifics ?

"We have some programs that are used multiple times with various inputs/outputs
plus it is easier to track"

Not quite clear when you say programs used multiple times. Assuming you *are*
using Net Express - do you want to live dangerously and cut your teeth on OO
:-). I can give you source to show that 4 classes (programs) can handle ISAM,
Relative, Sequential, LineSequential,  each file with a different record
length. E-mail me if interested.

I think my approach is simpler, but for another example of using OO with files,
go to cobolreport.com and check out the OO Examples from  Gene Web. He used Net
Express or its immediate predecessor VISOC. His file example is wrapped in a
tool called Rational Rose, so not knowing the tool it's a little difficult to
follow. But if you check through his code, I think you'll find it is
comprehensive and probably handles all you would want to do with COBOL files.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Getting File Name from a ksh script

- **From:** "Dan" <deacondan25@N.O.S.P.A.M.hotmail.com>
- **Date:** 2003-12-04T09:02:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vsuj4c2dgecnd5@corp.supernews.com>`
- **References:** `<vstl8o6jaibl11@corp.supernews.com> <3FCF1B15.F6821427@shaw.ca>`

```

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3FCF1B15.F6821427@shaw.ca...
>
>
…[4 more quoted lines elided]…
> > In Compaq Cobol I could assign a generic filename then override it in a
ksh
> > script. I MF Cobol it doesn't like that and tries to use the file in the
> > Select/Assign.
…[14 more quoted lines elided]…
> > Is there a way to do the same thing in MF? We have some programs that
are
> > used multiple times with various inputs/outputs plus it is easier to
track
> > the files in the scripts.
> >
…[3 more quoted lines elided]…
> I have no idea what a ksh script file is, plus I'm curious what the
reference
> is to the pgmname.exe in that file. I've been doing the following since
Day One
> using RM/COBOL, Microsoft COBOL and M/F DOS COBOL and Net Express. It must
be
> very close to what you want to do - see if it's adaptable.
>
…[5 more quoted lines elided]…
> The application has a Default file - one record - so uses ws-RelativeKey =
1
>
> 01 Relative-Record.
…[7 more quoted lines elided]…
> Application starts with a Master Menu and reads the Default file to see
what is
> the current Client/Facility setting. Uses Client/Facility with
> CBL_CHECK_FILE_EXISTS. Even just using the old limit of 8 plus 3 for
suffix
> each file in a subset (b) can be identified :-
>
…[15 more quoted lines elided]…
> Data-Filename can be passed to the called program or each called program
could
> read the Default file to establish what it wants.
>
…[3 more quoted lines elided]…
> above opening a fresh set of files and putting the new ID in the Default
File..
>
> 2. User might have finished with current set after two hours. Selects from
Menu
> to change current  ID. (Obviously close existing set). Prompt for new
> Client/Facility ID which is put into the Default record and as above,
…[3 more quoted lines elided]…
> record per user - for ten users, records 1 through 10. Don't do something
daft
> like allocating a 3-digit user ID otherwise you finish up with unnecessary
> empty space in your Relative file.
…[3 more quoted lines elided]…
> "We have some programs that are used multiple times with various
inputs/outputs
> plus it is easier to track"
>
> Not quite clear when you say programs used multiple times. Assuming you
*are*
> using Net Express - do you want to live dangerously and cut your teeth on
OO
> :-). I can give you source to show that 4 classes (programs) can handle
ISAM,
> Relative, Sequential, LineSequential,  each file with a different record
> length. E-mail me if interested.
>
> I think my approach is simpler, but for another example of using OO with
files,
> go to cobolreport.com and check out the OO Examples from  Gene Web. He
used Net
> Express or its immediate predecessor VISOC. His file example is wrapped in
a
> tool called Rational Rose, so not knowing the tool it's a little difficult
to
> follow. But if you check through his code, I think you'll find it is
> comprehensive and probably handles all you would want to do with COBOL
files.
>
> Jimmy, Calgary AB
>

ksh refers to using the Korn shell in Unix. The script is comparable to JCL
in MVS or DCL on a Vax. pgmname.exe is the name of the program I am running.
We append the .exe to make the file readily identifiable as a program. The
format is equivialant to EXEC PGM=PGMNAME in MVS JCL.

We do not run any interactive programs (other than some SAS). These programs
are used in a batch environment. MF Cobol allows you to hard code a file
name in the program, it should also allow you get the file name from the
script/JCL. /this makes it easier to track files as they move through the
system and allows a program to be used multiple times. For example, I have
an invoicing program that has creates standard invoices, but uses different
cover letters depending on what file I am using for the invoice.

The files exist, it's just not getting them from the script. I don't need to
check for existance since the OPEN will error if the file is not found.

Thanks
```

###### ↳ ↳ ↳ Re: Getting File Name from a ksh script

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-12-04T17:16:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FCF6975.F40EC38B@shaw.ca>`
- **References:** `<vstl8o6jaibl11@corp.supernews.com> <3FCF1B15.F6821427@shaw.ca> <vsuj4c2dgecnd5@corp.supernews.com>`

```


Dan wrote:

>
> ksh refers to using the Korn shell in Unix. The script is comparable to JCL
…[11 more quoted lines elided]…
>

BUT, PLEASE, PLEASE don't call it MF COBOL ! "MF" covers a group of compilers,
and at the current time there are three that even use the word 'Express".

Another example of ambiguity. Yours truly, an ex-Brit bumps into a Brit tourist
here in the summer. By accent can sort of place them in south-west, London and
south-east, Midlands, Wales, west coast (Lancashire), east coast (Yorkshire), or
up in bonny Scotland.
.
Conversation goes as follows :-

Q: "Hello. Where are you from ?"
A: "England"
-    (I already knew that !)
Q: 'Which part of England ?"
A: "London".
-    (I knew that too !)
Q: "Which part of London ?".
A: "South"
-  (Oh my gawd !)
Q: 'Where abouts in London ?"
A: "On the Thames"
-   (&%$$@! Again !)
Q: "Where on the Thames ?"
A: "At a place called Walton. Have you heard of it ?".

No question - just my final answer

"Yes I know Walton on Thames. That's where Julie Andrews comes from. And my wife
lived up the road at Sunbury on Thames".

Capice ?

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
