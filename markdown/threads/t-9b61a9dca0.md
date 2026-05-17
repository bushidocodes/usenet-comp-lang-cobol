[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Tabs

_10 messages · 9 participants · 1995-06 → 1995-07_

---

### Tabs

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1995-06-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3rhve1$8s3@gazette.tandem.com>`

```
1234567891123456789212345678931234567894123456789512345678961234567897
Does anyone use tabs in their COBOL source code? If so, what do you
expect the compiler to do with them? One option is if the tab is in
columns 1 to 6 to put spaces in so the next thing is in column 7. Or,
perhaps even column 8. Another is to have each one be four spaces or
some such. I have been told that everyone who programs for UNIX puts
tabs all over in their source code. Is this true?

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
Project Editor, 1997 ISO COBOL Standard
Moderator, COBOL Conference, Bix
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

#### ↳ Re: Tabs

- **From:** "684..." <ua-author-5610386@usenetarchives.gap>
- **Date:** 1995-06-11T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b61a9dca0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3rhve1$8s3@gazette.tandem.com>`
- **References:** `<3rhve1$8s3@gazette.tandem.com>`

```
In article <3rhve1$8.··.@gaz··m.com>
Don Nelson writes:

›
› 1234567891123456789212345678931234567894123456789512345678961234567897
› Does anyone use tabs in their COBOL source code? If so, what do you
Well, I don't use Tab. Although "It's a wonderful drink"
I spill coffee and/or Dr Pepper on my COBOL coding sheets.
On bad days I spill Jolt Cola when I have the D.T.s....
› expect the compiler to do with them? One option is if the tab is in
But seriously folks...
I expect the compiler to do the same thing the editor does,
i.e. space over appropriately according to what the tabs have been
set to, perhaps by stty command, or dumb terminal model specific...

› columns 1 to 6 to put spaces in so the next thing is in column 7.  Or,
› perhaps even column 8.  Another is to have each one be four spaces or
› some such.  I have been told that everyone who programs for UNIX puts
› tabs all over in their source code.  Is this true?
 
› Not only tabs, but cute little yellow post-its.
›
```

#### ↳ Re: Tabs

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1995-06-12T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b61a9dca0-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3rhve1$8s3@gazette.tandem.com>`
- **References:** `<3rhve1$8s3@gazette.tandem.com>`

```
SIn article <173··.@LMS··D.COM> ,
684··.@LMS··D.COM writes:
››› Does anyone use tabs in their COBOL source code?  If so, what do you
› Well, I don't use Tab.  Although "It's a wonderful drink"
› I spill coffee and/or Dr Pepper on my COBOL coding sheets.
› On bad days I spill Jolt Cola when I have the D.T.s....

I prefer Classic Coke. It is also bad to spill it on your card deck.
It really yucks it up.

›› expect the compiler to do with them?  One option is if the tab is in
› But seriously folks...
› I expect the compiler to do the same thing the editor does,
› i.e. space over appropriately according to what the tabs have been
› set to, perhaps by stty command, or dumb terminal model specific...

The compiler has no clue what the editor did. Almost all editors
allow varied specifications for tabs. This information is normally
not included in the text file (especially for UNIX text files).
Therefore, it is somewhat difficult to guess about what the right
values might be.

›› columns 1 to 6 to put spaces in so the next thing is in column 7.  Or,
›› perhaps even column 8.  Another is to have each one be four spaces or
…[4 more quoted lines elided]…
›› 
I like the blue ones.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
Project Editor, 1997 ISO COBOL Standard
Moderator, COBOL Conference, Bix
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

#### ↳ Re: Tabs

- **From:** "richard smith" <ua-author-515531@usenetarchives.gap>
- **Date:** 1995-06-12T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b61a9dca0-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3rhve1$8s3@gazette.tandem.com>`
- **References:** `<3rhve1$8s3@gazette.tandem.com>`

```
Don Nelson wrote:
› 
› Does anyone use tabs in their COBOL source code?  If so, what do you 
…[5 more quoted lines elided]…
› 

If you use the vi editor (and presumably others) you can end up with
tabs in your source. In this case tabs take you to columns 9, 17, 25
and so on and, in order to be compatible with these editors, the
compiler should assume the same tab stops when it reads the source
back in. Certainly this is the case with the MF compiler.

It's tempting to define COBOL-like tab stops for COBOL source but that
would only be useful if the tabs were put there in the first place by
an editor that used the same stops.

---
Regards,
Richard.
```

##### ↳ ↳ Re: Tabs

- **From:** "k..." <ua-author-17073840@usenetarchives.gap>
- **Date:** 1995-06-12T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b61a9dca0-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9b61a9dca0-p4@usenetarchives.gap>`
- **References:** `<3rhve1$8s3@gazette.tandem.com> <gap-9b61a9dca0-p4@usenetarchives.gap>`

```

In article <3rk3n4$6.··.@hyp··o.uk>, Richard Smith writes:
› Don Nelson  wrote:
›› 
…[12 more quoted lines elided]…
› back in.  Certainly this is the case with the MF compiler.

That's not strictly true. 'vi' (and other editors) will let you configure the
tab stops (vi:- ":set ts=n", where n is the number of characters a tab stop
will use, defaulting to 8 (hence your numbers above)).

When writing COBOL with 'vi', I would prefer to use a tab setting of 4 (8 is
useful for getting you past column 7 with a single tab, but it's far too much
for indentation within code, IMHO).

Ideally, your editor will let you configure the tabs for COBOL so that (for
instance) the first takes you to column 7, then column 8, then in multiples of
4.

› It's tempting to define COBOL-like tab stops for COBOL source but that
› would only be useful if the tabs were put there in the first place by
› an editor that used the same stops.

But why should you assume that people *aren't* using editors that do this (I
think emacs lets you, though I wouldn't swear it).

A directive like TABS(7,8,+4) (or something!) would be a reasonable way to
handle this ....

Cheers,
Kev.

Kevin.			 Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
These views are strictly my own.
I doubt very much that anyone else would want them.
```

###### ↳ ↳ ↳ Re: Tabs

- **From:** "jea..." <ua-author-11185568@usenetarchives.gap>
- **Date:** 1995-06-13T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b61a9dca0-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9b61a9dca0-p5@usenetarchives.gap>`
- **References:** `<3rhve1$8s3@gazette.tandem.com> <gap-9b61a9dca0-p4@usenetarchives.gap> <gap-9b61a9dca0-p5@usenetarchives.gap>`

```
In <3rk6oq$7.··.@ice··o.uk>, k.··.@mfl··o.uk (Kev Digweed) writes:

> A directive like TABS(7,8,+4) (or something!) would be a reasonable way to
> handle this ....

RM/COBOL allows the interpretation of hard tab characters in input files
to be configured in just that way. Unfortunately, the default tab
stops, for historical reasons, are COBOLish: every fourth column,
starting with one-based column 8 (not 9). That may have been convenient
on some TI-990 or ancient NCR box, but less so on DOS or UNIX. There
are people who use and like those tab stops. I have no idea what editor
they are using.

To address this problem, the RM/CodeBench development environment's tab
stops default to to 1,9,17,25... but can be reconfigured. It handles
tab expansion for the compiler, so what you see is what you get.

---------------------------------------------------------------------------
| Uwe Baemayr | E-mail: u.··.@li··t.com |
| Principal Programmer | or: jea··.@ccw··s.edu |
| Ryan McFarland Corp/Liant Software | Compuserve: 74774,47 / GO LIANT |
---------------------------------------------------------------------------
```

#### ↳ Re: Tabs

- **From:** "pet..." <ua-author-582426@usenetarchives.gap>
- **Date:** 1995-06-13T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b61a9dca0-p7@usenetarchives.gap>`
- **In-Reply-To:** `<3rhve1$8s3@gazette.tandem.com>`
- **References:** `<3rhve1$8s3@gazette.tandem.com>`

```
Don Nelson (nel··.@tan··m.com) wrote:
: 1234567891123456789212345678931234567894123456789512345678961234567897
: Does anyone use tabs in their COBOL source code? If so, what do you
: expect the compiler to do with them? One option is if the tab is in
: columns 1 to 6 to put spaces in so the next thing is in column 7. Or,
: perhaps even column 8. Another is to have each one be four spaces or
: some such. I have been told that everyone who programs for UNIX puts
: tabs all over in their source code. Is this true?

After col.7 tabs are OK. Use them all the time to make the source "readable".

Rgds
Petras
```

#### ↳ Re: Tabs

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1995-06-13T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b61a9dca0-p8@usenetarchives.gap>`
- **In-Reply-To:** `<3rhve1$8s3@gazette.tandem.com>`
- **References:** `<3rhve1$8s3@gazette.tandem.com>`

```
In message <<3rhve1$8.··.@gaz··m.com>> Don Nelson writes:
› Does anyone use tabs in their COBOL source code?  If so, what do you 
› expect the compiler to do with them?  One option is if the tab is in 
…[3 more quoted lines elided]…
› tabs all over in their source code.  Is this true?

I have my editor set up so the TAB key moves to 8, 12 and every
4 after that but it puts blocks of spaces and not tab characters
in the file. I find tab characters to be a pain and process
them out of any file found to have them.
```

##### ↳ ↳ Re: Tabs

- **From:** "ja..." <ua-author-14040743@usenetarchives.gap>
- **Date:** 1995-07-02T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b61a9dca0-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9b61a9dca0-p8@usenetarchives.gap>`
- **References:** `<3rhve1$8s3@gazette.tandem.com> <gap-9b61a9dca0-p8@usenetarchives.gap>`

```
In article ,
Dave Knell wrote:
› 
› On 14 Jun 1995, Richard Plinston wrote:
…[13 more quoted lines elided]…
› sort of smart tabbing system, and is certainly useable. 

Errrm. Now's probably not the time to mention "vi", is it ? :-)

James.
 "Yield to temptation --             | Work: ja··.@OiT··o.uk
  it may not pass your way again"    | Play: ja··.@her··o.uk
                                     | http://www.OiT.co.uk/~james/
        - Lazarus Long               |              James Fidell
```

#### ↳ Re: Tabs

- **From:** "fr..." <ua-author-6381038@usenetarchives.gap>
- **Date:** 1995-06-13T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b61a9dca0-p10@usenetarchives.gap>`
- **In-Reply-To:** `<3rhve1$8s3@gazette.tandem.com>`
- **References:** `<3rhve1$8s3@gazette.tandem.com>`

```
Don Nelson (nel··.@tan··m.com) wrote:
: 1234567891123456789212345678931234567894123456789512345678961234567897
: Does anyone use tabs in their COBOL source code? If so, what do you
: expect the compiler to do with them? One option is if the tab is in
: columns 1 to 6 to put spaces in so the next thing is in column 7. Or,
: perhaps even column 8. Another is to have each one be four spaces or
: some such. I have been told that everyone who programs for UNIX puts
: tabs all over in their source code. Is this true?

: Don Nelson
: COBOL Development, Tandem Computers, Inc.
: Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
: Project Editor, 1997 ISO COBOL Standard
: Moderator, COBOL Conference, Bix
: nel··.@tan··m.com
: do··.@b··.com
: No clever quotes here

I don't use them, mainly because different compilers handle tabs differently.
Spaces, on the other hand, are handled the same by all COBOL compilers.

C programmers use tabs. C interprets tabs as a common delimiter, such as a
space or comma. Again, in C, I don't use tabs because printing or display
varies, unlike spaces.

Lawrence A. Free | Email: fr··.@m··.com
A.F.Software Services, Inc. | Your MS/DOS, UNIX
(708) 232-0790 | business software developer
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
