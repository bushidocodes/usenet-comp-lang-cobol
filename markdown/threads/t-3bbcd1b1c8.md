[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# TSO ISPF, CLISTs and/or REXX exec

_26 messages · 16 participants · 1998-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### TSO ISPF, CLISTs and/or REXX exec

- **From:** "bob berman" <ua-author-6589116@usenetarchives.gap>
- **Date:** 1998-08-19T20:42:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35DB9C35.4B24@netbox.com>`

```
If this is not the proper newsgroup to direct this question, and you can
direct me elsewhere, please do.


Everywhere I have worked in the past has had a CLIST or REXX exec that
could be invoked from an ISPF Edit or View session that would open
another ISPF View or Edit panel - for example, if I was editing or
viewing a JCL stream or proc in a CNTL data set, I could type
DSNVER^B or DSNVER^E, put the cursor on the data set name in the proc,
hit enter and the data set would be opened for view or edit. At
another installation it was called PDFDSN^B or E.

At my current assignment, they don't seem to have this, but I have
found something similar, and I'm hoping that someone can help me
modify it, as I have not written a CLIST in 20 years, and don't know
REXX at all. Here it is:

on command line, type TSO ISPLOOK 'dsn' -
(I don't understand why the TSO is required but it is. The 'dsn'
is a positional parameter.)

I have found the code behind it in a PDS called APPLP.WRK.CLIST which
is allocated to a user's TSO session: (there is a similar clist called
ISPEDIT also)

PROC: 1 DSN DEBUG WRITE
IF &DEBUG EQ DEBUG THEN CONTROL LIST CONLIST SYSLIST MSG PROMPT
ELSE CONTROL NOLIST NOCONLIST NOSYMLIST NOMSG

ISPEXEC CONTROL ERRORS RETURN
ISPEXEC BROWSE DATASET(&DSN)

SET RTCODE = &LASTCC

IF &RTCODE LE 4 THEN DO
SET ZERRSM = &STR(ISPLOOK SUCCESSFUL)
SET ZERRLM = &STR(ISPLOOK CLIST SUCCESSFULLY COMPLETED, RC = &RTCODE)
SET ZERRALRM = &STR(NO)
SET ZERRHM = &STR(ISR00003)
END
ELSE +
IF &WRITE EQ WRITE THEN +
WRITE * ERROR * &ZERRLM

ISPEXEC SETMSG MSG(ISRZ002)

EXIT CODE(&RTCODE)

end of code.

My hope is to be able to run without typing in 'TSO', just ISPLOOK,
position the cursor on the dataset name, and hit enter.

I can follow basically what this does, but I don't know how to modify
it. I imagine that you can determine the cursor position, back off to
the equal sign + 1 for starting position, and advance to the ending
postion which would be a comma or space - 1, and string that as the
data set name. I wish I had reference manuals available, but they
seem to be a thing of the past, and again my CLIST experience was
from before ISPF.

Thanks in advance for any help -
Bob Berman

<----------------------------------------------------------------------> 
                 Bob Berman   -    West Hartford, CT                  
  mailto:bbe··.@net··x.com    homepage: http://www.ntplx.net/~bberman  
                                                                        
                 THE TRUE TERRORISTS IN AMERICA ARE                     
          THE PEOPLE WHO DEMAND TO SEE THE STORE MANAGER !              
<----+----+----+----+----+----+----+----+----+----+----+----+----+----+>
```

#### ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "ken baker" <ua-author-2142384@usenetarchives.gap>
- **Date:** 1998-08-18T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35DB9C35.4B24@netbox.com>`
- **References:** `<35DB9C35.4B24@netbox.com>`

```
Hey Bob,

Unfortunately, there's only one way to get around having to type in the
"TSO" before the CLIST name. That's if you type the CLIST name at the
"READY" prompt. (Of course if you're in an ISPF edit session, that doesn't
do you any good.) My understanding is that to execute any CLIST or REXX
exec, it MUST be preceded by the "TSO" We have a similar procedure at the
installation I work at, but unfortunately, I don't know the code behind it.
Or even if it's a REXX exec, or a CLIST.

Not much help I know, but thought I'd pass on what little info I do have.

Ken Baker

Ken··.@ya··o.com


›
› My hope is to be able to run without typing in 'TSO', just ISPLOOK,
› position the cursor on the dataset name, and hit enter.
›
```

##### ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "cit..." <ua-author-2934993@usenetarchives.gap>
- **Date:** 1998-08-18T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p2@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p2@usenetarchives.gap>`

```
In <6rg7ja$eb$1.··.@new··e.net>, "Ken Baker" writes:
› Hey Bob,
› 
…[9 more quoted lines elided]…
› 

You need to put the commands in a command table. Use the command table
utility found on option 3.x from the primary option menu. Read up on
this, command tables can be kind of tricky if you're not familiar with
how they work. Then concatenate your command table to ISPTLIB using a
clist(logon) or if you have high enough security you could probably
get it in one of your system command tables. Then you can just type
the string and it will look up the command in the table and execute
it.
```

##### ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "jeff" <ua-author-11765@usenetarchives.gap>
- **Date:** 1998-08-20T00:27:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p2@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p2@usenetarchives.gap>`

```
› Unfortunately, there's only one way to get around having to type in the
› "TSO" before the CLIST name. That's if you type the CLIST name at the
› "READY" prompt. (Of course if you're in an ISPF edit session, that doesn't


Not true. I know there is a way, rather complicated from what I hear, but I
have seen it done.
It has something to do with the ISPF command tables.
```

###### ↳ ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-08-19T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p4@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p2@usenetarchives.gap> <gap-3bbcd1b1c8-p4@usenetarchives.gap>`

```
Jeff wrote:
› 
›› Unfortunately, there's only one way to get around having to type in the
…[5 more quoted lines elided]…
› It has something to do with the ISPF command tables.

Yes, it is possible to configure things such that you don't have to
precede your command (REXX or Clist name) with "TSO", but when I asked
about it several years ago I was told that it was a complex and clunky
process (tables need to be updated globally, etc.). Sorry, but I don't
know the internals required to explain it better.

BTW, we do have similar local commands available to edit browse a
dataset without the "TSO" prefix (EDSN & BDSN). I use them all the time,
very handy.

Bill Lynch
```

