[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Advise on program structure needed

_32 messages · 19 participants · 2003-04 → 2003-06_

---

### Advise on program structure needed

- **From:** aliensite@excite.com (aliensite)
- **Date:** 2003-04-13T23:01:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com>`

```
I am learning COBOL and the programs structure in my text don't always
seem logical. Luckly my professor is a COBOL programmer who gives us
real world tips. He advises to use a period after each statement, but
I find one period after a paragraph easier to read. I don't like big
words since I am not a good spell checker, and I try to write code
that is modular, easy to read and modify. My final project produces a
report, I listed the paragraphs below. Is this structure ok? Thanks.

PROCEDURE DIVISION.                                              
    PERFORM 1000-INIT                                            
    PERFORM 2000-READ                                            
    PERFORM 3000-MAIN UNTIL EOF-SW = "Y"                         
    PERFORM 4000-TERM                                            
    GOBACK.                                                      

1000-INIT.

2000-READ.

3000-MAIN.
3100-PAGE-HEADINGS.
3200-DETAIL-LINE.
3210-VALIDATE.
3300-ADD-TOTALS.

4000-TERM.
4100-TOTAL-LINE.
4200-CLOSE-FILES.
```

#### ↳ Re: Advise on program structure needed

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-14T07:24:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9a5dd7.39995547@news.optonline.net>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com>`

```
aliensite@excite.com (aliensite) wrote:

>I am learning COBOL and the programs structure in my text don't always
>seem logical. Luckly my professor is a COBOL programmer who gives us
…[25 more quoted lines elided]…
>4200-CLOSE-FILES.


Your structure is ok -- it has a beginning, middle and end. But your
nomenclature sucks. Get rid of those four digit numbers. They were invented for
working on hard-copy program listings. Now that we use text editors, they just
get in the way. And stop writing in upper case. 

I would change 3000-MAIN to 'one-record' or 'one-detail-record'. I would put
TOTAL-LINE on par with DETAIL-LINE.
```

##### ↳ ↳ Re: Advise on program structure needed

- **From:** aliensite@excite.com (aliensite)
- **Date:** 2003-04-14T07:17:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ca0d9b0f.0304140617.41bc8bf@posting.google.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <3e9a5dd7.39995547@news.optonline.net>`

```
Thanks for the feedback, unfortunately WYLBUR uses uppercase :(

robert@wagner.net (Robert Wagner) wrote in message news:<3e9a5dd7.39995547@news.optonline.net>...
> 
> Your structure is ok -- it has a beginning, middle and end. But your
…[5 more quoted lines elided]…
> TOTAL-LINE on par with DETAIL-LINE.
```

##### ↳ ↳ Re: Advise on program structure needed

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-04-16T02:51:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030415225150.18724.00000658@mb-fn.aol.com>`
- **References:** `<3e9a5dd7.39995547@news.optonline.net>`

```
>From: robert@wagner.net  (Robert Wagner)
>Date: 4/14/03 3:24 AM Eastern Daylight Time

> Get rid of those four digit numbers. They were invented for
>working on hard-copy program listings. Now that we use text editors, they
>just
>get in the way. 

In addition to the other comments on this it may be that he has to turn in a
hard copy to the prof for grading (very hard to red pencil a text editor -
makes the screen messy).  Also can be useful with the cross reference that
alphabetises so they will list in order as coded.  Useful at the beginning -
kinda like training wheels.

>And stop writing in upper case. 

Not only does WYLBUR require upper case - so does the mainframe, at least all
the ones I've worked on so far .  While I may type in lower case the editor
upper cases it automatically and if I were to cut/paste the code here it would
be in upper case.  Please get the flea out of your undergarment on this one.
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-16T00:18:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ip34$peh$1@slb3.atl.mindspring.net>`
- **References:** `<3e9a5dd7.39995547@news.optonline.net> <20030415225150.18724.00000658@mb-fn.aol.com>`

```
"YukonMama" <yukonmama@aol.com> wrote in message
news:20030415225150.18724.00000658@mb-fn.aol.com...
> >From: robert@wagner.net  (Robert Wagner)
> >Date: 4/14/03 3:24 AM Eastern Daylight Time
>
<snip>
>
> >And stop writing in upper case.
>
> Not only does WYLBUR require upper case - so does the mainframe, at least
all
> the ones I've worked on so far .  While I may type in lower case the
editor
> upper cases it automatically and if I were to cut/paste the code here it
would
> be in upper case.  Please get the flea out of your undergarment on this
one.
>

This surprises me.  Even in the late '80s when VS COBOL II first started
accepting mixed case COBOL, I used ISPF settings for COBOL source code (with
the IBM environment) that fully supported mixed case.

What tools are you using that require upper-case source code?
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

_(reply depth: 4)_

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-04-16T05:44:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0304160444.e54a291@posting.google.com>`
- **References:** `<3e9a5dd7.39995547@news.optonline.net> <20030415225150.18724.00000658@mb-fn.aol.com> <b7ip34$peh$1@slb3.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message news:<b7ip34$peh$1@slb3.atl.mindspring.net>...
> "YukonMama" <yukonmama@aol.com> wrote in message
> news:20030415225150.18724.00000658@mb-fn.aol.com...
…[21 more quoted lines elided]…
> What tools are you using that require upper-case source code?

ISPF tends to default to "CAPS ON", which will uppercase each line as
it is entered.

This default can be changed, but only if you know about it.  It is
additionally complicated by any site installation options and user
modes that can alter the behavior (like CAPS(ON) on a custom edit
panel).

This can be turned off in ones profile, but ISPF will also flip it
back on if it ever notices you editing an all uppercase document in
"CAPS OFF" mode.  It is just trying to be helpful.
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

_(reply depth: 4)_

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-04-16T05:44:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0304160444.3d73c222@posting.google.com>`
- **References:** `<3e9a5dd7.39995547@news.optonline.net> <20030415225150.18724.00000658@mb-fn.aol.com> <b7ip34$peh$1@slb3.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message news:<b7ip34$peh$1@slb3.atl.mindspring.net>...
> "YukonMama" <yukonmama@aol.com> wrote in message
> news:20030415225150.18724.00000658@mb-fn.aol.com...
…[21 more quoted lines elided]…
> What tools are you using that require upper-case source code?

ISPF tends to default to "CAPS ON", which will uppercase each line as
it is entered.

This default can be changed, but only if you know about it.  It is
additionally complicated by any site installation options and user
modes that can alter the behavior (like CAPS(ON) on a custom edit
panel).

This can be turned off in ones profile, but ISPF will also flip it
back on if it ever notices you editing an all uppercase document in
"CAPS OFF" mode.  It is just trying to be helpful.
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

_(reply depth: 4)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-04-18T02:32:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030417223243.18914.00000095@mb-m18.aol.com>`
- **References:** `<b7ip34$peh$1@slb3.atl.mindspring.net>`

```
>From: "William M. Klein" wmklein@ix.netcom.com 
>Date: 4/16/03 1:18 AM Eastern Daylight Time

>This surprises me.  Even in the late '80s when VS COBOL II first started
>accepting mixed case COBOL, I used ISPF settings for COBOL source code (with
>the IBM environment) that fully supported mixed case.
>
>What tools are you using that require upper-case source code?


Perhaps 'require' was a poor choice of word.   I'm a predominately Roscoe user
and the default is upper case.  One can change the default to mixed case but in
all shops that I've been in that use it have it with the default.

I'm not sure what the default is on my ISPF as I don't use it for source code
editing and when file editing it just does what it wants which is usually what
I don't :).  However those in my shop that do use Elipse I believe also end up
with upper case as the default.

There isn't any source code in the shop that isn't in upper case.  Any lower
case is in literals.
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-17T02:20:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9e0e3c.281796915@news.optonline.net>`
- **References:** `<3e9a5dd7.39995547@news.optonline.net> <20030415225150.18724.00000658@mb-fn.aol.com>`

```
yukonmama@aol.com (YukonMama) wrote:

>>From: robert@wagner.net  (Robert Wagner)

>Not only does WYLBUR require upper case - so does the mainframe, at least all
>the ones I've worked on so far .  While I may type in lower case the editor
>upper cases it automatically and if I were to cut/paste the code here it would
>be in upper case.  Please get the flea out of your undergarment on this one.

Assuming you're referring to ISPF, that's an option. You can turn it off with
CAPS(OFF).
```

##### ↳ ↳ Re: Advise on program structure needed

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2003-06-14T07:48:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FcKdnWflTO0ThHajXTWcrg@comcast.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <3e9a5dd7.39995547@news.optonline.net>`

```
In article <3e9a5dd7.39995547@news.optonline.net>, robert@wagner.net wrote:

>Get rid of those four digit numbers. They were invented for working on 
>hard-copy program listings. Now that we use text editors, they just get
>in the way. 

What do you think we used to write COBOL programs in the past? :-)

Keep the numbering. It'll help you track logic flow, etc.
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

- **From:** docdwarf@panix.com
- **Date:** 2003-06-14T10:47:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcfci0$2pm$1@panix5.panix.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <3e9a5dd7.39995547@news.optonline.net> <FcKdnWflTO0ThHajXTWcrg@comcast.com>`

```
In article <FcKdnWflTO0ThHajXTWcrg@comcast.com>,
Ubiquitous <weberm@polaris.net> wrote:
>In article <3e9a5dd7.39995547@news.optonline.net>, robert@wagner.net wrote:
>
…[4 more quoted lines elided]…
>What do you think we used to write COBOL programs in the past? :-)

