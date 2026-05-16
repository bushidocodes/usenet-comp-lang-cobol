[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Use of declaratives on file errors

_49 messages · 16 participants · 2000-09_

---

### Use of declaratives on file errors

- **From:** Stefan Meyer <meyerst@my-deja.com>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q9v44$1r1$1@nnrp1.deja.com>`

```


At the moment I don't use declaratives on file errors (like use after
standard error procedure on demofile).

But I really would like to hear something about the advantages or
disadvantages when using this technique.

- Is this a good way to do re-reads on locked records?
- Shall they only be used to display error msgs?
- etc. pp.

Oh. I'm using Merant COBOL 4.1 on Unix.

TIA - Stefan Meyer




Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Use of declaratives on file errors

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g1713k0.pminews@news.wanadoo.es>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com>`

```
On Wed, 20 Sep 2000 09:13:53 GMT, Stefan Meyer wrote:

>
>
…[13 more quoted lines elided]…
>
Hi,

I always use DECLARATIVES for file error handling in my programs, because it
helps me to keep the error handling separated from the program logic.

For every file, I define a status field in WORKING-STORAGE with 88 levels for
the values I explicitly want to check, for example

01      INFILE-STATUS                     PIC XX.
          88    INFILE-PERMITTED      VALUES '10' '23'.
          88    INFILE-END-OF FILE     VALUE '10'.
          88    INFILE-INVALID-KEY     VALUE '23'.

DECLARATIVES.
DC-INFILE SECTION.
                    USE ON STANDARD ERROR PROCEDURE ON INFILE.
DC-10.
                    IF NOT INFILE-PERMITTED
                         DISPLAY 'ERROR ON FILE INFILE, STATUS '
INFILE-STATUS
                         STOP RUN.
DC-EXIT.
                    EXIT.
END DECLARATIVES.

Having coded this section, I know I don't have to worry about file errors.
Also, I never use AT END and INVALID KEY, but the defined 88 levels of the
status field. When using COBOL 74, it gives you the possibility to simulate
AT END and NOT AT END in a READ statement.
  
     READ INFILE.
     IF INFILE-AT-END
           CLOSE INFILE
     ELSE  PERFORM PROCESS-RECORD.

One catch, if your OPEN returns an error, the DECLARATIVES section is not
executed.

I have never used DECLARATIVES to re-read locked records, but I think it
would be possible,
although I don't know what happens if the re-read generates an error. Maybe
someone else has tried this out?

Just my opinion

Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

##### ↳ ↳ Re: Use of declaratives on file errors

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qa9js$rs0$1@slb6.atl.mindspring.net>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <jvyyrzubevmbagrfvasbezngvpnpbz.g1713k0.pminews@news.wanadoo.es>`

```
I see a note in your signature relating to "COBOL II".  Is this IBM's VS
COBOL II (and have you looked at their newer/strategic COBOL product)?

ANY WAY,
  My real question is WHAT type of problem is not getting handled by the
DECLARATIVE when you do an OPEN?  You really SHOULD go to the DECLARATIVE on
a OPEN with a problem - and I think that IBM COBOL's usually do - or at least
they did when I last tested them.

P.S.  Did you know that you were supposed to use the EROPT option in your JCL
for QSAM files.  Sometimes, failing to use this explains why some
DECLARATIVES are not executed.  See:

http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IGYPG204/1%2e8%2e1%2e4?
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g178m00.pminews@news.wanadoo.es>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <jvyyrzubevmbagrfvasbezngvpnpbz.g1713k0.pminews@news.wanadoo.es> <8qa9js$rs0$1@slb6.atl.mindspring.net>`

```
On Wed, 20 Sep 2000 07:12:53 -0500, William M. Klein wrote:

>I see a note in your signature relating to "COBOL II".  Is this IBM's VS
>COBOL II (and have you looked at their newer/strategic COBOL product)?
…[15 more quoted lines elided]…
>Bill Klein
Bill,

I have experienced problems with both ANSI 74 COBOL and COBOL II under VSE.
When defining a file status for a file (both VSAM and SAM) the open errors
are handled neither by the operating system, nor by the DECLARATIVES.
I had to check the status value after the open (and the close as well) to
make sure the file was opened correctly.
The EROPT option doesn't exist under VSE, only on MVS.
Unfortunately, I don't work anymore with mainframes, so I don't have any
experience with IBM's latest and greatest COBOL

Regards,
Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 4)_

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ncy5.1040$5p.9304@news2.mia>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <jvyyrzubevmbagrfvasbezngvpnpbz.g1713k0.pminews@news.wanadoo.es> <8qa9js$rs0$1@slb6.atl.mindspring.net> <jvyyrzubevmbagrfvasbezngvpnpbz.g178m00.pminews@news.wanadoo.es>`

```
Ony Wang VS COBOL, Honeywell COBOL
and IBM COBOL II and COBOL for MVS/VM,

if you code  a file status and a PROPER declarative section,
The system will normally update the File Status and then go to the
appropriate Declarative Section.

IF However, (on IBM), the input file is a SEQ file that has not had EOD set
(e.g. IEFBR14 to create the file vice IEBGENER or Repro) then the File
Status
is not set, instead you go directly to the Declaratives.  No Declaratives,
ABEND.
The same should probably work with opening OUPUT a KSDS that is not
specified REUS.

I've found that a lot of programmers don't use Declaratives (Nor Internal
Sorts)
because they do NOT know how to use them. (or use them effectively).

Willem Clements <willem@horizontes-informatica.com> wrote in message
news:jvyyrzubevmbagrfvasbezngvpnpbz.g178m00.pminews@news.wanadoo.es...
> On Wed, 20 Sep 2000 07:12:53 -0500, William M. Klein wrote:
>
…[5 more quoted lines elided]…
> >DECLARATIVE when you do an OPEN?  You really SHOULD go to the DECLARATIVE
on
> >a OPEN with a problem - and I think that IBM COBOL's usually do - or at
least
> >they did when I last tested them.
> >
> >P.S.  Did you know that you were supposed to use the EROPT option in your
JCL
> >for QSAM files.  Sometimes, failing to use this explains why some
> >DECLARATIVES are not executed.  See:
> >
>
>http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IGYPG204/1%2e8%2e1%2e
4?
> >
> >
…[4 more quoted lines elided]…
> I have experienced problems with both ANSI 74 COBOL and COBOL II under
VSE.
> When defining a file status for a file (both VSAM and SAM) the open errors
> are handled neither by the operating system, nor by the DECLARATIVES.
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qbsjf$9ke$1@slb7.atl.mindspring.net>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <jvyyrzubevmbagrfvasbezngvpnpbz.g1713k0.pminews@news.wanadoo.es> <8qa9js$rs0$1@slb6.atl.mindspring.net> <jvyyrzubevmbagrfvasbezngvpnpbz.g178m00.pminews@news.wanadoo.es> <7ncy5.1040$5p.9304@news2.mia>`

```
Did you include the correct EROPT parameter in your JCL and it still didn't
go to the DECLARATIVE?  If so, then this is a "bug" in the IBM compiler - as
any ANSI/ISO standard compiler is required to do this.