###### ↳ ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "wayne l. beavers" <ua-author-7682107@usenetarchives.gap>
- **Date:** 1998-08-19T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p4@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p2@usenetarchives.gap> <gap-3bbcd1b1c8-p4@usenetarchives.gap>`

```
Jeff wrote:
› 
›› Unfortunately, there's only one way to get around having to type in the
…[5 more quoted lines elided]…
› It has something to do with the ISPF command tables.

There is a way to add it to the ISPF command tables, but I don't recall
what it is.

When you want to determine what library a clist or tso command is in try
running

TSO ISRFIND
or
TSO ISRDDN

These are essentially commands to do a TSO LISTALC ST and then present a
scrollable table so that you can edit and browse allocated files. Very
handy to determine where a panel or program is installed.

Wayne L. Beavers         mailto:Way··.@Bey··e.com
Beyond Software, Inc.      http://www.beyond-software.com
"Transforming Legacy Applications"
```

#### ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-08-19T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p7@usenetarchives.gap>`
- **In-Reply-To:** `<35DB9C35.4B24@netbox.com>`
- **References:** `<35DB9C35.4B24@netbox.com>`

```
Bob,

In stead of using the ISPF command table, which is indeed a rather
complicated process, you could write a CLIST or Rexx exec that is designed
as an EDIT MACRO. (A Rexx exec is sometimes called "Rexec". I'll do so too).

Read on.

Bob Berman wrote:

› If this is not the proper newsgroup to direct this question, and you can
› direct me elsewhere, please do.

Try comp.lang.rexx. I found no newsgroup about CLIST in my news server, but
enayway IBM stated Rex to be the successor of CLIST, being the
cross-platform macro language from OS/2 trhu VM / MVS, even on AS/400 (?).

› Everywhere I have worked in the past has had a CLIST or REXX exec that
› could be invoked from an ISPF Edit or View session that would open
› another ISPF View or Edit panel

ISPF (or PDF) has this built in the editor. Just use the command EDIT (being
*in* edit already). Without a dataset name as an argument you get an entry
panel to specify the dataset(member). With argument this either is a
membername in the current dataset or an other datasetname. Anyway then you
get a nested edit session on the specified datasource.

› - for example, if I was editing or
› viewing a JCL stream or proc in a CNTL data set, I could type
› DSNVER^B or DSNVER^E, put the cursor on the data set name in the proc,
› hit enter and the data set would be opened for view or edit.  At
› another installation it was called PDFDSN^B or E.

Whatever the command (DSNVER/PDFDSN), this is almost sure a locally
developed in CLIST/Rexx. AAIK no standard feature in ISPF/PDF. To "read" the
dataset name "under" the cursor needs a special type of CLIST or Rexec.
First I would tell that normal CLISTs and Rexecs, like the one you show
later-on, are started througout PDF with the TSO command. The TSO command
needs at least one argument, the name of the CLIST/Rexec to execute. Other
arguments are passed thru (handed over to) the invoked CLIST/Rexec. To read
"under" the cursor I will talk later about.

› At my current assignment, they don't seem to have this, but I have
› found something similar, and I'm hoping that someone can help me
…[5 more quoted lines elided]…
›   is a positional parameter.)

I already explained this. ISPLOOK is just the choosen name, as nice as
DSNVER of PDFDSN or whatever.

› I have found the code behind it in a PDS called APPLP.WRK.CLIST which
› is allocated to a user's TSO session: (there is a similar clist called
› ISPEDIT also)

What do you mean with "similar"? Is ISPEDIT equal or nearly equal? This has
to do with getting the datasetname "under" the cursor. That requires some
extra coding, thus enhancing its functionality (it is handier) but it limits
the places where you can use of the CLIST/Rexec to the ISP editor i.e. it is
then usable only from within the ISPF editor.

› PROC: 1 DSN DEBUG WRITE
 
› 8< code snip
 
› ISPEXEC BROWSE DATASET(&DSN)

I guess that ISPEDIT hasISPEXEC EDIT DATASET(&DSN)
here?!

› SET RTCODE = &LASTCC
 
› 8< code snip
 
› end of code.

To make ISPLOOK or ISPEDIT aware of the text that is "under" the cursor, it
should be an EDIT MACRO. I am aware of the fact that there are possibilities
(using assembler I guess :)) to read data from an ISPF-formatted screen an
any CLIST/Rexec, but I don't know. The way I know is to use the MACRO
facilities of the ISPF editor. That limits the use of the CLIST to using it
within edit alone.

› My hope is to be able to run without typing in 'TSO', just ISPLOOK,
› position the cursor on the dataset name, and hit enter.

That's exactly what happens when a CLIST/Rexec is written as an EDIT MACRO:
you can type the CLIST/Rexec's name as if it were an ordinary built-in edit
command. No need to type the prefix TSO, moreover that would run the
CLIST/Rexec as a normal one, not as an EDIT MACRO so no macro facilities are
available.

› I can follow basically what this does, but I don't know how to modify
› it.  I imagine that you can determine the cursor position, back off to
› the equal sign + 1 for starting position, and advance to the ending
› postion which would be a comma or space - 1, and string that as the
› data set name.

Once you got in a string the contents (text) of the record in the currently
edited dataset. To realize that first (getting it), use the maco facility.
But beside that, first the CLIST(or Rexec) needs to claim itself as a
macro:ISREDIT MACRO
and than to get the line at which the cursor (row) points
ISREDIT getline at .ZCSR
than get the cursor column
ISREDIT put cursor r/c in CLIST vars
and than parse its contents from the data middle out from the col position
etc.

I do not remember the exact ISREDIT commands for all these, but they exist
and you can find all info in the manuals of ISPF/PFD (Take the edit manual,
the macro chapter I would try). I once even wrote COBOL and PL/1 programs to
run within and using ISPF services and as MACRO. All this years ago, so
syntaxis is gone, semantics I remember.

› I wish I had reference manuals available, but they
› seem to be a thing of the past, and again my CLIST experience was
› from before ISPF.

Oops. IBM has them probably online in the web. Try
urlhttp://ppdbooks.pok.ibm.com:80/cgi-bin/bookmgr/bookmgr.cmd/BOOKS/ISPEDT01/CCONTENTS

Sometimes it is wise to start at
http://ppdbooks.pok.ibm.com:80/cgi-bin/bookmgr/bookmgr.cmd/

Good luck Bob

› Thanks in advance for any help -
› Bob Berman

y. welcome
The COBOL Frog
```

#### ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "jeff" <ua-author-11765@usenetarchives.gap>
- **Date:** 1998-08-19T22:28:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p8@usenetarchives.gap>`
- **In-Reply-To:** `<35DB9C35.4B24@netbox.com>`
- **References:** `<35DB9C35.4B24@netbox.com>`

```
› Everywhere I have worked in the past has had a CLIST or REXX exec that
› could be invoked from an ISPF Edit or View session that would open
› another ISPF View or Edit panel - for example, if I was editing or
 
 
› try csred, csrbr, edd, brd, ed or br.
 
› My hope is to be able to run without typing in 'TSO', just ISPLOOK,
› position the cursor on the dataset name, and hit enter.
What you are talking about is an ISPF EDIT MACRO. To know where to put it
you need to do a few things. First, when in EDIT type TSO LISTALC STATUS on
the command line. This should spew out a bunch of dataset names, all should
be PDS's. These paths telll ISPF where to look for commands you type on the
command line. The important ones are SYSPROC and SYSEXEC. What is displayed
is a PDS name and then on the next line is the DDNAME associated with that
PDS. There will be a blank line to indicate a concatenated DSN list. You can
look in the PDS's associated with SYSPROC and SYSEXEC. These contain the
clists in SYSPROC and Rexx Execs in SYSEXEC. Try running a SUPERC search on
these PDS's looking for 'ISREDIT' and 'CURSOR'. If the clist/exec contains
these, chances are it is your cusor edit or cursor browse routines you are
looking for. If these work you can use those commands from the command line,
or better yet assign the command to a function key, move cursor to the line
with the DSN you want to browse, and simply hit the function key you
assigned the command to.

If you can't find the commands you need, you will have to create one. Before
that, you need to find out what PDS you need to put your macro in. In the
many places I have been this has always been done in a similar manner. A
Rexx Exec or Clist is executed as your logon process. You can find it by
going to your JES screen, where you watch your running batch jobs after
being submitted. You need to look at the job which is always running with
the jobname of your logon id. If you look at the JCL being executed it
should have an EXEC PGM=IKJEFT01 or EXEC PGM=IRXJCL. This is the exec which
does the dynamic allocations used to run ISPF and the customized
applications running under it. Somewhere in that Exec/Clist there will be an
allocation to DDNAME SYSEXEC or SYSPROC. There should be a conditional
allocation which checks for a PDS and if that PDS exists it will add it to
the concatenated DSN list for DDNAME SYSEXEC or SYSPROC. This is the PDS you
need to create and place your cursor edit and cursor browse in.

Some of the default EXEC/CLIST pds's I have encountered were:
USERID.PREXX.EXEC
USERID.CLIST
USERID.COMMAND
USERID.SYSPROC.CLIST

If this doesn't exist, or you can't find it there is one final solution I
have had to use. You have to set up the allocations yourself every time you
logon. This is done by creating a CLIST/EXEC to be executed every time you
log on by typig the following command:"TSO EXEC SETUP". This will execute a
clist called USERID.SETUP.CLIST by default. This will perform the
allocations necessary to run CLISTS or Rexx EXECS. You need to create a flat
file called USERID.SETUP.CLIST, no member name, just a plain old flat file.
Where USERID is your prefix/userid. Edit the USERID.SETUP.CLIST file and
place the following commands in it:
/* REXX */
"ALLOC FI(SYSEXEC) DA('USERID.REXX.SOURCE') SHR REUSE"
"ALTLIB ACTIVATE SYSTEM(EXEC)"

The above ALTLIB command activates the SYSTEM EXEC default DDNAME, SYSEXEC.
This means TSO/ISPF will look in this DDNAME for the commands executed by
the TSO command or from the command line in ISPF EDIT. Allowing you to
execute commands in ISPF EDIT directly from the command line. These commands
are ISPF EDIT MACROS written as either a CLIST or a REXX EXEC.

The SYSTEM option is the best way to get to EXEC's. If you are not allowed
to allocate the SYSEXEC DDNAME you will have to try to allocate the SYSUEXEC
DDNAME to your person REXX library:
/* REXX */
"ALLOC FI(SYSUEXEC) DA('USERID.REXX.SOURCE') SHR REUSE"
"ALTLIB ACTIVATE USER(EXEC)"

If this still does not work there is one last way which nearly always works:
/* REXX */
"ALLOC FI(MYEXEC) DA('USERID.REXX.SOURCE') SHR REUSE"
"ALTLIB ACTIVATE APPLICATION(EXEC) DDNAME(MYEXEC)"

If none of these works you are SOL. Be warned that the SYSTEM option should
be available from all command lines, where TSO COMMAND is necessary from all
command lines save the ISPF EDIT command line. Where COMMAND is the
EXEC/CLIST in your USERID.REXX.SOURCE pds. Strange things happen when you
use the USER and APPLICATION EXEC options. These are not acivated from all
screens.

One more note (yes I am running at the mouth a bit) you can execute a
default clist at logon if you use a standard TSO/ISPF logon screen. This is
done by placing the following command on the "COMMAND" line on the screen:
EXEC SETUP
It should be the very bottom option you can place information on. If that
doesn't work try one of the following commands:
EXEC SETUP.CLIST
EXEC 'USERID.SETUP.CLIST'
EXEC 'USERID.SETUP.CLIST' EXEC

Sometimes this command is executed before your ISPF session starts and
sometimes after. If before, OK, if after you are out of luck and you will
have to do it manually everytime you log on. To test this place the
following command in your USERID.SETUP.CLIST:
SAY 'EXECUTING SETUP ROUTINE'
When you see the EXECUTING SETUP ROUTINE statement come up on the screen,
this will tell you when the SETUP routine is executed.

I am sure this long winded explanation will raise many questions, but feel
free to post them.

This is just my opinion, I may be wrong.
```

#### ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "bob berman" <ua-author-6589116@usenetarchives.gap>
- **Date:** 1998-08-20T19:15:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p9@usenetarchives.gap>`
- **In-Reply-To:** `<35DB9C35.4B24@netbox.com>`
- **References:** `<35DB9C35.4B24@netbox.com>`

