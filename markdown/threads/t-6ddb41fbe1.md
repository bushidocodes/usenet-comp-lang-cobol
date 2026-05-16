[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS

_8 messages · 6 participants · 2003-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS

- **From:** "Janek" <neuros@polbox.com>
- **Date:** 2003-08-26T18:06:57+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<big0jm$mhr$1@atlantis.news.tpi.pl>`

```
Hi.

Can I call JCL, REX or unix functions(OMVS) from Cobol program under CICS?
I'm looking for documentation.

thanks
```

#### ↳ Re: CICS

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-08-26T18:37:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ON2b.14321$8i2.10650@newsread2.news.atl.earthlink.net>`
- **References:** `<big0jm$mhr$1@atlantis.news.tpi.pl>`

```
What do you actually WANT to do (what function)?  There may be a way to do
it, but from your question (as written) the general answer is NO.  (I think
there WAS a "REXX" - not "REX" for CICS, but I am not certain it is still
supported)
```

#### ↳ Re: CICS

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-08-26T19:59:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-BE06AD.19592226082003@corp.supernews.com>`
- **References:** `<big0jm$mhr$1@atlantis.news.tpi.pl>`

```
In article <big0jm$mhr$1@atlantis.news.tpi.pl>,
 "Janek" <neuros@polbox.com> wrote:

> Hi.
> 
…[4 more quoted lines elided]…
> 


You can not call a JCL procedure from CICS.  Though you can write a job 
stream using the SPOOL OPEN/WRITE/CLOSE, it is one way.  There is no way 
to get any results or return status about the stream.

You can use Rexx if your sysprogs have installed the necessaries.  You 
can also use Java under the same conditions.

You can use the various Unix API calls, but only if the region you are 
running in has certain things configured.  For example, the CICS region 
will at the very least need a USS security segment or every call is 
going to cause the region to die with an S913.  There are other possible 
requirements depending on what you want to do, again, check with your 
sysprogs.
```

##### ↳ ↳ Re: CICS

- **From:** "Janek" <neuros@polbox.com>
- **Date:** 2003-08-27T10:10:36+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bihp41$l8p$1@nemesis.news.tpi.pl>`
- **References:** `<big0jm$mhr$1@atlantis.news.tpi.pl> <joe_zitzelberger-BE06AD.19592226082003@corp.supernews.com>`

```
I want to use commands compress/uncompress from omvs.
I have file that was compressed by compress command. I want to uncompress
this file in Cobol program under CICS. Next i want to read this file.

Where can i find documentation for Unix API?

U�ytkownik "Joe Zitzelberger" <joe_zitzelberger@nospam.com> napisa� w
wiadomo�ci news:joe_zitzelberger-BE06AD.19592226082003@corp.supernews.com...
> In article <big0jm$mhr$1@atlantis.news.tpi.pl>,
>  "Janek" <neuros@polbox.com> wrote:
…[3 more quoted lines elided]…
> > Can I call JCL, REX or unix functions(OMVS) from Cobol program under
CICS?
> > I'm looking for documentation.
> >
…[16 more quoted lines elided]…
> sysprogs.
```

###### ↳ ↳ ↳ Re: CICS

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-08-27T13:08:58+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<il0pkvg2dip4e1176ra0apjivq52v252me@4ax.com>`
- **References:** `<big0jm$mhr$1@atlantis.news.tpi.pl> <joe_zitzelberger-BE06AD.19592226082003@corp.supernews.com> <bihp41$l8p$1@nemesis.news.tpi.pl>`

```
On Wed, 27 Aug 2003 10:10:36 +0200 "Janek" <neuros@polbox.com> wrote:

:>I want to use commands compress/uncompress from omvs.
:>I have file that was compressed by compress command. I want to uncompress
:>this file in Cobol program under CICS. Next i want to read this file.

Well, I really don't think there is a way to do this without having your CICS
systems programmer breaking your fingers.

But, if I had to do it, I would create an MVS subtask under CICS, have your
CICS transaction post a request to the subtask and then do a CICS wait for the
subtask to complete the compression / decompression.

This is not stuff for those weak at heart.

:>Where can i find documentation for Unix API?

:>Uï¿½ytkownik "Joe Zitzelberger" <joe_zitzelberger@nospam.com> napisaï¿½ w
:>wiadomoï¿½ci news:joe_zitzelberger-BE06AD.19592226082003@corp.supernews.com...
:>> In article <big0jm$mhr$1@atlantis.news.tpi.pl>,
:>>  "Janek" <neuros@polbox.com> wrote:
:>>
:>> > Hi.
:>> >
:>> > Can I call JCL, REX or unix functions(OMVS) from Cobol program under
:>CICS?
:>> > I'm looking for documentation.
:>> >
:>> > thanks
:>> >
:>>
:>>
:>> You can not call a JCL procedure from CICS.  Though you can write a job
:>> stream using the SPOOL OPEN/WRITE/CLOSE, it is one way.  There is no way
:>> to get any results or return status about the stream.
:>>
:>> You can use Rexx if your sysprogs have installed the necessaries.  You
:>> can also use Java under the same conditions.
:>>
:>> You can use the various Unix API calls, but only if the region you are
:>> running in has certain things configured.  For example, the CICS region
:>> will at the very least need a USS security segment or every call is
:>> going to cause the region to die with an S913.  There are other possible
:>> requirements depending on what you want to do, again, check with your
:>> sysprogs.
```

###### ↳ ↳ ↳ Re: CICS

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-08-27T09:15:04-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-68D575.09150327082003@corp.supernews.com>`
- **References:** `<big0jm$mhr$1@atlantis.news.tpi.pl> <joe_zitzelberger-BE06AD.19592226082003@corp.supernews.com> <bihp41$l8p$1@nemesis.news.tpi.pl>`

```
In article <bihp41$l8p$1@nemesis.news.tpi.pl>,
 "Janek" <neuros@polbox.com> wrote:

> I want to use commands compress/uncompress from omvs.
> I have file that was compressed by compress command. I want to uncompress
> this file in Cobol program under CICS. Next i want to read this file.

It sounds like this is not something you really want to get done under 
CICS.  If the file is compressed, can I assume it is quite large?  It 
would be quite detrimental to the region to uncompress and then read an 
entire file.

If you really need to process the file online, do the uncompress in a 
batch job (perhaps triggered by a SPOOLed job).  And have your 
transaction wait for the file to be opened by your batch job.

That is a big if though.  Could you not do the processing in a batch job?


> Where can i find documentation for Unix API?

There are many books.  I happen to like Curry's Unix System Programming 
for SvR4 and Chan's Unix System Programming Using C++.  But your 
compiler reference will have all the various system calls, including the 
ones to start a new shell and pass it the uncompress command.  Also 
check out the z/OS C/C++ Programmers Guide.
```

###### ↳ ↳ ↳ Re: CICS

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2003-08-27T21:40:32+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<270820032140327927%josephk@iinet.net.au>`
- **References:** `<big0jm$mhr$1@atlantis.news.tpi.pl> <joe_zitzelberger-BE06AD.19592226082003@corp.supernews.com> <bihp41$l8p$1@nemesis.news.tpi.pl>`

```
Look into using the EXCI interface of CICS.

This allows you to create a batch job which will uncompress the file,
extract the information and then call invoke a program in CICS passing
the information you just extracted. This program can then do any CICS
things it might need to do.

EXCI is an RPC interface from any MVS address space to CICS.

In article <bihp41$l8p$1@nemesis.news.tpi.pl>, Janek
<neuros@polbox.com> wrote:

> I want to use commands compress/uncompress from omvs.
> I have file that was compressed by compress command. I want to uncompress
…[33 more quoted lines elided]…
>
```

#### ↳ Re: CICS

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-08-27T17:09:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030827130950.17961.00000023@mb-m01.aol.com>`
- **References:** `<big0jm$mhr$1@atlantis.news.tpi.pl>`

```
Janek, neuros@polbox.com 
On: 8/26/03 11:06 AM EST

posted<<

Can I call JCL, REX or unix functions(OMVS) from Cobol program under CICS?
I'm looking for documentation.
>>

It is possible for CICS programs to write to what is called the 'internal
reader.' (also note that REXX can write to it also). This can be code as normal
CICS. I'm thinking it is actually a queue with a name like 'intrdr' or some
such. The CICS documentation should give you cross references to this.

The successful approaches I have seen submit jobs that invoke PROCs (an
instream PROC can be included any time in this sort of thing, if that matters
to you.)  But the only status information you are going to get is the status of
the CICS command sequence that writes the lines of the JCL. So it is not clear
that that will help you.

For my two cents worth, I would agree with the responses you are getting that
say if you are
considering decompressing some received file in CICS, then don't.

You may want to be a little more detailed in your
statement that, among other functions, you want to 'receive' a compressed file.
 Is it permissible for you to post what technology is sending it?

If some technology is going to send it and receive it into your OS environ, and
if, this is somehow sensible to an executable CICS transaction, you could use
the internal reader to schedule a job to decompress it and do any number of
things. 

It is possible to schedule routine jobs that might, on a time basis, look for
decompressed results and get yet another transaction for a CICS program that
would then read your file as you indicate you want to do, etc.  But if you want
this all as one transaction function it sounds too big, from your initial post.

However, trust that it is true that there are some really big CICS programs
that work. You might, if you actually need realtime processing for all of this,
and if you can get to the compression functionality as a callable capability
just write the file yourself instead of using JCL or REXX; those after all are
just scripting languages.

CICS has writes.  And CICS can definitely call programs with its CALL command
(and in some shops is allowed to do native language calls).

What do you plan to use to do the decompress?

After you do this, you can actually just read and process in the original
transaction process or CALL some more good code to read and process.

Is there anything about the decompression logic that makes it unavailable to
you in the initial 
real-time transaction?  If so that problem is leading you to JCL and REXX, and
the core issue is how to sense the end (and sense the success for that matter)
of the task that executes as a batch job or Time Share program. That is less
straight forward. 

There are probably good folks here who can tell you how to get batch MVS to
trigger a CICS transaction, that could complete your loop back.
(my experience is complicated by having seen IMS BMPs get into all this which
is not relevant).

So getting to JCL is probably not hard, getting back the return code (besides
the file) is hard.
So, if you can tell us about your decompressor,
as potentially a CICS transaction subfunction
plug-in.  And if you can tell us what 'receive' means. What technology
telecommunicates it into CICS in you plan?

Best Wishes,
Robert K. Rayhawk
RKRayhawk@aol.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
