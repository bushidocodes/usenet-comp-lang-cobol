[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Build failed Fujitsu V7

_21 messages · 9 participants · 2003-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Build failed Fujitsu V7

- **From:** "TeckDesign" <francis@teckdesign.com>
- **Date:** 2003-06-24T19:01:06+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt>`

```
        We are trying to use Fujitsu Cobol version 7, but too many problems
are coming up. We try to rebuild the all project but it send the following
message "Build failed"  without an explanation or just it stops in the
middle of the rebuild.
        We notice that using "#include" in the file section the rebuild
fails, so we replace it by "copy" the rebuild doesn�t fail but appears too
many warnings and the application doesn�t work correctly.
How can solve it??

Thanks
JM
```

#### ↳ Re: Build failed Fujitsu V7

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-06-24T13:47:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aEOdnQ-5hdBaAWWjXTWJiQ@giganews.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt>`

```

"TeckDesign" <francis@teckdesign.com> wrote in message
news:fn0Ka.3619$4a7.2051200@newsserver.ip.pt...
>         We are trying to use Fujitsu Cobol version 7, but too many
problems
> are coming up. We try to rebuild the all project but it send the following
> message "Build failed"  without an explanation or just it stops in the
…[4 more quoted lines elided]…
> How can solve it??

If this is the same 'bug' left over from V6, you must start a new project
then copy over all the modules from the crippled project to the new project
("save as" is insufficient).

You should use #INCLUDEs for the data division and COPY for the procedure
division.

You must also tie a red ribbon around your big toe (either side).

Only by doing these three things will you have any hope.
```

##### ↳ ↳ Re: Build failed Fujitsu V7

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-25T13:39:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef8fdb8_8@news.athenanews.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <aEOdnQ-5hdBaAWWjXTWJiQ@giganews.com>`

```
LOL!

Good stuff, Jerry <G>

This has to be one of the most frustrating errors in Fujitsu.

It has happened to me even when I didn't have INCLUDES or COPYs in the
source and it just leaves you with nothing.

"Build failed..."

"OK, gimme a clue..."

"Nope. Build failed..."

I found through (very) bitter experience that creating a new project seems
to work OK (provided you are sure that everything in the one that failed is
fine...). I have also fixed it on occasion by deleting the make file and
forcing it to rebuild all the project information (though I wouldn't
recommend this as a standard approach). Once you have encountered it and
corrected it, it seems to go away for ever <G> (Like it knows "Awww...that
one won't upset him anymore..."). I haven't seen it now for a couple of
years.

The ribbons on the toes is a novel solution. I'll try that one next
time...<G>

Pete.



"JerryMouse" <nospam@bisusa.com> wrote in message
news:aEOdnQ-5hdBaAWWjXTWJiQ@giganews.com...
>
> "TeckDesign" <francis@teckdesign.com> wrote in message
…[3 more quoted lines elided]…
> > are coming up. We try to rebuild the all project but it send the
following
> > message "Build failed"  without an explanation or just it stops in the
> > middle of the rebuild.
> >         We notice that using "#include" in the file section the rebuild
> > fails, so we replace it by "copy" the rebuild doesn�t fail but appears
too
> > many warnings and the application doesn�t work correctly.
> > How can solve it??
>
> If this is the same 'bug' left over from V6, you must start a new project
> then copy over all the modules from the crippled project to the new
project
> ("save as" is insufficient).
>
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Build failed Fujitsu V7

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-06-24T21:17:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<186cneJhqZa8m2SjXTWJhA@giganews.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <aEOdnQ-5hdBaAWWjXTWJiQ@giganews.com> <3ef8fdb8_8@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3ef8fdb8_8@news.athenanews.com...
> LOL!
>
…[14 more quoted lines elided]…
> to work OK (provided you are sure that everything in the one that failed
is
> fine...). I have also fixed it on occasion by deleting the make file and
> forcing it to rebuild all the project information (though I wouldn't
…[6 more quoted lines elided]…
> time...<G>

You know, come to think on it, I can't remember if this problem, once fixed,
ever reappears on the same project. My dim recollection says you're
correct - I can't say positively that I've ever had to do this little dance
more than once per project.....

Hmmm.
```

###### ↳ ↳ ↳ Re: Build failed Fujitsu V7

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-06-25T10:32:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SSeKa.2495$BM.1421210@newssrv26.news.prodigy.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <aEOdnQ-5hdBaAWWjXTWJiQ@giganews.com> <3ef8fdb8_8@news.athenanews.com>`

```
> "Build failed..."
>
> "OK, gimme a clue..."
>
> "Nope. Build failed..."

"But who is on second?"

"No, Who is on first."

"I don't know."

"Third base!"


MCM
```

##### ↳ ↳ Re: Build failed Fujitsu V7

- **From:** "R. Hendriks" <R.Hendriks_1@uvt.nl>
- **Date:** 2003-06-25T13:54:43+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdc2gq$rof$1@kostnix.uvt.nl>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <aEOdnQ-5hdBaAWWjXTWJiQ@giganews.com>`

```
-. Remove the entire debug directory. It'll be restored when totally
rebuilding the project, just don't delete the .ppj file!

-. Got any event scripts that are totally commented out? I've found out that
when event are created (aka a script is made) and is totally commented out,
the builder misses the various DIVISION's and will give strange build
errors, or not an error at all.

-. Check Fujitsu knowledgebase, wasn't there a fix for this? Don't remember,
can check it though.

Good luck,

Rik

"JerryMouse" <nospam@bisusa.com> wrote in message
news:aEOdnQ-5hdBaAWWjXTWJiQ@giganews.com...
>
> "TeckDesign" <francis@teckdesign.com> wrote in message
…[3 more quoted lines elided]…
> > are coming up. We try to rebuild the all project but it send the
following
> > message "Build failed"  without an explanation or just it stops in the
> > middle of the rebuild.
> >         We notice that using "#include" in the file section the rebuild
> > fails, so we replace it by "copy" the rebuild doesn�t fail but appears
too
> > many warnings and the application doesn�t work correctly.
> > How can solve it??
>
> If this is the same 'bug' left over from V6, you must start a new project
> then copy over all the modules from the crippled project to the new
project
> ("save as" is insufficient).
>
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Build failed Fujitsu V7

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-06-25T08:18:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jKGcnerZ3aWlPGSjXTWJhQ@giganews.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <aEOdnQ-5hdBaAWWjXTWJiQ@giganews.com> <bdc2gq$rof$1@kostnix.uvt.nl>`

```

"R. Hendriks" <R.Hendriks_1@uvt.nl>
>
> -. Check Fujitsu knowledgebase, wasn't there a fix for this? Don't
remember,
> can check it though.

----------

Bug Fix Report

1. Product
   COBOL97 and PowerCOBOL

2. SYMPTOMS
   The compiler returns a build error but no other message.

   This problem occurs when compiling source code from a precompiler such as
PowerCOBOL.
   If a source line containing a  # FILE/#LINE directive was in error, the
compiler erroneously reported
   the line number to be 0.

3. ACTION TO BE TAKEN
   To apply the Compiler fix:
    1) Unzip this file into a  temp directory,
    2) Locate the file "F3BH220.dll." in the COBOL folder. By default it
should be in
        "C:\Program Files\Fujitsu COBOL\COBOL",
    3) Copy the new "F3BH220.dll." from the temp directory to the COBOL