```
Thanks everyone for your input. Pointing me toward the possible PDS's
where it could be located was a great help. As it turns out, at this
installation it is called ZOOM (with the b or e option). Everyone still
there after the layoffs of the early 90's had forgotten it. I modified
it to add a 'v' option (View), and it works fine.

Again, many thanks -
Bob
<----------------------------------------------------------------------> 
                 Bob Berman   -    West Hartford, CT                  
  mailto:bbe··.@net··x.com    homepage: http://www.ntplx.net/~bberman  
                                                                        
                 THE TRUE TERRORISTS IN AMERICA ARE                     
          THE PEOPLE WHO DEMAND TO SEE THE STORE MANAGER !              
<----+----+----+----+----+----+----+----+----+----+----+----+----+----+>
```

##### ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-08-21T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p9@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p9@usenetarchives.gap>`

```
Bob Berman wrote:
› 
› Thanks everyone for your input.  Pointing me toward the possible PDS's
…[3 more quoted lines elided]…
› it to add a 'v' option (View), and it works fine.

Well, now that Mr Berman has found this happy conclusion permit me to
say... just proves me right again! (modest, ain't I?)

Y'see, in going from one shop to the next I've made it a practise never
to familiarise myself, or grow dependent on, CLISTs or REXs or other
macro-like extensions, no matter *how* common they seem... yea, verily,
even unto the old CUT and PASTE macros in ISPF edit.

Why? Because I never know what the next shop will have... so I rely on
the most basic set of commands (CUT? nope, create membrnam... PASTE?
nope, move membrnam... in Mr Berman's example, ZOOM b/e/s/p/q/r?...
nope, split the screen and type... or invoke a new edit/browse from the
command line)

Think I'm nuts? (well, you're right!... but for all the wrong reasons,
of course!) Just remember that within the past two years I put in a
contract in a shop so backwards that it not only was devoid of macros
but it had no FileAid... and no AbendAid.

They're out there... be prepared... Keep Watching The Skies!

DD

(oh, by the bye... is this Bob Berman the Bob Berman of ESCAPE-sequence
fame?)
```

