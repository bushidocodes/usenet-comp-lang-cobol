[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress RunTime Distribution

_19 messages · 7 participants · 1999-12 → 2000-01_

---

### NetExpress RunTime Distribution

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-12-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<839cls$1i6$1@nntp9.atl.mindspring.net>`

```
Anyone out here actually distribute MicroFocus NetExpress applications...???

I am very curious how you are distributing the MF Runtime modules (redist
application server)...

For well over a year now, MF has distributed/posted "FixPacks" to NE...These
however do not update the redistribution modules in the redist application
server portion of NE...I have complained several times...I have reported
problems that even today continue to go unanswered my MicroFocus
(MERANT)...I have received responses from them such as - they cannot provide
support for the problem because I do not use the OUTDATED redist application
server runtime...Instead, I try to use current modules from the NE/Base/bin
directory, which are current with the fixpacks...

Today, I asked them...."OK, when will you provide me a current reist
runtime?"

They're formal response is "This remains under study. It should be ready
soon. What will be available is a Service Pack that can be used to update a
Redist Run-time installation. However, this will probably not become
available until after the current problems with Service Pack 1 are
resolved."

How are other developers distributing their products developed with NE to
clients?

kenmullins
```

#### ↳ Re: NetExpress RunTime Distribution

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-12-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<839d3m$gvj$1@nntp9.atl.mindspring.net>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net>`

```
Forgot to mention...What this means is that it is not possible to distribute
a product using NetExpress and expect it to be supported by Merant...

kenmullins
```

##### ↳ ↳ Re: NetExpress RunTime Distribution

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83agkj$4ba$1@hyperion.mfltd.co.uk>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <839d3m$gvj$1@nntp9.atl.mindspring.net>`

```
Ken,

Could you explain why ? I don't understand how the lack of an automatic
update mechanism indicates that redistributable files are not supported by
Merant, which is what your comment seems to suggest.

I sympathise with your point about the redist directory not being
automatically updated, but the issue is actually more complicated than that.
A system may have more than one development system and/or multiple
applications. Typically those applications contain redistributable files
from the COBOL system, rather than a single redist directory, so in order to
bring everything up-to-date the installation mechanism would need to scan
the entire hard disk for any occurrences of any redistributable files and
prompt the person running the update as to whether an updated was desired on
each occurrence found, as it is quite possible that updates would only be
wanted on certain apps. I would imagine that there's quite a lot of work
involved in the coding and interface of such a mechanism and I'm sure the
group working on the technology want to make sure it works first, hence what
you were told.


Ken Mullins wrote in message <839d3m$gvj$1@nntp9.atl.mindspring.net>...
>Forgot to mention...What this means is that it is not possible to
distribute
>a product using NetExpress and expect it to be supported by Merant...
>
>kenmullins
>
>
```

###### ↳ ↳ ↳ Re: NetExpress RunTime Distribution

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83akgp$e19$1@nntp9.atl.mindspring.net>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <839d3m$gvj$1@nntp9.atl.mindspring.net> <83agkj$4ba$1@hyperion.mfltd.co.uk>`

```
> Could you explain why ? I don't understand how the lack of an automatic
> update mechanism indicates that redistributable files are not supported by
> Merant, which is what your comment seems to suggest.

Because this is the response I receive when reporting some serious problems
via the answerlab...

"We are up against the same wall as previously. If a standard install is not
being used Development will not participate in resolving non-standard
installation issues."

Now how can i do a standard install today, when the runtime modules are
outdated more than a year...???

kenmullins
```

###### ↳ ↳ ↳ Re: NetExpress RunTime Distribution

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38591477.B231FC31@home.com>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <839d3m$gvj$1@nntp9.atl.mindspring.net> <83agkj$4ba$1@hyperion.mfltd.co.uk>`

```

Gael Wilson wrote:
> 
> Ken,
…[6 more quoted lines elided]…
> automatically updated, but the issue is actually more complicated than that.

Gael,

All that you say may well be true. But the fact is, this is an OLD
problem, brought to the notice of Answerlab, by somebody other than Ken,
and I have to go from memory, well over a year ago.

Somebody didn't quite think this one through - yes there have been  Fix
Packs to adjust/fine-tune existing package, but the thinking missed the
boat on ensuring Redistribution was updated. Classical example, as I
recall, PC_PRINT was updated but not the files in Redistribution.

A recommendation I made, and I hope Newbury, (or whoever), follows
through - use a Project Wizard to select only those files needed from
the Redistribution required for a particular end-user - at the moment
you have to 'chuck' the lot at them, so you don't miss a feature you
need - and it sure as hell doesn't fit on a 1.4 floppy !

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: NetExpress RunTime Distribution

_(reply depth: 4)_

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 2000-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpBc4.1954$s5.71672@news1.frmt1.sfba.home.com>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <839d3m$gvj$1@nntp9.atl.mindspring.net> <83agkj$4ba$1@hyperion.mfltd.co.uk> <38591477.B231FC31@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote in message
news:38591477.B231FC31@home.com...
> A recommendation I made, and I hope Newbury, (or whoever), follows
> through - use a Project Wizard to select only those files needed from
> the Redistribution required for a particular end-user - at the moment
> you have to 'chuck' the lot at them, so you don't miss a feature you
> need - and it sure as hell doesn't fit on a 1.4 floppy !

unofficially, i've heard that this is indeed on the list to be implemented
in the next major release (presumably 4.0). of course, just because it's on
the list, doesn't mean it'll make it. and i have no sense of when the next
release will see the light of day (is that enough disclaimers on "forward
looking" statements? ;-).
```

###### ↳ ↳ ↳ Re: NetExpress RunTime Distribution

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387378A8.70CCD613@home.com>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <839d3m$gvj$1@nntp9.atl.mindspring.net> <83agkj$4ba$1@hyperion.mfltd.co.uk> <38591477.B231FC31@home.com> <gpBc4.1954$s5.71672@news1.frmt1.sfba.home.com>`

```


Gazaloo wrote:
> 
> "James J. Gavan" <jjgavan@home.com> wrote in message
…[11 more quoted lines elided]…
> looking" statements? ;-).

Thanks Mr. Gazaloo. You know, take out my quote, substitute the name WMK
for Gazaloo - and you'd swear the sender was talking about the Standards
for COBOL 2010 <G>

Jimmy
```

#### ↳ Re: NetExpress RunTime Distribution

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38584FC2.E7BCE607@home.com>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net>`

```


Ken Mullins wrote:
> 
> Anyone out here actually distribute MicroFocus NetExpress applications...???
> 
 
> How are other developers distributing their products developed with NE to
> clients?
> 

Sympathies Ken. As yet I haven't sent the final 'goodies' to my user -
but like you I will have EXACTLY the same problem AND - the size of that
distribution package !!!

Jimmy, Calgary AB
```

#### ↳ Re: NetExpress RunTime Distribution

- **From:** "Bill Wood" <beavis27@email.msn.com>
- **Date:** 1999-12-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uxRGwhbS$GA.274@cpmsnbbsa05>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net>`

```
Ken,
      Our product has been developed on NetExpress and we had the same
problem.  On one of the support calls we had I mentioned it to the support
person and he shipped me a copy of a .bat file they use at Merant.
Basically you copy the files from wherever they live (mostly
NetExpress\base\bin and NetExpress\DialogSystem\bin) into your redist
directory.  We have a redist directory on a shared drive and when our app is
built we dump down all of those files.  It isn't small, but we haven't had a
problem yet.  After I load a fixpack I run this .bat file and it copies all
of the files into this redist directory so it constantly stays updated.

bill


Ken Mullins wrote in message <839cls$1i6$1@nntp9.atl.mindspring.net>...
>Anyone out here actually distribute MicroFocus NetExpress
applications...???
>
>I am very curious how you are distributing the MF Runtime modules (redist
>application server)...
>
>For well over a year now, MF has distributed/posted "FixPacks" to
NE...These
>however do not update the redistribution modules in the redist application
>server portion of NE...I have complained several times...I have reported
>problems that even today continue to go unanswered my MicroFocus
>(MERANT)...I have received responses from them such as - they cannot
provide
>support for the problem because I do not use the OUTDATED redist
application
>server runtime...Instead, I try to use current modules from the NE/Base/bin
>directory, which are current with the fixpacks...
…[17 more quoted lines elided]…
>
```

##### ↳ ↳ Re: NetExpress RunTime Distribution

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385C2A62.524C5E78@home.com>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <uxRGwhbS$GA.274@cpmsnbbsa05>`

```


Bill Wood wrote:
> 
> Ken,
>       Our product has been developed on NetExpress and we had the same
> problem.  On one of the support calls we had I mentioned it to the support
> person and he shipped me a copy of a .bat file they use at Merant.

So, Merant - why haven't we ALL got a copy of this bat file ?????

Jimmy, Calgary AB
```

##### ↳ ↳ Re: NetExpress RunTime Distribution

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-12-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83ii07$rus$1@nntp2.atl.mindspring.net>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <uxRGwhbS$GA.274@cpmsnbbsa05>`

```
That is very strange...I made up my own .bat file doing the same thing,
except I copied all of the modules that were in the redist directory from
the netexpress\base\bin directory into my app's executables directory and
was told by answerlab folks that that was not supported...

I take it you distribute all the modules listed in the redist directory
whether you need them or not?

kenmullins

Bill Wood <beavis27@email.msn.com> wrote in message
news:uxRGwhbS$GA.274@cpmsnbbsa05...
> Ken,
>       Our product has been developed on NetExpress and we had the same
…[4 more quoted lines elided]…
> directory.  We have a redist directory on a shared drive and when our app
is
> built we dump down all of those files.  It isn't small, but we haven't had
a
> problem yet.  After I load a fixpack I run this .bat file and it copies
all
> of the files into this redist directory so it constantly stays updated.
>
…[12 more quoted lines elided]…
> >however do not update the redistribution modules in the redist
application
> >server portion of NE...I have complained several times...I have reported
> >problems that even today continue to go unanswered my MicroFocus
…[4 more quoted lines elided]…
> >server runtime...Instead, I try to use current modules from the
NE/Base/bin
> >directory, which are current with the fixpacks...
> >
…[4 more quoted lines elided]…
> >soon. What will be available is a Service Pack that can be used to update
a
> >Redist Run-time installation. However, this will probably not become
> >available until after the current problems with Service Pack 1 are
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: NetExpress RunTime Distribution

- **From:** "Bill Wood" <beavis27@bigfoot.com>
- **Date:** 1999-12-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<utBy57uT$GA.287@cpmsnbbsa05>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <uxRGwhbS$GA.274@cpmsnbbsa05> <83ii07$rus$1@nntp2.atl.mindspring.net>`

```
Sadly, this is true.  For example our entire application is written using
single-threading.  We still ship all of the multi-thread modules.
Eventually, we may go and try to figure out what we need and don't need but
for right now we ship the whole thing.

Bill

Ken Mullins wrote in message <83ii07$rus$1@nntp2.atl.mindspring.net>...
>That is very strange...I made up my own .bat file doing the same thing,
>except I copied all of the modules that were in the redist directory from
…[12 more quoted lines elided]…
>> problem.  On one of the support calls we had I mentioned it to the
support
>> person and he shipped me a copy of a .bat file they use at Merant.
>> Basically you copy the files from wherever they live (mostly
…[3 more quoted lines elided]…
>> built we dump down all of those files.  It isn't small, but we haven't
had
>a
>> problem yet.  After I load a fixpack I run this .bat file and it copies
…[10 more quoted lines elided]…
>> >I am very curious how you are distributing the MF Runtime modules
(redist
>> >application server)...
>> >
…[18 more quoted lines elided]…
>> >soon. What will be available is a Service Pack that can be used to
update
>a
>> >Redist Run-time installation. However, this will probably not become
…[3 more quoted lines elided]…
>> >How are other developers distributing their products developed with NE
to
>> >clients?
>> >
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: NetExpress RunTime Distribution

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3865B99F.9BE31B2D@home.com>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <uxRGwhbS$GA.274@cpmsnbbsa05> <83ii07$rus$1@nntp2.atl.mindspring.net> <utBy57uT$GA.287@cpmsnbbsa05>`

```


Bill Wood wrote:
> 
> Sadly, this is true.  For example our entire application is written using
…[3 more quoted lines elided]…
> 
I tried that Bill; all I wanted was OO and single-threading, no Dialog
System, no.... etc. Tried to figure it from the information in the
on-line help - short story - what I did, didn't work; in my case user
has a laptop so he came over and plugged into my desktop and transferred
the whole shebang that way.

Just not satisfactory. Don't get me wrong, overall I still think
NetExpress is a great product - but this Redistribution/Runtime Support
- sheesh ! There is a simple and effective answer, and I'm curious why
they haven't gone that route -  use a Project Wizard to determine what
you want, e.g. :-

	Do you use OO			Yes/No
	Single Thread/Multi		S/M
	Do you use Windows APIs		Yes/No
	Do you use Dialog System	Yes/No
	Do you use Fileshare		Yes/No
	Do you ....... etc.

and whatever necesary permutations on the above to make it fit.

I fail to the see the problem to achieve the above; fairly short
analysis required, followed up by one program to copy and build the
run-time package you want. Merant ?????

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: NetExpress RunTime Distribution

_(reply depth: 5)_

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 1999-12-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gAw94.13524$du4.320843@news1.frmt1.sfba.home.com>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <uxRGwhbS$GA.274@cpmsnbbsa05> <83ii07$rus$1@nntp2.atl.mindspring.net> <utBy57uT$GA.287@cpmsnbbsa05> <3865B99F.9BE31B2D@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote in message
news:3865B99F.9BE31B2D@home.com...
> Just not satisfactory. Don't get me wrong, overall I still think
> NetExpress is a great product - but this Redistribution/Runtime Support
> - sheesh ! There is a simple and effective answer, and I'm curious why
> they haven't gone that route -  use a Project Wizard to determine what
> you want, [snip]

i agree that this feature is much needed; i have forwarded the stream on to
MERANT Product Management for consideration.

technically, the solution is simple. what isn't so simple is the testing
requirements that a multi-personality run-time environment (RTE) imposes (i
assume you'd like the resulting RTE's tested? ;-). hence the RTE is tested
as a whole, although 'whole' in this instance actually means two RTE's
(single-threaded & multi-threaded).
```

###### ↳ ↳ ↳ Re: NetExpress RunTime Distribution

_(reply depth: 6)_

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-12-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8467tc$4qu$1@nntp6.atl.mindspring.net>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <uxRGwhbS$GA.274@cpmsnbbsa05> <83ii07$rus$1@nntp2.atl.mindspring.net> <utBy57uT$GA.287@cpmsnbbsa05> <3865B99F.9BE31B2D@home.com> <gAw94.13524$du4.320843@news1.frmt1.sfba.home.com>`

```
There also needs to be a way to include only the modules required by your
app...why distribute dialog system dll's, etc when they are not used by the
app? if app is single threaded, why distribute the multithreaded dll?...if
the app is a client side app, why distribute fileshare?...etc...etc...etc...

A wizard sounds like a good ideal to me...maybe have it create a directory
of runtime modules needed upon completion of the wizard...Or at minimum, an
exact list of modules required to distribute...
```

###### ↳ ↳ ↳ Re: NetExpress RunTime Distribution

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3866DB1F.99F41EFA@home.com>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <uxRGwhbS$GA.274@cpmsnbbsa05> <83ii07$rus$1@nntp2.atl.mindspring.net> <utBy57uT$GA.287@cpmsnbbsa05> <3865B99F.9BE31B2D@home.com> <gAw94.13524$du4.320843@news1.frmt1.sfba.home.com> <8467tc$4qu$1@nntp6.atl.mindspring.net>`

```


Ken Mullins wrote:
> 
> There also needs to be a way to include only the modules required by your
…[6 more quoted lines elided]…
> exact list of modules required to distribute...

Yes Ken, I think Gazloo misunderstood a bit. Let me just re-state it. Do
away with Distribution Diectory completely, all the files required exist
in the bin directories. Ask the "Wizard" questions and create
'customized' Support/RunTime according to developer's selection. We all
realize that many individual modules will be 'common' to variants of a
customized output - let developer pick his own name if necessary, and he
can select, as examples :- Multi-with-OO, Single-with-OO,
Dialog-System-with-OO, Dialog-System-Multi-Thread etc, etc....  Choosing
as many different versions as he may need, according to an
end-customer's requirements.

It then becomes a process of one program selecting from the bin
directories,( NOT Redistribution directory), and copying to a directory
for each customized RTE selected.

Hope that makes it just a bit clearer.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: NetExpress RunTime Distribution

_(reply depth: 8)_

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 1999-12-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LiC94.13801$du4.327653@news1.frmt1.sfba.home.com>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <uxRGwhbS$GA.274@cpmsnbbsa05> <83ii07$rus$1@nntp2.atl.mindspring.net> <utBy57uT$GA.287@cpmsnbbsa05> <3865B99F.9BE31B2D@home.com> <gAw94.13524$du4.320843@news1.frmt1.sfba.home.com> <8467tc$4qu$1@nntp6.atl.mindspring.net> <3866DB1F.99F41EFA@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote in message
news:3866DB1F.99F41EFA@home.com...
> Yes Ken, I think Gazloo misunderstood a bit. Let me just re-state it. Do
> away with Distribution Diectory completely, all the files required exist
> in the bin directories.

ya know, i don't think i did misunderstand; unless of course i've done it
again? ;-)

you're asking for custom RTE's -- i.e. only those files you need to host the
application. i can understand the need (why ship files you don't use), but
as i said, it does present some challenges for MERANT in terms of testing
all the various possible configurations of the RTE's. keeping the RTE whole
keeps it stable.
```

###### ↳ ↳ ↳ Re: NetExpress RunTime Distribution

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<846s6n$d0b$1@nntp9.atl.mindspring.net>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <uxRGwhbS$GA.274@cpmsnbbsa05> <83ii07$rus$1@nntp2.atl.mindspring.net> <utBy57uT$GA.287@cpmsnbbsa05> <3865B99F.9BE31B2D@home.com> <gAw94.13524$du4.320843@news1.frmt1.sfba.home.com> <8467tc$4qu$1@nntp6.atl.mindspring.net> <3866DB1F.99F41EFA@home.com> <LiC94.13801$du4.327653@news1.frmt1.sfba.home.com>`

```
Jimmy and Gary,
  The other possibility is to *NOT* test all the variations on packaged
RTEs - but instead to issue a "user-friendly" message if a required run-time
module is missing at a distributed site.  This should mean that the *ONLY*
bug that the end-user-site would have is that they are missing a module (some
answer in the Wizard was wrong - or not current).  This could be corrected by
the "distributor" of the RTE.  Any "bugs" other than this "missing module
one" should be "recreatable" with the full RTE - so MERANT not testing the
variations should make no difference.

NOTE WELL:
  If the end-user reported problem could NOT be recreated by the distributor
of the application - with the full RTE - then you are in deed in a "problem
condition".  However, I think that this is where the "onus" could be placed
on the distributor (to insure that the end-user had all the correct modules)
and get rid of Ken's problem of MERANT just refusing to deal with "different"
or "non-current" installations at end-user sites.
```

###### ↳ ↳ ↳ Re: NetExpress RunTime Distribution

_(reply depth: 10)_

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 1999-12-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vGC94.13807$du4.328554@news1.frmt1.sfba.home.com>`
- **References:** `<839cls$1i6$1@nntp9.atl.mindspring.net> <uxRGwhbS$GA.274@cpmsnbbsa05> <83ii07$rus$1@nntp2.atl.mindspring.net> <utBy57uT$GA.287@cpmsnbbsa05> <3865B99F.9BE31B2D@home.com> <gAw94.13524$du4.320843@news1.frmt1.sfba.home.com> <8467tc$4qu$1@nntp6.atl.mindspring.net> <3866DB1F.99F41EFA@home.com> <LiC94.13801$du4.327653@news1.frmt1.sfba.home.com> <846s6n$d0b$1@nntp9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:846s6n$d0b$1@nntp9.atl.mindspring.net...
> Jimmy and Gary,
>   The other possibility is to *NOT* test all the variations on packaged
> RTEs - but instead to issue a "user-friendly" message if a required
run-time
> module is missing at a distributed site.  This should mean that the *ONLY*
> bug that the end-user-site would have is that they are missing a module
(some
> answer in the Wizard was wrong - or not current).  This could be corrected
by
> the "distributor" of the RTE.  Any "bugs" other than this "missing module
> one" should be "recreatable" with the full RTE - so MERANT not testing the
> variations should make no difference.

sensible suggestions Bill.

also i think it's fair to expect that many of the problems of this type
would be found by the ISV during their own system test prior to customer
delivery.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
