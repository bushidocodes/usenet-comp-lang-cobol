[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Initializing a Linkage Section variable (On OS/390)

_21 messages · 11 participants · 2003-06_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Initializing a Linkage Section variable (On OS/390)

- **From:** chuck_leviton@yahoo.com (charles leviton)
- **Date:** 2003-06-24T13:10:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d280a253.0306241210.5baa00fc@posting.google.com>`

```
Hi,
I am primarily a CoolGEN developer using COBOL mostly to write
routines that will read files and CALLing these from CoolGEN.

Recently we encountered a situation where while stepping thru some
CoolGEN code (ie running in trace mode) some variables lost their
value after an invocation of a COBOL subroutine.
More by accident than design we tracked this down to an INITIALIZE
stmt in the COBOL program that was acting on a variable defined in the
LINKAGE SECTION.  When we moved the variable to WS the problem went
away.

So my question is what effect does it have when you initialize a
variable that is in the linkage section?
Thanks
```

#### ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-24T20:55:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef8b940.138496119@news.optonline.net>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com>`

```
chuck_leviton@yahoo.com (charles leviton) wrote:

>Hi,
>I am primarily a CoolGEN developer using COBOL mostly to write
…[11 more quoted lines elided]…
>variable that is in the linkage section.

Initialize clears the variable(s) to spaces if pic x, zero if pic 9, in either
section. Variables in working-storage are local to the COBOL program; variables
in linkage section are in the calling (CoolGEN) program's memory.
```

#### ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-06-24T17:43:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N_SdnfhppJ6ySWWjXTWJhg@giganews.com>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com>`

```

"charles leviton" <chuck_leviton@yahoo.com> wrote in message
news:d280a253.0306241210.5baa00fc@posting.google.com...
> Hi,
> I am primarily a CoolGEN developer using COBOL mostly to write
…[12 more quoted lines elided]…
> Thanks

The memory locations specified by the starting address + length of the
subprogram's named data item get set to blanks or zero. Suppose:

(calling program)
CALL 'A' USING X Y.  <== note two variables

(called program)
PROCEDURE DIVISION USING P Q R.  <== note subprogram expecting 3 variables
INITIALIZE P Q R.

You're screwed inasmuch as no starting address for "R" was passed by the
calling program (so the called program had to wing it). The  blanks/zeros
resulting from INITIALIZE could appear almost anywhere in memory (but
usually in the same place).

This is a fairly common mistake.

Note that SOME compilers catch this error at execution time.
```

##### ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** "Chuck Leviton" <Chuck_leviton@yahoo.com>
- **Date:** 2003-06-25T00:36:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<K86Ka.95484$nr.6272627@twister.southeast.rr.com>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <N_SdnfhppJ6ySWWjXTWJhg@giganews.com>`

```
Thanks all!  Glad to know it is a fairly common mistake!

"JerryMouse" <nospam@bisusa.com> wrote in message
news:N_SdnfhppJ6ySWWjXTWJhg@giganews.com...
>
> "charles leviton" <chuck_leviton@yahoo.com> wrote in message
…[36 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** "James" <magogrwr@bellsouth.net>
- **Date:** 2003-06-25T19:05:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hNpKa.29843$uK1.15530@fe05.atl2.webusenet.com>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <N_SdnfhppJ6ySWWjXTWJhg@giganews.com>`

```
Actually NO compiler catches ANYTHING at RUN-time.

"JerryMouse" <nospam@bisusa.com> wrote in message
news:N_SdnfhppJ6ySWWjXTWJhg@giganews.com...
>
> "charles leviton" <chuck_leviton@yahoo.com> wrote in message
…[36 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-06-25T19:48:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EFA42E6.8070700@Knology.net>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <N_SdnfhppJ6ySWWjXTWJhg@giganews.com> <hNpKa.29843$uK1.15530@fe05.atl2.webusenet.com>`

```
James wrote:
> Actually NO compiler catches ANYTHING at RUN-time.

:)
```

###### ↳ ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-06-25T20:26:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<X8ScnaLQiZd91mejXTWJjw@giganews.com>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <N_SdnfhppJ6ySWWjXTWJhg@giganews.com> <hNpKa.29843$uK1.15530@fe05.atl2.webusenet.com> <3EFA42E6.8070700@Knology.net>`

```

"LX-i" <DanielJSNOSPAM@Knology.net> wrote in message
news:3EFA42E6.8070700@Knology.net...
> James wrote:
> > Actually NO compiler catches ANYTHING at RUN-time.
>
> :)

Actually, my compiler catches hell every time I run it.
```

#### ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-06-24T18:30:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EF8DEFE.4010108@Knology.net>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com>`

```
charles leviton wrote:
> Hi,
> I am primarily a CoolGEN developer using COBOL mostly to write
…[11 more quoted lines elided]…
> variable that is in the linkage section?

Not to be smart, but you get exactly what describe above.  :)  Unless 
you specify otherwise, the variables you pass in the call are able to be 
changed by that called module.
```

#### ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-24T19:50:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdarko$t4$1@slb9.atl.mindspring.net>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com>`

```
Others have already replied, but in case another explanation would make this
any clearer ...

When you CALL a subprogram (in a  COBOL environment) and use the "default"
or explicitly state (in the CALLing program) that you are passing a
parameter "BY REFERENCE" - then the Linkage Section of the CALLed subprogram
just gets a "map" into the storage that is actually in the CALLing program.
Therefore, ANY (all) changes that you make in the subprogram to that Linkage
Section are ACTUALLY changing the field in the storage of the CALLing
program.

If you WANT to pass a parameter to a CALLed subprogram but do NOT want any
of the changes that occur in the subprogram to impact the storage of the
CALLing program, you should use the "BY CONTENT" phrase in the CALLing
program.  This will allow your subprogram to "get data" from the CALLing
program but prevent changes within the subprogram impacting the storage of
the CALLing program.

All of this is true whether you use INITIALIZE, MOVE, READ INTO or any other
"data changing" statement in the subprogram.

Contrary to the MIS-information in one of the replies to your question, the
INITIALIZE statement has several "options" that might impact what it does
and does not change (in any program - CALLing, or CALLed).  It is true that
BY DEFAULT it changes  *named* (not filler - not redefinition) alphanumeric
fields to spaces and numeric fields to zeroes.  However, there are lots of
other possibilities - depending upon exactly how you define the "receiving
field" and what features of INITIALIZE you use.

I don't think that any of this really impacts your "problem" - but did want
to correct the incomplete information posted elsewhere on INITIALIZE.
```

##### ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-25T13:19:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef8f932_3@news.athenanews.com>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <bdarko$t4$1@slb9.atl.mindspring.net>`

```
Funny thing...

I read ALL the responses (before yours, Bill) and wondered why no-one
bothered to explain the use of the various calling methods. How is it
helpful to someone who is experiencing the problem described, if they are
not aware that it is ONLY "BY REFERENCE" that will manifest in this way?

As usual, the quality of Bill's post is superb and covers ALL the bases.
(Jerry's point about a missed parameter was also valuable).

There is nothing I could/would add to Bill's response.

Pete.

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:bdarko$t4$1@slb9.atl.mindspring.net...
> Others have already replied, but in case another explanation would make
this
> any clearer ...
>
> When you CALL a subprogram (in a  COBOL environment) and use the "default"
> or explicitly state (in the CALLing program) that you are passing a
> parameter "BY REFERENCE" - then the Linkage Section of the CALLed
subprogram
> just gets a "map" into the storage that is actually in the CALLing
program.
> Therefore, ANY (all) changes that you make in the subprogram to that
Linkage
> Section are ACTUALLY changing the field in the storage of the CALLing
> program.
…[8 more quoted lines elided]…
> All of this is true whether you use INITIALIZE, MOVE, READ INTO or any
other
> "data changing" statement in the subprogram.
>
> Contrary to the MIS-information in one of the replies to your question,
the
> INITIALIZE statement has several "options" that might impact what it does
> and does not change (in any program - CALLing, or CALLed).  It is true
that
> BY DEFAULT it changes  *named* (not filler - not redefinition)
alphanumeric
> fields to spaces and numeric fields to zeroes.  However, there are lots of
> other possibilities - depending upon exactly how you define the "receiving
> field" and what features of INITIALIZE you use.
>
> I don't think that any of this really impacts your "problem" - but did
want
> to correct the incomplete information posted elsewhere on INITIALIZE.
>
…[21 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-06-24T21:13:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NCidnXzsoIenmGSjXTWJjQ@giganews.com>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <bdarko$t4$1@slb9.atl.mindspring.net> <3ef8f932_3@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3ef8f932_3@news.athenanews.com...
> Funny thing...
>
…[10 more quoted lines elided]…
> Pete.

Pete,

You're right. My response was deficient. I *assumed* the problem reported
was the result of an error I've made many times (and would be hard to
generate if BY VALUE was involved). Further, I *assumed* it wouldn't be
necessary to define in detail the vagaries of the INITIALIZE statement.

This is unusual for me; often when asked for a 3/8" socket I segue into the
origins of the metric system and how superior it is (did you know, for
example, that ALL American automotive engines have metric threads on spark
plugs and that they've always had them?).
```

##### ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-06-25T02:43:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c33ac3$8b809780$8bccf943@chottel>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <bdarko$t4$1@slb9.atl.mindspring.net>`

```
Correct as far as it goes, but I would make one comment. If the parameter
passed BY CONTENT is a POINTER then the copy of the pointer still points to
the original address which may then be changed.

-TOP POST- NO MORE FOLLOWS

William M. Klein <wmklein@ix.netcom.com> wrote in article
<bdarko$t4$1@slb9.atl.mindspring.net>...
> Others have already replied, but in case another explanation would make
this
> any clearer ...
> 
> When you CALL a subprogram (in a  COBOL environment) and use the
"default"
> or explicitly state (in the CALLing program) that you are passing a
> parameter "BY REFERENCE" - then the Linkage Section of the CALLed
subprogram
> just gets a "map" into the storage that is actually in the CALLing
program.
> Therefore, ANY (all) changes that you make in the subprogram to that
Linkage
> Section are ACTUALLY changing the field in the storage of the CALLing
> program.
> 
> If you WANT to pass a parameter to a CALLed subprogram but do NOT want
any
> of the changes that occur in the subprogram to impact the storage of the
> CALLing program, you should use the "BY CONTENT" phrase in the CALLing
> program.  This will allow your subprogram to "get data" from the CALLing
> program but prevent changes within the subprogram impacting the storage
of
> the CALLing program.
> 
> All of this is true whether you use INITIALIZE, MOVE, READ INTO or any
other
> "data changing" statement in the subprogram.
> 
> Contrary to the MIS-information in one of the replies to your question,
the
> INITIALIZE statement has several "options" that might impact what it does
> and does not change (in any program - CALLing, or CALLed).  It is true
that
> BY DEFAULT it changes  *named* (not filler - not redefinition)
alphanumeric
> fields to spaces and numeric fields to zeroes.  However, there are lots
of
> other possibilities - depending upon exactly how you define the
"receiving
> field" and what features of INITIALIZE you use.
> 
> I don't think that any of this really impacts your "problem" - but did
want
> to correct the incomplete information posted elsewhere on INITIALIZE.
> 
…[22 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-25T03:20:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef90fb4.160631331@news.optonline.net>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <bdarko$t4$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Contrary to the MIS-information in one of the replies to your question, the
>INITIALIZE statement has several "options" that might impact what it does
…[7 more quoted lines elided]…
>to correct the incomplete information posted elsewhere on INITIALIZE.

The options to which you refer were introduced in the 2002 standard. Unless
Charles is running CoolGEN on a Microsoft server, which is unlikely, AND has Net
Express 4.0, even more unlikely, the only INITIALIZE option in his COBOL is
REPLACING.
```

###### ↳ ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-06-25T01:00:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vfib66emp8fv81@corp.supernews.com>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <bdarko$t4$1@slb9.atl.mindspring.net> <3ef90fb4.160631331@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3ef90fb4.160631331@news.optonline.net...
> "William M. Klein" <wmklein@ix.netcom.com> wrote:
>
> >Contrary to the MIS-information in one of the replies to your question,
the
> >INITIALIZE statement has several "options" that might impact what it does
> >and does not change (in any program - CALLing, or CALLed).  It is true
that
> >BY DEFAULT it changes  *named* (not filler - not redefinition)
alphanumeric
> >fields to spaces and numeric fields to zeroes.  However, there are lots
of
> >other possibilities - depending upon exactly how you define the
"receiving
> >field" and what features of INITIALIZE you use.
> >
> >I don't think that any of this really impacts your "problem" - but did
want
> >to correct the incomplete information posted elsewhere on INITIALIZE.
>
> The options to which you refer were introduced in the 2002 standard.
Unless
> Charles is running CoolGEN on a Microsoft server, which is unlikely, AND
has Net
> Express 4.0, even more unlikely, the only INITIALIZE option in his COBOL
is
> REPLACING.

'Microsoft server'? 'Net Express'? The Subject says '(On OS/390)'.
You misinformed by stating the absolute behavior: "Initialize clears
the variable(s) to spaces if pic x, zero if pic 9, in either section.",
thus dismissing any possible effect for REPLACING. Mr Klein need
not rely upon the 2002 COBOL standard for his statements to be
correct concerning your post and you, Mr Wagner, are not even
mentioned in his!
```

###### ↳ ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-25T02:14:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdbi7f$dvm$1@slb5.atl.mindspring.net>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <bdarko$t4$1@slb9.atl.mindspring.net> <3ef90fb4.160631331@news.optonline.net>`

```
Of course RW is wrong again (see below for his part, I am "top posting" my
full reply)

The BY phrase has been part of the INITIALIZE statement since it was
introduced in 1985.  The BY phrase allows any of a specific set of
field-types to be initialized to any "valid" sending field value.  Spaces
and zeroes are (and - for as long as INITIALIZE has been a part of Standard
COBOL) *only* the default.

It is true that the 2002 Standard introduces several NEW features that are
also useful - but learning what is Standard (and available in many/most
existing compilers) will help others who may be as inaccurate in their
knowledge of COBOL as RW is.
```

###### ↳ ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-25T09:02:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef96368.182062710@news.optonline.net>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <bdarko$t4$1@slb9.atl.mindspring.net> <3ef90fb4.160631331@news.optonline.net> <bdbi7f$dvm$1@slb5.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>Of course RW is wrong again (see below for his part, I am "top posting" my
>full reply)
…[5 more quoted lines elided]…
>COBOL) *only* the default.

