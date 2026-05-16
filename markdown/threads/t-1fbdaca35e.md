[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do you list PDS member names to a dataset?

_12 messages · 7 participants · 1999-08_

---

### How do you list PDS member names to a dataset?

- **From:** hopi517@aol.com (Hopi517)
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990823134249.24653.00002118@ng-ch1.aol.com>`

```
Greetings, everyone!  This is my first time posting to this ng.  I did a Deja
News search for IEHLIST, and this ng popped up, so here goes:

I am maintaining an application which keeps track of mainframe program number
usage.  It is written in Dialog Management Services / CLISTs to search various
Panvalet libraries and write the member names to a sequential dataset.

We are switching to Endevor and will be using PDSs to store our programs. 
Previously, the application used a Panvalet utility to extract the member names
to a sequential dataset.  Now I need a utility to search a PDS.  I have two
options:  use listds (except that I can't figure out how to direct the output
to a file); or run IEHLIST/LISTPDS online to create a file of PDS member names.
 I tried the latter, but IBM's example (13.6.3 in the Utilities manual) of the
control statements aren't very helpful, and my brain is too rusty to figure it
out.

Anyone have any suggestions?
```

#### ↳ Re: How do you list PDS member names to a dataset?

- **From:** mike.newell@sas.com (Mike Newell, WB4HUC)
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37c15129.2759679539@newshost.unx.sas.com>`
- **References:** `<19990823134249.24653.00002118@ng-ch1.aol.com>`

```
On 23 Aug 1999 17:42:49 GMT, hopi517@aol.com (Hopi517) wrote:

>Greetings, everyone!  This is my first time posting to this ng.  I did a Deja
>News search for IEHLIST, and this ng popped up, so here goes:
…[14 more quoted lines elided]…
>Anyone have any suggestions?



I have a COBOL batch program that will read the directory of a PDS and
write the member list and stats (for "source" type datasets) to either a
sequential dataset or to the printer.

The program will allow you to specify a member name or pattern, and will
let you either include or exclude the members that match the pattern.

Let me know if your interested and I can email the source code to you.

Hope this helps,
```

#### ↳ Re: How do you list PDS member names to a dataset?

- **From:** "Gumbo" <gumbo@please.eatme.com>
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7ow3.17898$TM2.262205@viper>`
- **References:** `<19990823134249.24653.00002118@ng-ch1.aol.com>`

```
>options:  use listds (except that I can't figure out how to direct the
output


//LISTDS PGM=IKJEFT01,PARM='LISTDS '''PDS.TO.LIST.MEMBERS''
//SYSEXEC DD DUMMY
//SYSTSIN DD DUMMY
//SYSTSPRT DD DSN=OUTPUT.DSN,DISP=WHATEVER

This will run the output from the listds to the SYSTSPRT DSN. Not sure about
the single quotes around the PARM, experiment. I believe you need 3 in the
middle and 2 at the end.

If you are going to actually search  a PDS for a string, use the =3.14
SUPERC or SUPERCE utility under ISPF. There should be an option to run it in
the background and review the JCL before submitting. Then you can just cut
and paste it into your standard jcl pds as an example.

Also try the above JCL with the LISTCAT command which can give more detail
about the DSN. TSO HELP LISTCAT at the command line should give you adequate
explanation of the options.

//LISTDS PGM=IKJEFT01,PARM='LISTCAT ENTRY('''PDS.TO.LIST.MEMBERS''') ALL'

will list all of the options available.

From the =3.4 option a member list can be saved manually with the SAVE
command.
```

##### ↳ ↳ Re: How do you list PDS member names to a dataset?

- **From:** hopi517@aol.com (Hopi517)
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990824102759.11067.00000038@ng-ch1.aol.com>`
- **References:** `<c7ow3.17898$TM2.262205@viper>`

```
>This will run the output from the listds to the SYSTSPRT DSN.

The problem is, this process has to be run from within a CLIST or Dialog
Management Services, and should be transparent to the user.  I got IEHLIST to
work in batch, but it won't work in a CLIST, as TSO demands a DSN at execution
(I tried DUMMY in the CLIST, but it didn't work).

I'm going to try a series of commands in ISPEXEC that Mike Newell sent me, but
I was hoping for the ever-elusive "quick and dirty" solution of using a
utility, instead of reprogramming the application.

Karen
```

###### ↳ ↳ ↳ Re: How do you list PDS member names to a dataset?

- **From:** "Gumbo" <gumbo@please.eatme.com>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XiGw3.18976$TM2.276683@viper>`
- **References:** `<c7ow3.17898$TM2.262205@viper> <19990824102759.11067.00000038@ng-ch1.aol.com>`

```
>work in batch, but it won't work in a CLIST, as TSO demands a DSN at
execution


not sure what you mean here. What DSN is tso demanding be allocated?

>(I tried DUMMY in the CLIST, but it didn't work).
remember the syntax for DUMMY in ALLOC is:
"ALLOC FI(DDNAME) DUMMY"
```

###### ↳ ↳ ↳ Re: How do you list PDS member names to a dataset?

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990824202154.25874.00002703@ngol01.aol.com>`
- **References:** `<19990824102759.11067.00000038@ng-ch1.aol.com>`

```
In article <19990824102759.11067.00000038@ng-ch1.aol.com>, hopi517@aol.com
(Hopi517) writes:

>I'm going to try a series of commands in ISPEXEC that Mike Newell sent me,
>but
>I was hoping for the ever-elusive "quick and dirty" solution of using a
>utility, instead of reprogramming the application.
>

I thought that I had seen where someone was sending you a COBOL program 
that can read the content of the PDS to provide a listing.
The listing could be output to DASD and a subsequent SORT to extract the
names from the listing in descending order would put the highest assigned
program number at the top of the listing .

Is this sort of what you were looking for?

If you haven't received the program, I can scrounge up the source that I kept
from an earlier round of questions and forward a copy to you.
```

###### ↳ ↳ ↳ Re: How do you list PDS member names to a dataset?

_(reply depth: 4)_

- **From:** theodp@aol.com (Theo DP)
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990824204119.18405.00002662@ng-fj1.aol.com>`
- **References:** `<19990824202154.25874.00002703@ngol01.aol.com>`

```
>Subject: Re: How do you list PDS member names to a dataset?
>From: sff5ky@aol.comxxx123  (Sff5ky)
…[23 more quoted lines elided]…
>

If you've got SAS, here's a one line program: 

PROC SOURCE NOPRINT NODATA INDD='your.pds.dataset.name' DIRDD=outputdd;

More details can be found at
http://ftp.sas.com/techsup/download/technote/ts581.html
```

###### ↳ ↳ ↳ Re: How do you list PDS member names to a dataset?

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C3ECFE.1C641DEC@zip.com.au>`
- **References:** `<c7ow3.17898$TM2.262205@viper> <19990824102759.11067.00000038@ng-ch1.aol.com>`

```
Hopi517 wrote:
> 
> >This will run the output from the listds to the SYSTSPRT DSN.
…[11 more quoted lines elided]…
> Karen

Look up library management services (prefixed lm in the ISPF services
manual).  This allows you to open a PDS member list and read then
sequentially.

Ken
```

###### ↳ ↳ ↳ Re: How do you list PDS member names to a dataset?

_(reply depth: 4)_

- **From:** Jared Thomas <jared@techie.com>
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C48628.D73EDBB0@techie.com>`
- **References:** `<c7ow3.17898$TM2.262205@viper> <19990824102759.11067.00000038@ng-ch1.aol.com> <37C3ECFE.1C641DEC@zip.com.au>`

```
You will find the members one per line in the output data set
starting with the 5th? line.  If you want the names in a clist,
then in place of the EXECIO (and ALLOC and FREE) do something like
this (and watch the quotes on pds):

  for i = 5 to ot.0
    member = strip(ot.i)
    address TSO "COPY "pds"("member) NEW.DATA.SET("member") NONUM"
    end i

PS:  I did some hand editing afer cut+paste from a working EXEC. 
Your milage may vary.

/*REXX */
  arg pds out_dsn command
  if command = '' then command = "LISTDS "pds" MEM"

  address TSO "ALLOC DDN(ddn) DSN("out_dsn") SPACE(5,30) TRACKS",
      "LRECL(255) BLKSIZE(11440) RECFM(V B) REUSE"
  if rc <> 0 then do
    say "Could not allocate output data set "out_dsn", I quit"
    exit 32
    end

  /* Can't allow prompting as the user does not see anything at
the terminal.  */
  prompt = prompt('OFF')

  /* Start collecting output. */
  outtrap = outtrap('OT.')

  /*  Now the command. */
  trace = trace('Off')
  signal on halt
  address TSO command
halt:
  trace value trace
  signal off halt
  rc_tso = rc

  /* stop collecting output */
  outtrap = outtrap(off)

  /* Save the output in the data set. */
  'EXECIO 'ot.0' DISKW ddn ( FINIS STEM OT.'
  rc_execio_ rc
  if rc_execio <> 0 then say 'EXECIO rc='rc' saving output in
'out_dsn
  'FREE DDN(ddn)'
  exit max(rc_tso, rc_execio)
```

###### ↳ ↳ ↳ Re: How do you list PDS member names to a dataset?

_(reply depth: 5)_

- **From:** "Gumbo" <gumbo@please.eatme.com>
- **Date:** 1999-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2ADx3.256$mo.16141@viper>`
- **References:** `<c7ow3.17898$TM2.262205@viper> <19990824102759.11067.00000038@ng-ch1.aol.com> <37C3ECFE.1C641DEC@zip.com.au> <37C48628.D73EDBB0@techie.com>`

```
Or :

/* REXX */
ARG PDS_IN PDS_OUT

"ALLOC FI(OUTPDS) DA('"PDS_OUT"') NEW CATALOG",
    "LIKE('"PDS_IN"') RELEASE"
"FREE FI(OUTPDS)"

X=OUTTRAP(MEM.L.)
"LISTDS '"PDS_IN"' MEMBERS"
X=OUTTRAP(OFF)

DO A=5 TO MEM.L.0

    CURR_MEM=STRIP(MEM.L.A)
    "REPRO IDS('"PDS_IN"("CURR_MEM")') ODS("PDS_OUT"("CURR_MEM")')
NOREPLACE"
    /* NO NEED TO CHECK RC, REPRO WILL DISPLAY ERROR MESSAGES TO SYSOUT */

END
RETURN
```

#### ↳ Re: How do you list PDS member names to a dataset?

- **From:** "Gumbo" <gumbo@please.eatme.com>
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N9ow3.17899$TM2.263501@viper>`
- **References:** `<19990823134249.24653.00002118@ng-ch1.aol.com>`

```
>We are switching to Endevor and will be using PDSs to store our programs.
If there is such a thing, check the ENDEVOR MANUAL to see if there is a
report which can be generated a PDS MEMBER usage report.

Not sure what you mean by "NUMBER USAGE"???
```

##### ↳ ↳ Re: How do you list PDS member names to a dataset?

- **From:** hopi517@aol.com (Hopi517)
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990824103127.11067.00000046@ng-ch1.aol.com>`
- **References:** `<N9ow3.17899$TM2.263501@viper>`

```
>Not sure what you mean by "NUMBER USAGE"???

Which numbers have been assigned as identifiers to programs already.  The
application maintains a master list of all program numbers that have been
assigned.  When a programmer has to write a new program, he/she uses this
application to determine the next available program number.

Karen
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
