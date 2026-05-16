[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Revised Index versus Subscript

_8 messages · 3 participants · 2007-09_

---

### Revised Index versus Subscript

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-09-26T15:55:59+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fddodk$i23$00$1@news.t-online.com>`

```
While the original is getting buried with OT.

I really, really tried to keep away from this subject but ...
One of the problems with the speed2 prog is the
attempt to deduce the perform cost.
Now OC produces exactly the C code that reflects
the statements eg.
  /* speed2.cob:63: PERFORM */
  {
    for (n0 = ((int)COB_BSWAP_32(*(int *)(b_18 + 30))); n0 > 0; n0--)
      {
        {
          /* speed2.cob:64: EXIT */
          {
            goto l_5;
          }
        }

        /* EXIT PERFORM CYCLE 5: */
        l_5:;
      }
  }

(For those not informed, OpenCobol produces intermedaite C code)

BUT gcc (in current versions) is far more
clever and deletes the whole thing :-)

Revised test prog -
(This should be compatible with most compilers)

       identification division.
       program-id. speed5.
       data division.
       working-storage section.
       01  comp5-number      comp-5          pic s9(09).
       01  s-subscript       binary          pic s9(09).
       01  repeat-factor value 900000000 comp-5 pic s9(09).
       01  test-byte                         pic  x(01).

       01  misaligned-area.
           05  array-element occurs 4096 indexed x-index.
               10  misaligned-number    comp-5   pic s9(09).
               10  to-cause-misalignment         pic  x(01).
           05  byte-element occurs 4096 indexed x-index-1 pic x.

       procedure division.

           initialize misaligned-area

           display "Start prog   " function current-date
           set x-index to 1000
           display "Index start  " function current-date
           perform repeat-factor times
               if  x-index = 1000
                   set x-index up by 1
               else
                   set x-index down by 1
               end-if
               move array-element (x-index) to test-byte
           end-perform
           display "Index end    " function current-date

           move 1000 to s-subscript
           display "COMP start   " function current-date
           perform repeat-factor times
               if  s-subscript = 1000
                   add 1 to s-subscript
               else
                   subtract 1 from s-subscript
               end-if
               move array-element (s-subscript) to test-byte
           end-perform
           display "COMP end     " function current-date

           move 1000 to comp5-number
           display "COMP-5 start " function current-date
           perform repeat-factor times
               if  comp5-number = 1000
                   add 1 to comp5-number
               else
                   subtract 1 from comp5-number
               end-if
               move array-element (comp5-number) to test-byte
           end-perform
           display "COMP-5 end   " function current-date

           set x-index-1 to 1000
           display "Index start  " function current-date
           perform repeat-factor times
               if  x-index-1 = 1000
                   set x-index-1 up by 1
               else
                   set x-index-1 down by 1
               end-if
               move byte-element (x-index-1) to test-byte
           end-perform
           display "Index end    " function current-date

           move 1000 to s-subscript
           display "COMP start   " function current-date
           perform repeat-factor times
               if  s-subscript = 1000
                   add 1 to s-subscript
               else
                   subtract 1 from s-subscript
               end-if
               move byte-element (s-subscript) to test-byte
           end-perform
           display "COMP end     " function current-date

           move 1000 to comp5-number
           display "COMP-5 start " function current-date
           perform repeat-factor times
               if  comp5-number = 1000
                   add 1 to comp5-number
               else
                   subtract 1 from comp5-number
               end-if
               move byte-element (comp5-number) to test-byte
           end-perform
           display "COMP-5 end   " function current-date

           stop run.

Note that the repeat count is pushed up, otherwise the results are
statistically meaningless.Tests repeated 5 times with +- 1/100 second
difference.