folder

-----------
Note: The report does not say to which versions of FJ the fix pertains.
```

###### ↳ ↳ ↳ Re: Build failed Fujitsu V7

_(reply depth: 4)_

- **From:** "R. Hendriks" <R.Hendriks_1@uvt.nl>
- **Date:** 2003-06-25T15:46:30+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdc92d$8e$1@kostnix.uvt.nl>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <aEOdnQ-5hdBaAWWjXTWJiQ@giganews.com> <bdc2gq$rof$1@kostnix.uvt.nl> <jKGcnerZ3aWlPGSjXTWJhQ@giganews.com>`

```
I remember this fix, I believe it was released during version 6.1a. Most
fixes for V7 can be found by searching for 'v7' in the vast library of
knowledge called the 'knowledge base'.

"JerryMouse" <nospam@bisusa.com> wrote in message
news:jKGcnerZ3aWlPGSjXTWJhQ@giganews.com...
>
> "R. Hendriks" <R.Hendriks_1@uvt.nl>
…[15 more quoted lines elided]…
>    This problem occurs when compiling source code from a precompiler such
as
> PowerCOBOL.
>    If a source line containing a  # FILE/#LINE directive was in error, the
…[15 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Build failed Fujitsu V7

_(reply depth: 5)_

- **From:** "TeckDesign" <francis@teckdesign.com>
- **Date:** 2003-06-25T16:25:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<abjKa.3655$Aw3.2151477@newsserver.ip.pt>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <aEOdnQ-5hdBaAWWjXTWJiQ@giganews.com> <bdc2gq$rof$1@kostnix.uvt.nl> <jKGcnerZ3aWlPGSjXTWJhQ@giganews.com> <bdc92d$8e$1@kostnix.uvt.nl>`