I do not know who 'we' are in this instance, nor do I know when 'the past' 
was precisely... but some, at times, used coding-sheets which were handed 
to 'keypunch girls' (that's what they were called, aye) who generated 
edecks of Hollerith cards.

>
>Keep the numbering. It'll help you track logic flow, etc.

Keep the numbering *or* lose the numbering... depending on what the 
standards are of the shop in which you choose to work.

DD
```

#### ↳ Re: Advise on program structure needed

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-14T07:12:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OeWcnRBkd_grOAejXTWJhA@giganews.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com>`

```

"aliensite" <aliensite@excite.com> wrote in message
news:ca0d9b0f.0304132201.76fc0f6e@posting.google.com...
> I am learning COBOL and the programs structure in my text don't always
> seem logical. Luckly my professor is a COBOL programmer who gives us
…[25 more quoted lines elided]…
> 4200-CLOSE-FILES.

Excellent. Don't forget to include more comments than may seem necessary to
explain the inner workings.

Your paragraph-numbering scheme is likewise good practice.
```

##### ↳ ↳ Re: Advise on program structure needed

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-04-14T17:53:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0304141300.78cf76d9@posting.google.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <OeWcnRBkd_grOAejXTWJhA@giganews.com>`

```
Hi A,

Well done, but the real challenge comes with the addition of control
breaks. Fer instance, how do you code your report pgm when the
xactions contain order info for products invoiced on differing dates
for various accounts managed by each of the sales districts in the
organization you work for?

BTW, FWIW, numbered pgraphs always gave me a "feel" for where I was in
the code when viewing it on paper or in an editor. Sometimes it's
easier to page up or down than to issue a "find".

I find that it's "safer" to copy code from one place to another in a
pgm when there's no chance for a period to prematurely terminate an
"IF" stmt.

Just can't get used to upper/lower case code. One question: Are
My-Fld, MY-FLD, my-fld, equivilant? Or will referencing one by another
cause a compiler error?

Regards, Jack.     



"JerryMouse" <nospam@bisusa.com> wrote in message news:<OeWcnRBkd_grOAejXTWJhA@giganews.com>...
> "aliensite" <aliensite@excite.com> wrote in message
> news:ca0d9b0f.0304132201.76fc0f6e@posting.google.com...
…[32 more quoted lines elided]…
> Your paragraph-numbering scheme is likewise good practice.
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T03:18:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9b796b.112602677@news.optonline.net>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <OeWcnRBkd_grOAejXTWJhA@giganews.com> <8a2d426e.0304141300.78cf76d9@posting.google.com>`

```
jacksleight@hotmail.com (Jack Sleight) wrote:

>Just can't get used to upper/lower case code. One question: Are
>My-Fld, MY-FLD, my-fld, equivilant? Or will referencing one by another
>cause a compiler error?

In COBOL, they're the same. You will not get a compiler error.
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-04-17T23:17:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IqycnTDPX__K8wKjXTWcoQ@comcast.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <OeWcnRBkd_grOAejXTWJhA@giganews.com> <8a2d426e.0304141300.78cf76d9@posting.google.com>`

```

"Jack Sleight" <jacksleight@hotmail.com> wrote in message
news:8a2d426e.0304141300.78cf76d9@posting.google.com...
> Hi A,
>
…[13 more quoted lines elided]…
>

    Classroom programs are unlikely to be big enough
to make numbered paragraphs useful.  As with so many
other options, it all depends on what you get used to.

    I used to be happy with a 25x80 screen.  They now make
me feel like I am peering thru a keyhole.

    The jury is still out on periods.  The "stick a period everywhere
they will fit" school causes extra work when gathering several
lines into a single if, and as you noted, can terminate an if
prematurely.

    On the other hand, the "one and only one period" school
can have trouble with If's that extend farther than you would like.

RE  (View in courier)

IF A = B
        DO THIS
ELSE
        IF A = C
              DO THAT
END-IF                        *> If you put a period here,
                                   *> the error goes away
MORE CODE
END OF PARAGRAPH.


MORE-CODE will be part of the if, but clearly (if the indents survive),
should not.  But it will (should?) compile cleanly.


    I personally think that the "few periods" style will win, now
that we have END-IF.  I can't tell you how many times END-IF
has saved me a bug by forceing a compile error, ie

IF A = B
             DO THIS
             DO THIS ALSO.            *> NOTE PERIOD
             MORE STUFF
END-IF.

        This will fail to compile.






> Just can't get used to upper/lower case code. One question: Are
> My-Fld, MY-FLD, my-fld, equivilant? Or will referencing one by another
…[6 more quoted lines elided]…
> "JerryMouse" <nospam@bisusa.com> wrote in message
news:<OeWcnRBkd_grOAejXTWJhA@giganews.com>...
> > "aliensite" <aliensite@excite.com> wrote in message
> > news:ca0d9b0f.0304132201.76fc0f6e@posting.google.com...
…[29 more quoted lines elided]…
> > Excellent. Don't forget to include more comments than may seem necessary
to
> > explain the inner workings.
> >
> > Your paragraph-numbering scheme is likewise good practice.
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

_(reply depth: 4)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-04-19T11:07:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0304191007.5bd82617@posting.google.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <OeWcnRBkd_grOAejXTWJhA@giganews.com> <8a2d426e.0304141300.78cf76d9@posting.google.com> <IqycnTDPX__K8wKjXTWcoQ@comcast.com>`

```
Hi Russell,

I would have coded it:


IF A = B
   DO THIS
ELSE
   IF A = C
      DO THAT
   END-IF      *> extra end-if
END-IF                        *> If you put a period here,
                                   *> the error goes away
MORE CODE
END OF PARAGRAPH
.              *> separate line in the event I need to copy "end of pgraph" 

On the other hand I'm not a purist. If the end-ifs got out of hand I'd use a period.

Regards, Jack. 


"Russell Styles" <RWS0202@comcast.net> wrote in message news:<IqycnTDPX__K8wKjXTWcoQ@comcast.com>...
> "Jack Sleight" <jacksleight@hotmail.com> wrote in message
> news:8a2d426e.0304141300.78cf76d9@posting.google.com...
…[111 more quoted lines elided]…
> > > Your paragraph-numbering scheme is likewise good practice.
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-19T19:31:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Guhoa.1766$%_3.1320027@newssrv26.news.prodigy.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <OeWcnRBkd_grOAejXTWJhA@giganews.com> <8a2d426e.0304141300.78cf76d9@posting.google.com> <IqycnTDPX__K8wKjXTWcoQ@comcast.com> <8a2d426e.0304191007.5bd82617@posting.google.com>`

```
"Jack Sleight" <jacksleight@hotmail.com> wrote in message
news:8a2d426e.0304191007.5bd82617@posting.google.com...
> Hi Russell,
>
…[10 more quoted lines elided]…
>                                    *> the error goes away


EVALUATE A
     WHEN B
          DO THIS
     WHEN C
         DO THAT
END-EVALUATE

MCM
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

_(reply depth: 6)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-04-19T16:05:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aJacnd0K-Yx8MDyjXTWcog@comcast.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <OeWcnRBkd_grOAejXTWJhA@giganews.com> <8a2d426e.0304141300.78cf76d9@posting.google.com> <IqycnTDPX__K8wKjXTWcoQ@comcast.com> <8a2d426e.0304191007.5bd82617@posting.google.com> <Guhoa.1766$%_3.1320027@newssrv26.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:Guhoa.1766$%_3.1320027@newssrv26.news.prodigy.com...
> "Jack Sleight" <jacksleight@hotmail.com> wrote in message
> news:8a2d426e.0304191007.5bd82617@posting.google.com...
…[23 more quoted lines elided]…
>
    As noted in another message, this was intended to
be an example of BAD code that does not cause an error
or a flag when using the no period style.

    Yes, it should have the extra end-if.  If you
bother to look at it, the omission is obvious.  But
the compiler will do nothing to help you.
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

_(reply depth: 5)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-04-19T16:01:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aJacnaIK-Yx9MDyjXTWcog@comcast.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <OeWcnRBkd_grOAejXTWJhA@giganews.com> <8a2d426e.0304141300.78cf76d9@posting.google.com> <IqycnTDPX__K8wKjXTWcoQ@comcast.com> <8a2d426e.0304191007.5bd82617@posting.google.com>`

```
    Sorry I did not make myself clear.  That was the point, an accidental
missing END-IF.

    Both styles, one period and many periods have faults.

    That code (as I entered it) shows a problem with the
one period style.  Yes, it is easy to if you think to look.
But it does not cause a warning, or even a flag.




"Jack Sleight" <jacksleight@hotmail.com> wrote in message
news:8a2d426e.0304191007.5bd82617@posting.google.com...
> Hi Russell,
>
…[13 more quoted lines elided]…
> .              *> separate line in the event I need to copy "end of
pgraph"
>
> On the other hand I'm not a purist. If the end-ifs got out of hand I'd use
a period.
>
> Regards, Jack.
>
>
> "Russell Styles" <RWS0202@comcast.net> wrote in message
news:<IqycnTDPX__K8wKjXTWcoQ@comcast.com>...
> > "Jack Sleight" <jacksleight@hotmail.com> wrote in message
> > news:8a2d426e.0304141300.78cf76d9@posting.google.com...
…[64 more quoted lines elided]…
> >
        Original stuff snipped.
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

_(reply depth: 4)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T15:27:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b812kj$1is$1@peabody.colorado.edu>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <OeWcnRBkd_grOAejXTWJhA@giganews.com> <8a2d426e.0304141300.78cf76d9@posting.google.com> <IqycnTDPX__K8wKjXTWcoQ@comcast.com>`

```

On 17-Apr-2003, "Russell Styles" <RWS0202@comcast.net> wrote:

>     Classroom programs are unlikely to be big enough
> to make numbered paragraphs useful.  As with so many
> other options, it all depends on what you get used to.

However, if your teacher (or employer) uses these, learn to use them well.  
Save your fights for things that matter.


>     I used to be happy with a 25x80 screen.  They now make
> me feel like I am peering thru a keyhole.

Wait until your eyes get old.


>     On the other hand, the "one and only one period" school
> can have trouble with If's that extend farther than you would like.
…[11 more quoted lines elided]…
> END OF PARAGRAPH.

But this isn't the optimal solution - ALWAYS put in END-IF to be safe.
```

#### ↳ Re: Advise on program structure needed

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-14T09:58:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-525FED.09580014042003@corp.supernews.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com>`

```
In article <ca0d9b0f.0304132201.76fc0f6e@posting.google.com>,
 aliensite@excite.com (aliensite) wrote:

> I am learning COBOL and the programs structure in my text don't always
> seem logical. Luckly my professor is a COBOL programmer who gives us
…[25 more quoted lines elided]…
> 4200-CLOSE-FILES.

Structure looks good, but a few comments:

Your EOF-SW = "Y" would be quite nice as an 88-level conditional.  
"PERFORM 3000-MAIN UNTIL END-OF-FILE" reads clearer and ensures you 
never accidently move "X" to EOF-SW or somesuch.

Does your prof require the 4-digit prefixed paragraphs?  They used to be 
useful in finding your way around your listing, but these days they just 
screw up your source control and/or misrepresent the program.
```

##### ↳ ↳ Re: Advise on program structure needed

- **From:** aliensite@excite.com (aliensite)
- **Date:** 2003-04-14T18:58:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ca0d9b0f.0304141758.695ee651@posting.google.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <joe_zitzelberger-525FED.09580014042003@corp.supernews.com>`

```
Thanks, this program was based on a previous project without 88-level.
I had already defined the condition name, but forgot to edit the
switch.
It now reads.
     PERFORM 3000-MAIN UNTIL EOF

Our professor does not require 4-digit prefixed paragraph, but he
recommends it. He was from Russia and now works in the NY financial
district, not sure where he got the paragraph style from.

I am actually jumping ahead, this is the final project for the
semister, so the topics are not yet covered, but I already did the
rest of them :)