NOTE: This is talking about OS/390 (or MVS-ish) environments *and* QSAM.
There are different rules for VSAM.
```

#### ↳ Re: Use of declaratives on file errors

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qffb3$h7k$1@nnrp1.deja.com>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com>`

```
In article <8q9v44$1r1$1@nnrp1.deja.com>,
  Stefan Meyer <meyerst@my-deja.com> wrote:
>
>
…[8 more quoted lines elided]…
> - etc. pp.

Hi:

Testing the File-status after EVERY SINGLE I-O operation, is,
in my opinion, ESSENTIAL to writing dependable programs.

Testing the status and coding the appropriate error-messages or
responses is imperative. Using declaratives is a cop-out.

If an I-O operation produces a non-zero file-status, the
programmer has to decide what to do about it depending on the
circumstances.

I have never seen COBOL code posted to the forum which
tested the File-Status. What does this imply?

Thanks

Tony Dilworth



Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Use of declaratives on file errors

- **From:** Stefan Meyer <meyerst@my-deja.com>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qfjra$lv2$1@nnrp1.deja.com>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com>`

```
I also check the file-status after every (really) file-operation. And
I've only one section/library for each file to deal with.
Outside the section/lib I set some 88-Levels to define what to do on
the next read/write....

But I would like to know how other people are working and to learn more
about COBOL features...

All the best - Stefan Meyer

In article <8qffb3$h7k$1@nnrp1.deja.com>,
  Foodman <foodman123@aol.com> wrote:
> Hi:
>
…[19 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qh63v$p38$1@sshuraaa-i-1.production.compuserve.com>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfjra$lv2$1@nnrp1.deja.com>`

```
    When using Merant on pc's. it seems to me that the default,
no file status, no declaratives
option works well enough if all that you want to do is stop run.
The at end and Invalid key clauses
take care of routine stuff.

    One reason I have indentified for using file status (or
declaratives) would be to enable
the program to inform the user what is happening in something
approaching plain english.
Ie, "The customer file is corrupt.  Please rebuild.".


Stefan Meyer <meyerst@my-deja.com> wrote in message
news:8qfjra$lv2$1@nnrp1.deja.com...
> I also check the file-status after every (really)
file-operation. And
> I've only one section/library for each file to deal with.
> Outside the section/lib I set some 88-Levels to define what to
do on
> the next read/write....
>
> But I would like to know how other people are working and to
learn more
> about COBOL features...
>
…[9 more quoted lines elided]…
> > Testing the status and coding the appropriate error-messages
or
> > responses is imperative. Using declaratives is a cop-out.
> >
…[9 more quoted lines elided]…
> > Tony Dilworth
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qi1oh$g3k$1@nnrp1.deja.com>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfjra$lv2$1@nnrp1.deja.com> <8qh63v$p38$1@sshuraaa-i-1.production.compuserve.com>`

```
In article <8qh63v$p38$1@sshuraaa-i-1.production.compuserve.com>,
  "Russell Styles" <RWSTYLES@COMPUSERVE.COM> wrote:
>     When using Merant on pc's. it seems to me that the default,
> no file status, no declaratives
> option works well enough if all that you want to do is stop run.
> The at end and Invalid key clauses
> take care of routine stuff.

Hi:

Yes, they will work fine SO LONG AS NOTHING EVER GOES WRONG.

THanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 5)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qis8t$nef$1@sshuraab-i-1.production.compuserve.com>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfjra$lv2$1@nnrp1.deja.com> <8qh63v$p38$1@sshuraaa-i-1.production.compuserve.com> <8qi1oh$g3k$1@nnrp1.deja.com>`

```
    You don't understand - the default no file status, no
decalaratives action works fine
if, and only if, ALL that you want to do is stop run with a
enigmatic message (to the user
at any rate).

    It will handle errors.  Not very well, but it will handle
them.

    PS - I understand that the rules for some other
compiler/runtimes
differ.  So far as  I know, merant normally (always?) displays a
message and does a stop run
with any "9" level error.

    For the record, I do use file status.


Foodman <foodman123@aol.com> wrote in message
news:8qi1oh$g3k$1@nnrp1.deja.com...
> In article
<8qh63v$p38$1@sshuraaa-i-1.production.compuserve.com>,
>   "Russell Styles" <RWSTYLES@COMPUSERVE.COM> wrote:
> >     When using Merant on pc's. it seems to me that the
default,
> > no file status, no declaratives
> > option works well enough if all that you want to do is stop
run.
> > The at end and Invalid key clauses
> > take care of routine stuff.
…[11 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39ccb2bb.127439477@207.126.101.100>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfjra$lv2$1@nnrp1.deja.com> <8qh63v$p38$1@sshuraaa-i-1.production.compuserve.com>`

```
With the callable rebuild, we simply detected that the file was
corrupt and rebuilt it for them!

On Fri, 22 Sep 2000 22:44:15 -0400, "Russell Styles"
<RWSTYLES@COMPUSERVE.COM> wrote:

>    When using Merant on pc's. it seems to me that the default,
>no file status, no declaratives
…[49 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 5)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qijsf$2rb$1@nnrp1.deja.com>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfjra$lv2$1@nnrp1.deja.com> <8qh63v$p38$1@sshuraaa-i-1.production.compuserve.com> <39ccb2bb.127439477@207.126.101.100>`

```
In article <39ccb2bb.127439477@207.126.101.100>,
  thaneH@softwaresimple.com (Thane Hubbell) wrote:
> With the callable rebuild, we simply detected that the file was
> corrupt and rebuilt it for them!


Hi:

Yes, this is the ideal solution. I think you want to
tell the user that you are doing it though and let him
bless your action.

Do you know if the REBUILD with my ancient compiler
Microsoft v5 is callable and if so how?

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 6)_

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-4oHXMyZNE6Tj@tcpserver>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfjra$lv2$1@nnrp1.deja.com> <8qh63v$p38$1@sshuraaa-i-1.production.compuserve.com> <39ccb2bb.127439477@207.126.101.100> <8qijsf$2rb$1@nnrp1.deja.com>`

