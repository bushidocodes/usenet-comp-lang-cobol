[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol fo Unix

_17 messages · 10 participants · 2005-12 → 2006-01_

---

### Cobol fo Unix

- **From:** Michael Russell <Michael.Russell@msn.com>
- **Date:** 2005-12-25T11:12:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net>`

```
Hi,

Anyone like to volunteer info on what they think is the least expensive 
Cobol for Unix?
This is as regards run-time licences - a confusing area, I know!

If we take Micro Focus as 'the benchmark Cobol', for functionality,
then 'least expensive' shouldn't mean seriously less functionality when 
compared with MF.

(Except - I'm not bothered about availability of SQL (odd, I know))

Happy Christmas-time!

Michael
```

#### ↳ Re: Cobol fo Unix

- **From:** "Bruintje Beer" <me@knoware.nl>
- **Date:** 2005-12-26T08:35:11+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43af9d28$0$724$5fc3050@dreader2.news.tiscali.nl>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net>`

```

"Michael Russell" <Michael.Russell@msn.com> schreef in bericht 
news:43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net...
> Hi,
>
…[13 more quoted lines elided]…
>

look for

tiny cobol
COBOL For GCC

John
```

#### ↳ Re: Cobol fo Unix

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-12-26T10:47:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1135622862.727599.66730@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net>`

```
> If we take Micro Focus as 'the benchmark Cobol', for functionality,
> then 'least expensive' shouldn't mean seriously less functionality when
> compared with MF.

Then the 'least expensive' will be MicroFocus.

MF has a large number of extensions primarily to ensure lock in. If
those functions are important then you are locked in.

It may also what you mean by 'Unix'. There are free and cheap Cobols
that run on Linux, but not necessarily the Unix you want.
```

#### ↳ Re: Cobol fo Unix

- **From:** "Sergey Kashyrin" <ska@resqnet.com>
- **Date:** 2005-12-28T23:34:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bHJsf.36$Ic5.194629@news.sisna.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net>`

```
Michael,

If you don't need object cobol, check opencobol.org.
Soon will be working on solaris-64bit, aix5.3-64bit and hpux11.11-64bit
My understanding that it's already working on linux
SQL should be covered by preprocessors. At least working with Oracle, UDB 
and Sybase.

Regards,
Sergey

"Michael Russell" <Michael.Russell@msn.com> wrote in message 
news:43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net...
> Hi,
>
…[13 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol fo Unix

- **From:** Michael Russell <Michael.Russell@msn.com>
- **Date:** 2005-12-29T19:25:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43b43833$0$27881$ed9e5944@text-readers.news.pipex.net>`
- **In-Reply-To:** `<bHJsf.36$Ic5.194629@news.sisna.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net> <bHJsf.36$Ic5.194629@news.sisna.com>`

```
Thank you, Sergey.

Michael

Sergey Kashyrin wrote:

>Michael,
>
…[34 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol fo Unix

- **From:** "Erez" <moonbuzz@gmail.com>
- **Date:** 2006-01-02T07:32:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1136215961.283415.191000@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<bHJsf.36$Ic5.194629@news.sisna.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net> <bHJsf.36$Ic5.194629@news.sisna.com>`

```
I've just installed OpenCOBOL on GNU/Linux (Ubuntu), and I've been
getting the following error when attempting to run a program: error
while loading shared libraries: libcob.so.1: cannot open shared object
file: No such file or directory

Any ideas what causing it? I've googled this message and came with
several others asking for it, but no answers,

TIA, Erez
```

###### ↳ ↳ ↳ Re: Cobol fo Unix

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-01-02T11:37:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1136230643.174032.95200@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<1136215961.283415.191000@z14g2000cwz.googlegroups.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net> <bHJsf.36$Ic5.194629@news.sisna.com> <1136215961.283415.191000@z14g2000cwz.googlegroups.com>`

```
>  error while loading shared libraries: libcob.so.1: cannot open
> shared object file: No such file or directory

libcob.so.1 needs to be on your LD_LIBRARY_PATH. It should have been
copied into your /usr/local/lib directory and this should be in your
LD_LOAD_LIBRARY. If you did not install as root then it may not have
copied it there.

You may be able to simply add ~/??/open-cobol-0.31/libcob/.libs to your
library path and have it used from there:

LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:open-cobol-0.31/libcob/.libs
export LD_LIBRARY_PATH
runprogram
```

###### ↳ ↳ ↳ Re: Cobol fo Unix

_(reply depth: 4)_

- **From:** "Erez" <moonbuzz@gmail.com>
- **Date:** 2006-01-04T22:48:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1136443694.933677.181470@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1136230643.174032.95200@z14g2000cwz.googlegroups.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net> <bHJsf.36$Ic5.194629@news.sisna.com> <1136215961.283415.191000@z14g2000cwz.googlegroups.com> <1136230643.174032.95200@z14g2000cwz.googlegroups.com>`

```
Thanks for the reply, I would appreciate if you give me some further
information, as I've no idea how to add stuff to my library path.

I installed it as root, and just did a reinstallation, as root, just to
make sure, but it still runs the same error.
```

###### ↳ ↳ ↳ Re: Cobol fo Unix

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-01-04T23:40:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1136446835.108331.38980@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1136443694.933677.181470@g14g2000cwa.googlegroups.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net> <bHJsf.36$Ic5.194629@news.sisna.com> <1136215961.283415.191000@z14g2000cwz.googlegroups.com> <1136230643.174032.95200@z14g2000cwz.googlegroups.com> <1136443694.933677.181470@g14g2000cwa.googlegroups.com>`

```
> Thanks for the reply, I would appreciate if you give me some further
> information, as I've no idea how to add stuff to my library path.

> I installed it as root, and just did a reinstallation, as root, just to
> make sure, but it still runs the same error.

As root run:

updatedb

(this may take some time) which builds a database of all files on the
system.  When complete enter command (you don't need to be root):

locate libcob .so

This will list all the files with libcob.so in the path or name.

To find what your current library path is use the set command and the
grep command:

set | grep LD_LIBRARY_PATH

If the paths do not include the location of the libcob.so.1 then make a
shell script file:

vi run.sh       (or use your favourite editor)
----------------------------------------------------------
#!/bin/sh

LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:path
export LD_LIBRARY_PATH

yourprogramname

-----------------------------------------------------------

where 'path' is where libcob.so.1 is
           'yourprogramname' is your program name

run this with:

sh run.sh
```

###### ↳ ↳ ↳ Re: Cobol fo Unix

_(reply depth: 6)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-01-06T15:45:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dpm3an02l2s@news1.newsguy.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net> <1136446835.108331.38980@g14g2000cwa.googlegroups.com>`

```

In article <1136446835.108331.38980@g14g2000cwa.googlegroups.com>, "Richard" <riplin@Azonic.co.nz> writes:
> Erez <moonbuzz@gmail.com>
> > Thanks for the reply, I would appreciate if you give me some further
> > information, as I've no idea how to add stuff to my library path.

That's a rather basic task - it's just a matter of changing the
value of an environment variable.  If you don't know how to do that,
you really need to read a primer for the shell you're using, and
probably one for Unix in general or the flavor you're running..

> > I installed it as root, and just did a reinstallation, as root, just to
> > make sure, but it still runs the same error.

Randomly stumbling around using the superuser account is a good way
to ruin your OS installation.

> To find what your current library path is use the set command and the
> grep command:
> 
> set | grep LD_LIBRARY_PATH

Not the best idiom, I think, since the "set" command is a builtin in
some, but not all, shells.  In some, notably csh and its derivatives,
it's a builtin that has a different function.  (While I don't
recommend csh, there are still people who use it.)

The "env" command is external, and should work in all shells, but even

   env | grep LD_LIBRARY_PATH

is unnecessarily complex.  I'd just echo the value of the variable:

   echo $LD_LIBRARY_PATH

That works in every shell I've used.

Note that while LD_LIBRARY_PATH contains the shared library path for
most contemporary Unix implementations, it's not universal.  Learning
the Unix (and shell) you're running is really the better plan.

(There are alternatives to the shell script solution Richard
recommends, too, but I suspect they'd just confuse Erez.)
```

###### ↳ ↳ ↳ Re: Cobol fo Unix

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-06T17:01:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dpm7pt$env$1@reader2.panix.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net> <1136446835.108331.38980@g14g2000cwa.googlegroups.com> <dpm3an02l2s@news1.newsguy.com>`

```
In article <dpm3an02l2s@news1.newsguy.com>,
Michael Wojcik <mwojcik@newsguy.com> wrote:

[snip to the .sig]

>(I can't wait till he finds out I replaced
>his toothpaste with A COMPETING BRAND OF TOOTHPASTE!) -- Ryan North

Well, I hate to tell you this... but I am reminded of... A Story!

Back in the Oldene Dayse an expression used to indicate the futility of 
trying to un-do certain tasks was 'you can't put the toothpaste back into 
the tube'.  Modern times have changed that; with the advent of plastic 
toothpaste-tubes one *can* put the toothpaste back... and more.

A decade or so back I visited a buddy o' mine and noticed that he had one 
of these newfangled plastic tubes... but his taste in toothpaste had 
remained unchanged, he was still using Colgate or Crest or whatever brand 
had been imprinted upon him in his youth... but, essentially, the same old 
wine in a new bottle.

The day my visit ended was a workday for him; we made our farewells over 
morning coffee - 'bleargh... been fun... where'za sugar?' - and he went to 
his job.  After waking up a bit I went out to a nearby store and purchased 
a plastic tube of a different toothpaste; I then very carefully dumped out 
his usual brand into the trashcan behind the house and aligned the two 
tubes so I could squeeze out of the new into the old.

The next day he got a brushful of Happy Kiddy Bubble-Gum Flavored Tooth 
Delight.

DD
```

###### ↳ ↳ ↳ Re: Cobol fo Unix

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-01-06T09:13:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dpm8f8$29fd$1@si05.rsvl.unisys.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net> <1136446835.108331.38980@g14g2000cwa.googlegroups.com> <dpm3an02l2s@news1.newsguy.com> <dpm7pt$env$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:dpm7pt$env$1@reader2.panix.com...

> A decade or so back I visited a buddy o' mine and noticed that he had one
> of these newfangled plastic tubes... but his taste in toothpaste had
> remained unchanged, he was still using Colgate or Crest or whatever brand
> had been imprinted upon him in his youth...

Alas, I haven't had much luck finding Ipana lately ...

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Cobol fo Unix

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-06T17:52:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dpmao4$o92$1@reader2.panix.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net> <dpm3an02l2s@news1.newsguy.com> <dpm7pt$env$1@reader2.panix.com> <dpm8f8$29fd$1@si05.rsvl.unisys.com>`

```
In article <dpm8f8$29fd$1@si05.rsvl.unisys.com>,
Chuck Stevens <charles.stevens@unisys.com> wrote:
>
><docdwarf@panix.com> wrote in message news:dpm7pt$env$1@reader2.panix.com...
…[6 more quoted lines elided]…
>Alas, I haven't had much luck finding Ipana lately ...

Gotta love this WorldWide Web thingie...

<http://www.vermontcountrystore.com/jump.jsp?itemID=31408&itemType=PRODUCT&searchid=inceptor>

DD
```

###### ↳ ↳ ↳ Re: Cobol fo Unix

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-01-06T10:24:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dpmckc$2c75$1@si05.rsvl.unisys.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net> <dpm3an02l2s@news1.newsguy.com> <dpm7pt$env$1@reader2.panix.com> <dpm8f8$29fd$1@si05.rsvl.unisys.com> <dpmao4$o92$1@reader2.panix.com>`

```
Amazing!  Thanks, DD!     -CCS

<docdwarf@panix.com> wrote in message news:dpmao4$o92$1@reader2.panix.com...
> In article <dpm8f8$29fd$1@si05.rsvl.unisys.com>,
> Chuck Stevens <charles.stevens@unisys.com> wrote:
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol fo Unix

_(reply depth: 8)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-01-07T16:05:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11s0ep1g1ckon28@news.supernews.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net> <1136446835.108331.38980@g14g2000cwa.googlegroups.com> <dpm3an02l2s@news1.newsguy.com> <dpm7pt$env$1@reader2.panix.com>`

```
docdwarf@panix.com wrote:
> In article <dpm3an02l2s@news1.newsguy.com>,
> Michael Wojcik <mwojcik@newsguy.com> wrote:
…[29 more quoted lines elided]…
> Tooth Delight.

Back in the college dorm days we did the same thing - except it wasn't 
bubble-gum flavored stuff we found hot and steamy on the sidewalk. And, 
contrary to your earlier rememberance, you COULD put toothpaste (or 
something vile) back in the tube. Here's how:

Squeeze out all the remaining proper product and force as much water as you 
can into the flattened tube. Put on the cap.

Place on hot plate. Soon the water boils and the internal pressue forces the 
lead tube to expand to it's original shape. Let cool.

Carefully unfold the un-business end. Pour or pack the new contents into the 
tube. Carefully refold the end flap. Place on sink.

By this time, the twenty or so packages of Gelatin you put in the commode 
should have solidified.

Time to leave.
```

###### ↳ ↳ ↳ Re: Cobol fo Unix

_(reply depth: 9)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-01-08T09:54:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1136742862.002591.6060@g43g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<11s0ep1g1ckon28@news.supernews.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net> <1136446835.108331.38980@g14g2000cwa.googlegroups.com> <dpm3an02l2s@news1.newsguy.com> <dpm7pt$env$1@reader2.panix.com> <11s0ep1g1ckon28@news.supernews.com>`

```

HeyBub wrote:
> docdwarf@panix.com wrote:
> >
…[20 more quoted lines elided]…
> Time to leave.


Love it. Pure evil.
```

###### ↳ ↳ ↳ Re: Cobol fo Unix

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-01-09T10:21:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dptdf4$a4c$1@reader2.panix.com>`
- **References:** `<43ae7eb7$0$27881$ed9e5944@text-readers.news.pipex.net> <dpm3an02l2s@news1.newsguy.com> <dpm7pt$env$1@reader2.panix.com> <11s0ep1g1ckon28@news.supernews.com>`

```
In article <11s0ep1g1ckon28@news.supernews.com>,
HeyBub <heybubNOSPAM@gmail.com> wrote:
>docdwarf@panix.com wrote:
>> In article <dpm3an02l2s@news1.newsguy.com>,
…[11 more quoted lines elided]…
>> back into the tube'.

[snip]

>Back in the college dorm days we did the same thing - except it wasn't 
>bubble-gum flavored stuff we found hot and steamy on the sidewalk. And, 
…[7 more quoted lines elided]…
>lead tube to expand to it's original shape. Let cool.

Ahhhhh... someone went to school with engineers, did he?

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