He adds his own twists to the programs that are not in the text, so
its a challenge. The only part I have to figure out is the two output
files, the report and an error report. Not sure if its to be printed
on the same paper.


Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote in message news:<joe_zitzelberger-525FED.09580014042003@corp.supernews.com>...
> 
> Your EOF-SW = "Y" would be quite nice as an 88-level conditional.  
…[5 more quoted lines elided]…
> screw up your source control and/or misrepresent the program.
```

#### ↳ Re: Advise on program structure needed

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-04-14T18:44:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0304141612.46245c04@posting.google.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com>`

```
aliensite@excite.com (aliensite) wrote in message news:<ca0d9b0f.0304132201.76fc0f6e@posting.google.com>...
> I am learning COBOL and the programs structure in my text don't always
> seem logical. Luckly my professor is a COBOL programmer who gives us
…[25 more quoted lines elided]…
> 4200-CLOSE-FILES.

I generally agree with the comments made by other people, though I see
no harm in using prefixes the way that you have.

However, I would not have 2000-READ where it is, but subordinate to
3000-MAIN, where it would be the first procedure executed.

You could consider a 0000-CONTROL procedure name at the very start of
the program, good for anarchists!.

You could consider a 9xxx- series for error handling procedures,
alternatively you might prefer to use declaratives, especially if you
have a 2002 standard compiler.

For larger programs, you could consider an 8xxx- series for your I-O
procedures, especially for those that can be performed from a variety
of places.  Similarly a 7xxx- series for commonly invoked non-I-O
procedures.

I generally prefer alphanumeric prefixes such as in A-CONTROL,
B-INITIALISE, C-PROCESS, D-END-OF-JOB, with subordinate procedures to
these prefixed with additional letters such as BA-SET-VALUES,
BA-OPEN-FILES, etc.  But this is a matter of style.  On EBCDIC systems
the numbers follow the letters, but in any case there are 26 letters
as opposed to 10 digits, so more complex programs with a flattish
profile are more easily accommodated.  Use of letters (or digits) as
prefixes in this manner is arguably more flexible, as more complex
programs can use any number of letters in a prefix.

I agree that such prefixes, either alphanumeric or numeric can make
shuffling the procedures around during program development and
subsequent maintenance/development more difficult, though when used
well, they make program organisation easier to comprehend to other
programmers and even to the author several months later.  I would like
to see program editors with an outlining facility that would handle
this semi-automatically, but appreciate that I couldn't write one
myself, well I don't think I could.
```

