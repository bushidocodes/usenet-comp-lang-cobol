[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Underscore in datanames

_35 messages · 11 participants · 2009-06_

---

### Underscore in datanames

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-10T02:15:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79794vF1pep3iU1@mid.individual.net>`

```
I tripped up recently when processing some client source data definitions.

Looked at it for ages and couldn't see a problem, then realised that certain 
fields had been defined with underscores instead of hyphens in the names. It 
looked like a maintenance programmer had made two sets of amendments to a 
very large record definition (Hundreds of datanames, lots of REDEFINES and 
OCCURS, an absolute delight that caused my Toolset to give up and just 
declare "Too many fields".)  I enlarged the Toolset buffers considerably but 
then it gave the same message from ACCESS and SQL Server when the Toolset 
tried to EXECUTE the DDL it had generated, in order to create an equivalent 
RDB table.

It turned out that the underscores were contributing signally to the 
problem. (Various parsers internal in the Toolset just spat the dummy when 
they found these underscores and this caused duplicate datanames, which 
cannot be added to a RDB table and so on...)

Obviously, I fixed up the definition but this means that any applications 
which reference those underscore fields will fail now and will have to be 
globally edited and recompiled.

Can anyone tell me if they use underscores as a matter of course in COBOL 
datanames? I understood that the underscore is NOT part of the COBOL 
standard character set (and wrote my parsers accordingly), but there is at 
least one site where they DO use it and have managed to get away with it. 
(It must have compiled OK. Clue: I'm not sure, but it may be a PR1ME 
site...)

Any comments?

Pete.
```

#### ↳ Re: Underscore in datanames

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-09T14:33:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h0lrrg$lsv$1@reader1.panix.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net>`

```
In article <79794vF1pep3iU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>Can anyone tell me if they use underscores as a matter of course in COBOL 
>datanames?

Given that DB2 is not COBOL I would say 'no, my experience leads me to 
conclude that underscores are not used as a matter of course in COBOL 
datanames'.  Evertthing-is-done-with-dashes.

On the other hand... I can readily imagine a site where someone said 'Gee, 
Mom, I'm a Programmer!' and by some obscure mangling of SPECIAL-NAMES an 
ALHPABET or a SYMBPOLIC CHARACTER or something else I rarely deal with 
allowed a_data_name to be as valid as a-data-name.

DD
```

##### ↳ ↳ Re: Underscore in datanames

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-09T09:16:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q3vs25dc0jte4o1kafonkbc1b18a4tep4f@4ax.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0lrrg$lsv$1@reader1.panix.com>`

```
On Tue, 9 Jun 2009 14:33:20 +0000 (UTC), docdwarf@panix.com () wrote:

>Given that DB2 is not COBOL I would say 'no, my experience leads me to 
>conclude that underscores are not used as a matter of course in COBOL 
>datanames'.  Evertthing-is-done-with-dashes.

Moving to Oracle, it is an irritant to switch to data names with
underscores.   Now I have to slow down to make capital dashes as I
type.
```

#### ↳ Re: Underscore in datanames

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2009-06-10T07:08:41+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h0mq8e$dsi$1@news-01.bur.connect.com.au>`
- **References:** `<79794vF1pep3iU1@mid.individual.net>`

```
Hi Pete,

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:79794vF1pep3iU1@mid.individual.net...
> I tripped up recently when processing some client source data definitions.
>
> Looked at it for ages and couldn't see a problem, then realised that
certain
> fields had been defined with underscores instead of hyphens in the names.
It
> looked like a maintenance programmer had made two sets of amendments to a
> very large record definition (Hundreds of datanames, lots of REDEFINES and
> OCCURS, an absolute delight that caused my Toolset to give up and just
> declare "Too many fields".)  I enlarged the Toolset buffers considerably
but
> then it gave the same message from ACCESS and SQL Server when the Toolset
> tried to EXECUTE the DDL it had generated, in order to create an
equivalent
> RDB table.
>
…[16 more quoted lines elided]…
> Any comments?

FWIW, I (and many others) use underscores for *everything* except where you
can't (end-if, i-o-control, end-perform etc) and have done for over twenty
years.

>
> Pete.

Cheers Richard Maher.

PS. I once saw a CamelCase program in cobol.

>
> -- 
> "I used to write COBOL...now I can do anything."
>
>
```

##### ↳ ↳ Re: Underscore in datanames

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2009-06-09T23:30:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7989kkF1pl2pqU1@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0mq8e$dsi$1@news-01.bur.connect.com.au>`

```
In article <h0mq8e$dsi$1@news-01.bur.connect.com.au>,
	"Richard Maher" <maher_rj@hotspamnotmail.com> writes:
> Hi Pete,
> 
…[38 more quoted lines elided]…
> years.

Interesting as I just looked it up and ANSI-79 COBOL does not list
underscore as a valid character except in a nun-numeric literal.


This is the second newsgroup I have seen this same question in today!!

bill
```

###### ↳ ↳ ↳ Re: Underscore in datanames

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-10T23:24:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<799jfcF1q5nd8U1@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0mq8e$dsi$1@news-01.bur.connect.com.au> <7989kkF1pl2pqU1@mid.individual.net>`

```
Bill Gunshannon wrote:
> In article <h0mq8e$dsi$1@news-01.bur.connect.com.au>,
> "Richard Maher" <maher_rj@hotspamnotmail.com> writes:
…[42 more quoted lines elided]…
>

Yep, that's my understanding too...
>
> This is the second newsgroup I have seen this same question in today!!

Maybe it's the season... :-)

Pete.
```

##### ↳ ↳ Re: Underscore in datanames

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-10T23:22:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<799jc7F1q46icU1@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0mq8e$dsi$1@news-01.bur.connect.com.au>`

```
Richard Maher wrote:
> Hi Pete,
>
…[42 more quoted lines elided]…
> PS. I once saw a CamelCase program in cobol.

Thanks for your response, Richard. I would expect CamelCase to work and have 
found myself using it in COBOL over the last few years.

But I WOULDN'T expect names with underscores in them to even compile.

Can you tell me what environment you are compiling in?

Cheers,

Pete.
```

###### ↳ ↳ ↳ Re: Underscore in datanames

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2009-06-11T07:09:10+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h0pebk$44t$1@news-01.bur.connect.com.au>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0mq8e$dsi$1@news-01.bur.connect.com.au> <799jc7F1q46icU1@mid.individual.net>`

```
Hi Pete,

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:799jc7F1q46icU1@mid.individual.net...
> Richard Maher wrote:
> > Hi Pete,
…[45 more quoted lines elided]…
> Thanks for your response, Richard. I would expect CamelCase to work and
have
> found myself using it in COBOL over the last few years.
>
> But I WOULDN'T expect names with underscores in them to even compile.
>
> Can you tell me what environment you are compiling in?

VAX COBOL, now DEC COBOL that runs on VMS (and TRU64 Unix for a while)

Don't know what the standard says about "$" signs and link-time resolved
variables either?

identification division.
program-id. yyy.
data division.
working-storage section.
01 ss$_wasclr pic 9(9) comp value external ss$_wasclr.
01 ss$_wasset pic 9(9) comp value external ss$_wasset.
01  sys_status pic 9(9) comp.
procedure division.
00.
    display "set = " ss$_wasset with conversion.
    display "clr = " ss$_wasclr with conversion.
    call "sys$setast"  giving sys_status.
    call "sys$exit" using by value sys_status.
    exit program.
end program yyy.

>
> Cheers,
>
> Pete.

Cheers Richard Maher
```

###### ↳ ↳ ↳ Re: Underscore in datanames

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2009-06-10T20:09:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<K5mdnZmUjoiH1q3XnZ2dnUVZ_vCdnZ2d@earthlink.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0mq8e$dsi$1@news-01.bur.connect.com.au> <799jc7F1q46icU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:799jc7F1q46icU1@mid.individual.net...

<snip>

My compiler does not accept underscores in data names:
>
PP 5655-G53 IBM Enterprise COBOL for z/OS  3.4.1               COBPTR
  LineID  PL 
L  ----+-*A-1-B--+----2----+----3----+----4----+----5----+----6---
  000025               /
  000026                WORKING-STORAGE SECTION.
  000027
  000028                01  PETE_DASHWOOD PIC X.

==000028==> IGYDS0001-W A blank was missing before character "_" in column 
16.
                        A blank was assumed.

==000028==> IGYDS0027-S Non-COBOL character(s) were found starting with "_"
                        in column 16.  The characters were discarded.

==000028==> IGYDS1089-S "DASHWOOD" was invalid.  Scanning was resumed at the
                        next area "A" item, level-number, or the start of 
the
                        next clause.

```

###### ↳ ↳ ↳ Re: Underscore in datanames

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-12T01:05:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79cdopF1pto82U1@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0mq8e$dsi$1@news-01.bur.connect.com.au> <799jc7F1q46icU1@mid.individual.net> <K5mdnZmUjoiH1q3XnZ2dnUVZ_vCdnZ2d@earthlink.com>`

```
Charles Hottel wrote:
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
> news:799jc7F1q46icU1@mid.individual.net...
…[20 more quoted lines elided]…
> ==000028==> IGYDS1089-S "DASHWOOD" was invalid.

ROFL!   Well, I guess it got that right... :-)


> Scanning was resumed
>                        at the next area "A" item, level-number, or
> the start of the
>                        next clause.
> 

Thanks Charlie, very informative...

Pete.
```

##### ↳ ↳ Re: Underscore in datanames

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-10T09:02:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmiv25p54mlp8hjp22b1kq4191rnbg0t1f@4ax.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0mq8e$dsi$1@news-01.bur.connect.com.au>`

```
On Wed, 10 Jun 2009 07:08:41 +0800, "Richard Maher"
<maher_rj@hotspamnotmail.com> wrote:

>FWIW, I (and many others) use underscores for *everything* except where you
>can't (end-if, i-o-control, end-perform etc) and have done for over twenty
>years.

Why?   It's a bit more work to type.   Is there any advantage to it?
```

###### ↳ ↳ ↳ Re: Underscore in datanames

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2009-06-11T07:10:48+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h0peem$46m$1@news-01.bur.connect.com.au>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0mq8e$dsi$1@news-01.bur.connect.com.au> <vmiv25p54mlp8hjp22b1kq4191rnbg0t1f@4ax.com>`

```
Hi Howard,

"Howard Brazee" <howard@brazee.net> wrote in message
news:vmiv25p54mlp8hjp22b1kq4191rnbg0t1f@4ax.com...
> On Wed, 10 Jun 2009 07:08:41 +0800, "Richard Maher"
> <maher_rj@hotspamnotmail.com> wrote:
>
> >FWIW, I (and many others) use underscores for *everything* except where
you
> >can't (end-if, i-o-control, end-perform etc) and have done for over
twenty
> >years.
>
> Why?   It's a bit more work to type.   Is there any advantage to it?

Why use any standard/convention? Consistency with SQL perhaps? Who knows? (I
like it :-)
>
> -- 
…[4 more quoted lines elided]…
> - James Madison

Cheers Richard Maher
```

##### ↳ ↳ Re: Underscore in datanames

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2009-06-10T13:42:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a1sv25l46uc4icf0pbhkh3k2or94qkbia3@4ax.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0mq8e$dsi$1@news-01.bur.connect.com.au>`

```
On Wed, 10 Jun 2009 07:08:41 +0800, "Richard Maher"
<maher_rj@hotspamnotmail.com> wrote:

>Hi Pete,
>
…[52 more quoted lines elided]…
>

As I seem to recall from a project I did many, many moons ago, the
underscore was required for data names in PL1.  As for COBOL, I've
never seen them used for data names.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"Who are you going to believe, me or your own eyes?"

-- Groucho Marx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Underscore in datanames

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-10T12:21:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bbuv25la4ltuaqa3i9hrof9ebm3nuhsfqi@4ax.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0mq8e$dsi$1@news-01.bur.connect.com.au> <a1sv25l46uc4icf0pbhkh3k2or94qkbia3@4ax.com>`

```
On Wed, 10 Jun 2009 13:42:30 -0400, SkippyPB
<swiegand@Nospam.neo.rr.com> wrote:

>As I seem to recall from a project I did many, many moons ago, the
>underscore was required for data names in PL1.  As for COBOL, I've
>never seen them used for data names.

Maybe I had my PL/I work confused with some CoBOL compiler.   Worked
too may places...
```

###### ↳ ↳ ↳ Re: Underscore in datanames

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-12T01:11:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79ce3kF1q7kavU1@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0mq8e$dsi$1@news-01.bur.connect.com.au> <a1sv25l46uc4icf0pbhkh3k2or94qkbia3@4ax.com>`

```
SkippyPB wrote:
> On Wed, 10 Jun 2009 07:08:41 +0800, "Richard Maher"
> <maher_rj@hotspamnotmail.com> wrote:
…[57 more quoted lines elided]…
> never seen them used for data names.

Yes, they are pretty standard practise for PL/1.

I've also seen them used in COBOL as the beginning of a subroutine name. I'm 
trying to remember and I think it was the Micro Focus environment many years 
ago. If you used an underscore or two underscores (I'm fuzzy on the 
details... someone else may know) it would force the subroutine to 
statically link (or something like that...)

Pete.
```

##### ↳ ↳ Re: Underscore in datanames

- **From:** Bernard Giroud <bgiroud3@nospam.free.fr>
- **Date:** 2009-06-13T10:19:34+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4a336117$0$21364$426a34cc@news.free.fr>`
- **In-Reply-To:** `<h0mq8e$dsi$1@news-01.bur.connect.com.au>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0mq8e$dsi$1@news-01.bur.connect.com.au>`

```
Richard Maher wrote:
> Hi Pete,
> 
…[39 more quoted lines elided]…
> 

In the shop I was, we were first under PR1MOS and we used hyphens (I 
don't remember if underscores were authorized or not). Then when we 
migrated to VAX VMS, we began to use underscores initially for system 
names, especially external symbols. Then we bought a dictionary (CDD) 
and a query language (DTR), but because all other supported languages 
used ONLY underscores and NO hyphens, we decided to support fields with 
underscores because it was compatible with all languages used in the 
shop (COBOL and DTR).

>> Pete.
> 
…[9 more quoted lines elided]…
> 

Bernard
```

###### ↳ ↳ ↳ Re: Underscore in datanames

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-14T11:06:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79ipnnF1r14prU1@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0mq8e$dsi$1@news-01.bur.connect.com.au> <4a336117$0$21364$426a34cc@news.free.fr>`

```
Bernard Giroud wrote:
> Richard Maher wrote:
>> Hi Pete,
…[60 more quoted lines elided]…
> Bernard

Thanks for the response, Bernard.

I'm coming to the conclusion that the code is from a very old DEC Vax site.

Pete.
```

#### ↳ Re: Underscore in datanames

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2009-06-09T19:54:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W8mdnZz5Evuia7PXnZ2dnUVZ_jqdnZ2d@earthlink.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:79794vF1pep3iU1@mid.individual.net...
>I tripped up recently when processing some client source data definitions.
>
…[32 more quoted lines elided]…
>

I don't  use underscores.  I searched the IBM Language Reference manual for 
the word "underscore" and the only reference I found was under XML element 
name formation.  Likewise for the IBM Programmer's Guide where the only 
reference had to do with OO COBOL and changing a period in a DLL module name 
to an underscore.

All that being said I don't think their use is prohibited.
```

##### ↳ ↳ Re: Underscore in datanames

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2009-06-10T00:01:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<798bedF1pkgejU1@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <W8mdnZz5Evuia7PXnZ2dnUVZ_jqdnZ2d@earthlink.com>`

```
In article <W8mdnZz5Evuia7PXnZ2dnUVZ_jqdnZ2d@earthlink.com>,
	"Charles Hottel" <chottel@earthlink.net> writes:
> 
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
…[43 more quoted lines elided]…
> All that being said I don't think their use is prohibited. 
 
Try looking under "COBOL Character Set".  That's where I found it in my
ANSI COBOL Programmers Reference.

bill 
```

###### ↳ ↳ ↳ Re: Underscore in datanames

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2009-06-09T20:18:04-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2M-dnbhfVMsoZrPXnZ2dnUVZ_i2dnZ2d@earthlink.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <W8mdnZz5Evuia7PXnZ2dnUVZ_jqdnZ2d@earthlink.com> <798bedF1pkgejU1@mid.individual.net>`

```

"Bill Gunshannon" <billg999@cs.uofs.edu> wrote in message 
news:798bedF1pkgejU1@mid.individual.net...
> In article <W8mdnZz5Evuia7PXnZ2dnUVZ_jqdnZ2d@earthlink.com>,
> "Charles Hottel" <chottel@earthlink.net> writes:
…[69 more quoted lines elided]…
> Scranton, Pennsylvania   |         #include <std.disclaimer.h>

From the Language Reference manual:

The default character set used in forming character-strings and separators 
is shown in Enterprise COBOL basic character set (Table 1 on page 4).

....

Well I was not able to copy/paste that chart, but the underscore character 
was not listed.  I will try to use it in a compile tomorrow and see what 
happens.
```

###### ↳ ↳ ↳ Re: Underscore in datanames

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-10T23:27:35+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<799jl9F1mk540U1@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <W8mdnZz5Evuia7PXnZ2dnUVZ_jqdnZ2d@earthlink.com> <798bedF1pkgejU1@mid.individual.net> <2M-dnbhfVMsoZrPXnZ2dnUVZ_i2dnZ2d@earthlink.com>`

```
Charles Hottel wrote:
> "Bill Gunshannon" <billg999@cs.uofs.edu> wrote in message
> news:798bedF1pkgejU1@mid.individual.net...
…[82 more quoted lines elided]…
> and see what happens.

Thanks Charlie, I'll be interested to see your result. (Don't forget to let 
us know what environment it is... :-))

Pete.
```

###### ↳ ↳ ↳ Re: Underscore in datanames

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-10T14:55:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h0ohhd$pok$4@reader1.panix.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <W8mdnZz5Evuia7PXnZ2dnUVZ_jqdnZ2d@earthlink.com> <798bedF1pkgejU1@mid.individual.net>`

```
In article <798bedF1pkgejU1@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:

[snip]

>Try looking under "COBOL Character Set".

Oh, I *cannot* resist...

... so *that's* how the bill-collectors have been finding me!

DD
```

###### ↳ ↳ ↳ Re: Underscore in datanames

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-10T09:30:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ckv251h8pchlepr2mak0b9no1vlqpnv9v@4ax.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <W8mdnZz5Evuia7PXnZ2dnUVZ_jqdnZ2d@earthlink.com> <798bedF1pkgejU1@mid.individual.net> <h0ohhd$pok$4@reader1.panix.com>`

```
On Wed, 10 Jun 2009 14:55:41 +0000 (UTC), docdwarf@panix.com () wrote:

>>Try looking under "COBOL Character Set".
>
>Oh, I *cannot* resist...
>
>... so *that's* how the bill-collectors have been finding me!

Some CoBOL characters are more obvious than others.
```

###### ↳ ↳ ↳ Re: Underscore in datanames

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-10T17:12:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h0opil$3l4$2@reader1.panix.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <798bedF1pkgejU1@mid.individual.net> <h0ohhd$pok$4@reader1.panix.com> <9ckv251h8pchlepr2mak0b9no1vlqpnv9v@4ax.com>`

```
In article <9ckv251h8pchlepr2mak0b9no1vlqpnv9v@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Wed, 10 Jun 2009 14:55:41 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[6 more quoted lines elided]…
>Some CoBOL characters are more obvious than others.

It might be, Mr Brazee, that some folks might think you neglected an 'li' 
in one of your adjectives there.

DD
```

###### ↳ ↳ ↳ Re: Underscore in datanames

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-10T09:03:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<koiv25hcl9ugvecim4tu7427iognjbtlsa@4ax.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <W8mdnZz5Evuia7PXnZ2dnUVZ_jqdnZ2d@earthlink.com> <798bedF1pkgejU1@mid.individual.net>`

```
It seems to me I came across a CoBOL compiler that used underscores
instead of dashes - but I am not remembering what compiler that was.
```

###### ↳ ↳ ↳ Re: Underscore in datanames

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-12T01:13:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79ce7mF1np4m1U1@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <W8mdnZz5Evuia7PXnZ2dnUVZ_jqdnZ2d@earthlink.com> <798bedF1pkgejU1@mid.individual.net> <koiv25hcl9ugvecim4tu7427iognjbtlsa@4ax.com>`

```
Howard Brazee wrote:
> It seems to me I came across a CoBOL compiler that used underscores
> instead of dashes - but I am not remembering what compiler that was.

From posts so far, it looks like DEC Vax could be a PR1ME candidate... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Underscore in datanames

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-11T08:59:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qt62359l0ptf571busd1kf40a5t3e39cp0@4ax.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <W8mdnZz5Evuia7PXnZ2dnUVZ_jqdnZ2d@earthlink.com> <798bedF1pkgejU1@mid.individual.net> <koiv25hcl9ugvecim4tu7427iognjbtlsa@4ax.com> <79ce7mF1np4m1U1@mid.individual.net>`

```
On Fri, 12 Jun 2009 01:13:23 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> It seems to me I came across a CoBOL compiler that used underscores
>> instead of dashes - but I am not remembering what compiler that was.
>
>From posts so far, it looks like DEC Vax could be a PR1ME candidate... :-)

I have programmed CoBOL on a Vax.
```

###### ↳ ↳ ↳ Re: Underscore in datanames

_(reply depth: 6)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2009-06-11T15:33:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79cmdtF1qdfkoU2@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <W8mdnZz5Evuia7PXnZ2dnUVZ_jqdnZ2d@earthlink.com> <798bedF1pkgejU1@mid.individual.net> <koiv25hcl9ugvecim4tu7427iognjbtlsa@4ax.com> <79ce7mF1np4m1U1@mid.individual.net> <qt62359l0ptf571busd1kf40a5t3e39cp0@4ax.com>`

```
In article <qt62359l0ptf571busd1kf40a5t3e39cp0@4ax.com>,
	Howard Brazee <howard@brazee.net> writes:
> On Fri, 12 Jun 2009 01:13:23 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[6 more quoted lines elided]…
> I have programmed CoBOL on a Vax.
 
So have I.  But being as I knew that ANSI COBOL didn't allow them
why would I ever have tried them?

bill
```

###### ↳ ↳ ↳ Re: Underscore in datanames

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-11T10:27:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kvb2359oritcokr3fpccbr1sufmgovo1b2@4ax.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <W8mdnZz5Evuia7PXnZ2dnUVZ_jqdnZ2d@earthlink.com> <798bedF1pkgejU1@mid.individual.net> <koiv25hcl9ugvecim4tu7427iognjbtlsa@4ax.com> <79ce7mF1np4m1U1@mid.individual.net> <qt62359l0ptf571busd1kf40a5t3e39cp0@4ax.com> <79cmdtF1qdfkoU2@mid.individual.net>`

```
On 11 Jun 2009 15:33:17 GMT, billg999@cs.uofs.edu (Bill Gunshannon)
wrote:

>> I have programmed CoBOL on a Vax.
> 
>So have I.  But being as I knew that ANSI COBOL didn't allow them
>why would I ever have tried them?

The Vax also had a compile option to eliminate the left sequence
numbers - looking for a dash or * in column 1 (I wonder if it looked
for "D") to decide what to do.    

I worked with the code and conventions others established before me.
```

#### ↳ Re: Underscore in datanames

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-06-10T11:07:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tVQXl.32919$Qg6.20620@newsfe08.iad>`
- **References:** `<79794vF1pep3iU1@mid.individual.net>`

```

Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote in message
news:79794vF1pep3iU1@mid.individual.net...
> I tripped up recently when processing some client source data definitions.

> Can anyone tell me if they use underscores as a matter of course in COBOL
> datanames? I understood that the underscore is NOT part of the COBOL
…[4 more quoted lines elided]…
>

Probably not Prime.  A-Z, 0-9, and hyphens are allowed in data names.
Still, it's not impossible: in the earlier days it was not unusual for Prime
users (very highly skilled ones, that is)  to modify the software to suit
themselves.  And there were one or two compilers from non-Prime sources that
may have used their own rules.

PL
```

##### ↳ ↳ Re: Underscore in datanames

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-12T01:14:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79ce9qF1qifhuU1@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <tVQXl.32919$Qg6.20620@newsfe08.iad>`

```
tlmfru wrote:
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote in message
> news:79794vF1pep3iU1@mid.individual.net...
…[17 more quoted lines elided]…
> PL

Cheers, Peter. I guiess we're down to DEC Vax...

Pete.
```

#### ↳ Re: Underscore in datanames

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-06-10T13:00:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h0or1g119kn@news1.newsguy.com>`
- **In-Reply-To:** `<79794vF1pep3iU1@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> Can anyone tell me if they use underscores as a matter of course in COBOL 
> datanames?

I use hyphens in native COBOL, but I use underscores and/or mixed case
in .NET COBOL, because those names interoperate properly with other
.NET languages.

I am not personally a fan of the underscore (I find it inconvenient to
touch-type on a US keyboard), and prefer CamelCase or pascalCase to
separate words in identifiers, but my .NET COBOL team decided on
underscores as part of our naming convention.
```

##### ↳ ↳ Re: Underscore in datanames

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-12T01:16:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79cedtF1p85aiU1@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <h0or1g119kn@news1.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>>
…[10 more quoted lines elided]…
> underscores as part of our naming convention.

Thanks Michael.

I think I mentioned elsewhere I've tended to use CamelCase in COBOL over the 
last few years. I'm sure it is becuase of the .NET influence.

Pete.
```

#### ↳ Re: Underscore in datanames

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-06-10T23:04:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mn%Xl.152568$jp1.16780@en-nntp-06.dc1.easynews.com>`
- **References:** `<79794vF1pep3iU1@mid.individual.net>`

```
Pete,
  I am JUST starting to read this thread.  Let me give a couple of "definitive" 
answers and then try and read further.

The underscore was NOT a part of the '85 Standard (or its amendments) as a part 
of the "COBOL Character Set".

The underscore WAS added to the COBOL character "repertoire" in the '02 
Standard.

There are a number of COBOL implementations that added the underscore to the 
COBOL character set (as an extension) to the '85 Standard and, I think, a few 
more that have included it as they implement parts of the '02 Standard.  (Micro 
Focus has allowed it for many years - but I don't think it has for the 20 years 
mentioned in another note.  IBM does NOT include it in their Enterprise COBOL or 
IBM COBOL for Windows.  I don't think they do for the iSeries or pSeries COBOL 
compilers - but I am less certain of that.)

In the '02 Standard (and the draft of the next revision), the underscore may be 
used in the same places in user-defined words as the hyphen.

As I recall, at least one vendor (possibly HP - for their NON-Micro Focus COBOL 
compiler) had a "special" meaning for when the underscore was the first 
character of a data name.  (Either it was a system name or an external data name 
or something else.  This was a LONG time ago).

Bottom-Line:
  If you want to handle Micro Focus COBOL, then you need to be prepared for the 
underscore in user-defined names.  Similarly, for other '02 Standard compilers. 
If you are working with only IBM mainframe COBOL, then you don't need to be 
prepared to handle it (yet).  (There is a SHARE requirement to add it.)

  * * * *

I hope this helps and  I will now try and read the rest of this thread.
```

##### ↳ ↳ Re: Underscore in datanames

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-12T01:21:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79cemlF1plfm9U1@mid.individual.net>`
- **References:** `<79794vF1pep3iU1@mid.individual.net> <mn%Xl.152568$jp1.16780@en-nntp-06.dc1.easynews.com>`

```
William M. Klein wrote:
> Pete,
>  I am JUST starting to read this thread.  Let me give a couple of
…[33 more quoted lines elided]…
> thread.

Thanks Bill.

It certainly is helpful and, as usual, clear and authoritative.

I have amended the parsers to accept it... (I suppose we should do the same 
for COBDATA...)

Cheers,

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