###### ↳ ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "bob berman" <ua-author-6589116@usenetarchives.gap>
- **Date:** 1998-08-22T12:55:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p10@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p9@usenetarchives.gap> <gap-3bbcd1b1c8-p10@usenetarchives.gap>`

```
The Goobers wrote:
› Well, now that Mr Berman has found this happy conclusion permit me to
› say... just proves me right again!  (modest, ain't I?)
…[16 more quoted lines elided]…
› 

Hello DD -

I understand what you're saying, so I've now made a practice of saving
all these clists,macros,and other PRODUCTIVITY aids to a diskette, so
that I can create an appropriate library and use them at whatever
installation I am at. So I am not dependent on the installation having
these tools ! I have not forgotten the basic techniques that you
mention, but again, productivity aids help me get the job done quicker
and that extra performance edge helps justifies the rate. And the
client staff members I work with appreciate my showing them these tools,
and leaving them behind for them to use.

But no FileAid or AbendAid - where have these people been for the last
dozen years, clueless ?? (I know, I know, they do it the hard way,
like *real* programmers .)

› (oh, by the bye... is this Bob Berman the Bob Berman of ESCAPE-sequence
› fame?)

I'm don't understand your reference - is this fame a good thing or a bad
thing ? Can't tell if you're being sarcastic. The answer is probably
not, but again, I don't know what you mean.

Bob
<----------------------------------------------------------------------> 
                 Bob Berman   -    West Hartford, CT                  
  mailto:bbe··.@net··x.com    homepage: http://www.ntplx.net/~bberman  
                                                                        
                 THE TRUE TERRORISTS IN AMERICA ARE                     
          THE PEOPLE WHO DEMAND TO SEE THE STORE MANAGER !              
<----+----+----+----+----+----+----+----+----+----+----+----+----+----+>
```

###### ↳ ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

_(reply depth: 4)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-08-21T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p11@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p9@usenetarchives.gap> <gap-3bbcd1b1c8-p10@usenetarchives.gap> <gap-3bbcd1b1c8-p11@usenetarchives.gap>`

```
Bob Berman wrote:
› 
› The Goobers wrote:
…[30 more quoted lines elided]…
› and leaving them behind for them to use.

Weeeeelllll... I've had it work both ways, of course... a hearty 'Hey,
that's a new one, thanks a bunch!' and a sneered 'Oh, *you* must be
*new* here... *nobody* does it *that* way!'

›
› But no FileAid or AbendAid - where have these people been for the last
› dozen years, clueless ?? (I know, I know, they do it the hard way,
› like *real* programmers .)

They've been Making Money, of course... this particular firm is now run
by the grandson of the Founder, and a story is still told, with glee,
about the subsidiary which had some whacky piece of equipment; this bit
of gear had an odd-sized drive-belt for which a standard bicycle-tire
inner-tube was a perfect replacement.

Anyhow, fifteen years after the Founder 'turned over the reigns' to
Son-of-Founder the Facilities Manager of this particular subsidiary
received a call... from the Founder himself.

'What's this I see about a purchase-order for an inner-tube? You buyin'
personal items on the company nickel?!?'

... and they were *proud* of this kind of micromanagement!

› 
›› (oh, by the bye... is this Bob Berman the Bob Berman of ESCAPE-sequence
…[4 more quoted lines elided]…
› not, but again, I don't know what you mean.

Maybe I got the name wrong, of course, but I recall a Bob Berman... or
maybe it was Beeman?... as the one responsible, back in the '60's, for
the series of commands which became the ASCII Esc (ESCAPE) sequence... I
guess you ain't him, though.

DD
```

###### ↳ ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

_(reply depth: 5)_

- **From:** "george young" <ua-author-1947495@usenetarchives.gap>
- **Date:** 1998-08-21T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p12@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p9@usenetarchives.gap> <gap-3bbcd1b1c8-p10@usenetarchives.gap> <gap-3bbcd1b1c8-p11@usenetarchives.gap> <gap-3bbcd1b1c8-p12@usenetarchives.gap>`

```
The Goobers wrote:
› 
› 
…[5 more quoted lines elided]…
› DD

I suspect you mean Bob Bemer (involved in creation of COBOL and ASCII).
See http://www.bmrsoftware.com/ for what he's up to lately.

George
```

###### ↳ ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

_(reply depth: 5)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-08-22T20:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p12@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p9@usenetarchives.gap> <gap-3bbcd1b1c8-p10@usenetarchives.gap> <gap-3bbcd1b1c8-p11@usenetarchives.gap> <gap-3bbcd1b1c8-p12@usenetarchives.gap>`

```
The Goobers wrote:
› 
› (snip)
…[7 more quoted lines elided]…
› guess you ain't him, though.

It's Bob Bemer, former IBMer, who currently has (or did have) some form
of magic bullet solution for Y2K problems. Roughly some microcode that
recognizes date arithmetic/manipulation and windows them on the fly,
without any program mods, of course.

Bill Lynch
```

###### ↳ ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-08-22T20:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p10@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p9@usenetarchives.gap> <gap-3bbcd1b1c8-p10@usenetarchives.gap>`

```
lae··.@min··g.com wrote:
› 
› The Goobers  wrote:
…[9 more quoted lines elided]…
› AbendAid though. :(

Maybe, maybe not... my manager was none too technical but I'm sure he
wasn't the only one there... are you in Maryland, by any chance?

DD
```

###### ↳ ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-08-22T20:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p10@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p9@usenetarchives.gap> <gap-3bbcd1b1c8-p10@usenetarchives.gap>`

```
The Goobers wrote:
› 
› Bob Berman wrote:
…[13 more quoted lines elided]…
› even unto the old CUT and PASTE macros in ISPF edit.

Well, whatever works. I've taken a different tack, I write the REXX that
the rest of the dept. uses to copy source, compile & stage programs,
etc., plus I've written *lots* of REXX programs (some tiny, some not) to
sift thru data, do file conversions/expansions, etc. Maybe I'm just a
malcontent in refusing to do without all the things that make life
easier.

Bill Lynch

PS: Not a flame.
```

#### ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "ken foskey" <ua-author-3204800@usenetarchives.gap>
- **Date:** 1998-08-20T20:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p17@usenetarchives.gap>`
- **In-Reply-To:** `<35DB9C35.4B24@netbox.com>`
- **References:** `<35DB9C35.4B24@netbox.com>`

```
Bob,

In edit you can type the command EDIT on the command line and open up a
new session, the BROWSE allows you to open browse, the same with SDSF.

Problem statement: You are in edit on JCL and you with to put your
cursor on the beginning of a dataset name and then press enter and open
up that dataset in browse (You could equally set it up as a PF key)

I do not have my manuals so if I am wrong RTFM.

First of all look up edit macros and change the first line to :

ISREDIT

Note there are no options because you will find it from the cursor
location:

there are special edit macro calls that give you your cursor location
and line, get the line go to the cursor location and parse the line to a
non dot/char/digit (probably space or comma).

There are also some neat tools like putting in NOTE lines and
automatically inserting comments blocks. Great tool well worth reading
up on.

Easy as pi
Ken

PS: Send me a copy of your next attempt or put it on the group have if
you have further problems.

Bob Berman wrote:
› 
› If this is not the proper newsgroup to direct this question, and you can
…[69 more quoted lines elided]…
› <----+----+----+----+----+----+----+----+----+----+----+----+----+----+>
```

#### ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "gilbert saint-flour" <ua-author-14669543@usenetarchives.gap>
- **Date:** 1998-08-21T12:11:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p18@usenetarchives.gap>`
- **In-Reply-To:** `<35DB9C35.4B24@netbox.com>`
- **References:** `<35DB9C35.4B24@netbox.com>`

```
In <35D··.@net··x.com>, on 08/19/98 at 08:47 PM, Bob Berman
said:

› Everywhere I have worked in the past has had a CLIST or REXX exec that
› could be invoked from an ISPF Edit or View session that would open 
…[4 more quoted lines elided]…
› installation it was called PDFDSN^B or E.
 
› At my current assignment, they don't seem to have this, ...

If you're looking for a general-purpose "point-and-shoot" facility, there
is one that goes way beyond what you can do in a CLIST: it's a program
called FASTPATH and it is available for free. With FASTPATH, you can
enter BR, ED or VI on the ISPF command line, move the cursor under a
dsname that appears on the screen, press ENTER, et voila, you browse, edit
or view the corresponding data set. BR works in EDIT, SDSF, or any ISPF
application; it even works with VSAM data sets if you also install the
"BR" command processor. The doc for FASTPATH can be found here:

http://members.home.net/gsf/tools/fastpath.html

The PDFTools package contains the assembler source code for FASTPATH as
well as the load-module; it can be downloaded from the Tools&Docs section
of my Web page:

http://members.home.net/gsf

Gilbert Saint-flour

PS: This is not a COBOL question, news:bit.listserv.ispf-l or
news:bit.listserv.ibm-main would be more appropriate.
```

#### ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** gchomuk@my-dejanews.com
- **Date:** 1998-08-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6s1q6q$1t4$1@nnrp1.dejanews.com>`
- **References:** `<35DB9C35.4B24@netbox.com>`

```
Bob,

This may be very simple.  If you are in an edit or view dialog, an edit macro
will do exactly what you want.  I have one that I'll post here.  If you want,
I'll email the macro as a text file that you can upload.

Essentially I have two: One for edit (E) and one for browse (B).  Because it's
an edit macro (which works in View mode, not Browse), you can be editting a
member/dataset session and type the command (E or B in this case).

You'll have to take a look it's not in CLIST, it's REXX source and should be
added to a dataset allocated as SYSUPROC.  It's even documented and has usage
help available typing "E ?".

Good luck.  I hope this helps!

********* Start of paste **************
/* REXX */
/*

   Edit another member in the same or another dataset.
   Does not disturb the current edit session. Current session
   resumes after subsequent edit session.

   This macro works in Panvalet edit as well as ISPF edit, however
   you cannot try to edit a panlib, for obvious reasons.

   Syntax:

       To edit a member in the same dataset: "E member"
       To edit a member in another dataset: "E node.node(mbr)"
       To get a list of members in a dataset: "E node.node"

       NOTE: If high level qualifier of dsn is not the same as
             the ISPF Profile Prefix setting, the dsn should be
             enclosed in apostrophes: E 'QUAL.FNTST.SOURCE'.

   Assumptions:

     - First node of dsn has been omitted and will be replaced by
       the TSO Profile Prefix unless dsn is enclosed in aposts.
     - If only one node of dsn has been passed, we build the second
       node using the assumption that the second node is users initials.
     - Standard dataset names are used for datasets;  there are three
       nodes in the dsn, such as "DEVL.GPC.EMAC", "DEVL.GPC.REXX", etc.

   GPC - 2/04/95
*/
arg parm
address ISPEXEC
"ISREDIT MACRO PROCESS (PARM)"  /* we be a macro         */
address ISPEXEC "VGET ZUSER"      /* get userid            */

if parm ="?" then do
  say "Usage: e "
  say "       e member"
  say "or:    e q3(member)"
  say "or:    e q2.q3(member)"
  say "or:    e q1.q2.q3(member)"
  say "or:    e 'q1.q2.q3...qn(member)'"
  say "                          "
  say "This edit macro assumes your tso profile PREFIX setting matches"
  say "high level qualifier of the target dataset.  If this is not "
  say "true you must enclose the fully qualified dsn in apostrophies."
  say "                          "
  say "e (no argument) displays a member list of current dataset."
  say "e member works if member is in same dataset being editted."
  say "e q3(member) works when 1st and 2nd nodes match current dsn."
  say "e q2.q3(member) works when 1st, 2nd and 3rd node match dsn."
  say "dsn(member) in apostrophes work with any dataset."
  say "                          "
  say "                          "
  exit 4
  end

user=zuser                        /* save it               */
initials="RIGHT"(user,3)          /* get user initials     */
if initials="GXC" then initials='GPC'
/*
   If a dsn was used, we'll find periods separating the nodes.
 */

if "POS"(".",parm)>0 then do      /* have nodes, ie dsn?   */
  if "POS"("(",parm)>0 then do    /* have member too?      */
    parse var parm ds "(" member ")" . . /* get components */
    eparm=parm
    DOEDIT(EPARM)
    end
  else do                         /* no mbr, must be flat  */
    eparm=parm
    DOEDIT(eparm)
    end
  end

/*
   If we get here we have one node and a member, or we simply want
   an msl of the members in the current dataset.

   If the former, tack on the initials as the 2nd node of the dsn.
 */

if "POS"("(",parm)>0 then do            /* have member too?    */
  parse var parm ds "(" member ")" . .  /* break it up         */
  eparm=initials��"."��parm             /* add the second node */
  DOEDIT(eparm)
  end
else do                                 /* just member, must be seq */
  address ISREDIT "(ds)=DATASET"        /* current dsn              */
  parse var ds ."."n2"."n3 rest
  ds=n2��"."��n3��rest
  if parm<>"" then do                   /* parm must be member      */
    eparm=ds��"("��parm��")"            /* build dsn(mbr)           */
    DOEDIT(eparm)
    end
  else do                               /* no parms, just an msl    */
    eparm=ds
    DOEDIT(eparm)
    end
  end

DOEDIT:
arg eparm
tparm="TRANSLATE"(eparm," ",".") /* Remove the periods */
parse var tparm n1 n2 n3  /* Probable, if high lvl qual="PANVALET" */
if n1="PANVALET" then do
  ZEDLMSG="When in PVEDIT you must specify a PDS dataset node and member."
  "SETMSG MSG(ISRZ001)"
  exit 4
  end
x="SYSDSN"(eparm)
if x<>"OK" & x<>"MEMBER NOT FOUND" then do /* can create new member */
  ZEDLMSG = x ��"<" eparm ">"
  "SETMSG MSG(ISRZ001)"
  exit 4
  end
  address ISPEXEC "EDIT DATASET("eparm")"


************* End of Paste

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

##### ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "Wayne L. Beavers" <wayneb@beyond-software.com>
- **Date:** 1998-08-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35E4740A.1375@beyond-software.com>`
- **References:** `<35DB9C35.4B24@netbox.com> <6s1q6q$1t4$1@nnrp1.dejanews.com>`

```
gchomuk@my-dejanews.com wrote:
> 
> Bob,
…[13 more quoted lines elided]…
>

ISPF already supports this. In EDIT if I enter the primary command EDIT
I get the edit panel. Ditto for browse. If I enter EDIT member then I
can edit the new member from the same library.

Or am I missing something?
```

###### ↳ ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "Chomuk Family" <gpchomuk@wwa.com>
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdd17e$7f4a4460$1e3ef1cf@Pchomuk>`
- **References:** `<35DB9C35.4B24@netbox.com> <6s1q6q$1t4$1@nnrp1.dejanews.com> <35E4740A.1375@beyond-software.com>`

```
The macro saves me a heck of alot of typing time and lessens the chance of
fat-fingering dataset names.

I should point out that I use edit macros just to avoid having to type TSO
..
Example: an edit macro that I call JES, allows me to type JES H from the
edit command line.  It issues the TSO SDSF command rather than using, say
"=s" to get to SDSF.

Most sites have some sort of dataset naming standards.  The edit macro,
with modifications to match dataset naming conventions, allow you to omit
higher level nodes of the dataset name.  I try to stick to a simple naming
standard for my personal and project dataset names. 

Example. our project team uses standard, three node dsns and all datasets
have high-level-qualifier (hlq) of  YYYY.  Therefore, if all I ever do is
edit/view datasets that start with YYYY, the macro allows me now to never
have to type it again at the command line; it's assumed.  

Further, for my datasets I use my initials for the second qualifier.  If
all I ever worked were my own datasets, all those starting with "DEVL.GPC",
the macro allows me to never have to type "DEVL.GPC".  It's assumed.

Edit supports a subset of what the edit macro performs.  Edit does allow
recursive edits. EDIT member on the command line will work.  EDIT
'fully.qualified.dsn(member)' works also.  Edit w/no argument brings up the
edit dialog.

Assume three datasets exist and are:

	groupa.usera.jcl
	groupa.usera.rexx
	groupa.usera.emac

During an edit session on any dataset, the macro would allow you to enter
"E jcl(imaspzap)".  The macro will assume dataset name to be
group.user.jcl(imaspzap).

Similarly I could type "e data(member)".   Hope this help at least
understand the macro.  


Wayne L. Beavers <wayneb@beyond-software.com> wrote in article
<35E4740A.1375@beyond-software.com>...
> gchomuk@my-dejanews.com wrote:
> > 
> > Bob,
> > 
> > This may be very simple.  If you are in an edit or view dialog, an edit
macro
> > will do exactly what you want.  I have one that I'll post here.  If you
want,
> > I'll email the macro as a text file that you can upload.
> > 
> > Essentially I have two: One for edit (E) and one for browse (B). 
Because it's
> > an edit macro (which works in View mode, not Browse), you can be
editting a
> > member/dataset session and type the command (E or B in this case).
> > 
> > You'll have to take a look it's not in CLIST, it's REXX source and
should be
> > added to a dataset allocated as SYSUPROC.  It's even documented and has
usage
> > help available typing "E ?".
> > 
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** gchomuk@my-dejanews.com
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6s45ab$oro$1@nnrp1.dejanews.com>`
- **References:** `<35DB9C35.4B24@netbox.com> <6s1q6q$1t4$1@nnrp1.dejanews.com> <35E4740A.1375@beyond-software.com>`

```
ISPF supports the edit membername or edit "fully.qualified.dataset(name)".

This macro fills in high level qualifiers so they don't have to be typed in.
For example assume the following pds datasets exist:

project.groupa.typea
project.groupa.typeb
project.groupb.whatever

While in browse or view, I can issue:

- "e typea(member)" the macro ensures that the dsn is expanded to
Project.groupa.typea(member).

I also use edit macros to front-end rexx procedures.  For example, I have
another macro that I call "JES" that invokes sdsf, sets the prefix and you can
also to specify which queue to start in.  Example:  "JES H"  displays the held
queue and sets the prefix.  The prefix needs to be set because sdsf invoked
this way does not profile this information.  Another way of doing this would
have been issue TSO SDSF, but you  lose the ability to swap to your split
screen.

Here's the (much smaller) rexx procedure I call JES:

This also demonastrate A way to start a rexx procedure without having to issue
TSO.

/* rexx */
/*
   Macro to start SDSF and go directly to the requested queue.
   gpc - 1/15/95
*/
parse upper arg q prefix
"ISREDIT MACRO NOPROCESS JES (Q PREFIX)"
address ISPEXEC
doprefix=0
if prefix<>"" then doprefix=1
if doprefix then do
  if 'LEFT'(prefix,3)="IMS" then pc="pre imstreg*";
  else pc="pre d966gpc"
end /* doprefix */
/*"&ZCMD = 'REM'"*/
/*.resp = enter  */
"SELECT PGM(ISFISP) NOCHECK NEWAPPL(ISF) PARM("Q")"
**************************** Bottom of Data *********************




In article <35E4740A.1375@beyond-software.com>,
  Wayne_Beavers@beyond-software.com wrote:
> gchomuk@my-dejanews.com wrote:
> >
> > Bob,
> >
> > This may be very simple.  If you are in an edit or view dialog, an edit
macro
> > will do exactly what you want.  I have one that I'll post here.  If you
want,
> > I'll email the macro as a text file that you can upload.
> >
> > Essentially I have two: One for edit (E) and one for browse (B).  Because
it's
> > an edit macro (which works in View mode, not Browse), you can be editting a
> > member/dataset session and type the command (E or B in this case).
> >
> > You'll have to take a look it's not in CLIST, it's REXX source and should be
> > added to a dataset allocated as SYSUPROC.  It's even documented and has
usage
> > help available typing "E ?".
> >
…[12 more quoted lines elided]…
>

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "gch..." <ua-author-8572508@usenetarchives.gap>
- **Date:** 1998-08-26T16:12:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p19@usenetarchives.gap>`
- **In-Reply-To:** `<35DB9C35.4B24@netbox.com>`
- **References:** `<35DB9C35.4B24@netbox.com>`

```
Bob,

This may be very simple. If you are in an edit or view dialog, an edit macro
will do exactly what you want. I have one that I'll post here. If you want,
I'll email the macro as a text file that you can upload.

Essentially I have two: One for edit (E) and one for browse (B). Because it's
an edit macro (which works in View mode, not Browse), you can be editting a
member/dataset session and type the command (E or B in this case).

You'll have to take a look it's not in CLIST, it's REXX source and should be
added to a dataset allocated as SYSUPROC. It's even documented and has usage
help available typing "E ?".

Good luck. I hope this helps!

********* Start of paste **************
/* REXX */
/*

Edit another member in the same or another dataset.
Does not disturb the current edit session. Current session
resumes after subsequent edit session.

This macro works in Panvalet edit as well as ISPF edit, however
you cannot try to edit a panlib, for obvious reasons.

Syntax:

To edit a member in the same dataset: "E member"
To edit a member in another dataset: "E node.node(mbr)"
To get a list of members in a dataset: "E node.node"

NOTE: If high level qualifier of dsn is not the same as
the ISPF Profile Prefix setting, the dsn should be
enclosed in apostrophes: E 'QUAL.FNTST.SOURCE'.

Assumptions:

- First node of dsn has been omitted and will be replaced by
the TSO Profile Prefix unless dsn is enclosed in aposts.
- If only one node of dsn has been passed, we build the second
node using the assumption that the second node is users initials.
- Standard dataset names are used for datasets; there are three
nodes in the dsn, such as "DEVL.GPC.EMAC", "DEVL.GPC.REXX", etc.

GPC - 2/04/95
*/
arg parm
address ISPEXEC
"ISREDIT MACRO PROCESS (PARM)" /* we be a macro */
address ISPEXEC "VGET ZUSER" /* get userid */

if parm ="?" then do
say "Usage: e "
say " e member"
say "or: e q3(member)"
say "or: e q2.q3(member)"
say "or: e q1.q2.q3(member)"
say "or: e 'q1.q2.q3...qn(member)'"
say " "
say "This edit macro assumes your tso profile PREFIX setting matches"
say "high level qualifier of the target dataset. If this is not "
say "true you must enclose the fully qualified dsn in apostrophies."
say " "
say "e (no argument) displays a member list of current dataset."
say "e member works if member is in same dataset being editted."
say "e q3(member) works when 1st and 2nd nodes match current dsn."
say "e q2.q3(member) works when 1st, 2nd and 3rd node match dsn."
say "dsn(member) in apostrophes work with any dataset."
say " "
say " "
exit 4
end

user=zuser /* save it */
initials="RIGHT"(user,3) /* get user initials */
if initials="GXC" then initials='GPC'
/*
If a dsn was used, we'll find periods separating the nodes.
*/

if "POS"(".",parm)>0 then do /* have nodes, ie dsn? */
if "POS"("(",parm)>0 then do /* have member too? */
parse var parm ds "(" member ")" . . /* get components */
eparm=parm
DOEDIT(EPARM)
end
else do /* no mbr, must be flat */
eparm=parm
DOEDIT(eparm)
end
end

/*
If we get here we have one node and a member, or we simply want
an msl of the members in the current dataset.

If the former, tack on the initials as the 2nd node of the dsn.
*/

if "POS"("(",parm)>0 then do /* have member too? */
parse var parm ds "(" member ")" . . /* break it up */
eparm=initials嚙踝蕭"."嚙踝蕭parm /* add the second node */
DOEDIT(eparm)
end
else do /* just member, must be seq */
address ISREDIT "(ds)=DATASET" /* current dsn */
parse var ds ."."n2"."n3 rest
ds=n2嚙踝蕭"."嚙踝蕭n3嚙踝蕭rest
if parm<>"" then do /* parm must be member */
eparm=ds嚙踝蕭"("嚙踝蕭parm嚙踝蕭")" /* build dsn(mbr) */
DOEDIT(eparm)
end
else do /* no parms, just an msl */
eparm=ds
DOEDIT(eparm)
end
end

DOEDIT:
arg eparm
tparm="TRANSLATE"(eparm," ",".") /* Remove the periods */
parse var tparm n1 n2 n3 /* Probable, if high lvl qual="PANVALET" */
if n1="PANVALET" then do
ZEDLMSG="When in PVEDIT you must specify a PDS dataset node and member."
"SETMSG MSG(ISRZ001)"
exit 4
end
x="SYSDSN"(eparm)
if x<>"OK" & x<>"MEMBER NOT FOUND" then do /* can create new member */
ZEDLMSG = x 嚙踝蕭"<" eparm ">"
"SETMSG MSG(ISRZ001)"
exit 4
end
address ISPEXEC "EDIT DATASET("eparm")"


************* End of Paste

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

##### ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "wayne l. beavers" <ua-author-7682107@usenetarchives.gap>
- **Date:** 1998-08-25T20:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p19@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p19@usenetarchives.gap>`

```
gch··.@my-··s.com wrote:
› 
› Bob,
…[13 more quoted lines elided]…
› 

ISPF already supports this. In EDIT if I enter the primary command EDIT
I get the edit panel. Ditto for browse. If I enter EDIT member then I
can edit the new member from the same library.

Or am I missing something?

Wayne L. Beavers         mailto:Way··.@Bey··e.com
Beyond Software, Inc.      http://www.beyond-software.com
"Transforming Legacy Applications"
```

###### ↳ ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "chomuk family" <ua-author-17074570@usenetarchives.gap>
- **Date:** 1998-08-26T20:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p20@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p19@usenetarchives.gap> <gap-3bbcd1b1c8-p20@usenetarchives.gap>`

```
The macro saves me a heck of alot of typing time and lessens the chance of
fat-fingering dataset names.

I should point out that I use edit macros just to avoid having to type TSO
..
Example: an edit macro that I call JES, allows me to type JES H from the
edit command line. It issues the TSO SDSF command rather than using, say
"=s" to get to SDSF.

Most sites have some sort of dataset naming standards. The edit macro,
with modifications to match dataset naming conventions, allow you to omit
higher level nodes of the dataset name. I try to stick to a simple naming
standard for my personal and project dataset names.

Example. our project team uses standard, three node dsns and all datasets
have high-level-qualifier (hlq) of YYYY. Therefore, if all I ever do is
edit/view datasets that start with YYYY, the macro allows me now to never
have to type it again at the command line; it's assumed.

Further, for my datasets I use my initials for the second qualifier. If
all I ever worked were my own datasets, all those starting with "DEVL.GPC",
the macro allows me to never have to type "DEVL.GPC". It's assumed.

Edit supports a subset of what the edit macro performs. Edit does allow
recursive edits. EDIT member on the command line will work. EDIT
'fully.qualified.dsn(member)' works also. Edit w/no argument brings up the
edit dialog.

Assume three datasets exist and are:

groupa.usera.jcl
groupa.usera.rexx
groupa.usera.emac

During an edit session on any dataset, the macro would allow you to enter
"E jcl(imaspzap)". The macro will assume dataset name to be
group.user.jcl(imaspzap).

Similarly I could type "e data(member)". Hope this help at least
understand the macro.


Wayne L. Beavers wrote in article
<35E··.@bey··e.com>...
› gch··.@my-··s.com wrote:
›› 
…[32 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: TSO ISPF, CLISTs and/or REXX exec

- **From:** "gch..." <ua-author-8572508@usenetarchives.gap>
- **Date:** 1998-08-27T13:34:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3bbcd1b1c8-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3bbcd1b1c8-p20@usenetarchives.gap>`
- **References:** `<35DB9C35.4B24@netbox.com> <gap-3bbcd1b1c8-p19@usenetarchives.gap> <gap-3bbcd1b1c8-p20@usenetarchives.gap>`

```
ISPF supports the edit membername or edit "fully.qualified.dataset(name)".

This macro fills in high level qualifiers so they don't have to be typed in.
For example assume the following pds datasets exist:

project.groupa.typea
project.groupa.typeb
project.groupb.whatever

While in browse or view, I can issue:

- "e typea(member)" the macro ensures that the dsn is expanded to
Project.groupa.typea(member).

I also use edit macros to front-end rexx procedures. For example, I have
another macro that I call "JES" that invokes sdsf, sets the prefix and you can
also to specify which queue to start in. Example: "JES H" displays the held
queue and sets the prefix. The prefix needs to be set because sdsf invoked
this way does not profile this information. Another way of doing this would
have been issue TSO SDSF, but you lose the ability to swap to your split
screen.

Here's the (much smaller) rexx procedure I call JES:

This also demonastrate A way to start a rexx procedure without having to issue
TSO.

/* rexx */
/*
Macro to start SDSF and go directly to the requested queue.
gpc - 1/15/95
*/
parse upper arg q prefix
"ISREDIT MACRO NOPROCESS JES (Q PREFIX)"
address ISPEXEC
doprefix=0
if prefix<>"" then doprefix=1
if doprefix then do
if 'LEFT'(prefix,3)="IMS" then pc="pre imstreg*";
else pc="pre d966gpc"
end /* doprefix */
/*"&ZCMD = 'REM'"*/
/*.resp = enter */
"SELECT PGM(ISFISP) NOCHECK NEWAPPL(ISF) PARM("Q")"
**************************** Bottom of Data *********************




In article <35E··.@bey··e.com>,
Way··.@bey··e.com wrote:
› gch··.@my-··s.com wrote:
›› 
…[30 more quoted lines elided]…
› 

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