```
Hi,

    The last suggestion only works with v6.
    Thanks to everyone who tried to help me, but until now I couldn�t
accomplish nothing.
    I've tried everything you all suggested without success.

Thanks again,


"R. Hendriks" <R.Hendriks_1@uvt.nl> escreveu na mensagem
news:bdc92d$8e$1@kostnix.uvt.nl...
> I remember this fix, I believe it was released during version 6.1a. Most
> fixes for V7 can be found by searching for 'v7' in the vast library of
…[21 more quoted lines elided]…
> >    This problem occurs when compiling source code from a precompiler
such
> as
> > PowerCOBOL.
> >    If a source line containing a  # FILE/#LINE directive was in error,
the
> > compiler erroneously reported
> >    the line number to be 0.
…[16 more quoted lines elided]…
>
```

#### ↳ Re: Build failed Fujitsu V7

- **From:** gmspano <member9303@dbforums.com>
- **Date:** 2003-06-25T20:52:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3043414.1056574322@dbforums.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt>`

```

I agree with Jerry.

You need to open a new project running a new instance of Netcobol and
copy/paste all your forms and scripts.
I did this way a lot. There aren't other solutions..

The fix mentioned is for v6.1 and this patch was been created to resolve
a trouble i have had during a compilation.
Japan team didn't believe about my request, then i sent them a project
and they have been able to reproduce the error message.

There is another GREAT bug in Netcobol.
If you have a project that is using a custom control not longer
registered on your system, Netcobol doesn't allow to cut the control
from the form and you are unable to save your project without it.
It needs to create a new project copying/pasting forms and scripts from
the unavailable project...
Japan team has promised (some years ago) "In the next release the
problems will be resolved"...Nothing to do!! It is always the same...

Japan team think different from the rest of the world.
For your informations, they released a particular version for .NET that
is not the same for the rest of world, not only for the Japanese
language, but with a series of different features.

There is another consideration: when we see a new release of the
product, Japan is using the same version a year before. (???)

Gianni
```

##### ↳ ↳ Re: Build failed Fujitsu V7

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-26T10:58:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3efa25f2_2@corp-news.newsgroups.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <3043414.1056574322@dbforums.com>`

```

"gmspano" <member9303@dbforums.com> wrote in message
news:3043414.1056574322@dbforums.com...
>
> I agree with Jerry.
…[30 more quoted lines elided]…
> Posted via http://dbforums.com
```

##### ↳ ↳ Re: Build failed Fujitsu V7

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-26T11:09:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3efa28b6_2@corp-news.newsgroups.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <3043414.1056574322@dbforums.com>`

```

"gmspano" <member9303@dbforums.com> wrote in message
news:3043414.1056574322@dbforums.com...
>
>
…[8 more quoted lines elided]…
>
This is NOT just a problem with NETCobol. The same thing happens in V6.

I found this to my cost a few months ago when I de-registered some
components I had written, with a view to replacing them.

I was staggered to find that any project that used them was no longer
savable. I even re-registered them but it made no difference. (To be fair,
the OLE ClassID had changed; nevertheless, the OLE ProgramID was the same).