You're really clutching at straws to make me look stupid. This borders on
deceit. The "BY phrase" is part of the REPLACING clause I mentioned. The 85
syntax is:

INITIALIZE { identifier-1 } ...
THEN REPLACING category-name DATA BY identifier-2 or
literal-1 

>It is true that the 2002 Standard introduces several NEW features that are
>also useful - but learning what is Standard (and available in many/most
>existing compilers) will help others who may be as inaccurate in their
>knowledge of COBOL as RW is.

If the criterion is many/most existing compilers, specifically OS/390, why do
you confuse the issue by mentioning features which don't exist in that realm? Is
your goal to inform the original poster, or is it to make RW look stupid? We
both know the answer, as does everyone else who has followed the saga.

Your claim of 'fact-based' becomes increasing weaker with each posting. You're
now intentionally twisting words to support your thesis that I'm inaccurate.
Keep it up and I'll write a caution advising newcomers of your disingenuity ..
supported by Facts like this one and others to come, evinced by Google searches.


Wake up and stop being an asshole. The spamming and word-twisting is digging you
into a hole. Please return to your former dignified persona. 

----- history below -----
>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3ef90fb4.160631331@news.optonline.net...
…[28 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-25T08:28:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdc81f$svs$1@slb3.atl.mindspring.net>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <bdarko$t4$1@slb9.atl.mindspring.net> <3ef90fb4.160631331@news.optonline.net> <bdbi7f$dvm$1@slb5.atl.mindspring.net> <3ef96368.182062710@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3ef96368.182062710@news.optonline.net...
> "William M. Klein" <wmklein@ix.netcom.com> wrote:
>
<snip>
>
> You're really clutching at straws to make me look stupid. This borders on
> deceit. The "BY phrase" is part of the REPLACING clause I mentioned. The
85
> syntax is: ...
>
But in YOUR ORIGINAL NOTE  you indicated that INITIALIZE moves spaces or
zeroes to a field - thus in that note, you DO ignore the REPLACE portion of
the syntax completely.  You also impied (or it is possible that I infered)
that this happened to ALL fields in the record that was INITIALIZED (which
relates to one of your old problems with INITIALIZE)


>
> If the criterion is many/most existing compilers, specifically OS/390, why
do
> you confuse the issue by mentioning features which don't exist in that
realm? Is
> your goal to inform the original poster, or is it to make RW look stupid?
We
> both know the answer, as does everyone else who has followed the saga.
>

My exact words (in my original post) were,

"I don't think that any of this really impacts your "problem" - but did want
to correct the incomplete information posted elsewhere on INITIALIZE.


I am not at all worried (personally) about how people view this "saga" - as
long as they do understand what INITIALIZE does and does not do - and don't
simply read and believe your original note.
```

###### ↳ ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

_(reply depth: 6)_

- **From:** Rosa Fischer <Rosa.Fischer@fujitsu-siemens.com>
- **Date:** 2003-06-26T08:01:02+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EFA8C1E.97A08988@fujitsu-siemens.com>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <bdarko$t4$1@slb9.atl.mindspring.net> <3ef90fb4.160631331@news.optonline.net> <bdbi7f$dvm$1@slb5.atl.mindspring.net> <3ef96368.182062710@news.optonline.net> <bdc81f$svs$1@slb3.atl.mindspring.net>`

```
> With the new standard I see another possibility to use an "INITIALIZE"
> statement for data defined in the LINKAGE SECTION, where the data definition
> is not used as parameter by the calling program:

working-storage section.
01 w pic x(100).

linkage section.
01 a pic x(100).
01 b based.
     02 b1 occurs 10 indexed by i pic x(10).

PROCEDURE DIVISION using a.
1st section.
1.
            set address of b to address of w.
* this means w is filled with spaces
            initialize b.

           set address of b to address of a.
* this means b is filled with spaces
           initialize b.

The new standard allows to define b in LINKAGE SECTION or in WORKING-STORAGE or
LOCAL-STORAGE SECTION.

Best wishes from old Europe
Rosa Fischer
```

###### ↳ ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-26T12:19:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdf9un$r4p$1@slb9.atl.mindspring.net>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <bdarko$t4$1@slb9.atl.mindspring.net> <3ef90fb4.160631331@news.optonline.net> <bdbi7f$dvm$1@slb5.atl.mindspring.net> <3ef96368.182062710@news.optonline.net> <bdc81f$svs$1@slb3.atl.mindspring.net> <3EFA8C1E.97A08988@fujitsu-siemens.com>`

```
To expand upon Rosa's commetns below.

In the 2002 Standard, it is legal (not just an extention) to have a VALUE
clause in the Linkage (or File) sections.  Along with the *new* INITIALIZE
TO VALUE feature, the code below can be expanded as follows. (I haven't
"compiled" this - so there may be some typos)


 01 w.   *>  pic x(100)
    05 W-Alpha Pic X(80) Value Low-Values.
    05  W-Num  Pic 9(20) Value 123.

 linkage section.
 01 a pic x(100).
    05  a-Alpha Pic X(80) Value High-Values.
    05  a-Num  Pic 9(20) Value 987.

 01 b based.
      02 b1 occurs 10 indexed by i pic x(10)
*>  The following is the new format of VALUE clauses for tables
           Value Quote from 1 to 9 Zeroes 10.

 PROCEDURE DIVISION using a.
 1st section.
 1.
             set address of b to address of w.
 *> The following will use the VALUE clauses under B to filling the datat
 *> for both the "mappings" at  B and W
            initialize b to Value.

            set address of b to address of a.
 *> The following will still use the mapping of "B" to initialize the
storage poiinted to
 *> at B and A
            initialize b to Value.
            Move A to W
*> the following will initialize both the mappings at A and B to the values
from A
           initialize A to Value.
```

##### ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** chuck_leviton@yahoo.com (charles leviton)
- **Date:** 2003-06-25T05:42:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d280a253.0306250442.5965d249@posting.google.com>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <bdarko$t4$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message news:<bdarko$t4$1@slb9.atl.mindspring.net>...
> Others have already replied, but in case another explanation would make this
> any clearer ...
…[30 more quoted lines elided]…
> --
Thank you, Bill.  I can vaguely recollect from my C programming
classes in school the concept of putting an ampersand (or it might
have been an asterisk) before a variable name when using it as an
argument in a function call.  In this case the function would actually
change the value of the variable itself as opposed to changing the
value of a copy of the variable.  We called it "Call by Value" vs
"Call By reference"

I looked at the COBOL code generated by CoolGEN (something one should
avoid if you can!) and since it doesn't explicitly say CONTENT it must
be a CALL by REFERENCE.
```

###### ↳ ↳ ↳ Re: Initializing a Linkage Section variable (On OS/390)

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-06-25T09:21:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-C4B81B.09212325062003@corp.supernews.com>`
- **References:** `<d280a253.0306241210.5baa00fc@posting.google.com> <bdarko$t4$1@slb9.atl.mindspring.net> <d280a253.0306250442.5965d249@posting.google.com>`

```
In article <d280a253.0306250442.5965d249@posting.google.com>,
 chuck_leviton@yahoo.com (charles leviton) wrote:
> Thank you, Bill.  I can vaguely recollect from my C programming
> classes in school the concept of putting an ampersand (or it might
…[4 more quoted lines elided]…
> "Call By reference"


Creator of Pascal Nick Wirth (pronounced "wert", but oftem mispronounced 
"worth") once quipped that Europeans call him by name ("wirth"), while 
Americans call him by value ("worth").
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