```
On Sat, 23 Sep 2000 15:57:11, Foodman <foodman123@aol.com> wrote:

> In article <39ccb2bb.127439477@207.126.101.100>,
>   thaneH@softwaresimple.com (Thane Hubbell) wrote:
…[12 more quoted lines elided]…
> 

From what I can remember (it's a long time ago) the
Microsoft compiler did not have a "callable rebuild". You
have to assemble a command line and execute
the command by passing it off to the OS. 

I can't remember how to do that either - maybe the CHAIN
statement? I know there was a way to do it because
I did some code like that but I converted it to the Microfocus
compiler about 8 years ago. I called the DOS version
of Word to edit a document file created by MS-COBOL
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-09-24T00:26:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CD4861.5B894CDD@home.com>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfjra$lv2$1@nnrp1.deja.com> <8qh63v$p38$1@sshuraaa-i-1.production.compuserve.com> <39ccb2bb.127439477@207.126.101.100> <8qijsf$2rb$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> In article <39ccb2bb.127439477@207.126.101.100>,
…[11 more quoted lines elided]…
> Microsoft v5 is callable and if so how?

Like the other writer - so long ago since M/S V5 - just a wild
suggestion - can you display upon Command Line to call the Rebuild ?

Jimmy
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-25T03:52:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39cecbe2.22224892@207.126.101.100>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfjra$lv2$1@nnrp1.deja.com> <8qh63v$p38$1@sshuraaa-i-1.production.compuserve.com> <39ccb2bb.127439477@207.126.101.100> <8qijsf$2rb$1@nnrp1.deja.com>`

```
I don't know, but if it's there it will be CALLRB.

On Sat, 23 Sep 2000 15:57:11 GMT, Foodman <foodman123@aol.com> wrote:

>In article <39ccb2bb.127439477@207.126.101.100>,
>  thaneH@softwaresimple.com (Thane Hubbell) wrote:
…[19 more quoted lines elided]…
>Before you buy.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 5)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qis93$nef$2@sshuraab-i-1.production.compuserve.com>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfjra$lv2$1@nnrp1.deja.com> <8qh63v$p38$1@sshuraaa-i-1.production.compuserve.com> <39ccb2bb.127439477@207.126.101.100>`

```
    This is probably the best way to handle a corrupt file, but:
1.  You need to have enough memory available.  This can be tough
if using 16 bit runtime.  Until someone comes up with a 32 bit
runtime
that is al least 80% as fast as the 16 bit runtime, the 16 bit
will
linger (painfully).

2.  Is everyone REALLY out of the GD file?


Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:39ccb2bb.127439477@207.126.101.100...
> With the callable rebuild, we simply detected that the file was
> corrupt and rebuilt it for them!
>
/Eureka/2006/
```

##### ↳ ↳ Re: Use of declaratives on file errors

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qfitl$m6q$1@nntp9.atl.mindspring.net>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com>`

```
"Foodman" <foodman123@aol.com> wrote in message news:8qffb3
>
> Testing the status and coding the appropriate error-messages or
> responses is imperative. Using declaratives is a cop-out.
>

Tony,
  I do tend to disagree with almost every coding suggestion that you make
(purely for personal coding "style" development reasons) - but in this case,
I really would like to know/understand WHY you think that in-line file-status
checking is "so much better" (my words - not yours) than using DECLARATIVES.
I do understand the reasoning for doing ONE OR THE OTHER - but I don't
understand why you consider one to be a "cop-out" - as there is nothing that
you can do in one that you can't really do in the other.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39cb60bb.40898070@207.126.101.100>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfitl$m6q$1@nntp9.atl.mindspring.net>`

```
I'm not Tony, and I don't necessarily check the file status after
EVERY operation (but I do after most) -- but here's why I "shun"
declaratives.

Given a choice (and sometimes I am) I use inline file status checking
instead of Declaratives.  I dislike the constraints of perform range
placed on me by use if declaratives.  Additionally, I see little
utility in something that is executed on a near fatal (or fatal) error
that then returns control to the program immediately after the error.
I've either got to JUMP out of the declaratives - having no real idea
where I am insinde the program's execution, or I have to set some flag
in the declaratives and react in the code after the declaratives have
executed.

Additionally, I dislike the fact that that these things can get
performed basically from ANYWHERE I have a file operation.  I dislike
the implicitness of it -- I much prefer EXPLICIT logic in my code.

I set up 88 levels for file status fields and check based on those.

Most of this is just personal preference.

On Fri, 22 Sep 2000 07:21:24 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>"Foodman" <foodman123@aol.com> wrote in message news:8qffb3
>>
…[19 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 4)_

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g1bg7d0.pminews@news.wanadoo.es>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfitl$m6q$1@nntp9.atl.mindspring.net> <39cb60bb.40898070@207.126.101.100>`

```
On Fri, 22 Sep 2000 13:41:56 GMT, Thane Hubbell wrote:

>I'm not Tony, and I don't necessarily check the file status after
>EVERY operation (but I do after most) -- but here's why I "shun"
…[17 more quoted lines elided]…
>
Well, I always use declaratives, but using the same reasoning as you.

In my program logic, I don't want to handle any strange file situation. If
something occurs that I didn't foresee, I want my program to stop. So, what I
do, I define with 88 levels the conditions I want to handle in my program,
and all the others get caught in my declaratives and my declaratives section
ends with a STOP RUN. for example

01   STATUSFIELD                PIC XX.
       88  END-OF FILE             VALUE '10'.



DECLARATIVES.
STAT SECTION
    USE AFTER ERROR PROCEDURE ON INFILE.

STAT-10.
      IF NOT END-OF FILE
              DISPLAY ' THERE IS SOMETHING WRONG HERE ' STATUSFIELD
              STOP RUN.
STAT-EXIT.
      EXIT.
END DECLARATIVES

So either my program continues after the I-O instruction, or it cancels in
the DECLARATIVES.

If this is just a simple input file it doesn't make much difference, but when
this file has a lot of operations it really makes the code more readable,
because I don't have any error checking code in the middle of my program
logic. Also, when writing the program, I can be sure that every situation
will be handled. I do agree that whenever you define a status field for a
file, you'll have to use either declaratives or check the status after any
file operation.

Of course, both ways are valid.

Just my opinion

Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 5)_

- **From:** "David W. Furin" <dfurin@larich.com>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CBCD9E.11ED8B8E@larich.com>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfitl$m6q$1@nntp9.atl.mindspring.net> <39cb60bb.40898070@207.126.101.100> <jvyyrzubevmbagrfvasbezngvpnpbz.g1bg7d0.pminews@news.wanadoo.es>`

```
Willem Clements wrote:
> 
> Well, I always use declaratives, but using the same reasoning as you.
…[39 more quoted lines elided]…
> http://www.brainbench.com


We do almost exactly the same thing.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 4)_

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wtVy5.5115$5p.33265@news2.mia>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfitl$m6q$1@nntp9.atl.mindspring.net> <39cb60bb.40898070@207.126.101.100>`

