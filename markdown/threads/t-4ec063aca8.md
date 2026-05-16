[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress Distribution Question

_5 messages · 3 participants · 1999-05_

---

### NetExpress Distribution Question

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1999-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990514101641.18174.00000442@ng-cq1.aol.com>`

```
Good Morning,

I have recently converted from Version 2.0 to Version 3.0. When i run my
application from inside of the IDE everything works great. When i compile my
application to an EXE and try and run it outside of the IDE i get the following
error message:

Load error: file 'FS_SPLIT_FILENAME'
error code: 173, pc=0, call=1, seg=0
173 Called program file not found in drive/directory

Could someone help me out with what is wrong ?

Thanks,
Bob Hennessey
```

#### ↳ Re: NetExpress Distribution Question

- **From:** Kevin Digweed <ked@mfltd.co.uk>
- **Date:** 1999-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373C42F8.8CBE77DC@mfltd.co.uk>`
- **References:** `<19990514101641.18174.00000442@ng-cq1.aol.com>`

```
Bob7536 wrote:
> Good Morning,
> 
…[9 more quoted lines elided]…
> Could someone help me out with what is wrong ?

Hi Bob.

This is a routine the file handler uses to split the "$$<server-name>"
type of filename. It only tries to call it if it sees that style of
name passed to it. It's actually in the "FHRSUB.OBJ" file which you can
explicitly link in to your app to resolve the call (the routine is
visible to the file handler when running within the IDE by default).

However, you shouldn't see this error as if you're using the
"$$<server-name>" filename syntax you would normally compile with
the directive CALLFH(FHREDIR) and this will cause FHRSUB.OBJ to be
automatically included. You shouldn't have to do this sort of thing
manually, so please raise a bug on it if you aren't doing anything
"unexpected" (for want of a better word).

Cheers, Kev.

PS. Compiling CALLFH(FHREDIR) will also automatically link in
    "FHRDRPWD.OBJ" - you may also want to do that.
```

##### ↳ ↳ Re: NetExpress Distribution Question

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1999-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990514174622.18181.00000546@ng-cq1.aol.com>`
- **References:** `<373C42F8.8CBE77DC@mfltd.co.uk>`

```
Hi Kevin,

Thanks for the reply.  I changed my build settings to link in the "FHRSUB.OBJ"
and the problem has gone away.  I am not using a "$$<server>" type of file
name.  All of my file names are specified as follows:

ASSIGN TO DYNAMIC WS-FILE-NAME.

Then in working storage i have something like
01  ws-file-name            pic x(12)  value "customer.dat".

Also, it appears to start up a DOS application in a seperate window. If i run
my EXE i notice a DOS application being started in another window. Also, if i
do an Ctrl Alt Del I notice a Winoldap is listed.   This has only been since I
had to link in the OBJ.  Any suggestions ?

Thanks,
Bob
```

###### ↳ ↳ ↳ Re: NetExpress Distribution Question

- **From:** philhickling@my-dejanews.com
- **Date:** 1999-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hk81t$8n2$1@nnrp1.deja.com>`
- **References:** `<373C42F8.8CBE77DC@mfltd.co.uk> <19990514174622.18181.00000546@ng-cq1.aol.com>`

```
In article <19990514174622.18181.00000546@ng-cq1.aol.com>,
  bob7536@aol.com (Bob7536) wrote:
>
>
>>> Also, it appears to start up a DOS application in a seperate
window.
If i run
> my EXE i notice a DOS application being started in another window. <<

Hi Bob.  I'm not an expert, so don't quote me.  But I have noticed with
old code that I've ported into NetExpress, that any DISPLAY command
causes the DOS window to be started.  Once I removed all DOS
statements, and used gui DIALOG then the DOS window stopped being
created.

Bye,  Phil Hickling.


--== Sent via Deja.com http://www.deja.com/ ==--
---Share what you know. Learn what you don't.---
```

###### ↳ ↳ ↳ Re: NetExpress Distribution Question

_(reply depth: 4)_

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1999-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990515195509.18177.00001091@ng-cq1.aol.com>`
- **References:** `<7hk81t$8n2$1@nnrp1.deja.com>`

```
Hi Phil,

Thanks for the reply.  This just started when i converted to NetExpress Version
3.0.  I did not have this problem with Version 1 and 2.  It appears to becaused
by the link in of "FHRSUB.OBJ".  I am unsure why I have to link in this module
as it deals with spliting a "$$server-name" type of file name.  Which i am not
using.  Hopefully Kevin will be able to shed some light on this.

Thanks,
Bob Hennessey
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