##### ↳ ↳ Re: Advise on program structure needed

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-15T03:58:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E9B848C.D4C5DF34@shaw.ca>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <fcd09c56.0304141612.46245c04@posting.google.com>`

```


Robert Jones wrote:

> aliensite@excite.com (aliensite) wrote in message news:<ca0d9b0f.0304132201.76fc0f6e@posting.google.com>...
> > I am learning COBOL and the programs structure in my text don't always
…[63 more quoted lines elided]…
> myself, well I don't think I could.

Robert,

Actually I bet you could write a non-OO template <G>. So happens in the case of Net Express that M/F does
provide some OO templates - but the very basics. Certainly a good starting point for beginners in OO. (I don't
use them preferring my own customized format where I use the word 'FACTORY' - doesn't appear in the M/F
template because they firmed up on them quite some years ago).

By no means 'smooth' but triggered by something Richard wrote a short while back, I have backtracked in OO -
where I have a dialog I've now written program templates that create (1) the 'guts' of the Business Class, and
(2) a Parameter Class which passes properties to a generic Dialog Class. Based on the controls in the Dialog
the methods for the returned events are written into (1) the Business Class above. Get the thing running really
smoothly and I will have saved myself about 80% of the repetitive coding. Even copy file entries can be
renamed.

How you would do it non-OO depends. Is it an 'all embracing program' or is it split out into a Three Tier
System - (1) Business Logic (Public Domain - oooh  I hate that fancy academic name !), (2) UI (Screen
Section/green screen/GUIs ?) and (3) DBI
(Database Interface - COBOL files or DB tables).