```
Actually, and Thane I'm suprised this came from you (but I havn't read your
Book),
it seems to me that you lack understanding of how to use DECLARATIVES.
Every point you made against them can be made for in-line FILE STATUS
checking
as well:
     > I dislike the constraints of perform range
    > placed on me by use if declaratives.  Additionally, I see little
…[5 more quoted lines elided]…
    > executed.

There is no 'perform Range Constraint other than Don't perform your caller'
(and that's bad coding anyways)

The reason you have no Idea where you are is your fault.  At PARAGRAPH entry
'MOVE C-100-OBTAIN-TRANS'  TO WS-LAST-PARAGRAPH.'
At Critical junctures, 'MOVE 'READ EMP-MSTR BY DATE'  TO WS-SUB-PARA'
Setup your declaratives by 'INPUT' 'OUTPUT' 'I-O' 'EXTEND' and by SPECIFIC
NAME
which overrides MODE.

EXCEPTION/ERROR procedures can be used to check the status key values
whenever an input/output error occurs.

So, if it is an error you want to ignore, just exit the section,
ELSE set some values and perform the appropriate error routine.

YOU GET to choose for each file operation whether DECLARATIVES will be used!

The EXCEPTION/ERROR procedure is executed:

   Either after completing the system-defined input/output error routine,
or

   Upon recognition of an INVALID KEY or AT END condition when an INVALID
KEY or AT END phrase has not been specified in the input/output statement,
or

   Upon recognition of an IBM-defined condition that causes status key 1 to
be set to 9.  (See "Status Key" in topic 6.1.8.9.1.)


So, you can 'MIX AND MATCH'!

AND besides, Invalid Key and AT END, etc are ALL EXCEPTIONS to the regular
processing!




I dislike the fact that that these things can get
> performed basically from ANYWHERE I have a file operation.  I dislike
> the implicitness of it -- I much prefer EXPLICIT logic in my code.


Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:39cb60bb.40898070@207.126.101.100...
> I'm not Tony, and I don't necessarily check the file status after
> EVERY operation (but I do after most) -- but here's why I "shun"
…[31 more quoted lines elided]…
> >(purely for personal coding "style" development reasons) - but in this
case,
> >I really would like to know/understand WHY you think that in-line
file-status
> >checking is "so much better" (my words - not yours) than using
DECLARATIVES.
> >I do understand the reasoning for doing ONE OR THE OTHER - but I don't
> >understand why you consider one to be a "cop-out" - as there is nothing
that
> >you can do in one that you can't really do in the other.
> >
…[10 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39ccb327.127547527@207.126.101.100>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfitl$m6q$1@nntp9.atl.mindspring.net> <39cb60bb.40898070@207.126.101.100> <wtVy5.5115$5p.33265@news2.mia>`

```
Oh, I understand them.  In my book I describe their proper use in
detail, without negative comment.  Read on....

On Fri, 22 Sep 2000 23:24:46 -0700, "mangogwr"
<mangogwr@bellsouth.net> wrote:

>Actually, and Thane I'm suprised this came from you (but I havn't read your
>Book),
…[14 more quoted lines elided]…
>(and that's bad coding anyways)

Of course - but often you find people coding special sections in
Declaratives with no USE statement or with a dummy file so that they
can perform some common code.  Maybe I've just seen too much abuse to
like them.

>
>The reason you have no Idea where you are is your fault.  At PARAGRAPH entry
…[4 more quoted lines elided]…
>which overrides MODE.

I'm familiar with this, but coding a specifif name means the INPUT,
OUTPUT etc will not be executed, only the declarative associted with
the file.  

>
>EXCEPTION/ERROR procedures can be used to check the status key values
>whenever an input/output error occurs.

Yes, that is how we use them where I work.

>
>So, if it is an error you want to ignore, just exit the section,
>ELSE set some values and perform the appropriate error routine.

Occasionally in one place a particular error is to be ignored but in
another it is not.  This leads to complicated coding and the setup of
all kinds of identifiers and switches.  Now, this really isn't an
issue if one is using a SINGLE instance of each operation in your
program.  As you illustrate, a properly written program can make good
use of declaratives. 

>
>YOU GET to choose for each file operation whether DECLARATIVES will be used!
…[17 more quoted lines elided]…
>processing!

No argument there.  

As always I learn from this forum.  I'm even rethinking my stand on
this particular issue.  Declaratives are more important to me in my OO
COBOL programming - because they are used to catch exceptions.  As I
get more comfortable with them for that, I will probably revert to
useing them for files.  

My normal setup is to have a performed open, Read, Write, Delete,
Close etc.   After the perform I check the validitiy based on an 88
level defined on the file status for the file.  Different operations
within my programs have different sets of "succes" status codes.  On a
failure, I determine if it's fatal or not and if so I display a
detailed error message about the coditions within the program that
relate to this error and report it, then abort.  

It is entirely possible to do this within Declaratives.  However, as
you stated there is extra overhead to setup indicator areas so I can
get the level of detail I desire.  There is also the chance that
errors that I traditionally overlook (say a 23 when I don't code an
invalid key) will cause declaratives to be executed needlessly.  

There are a million differnt ways of doing things.  As I continue to
learn I change my mind constantly about what is the "best" way to do
things for me.  I sitll have to live with my old code, however.

Consider me voting "undecided" on the issue.

>
>
…[65 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Use of decl..: Apology to Thane

_(reply depth: 6)_

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S_5z5.6068$5p.35599@news2.mia>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfitl$m6q$1@nntp9.atl.mindspring.net> <39cb60bb.40898070@207.126.101.100> <wtVy5.5115$5p.33265@news2.mia> <39ccb327.127547527@207.126.101.100>`

