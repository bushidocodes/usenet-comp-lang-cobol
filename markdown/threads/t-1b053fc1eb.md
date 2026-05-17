[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# O.T. - Need REXX For Renumbering

_12 messages · 5 participants · 1998-05_

---

### O.T. - Need REXX For Renumbering

- **From:** "stev..." <ua-author-6589195@usenetarchives.gap>
- **Date:** 1998-05-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3565e5c8.3548264@news.apk.net>`

```

Do any of you COBOL gurus out there who work in the MVS/ISPF
environment have an REXX program for renumbering COBOL sequence
numbers in columns 1-6 that allows a starting number and an increment?
Or how about a CUT and PASTE REXX program? Use to have these in my
old VM/CMS environment, but can't find them anymore.

Please post here...there may be others who could use them.

Thanks.



////
(o o)
-oOO--(_)--OOo-

Steve

Mind Like A Steel Trap - Rusty and Illegal in 37 States.
```

#### ↳ Re: O.T. - Need REXX For Renumbering

- **From:** "mickey" <ua-author-28912@usenetarchives.gap>
- **Date:** 1998-05-23T14:08:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b053fc1eb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3565e5c8.3548264@news.apk.net>`
- **References:** `<3565e5c8.3548264@news.apk.net>`

```

SkippyPB wrote:
› 
› Do any of you COBOL gurus out there who work in the MVS/ISPF
…[4 more quoted lines elided]…
› 

Cut and paste have been available in MVS since release 3.2 of ISPF. As
for renumbering, the editor does that. I believe this is a case of RTFM.

mickey
```

##### ↳ ↳ Re: O.T. - Need REXX For Renumbering

- **From:** "stev..." <ua-author-6589195@usenetarchives.gap>
- **Date:** 1998-05-23T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b053fc1eb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1b053fc1eb-p2@usenetarchives.gap>`
- **References:** `<3565e5c8.3548264@news.apk.net> <gap-1b053fc1eb-p2@usenetarchives.gap>`

```

On Sat, 23 May 1998 18:08:24 GMT, Mickey was
insane enough to write:

› SkippyPB wrote:
›› 
…[10 more quoted lines elided]…
› mickey

There is no true CUT and PASTE in ISPF. CUT or COPY would allow you
to PASTE the data multiple times in different places - see ICCF. The
renumber in the editor does not give you the option of setting the
starting number and giving an increment. And what is RTFM??

Regards,


////
(o o)
-oOO--(_)--OOo-

Steve

Mind Like A Steel Trap - Rusty and Illegal in 37 States.
```

###### ↳ ↳ ↳ Re: O.T. - Need REXX For Renumbering

- **From:** "mickey" <ua-author-28912@usenetarchives.gap>
- **Date:** 1998-05-24T15:29:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b053fc1eb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1b053fc1eb-p3@usenetarchives.gap>`
- **References:** `<3565e5c8.3548264@news.apk.net> <gap-1b053fc1eb-p2@usenetarchives.gap> <gap-1b053fc1eb-p3@usenetarchives.gap>`

```

SkippyPB wrote:
› 
› On Sat, 23 May 1998 18:08:24 GMT, Mickey  was
…[20 more quoted lines elided]…
› 

ISPF 101. The Cut macro (ISREDIT MACRO) has an optional parm (Cut R):
this will replace the cut file. The paste macro has one (Paste K) to
keep the cut data. By this method, one can use "CUT R" and subsequent
"CUT"s to build the cut data, and then "PASTE K" to paste it as many
times and places as one desires.

The renum does most certainly allow one to set the increment.

RTFM - Read The F**king manual

mickey
```

###### ↳ ↳ ↳ Re: O.T. - Need REXX For Renumbering

_(reply depth: 4)_

- **From:** "stev..." <ua-author-6589195@usenetarchives.gap>
- **Date:** 1998-05-24T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b053fc1eb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1b053fc1eb-p4@usenetarchives.gap>`
- **References:** `<3565e5c8.3548264@news.apk.net> <gap-1b053fc1eb-p2@usenetarchives.gap> <gap-1b053fc1eb-p3@usenetarchives.gap> <gap-1b053fc1eb-p4@usenetarchives.gap>`

```

On Sun, 24 May 1998 19:29:56 GMT, Mickey was
insane enough to write:

› SkippyPB wrote:
›› 
…[33 more quoted lines elided]…
› mickey

I believe that I described the environment I need the REXX Execs in
incorrectly. The environment I need them in is EDIT under TSO under
ISPF. The system I have access to is ISPF 4.2 and it may be true that
the commands you described are available, but not in EDIT.

Since I work exclusively from home in a telecommuting mode, I don't
have access to any manuals, otherwise I would have looked it up by now
and not have needed to pose the question here.



////
(o o)
-oOO--(_)--OOo-

Steve

Mind Like A Steel Trap - Rusty and Illegal in 37 States.
```

###### ↳ ↳ ↳ Re: O.T. - Need REXX For Renumbering

_(reply depth: 5)_

- **From:** "gilbert saint-flour" <ua-author-14669543@usenetarchives.gap>
- **Date:** 1998-05-25T14:38:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b053fc1eb-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1b053fc1eb-p5@usenetarchives.gap>`
- **References:** `<3565e5c8.3548264@news.apk.net> <gap-1b053fc1eb-p2@usenetarchives.gap> <gap-1b053fc1eb-p3@usenetarchives.gap> <gap-1b053fc1eb-p4@usenetarchives.gap> <gap-1b053fc1eb-p5@usenetarchives.gap>`

```

In <356··.@new··k.net>, on 05/25/98 at 05:00 PM,
ste··.@apk··t.net (SkippyPB) said:

› I believe that I described the environment I need the REXX Execs in
› incorrectly.  The environment I need them in is EDIT under TSO under
› ISPF.  The system I have access to is ISPF 4.2 and it may be true that
› the commands you described are available, but not in EDIT.  

The CUT and PASTE EDIT macros can be found in the ISPF sample library
(called SISPSAMP) under the names ISRCUT and ISRPASTE. To be available to
programmers, ISRCUT and ISRPASTE have to be copied to a library in the
SYSPROC (or SYSEXEC) concatenation under the names CUT and PASTE.

Most people agree that ISREDIT and ISRPASTE aren't very well designed:
they store the data in the profile data set (ISPPROF), leading to SD37
abends when you cut too many lines; also, they're APPLID-dependant which
means that if you CUT in an APPLID, you can't PASTE into another. The
ISPF developpers are working on a new design which will use data-spaces
and provide multiple clip-boards.

You can find numerous CUT/PASTE combos on the CBT tape, Xephon and other
places. I'll suggest my own, which can be found in the PDFTOOLS package
in the /tools directory of my Web page.

Hope this helps.

Gilbert Saint-flour
http://members.home.net/gsf/
```

###### ↳ ↳ ↳ Re: O.T. - Need REXX For Renumbering

_(reply depth: 5)_

- **From:** "mickey" <ua-author-28912@usenetarchives.gap>
- **Date:** 1998-05-25T15:52:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b053fc1eb-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1b053fc1eb-p5@usenetarchives.gap>`
- **References:** `<3565e5c8.3548264@news.apk.net> <gap-1b053fc1eb-p2@usenetarchives.gap> <gap-1b053fc1eb-p3@usenetarchives.gap> <gap-1b053fc1eb-p4@usenetarchives.gap> <gap-1b053fc1eb-p5@usenetarchives.gap>`

```

SkippyPB wrote:
› 
› On Sun, 24 May 1998 19:29:56 GMT, Mickey  was
…[47 more quoted lines elided]…
› 
Cut and Paste are part of ISPF. As to the rest, I'll look it up for you
and e-mail it direct.

mickey
```

###### ↳ ↳ ↳ Re: O.T. - Need REXX For Renumbering

_(reply depth: 5)_

- **From:** "stev..." <ua-author-6589195@usenetarchives.gap>
- **Date:** 1998-05-25T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b053fc1eb-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1b053fc1eb-p5@usenetarchives.gap>`
- **References:** `<3565e5c8.3548264@news.apk.net> <gap-1b053fc1eb-p2@usenetarchives.gap> <gap-1b053fc1eb-p3@usenetarchives.gap> <gap-1b053fc1eb-p4@usenetarchives.gap> <gap-1b053fc1eb-p5@usenetarchives.gap>`

```

On Mon, 25 May 1998 17:00:36 GMT, ste··.@apk··t.net (SkippyPB) was
insane enough to write:

› On Sun, 24 May 1998 19:29:56 GMT, Mickey  was
› insane enough to write:
…[55 more quoted lines elided]…
› Mind Like A Steel Trap - Rusty and Illegal in 37 States.


Thanks Gilbert for setting me straight and I'll certainly check out
your web site.

Regards,


////
(o o)
-oOO--(_)--OOo-

Steve

Mind Like A Steel Trap - Rusty and Illegal in 37 States.
```

###### ↳ ↳ ↳ Re: O.T. - Need REXX For Renumbering

_(reply depth: 5)_

- **From:** "css..." <ua-author-6589296@usenetarchives.gap>
- **Date:** 1998-05-26T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b053fc1eb-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1b053fc1eb-p5@usenetarchives.gap>`
- **References:** `<3565e5c8.3548264@news.apk.net> <gap-1b053fc1eb-p2@usenetarchives.gap> <gap-1b053fc1eb-p3@usenetarchives.gap> <gap-1b053fc1eb-p4@usenetarchives.gap> <gap-1b053fc1eb-p5@usenetarchives.gap>`

```

Cut and Paste won't work properly because it will displace the content of
the rest of the line. If you have space built in to allow for this then I
suess you would be ok but probably dont. Why would you want to build a
rexx for this, why not just write a simple batch program to do it ?

-Chris


SkippyPB (ste··.@apk··t.net) wrote:
: On Sun, 24 May 1998 19:29:56 GMT, Mickey was
: insane enough to write:

: >SkippyPB wrote:
: >>
: >> On Sat, 23 May 1998 18:08:24 GMT, Mickey was
: >> insane enough to write:
: >>
: >> >SkippyPB wrote:
: >> >>
: >> >> Do any of you COBOL gurus out there who work in the MVS/ISPF
: >> >> environment have an REXX program for renumbering COBOL sequence
: >> >> numbers in columns 1-6 that allows a starting number and an increment?
: >> >> Or how about a CUT and PASTE REXX program? Use to have these in my
: >> >> old VM/CMS environment, but can't find them anymore.
: >> >>
: >> >
: >> >Cut and paste have been available in MVS since release 3.2 of ISPF. As
: >> >for renumbering, the editor does that. I believe this is a case of RTFM.
: >> >
: >> >mickey
: >>
: >> There is no true CUT and PASTE in ISPF. CUT or COPY would allow you
: >> to PASTE the data multiple times in different places - see ICCF. The
: >> renumber in the editor does not give you the option of setting the
: >> starting number and giving an increment. And what is RTFM??
: >>
: >
: >ISPF 101. The Cut macro (ISREDIT MACRO) has an optional parm (Cut R):
: >this will replace the cut file. The paste macro has one (Paste K) to
: >keep the cut data. By this method, one can use "CUT R" and subsequent
: >"CUT"s to build the cut data, and then "PASTE K" to paste it as many
: >times and places as one desires.
: >
: >The renum does most certainly allow one to set the increment.
: >
: >RTFM - Read The F**king manual
: >
: >mickey

: I believe that I described the environment I need the REXX Execs in
: incorrectly. The environment I need them in is EDIT under TSO under
: ISPF. The system I have access to is ISPF 4.2 and it may be true that
: the commands you described are available, but not in EDIT.

: Since I work exclusively from home in a telecommuting mode, I don't
: have access to any manuals, otherwise I would have looked it up by now
: and not have needed to pose the question here.



: ////
: (o o)
: -oOO--(_)--OOo-

: Steve

: Mind Like A Steel Trap - Rusty and Illegal in 37 States.
```

###### ↳ ↳ ↳ Re: O.T. - Need REXX For Renumbering

_(reply depth: 6)_

- **From:** "stev..." <ua-author-6589195@usenetarchives.gap>
- **Date:** 1998-05-26T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b053fc1eb-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1b053fc1eb-p9@usenetarchives.gap>`
- **References:** `<3565e5c8.3548264@news.apk.net> <gap-1b053fc1eb-p2@usenetarchives.gap> <gap-1b053fc1eb-p3@usenetarchives.gap> <gap-1b053fc1eb-p4@usenetarchives.gap> <gap-1b053fc1eb-p5@usenetarchives.gap> <gap-1b053fc1eb-p9@usenetarchives.gap>`

```

On 27 May 1998 12:41:32 GMT, css··.@gar··u.edu (Skinner) was
insane enough to write:

› Cut and Paste won't work properly because it will displace the content of
› the rest of the line.  If you have space built in to allow for this then I
…[4 more quoted lines elided]…
› 



I am working in an EDIT environment. That is, I do a lot of program
development and , since I don't like to reinvent the wheel, I usually
get a shell program that has many of the essentials I need already in
it. There are times when I would like to copy a line or a number of
lines into multiple places in the program. In ICCF this can be
accomplished very easily. However in EDIT (TSO/ISPF), you have to
recopy the lines everytime before inserting them where you want them.
Also you cannot copy lines (using line commands C or CC) in one
memeber, enter EDIT member name, and insert the lines (using A or B
line commands) in the new member. This you can do very easily in
ICCF. It is that type of functionality I am trying to achieve using
REXX execs. A batch solution is not pertinent to the problem. But
thanks for trying anyway.

Regards,


////
(o o)
-oOO--(_)--OOo-

Steve

Mind Like A Steel Trap - Rusty and Illegal in 37 States.
```

###### ↳ ↳ ↳ Re: O.T. - Need REXX For Renumbering

_(reply depth: 7)_

- **From:** "bob berman" <ua-author-6589116@usenetarchives.gap>
- **Date:** 1998-05-26T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b053fc1eb-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1b053fc1eb-p10@usenetarchives.gap>`
- **References:** `<3565e5c8.3548264@news.apk.net> <gap-1b053fc1eb-p2@usenetarchives.gap> <gap-1b053fc1eb-p3@usenetarchives.gap> <gap-1b053fc1eb-p4@usenetarchives.gap> <gap-1b053fc1eb-p5@usenetarchives.gap> <gap-1b053fc1eb-p9@usenetarchives.gap> <gap-1b053fc1eb-p10@usenetarchives.gap>`

```

›› Cut and Paste won't work properly because it will displace the content of
›› the rest of the line.  If you have space built in to allow for this then I
›› suess you would be ok but probably dont.  Why would you want to build a
›› rexx for this, why not just write a simple batch program to do it ?
 
› I am working in an EDIT environment.  That is, I do a lot of program
› development and , since I don't like to reinvent the wheel, I usually
…[10 more quoted lines elided]…
› thanks for trying anyway.

At my last assignment, we had those commands under edit (PDFCUT &
PDFPASTE). At my new assignment, they don't seem to have these, and I
sorely miss them ! I didn't realize that they were REXX execs or
CLISTS, I thought they were ISPF edit commands, or I would have copied
them for my toolbox ! If you get any insight into these, please let me
know.

Regards -
Bob
<----------------------------------------------------------------------> 
                 Bob Berman   -    West Hartford, CT                  
  mailto:bbe··.@net··x.com    homepage: http://www.ntplx.net/~bberman  
                                                                        
                 THE TRUE TERRORISTS IN AMERICA ARE                     
          THE PEOPLE WHO DEMAND TO SEE THE STORE MANAGER !              
<----+----+----+----+----+----+----+----+----+----+----+----+----+----+>
```

###### ↳ ↳ ↳ Re: O.T. - Need REXX For Renumbering

_(reply depth: 7)_

- **From:** "stev..." <ua-author-6589195@usenetarchives.gap>
- **Date:** 1998-05-27T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b053fc1eb-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1b053fc1eb-p10@usenetarchives.gap>`
- **References:** `<3565e5c8.3548264@news.apk.net> <gap-1b053fc1eb-p2@usenetarchives.gap> <gap-1b053fc1eb-p3@usenetarchives.gap> <gap-1b053fc1eb-p4@usenetarchives.gap> <gap-1b053fc1eb-p5@usenetarchives.gap> <gap-1b053fc1eb-p9@usenetarchives.gap> <gap-1b053fc1eb-p10@usenetarchives.gap>`

```

On 27 May 98 16:30:06 GMT, red··.@i··.net (Thane Hubbell) was insane
enough to write:

› On Wed, 27 May 1998 14:55:06, ste··.@apk··t.net (SkippyPB) wrote:
› 
…[15 more quoted lines elided]…
› 

Thane,

Yes, I use a PC to remote link (dial-up line) to the mainframe using
RLINK. I have used the Windows copy and paste function, but find I
have to reformat everything as it never pastes into the PDS member the
same way it was copied.

Thanks for the suggestion, though.

Regards,


////
(o o)
-oOO--(_)--OOo-
I love defenseless animals, especially in good gravy.
Steve
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
