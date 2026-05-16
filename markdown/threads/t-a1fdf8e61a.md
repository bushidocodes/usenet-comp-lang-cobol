[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobfattr in Power Cobol

_12 messages · 5 participants · 2003-05_

---

### Cobfattr in Power Cobol

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-05-20T12:02:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2900664.1053432122@dbforums.com>`

```

Hi, If you  in DOS prompt

type Cobfattr  nameoffile > trash

you get all information about this file, but
if you  do this inside a PowerCobol Program
doesnt work .

Anybody he Knows why ?

by the way any other command works


 WORKING-STORAGE SECTION.
 01 Command-Line        PIC X(128).
 01 ReturnValue PIC S9(9) COMP-5.
 PROCEDURE       DIVISION.
     MOVE "Cobfattr nomeoffile > trash"   TO Command-Line
     INVOKE CmDDE1 "Execute"
       USING     Command-Line
                 POW-SWSHOWNORMAL
       RETURNING ReturnValue


C. Lages
```

#### ↳ Re: Cobfattr in Power Cobol

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-05-20T16:05:39+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jl9kcvkjq0h0k8c0dm67k3b0t9k3c1fctt@4ax.com>`
- **References:** `<2900664.1053432122@dbforums.com>`

```
On Tue, 20 May 2003 12:02:02 +0000 Carlos lages <member129@dbforums.com>
wrote:

:>Hi, If you  in DOS prompt

:>type Cobfattr  nameoffile > trash

:>you get all information about this file, but
:>if you  do this inside a PowerCobol Program
:>doesnt work .

:>Anybody he Knows why ?

:>by the way any other command works

:> WORKING-STORAGE SECTION.
:> 01 Command-Line        PIC X(128).
:> 01 ReturnValue PIC S9(9) COMP-5.
:> PROCEDURE       DIVISION.
:>     MOVE "Cobfattr nomeoffile > trash"   TO Command-Line
:>     INVOKE CmDDE1 "Execute"
:>       USING     Command-Line
:>                 POW-SWSHOWNORMAL
:>       RETURNING ReturnValue

That is because COMMAND.COM does the redirection to support this.

As you are not invoking COMMAND.COM to process it, you must do the redirection
yourself, i.e., redirecting standard output to TRASH. 

Unfortunately I have misplaced my DOS BIBLE, but I am sure that there are
sites with the information on how to do the DOS call.

If you wish to be sloppy, you can invoke a batch file which does it.
```

##### ↳ ↳ Re: Cobfattr in Power Cobol

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-05-20T18:54:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2902677.1053456863@dbforums.com>`
- **References:** `<2900664.1053432122@dbforums.com> <jl9kcvkjq0h0k8c0dm67k3b0t9k3c1fctt@4ax.com>`

```

Even I use with no redirection , doesnt work too.

C. Lages
```

##### ↳ ↳ Re: Cobfattr in Power Cobol

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-05-21T07:57:00+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bae1a1$lbk$1@aklobs.kc.net.nz>`
- **References:** `<2900664.1053432122@dbforums.com> <jl9kcvkjq0h0k8c0dm67k3b0t9k3c1fctt@4ax.com>`

```
Binyamin Dissen wrote:

> On Tue, 20 May 2003 12:02:02 +0000 Carlos lages <member129@dbforums.com>
> wrote:
> 
> :>Hi, If you  in DOS prompt

> :>     MOVE "Cobfattr nomeoffile > trash"   TO Command-Line
> :>     INVOKE CmDDE1 "Execute"
…[10 more quoted lines elided]…
> sites with the information on how to do the DOS call.

Possibly:

     MOVE "COMMAND.COM /C cobfattr nameofile >trash" & x"0A" TO Command-Line
```

###### ↳ ↳ ↳ Re: Cobfattr in Power Cobol

- **From:** pvieira@emporsoft.pt (Paulo Vieira)
- **Date:** 2003-05-21T04:24:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b8d7c7.0305210324.4a27cd6f@posting.google.com>`
- **References:** `<2900664.1053432122@dbforums.com> <jl9kcvkjq0h0k8c0dm67k3b0t9k3c1fctt@4ax.com> <bae1a1$lbk$1@aklobs.kc.net.nz>`

```
Hi,
Are you sure COMMAND.COM is DDE enabled ? Why not use POW-SELF instead of CmDDE1?
Paulo Vieira, Emporsoft

Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<bae1a1$lbk$1@aklobs.kc.net.nz>...
> Binyamin Dissen wrote:
> 
…[21 more quoted lines elided]…
>      MOVE "COMMAND.COM /C cobfattr nameofile >trash" & x"0A" TO Command-Line
```

###### ↳ ↳ ↳ Re: Cobfattr in Power Cobol

_(reply depth: 4)_

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-05-22T14:49:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2911281.1053614966@dbforums.com>`
- **References:** `<2900664.1053432122@dbforums.com> <jl9kcvkjq0h0k8c0dm67k3b0t9k3c1fctt@4ax.com> <bae1a1$lbk$1@aklobs.kc.net.nz> <b5b8d7c7.0305210324.4a27cd6f@posting.google.com>`

```

Paulo, using Pow-self  instead of POW-DDE  doesnt Work too
in other words , It runs, but no answer is given.

I thing there are some tricks  to not  run in  Power only in
DOS Prompt.

indeed i  want  to Get  Number of record of a File

Carlos  Lages

By the way  Fujitusu Should release a routine to give us
this information,

Carlos Lages
```

###### ↳ ↳ ↳ Re: Cobfattr in Power Cobol

_(reply depth: 5)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-05-22T16:39:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<awSdneOKLd8e3lCjXTWJkA@giganews.com>`
- **References:** `<2900664.1053432122@dbforums.com> <jl9kcvkjq0h0k8c0dm67k3b0t9k3c1fctt@4ax.com> <bae1a1$lbk$1@aklobs.kc.net.nz> <b5b8d7c7.0305210324.4a27cd6f@posting.google.com> <2911281.1053614966@dbforums.com>`

```

"Carlos lages" <member129@dbforums.com> wrote in message
news:2911281.1053614966@dbforums.com...
>
> Paulo, using Pow-self  instead of POW-DDE  doesnt Work too
…[11 more quoted lines elided]…
>

You could write your own. Try something like this:

    SELECT MYFILE ASSIGN TO IDISAM
        ORGANIZATION IS SEQUENTIAL
        FILE STATUS IS MYFILE-FS.

FD  MYFILE.
01  MYREC.
   02  FILLER        PIC X(50).
  02  NUMREC-1  PIC S9(9) COMP-4.
  02  FILLER        PIC X(2).
  02  NUMREC-2  PIC 9(9) COMP-4.

LINKAGE SECTION.
01  FILE-REC-1            PIC S9(9) COMP-4.

PROCEDURE DIVISION USING FILE-REC-1.

OPEN INPUT MYFILE.
READ MYFILE.
CLOSE MYFILE.
IF MYFILE-FS NOT = '00'
    MOVE 0 TO NUMREC-1.
MOVE NUMREC-1 TO FILE-REC-1
GOBACK.

It looks like, from scanning the file header, Fujitsu has three locations
for number of records (these two at bytes 51 and 57 and another starting at
byte 267).

It may take some experimenting to discover which is the real one (or they
may be redundant).
```

###### ↳ ↳ ↳ Re: Cobfattr in Power Cobol

_(reply depth: 6)_

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-05-22T23:32:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2913486.1053646342@dbforums.com>`
- **References:** `<2900664.1053432122@dbforums.com> <jl9kcvkjq0h0k8c0dm67k3b0t9k3c1fctt@4ax.com> <bae1a1$lbk$1@aklobs.kc.net.nz> <b5b8d7c7.0305210324.4a27cd6f@posting.google.com> <2911281.1053614966@dbforums.com> <awSdneOKLd8e3lCjXTWJkA@giganews.com>`

```

oK, TKS, I WILL DO IT

but  i dont have Fujitsu header files layout,
if I had ,i will do my own routine in "C"

by the way do you have this layouts, or where can i get one ?

Carlos Lages
```

###### ↳ ↳ ↳ Re: Cobfattr in Power Cobol

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-05-22T22:22:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cAGdnXqH2aJ0DlCjXTWJkA@giganews.com>`
- **References:** `<2900664.1053432122@dbforums.com> <jl9kcvkjq0h0k8c0dm67k3b0t9k3c1fctt@4ax.com> <bae1a1$lbk$1@aklobs.kc.net.nz> <b5b8d7c7.0305210324.4a27cd6f@posting.google.com> <2911281.1053614966@dbforums.com> <awSdneOKLd8e3lCjXTWJkA@giganews.com> <2913486.1053646342@dbforums.com>`

```

"Carlos lages" <member129@dbforums.com> wrote in message
news:2913486.1053646342@dbforums.com...
>
> oK, TKS, I WILL DO IT
…[6 more quoted lines elided]…
> Carlos Lages

I don't have the header layouts. I wrote 2001 records and looked at the
start of the file for 00 00 07 D1.

Why would you do the routine in C and introduce linkage confusion?
```

###### ↳ ↳ ↳ Re: Cobfattr in Power Cobol

_(reply depth: 8)_

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-05-23T12:05:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2915058.1053691513@dbforums.com>`
- **References:** `<2900664.1053432122@dbforums.com> <jl9kcvkjq0h0k8c0dm67k3b0t9k3c1fctt@4ax.com> <bae1a1$lbk$1@aklobs.kc.net.nz> <b5b8d7c7.0305210324.4a27cd6f@posting.google.com> <2911281.1053614966@dbforums.com> <awSdneOKLd8e3lCjXTWJkA@giganews.com> <2913486.1053646342@dbforums.com> <cAGdnXqH2aJ0DlCjXTWJkA@giganews.com>`

```

I think will be easier,.

Imagine this scenario

A Power Cobol Forms running using 10 Files
and I need to Know # of records from  one of them
or evem more than one

Using in Power cobol , I have to declare all the files
twice ( once Indexed other sequential)
Open the File twice, etc

because i can only access a file if  its declared (File section, etc)

Using in "C"  I dont need  nothing of this

in Power cobol I do a CALL  passing nameoffile
returning Number Of records.

Like basic , I need only  name of a file

Ok, ok, OK  I could do this in Power too, but hard work

Carlos Lages
```

###### ↳ ↳ ↳ Re: Cobfattr in Power Cobol

_(reply depth: 9)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-05-23T17:59:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Joucne1ztsxzOlOjXTWcoA@giganews.com>`
- **References:** `<2900664.1053432122@dbforums.com> <jl9kcvkjq0h0k8c0dm67k3b0t9k3c1fctt@4ax.com> <bae1a1$lbk$1@aklobs.kc.net.nz> <b5b8d7c7.0305210324.4a27cd6f@posting.google.com> <2911281.1053614966@dbforums.com> <awSdneOKLd8e3lCjXTWJkA@giganews.com> <2913486.1053646342@dbforums.com> <cAGdnXqH2aJ0DlCjXTWJkA@giganews.com> <2915058.1053691513@dbforums.com>`

```

"Carlos lages" <member129@dbforums.com> wrote in message
news:2915058.1053691513@dbforums.com...
>
> I think will be easier,.
…[20 more quoted lines elided]…
> Ok, ok, OK  I could do this in Power too, but hard work

No, it's a single subroutine compiled outside of PowerCobol. We have
HUNDREDS of special-purpose subprograms: Utilities (left-justify), IO (all
our file IO are in a subroutines), Conversion (Text-to-CSV), Date validation
and editing, etc. Hundreds.

You'll only need one more parameter: the name of the file.
```

###### ↳ ↳ ↳ Re: Cobfattr in Power Cobol

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-05-23T17:38:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bakc64$c1a$1@aklobs.kc.net.nz>`
- **References:** `<2900664.1053432122@dbforums.com> <b5b8d7c7.0305210324.4a27cd6f@posting.google.com> <2911281.1053614966@dbforums.com> <awSdneOKLd8e3lCjXTWJkA@giganews.com>`

```
JerryMouse wrote:

> You could write your own. Try something like this:
> 
…[20 more quoted lines elided]…
>     MOVE 0 TO NUMREC-1.

You are check the file status result from the CLOSE, I suspect that you 
should be checking after the READ.

> MOVE NUMREC-1 TO FILE-REC-1

You are accessing the record area after the file has been closed.  This is 
OK with some systems, such as MF.  It is not guaranteed that such action 
will work.  You should be doing the CLOSE later.

> It looks like, from scanning the file header, Fujitsu has three locations
> for number of records (these two at bytes 51 and 57 and another starting
…[3 more quoted lines elided]…
> may be redundant).

It is possible that one is the number of records including deleted records.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