```
Thane, I didn't actually intend to come off sounding harsh, but I've just
spent
(wasted actually) several hours this week at work with a 'PrimaDonna'
who won't check her work, before accusing someone else of making a mistake.

I had to modify a common copybook (I own it) for a new 'Addendum' record,
and she's telling me 'it doesn't work' for two hours.  I take 5 minutes
to look at her code and she's not moving the data to the structure before
she tries to reference it.  So of course when her code
'IF AUX-MONO-MFR-TRAN-TYPE > SPACES'
is executed, it isn't because she didn't move that data into it!


If it was up to me, she wouldn't be on the project because this is the
fourth time I know this type thing, and she always has to 'CC' the Bosses
especially when she claims 'you changed a data element and now my compile
won't work' and her compile jcl is pointing to an out of date library.  She
won't
take 2 minutes to double-check her work.


So the 'cop out' just ticked me off and I 'backlashed' at you.
Please accept my apologies.



Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:39ccb327.127547527@207.126.101.100...
> Oh, I understand them.  In my book I describe their proper use in
> detail, without negative comment.  Read on....
…[4 more quoted lines elided]…
> >Actually, and Thane I'm suprised this came from you (but I havn't read
your
> >Book),
> >it seems to me that you lack understanding of how to use DECLARATIVES.
…[5 more quoted lines elided]…
> >    > utility in something that is executed on a near fatal (or fatal)
error
> >    > that then returns control to the program immediately after the
error.
> >    > I've either got to JUMP out of the declaratives - having no real
idea
> >    > where I am insinde the program's execution, or I have to set some
flag
> >    > in the declaratives and react in the code after the declaratives
have
> >    > executed.
> >
> >There is no 'perform Range Constraint other than Don't perform your
caller'
> >(and that's bad coding anyways)
>
…[6 more quoted lines elided]…
> >The reason you have no Idea where you are is your fault.  At PARAGRAPH
entry
> >'MOVE C-100-OBTAIN-TRANS'  TO WS-LAST-PARAGRAPH.'
> >At Critical junctures, 'MOVE 'READ EMP-MSTR BY DATE'  TO WS-SUB-PARA'
> >Setup your declaratives by 'INPUT' 'OUTPUT' 'I-O' 'EXTEND' and by
SPECIFIC
> >NAME
> >which overrides MODE.
…[23 more quoted lines elided]…
> >YOU GET to choose for each file operation whether DECLARATIVES will be
used!
> >
> >The EXCEPTION/ERROR procedure is executed:
> >
> >   Either after completing the system-defined input/output error
routine,
> >or
> >
> >   Upon recognition of an INVALID KEY or AT END condition when an
INVALID
> >KEY or AT END phrase has not been specified in the input/output
statement,
> >or
> >
> >   Upon recognition of an IBM-defined condition that causes status key 1
to
> >be set to 9.  (See "Status Key" in topic 6.1.8.9.1.)
> >
…[3 more quoted lines elided]…
> >AND besides, Invalid Key and AT END, etc are ALL EXCEPTIONS to the
regular
> >processing!
>
…[71 more quoted lines elided]…
> >> >  I do tend to disagree with almost every coding suggestion that you
make
> >> >(purely for personal coding "style" development reasons) - but in this
> >case,
…[5 more quoted lines elided]…
> >> >understand why you consider one to be a "cop-out" - as there is
nothing
> >that
> >> >you can do in one that you can't really do in the other.
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Use of decl..: Apology to Thane

_(reply depth: 7)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-25T03:56:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39cec8ea.21465127@207.126.101.100>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfitl$m6q$1@nntp9.atl.mindspring.net> <39cb60bb.40898070@207.126.101.100> <wtVy5.5115$5p.33265@news2.mia> <39ccb327.127547527@207.126.101.100> <S_5z5.6068$5p.35599@news2.mia>`

```
Uh.. . no need to apologize - but it is accepted in the spirit it was
given.  If nothing else, you had me go back and look at my own use of
declaratives and this can only be a good thing.  I think I'll give
them another shot in my next new development project (whatever it
turns out to be!).

On Sat, 23 Sep 2000 13:39:30 -0700, "mangogwr"
<mangogwr@bellsouth.net> wrote:

>Thane, I didn't actually intend to come off sounding harsh, but I've just
>spent
…[224 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CD36E0.55826C16@istar.ca>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfitl$m6q$1@nntp9.atl.mindspring.net>`

```
While I can't speak for Tony, I have felt them to be of little use and
much danger for what I do.  The file error handling declaratives predate
the availability of status codes.  They are generic and not tied to the
verb but only to the file or type of access.  IIRC they were intended to
be used for the non AT END/INVALID KEY exceptions.  While my reading of
the IBM manuals on the subject of DECLARATIVES was cursory at best since
I don't use them, I don't think they are invoked if the file has a
status code defined for it and Carol Baroudi's book Mastering COBOL is
unclear on it in the two places I looked.  Since status codes are now
available and contain more information than was available in the
DECLARATIVE prior to COBOL 74, the status code is what I want to check. 
If I were writing a program to run under TSO or ISPF, I would be
checking all file I-O and taking appropriate action including issuing
specific error messages on unsuccessful completion where useful.  Doing
so with DECLARATIVES becomes tricky at best.  In the DECLARATIVE I have
no idea of what the operation was that found/caused the error unless I
take special care.  Nor do I recall any facility to find out what the
error was.  With status code checking I can have  individualized
handling, common handling via a PERFORM or CALL statement or some
combination where some errors are considered generic.  When the common
exception handling facility in the COBOL 2xxx standard becomes available
I will look at it to see if it would be useful and worth the potential
overhead.      

If the standard system action on exceptions other than AT END and
INVALID KEY is inadequate then I want to be able to do more than a
DECLARATIVE will let me do.

Clark Morris, CFM Technical Programming Services Inc., cfmtech@istar.ca

"William M. Klein" wrote:
> 
> "Foodman" <foodman123@aol.com> wrote in message news:8qffb3
…[16 more quoted lines elided]…
>     wmklein <at> ix dot netcom dot com
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-25T03:56:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39cecc66.22357155@207.126.101.100>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfitl$m6q$1@nntp9.atl.mindspring.net> <39CD36E0.55826C16@istar.ca>`

```
At great risk of stating this incorrectly -- this is my
understanding.....

Declaratives are executed any time the status value does not begin
with ZERO - EXCEPT ....

When Invalid Key or At End is coded, and the status values fit those
conditions, the declaratives are not executed.

Interestingly - if you have a CURRENTLY standards conforming compiler
(Note in the next standard this restriction is lifted) you MUST code
either Invalid Key/At End or have Declaratives.


On Sat, 23 Sep 2000 20:04:00 -0300, "Clark F. Morris, Jr."
<cfmtech@istar.ca> wrote:

>While I can't speak for Tony, I have felt them to be of little use and
>much danger for what I do.  The file error handling declaratives predate
…[48 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CF768B.5802E25B@brazee.net>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfitl$m6q$1@nntp9.atl.mindspring.net> <39CD36E0.55826C16@istar.ca> <39cecc66.22357155@207.126.101.100>`

```


Thane Hubbell wrote:

> At great risk of stating this incorrectly -- this is my
> understanding.....
…[9 more quoted lines elided]…
> either Invalid Key/At End or have Declaratives.

I don't think I have ever tried a READ without one of those.  But certainly I have
coded OPEN, CLOSE, and WRITE without one of those, with several different compilers.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qi1k8$g37$1@nnrp1.deja.com>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <8qfitl$m6q$1@nntp9.atl.mindspring.net>`