Consider the template just for COBOL File handling - come up with a PERFORM PARAGRAPH for each file verb -
allow for copy/replace on filename and keys etc.
Couple these paragraphs with checking file status (my preference) or offer as an alternative DECLARATIVES. The
Beginner has a template of all file verbs and just 'chops out' the paragraphs (s)he doesn't need.

Jimmy, Calgary AB
```

#### ↳ Re: Advise on program structure needed

- **From:** poopiehead <member15404@dbforums.com>
- **Date:** 2003-04-18T17:25:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2782630.1050686758@dbforums.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com>`

```

YOUR UPPER CASE STYLE IS THE WAY TO GO.  ITS CRAZY TO CHANGE YEARS OF
PRESIDENCE BECAUSE A COMPILER ACCEPTS A NEW STYLE.  THERE IS NO
PERFORMANCE INCREASE WITH LOWER CASE AND MOST COBOL PROGRAMMERS THAT
AREN'T MENTALLY HANDICAPPED DON'T THINK YOUR SCREAMING IN YOUR CODE.
CONTINUE TO PROGRAM IN UPPERCASE BECAUSE THAT WAS AND IS THE STANDARD.

PS:  NO MY KEYBOARD IS NOT BROKE AND I'M NOT MAD.  IDIOTS JUST WANTED TO
     EXPRESS EMOTIONS ON THE WEB AND CERTAIN MORONS FOLLOWED THE IDIOTS
     OF THE CLIFFS.  DON'T FOLLOW!!!!!  COBOL IS PROGRAMMED IN
     UPPERCASE!!!  LEAVE CASES TO JAVA PROGRAMMERS BECAUSE ITS THEIR
     KIND THAT CHANGED THE RULES.
```