As Gianni described, I had to create new projects and laboriously copy every
element from the old projects (including event code, not just controls) to
the new project. One of these projects took a full day of really boring
error-prone cut-and-pasting to recover. It's a nightmare...

I haven't investigated it fully (yet) because I've been too busy, but I
believe there HAS to be a way to amend the build information (or the system
registry) so the reference to the de-registered component is removed.

This is something that Fujitsu SHOULD fix and fix quickly.

>
> There is another consideration: when we see a new release of the
> product, Japan is using the same version a year before. (???)
>

That has been the case for a long time. There is nothing wrong with this. It
means the version we get is more stable and the price we pay for it is less
than the price the Japanese pay.

Pete.
```

###### ↳ ↳ ↳ Re: Build failed Fujitsu V7

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-06-25T20:31:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YqSdncz8J5F30WejXTWJkw@giganews.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <3043414.1056574322@dbforums.com> <3efa28b6_2@corp-news.newsgroups.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz>
>
> As Gianni described, I had to create new projects and laboriously copy
every
> element from the old projects (including event code, not just controls) to
> the new project. One of these projects took a full day of really boring
> error-prone cut-and-pasting to recover. It's a nightmare...

Wow! I never had to do that!

I just had to create a new project and copy the "module." And tune up some
stuff like library names and locations for debug and release modules,
version numbers, blah-blah-blah. Takes maybe three minutes.
```

###### ↳ ↳ ↳ Re: Build failed Fujitsu V7

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-26T14:58:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3efa5e2c_2@corp-news.newsgroups.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <3043414.1056574322@dbforums.com> <3efa28b6_2@corp-news.newsgroups.com> <YqSdncz8J5F30WejXTWJkw@giganews.com>`

```

"JerryMouse" <nospam@bisusa.com> wrote in message
news:YqSdncz8J5F30WejXTWJkw@giganews.com...
>
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
…[3 more quoted lines elided]…
> > element from the old projects (including event code, not just controls)
to
> > the new project. One of these projects took a full day of really boring
> > error-prone cut-and-pasting to recover. It's a nightmare...
…[6 more quoted lines elided]…
>
How do you copy the "module" when you are not allowed to save it? Even a
Ctrl-C brings up:"You cannot save an uninstalled component.".

You CAN copy (cut and paste) the constituents of the module and that's what
I (and I think, Gianni also) had to do.

You have to do this one-by-one to the new project, taking care to EXCLUDE
the  de-registered component.

It is a real pain in the arse...

If it really is that easy, Jerry I'm going to sulk for a day or two...<G>

Pete.
```

###### ↳ ↳ ↳ Re: Build failed Fujitsu V7

_(reply depth: 4)_

- **From:** pvieira@emporsoft.pt (Paulo Vieira)
- **Date:** 2003-06-26T01:52:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b8d7c7.0306260052.20552b83@posting.google.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <3043414.1056574322@dbforums.com> <3efa28b6_2@corp-news.newsgroups.com> <YqSdncz8J5F30WejXTWJkw@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message news:<YqSdncz8J5F30WejXTWJkw@giganews.com>...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
> >
…[10 more quoted lines elided]…
> version numbers, blah-blah-blah. Takes maybe three minutes.

My experience goes along with those os Pete and Gianni, and since
version 4.2.
It shouldn't be too hard to allow to delete the damm thing (control)
from the project...
```

#### ↳ Re: Build failed Fujitsu V7

- **From:** gmspano <member9303@dbforums.com>
- **Date:** 2003-06-26T08:20:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3045040.1056615641@dbforums.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt>`

```

I confirm what Pete says.

It's not so easy.  You need to copy and paste all the stuff step by
step, avoiding to include the "bad" control.
Sometime is possible to copy the entire module.

I'm using v6.1, but i know in the new v7 the problem still remains.

As Pete is suggesting, Fujitsu SHOULD FIX this problem, but thinking
about  the normal course to release a new version, probably we need to
wait another year to see some bugs fixed.