```
In article <8qfitl$m6q$1@nntp9.atl.mindspring.net>,> Tony,
>   I do tend to disagree with almost every coding suggestion that you
make
> (purely for personal coding "style" development reasons) - but in
this case,
> I really would like to know/understand WHY you think that in-line
file-status
> checking is "so much better" (my words - not yours) than using
DECLARATIVES.
> I do understand the reasoning for doing ONE OR THE OTHER - but I don't
> understand why you consider one to be a "cop-out" - as there is
nothing that
> you can do in one that you can't really do in the other.

Hi:

I know only too well that the majority of people who read my stuff
think I am a hopeless nitwit.  The reason I continue to post my
opinions is for the benefit of the newcomers. Hopefully, a
different point of view might make them think.  This thread is
a good example of this, I think.

The main reason is that I ALWAYS provide a DETAILED error message
telling the user what the problem is. The user must acknowledge
the message and the program will then take appropriate action.

If the error is something the user can do something about, e.g.,
rebuild a damaged file, they would be told to do so. In certain
cases, it may be permissible for the program to continue, so long
as the user knows about the error.

I grant one thing, checking the file-status all the time is
horribly tedious. i just checked one of my POS programs and
there are 92 error messages to which the user can respond
and 30 fatal messages which merely tell the user he is dead
and why for a total of 122 messages. That does NOT include
error messages in my standard copies.

As you know, I am not a structured programmer but would like
to see the file-status tested in the structured examples which
appear in the forum.

Of course, checking the file-status for a locked record is
required in a multi-user application - how do you do that
in the body of your structured code?

My standard error routine displays a separate panel giving the details
and the file-status. Unless I am wrong, the declaratives do
give give sufficient level of detail in their reporting of
the error. Another consideration is that the file-status can
mean different things application-wise depending on circumstances
(e.g., at end on the first read versus at end later.)

I also think it IMPORTANT that newcomers be made fully aware
of things like checking the file-status.  Based on the code
examples I have seen here, nobody ever checks the status.

At present, I have about 600 users all over the world (the majority
in the US and Canada). I provide free telephone support. The number
of calls for support I get is virtually zero. I do NOT believe
this would be the case if I didn't SCRUPULOUSLY check the file-status
and EVERYTHING the user enters. The objective must be to write
foolproof programs.

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Use of declaratives on file errors

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CB615C.7CD1C8A9@brazee.net>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com>`

```
Foodman wrote:

> Testing the File-status after EVERY SINGLE I-O operation, is,
> in my opinion, ESSENTIAL to writing dependable programs.

Then I rarely write dependable programs.  Fortunately they work just as
though they were dependable.

My environment is different from yours (MVS and other big iron shops), but
your statement is a blanket statement.

> Testing the status and coding the appropriate error-messages or
> responses is imperative. Using declaratives is a cop-out.

The system (MVS) tells us all we need to know - but we need the abort to
make sure the computer room operators notice.

I use declaratives even less often than I use File-status.  But I have no
idea why you say it is a cop-out.  Could you please explain?


> If an I-O operation produces a non-zero file-status, the
> programmer has to decide what to do about it depending on the
> circumstances.

What if the desired behavior for any non-zero result is to abort?


> I have never seen COBOL code posted to the forum which
> tested the File-Status. What does this imply?

You haven't been reading as many messages as I have.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qi27r$glc$1@nnrp1.deja.com>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <39CB615C.7CD1C8A9@brazee.net>`

```

>
> Then I rarely write dependable programs.  Fortunately they work just
as
> though they were dependable.

Hi:

They probably work fine just so long as nothing ever goes wrong. . .

>
> My environment is different from yours (MVS and other big iron
shops), but
> your statement is a blanket statement.
>
…[3 more quoted lines elided]…
> The system (MVS) tells us all we need to know - but we need the abort
to
> make sure the computer room operators notice.

I would also hope that the end-user somehow finds out something
went wrong whether the operators did or not.
>
> I use declaratives even less often than I use File-status.  But I
have no
> idea why you say it is a cop-out.  Could you please explain?

See message 16 which is my response to the same question
asked by Mr. Klein.

>
> > If an I-O operation produces a non-zero file-status, the
…[3 more quoted lines elided]…
> What if the desired behavior for any non-zero result is to abort?

An error message requiring operator acknowledgment should be
given.

>
> > I have never seen COBOL code posted to the forum which
> > tested the File-Status. What does this imply?
>
> You haven't been reading as many messages as I have.

Probably not. . .

Thanks

Tony Dilworth




Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 4)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-09-24T00:20:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000923202000.26773.00000429@ng-cj1.aol.com>`
- **References:** `<8qi27r$glc$1@nnrp1.deja.com>`

```
>From: Foodman foodman123@aol.com 
>Date: 9/23/00 6:55 AM Eastern Daylight Time

>I would also hope that the end-user somehow finds out something
>went wrong whether the operators did or not.

Where I work it depends on the end-user. If CICS goes down or something crashes
in CICS the phones go off the hook with end-users calling.  This situation can
cause the company mucho money.  However if a batch job goes down (most of which
are run between the hours of 11:30pm and 4am) we don't hear much from the
end-user unless they happen to really really want the report they haven't
looked at in 6 months that particular day.

For those jobs that run during the day we usually hear from operations long
before the end-user unless the user is again anxious for their reports. 

Telling the end-users something died during the night is the last thing we do. 
Most times they are totally unaware unless as stated above.

Eileen
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CF7361.3ED29AA6@brazee.net>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <39CB615C.7CD1C8A9@brazee.net> <8qi27r$glc$1@nnrp1.deja.com>`

```


Foodman wrote:

> >
> > Then I rarely write dependable programs.  Fortunately they work just
…[5 more quoted lines elided]…
> They probably work fine just so long as nothing ever goes wrong. . .

The procedures also works when thing do go wrong.

> > My environment is different from yours (MVS and other big iron
> shops), but
…[10 more quoted lines elided]…
> went wrong whether the operators did or not.

Can't wait.  Most of our batch programs and jobs have dependencies which
require something be done now - before the next job program or job in the
dependencies can be run.

> > I use declaratives even less often than I use File-status.  But I
> have no
…[3 more quoted lines elided]…
> asked by Mr. Klein.

"message 16" is meaningless to me.  I will watch for your reply.


> > > If an I-O operation produces a non-zero file-status, the
> > > programmer has to decide what to do about it depending on the
…[5 more quoted lines elided]…
> given.

We don't have any way to lock up the console - I haven't seen a mainframe
shop which allowed that in decades.  The batch systems are written around
success vs aborts.

I have seen errors create e-mail to people who need to know the next day
about troubles.  But the troubles have to be handled now.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-09-23T02:37:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000922223742.23666.00000322@ng-ca1.aol.com>`
- **References:** `<39CB615C.7CD1C8A9@brazee.net>`

```
If we're tallying votes here I'm with Thane and Howard :)

Eileen
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 4)_

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ayVy5.5122$5p.33329@news2.mia>`
- **References:** `<39CB615C.7CD1C8A9@brazee.net> <20000922223742.23666.00000322@ng-ca1.aol.com>`