##### ↳ ↳ Re: Advise on program structure needed

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-18T15:36:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EmqdnWF7wOhX_D2jXTWJig@giganews.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <2782630.1050686758@dbforums.com>`

```

"poopiehead" <member15404@dbforums.com> wrote in message
news:2782630.1050686758@dbforums.com...
>
> YOUR UPPER CASE STYLE IS THE WAY TO GO.  ITS CRAZY TO CHANGE YEARS

[...]

Advanced Keyboard Course - $12
```

##### ↳ ↳ Re: Advise on program structure needed

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-18T14:25:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304181325.3f448778@posting.google.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <2782630.1050686758@dbforums.com>`

```
poopiehead <member15404@dbforums.com> wrote 

> YOUR UPPER CASE STYLE IS THE WAY TO GO.  ITS CRAZY TO CHANGE YEARS OF
> PRESIDENCE BECAUSE A COMPILER ACCEPTS A NEW STYLE.  THERE IS NO
…[8 more quoted lines elided]…
>      KIND THAT CHANGED THE RULES.

I tried compiling this COBOL code but my compiler rejects it saying
there is no PROGRAM-ID.  Which compiler are you using ?  Until I can
get a clean compile I'm afraid I can't help with the problems you are
having getting this program to work.
```

##### ↳ ↳ Re: Advise on program structure needed

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-18T19:58:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA09F3C.6080906@Knology.net>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <2782630.1050686758@dbforums.com>`

```
poopiehead wrote:
> YOUR UPPER CASE STYLE IS THE WAY TO GO.  ITS CRAZY TO CHANGE YEARS OF
> PRESIDENCE BECAUSE A COMPILER ACCEPTS A NEW STYLE.  THERE IS NO
…[8 more quoted lines elided]…
>      KIND THAT CHANGED THE RULES.