I heard from a friend that Fujitsu probably will stop the Netcobol for
Windows development, pointing their money and efforts on the .NET
environment...If that is true, i'm really surprised.
Netcobol for .Net doesn't provide any tool to help us to migrate "old"
Netcobol for Win projects, so we need to rebuild them from the scratch.

Powercobol (or Netcobol for Win) is a great product, and actually in the
market there aren't other Cobol company offering a similar product, but
Fujitsu needs to improve better its IDE, adding new features. I sent
them last year a list of these features, hoping to see them in the next
v8.0...(I hope!!).

Gianni
```

##### ↳ ↳ Re: Build failed Fujitsu V7

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-06-26T07:47:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1pqcnTj5mvXydmejXTWJhQ@giganews.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <3045040.1056615641@dbforums.com>`

```

"gmspano" <member9303@dbforums.com>
>
> I heard from a friend that Fujitsu probably will stop the Netcobol for
…[3 more quoted lines elided]…
> Netcobol for Win projects, so we need to rebuild them from the scratch.

That's the Catch-22. We certainly are not going to re-write an untold number
of lines of code and redesign uncountably many forms. Fujitsu may be
reluctant to develop a conversion tool for moving from PowerCOBOL to
NetCOBOL but I can't see how they can get their existing users to migrate
otherwise.
```

###### ↳ ↳ ↳ Re: Build failed Fujitsu V7

- **From:** "JC" <Kaos_Theory99@hotmail.com>
- **Date:** 2003-06-26T14:58:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdf1m4$7om$1@hercules.btinternet.com>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt> <3045040.1056615641@dbforums.com> <1pqcnTj5mvXydmejXTWJhQ@giganews.com>`

```
JerryMouse <nospam@bisusa.com> wrote in message
news:1pqcnTj5mvXydmejXTWJhQ@giganews.com...
>
>
> That's the Catch-22. We certainly are not going to re-write an untold
number
> of lines of code and redesign uncountably many forms. Fujitsu may be
> reluctant to develop a conversion tool for moving from PowerCOBOL to
> NetCOBOL but I can't see how they can get their existing users to migrate
> otherwise.
>
Their .NET 1.1 product is a bit deficient in a few areas...

preprocessor support & tailoring the reserved words list
```

##### ↳ ↳ Re: Build failed Fujitsu V7

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-06-26T20:48:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3048100.1056660519@dbforums.com>`
- **References:** `<3045040.1056615641@dbforums.com>`

```

People dont forget  to tell fujitsu to fix, or improve
when we want  copy an Objetc and bring together all
the  script from all Event  or  Ask  if we want to copy the
Script too.

I am tired to tell they  to do that, this will improve a lot
all de development process.

Carlos Lages
```

###### ↳ ↳ ↳ Re: Build failed Fujitsu V7

- **From:** "TeckDesign" <francis@teckdesign.com>
- **Date:** 2003-06-27T10:21:20+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_1UKa.3755$mK4.2168944@newsserver.ip.pt>`
- **References:** `<3045040.1056615641@dbforums.com> <3048100.1056660519@dbforums.com>`

```

THE PROBLEM WAS  SOLVED BY A FUJITSU PATCH..
AND WORK FINE!!!



"Carlos lages" <member129@dbforums.com> escreveu na mensagem
news:3048100.1056660519@dbforums.com...
>
> People dont forget  to tell fujitsu to fix, or improve
…[11 more quoted lines elided]…
>
```

#### ↳ Re: Build failed Fujitsu V7

- **From:** "TeckDesign" <francis@teckdesign.com>
- **Date:** 2003-06-27T10:26:57+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f7UKa.3756$eq6.2195566@newsserver.ip.pt>`
- **References:** `<fn0Ka.3619$4a7.2051200@newsserver.ip.pt>`

```
THE PROBLEM WAS  SOLVED BY A FUJITSU PATCH..
AND WORK FINE!!!




"TeckDesign" <francis@teckdesign.com> escreveu na mensagem
news:fn0Ka.3619$4a7.2051200@newsserver.ip.pt...
>         We are trying to use Fujitsu Cobol version 7, but too many
problems
> are coming up. We try to rebuild the all project but it send the following
> message "Build failed"  without an explanation or just it stops in the
…[11 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
