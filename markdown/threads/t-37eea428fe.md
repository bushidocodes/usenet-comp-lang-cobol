[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Perform statement question

_8 messages · 5 participants · 1999-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: Perform statement question

- **From:** "Eileen Preston" <epreston@lear.com>
- **Date:** 1999-10-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s80b66e8.004@UTAEMAIL.UTA.COM>`

```
Here the standard is mostly PERFORM THRU.  I use it to GO TO EXIT and yes I've been bit (wrong exit - result - infinate loop at 2am).  Many moons ago when I learned structured programming the GO TO statement was verbotin.  Internal sorts were not allowed because they required a GO TO to skip over the input procedure (well - that's another discussion).  I would prefer just a straight PERFORM as I don't get a lot of calls at 2am as a result but when doing maintenance on some very old code ya go with the flow.

In any event I have found that in CICS programs it is rather hard to avoid the PERFORM THRU and the use of the GO TO EXIT if one uses HANDLE CONDITION instead of response codes.

For those of you not familiar with CICS coding a HANDLE CONDITION tells the program what to do in the case of an 'error' such as a not found in the read of a file.  These end up translating into GO TO statements - so if you don't find the record you're looking for the program will GO TO the paragraph you designate to handle that condition. 

So...
In a CICS program you would code a PERFORM THRU where you perform the read paragraph with a GO TO EXIT after the read (which means you've found the record) followed by the paragraph that does what you want done if you don't find the record, followed by the exit.  Control returns to where you did the initial perform and execution continues.

PERFORM READ-FILE THRU READ-EXIT

READ-FILE.
   EXEC CICS READ 

   GO TO READ-EXIT

RECORD-NOT-FOUND.
   MOVE 'N' TO FOUND-SW

READ-EXIT.
   EXIT.


 Sent via Deja.com http://www.deja.com/
 Before you buy.
```

#### ↳ Re: Perform statement question

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-10-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380BB7AA.7130644A@att.net>`
- **References:** `<s80b66e8.004@UTAEMAIL.UTA.COM>`

```
Eileen Preston wrote:
> 
(snip)
> 
> In any event I have found that in CICS programs it is rather hard to avoid the PERFORM THRU and the use of the GO TO EXIT if one uses HANDLE CONDITION instead of response codes.

So why not omit the "HANDLE CONDITION" commands, code your imperative
commands with RESP(response_field), then EVALUATE your response_field?
Works for me.

Bill Lynch
```

##### ↳ ↳ Re: Perform statement question

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-10-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ugg71$i7c$1@nntp8.atl.mindspring.net>`
- **References:** `<s80b66e8.004@UTAEMAIL.UTA.COM> <380BB7AA.7130644A@att.net>`

```
William Lynch <WBLynch@att.net> wrote in message
news:380BB7AA.7130644A@att.net...
> Eileen Preston wrote:
> >
> (snip)
> >
> > In any event I have found that in CICS programs it is rather hard to
avoid the PERFORM THRU and the use of the GO TO EXIT if one uses HANDLE
CONDITION instead of response codes.
>
> So why not omit the "HANDLE CONDITION" commands, code your imperative
…[3 more quoted lines elided]…
> Bill Lynch

Which is (EVALUATE RESP-field) the current IBM recommendation (I believe).
However, it doesn't  solve the problem of maintaining existing code (which
uses both HANDLE AID and HANDLE CONDITION).
```

###### ↳ ↳ ↳ Re: Perform statement question

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380BF916.422862EC@att.net>`
- **References:** `<s80b66e8.004@UTAEMAIL.UTA.COM> <380BB7AA.7130644A@att.net> <7ugg71$i7c$1@nntp8.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> William Lynch <WBLynch@att.net> wrote in message
…[17 more quoted lines elided]…
> uses both HANDLE AID and HANDLE CONDITION).

Right, so we have to migrate away from the crummy code.

Bill Lynch
```

#### ↳ Re: Perform statement question

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf1a6a$ff87f920$0100007f@vaagshaugen>`
- **References:** `<s80b66e8.004@UTAEMAIL.UTA.COM>`

```
Eileen Preston <epreston@lear.com> wrote in article
<s80b66e8.004@UTAEMAIL.UTA.COM>...
> In any event I have found that in CICS programs it is rather hard to
avoid the PERFORM THRU and the use of the GO TO EXIT if one uses HANDLE
CONDITION instead of response codes.

Then simply don't use it.  HANDLE CONDITION was a bad idea from the CICS
lab.  It is far more safe to code explicit tests on response codes after
each command. I find no trouble at all using single period paragraphs and
avoiding PERFORM THRU and GO TO in CICS programs.

perform Read-file

Read-file.
    exec cics read ... nohandle end-exec
    evaluate EIBRESP
        when DFHRESP(NORMAL) continue
        when DFHRESP(NOTFND) move 'N' to FOUND-SW
        when other perform Error-routine
    end-evaluate
    .

The Error-routine may set return info and do exec cics return.

Gunnar.
```

#### ↳ Re: Perform statement question

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380DD055.9C698078@NOSPAMhome.com>`
- **References:** `<s80b66e8.004@UTAEMAIL.UTA.COM>`

```
Eileen Preston wrote:
> 
>Many moons ago when I learned structured programming the GO TO statement was verbotin. > Internal sorts were not allowed because they required a GO TO to skip over the input 
> procedure (well - that's another discussion).

OK, starting the other discussion.  I have never written an internal
sort with a GO TO.  Why do you need to "skip over the input procedure"?
```

##### ↳ ↳ Re: Perform statement question

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ukng2$9bp$1@nntp4.atl.mindspring.net>`
- **References:** `<s80b66e8.004@UTAEMAIL.UTA.COM> <380DD055.9C698078@NOSPAMhome.com>`

```
NONE of the following applies to the '85 Standard, but if you had a
"strictly" conforming '74 Standard COBOL program with an INPUT or OUTPUT
procedure, you DID need to use the GO TO.  This was because:

A) The Input/Output procedure had to be a Section name

B) It would be "performed" once

C) You could NOT PERFORM anything outside of that Section.

Therefore, you would end-up with logic either like,

 ... Sort ... Input Procedure XYZ

XYZ Section.
    Get your data
   If Not out of input data
     Release your data
     Go to XYZ
    .

       *** or   ***

XYZ Section.
   AAA-Para.
      Perform BBB-Para until whatever
      If Whatever Go To XYZ-EXIT
   BBB-Para.
      do your gets and releases.
XYZ-Exit.
     Exit.

Either you had to use the GO TO to do the loop or you had to use it to avoid
"falling thru" a paragraph after your loop was done.

NOTE: Lots of compilers allowed you to PERFORM something outside the range of
the INPUT/OUTPUT procedure - but that wasn't standard.
```

###### ↳ ↳ ↳ Re: Perform statement question

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380DEB38.C1ACF719@NOSPAMhome.com>`
- **References:** `<s80b66e8.004@UTAEMAIL.UTA.COM> <380DD055.9C698078@NOSPAMhome.com> <7ukng2$9bp$1@nntp4.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> NONE of the following applies to the '85 Standard, but if you had a
…[7 more quoted lines elided]…
> C) You could NOT PERFORM anything outside of that Section.

I guess the compilers I used did not comply with "C)" above.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