Never has a handle been more fitting....


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Advise on program structure needed

- **From:** "Gwendolyn" <gwendolyn.peters@gbi.state.ga.us>
- **Date:** 2003-04-21T09:02:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b80q00$pbn$1@newsreader.mailgate.org>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <2782630.1050686758@dbforums.com> <3EA09F3C.6080906@Knology.net>`

```

"LX-i" <DanielJS@Knology.net> wrote in message
news:3EA09F3C.6080906@Knology.net...
> poopiehead wrote:
> > YOUR UPPER CASE STYLE IS THE WAY TO GO.  ITS CRAZY TO CHANGE YEARS OF
…[3 more quoted lines elided]…
>
You took the keystrokes right off of my fingers.  Interpretation for those
who need it:  YOU TOOK THE WORDS RIGHT OUT OF MY MOUTH!!!!!!!!!!!
```

#### ↳ Re: Advise on program structure needed

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T15:18:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8124d$19r$1@peabody.colorado.edu>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com>`

```

On 14-Apr-2003, aliensite@excite.com (aliensite) wrote:

> I am learning COBOL and the programs structure in my text don't always
> seem logical. Luckly my professor is a COBOL programmer who gives us
…[4 more quoted lines elided]…
> report, I listed the paragraphs below. Is this structure ok? Thanks.

When you get out of his class, get rid of the periods that he asks for, if you
like (they are all style if you use terminators).   While you're in his class
pretend he's an employer with strict standards.   Real life IS like that.

Your structure needs a bit more fleshing out for me to know whether it would be
acceptable at my shop.

This is style, not substance - but typically if I am in a shop that names its
paragraphs like that, I would number them like this:

0000-MAIN
0100-INIT.
1000-MAIN.

5000-CLEAN-UP.

8000-READ.
9000-WRITE.
9100-PAGE-HEADINGS.

We put the I/O paragraphs at the end, and leave lots of room for sub-paragraphs
functionally after 1000-MAIN.
```

