[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus COBOL problem

_6 messages · 5 participants · 1996-07 → 1996-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus COBOL problem

- **From:** "robert harrison" <ua-author-90045@usenetarchives.gap>
- **Date:** 1996-07-31T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bb7fdf$362bdf20$5d0c40ce@admin.inetport.com>`

```

I'm using MF-COBOL on an HP9000 system (HPUX). What I'm trying to do is
call a C routine (or just execute a unix command line) from within the
COBOL program. So far, have been unsuccessful. Can anyone point me in the
right direction or just tell where else I might ask the question to get
some answere? Thanks.
```

#### ↳ Re: MicroFocus COBOL problem

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-07-31T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e396dfeae0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bb7fdf$362bdf20$5d0c40ce@admin.inetport.com>`
- **References:** `<01bb7fdf$362bdf20$5d0c40ce@admin.inetport.com>`

```

Robert Harrison wrote:
› I'm using MF-COBOL on an HP9000 system (HPUX). What I'm trying to do is
› call a C routine (or just execute a unix command line) from within the
› COBOL program. So far, have been unsuccessful.

Calling a C program:

CALL "cprog" USING BY VALUE 106 SIZE 4, BY REFERENCE "Hello from COBOL" & x"00"
DISPLAY RETURN-CODE

.....

int
cprog(int value, char *string)
{
printf("From COBOL: %d, %s\n", value, string);
return 99;
}

You need the C functions linked into a COBOL RTS for them to be visible to COBOL :

cob -xo myrts cprog.c -e ""
cob -i cobolprog.cbl
./myrts cobolprog.int

OR

cob -x cobolprog.cbl cprog.c
./cobolprog

Excuting a Unix command :

CALL "SYSTEM" USING "ls -l" & x"00"

One thing that may have and effect is the COBSW=-e switch. This disables COBOL
from being able to "see" the C environment, so you would not be able to call C
functions or have COBOL "EXTERNAL" variables map onto C externs. So make sure
it's not switched on. If you still have no luck, mail me with a demo.

[which reminds me - I have a couple of outstanding things to look at from various
people - I still have your questions logged, but if you're in dire need of urgent
help I suggest you contact your Technical Support rep and get something official
pushed through 'cause it's a busy time right now. I will get around to looking at
everything sent to me though ...]

Cheers,
Kev.
```

##### ↳ ↳ Re: MicroFocus COBOL problem

- **From:** "dan jalbert" <ua-author-17086160@usenetarchives.gap>
- **Date:** 1996-08-04T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e396dfeae0-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e396dfeae0-p2@usenetarchives.gap>`
- **References:** `<01bb7fdf$362bdf20$5d0c40ce@admin.inetport.com> <gap-e396dfeae0-p2@usenetarchives.gap>`

```

Kevin,

I'm also trying to mix C and Cobol under AIX. Calling C from Cobol and vice versa is working okay but
I'm having trouble with the debugger. If I start dbx, set a break point in the C code, and go the animator
comes up fine. The trouble starts when I "go" in the animator. Either the terminal freezes or I get an
interesting display where the screen looks something like:

(dbx)
(dbx)
(dbx)
(dbx) ...

HAny suggestions for working through this?

thanks!
Dan Jalbert

p.s. Are there any news groups specifically dedicated to MicroFocus Cobol?
›
›
```

###### ↳ ↳ ↳ Re: MicroFocus COBOL problem

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-08-05T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e396dfeae0-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e396dfeae0-p3@usenetarchives.gap>`
- **References:** `<01bb7fdf$362bdf20$5d0c40ce@admin.inetport.com> <gap-e396dfeae0-p2@usenetarchives.gap> <gap-e396dfeae0-p3@usenetarchives.gap>`

```

Dan Jalbert wrote:
› 
› Kevin,
 
› Hello Dan.
 
›         I'm also trying to mix C and Cobol under AIX.  Calling C from Cobol and vice versa is working okay but
› I'm having trouble with the debugger.  If I start dbx, set a break point in the C code, and go the animator
…[8 more quoted lines elided]…
› HAny suggestions for working through this?

You seem to be suffering from the Animator and DBX fighting over the terminal
mode they both prefer. The best solution would probably be cross-process
animation. There's a chapter devoted to it in the Toolbox Operating Guide.
You set it up something like this :

screen 1:
COBANIM_2=ANIMATOR
export COBANIM_2
COBSW=+A
export COBSW


- you should see a message along the lines of "waiting for animated program to
start".

screen 2:
COBANIM_2=ANIMATED
export COBANIM_2
COBSW=+A
export COBSW


- When entered, the animator in this process will talk to the animator in the
other process, which will act just as a user-interface. DBX will use this screen
as normal, so the two debuggers will not be fighting with screen modes.

Obviously, the best environment to be using this is X or something where both
"screens" are just windows on the same monitor - you have to swap between windows
as the different debuggers become active.

If you don`t get any luck, shout again - I didn't get a chance to quickly try it
out today, but that's the idea behind the cross-session animation stuff anyway.

› p.s. Are there any news groups specifically dedicated to MicroFocus Cobol?

No, but there are several Micro Focus people who monitor this group, so this is
as good a place to post as anywhere. There's a dedicated compuserve forum though,
but I'm not sure if any of the Unix people read that (I know I don't! :)).

Cheers, Kev.
```

###### ↳ ↳ ↳ Re: MicroFocus COBOL problem

_(reply depth: 4)_

- **From:** "joan colley" <ua-author-15559010@usenetarchives.gap>
- **Date:** 1996-08-06T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e396dfeae0-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e396dfeae0-p4@usenetarchives.gap>`
- **References:** `<01bb7fdf$362bdf20$5d0c40ce@admin.inetport.com> <gap-e396dfeae0-p2@usenetarchives.gap> <gap-e396dfeae0-p3@usenetarchives.gap> <gap-e396dfeae0-p4@usenetarchives.gap>`

```

Kevin Digweed wrote:
› 
› Dan Jalbert wrote:
…[61 more quoted lines elided]…
› STUFF FOR SALE: Here!

Hi Kev and Dan

Would it be a workable solution to use `dbx -a pid` to attach to a running process from
a separate tty?

Joan.
```

#### ↳ Re: MicroFocus COBOL problem

- **From:** "skyw..." <ua-author-17071604@usenetarchives.gap>
- **Date:** 1996-08-01T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e396dfeae0-p6@usenetarchives.gap>`
- **In-Reply-To:** `<01bb7fdf$362bdf20$5d0c40ce@admin.inetport.com>`
- **References:** `<01bb7fdf$362bdf20$5d0c40ce@admin.inetport.com>`

```

"Robert Harrison" wrote:

Calling "C" routine is different than calling a shell command.

Calling "C" modues.

All you have to do is get a clean compile and link it your cobol
program and everything will work. If you want your animator to make
use of "C" code, recreate a RTS32 with the new object.

Calling "Unix command" is easy.
Use following format
call "system" using parm-val.

define parm-val as x(100).
The catch here is you need to null terminate the parm.

For example if you want to cat x.log,
STRING "cat x.log" X"00" delimited by size into parm-val.
call "system" using parm-val.


› I'm using MF-COBOL on an HP9000 system (HPUX).  What I'm trying to do is
› call a C routine (or just execute a unix command line) from within the
› COBOL program.  So far, have been unsuccessful.  Can anyone point me in the
› right direction or just tell where else I might ask the question to get
› some answere?  Thanks.


Disclaimer : If my employer shares my views,
I will be surprised
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