```
Eileen, how can you agree with Thand & Howard
when Thane despises DECLARATIVES and Howard
uses them, uses FILE STATUS a little more and uses neither much?

YukonMama <yukonmama@aol.com> wrote in message
news:20000922223742.23666.00000322@ng-ca1.aol.com...
> If we're tallying votes here I'm with Thane and Howard :)
>
> Eileen
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39ccb273.127367497@207.126.101.100>`
- **References:** `<39CB615C.7CD1C8A9@brazee.net> <20000922223742.23666.00000322@ng-ca1.aol.com> <ayVy5.5122$5p.33329@news2.mia>`

```
I would not go so far as to say I "Despise" them.  The shop I work
most in uses them exclusively - I can live with it.

On Fri, 22 Sep 2000 23:29:44 -0700, "mangogwr"
<mangogwr@bellsouth.net> wrote:

>Eileen, how can you agree with Thand & Howard
>when Thane despises DECLARATIVES and Howard
…[8 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qi2b7$gln$1@nnrp1.deja.com>`
- **References:** `<39CB615C.7CD1C8A9@brazee.net> <20000922223742.23666.00000322@ng-ca1.aol.com>`

```
In article <20000922223742.23666.00000322@ng-ca1.aol.com>,
  yukonmama@aol.com (YukonMama) wrote:
> If we're tallying votes here I'm with Thane and Howard :)
>
> Eileen
>

Hi Eileen:

Well, the last thing that I would expect is to find
anyone to agree with me :(  Even so, I won't give up :)

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CF740F.C09DC1DA@brazee.net>`
- **References:** `<39CB615C.7CD1C8A9@brazee.net> <20000922223742.23666.00000322@ng-ca1.aol.com> <8qi2b7$gln$1@nnrp1.deja.com>`

```
Foodman wrote:

> Hi Eileen:
>
…[5 more quoted lines elided]…
> Tony Dilworth

My disagreement here isn't against your practice - it is against your
blanket statement.  My environment is different from yours and I have to
use what works best in my environment.  Meanwhile my curiosity leads me
to find out more about what works and doesn't work in your environment.
If we knew everything and were in agreement, there would be no reason to
communicate at all.  And if we had nothing left to learn, we might as
well die, our lives are over.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 4)_

- **From:** frlsfly@aol.com (FRLSFLY)
- **Date:** 2000-09-23T03:32:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000922233236.27190.00000456@ng-fb1.aol.com>`
- **References:** `<20000922223742.23666.00000322@ng-ca1.aol.com>`

```
>If we're tallying votes here I'm with Thane and Howard :)
>
>Eileen

Me too.  I've worked in shops where declaratives were the standard, and they
always seem to have more "mystery" problems than the ones that do inline I/O
status checks. I can't honestly say I can tell you WHY that should be true; as
I agree that in theory Declaratives should be equivalent.

I would also like to note that people who promiscuously call "stop run" in
online programs will often get their heads nailed to the conference room table
during the post-mortem.  This is especially true in CICS shops...


Nathan Meyer
Berkeley, CA
"Big Endian" is what I like.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 5)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qis99$nef$3@sshuraab-i-1.production.compuserve.com>`
- **References:** `<20000922223742.23666.00000322@ng-ca1.aol.com> <20000922233236.27190.00000456@ng-fb1.aol.com>`

```
    For those of us with little mainframe experience, or CICS for
that matter,
why is stop run frowned on.  On a pc, it can be used for the same
purposes that abend is used for on mainframes - to get someone's
attention.



> I would also like to note that people who promiscuously call
"stop run" in
> online programs will often get their heads nailed to the
conference room table
> during the post-mortem.  This is especially true in CICS
shops...
>
>
> Nathan Meyer
> Berkeley, CA
> "Big Endian" is what I like.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 6)_

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g1dbh80.pminews@news.wanadoo.es>`
- **References:** `<20000922223742.23666.00000322@ng-ca1.aol.com> <20000922233236.27190.00000456@ng-fb1.aol.com> <8qis99$nef$3@sshuraab-i-1.production.compuserve.com>`

```
On Sat, 23 Sep 2000 14:13:21 -0400, Russell Styles wrote:

>    For those of us with little mainframe experience, or CICS for
>that matter,
…[4 more quoted lines elided]…
>
Russel,

In a mainframe batch program, STOP RUN is ok, it stops your program. Under
CICS however, it stops CICS (depending on the COBOL and CICS versions and
platform you are running) CICS is the teleprocessing monitor on an IBM
mainframe, so you can imagine what happens when suddenly CICS stops. All
terminals connected (and this might be thousands) stop working. BTW I never
have understood why the IBM CICS preprocessor doesn't flag forbidden COBOL
instructions.

Hope this helps,

Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 7)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qk1gl$l92$1@newssvr05-en0.news.prodigy.com>`
- **References:** `<20000922223742.23666.00000322@ng-ca1.aol.com> <20000922233236.27190.00000456@ng-fb1.aol.com> <8qis99$nef$3@sshuraab-i-1.production.compuserve.com> <jvyyrzubevmbagrfvasbezngvpnpbz.g1dbh80.pminews@news.wanadoo.es>`

```

Even in a batch program, I don't use the STOP RUN statement anymore.  It
doesn't hurt using it for a calling program, but using it in a called
program will not return control to the calling program but to MVS, which is
usually not the desired result.  I prefer to use GOBACK for a calling
program and EXIT PROGRAM for a called program.  A "gotcha" to watch out for
is that an EXIT PROGRAM functions like GOBACK in a called program but like
CONTINUE in a calling program!
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CF761B.D0C8D91@brazee.net>`
- **References:** `<20000922223742.23666.00000322@ng-ca1.aol.com> <20000922233236.27190.00000456@ng-fb1.aol.com> <8qis99$nef$3@sshuraab-i-1.production.compuserve.com> <jvyyrzubevmbagrfvasbezngvpnpbz.g1dbh80.pminews@news.wanadoo.es> <8qk1gl$l92$1@newssvr05-en0.news.prodigy.com>`

```


Terry Heinze wrote:

> Even in a batch program, I don't use the STOP RUN statement anymore.  It
> doesn't hurt using it for a calling program, but using it in a called
…[4 more quoted lines elided]…
> CONTINUE in a calling program!

I haven't noticed this, and use GOBACK in both programs.  I do get warnings
saying that GOBACK is an IBM extension which may not be supported in the future.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 9)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-09-26T00:34:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qpcj9$29kc$1@newssvr05-en0.news.prodigy.com>`
- **References:** `<20000922223742.23666.00000322@ng-ca1.aol.com> <20000922233236.27190.00000456@ng-fb1.aol.com> <8qis99$nef$3@sshuraab-i-1.production.compuserve.com> <jvyyrzubevmbagrfvasbezngvpnpbz.g1dbh80.pminews@news.wanadoo.es> <8qk1gl$l92$1@newssvr05-en0.news.prodigy.com> <39CF761B.D0C8D91@brazee.net>`