#### ↳ Re: Advise on program structure needed

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2003-06-14T07:45:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FcKdnWTlTO1EhXajXTWcrg@comcast.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com>`

```
In article <ca0d9b0f.0304132201.76fc0f6e@posting.google.com>, 
aliensite@excite.com wrote:

>I am learning COBOL and the programs structure in my text don't always
>seem logical. Luckly my professor is a COBOL programmer who gives us
>real world tips. He advises to use a period after each statement, but
>I find one period after a paragraph easier to read. 

I find it easier to put a period after each line so I don't accidentally
get weird runaway IF-clauses and such, but I suspect that topic's
been discussed to death already. :-)

>Is this structure ok? Thanks.
>
…[19 more quoted lines elided]…
>4200-CLOSE-FILES.

Not to be doing your homework for you, but rememebr that everything
in the 3000's is going to be repeated multiple times...
```

##### ↳ ↳ Re: Advise on program structure needed

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-06-14T13:57:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nRFGa.3563$87.2291601@newssrv26.news.prodigy.com>`
- **References:** `<ca0d9b0f.0304132201.76fc0f6e@posting.google.com> <FcKdnWTlTO1EhXajXTWcrg@comcast.com>`

```
"Ubiquitous" <weberm@polaris.net> wrote in message
news:FcKdnWTlTO1EhXajXTWcrg@comcast.com...
> In article <ca0d9b0f.0304132201.76fc0f6e@posting.google.com>,
> aliensite@excite.com wrote:
>
> >I am learning COBOL and the programs structure in my text don't always
> >seem logical.

Don't feel left out. You've just described about a third of the code I see
from "veterans."

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