Results from Linux boxen (in single-user mode)
(As all benchmarks should be done on 'nix systems)
(32 bit is P4 prescott with 3.2GhZ)
(64 bit is P4 650 3.4 GhZ)

MF SE 2.2 (Linux x86 32 bit)
cob -u -O -C notrunc -C sourceformat=free speed5.cob
cobrun speed5
Start prog   2007092612363397+0200
Index start  2007092612363397+0200
Index end    2007092612363681+0200
COMP start   2007092612363681+0200
COMP end     2007092612364047+0200
COMP-5 start 2007092612364047+0200
COMP-5 end   2007092612364361+0200
Index start  2007092612364361+0200
Index end    2007092612364672+0200
COMP start   2007092612364672+0200
COMP end     2007092612365034+0200
COMP-5 start 2007092612365034+0200
COMP-5 end   2007092612365357+0200

OC 0.33 current -
cobc -x -O2 -std=mf -free speed5.cob
./speed5
Start prog   2007092612311407+0200
Index start  2007092612311407+0200
Index end    2007092612311690+0200
COMP start   2007092612311690+0200
COMP end     2007092612312044+0200
COMP-5 start 2007092612312044+0200
COMP-5 end   2007092612312326+0200
Index start  2007092612312326+0200
Index end    2007092612312609+0200
COMP start   2007092612312609+0200
COMP end     2007092612312963+0200
COMP-5 start 2007092612312963+0200
COMP-5 end   2007092612313246+0200

OC 0.33 current on Linux x86_64 (64 bit)
cobc -x -O2 -std=mf -free speed5.cob
./speed5
Start prog   2007092612285455+0200
Index start  2007092612285455+0200
Index end    2007092612285602+0200
COMP start   2007092612285602+0200
COMP end     2007092612285855+0200
COMP-5 start 2007092612285855+0200
COMP-5 end   2007092612290004+0200
Index start  2007092612290004+0200
Index end    2007092612290135+0200
COMP start   2007092612290135+0200
COMP end     2007092612290366+0200
COMP-5 start 2007092612290366+0200
COMP-5 end   2007092612290497+0200

Now as to what has all been said in this thread, then I have the
following comments -
COMP (aka BINARY) is stored as big-endian by all
compilers these days.
Therefore there is a penalty on little-endian machines
(or better the OS/firmware for eg. bi-endian) to
byte-swap, operate and re-byteswap results.
This, of course, affects eg. x86(_64).
However, see below

Alignment -
There are in fact not that many alignment tolerant machines there.
Intel x86(_64) and Power PC are known. (The Itanium is not)
This means that any reference to a COMP/COMP-5 item must
be moved to an intermediate area unless it can be proved at compile
time that it is appropiately aligned. (eg. at 01 level)

So we have to look at a bisection of the above two attributes.
Generally speaking, for performance, (other than INDEX)
one should use COMP-5 (aka BINARY-LONG SIGNED/UNSIGNED)
for subscripts/counters etc. and define them at the 01 level.

Not only that, a particular compiler implementation has it's
own INDEX definition which is somewhat difficult to ascertain.
(And which is not necessarily a C-5 item)

Roger
```

#### ↳ Re: Revised Index versus Subscript

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-09-26T16:14:19+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fddpg5$1j9$03$1@news.t-online.com>`
- **References:** `<fddodk$i23$00$1@news.t-online.com>`

```
Note that on big-endian boxen, COMP == COMP-5 which
I did not make clear in my post.

What it all comes down to is: can you define
a subscript equivalent to an index with the attributes that apply to this
specific implemenation on this specific hardware?

And regards asm instructions -
Mostly compiler producers release according to
a platform and a OS release.
MF releases on a LCD (least common demoninator) from
supported platforms.

This means that MF does not (and can not) use eg SSE stuff
unless it is specifically targeted/required.

Roger

"Roger While" <simrw@sim-basis.de> schrieb im Newsbeitrag 
news:fddodk$i23$00$1@news.t-online.com...
> While the original is getting buried with OT.
>
…[213 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Revised Index versus Subscript

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-26T20:29:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2q1mf3t9mjvlfrpnijijm1vgea6tb5ss0t@4ax.com>`
- **References:** `<fddodk$i23$00$1@news.t-online.com> <fddpg5$1j9$03$1@news.t-online.com>`

```
On Wed, 26 Sep 2007 16:14:19 +0200, "Roger While" <simrw@sim-basis.de> wrote:

>Note that on big-endian boxen, COMP == COMP-5 which
>I did not make clear in my post.
…[12 more quoted lines elided]…
>unless it is specifically targeted/required.

BSWAP is not an SSE instruction. It has been available on every Intel since '486.
```

###### ↳ ↳ ↳ Re: Revised Index versus Subscript

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-09-28T13:24:14+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fdio95$qpg$00$1@news.t-online.com>`
- **References:** `<fddodk$i23$00$1@news.t-online.com> <fddpg5$1j9$03$1@news.t-online.com> <2q1mf3t9mjvlfrpnijijm1vgea6tb5ss0t@4ax.com>`

```

"Robert" <no@e.mail> schrieb im Newsbeitrag 
news:2q1mf3t9mjvlfrpnijijm1vgea6tb5ss0t@4ax.com...
> On Wed, 26 Sep 2007 16:14:19 +0200, "Roger While" <simrw@sim-basis.de> 
> wrote:
…[18 more quoted lines elided]…
> since '486.

I never said the above.
Both OC and MF use bswap.
```

#### ↳ Re: Revised Index versus Subscript

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-26T20:24:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nvtlf3hflf9ispjjcjmha203ml6fa8s7h2@4ax.com>`
- **References:** `<fddodk$i23$00$1@news.t-online.com>`

```
On Wed, 26 Sep 2007 15:55:59 +0200, "Roger While" <simrw@sim-basis.de> wrote:

>While the original is getting buried with OT.
>
…[24 more quoted lines elided]…
>clever and deletes the whole thing :-)

Micro Focus did the same when the loop was empty or contained only CONTINUE. I added exit
perform cycle to stop it from optimizing out the null loop. Since that didn't do the trick
with OC, you should have found SOMEthing that made it run the null loop repeat-count
times. Failing to measure and then subtract loop control time distorts the relative speeds
reported. 

Suppose loop control takes 5 time units, index takes 5 and subscript takes 10. The program
should report that subscript takes twice as long (10/5). Without discounting loop control,
it will report 1.5 times as long (15/10). 


>Results from Linux boxen (in single-user mode)
>(As all benchmarks should be done on 'nix systems)
…[5 more quoted lines elided]…
>cobrun speed5

>Index start  2007092612363397+0200
>Index end    2007092612363681+0200    3.3 - .5 / .9  = 3.1
…[3 more quoted lines elided]…
>COMP-5 end   2007092612364361+0200  3.1                  2.9

>OC 0.33 current -
>cobc -x -O2 -std=mf -free speed5.cob
>./speed5

>Index start  2007092612311407+0200
>Index end    2007092612311690+0200    2.8 - .5 / .9 = 2.6
…[3 more quoted lines elided]…
>COMP-5 end   2007092612312326+0200  2.1                1.8

You removed the null loop and computation of test time. The machines are called COMPUTERS
because they're good at COMPUTING. There's no reason to make the human do it.

Above I subtracted an estimated .5 for loop control and adjusted for 9/10 difference in
repeat factor. OC is 38% faster than MF for tests 1 and 3, which use native integers, only
slightly faster on test 2, which uses a big-endian integer.

>Now as to what has all been said in this thread, then I have the
>following comments -
…[4 more quoted lines elided]…
>byte-swap, operate and re-byteswap results.

The byte swap can be done with a single instruction: BSWAP. GCC has a very smart
optimizer, yet doesn't seem to be using that instruction. I would inspect generated code
to see what's going on. 

My guess would be it's doing the byte swap in C rather than machine language.  Something
like (((LongNumber&0x000000FF)<<24)+((LongNumber&0x0000FF00)<<8)+
   ((LongNumber&0x00FF0000)>>8)+((LongNumber&0xFF000000)>>24

>This, of course, affects eg. x86(_64).
>However, see below
…[6 more quoted lines elided]…
>time that it is appropiately aligned. (eg. at 01 level)

That's why the original had SYNC on critical integers.

>So we have to look at a bisection of the above two attributes.
>Generally speaking, for performance, (other than INDEX)
…[5 more quoted lines elided]…
>(And which is not necessarily a C-5 item)

It's EASY to ascertain. Set a data item of type index to the table-oriented index,
redefine as comp-5 and display.
```

##### ↳ ↳ Re: Revised Index versus Subscript

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-09-28T13:21:51+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fdio4p$qge$00$1@news.t-online.com>`
- **References:** `<fddodk$i23$00$1@news.t-online.com> <nvtlf3hflf9ispjjcjmha203ml6fa8s7h2@4ax.com>`

```
"Robert" <no@e.mail> schrieb im Newsbeitrag 
news:nvtlf3hflf9ispjjcjmha203ml6fa8s7h2@4ax.com...
> On Wed, 26 Sep 2007 15:55:59 +0200, "Roger While" <simrw@sim-basis.de> 
> wrote:
…[126 more quoted lines elided]…
> redefine as comp-5 and display.

Really ?
Ever heard about 64 bit index?
How do you redefine (compatibly) an index ?

Roger
```

###### ↳ ↳ ↳ Re: Revised Index versus Subscript

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-28T12:05:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m40qf3luuhibfrod9cf5u5d8k520cqaj32@4ax.com>`
- **References:** `<fddodk$i23$00$1@news.t-online.com> <nvtlf3hflf9ispjjcjmha203ml6fa8s7h2@4ax.com> <fdio4p$qge$00$1@news.t-online.com>`

```
On Fri, 28 Sep 2007 13:21:51 +0200, "Roger While" <simrw@sim-basis.de> wrote:

>"Robert" <no@e.mail> schrieb im Newsbeitrag 
>news:nvtlf3hflf9ispjjcjmha203ml6fa8s7h2@4ax.com...
>> On Wed, 26 Sep 2007 15:55:59 +0200, "Roger While" <simrw@sim-basis.de> 

>>>
>>>Not only that, a particular compiler implementation has it's
…[9 more quoted lines elided]…
>How do you redefine (compatibly) an index ?

01  an-index     usage  index.
01  an-iindex-redefined redefines an-index usage binary-double.

set an-index to table-index
display an-index-redefined
```

###### ↳ ↳ ↳ Re: Revised Index versus Subscript

_(reply depth: 4)_

- **From:** Robert Jones <rjones0@hotmail.com>
- **Date:** 2007-09-28T10:46:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1191001576.856733.203450@w3g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<m40qf3luuhibfrod9cf5u5d8k520cqaj32@4ax.com>`
- **References:** `<fddodk$i23$00$1@news.t-online.com> <nvtlf3hflf9ispjjcjmha203ml6fa8s7h2@4ax.com> <fdio4p$qge$00$1@news.t-online.com> <m40qf3luuhibfrod9cf5u5d8k520cqaj32@4ax.com>`

```
On Sep 28, 6:05 pm, Robert <n...@e.mail> wrote:
> On Fri, 28 Sep 2007 13:21:51 +0200, "Roger While" <si...@sim-basis.de> wrote:
> >"Robert" <n...@e.mail> schrieb im Newsbeitrag
…[19 more quoted lines elided]…
> display an-index-redefined

While it may seem reasonable to assume that a data item with usage
index has the same format as the index that is actually associated
with the table from which it has been derived with a SET statement, an
implementor is not bound to do this.  For example in a small table in
an IBM mainframe compiler the actual index could be a binary halfword,
if that is big enough to do the job.  A compiler's optimiser might
well do this.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
