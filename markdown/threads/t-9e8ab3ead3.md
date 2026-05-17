[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Report Writer

_55 messages · 9 participants · 2017-04 → 2018-09_

---

### Report Writer

- **From:** "paulrichards" <ua-author-14501816@usenetarchives.gap>
- **Date:** 2017-04-11T18:50:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au>`

```
I know that the COBOL RW is for producing printed reports. However is
it possible to use RW to produce a report for screen display?

Paul
Melbourne, Australia

---
This email has been checked for viruses by Avast antivirus software.
https://www.avast.com/antivirus
```

#### ↳ Re: Report Writer

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2017-04-11T19:56:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au>`

```
On Tuesday, April 11, 2017 at 6:50:57 PM UTC-4, Paul Richards wrote:
› I know that the COBOL RW is for producing printed reports. However is
› it possible to use RW to produce a report for screen display?

Interesting question!

For standard COBOL, no. The output is formatted for a printer
even if the original destination is a disk file.

However, depending on implementation there may be a way around
that. One might direct the output to a file, then copy the
file to the screen. On IBM that would require processing the
first character as a carriage control character. For those
implementations on 'nix or PC, the report spacing uses some
combination of line feed or carriage return and line feed.
Using Micro Focus on a PC, I write the file with a '.txt'
extension and open with notepad without a problem; but I could
read it with a COBOL program and display on the screen.

I have not tried it, but it may be possible with, say, Micro
Focus, to use something like ASSIGN TO DISPLAY ORGANIZATION
LINE SEQUENTIAL. That would be a non-standard extension, but
it might work for your purposes.

It is, ultimately, implementation dependent, so knowing which
compiler you are using might allow for a better answer to
your question.
```

##### ↳ ↳ Re: Report Writer

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2017-04-11T20:33:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p2@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap>`

```
On Tuesday, April 11, 2017 at 7:56:24 PM UTC-4, Rick Smith wrote:
› On Tuesday, April 11, 2017 at 6:50:57 PM UTC-4, Paul Richards wrote:
›› I know that the COBOL RW is for producing printed reports. However is
›› it possible to use RW to produce a report for screen display?
› 
› Interesting question!
 
› [snip]
 
› I have not tried it, but it may be possible with, say, Micro
› Focus, to use something like ASSIGN TO DISPLAY ORGANIZATION
› LINE SEQUENTIAL.

I had to find out!

-----
program-id. rw-test.
environment division.
input-output section.
file-control.
select rpt-file assign to display
organization line sequential
.
data division.
file section.
fd rpt-file
report is rpt.
working-storage section.
1 num comp pic 99.
report section.
rd rpt.
1 rpt-line type is detail.
2 line plus 1.
3 rpt-item column 1 pic z9 source is num.
procedure division.
open output rpt-file
initiate rpt
perform varying num from 1 by 1
until num > 10
generate rpt-line
end-perform
terminate rpt
close rpt-file
stop run
.
end program rw-test.
-----
1
2
3
4
5
6
7
8
9
10
-----
```

###### ↳ ↳ ↳ Re: Report Writer

- **From:** "paulrichards" <ua-author-14501816@usenetarchives.gap>
- **Date:** 2017-04-12T00:18:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p3@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap>`

```
Rick Smith wrote:

› On Tuesday, April 11, 2017 at 7:56:24 PM UTC-4, Rick Smith wrote:
›› On Tuesday, April 11, 2017 at 6:50:57 PM UTC-4, Paul Richards wrote:
…[56 more quoted lines elided]…
› -----

Rick

Thanks. I am using MicroFocus compiler so it seems your example will
provide a basis for some experimentation on my side. Thanks again.

Paul
Melbourne, Australia

---
This email has been checked for viruses by Avast antivirus software.
https://www.avast.com/antivirus
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-04-14T20:47:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p4@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p4@usenetarchives.gap>`

```
On 12/04/2017 4:18 p.m., Paul Richards wrote:
› Rick Smith wrote:
› 
…[64 more quoted lines elided]…
› 

Sorry Rick,

I thought it was Paul who had "had to find out" :-)

Well done you! (as always...)

Pete.


I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Report Writer

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-04-14T20:44:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p3@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap>`

```
On 12/04/2017 12:33 p.m., Rick Smith wrote:
› On Tuesday, April 11, 2017 at 7:56:24 PM UTC-4, Rick Smith wrote:
›› On Tuesday, April 11, 2017 at 6:50:57 PM UTC-4, Paul Richards wrote:
…[56 more quoted lines elided]…
› 
Good job, Paul!

An interesting idea.

Most of our COBOL clients move to a package like StimulSoft to handle
Reporting. (It is an excellent package and can report from XML as well
as RDB). But this might be another option for some.

Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Report Writer

- **From:** "paulrichards" <ua-author-14501816@usenetarchives.gap>
- **Date:** 2017-04-17T23:34:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p3@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap>`

```
Rick Smith wrote:

› On Tuesday, April 11, 2017 at 7:56:24 PM UTC-4, Rick Smith wrote:
›› On Tuesday, April 11, 2017 at 6:50:57 PM UTC-4, Paul Richards wrote:
…[56 more quoted lines elided]…
› -----

Rick

I've been experimenting with RW-to-the-screen and have hit a problem I
can't resolve. I have a line sequential file (name.dat) containing 3
records (Last name, Middle name and Initial). I created the file with a
normal COBOL program and can read and display the contents with amother
program.

When I try to use RW and send the output to the screen the program
fails as it starts to read the third record with a status '9/18, Read
part record error" EOF before EOR of file open in wrong mode'.

I know the name.dat file is correctly formatted since my other 2
programs have created and read it. Any idea what's going wrong? The RW
code is below.

Thanks

identification division.
program-id. rw-test.
environment division.
input-output section.
file-control.
select mail-label assign to display
organization line sequential.

select name-file
assign to 'c:\workarea\cobol\name.dat'
organization line sequential.
*----------------------------------------------------------
data division.
file section.
fd name-file.
01 name-record.
05 last-name pic x(20).
05 first-name pic x(12).
05 middle-initial pic x.

fd mail-label
report is name-labels.
*----------------------------------------------------------
working-storage section.
01 dummystuff.
03 dummystf pic x.
88 endoffile value high-values.
*----------------------------------------------------------
report section.
rd name-labels.
01 mailing-label type is detail.
05 line plus 1.
10 column 1 pic x(20) source last-name.
10 column 22 pic x(12) source first-name.
10 column 35 pic x source middle-initial.

procedure division.
open output mail-label input name-file
read name-file
at end set endoffile to true
end-read
initiate name-labels
perform until endoffile
generate mailing-label
read name-file
at end set endoffile to true
end-read
end-perform
terminate name-labels
close mail-label name-file
stop run
end program rw-test.

Paul
Melbourne, Australia

---
This email has been checked for viruses by Avast antivirus software.
https://www.avast.com/antivirus
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 4)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2017-04-18T06:15:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p7@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap>`

```
On Monday, April 17, 2017 at 11:34:32 PM UTC-4, Paul Richards wrote:

[snip]

› Rick
› 
…[12 more quoted lines elided]…
› code is below.

[snip]

Using Micro Focus 3.2.50:

I copied the code (changing the location of 'name.dat' for my system),
created a file using the COBOL editor, and the program ran properly.
I then used notepad to alter the data file in various ways including
eliminating all cr+lf pairs, and shortening and lengthening the third
record. I checked the file with hexedit to ensure the intended input
for each test. It, simply, would not fail!

As I recall, the only time I have ever seen a '9/18' was with a
corrupted indexed file, which can't apply here. I would use
the hexedit utility to examine 'name.dat' to make sure everything
is as expected.

notepad display of name.dat -----
Jones Alex P
Jones Mary A
Jones Sam W

hexedit of name.dat -----
-
--------------------------------------------------------------------------------
000000 4A 6F 6E 65 73 20 20 20-20 20 20 20 20 20 20 20 Jones
000010 20 20 20 20 41 6C 65 78-20 20 20 20 20 20 20 20 Alex
000020 50 0D 0A 4A 6F 6E 65 73-20 20 20 20 20 20 20 20 P..Jones
000030 20 20 20 20 20 20 20 4D-61 72 79 20 20 20 20 20 Mary
000040 20 20 20 41 0D 0A 4A 6F-6E 65 73 20 20 20 20 20 A..Jones
000050 20 20 20 20 20 20 20 20-20 20 53 61 6D 20 20 20 Sam
000060 20 20 20 20 20 20 57 0D-0A W..
-
-
-
-
-
-
-
-
-
--------------------------------------------------------------------------------
-

Hexediting-NAME.DAT-------Len--000069-Adrs-000000-------------------------------
F1=help F2=hex/char F3=load-file F4=save-file F5=goto F6=display-all/ASC/EBC
F7=hex/dec-address F8=list-file F10=find Escape

display from running program -----
Jones Alex P
Jones Mary A
Jones Sam W
-----
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 5)_

- **From:** "paulrichards" <ua-author-14501816@usenetarchives.gap>
- **Date:** 2017-04-18T08:42:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p8@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap>`

```
Rick Smith wrote:

› On Monday, April 17, 2017 at 11:34:32 PM UTC-4, Paul Richards wrote:
› 
…[70 more quoted lines elided]…
› -----

Rick

Thanks for looking at this.

I have examined name.dat with HexEdit and it looks fine (comparing it
with your output):

Richards
Paul
A..Richards
Zoe
K..Richards
Leonie
F..

Display from Notepad:

Richards Paul A
Richards Zoe K
Richards Leonie F

What I get from the running program is:

Richards Paul A
Richards Zoe

at which point it errors out.

So I'm at a loss to know what's going on.
Paul
Melbourne, Australia

---
This email has been checked for viruses by Avast antivirus software.
https://www.avast.com/antivirus
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 6)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2017-04-18T12:14:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p9@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap>`

```
On Tuesday, April 18, 2017 at 8:42:13 AM UTC-4, Paul Richards wrote:

[snip]

› What I get from the running program is:
› 
…[5 more quoted lines elided]…
› So I'm at a loss to know what's going on.

The missing 'K' bothers me.

I suggest putting 'display name-record' before the generate,
comment the generate, and test. If that works, uncomment the
generate and test again. There may be some interaction between
the generate and the read that may not appear with the display
statement only. I have no idea what that interaction may be.
Just trying to turn a loss into a gain.

The output with both display (D) and generate (G) did not quite
interleave on my system. The generate output was delayed
one cycle, Instead of 'DGDGDG' it was 'DDGDGG'.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 7)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2017-04-18T12:34:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p10@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap>`

```
On Tuesday, April 18, 2017 at 12:14:27 PM UTC-4, Rick Smith wrote:
› On Tuesday, April 18, 2017 at 8:42:13 AM UTC-4, Paul Richards wrote:
› 
…[18 more quoted lines elided]…
› Just trying to turn a loss into a gain.

It also occurs to me that, if there is an interaction, reading
the record into working-storage before generating the output
from working-storage might correct the problem. You can thank
Mr Dwarf if that resolves the problem.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 8)_

- **From:** "paulrichards" <ua-author-14501816@usenetarchives.gap>
- **Date:** 2017-04-18T21:37:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p11@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap>`

```
Rick Smith wrote:

› On Tuesday, April 18, 2017 at 12:14:27 PM UTC-4, Rick Smith wrote:
›› On Tuesday, April 18, 2017 at 8:42:13 AM UTC-4, Paul Richards wrote:
…[24 more quoted lines elided]…
› Mr Dwarf if that resolves the problem.

Rick

I'm not sure what I did :-( but the 'display' option produced the
required result and when I reinstituted the 'generate', commenting out
'display', the correct output resulted. So I'm a bit stumped. Anyway
got there in the end. Many thanks for your assistance. I'd never uses
Report Writer before so this was a useful lesson.

Incidentally who is Mr Dwarf?docdwarf?

Paul
Melbourne, Australia

---
This email has been checked for viruses by Avast antivirus software.
https://www.avast.com/antivirus
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 9)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2017-04-18T21:47:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p12@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p12@usenetarchives.gap>`

```
On Tuesday, April 18, 2017 at 9:37:36 PM UTC-4, Paul Richards wrote:

[snip]

› I'm not sure what I did :-( but the 'display' option produced the
› required result and when I reinstituted the 'generate', commenting out
› 'display', the correct output resulted. So I'm a bit stumped. Anyway
› got there in the end. Many thanks for your assistance. I'd never uses
› Report Writer before so this was a useful lesson.
 
› Glad I could help.
 
› Incidentally who is Mr Dwarf?docdwarf?

Yes.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 8)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-04-19T07:50:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p11@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap>`

```
In article <01cf8821-bd4e-4961-822b-ed1··e@goo··s.com>,
Rick Smith wrote:

[snip]

› It also occurs to me that, if there is an interaction, reading
› the record into working-storage before generating the output
› from working-storage might correct the problem. You can thank
› Mr Dwarf if that resolves the problem.

Always READ INTO, WRITE FROM... that is the Chant of the Elders which I
was taught.

(It was based on the injunction Thou Shalt Not Perform Arithmetic
Operations In A Buffer)

And please... jes' ol' Doc, that's all.

DD
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 9)_

- **From:** "cfmpublic" <ua-author-127808@usenetarchives.gap>
- **Date:** 2017-04-19T11:36:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p14@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap>`

```
On Wed, 19 Apr 2017 11:50:57 +0000 (UTC), doc··f@pa··x.com () wrote:

› In article <01cf8821-bd4e-4961-822b-ed1··e@goo··s.com>,
› Rick Smith   wrote:
…[9 more quoted lines elided]…
› was taught.

On IBM compilers prior to VS COBOL 1.4 this made sense for read
because the addressability of the read buffer dropped when AT END was
detected. This changed to being dropped when a CLOSE was issued with
the implementation of 1.4 and it was easier to find data in the dump
when debugging especially in later releases with LE (Language
Environment). WRITE FROM for files with variable length records
continued to be of value because it allowed best use of the write
buffer.

Clark Morris
› 
› (It was based on the injunction Thou Shalt Not Perform Arithmetic 
…[4 more quoted lines elided]…
› DD
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 10)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2017-04-19T12:38:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p15@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p15@usenetarchives.gap>`

```
On Wednesday, April 19, 2017 at 5:37:00 PM UTC+2, Clark F Morris wrote:
[...]
› On IBM compilers prior to VS COBOL 1.4 this made sense for read
› because the addressability of the read buffer dropped when AT END was
…[7 more quoted lines elided]…
› Clark Morris

Always if doing "one behind", have all necessary data in WORKING STORAGE anyway. So even end-of-file should not be a problem.

I'm interested in what you could mean by how WRITE ... FROM ... "allowed best use of the write buffer".
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 11)_

- **From:** "cfmpublic" <ua-author-127808@usenetarchives.gap>
- **Date:** 2017-04-19T21:44:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p16@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p15@usenetarchives.gap> <gap-9e8ab3ead3-p16@usenetarchives.gap>`

```
On Wed, 19 Apr 2017 09:38:37 -0700 (PDT), Bill Woodger
wrote:

› On Wednesday, April 19, 2017 at 5:37:00 PM UTC+2, Clark F Morris wrote:
› [...] 
…[13 more quoted lines elided]…
› I'm interested in what you could mean by how WRITE ... FROM ... "allowed best use of the write buffer".

For variable length non-VSAM files if WRITE is used then the buffer
must always have to be able to accommodate the maximum size record
being built. If WRITE FROM is used then the buffer is filled by
moving the actual size of the record for each new record until the
record being moved won't fit.

Clark Morris
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 12)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2017-04-20T01:07:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p17@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p15@usenetarchives.gap> <gap-9e8ab3ead3-p16@usenetarchives.gap> <gap-9e8ab3ead3-p17@usenetarchives.gap>`

```
On Thursday, April 20, 2017 at 3:44:16 AM UTC+2, Clark F Morris wrote:
› On Wed, 19 Apr 2017 09:38:37 -0700 (PDT), Bill Woodger
› [...]
…[8 more quoted lines elided]…
› Clark Morris

Thanks Clark. That would be nice, but it is not so. Here's the generated code for MOVE followed by WRITE and then WRITE ... FROM ...

000041 MOVE
0004F6 5840 9138 L 4,312(0,9) BLF=1
0004FA D209 4000 8000 MVC 0(10,4),0(8) OUT-REC OUT-STUFF
000042 WRITE
000500 5840 9140 L 4,320(0,9) OUTPUT-FILE
000504 9200 40C9 MVI 201(4),X'00' FCB=2
000508 9200 40B3 MVI 179(4),X'00' FCB=2
00050C 5850 9138 L 5,312(0,9) BLF=1
000510 4B50 A01C SH 5,28(0,10) PGMLIT AT +20
000514 1F66 SLR 6,6
000516 BF63 8010 ICM 6,3,16(8) OUT-LENGTH
00051A 5960 A010 C 6,16(0,10) PGMLIT AT +8
00051E 4740 B1E2 BC 4,482(0,11) GN=17(00052A)
000522 5960 A010 C 6,16(0,10) PGMLIT AT +8
000526 47D0 B1EC BC 13,492(0,11) GN=16(000534)
00052A GN=17 EQU *
00052A 9680 4073 OI 115(4),X'80' FCB=2
00052E D203 4040 4054 MVC 64(4,4),84(4) FCB=2 FCB=2
000534 GN=16 EQU *
000534 4A60 A01C AH 6,28(0,10) PGMLIT AT +20
000538 8960 0010 SLL 6,16(0)
00053C 5060 5000 ST 6,0(0,5) BUFFER
000540 D203 4074 A07E MVC 116(4,4),126(10) FCB=2 PGMLIT AT +118
000546 58F0 4040 L 15,64(0,4) FCB=2
00054A 0D5F BASR 5,15
00054C 9500 40C9 CLI 201(4),X'00' FCB=2
000550 4770 B214 BC 7,532(0,11) GN=18(00055C)
000554 4110 1004 LA 1,4(0,1)
000558 5010 9138 ST 1,312(0,9) BLF=1
00055C GN=18 EQU *


000043 WRITE
00055C 5840 9138 L 4,312(0,9) BLF=1
000560 D209 4000 8000 MVC 0(10,4),0(8) OUT-REC OUT-STUFF
000566 5840 9140 L 4,320(0,9) OUTPUT-FILE
00056A 9200 40C9 MVI 201(4),X'00' FCB=2
00056E 9200 40B3 MVI 179(4),X'00' FCB=2
000572 5850 9138 L 5,312(0,9) BLF=1
000576 4B50 A01C SH 5,28(0,10) PGMLIT AT +20
00057A 1F66 SLR 6,6
00057C BF63 8010 ICM 6,3,16(8) OUT-LENGTH
000580 5960 A010 C 6,16(0,10) PGMLIT AT +8
000584 4740 B248 BC 4,584(0,11) GN=20(000590)
000588 5960 A010 C 6,16(0,10) PGMLIT AT +8
00058C 47D0 B252 BC 13,594(0,11) GN=19(00059A)
000590 GN=20 EQU *
000590 9680 4073 OI 115(4),X'80' FCB=2
000594 D203 4040 4054 MVC 64(4,4),84(4) FCB=2 FCB=2
00059A GN=19 EQU *
00059A 4A60 A01C AH 6,28(0,10) PGMLIT AT +20
00059E 8960 0010 SLL 6,16(0)
0005A2 5060 5000 ST 6,0(0,5) BUFFER
0005A6 D203 4074 A07E MVC 116(4,4),126(10) FCB=2 PGMLIT AT +118
0005AC 58F0 4040 L 15,64(0,4) FCB=2
0005B0 0D5F BASR 5,15
0005B2 9500 40C9 CLI 201(4),X'00' FCB=2
0005B6 4770 B27A BC 7,634(0,11) GN=21(0005C2)
0005BA 4110 1004 LA 1,4(0,1)
0005BE 5010 9138 ST 1,312(0,9) BLF=1
0005C2 GN=21 EQU *

Put those side-by-side in a fixed-width font and compare. The only things different are the names of the branches, and the displacements that are branched to.

The code is otherwise identical, as it should be, because that is what the Standard says.

With IBM's Enterprise COBOL (and before, I'm just not going to check for now *when* before) it works like this:

For blocked, variable-length, sequential files, the FD maps to an area in an output buffer. Once you do a WRITE (whether plain or with FROM) the IO routines compare the amount of space left in the buffer with the maximum-length record possible (the LRECL-value for the file). If there is not enough space to accommodate the largest record possible, then the buffer is written.

This behaviour can be modified (remembering for other readers that that doesn't mean "change a program to do something else") by using APPLY WRITE-ONLY for the file (or compiler option AWO, which then automatically applies APPLY WRITE-ONLY for all files that have the specification for which APPLY WRITE-ONLY would work).

With APPLY WRITE-ONLY, the FD is no longer mapped to the buffer, but has its own record-area. When the WRITE is attempted it can be determined whether or not the data can fit in the buffer (block). If not, on to the next buffer.

With APPLY WRITE-ONLY there is another, implicit, MOVE of the data - from record-area to whichever buffer. If used where needed, APPLY WRITE-ONLY improves performance when taking into account the subsequent reading of the data. Across the board, with AWO, no guarantees. Most effective when there is a wide variance of record-lengths within record-types. Pointless when record-lengths are very similar through the file.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 13)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-04-22T21:35:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p18@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p15@usenetarchives.gap> <gap-9e8ab3ead3-p16@usenetarchives.gap> <gap-9e8ab3ead3-p17@usenetarchives.gap> <gap-9e8ab3ead3-p18@usenetarchives.gap>`

```
On 20/04/17 5:07 PM, Bill Woodger wrote:
› On Thursday, April 20, 2017 at 3:44:16 AM UTC+2, Clark F Morris wrote:
›› On Wed, 19 Apr 2017 09:38:37 -0700 (PDT), Bill Woodger
…[88 more quoted lines elided]…
› 
Thanks Bill,

for a masterly analysis and summation.

(I never knew about APPLY WRITE-ONLY and was interested to see how it
works.)

Reading the Assembler brought back some happy memories from a distant
lifetime in a Galaxy far away... :-)

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 9)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2017-04-19T12:36:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p14@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap>`

```
On Wednesday, April 19, 2017 at 1:50:59 PM UTC+2, doc··.@pa··x.com wrote:
[...]
› Always READ INTO, WRITE FROM... that is the Chant of the Elders which I 
› was taught.
…[3 more quoted lines elided]…
› 

I've never had a problem *not* using READ ... INTO .../WRITE ... FROM ..., so other than being old, I'm not sure what your Elders had.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 10)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-04-19T15:35:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p20@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap>`

```
In article <530a5ecd-1222-4609-a1e4-7d3··6@goo··s.com>,
Bill Woodger wrote:
› On Wednesday, April 19, 2017 at 1:50:59 PM UTC+2, doc··.@pa··x.com wrote:
› [...]
…[8 more quoted lines elided]…
› ..., so other than being old, I'm not sure what your Elders had.

The Elders had great abilities, Mr Wodger, and could code code such as
*ten* programmers cannot, today. That you have had no problem may speak
less to what The Elders knew and more to your experience.

<https://groups.google.com/forum/#!search/%22RESERVE$20NO$20ALTERNATE$20AREAS%22/comp.lang.cobol/wtoadHUrX2s/aNmeHAFTvmMJ>

DD
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 11)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2017-04-19T16:27:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p21@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap>`

```
On Wednesday, April 19, 2017 at 9:35:08 PM UTC+2, doc··.@pa··x.com wrote:
› In article <530a5ecd-1222-4609-a1e4-7d3··6@goo··s.com>,
› Bill Woodger wrote:
…[18 more quoted lines elided]…
› DD

Let's see you try to code that. Show us the results, please.

Examples of pre-1964 COBOL, even given that NO existed at the time, are... how useful? Out with 1985.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 12)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-04-19T17:15:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p22@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p22@usenetarchives.gap>`

```
In article <92c35cf5-0af5-4c24-a04a-a0d··6@goo··s.com>,
Bill Woodger wrote:
› On Wednesday, April 19, 2017 at 9:35:08 PM UTC+2, doc··.@pa··x.com wrote:
›› In article <530a5ecd-1222-4609-a1e4-7d3··6@goo··s.com>,
…[20 more quoted lines elided]…
› Let's see you try to code that.

You're asking me to do my job, Mr Woodger, with no discussion of a rate
(or a range of rates).

› Show us the results, please.
›
› Examples of pre-1964 COBOL, even given that NO existed at the time,
› are... how useful?

In that they save time and resources during a Production Implementation
Review, rather useful. In that seeing beauty and elegance are useful,
very useful.

DD
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 11)_

- **From:** "vbcoen" <ua-author-7065949@usenetarchives.gap>
- **Date:** 2017-04-19T18:08:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p21@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap>`

```
Hello Bill!

Wednesday April 19 2017 21:27, Bill Woodger wrote to All:


> Let's see you try to code that. Show us the results, please.

> Examples of pre-1964 COBOL, even given that NO existed at the time,
> are... how useful? Out with 1985.

Opps - oh yes there was think back to :

IBM 1401
ICT 1501
ICT 1901 - may be out here.

I started in computers in 1961 operating and programming the next year yes
it was machine code then autocode (possibly because the company did not
install the latest release / compiler/ assemblers etc) then Cobol and I
remember coding both Cobol 59 startdard -for want of a description, along
with Fortran as any strong maths was poor under Cobol then so we used to
call into Fortan (very much so with the link to a 7094.



Vince
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 12)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2017-04-19T18:49:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p25@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p24@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p24@usenetarchives.gap>`

```
Hello Vince!

The thing about advice is that it ages. Or its merit ages, even though the advice does not (and should).

If Cant, Rant and Mantra from Olden Times is flapped around in front of newcomers, it does nothing for them.

"Always sign your binary fields, and make them the maximum number of digits which fit in the size - for performance!".

If you do that with Enterprise COBOL on an IBM Mainframe, you'll get no difference in performance, at best, or worse performance, with poorly-described fields. No benefit. Disbenefit for sure through the poor data-description, and performance loss. But try telling that to the Cant, Rant and Mantra people.

There is no intrinsic merit in READ ... INTO .... It is, by Standard, exactly the same as READ ... followed by MOVE ... TO ... Same with WRITE ... FROM .... What is supposed to happen? The data suddenly "goes bad" after the use of one COBOL verb?

OK, so, due to Ancient Compilers (and lets assume 100% correct problem-determination) an irrational fear of referencing data under an FD has grown.

Irrational. Until someone can rationalise it (and "We've always done it that way" or "Joe Blogs said so" don't count as rationalisation) it remains irrational.

I can't rationalise it, and I'd be mightily impressed if someone can, with relation to compilers to at least the 1985 Standard.

As alluded to, and mentioned in the link, it is entirely possible to have an FD whose data is in a storage area which can be referenced before a file is opened, before a record is read, after end-of-file, and after a file is closed. Although entirely possible, and entirely Standard, I see absolutely no point in achieving that. What use is putting something in a record-area before a READ? What use is INTIALIZE (or initialising) of a structure which is to be read?

Do people do that? Yes. Do people recommend that? Yes. Is it rational? No.

Why would data be left lying around after a WRITE? Do people expect it to be? Yes.

Can mistakes be made with READ ... INTO ... and WRITE ... FROM ...? Of course.

You can 100% rely on all fields in the current record (subject to the record description being accurate, and if not accurate INTO/FROM isn't going to fix it). When the current record is no longer current, you can 100% rely on the data being different, other than by coincidence (subject to not using a "record area").

If newcomers are told that, rather than "Do as I say, and as I do, even though neither of us know why, or will ever likely find out, we've always done it that way", they are done a service.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 13)_

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2017-04-20T17:40:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p26@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p25@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p24@usenetarchives.gap> <gap-9e8ab3ead3-p25@usenetarchives.gap>`

```
On Thursday, April 20, 2017 at 10:50:01 AM UTC+12, Bill Woodger wrote:

› Why would data be left lying around after a WRITE? Do people expect it to be? Yes.


On an ICL 1900 with ISAM files using bucket overflow one can get strange results.

A new record had to go into a particular bucket in the pre-allocated, fixed length file to maintain record sequence. If there was no room in the bucket then the record would be put into level 1 overflow (pre-allocated on the end of the same cylinder) and a tag put into the bucket pointing to the record. If there was no room for the tag then a record would be moved from the bucket into overflow and a tag put in for that. If level 1 overflow became full then level 2 overflow was used (pre-allocated at the end of the file) and extra blocks were logically added to the bucket.

The problem occurred when the file ran out of level 2 overflow when trying to WRITE a new record. The FD record buffer was used to do the move of an existing record into overflow to give room for the tag (after the record being written had gone into overflow). There was now no room in the file for the record being moved. An error was given that the record could not be written, but the FD record area no longer contains the record just created, it has an old record that is now no longer in the file.

Even if the WRITE was successful the FD record area may be a different record.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 14)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2017-04-20T18:34:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p26@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p24@usenetarchives.gap> <gap-9e8ab3ead3-p25@usenetarchives.gap> <gap-9e8ab3ead3-p26@usenetarchives.gap>`

```
On Thursday, April 20, 2017 at 11:40:55 PM UTC+2, Richard wrote:
› On Thursday, April 20, 2017 at 10:50:01 AM UTC+12, Bill Woodger wrote:
› 
›› Why would data be left lying around after a WRITE? Do people expect it to be? Yes. 
› 
 
› Case in point.
 
› Even if the WRITE was successful the FD record area may be a different record.

14.9.47.3
General rules
ALL FILES
...
2) The logical record released by the successful execution of the WRITE statement is no longer available in the record area unless the file-name associated with record-name-1 is specified in a SAME RECORD AREA clause.
The logical record is also available as a record of other files referenced in the same SAME RECORD AREA clause as the associated output file, as well as the file associated with record-name-1.
3) The result of the execution of a WRITE statement specifying record-name-1 and the FROM phrase is equivalent to the execution of the following statements in the order specified:
a)The statement:
MOVE identifier-1 TO record-name-1
or
MOVE literal-1 TO record-name-1
according to the rules specified for the MOVE statement.
b) The same WRITE statement without the FROM phrase.
NOTE 14.6.9, Overlapping operands, and 14.9.24, MOVE statementt [sic], general rules, apply to any cases in which a storage area identified by identifier-1 and the record area associated with record-name-1 share any part of their storage
areas. The result of execution of the WRITE statement is undefined if the result of execution of the implicit MOVE statement described in general rule 3a is undefined.

...
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 13)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-04-21T10:59:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p28@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p25@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p24@usenetarchives.gap> <gap-9e8ab3ead3-p25@usenetarchives.gap>`

```
In article <84db88d5-adb9-49bd-b0be-5b8··0@goo··s.com>,
Bill Woodger wrote:
› Hello Vince!
› 
…[7 more quoted lines elided]…
› digits which fit in the size - for performance!".

'Hey, Senior-Level Resource Person, this code has IFs that go on for
pages, what's the reason they didn't use an EVALUATE?'

'Hey, Senior-Level Resource Person, this code's full of 'READ INTOs,
what's the reason for that?'

'Hey, Senior-Level Resource Person, these comments say 'SUBSCRIPT OVERFLOW
FOR TABLE SIZE LIMIT'... what does that mean?'

'There's no need to know anything about that... all besides me are fools
and there are no giants upon whose shoulders you might stand.'

... and I am the King of England.

DD
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 14)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2017-04-21T13:54:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p29@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p28@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p24@usenetarchives.gap> <gap-9e8ab3ead3-p25@usenetarchives.gap> <gap-9e8ab3ead3-p28@usenetarchives.gap>`

```
On Friday, April 21, 2017 at 5:00:01 PM UTC+2, doc··.@pa··x.com wrote:
› 
› Bill Woodger  
…[25 more quoted lines elided]…
› DD

"Always READ INTO, WRITE FROM... that is the Chant of the Elders which I
was taught.

(It was based on the injunction Thou Shalt Not Perform Arithmetic
Operations In A Buffer)"

You can't (well, you can, you did) side-slip into a completely different thing (explaining) from the promulgating the dictation of Cant and Mantra. Make your Straw Man if you like, but it is clear what it is.

There is no reason to "explain" READ ... INTO ... where it is *actually* useful (the entire record required for "one behind"), I guess we will forever disagree on what "*actually* useful" means, I just want to be clear to other readers (their own choice to believe me or not) that there is no "Always READ INTO, WRITE FROM...".

I assume you mean a nested-IF? In which case, the EVALUATE will span pages anyway. Perhaps a better question would be "why does span pages?".

The third is for sure a used technique. It would be obtuse to do that today (so I hope that isn't in your Cant and Mantra as well), but valuable to be able to explain why it was ever done when someone asks. This is entirely different from anything to do with READ ... INTO ... and WRITE ... FROM ..., where a reasonable explanation can be "that's what the programmer chose to do" as well as, for sure, "they were told to do it that way, for reasons irrelevant today (without having to bother with whether or not they were relevant at the time, because it was just Cant and Mantra anyway)".
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 15)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-04-25T07:51:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p30@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p29@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p24@usenetarchives.gap> <gap-9e8ab3ead3-p25@usenetarchives.gap> <gap-9e8ab3ead3-p28@usenetarchives.gap> <gap-9e8ab3ead3-p29@usenetarchives.gap>`

```
In article ,
Bill Woodger wrote:
› On Friday, April 21, 2017 at 5:00:01 PM UTC+2, doc··.@pa··x.com wrote:
›› 
…[36 more quoted lines elided]…
› Mantra. Make your Straw Man if you like, but it is clear what it is.

Mr Woodger, by your own words I did, in fact, get from the Chant of the
Elders into explaining. As long as there's Production Code that might be
made more clear by such techniques then benefit might arise from applying
them.

DD
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 13)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-04-22T22:43:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p31@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p25@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p24@usenetarchives.gap> <gap-9e8ab3ead3-p25@usenetarchives.gap>`

```
On 20/04/17 10:49 AM, Bill Woodger wrote:
› Hello Vince!
› 
…[27 more quoted lines elided]…
› 

Amen to that!

Couldn't agree more emphatically.

Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 11)_

- **From:** "vbcoen" <ua-author-7065949@usenetarchives.gap>
- **Date:** 2017-04-20T09:51:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p32@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p21@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap>`

```
Hello Bill!

Wednesday April 19 2017 23:49, Bill Woodger wrote to All:

> You can 100% rely on all fields in the current record (subject to the
> record description being accurate, and if not accurate INTO/FROM isn't
> going to fix it). When the current record is no longer current, you
> can 100% rely on the data being different, other than by coincidence
> (subject to not using a "record area").

> If newcomers are told that, rather than "Do as I say, and as I do,
> even though neither of us know why, or will ever likely find out,
> we've always done it that way", they are done a service.

I don't tell new programmers how to right code.

I did specify or help to do so depending on site a site standards
document/s for programming, programmer testing, Test docs for the dedicated
Test group/s with processes and procedures and where needed CASE tools etc.

I do not tell a programmer how to write Cobol howver that said there are
recommendations and these do include the reasons why.

May be now adays with modern compilers it is not needed but new progs to
site DO need to know why coding on existing programs were done in a
specific way and the real rish of problems of changing the processes and
the READ into etc is a good example another one is usage of SAME
(RECORD) AREA clauses - a great way of auto creating a lot of bugs just for
the sake of removing them.

I come from the old school at least in management - If it aint broke don't
fix it! As more often than not it will be very expense in both time and
budget.

I still come across cobol code that goes back to the 60's, heck some of
mine (now made O/S) goes back to 65-7. Now must admit that the code has
been changed since but . .

I will put my hand up that one recommendation going back to the late 60's
early 70's was avoid using COMPUTE statements in other than simple math
should be totally avoided as compilers now handle them well although not
may be as efficiently as add/subtract/divide etc at least regarding
rounding etc. The last bit is the only one that might still apply :)


Vince
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 12)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2017-04-20T19:19:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p33@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p32@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p32@usenetarchives.gap>`

```
Hello Vince!

On Thursday, April 20, 2017 at 9:30:02 PM UTC+2, Vince Coen wrote:
› Hello Bill!
› 
…[12 more quoted lines elided]…
› I don't tell new programmers how to right code.
 
› "There is a GOOD reason for this logic" you said. Well, there isn't, until it is shown.
 
› 
› I did specify or help to do so depending on site a site standards
…[5 more quoted lines elided]…
› 
 
› Well, the reason why is?
 
 
› May be now adays with modern compilers it is not needed but new progs to
› site DO need to know why coding on existing programs were done in a
…[4 more quoted lines elided]…
› 

What's to "explain" about READ ... INTO ... and WRITE ... FROM ...? The manual for the compiler will readily deal with that. There is nothing intrinsically "good" or "bad" about them. They are the same as READ ... followed by an equivalent MOVE, or a WRITE ... preceded by the equivalent MOVE.

"Explaining" in any terms beyond that is...? It's not a technique, it's not a method, it's the same thing, and the results are the same.

Nothing "happens" to the data under the FD after a READ, nor before a WRITE, except what has been coded by the programmer. Nothing to explain here.

› I come from the old school at least in management  - If it aint broke don't
› fix it! As more often than not it will be very expense in both time and
…[13 more quoted lines elided]…
› Vince

COMPUTE will always (did I say always?) be faster then multiple other arithmetic operations in other than trivial uses. In trivial use, it will be identical. It's been that way ever since I started.

Of course, that does not mean you can code any random sequence of stuff in a COMPUTE and expect it to work like a calculator (until the COBOL 2014 Standard). Then you see the Cant, Myth, Magic and Mantra with recommendations for excessive numbers of decimal places, because "it is the only way that COMPUTE works".
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 12)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-04-22T22:40:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p34@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p32@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p32@usenetarchives.gap>`

```
On 21/04/17 1:51 AM, Vince Coen wrote:
› Hello Bill!
› 
…[12 more quoted lines elided]…
› I don't tell new programmers how to right code.
 
› I like the unintended homonym there, Vince. :-)
› 
…[5 more quoted lines elided]…
› recommendations and these do include the reasons why.

I too, during the course of a very long career, have been responsible
for writing COBOL Programming standards for a site. Like you, I agree
that the BEST standards are "guidelines" which MUST have the
justification for them explained. Bill Woodger made the same point some
posts back in this thread. An arbitrary "because I say so" or "that's
the way I was taught" can never be OK if you want a site where people
use their intelligence and are not just "coding automatons".
› 
› May be now adays with modern compilers it is not needed but new progs to
…[4 more quoted lines elided]…
› the sake of removing them.

Like Bill, I have never experienced a problem with NOT using READ INTO
or WRITE FROM, but I have never experienced a problem when using them
either. (And I DID write code for the ICL 1900 Richard mentioned and am
familiar with the use of buckets and handling second level overflow...).
I have also never EXPECTED the contents of a WRITE buffer to remain the
same AFTER a WRITE... (You have to cut the compiler writers some slack...)
›
› I come from the old school at least in management - If it aint broke don't
› fix it! As more often than not it will be very expense in both time and
› budget.

Fortunately, that particular Old School is not so popular anymore.
Applying that particular mantra means there is no attempt to improve
things or evolve them further. The FACT is that code will ALWAYS cost
you money and if you intend to continue developing it manually, then you
need (from a Management perspective) to be prepared to spend money on it.
› 
› I still come across cobol code that goes back to the 60's, heck some of
…[9 more quoted lines elided]…
› 
Thankfully, although I was around and programming at that time, I never
heard that one. I have always enjoyed the use of COMPUTE. (You do know
that you can apply the same ROUNDING clause to it that you can to any
other arithmetic verb?)

Nowadays, optimizing compilers will produce good code whether you use
the basic arithmetic verbs or COMPUTE. Historically, I have never
experienced a problem when using it.

So, what comes out of all this is that there is a lot of folklore in
COBOL. Different experiences working on different sites creates
different patterns of use which, after a while, are no longer
questioned, but are simply passed to newbies as the "Wisdom of Elders"
or "That's how we do it here". I have worked on sites where the local
standards actually made code production more difficult and inhibited
productivity... here are some of my favourites:

1. Thou shalt NOT use "NOT" in an IF statement.
2. Thou shalt NOT use "VARYING" more than ONCE in a PERFORM. (Like they
were never going to process tables with more than one dimension, or, if
they did, you need another nested PERFORM...
3. The ONLY acceptable statement following AT END is GO TO. (When I
queried this, I was told it was due to a bug in the IBM Compiler. It
wasn't, of course. Some ancient programmer had screwed up putting verbs
into the AT END branch and decided the compiler must be wrong...
4. Thou shalt NOT nest an IF statement inside an IF statement.

What really bugged me about most of these (so much so, that I remember
them after 30 years) was that the "line of least resistance" was taken.
(the "line of least resistance" is a teaching from the "If it ain't
broke don't fix it!" management school...) Don't teach your people how
to code, just stop them using things that might be troublesome. Let's
all code to the the lowest common denominator of ability, so that poor
old Dopey can do maintenance on it, and that way we'll have no problems.

As noted previously in this thread, I endorse what Bill Woodger is
saying: NO arbitrary Cant, Mantra, or Dogma; investigate what is
problematic, analyze it, resolve it, then document it for others.

In the majority of cases, it is a PICNIC ("Problem in CHAIR, NOT in
computer...)

Finally, you have to ask yourself: "If using READ INTO and WRITE FROM is
the only "safe" way to code, why isn't THAT the Standard?...

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 11)_

- **From:** "vbcoen" <ua-author-7065949@usenetarchives.gap>
- **Date:** 2017-04-21T06:44:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p35@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p21@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap>`

```
Hello Bill!

Friday April 21 2017 00:19, Bill Woodger wrote to All:

You seem to be writing about reasonably modern compilers that have good
test history over time as many new one are derived from a previous
incantation.

In the 60's this was NOT the case at least on IBM 1401, ICL 1900's and
likewise IBM 360.

This also includes the dogs that were issued (and charged for) that we the
programmers had to find bugs and more immportantly find ways around as
patches came very slowly.

Hence the coding standard that had to be introduced to ensure new hires did
not revisit the problems.

The READ / WRITE into/from rules was put into place for good reasons to
avoid possible coding bugs and others have given some of the bug examples.

Here a good example is working on data in the FD area after a write is
issued that will not contain the same data under some (or even all)
conditions.

Wasting programmers time finding bugs in programs that should NOT have been
there in the first place if the programmer had followed the porgramming
standards and recommendation is just time and more importantly budget
wasting and as now in the 60's money was always tight and we had to stick
to the project budget like glue. Excuses for overruns was not reated kindly
by the top management nor the shareholders.

Remember most sites has many different projects on the go at any one time
and at more than one site I was in, programmer costs was > 250,000 per
month.

Some of us apart from the day job had to control costs as well and ensure
projects had to be delivered tested, on time!


> Hello Vince!

> On Thursday, April 20, 2017 at 9:30:02 PM UTC+2, Vince Coen wrote:
>> Hello Bill!
…[18 more quoted lines elided]…
>> I don't tell new programmers how to right code.

> "There is a GOOD reason for this logic" you said. Well, there isn't,
> until it is shown.

>>
>> I did specify or help to do so depending on site a site standards
…[4 more quoted lines elided]…
>> include the reasons why.

> Well, the reason why is?


>> May be now adays with modern compilers it is not needed but new
>> progs to site DO need to know why coding on existing programs were
…[3 more quoted lines elided]…
>> lot of bugs just for the sake of removing them.

> What's to "explain" about READ ... INTO ... and WRITE ... FROM ...?
> The manual for the compiler will readily deal with that. There is
> nothing intrinsically "good" or "bad" about them. They are the same as
> READ ... followed by an equivalent MOVE, or a WRITE ... preceded by
> the equivalent MOVE.

> "Explaining" in any terms beyond that is...? It's not a technique,
> it's not a method, it's the same thing, and the results are the same.

> Nothing "happens" to the data under the FD after a READ, nor before a
> WRITE, except what has been coded by the programmer. Nothing to
> explain here.

>> I come from the old school at least in management - If it aint
>> broke don't fix it! As more often than not it will be very expense
…[8 more quoted lines elided]…
>> might still apply :) Vince

> COMPUTE will always (did I say always?) be faster then multiple other
> arithmetic operations in other than trivial uses. In trivial use, it
> will be identical. It's been that way ever since I started.

> Of course, that does not mean you can code any random sequence of
> stuff in a COMPUTE and expect it to work like a calculator (until the
> COBOL 2014 Standard). Then you see the Cant, Myth, Magic and Mantra
> with recommendations for excessive numbers of decimal places, because
> "it is the only way that COMPUTE works".




Vince
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 12)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2017-04-21T14:01:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p36@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p35@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p35@usenetarchives.gap>`

```
Hello Vince!

On Friday, April 21, 2017 at 12:59:48 PM UTC+2, Vince Coen wrote:
› Hello Bill!
› 
…[5 more quoted lines elided]…
› 

Yes, I've never used a compiler prior to the 1968 Standard. Newcomers will be unlucky if they have to use a compiler to the 1974 Standard (there are some still extant).

[...]

›
› The READ / WRITE into/from rules was put into place for good reasons to
› avoid possible coding bugs and others have given some of the bug examples.
›

Can you point to the bug examples given? I've missed them.

What you'd need is examples where the contents of the FD change all on their own after a READ, or change after the last reference to them in the code and before the WRITE.

Unless either (or both) of those happen, then what was the intrinsic reason for enforcing READ ... INTO ... and WRITE ... FROM ...?
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 13)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-04-25T07:59:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p37@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p36@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p35@usenetarchives.gap> <gap-9e8ab3ead3-p36@usenetarchives.gap>`

```
In article ,
Bill Woodger wrote:
› Hello Vince!
› 
…[12 more quoted lines elided]…
› (there are some still extant).

Newcomers to the shops in which I've worked will work on code written
under the limitations of such compilers... and written under the
incomplete understandings that their Corporate Superiors, past and
present, had of such compilers.

'You cannot use SORT... Senior Regional Director Hoonck was *very*
specific about that!'

'I see... when did Senior Regional Director Hoonck retire?'

'Six years ago.'

'I see... and when was Senior Regional Director Hoonck's funeral?'

'Two years ago... but he was *very* specific about it!'

DD
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 11)_

- **From:** "vbcoen" <ua-author-7065949@usenetarchives.gap>
- **Date:** 2017-04-21T06:59:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p38@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p21@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap>`

```
<01cf8821-bd4e-4961-822b-ed1··e@goo··s.com>

<530a5ecd-1222-4609-a1e4-7d3··6@goo··s.com>
<92c35cf5-0a
Hello Richard!

Thursday April 20 2017 22:40, Richard wrote to All:

Thanks for that, now I remembered the problem, one amonst many others :)

For the ICL 1900 compiler I was at 2 - 3 sites where I was the Compiler
liason between ICT/ICL and the site and that included passing bug reports
back to the dev. team as well as fixes to the compiler that I had coded and
tested against inhouse programs and test systems. Yes I had the source code
for the compiler - it saved time and money.

After the test completed giving correct results the code changes was then
passed to the compiler liason person for inclusion into the next release or
patch and these were issued to all sites (well all sites that had a
maintainance contract of one description or another).

My site/s had this as a freebie to cover my costs not that I was doing this
full time as I was a A/P or Lead A/P at the time working on site
applications using Cobol, Plan and what ever else. The role continued with
the introduction of new range (2900) by which time I was working for ICL
and was also involved in writing VME. I said writing it not designing the
missmash that was the first release - It was written in Algol 68R in a very
modular fashion with very detailed specs so all programming was in fact
just coding directly from the module spec. It did NOT help to see bugs in
the design as each programmer had a block of specs to code that did not
link together. It did allow VME to be written very quickly but the testing
of it was another kettle of fish and yes tested on a 1900 series.

After the first release some modules was rewritten (after design changes)
into S3.

Those were the days :)

> On Thursday, April 20, 2017 at 10:50:01 AM UTC+12, Bill Woodger wrote:

>> Why would data be left lying around after a WRITE? Do people expect
>> it to be? Yes.


> On an ICL 1900 with ISAM files using bucket overflow one can get
> strange results.

> A new record had to go into a particular bucket in the pre-allocated,
> fixed length file to maintain record sequence. If there was no room in
…[6 more quoted lines elided]…
> logically added to the bucket.

> The problem occurred when the file ran out of level 2 overflow when
> trying to WRITE a new record. The FD record buffer was used to do the
…[5 more quoted lines elided]…
> longer in the file.

> Even if the WRITE was successful the FD record area may be a different
> record.



Vince
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 12)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-04-22T22:51:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p39@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p38@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p38@usenetarchives.gap>`

```
On 21/04/17 10:59 PM, Vince Coen wrote:
› <01cf8821-bd4e-4961-822b-ed1··e@goo··s.com>
› 
…[71 more quoted lines elided]…
› 
Very interesting, Vince.

I remember ICL 1900 with great affection and I learned PLAN before I
learned BAL. (Sometimes in conversation, to this day, I say "STOZ
that..." when I wish to withdraw a statement I made; much as a sailor
says "Belay that.." :-)

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 11)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-04-22T21:47:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p40@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p21@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap>`

```
On 20/04/17 7:35 AM, doc··f@pa··x.com wrote:
› In article <530a5ecd-1222-4609-a1e4-7d3··6@goo··s.com>,
› Bill Woodger   wrote:
…[19 more quoted lines elided]…
› 
Really enjoyed this linked story.

I don't remember reading it in 1989 but it is well told and makes a good
point.

Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 12)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-04-25T07:46:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p41@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p40@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p14@usenetarchives.gap> <gap-9e8ab3ead3-p20@usenetarchives.gap> <gap-9e8ab3ead3-p21@usenetarchives.gap> <gap-9e8ab3ead3-p40@usenetarchives.gap>`

```
In article ,
pete dashwood wrote:
› On 20/04/17 7:35 AM, doc··f@pa··x.com wrote:
 
› [snip]
 
›› The Elders had great abilities, Mr Wodger, and could code code such as
›› *ten* programmers cannot, today.  That you have had no problem may speak
…[5 more quoted lines elided]…
› Really enjoyed this linked story.

Pshaw, Mr Dashwood... you'se jes' easily amused.

DD
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 8)_

- **From:** "vbcoen" <ua-author-7065949@usenetarchives.gap>
- **Date:** 2017-04-19T13:03:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p42@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p11@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap>`

```
Hello docdwarf!

Wednesday April 19 2017 12:50, you wrote to All:

> In article <01cf8821-bd4e-4961-822b-ed1··e@goo··s.com>,
> Rick Smith wrote:

> [snip]

>> It also occurs to me that, if there is an interaction, reading
>> the record into working-storage before generating the output
>> from working-storage might correct the problem. You can thank
>> Mr Dwarf if that resolves the problem.

> Always READ INTO, WRITE FROM... that is the Chant of the Elders which
> I was taught.

> (It was based on the injunction Thou Shalt Not Perform Arithmetic
> Operations In A Buffer)

There is a GOOD reason for this logic -

Many compilers, at least on mainframes release the memory after a record is
written and only issues it on a read so by doing READ into and WRITE from
cuts down the possibility of getting silly program faults that get trapped
by the OS which issues a large dump for no good reason :)

Now this is been wriiten by a person that spend many an hour/day/week
reading the blasted things only to find out there was a simple way of
avoiding the issue let alone the dumps.

This does also include spending a year or two on developing the OS where
faults produced dump as I was therefore involved in Dump Cracking and these
run to 1,000 of pages of continious stationery.

Bad enough reading 'em but the carrying was tougher on the arms and back
taking them from the machine room to my office!



Vince
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 9)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2017-04-19T14:59:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p43@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p42@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p42@usenetarchives.gap>`

```
On Wednesday, April 19, 2017 at 7:44:54 PM UTC+2, Vince Coen wrote:
[...]
› 
› There is a GOOD reason for this logic -
…[5 more quoted lines elided]…
› 

Not so.

WRITEs of a sequential data set are to a "buffer". After a WRITE, the FD points to the next available position in the buffer (or in the next buffer, if the previously current one was deemed "full"). Entirely Standard behaviour.

To modify that behaviour, in an entirely Standard way, is simple.

READs are the same.

We've discussed this before elsewhere, Vince https://sourceforge.net/p/open-cobol/discussion/help/thread/b4890407/

Coughing up an old pointless Mantra does a disservice to newcomers to COBOL (and they are there).

If your program logic is correct, there is no problem with leaving data where it was read, or building a record in the definitions beneath an FD.

If your program logic is not correct, then Mantra, even when it "saves" by coincidence, is just Mantra. The program is still incorrect.


[...]
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 10)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-04-19T15:45:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p44@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p43@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p42@usenetarchives.gap> <gap-9e8ab3ead3-p43@usenetarchives.gap>`

```
In article <3bd1cb9d-0422-45e6-b140-75b··d@goo··s.com>,
Bill Woodger wrote:
› On Wednesday, April 19, 2017 at 7:44:54 PM UTC+2, Vince Coen wrote:
› [...]
…[16 more quoted lines elided]…
› To modify that behaviour, in an entirely Standard way, is simple. 

Every line of modified code takes time to disscuss in the Production
Implementation Meeting, Mr Woodger.

[snip]

› Coughing up an old pointless Mantra does a disservice to newcomers to
› COBOL (and they are there).
…[6 more quoted lines elided]…
› by coincidence, is just Mantra. The program is still incorrect.

When black-letter law changes in a way that was not predicted when the
program's skeleton was written a half-century ago there is no 'your
program' or 'your program logic'.

When a newcomer to COBOL asks 'what is the reason for this?' an
Elder-to-be has an explanation.

When a newcomer to COBOL has any sort of difficulty with READ INTO, WRITE
FROM it is time to suggest a different way of making a living.

DD
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 11)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2017-04-19T16:36:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p45@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p44@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p42@usenetarchives.gap> <gap-9e8ab3ead3-p43@usenetarchives.gap> <gap-9e8ab3ead3-p44@usenetarchives.gap>`

```
On Wednesday, April 19, 2017 at 9:45:42 PM UTC+2, doc··.@pa··x.com wrote:
› Bill Woodger   wrote:
›› On Wednesday, April 19, 2017 at 7:44:54 PM UTC+2, Vince Coen wrote:
…[20 more quoted lines elided]…
› Implementation Meeting, Mr Woodger.
 
› Who's talking of modifying anything?
 
› 
› [snip]
…[21 more quoted lines elided]…
› DD

When black-letter law is Cant and nonsense it can be forgotten. Simple.

You'd be happy with this?

READ INPUT-MASTER INTO MASTER-RECORD

If you can explain the Cant, so it isn't Cant, then do so. You can't.

If you have trouble understanding the context of "your program", read it as "the program you are writing".
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 12)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-04-19T17:05:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p46@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p45@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p42@usenetarchives.gap> <gap-9e8ab3ead3-p43@usenetarchives.gap> <gap-9e8ab3ead3-p44@usenetarchives.gap> <gap-9e8ab3ead3-p45@usenetarchives.gap>`

```
In article <63bca544-da91-4b1c-98ca-798··4@goo··s.com>,
Bill Woodger wrote:
› On Wednesday, April 19, 2017 at 9:45:42 PM UTC+2, doc··.@pa··x.com wrote:
›› Bill Woodger   wrote:
 
›› [snip]
 
››› To modify that behaviour, in an entirely Standard way, is simple. 
 
››     ^^^^^^^^^
›› 
…[3 more quoted lines elided]…
› Who's talking of modifying anything?
 
› You introduced it and quoted yourself doing so, Mr Woodger.
 
› 
›› 
…[22 more quoted lines elided]…
› When black-letter law is Cant and nonsense it can be forgotten. Simple.
 
› Simple enough to result in illegal practises.
 
› 
› You'd be happy with this?
…[3 more quoted lines elided]…
› If you can explain the Cant, so it isn't Cant, then do so. You can't.

I believe I am able to explain it automatically but my first response
would be towards The Manual.

DD
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 13)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2017-04-19T17:27:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p47@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p46@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p42@usenetarchives.gap> <gap-9e8ab3ead3-p43@usenetarchives.gap> <gap-9e8ab3ead3-p44@usenetarchives.gap> <gap-9e8ab3ead3-p45@usenetarchives.gap> <gap-9e8ab3ead3-p46@usenetarchives.gap>`

```
Gosh, you mean this? "To modify that behaviour, in an entirely Standard way, is simple."

This means "to modify the behaviour of the use of a 'buffer' for IBM Mainframe COBOLs and to modify the behaviour of whatever (if anything) other compilers do".

It must be worth all of nothing to write the line of code. I'll give you 0.02 euro cents, compiler must be to at least 1985 Standard, and program must compile clean.

Save time during a Review? What, big tick, and don't look at the code if using INTO and FROM?
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 14)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-04-21T10:52:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p48@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p47@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p42@usenetarchives.gap> <gap-9e8ab3ead3-p43@usenetarchives.gap> <gap-9e8ab3ead3-p44@usenetarchives.gap> <gap-9e8ab3ead3-p45@usenetarchives.gap> <gap-9e8ab3ead3-p46@usenetarchives.gap> <gap-9e8ab3ead3-p47@usenetarchives.gap>`

```
In article ,
Bill Woodger wrote:

[snip]

› It must be worth all of nothing to write the line of code.

We each evaluate the worth of our production, Mr Woodger.

Hit the machine ; US$25

Knowing where to hit the machine: substantially more

DD
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 15)_

- **From:** "bill.woodger" <ua-author-14501802@usenetarchives.gap>
- **Date:** 2017-04-21T13:34:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p49@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p48@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p42@usenetarchives.gap> <gap-9e8ab3ead3-p43@usenetarchives.gap> <gap-9e8ab3ead3-p44@usenetarchives.gap> <gap-9e8ab3ead3-p45@usenetarchives.gap> <gap-9e8ab3ead3-p46@usenetarchives.gap> <gap-9e8ab3ead3-p47@usenetarchives.gap> <gap-9e8ab3ead3-p48@usenetarchives.gap>`

```
On Friday, April 21, 2017 at 4:52:57 PM UTC+2, doc··.@pa··x.com wrote:
› Bill Woodger 
› 
…[10 more quoted lines elided]…
› DD

Well, it just can't be done. Avoid that if you will.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 16)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-04-25T07:47:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p50@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p49@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p42@usenetarchives.gap> <gap-9e8ab3ead3-p43@usenetarchives.gap> <gap-9e8ab3ead3-p44@usenetarchives.gap> <gap-9e8ab3ead3-p45@usenetarchives.gap> <gap-9e8ab3ead3-p46@usenetarchives.gap> <gap-9e8ab3ead3-p47@usenetarchives.gap> <gap-9e8ab3ead3-p48@usenetarchives.gap> <gap-9e8ab3ead3-p49@usenetarchives.gap>`

```
In article ,
Bill Woodger wrote:
› On Friday, April 21, 2017 at 4:52:57 PM UTC+2, doc··.@pa··x.com wrote:
›› Bill Woodger 
…[11 more quoted lines elided]…
› Well, it just can't be done. Avoid that if you will.

As easily as I've avoided the schoolyards on which I've heard it.

DD
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 9)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-04-19T15:38:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p51@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p42@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p42@usenetarchives.gap>`

```
In article <149··9@f1.··t.ftn>,
Vince Coen wrote:
› Hello docdwarf!

Good day, Mr Coen!

[snip]

› Bad enough reading 'em but the carrying was tougher on the arms and back
› taking them from the machine room to my office!

Reading dumps was a duty of mixed blessings. On the one hand the
character-development and plot-lines were often wanting...

... on the other hand the sudden denouement of 'There it is!' was always a
source of joy.

DD
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 8)_

- **From:** "vbcoen" <ua-author-7065949@usenetarchives.gap>
- **Date:** 2017-04-19T18:03:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p52@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p11@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap>`

```
Hello Bill!

Wednesday April 19 2017 19:59, Bill Woodger wrote to All:

Your logic may weell be totally valid today BUT for compilers going back to
say :

Well I could say 1401, but will start with 360 such as:

ANSI Cobol
OS/VS 1 and possibly 2.

There was also some of the next batch of compiler with similar issues -
sorry can't remeber the details - too far back. Heck, have enough problems
trying to remember why I went from one room to another at times.

Vince

> On Wednesday, April 19, 2017 at 7:44:54 PM UTC+2, Vince Coen wrote:
> [...]
…[8 more quoted lines elided]…
>>

> Not so.

> WRITEs of a sequential data set are to a "buffer". After a WRITE, the
> FD points to the next available position in the buffer (or in the next
> buffer, if the previously current one was deemed "full"). Entirely
> Standard behaviour.

> To modify that behaviour, in an entirely Standard way, is simple.

> READs are the same.

> We've discussed this before elsewhere, Vince
> https://sourceforge.net/p/open-cobol/discussion/help/thread/b4890407/

> Coughing up an old pointless Mantra does a disservice to newcomers to
> COBOL (and they are there).

> If your program logic is correct, there is no problem with leaving
> data where it was read, or building a record in the definitions
> beneath an FD.

> If your program logic is not correct, then Mantra, even when it
> "saves" by coincidence, is just Mantra. The program is still
> incorrect.


> [...]



Vince
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 9)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-04-22T23:11:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p53@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p52@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p2@usenetarchives.gap> <gap-9e8ab3ead3-p3@usenetarchives.gap> <gap-9e8ab3ead3-p7@usenetarchives.gap> <gap-9e8ab3ead3-p8@usenetarchives.gap> <gap-9e8ab3ead3-p9@usenetarchives.gap> <gap-9e8ab3ead3-p10@usenetarchives.gap> <gap-9e8ab3ead3-p11@usenetarchives.gap> <gap-9e8ab3ead3-p52@usenetarchives.gap>`

```
On 20/04/17 10:03 AM, Vince Coen wrote:
› Hello Bill!
› 
…[14 more quoted lines elided]…
› Vince

Although it is fun remembering old times and Glory Days, it doesn't
actually serve a USEFUL purpose unless lessons are learned and relayed
to the rising generation. (Of course not everything HAS to have a useful
purpose...)

The nub of this debate comes down to:

1. Do the lessons learned using software from 40 years ago, still have
relevance today? (My answer would be: Probably, in some cases. But in
general principles, rather than specific code, like READ INTO. I'm sure
others will have other answers...)

2. Should we accept Cant, Mantra, and arbitrary demands, without
question, or should we encourage people to think and question for
themselves?

I'll let my posts here over the past 30 years speak to my position on
this one.

Pete.

I used to write COBOL; now I can do anything...
```

#### ↳ Re: Report Writer

- **From:** "jlturriff" <ua-author-14501849@usenetarchives.gap>
- **Date:** 2018-09-25T01:52:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p54@usenetarchives.gap>`
- **In-Reply-To:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au>`

```
Paul Richards wrote:

› I know that the COBOL RW is for producing printed reports. However is
› it possible to use RW to produce a report for screen display?
›
Possibly, but would it not be better to use the SCREEN SECTION,
etc?
JLT
```

##### ↳ ↳ Re: Report Writer

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-09-30T23:00:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e8ab3ead3-p55@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e8ab3ead3-p54@usenetarchives.gap>`
- **References:** `<VbGdnXuzfulRwHDFnZ2dnUU7-cvNnZ2d@westnet.com.au> <gap-9e8ab3ead3-p54@usenetarchives.gap>`

```
On 25/09/2018 5:52 PM, J Leslie Turriff wrote:
› Paul Richards wrote:
› 
…[5 more quoted lines elided]…
› 
This post made me smile; it's like 2 bald men fighting for a comb...

Two obsolete facilities in an obsolete language... which should be used
to display results?

in this century the problem of how best to display stuff has been long
solved. COBOL can CALL Crystal reports or the really superb reporting
facility StimulSoft, or you can pick a solution from any of those found
here:

https://en.wikipedia.org/wiki/List_of_reporting_software

Deciding between RW or SCREEN SECTION might as well include DISPLAY UPON
CONSOLE...

Pete.

I used to write COBOL; now I can do anything...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