```

GOBACK is safe to use for both calling and called programs.  A drawback of
using GOBACK instead of EXIT PROGRAM in a called program is that if it's the
last statement of a performed paragraph, the GOBACK will generate a warning
that the "performed paragraph cannot reach it's exit."  An EXIT PROGRAM in
this same situation won't.  Granted, it's only a warning message, but I try
to eliminate as many informational and warning messages as possible.  Makes
it easier for the next maintenance programmer.  This has been my experience
with COBOL II in an IBM mainframe environment.  Your mileage may vary!
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CF755D.E02BAA9F@brazee.net>`
- **References:** `<20000922223742.23666.00000322@ng-ca1.aol.com> <20000922233236.27190.00000456@ng-fb1.aol.com> <8qis99$nef$3@sshuraab-i-1.production.compuserve.com>`

```


Russell Styles wrote:

>     For those of us with little mainframe experience, or CICS for
> that matter,
> why is stop run frowned on.  On a pc, it can be used for the same
> purposes that abend is used for on mainframes - to get someone's
> attention.

Mainframes have pretty much disabled such behavior.  I remember using
CALL EXIT to make sure when the program ended, it didn't have any effect
on other processes.  In the early days of multi-tasking, you could do
things which reminds one of working with Windows or Macs, where one
application could stop other unrelated applications.

Also, many on-line systems are actually a shell program which load CoBOL
programs as modules.  Historically, they had problems with STOP RUNs as
well.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 5)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-09-23T04:03:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000923000306.22224.00000501@ng-fx1.aol.com>`
- **References:** `<20000922233236.27190.00000456@ng-fb1.aol.com>`

```
>From: frlsfly@aol.com  (FRLSFLY)
>Date: 9/22/00 11:32 PM Eastern Daylight Time

>
>I would also like to note that people who promiscuously call "stop run" in
…[7 more quoted lines elided]…
>"Big Endian" is what I like.

Only their heads???!!!  I'd nail various other body parts as well (VBEG).

As to the other question...

>Eileen, how can you agree with Thand & >Howard
>when Thane despises DECLARATIVES >and Howard
>uses them, uses FILE STATUS a little >more and uses neither much?

I don't despise DECLARATIVES - I don't use them because I've had mucho trouble
with them (although the discussion here is making some of it a bit clearer) I
much prefer checking a FILE STATUS.  As for Howard - I'm agreeing with him that
an abend - especially in a big iron shop - is sometimes more desirous then a
clean get away via DECLARATIVES and FILE STATUS.

Each has its uses.

Eileen
```

##### ↳ ↳ Re: Use of declaratives on file errors

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LgVy5.5100$5p.33238@news2.mia>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com>`

```
Another 'COBOL' programmer who does NOT understand DECLARATIVES.
DECLARATIVES, FILE STATUS, and 'INVALID KEY' are all TOOLS in our
TOOLBAG.

I can write MUCH clearer and more concise code using DECLARATIVES
CORRECTLY in conjunction with the FILE STATUS Values than simply
using FILE STATUS.  Unfortunately, too many programmers today can't even
get a clean compile with a declarative coded, let alone understand how
to use them.


Foodman <foodman123@aol.com> wrote in message
news:8qffb3$h7k$1@nnrp1.deja.com...
> In article <8q9v44$1r1$1@nnrp1.deja.com>,
>   Stefan Meyer <meyerst@my-deja.com> wrote:
…[34 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 2000-09-26T01:22:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39cffa1b.23900973@news1.frb.gov>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <LgVy5.5100$5p.33238@news2.mia>`

```
On Fri, 22 Sep 2000 23:11:09 -0700, mangogwr wrote:


>DECLARATIVES, FILE STATUS, and 'INVALID KEY' are all TOOLS in our
>TOOLBAG.

>I can write MUCH clearer and more concise code using DECLARATIVES
>CORRECTLY in conjunction with the FILE STATUS Values than simply
>using FILE STATUS.  [...]

I think you hit the nail on the head with the tools/toolbag
description.  The same concept should hold for all of the "IF vs.
EVALUATE" and similar "this vs. that" wars.

I find that for most flat file work, the INVALID KEY and AT END
clauses do an acceptable job, particularly if each file has only one
read or write procedure which is performed where needed.

I nearly always assign a FILE STATUS item for each file, even if I
don't reference it.  It can sometimes provide valuable information in
the memory dump of a failed program.

Where things get more complex, such as when there likely would be any
of several values for FILE STATUS as the result of an I/O operation,
then a DECLARATIVES procedure is frequently a good place to evaluate
this.  It must be kept in mind, however, that implementations vary as
to which of the implementor defined values for the FILE STATUS item
are considered "errors" in determining whether or not to invoke the
declarative error procedure.
```

###### ↳ ↳ ↳ Re: Use of declaratives on file errors

_(reply depth: 4)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-09-26T01:00:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qpbs9$nvb$2@sshuraab-i-1.production.compuserve.com>`
- **References:** `<8q9v44$1r1$1@nnrp1.deja.com> <8qffb3$h7k$1@nnrp1.deja.com> <LgVy5.5100$5p.33238@news2.mia> <39cffa1b.23900973@news1.frb.gov>`

```

WDS <WDS@WDS.WDS.5> wrote in message
news:39cffa1b.23900973@news1.frb.gov...
> On Fri, 22 Sep 2000 23:11:09 -0700, mangogwr wrote:
>
>
> >DECLARATIVES, FILE STATUS, and 'INVALID KEY' are all TOOLS in
our
> >TOOLBAG.
>
> >I can write MUCH clearer and more concise code using
DECLARATIVES
> >CORRECTLY in conjunction with the FILE STATUS Values than
simply
> >using FILE STATUS.  [...]
>
> I think you hit the nail on the head with the tools/toolbag
> description.  The same concept should hold for all of the "IF
vs.
> EVALUATE" and similar "this vs. that" wars.
>
> I find that for most flat file work, the INVALID KEY and AT END
> clauses do an acceptable job, particularly if each file has
only one
> read or write procedure which is performed where needed.
>

    I don't know about other COBOLs, but MERANT cobol on
the pc assumes that you know what you are doing if you define
a file status, and does NOT stop run/abend after an error.


> I nearly always assign a FILE STATUS item for each file, even
if I
> don't reference it.  It can sometimes provide valuable
information in
> the memory dump of a failed program.
>
> Where things get more complex, such as when there likely would
be any
> of several values for FILE STATUS as the result of an I/O
operation,
> then a DECLARATIVES procedure is frequently a good place to
evaluate
> this.  It must be kept in mind, however, that implementations
vary as
> to which of the implementor defined values for the FILE STATUS
item
> are considered "errors" in determining whether or not to invoke
the
> declarative error procedure.
>
> --
> Reply Addr:-->WDavid dot Simon at ATL dot frb dot org<--
> -------------------Decoy@Spammer.Trasher----------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
