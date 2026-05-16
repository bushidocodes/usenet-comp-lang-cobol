[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EOF location?

_39 messages · 11 participants · 2006-05_

---

### EOF location?

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-05-27T16:00:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<127hfdman9s836f@news.supernews.com>`

```
Anyone know where the EOF is supposed to be located on a PC file?

In other words, if Windows reports a file is, say, 100 bytes long, is the 
EOF (X'1A') supposed to be in the 100th or 101st byte?

I've got copy books with both conditions and I suspect this inconsistency is 
screwing up PowerCOBOL's "#INCLUDE" commands. (I suspect this because I get 
the dreaded "...error in .SVD file according to INCLUDE or COPY turnip...")

Diligent research reveals I've got 107 copy books of which 33 have the EOF 
beyond the size reported by Windows and 74 files where the Windows-reported 
length includes the EOF.

And shouldn't a copy book end with a CR or LF?

It's a mystery...

I'm going to have a lie-down.
```

#### ↳ Re: EOF location?

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-27T14:32:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148765557.999846.166770@y43g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<127hfdman9s836f@news.supernews.com>`
- **References:** `<127hfdman9s836f@news.supernews.com>`

```
> In other words, if Windows reports a file is, say, 100 bytes long, is the
> EOF (X'1A') supposed to be in the 100th or 101st byte?

There is no need for there to be a x'1A' (Ctrl-Z) at all.  The EOF is
indicated by the size of the file.

The use of x'1A' was actually in CP/M of the 1970s when the size of the
file was only the number of blocks (of 128byte) that it contained.  The
program (eg the text editor) had to fill the remainder of the last
block with Ctrl-Z and then trim these off on reading.

As MS-DOS was initially a clone of CP/M for 8086 much CP/M software
could be ported to it and these still used Ctrl-Z even though MS-DOS
maintained the file size in bytes.  As Windows was initially just a
graphics front-end running on top of DOS it maintained all the legacy
stuff from the 70s, as did much of the software.

> Diligent research reveals I've got 107 copy books of which 33 have the
> EOF beyond the size reported by Windows and 74 files where the
> Windows-reported length includes the EOF.

There _isn't_ anything in the file that is "beyond the reported
length".  The Length is of all the content.  What lises beyond that
length in the remainder of the block/buffer is irrelevant and not part
of the file.

That is, 'EOF' is not a character, it is a state.

> And shouldn't a copy book end with a CR or LF?

No.  It can, it may, it could, but 'should' is not the word I would
use.
```

#### ↳ Re: EOF location?

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-28T17:35:00+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4dsr45F1bi54rU1@individual.net>`
- **References:** `<127hfdman9s836f@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:127hfdman9s836f@news.supernews.com...
> Anyone know where the EOF is supposed to be located on a PC file?
>

Er...please sir! please sir!... at the END of the file, sir!

> In other words, if Windows reports a file is, say, 100 bytes long, is the 
> EOF (X'1A') supposed to be in the 100th or 101st byte?
>

I did a quick experiment using a DOS box....

Here's the results... (I have added comments for those who were not born 
when the only option was a command line interface...these comments (as this 
is a COBOL forum) are prefixed with *>

================== start of DOS box ===============

Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.

*> Create a simple text file with the characters 1 thru 8...

C:\Documents and Settings\dashwood>echo 12345678 > testfile.txt

*> Make sure that textfile.txt DOES contain the expected characters...

C:\Documents and Settings\dashwood>type testfile.txt
12345678

*> Get a directory report on the file...

C:\Documents and Settings\dashwood>dir testfile.txt
 Volume in drive C is PetesP4system
 Volume Serial Number is D499-5305

 Directory of C:\Documents and Settings\dashwood

28/05/2006  17:07                11 testfile.txt
               1 File(s)             11 bytes
               0 Dir(s)  10,042,187,776 bytes free

It would appear that there are three more characters than we actually input.

Windows reports the file as 11 bytes; yet only 8 characters were input...

Looks like a job for Hex Editor...(AXE version 3 ...)

31 32 33 34 35 36 37 38 20 0d 0a

Aha! NINE characters were input; I inadvertently entered a space... (x20)

So, the answer to your question:

YES, the two characters which indicate EOF (in the Windows environment) ARE 
included in the file size reported by the Operating System. Your Hex 1F EOF 
is incorrect for a text file (possibly COBOL uses a different EOF, but I 
doubt it); it is x'0D' x'0A' and both these characters ARE INCLUDED in the 
size reported by the OS.


> I've got copy books with both conditions and I suspect this inconsistency 
> is screwing up PowerCOBOL's "#INCLUDE" commands. (I suspect this because I 
> get the dreaded "...error in .SVD file according to INCLUDE or COPY 
> turnip...")

Fell into the old PowerCOBOL #include trap, huh :-)... best avoided. I used 
it for a while then completely scrapped it.

> Diligent research reveals I've got 107 copy books of which 33 have the EOF 
> beyond the size reported by Windows and 74 files where the 
> Windows-reported length includes the EOF.
>
> And shouldn't a copy book end with a CR or LF?

As you can see from the above, it does...

HTH,

Pete
```

##### ↳ ↳ Re: EOF location?

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-05-28T02:37:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<127ihcv1n0jub63@corp.supernews.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
news:4dsr45F1bi54rU1@individual.net...
>
> "HeyBub" <heybubNOSPAM@gmail.com> wrote in message
…[6 more quoted lines elided]…
> > In other words, if Windows reports a file is, say, 100 bytes long, is
the
> > EOF (X'1A') supposed to be in the 100th or 101st byte?
> >
…[4 more quoted lines elided]…
> when the only option was a command line interface...these comments (as
this
> is a COBOL forum) are prefixed with *>
>
…[26 more quoted lines elided]…
> It would appear that there are three more characters than we actually
input.
>
> Windows reports the file as 11 bytes; yet only 8 characters were input...
…[9 more quoted lines elided]…
> YES, the two characters which indicate EOF (in the Windows environment)
ARE
> included in the file size reported by the Operating System. Your Hex 1F
EOF
> is incorrect for a text file (possibly COBOL uses a different EOF, but I
> doubt it); it is x'0D' x'0A' and both these characters ARE INCLUDED in the
> size reported by the OS.

So that settles it?

Try using, copy con: testfile.txt.
After typing the numbers 1 through 8, press F6 then Enter.

On Windows 98SE, I get 8 characters in the file.
```

###### ↳ ↳ ↳ Re: EOF location?

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-28T20:07:43+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4dt42nF1brnadU1@individual.net>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:127ihcv1n0jub63@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
…[69 more quoted lines elided]…
> So that settles it?


> Try using, copy con: testfile.txt.
> After typing the numbers 1 through 8, press F6 then Enter.
>
> On Windows 98SE, I get 8 characters in the file.
>
Copying a console stream (or an existing file) is NOT the same thing at all. 
The COPY command will only duplicate EXACTLY what it gets (this can be 
modified by the various options to the command, but the default is an exact 
duplication of whatever is in operand 1). If there is no EOF marker then it 
won't be copied or created on the output.  That is why I chose to use ECHO 
and redirect the output from it.

What does F6 do?

As to it being settled, that is for HeyBub to decide. If he's using Win 98 
SE he may be very interested in your results.

Pete.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-05-28T05:57:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<127it2ff7bacs46@corp.supernews.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com> <4dt42nF1brnadU1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
news:4dt42nF1brnadU1@individual.net...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message
…[19 more quoted lines elided]…
> >> Here's the results... (I have added comments for those who were not
born
> >> when the only option was a command line interface...these comments (as
> > this
…[31 more quoted lines elided]…
> >> Windows reports the file as 11 bytes; yet only 8 characters were
input...
> >>
> >> Looks like a job for Hex Editor...(AXE version 3 ...)
…[3 more quoted lines elided]…
> >> Aha! NINE characters were input; I inadvertently entered a space...
(x20)
> >>
> >> So, the answer to your question:
…[5 more quoted lines elided]…
> >> is incorrect for a text file (possibly COBOL uses a different EOF, but
I
> >> doubt it); it is x'0D' x'0A' and both these characters ARE INCLUDED in
> >> the
…[10 more quoted lines elided]…
> Copying a console stream (or an existing file) is NOT the same thing at
all.

I agree that COPY is not the same as redirecting ECHO;
but it demonstrates that x"0D" x"0A" is not an EOF marker
--file size is.

> The COPY command will only duplicate EXACTLY what it gets (this can be
> modified by the various options to the command, but the default is an
exact
> duplication of whatever is in operand 1). If there is no EOF marker then
it
> won't be copied or created on the output.  That is why I chose to use ECHO
> and redirect the output from it.
>
> What does F6 do?

On MS-DOS 1.0 through Windows 98SE, apparently, it
insert a Ctrl+Z (or x"1A") into the stream. Only that preceeding
the Ctrl+Z is copied.

> As to it being settled, that is for HeyBub to decide. If he's using Win 98
> SE he may be very interested in your results.

Or some additional experimentation might be revealing.
For example,

echo 12345678^Z > testfile.txt

where "^Z" is Ctrl+Z, creates a file with an embedded
x"1A" and terminated by x"0D" x"0A; and with a file
size of 12. [For HeyBub, the x"1A" is in the 9th, not the
12th or 13th position.]

Then

type testfile.txt > testfile2.txt

Creates a file with a file size of 8--no embedded x"1A"
and no termianting x"0D" x"0A".

The type command reads until it encounters a x"1A" or
end of file; but Windows does not insert additional characters
in the output file, as an EOF marker.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-29T00:33:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4dtjl5F1btl54U1@individual.net>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com> <4dt42nF1brnadU1@individual.net> <127it2ff7bacs46@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:127it2ff7bacs46@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
…[95 more quoted lines elided]…
> --file size is.

I never intended to suggest otherwise, Rick.

I know very well that size determines the length of a file and I have 
written bit stream IO routines in both x86 assembler and COBOL that utilise 
this fact. Nevertheless, I wasn't 100% sure what might happen when a line 
sequential file was created in this environment.  The above test seems to 
indicate that, when using COBOL files of type line sequential in this 
environment CR LF ARE used to indicate the end of the file. The question was 
whether these 'tokens' are included in the file size and my answer is that 
they are.

I did NOT say that every file will include these characters, I did NOT say 
that EOF is always indicated by these characters, I siimply responded to the 
specific case that was presented.

I think your point is taken that there are cases where they are not used as 
EOF markers or are entirely absent. I see that Richard made a clear 
statement about this too.


>> The COPY command will only duplicate EXACTLY what it gets (this can be
>> modified by the various options to the command, but the default is an
…[11 more quoted lines elided]…
> the Ctrl+Z is copied.

Interesting. I never knew that. Thanks.
>
>> As to it being settled, that is for HeyBub to decide. If he's using Win 
…[11 more quoted lines elided]…
> 12th or 13th position.]

I don't believe PowerCOBOL #INCLUDE files use this format, but, I haven't 
checked and it is interesting, nonetheless.

>
> Then
…[9 more quoted lines elided]…
>

It might be best for HeyBub to simply use a hex editor on one of his Include 
files and see how it is formatted.

Pete.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 6)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-28T15:24:20+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e5c8aa$8k6$00$1@news.t-online.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com> <4dt42nF1brnadU1@individual.net> <127it2ff7bacs46@corp.supernews.com> <4dtjl5F1btl54U1@individual.net>`

```
Sorry PD, CR/LF has never, and will never indicate EOF.
CR/LF indicates end-of-line (EOL)(in a text file); period.
The extra end-of-file (EOF) byte comes from MSDOS which indeed
inserted an ASCII 26 (control-z) at end of file.
Modern windows "command window" do NOT insert
this EOF anymore although they will read/interpret it.

Roger

"Pete Dashwood" <dashwood@enternet.co.nz> schrieb im Newsbeitrag 
news:4dtjl5F1btl54U1@individual.net...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message 
…[176 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-05-28T14:15:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3gieg.714$VE1.70@newssvr14.news.prodigy.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com> <4dt42nF1brnadU1@individual.net> <127it2ff7bacs46@corp.supernews.com> <4dtjl5F1btl54U1@individual.net> <e5c8aa$8k6$00$1@news.t-online.com>`

```
"Roger While" <simrw@sim-basis.de> wrote in message
news:e5c8aa$8k6$00$1@news.t-online.com...
> Sorry PD, CR/LF has never, and will never indicate EOF.
> CR/LF indicates end-of-line (EOL)(in a text file); period.
…[3 more quoted lines elided]…
> this EOF anymore although they will read/interpret it.

We seem to have reached a point where the difference between the computer's
operating system and the application has become blurred.

What characters are written to disk, and how they are read back, is a
function of the application which writes or reads. The Windows and its
predecessor MS-DOS operating systems are totally ignorant of any special
meanings for any character.

"By convention" CRLF means "end of record when the application considers the
file a text file" and this convention is respected by all applications which
consider themselves "text editor/viewer" applications. (FWIW, the definition
of a "text" file as a "collection of carriage-return-line-feed delimited
logical records" is about as universal a definition as exists).

Also "by convention" a "text file" is terminated by Ctrl-Z (0x1A), but this
is nowhere near as widely recognized; or more accurately, is no longer as
widely recognized as it used to be.

Type at a prompt "1,2,3,4,5,6,<enter>?"  The application reading the
keystrokes (in this case the command shell) arbitrarily decides that <Enter>
means "add CR LF to the file".

Need 0x1A?    Type 1,2,3,4,5,6,<Ctrl-z>  using the same application, the
command shell - you got it. Type <Ctrl-z> in another 'text editor'
application such as Notepad - you get nada; or maybe a beep; or maybe "The
quick brown fox jumped over the lazy white dog  <CRLF>."   Hit the "F6" key?
The command shell application decides this means "append a single 0x1A to
the file."

Bottom line is, on the MS-DOS and WIndows operating systems all files are
but a stream of bytes; there are no end-of-record markers, there is no
end-of-file marker; all characaters stored in the file are equally
considered valid 'data' characters. (Not necessarily true of other operating
systems.).

Only by understanding this and your application requirements can you select
the proper COBOL tool for the task at hand.. shall I use what my compiler
application calls a LINE SEQUENTIAL file organization? Or shall I treat the
file as a stream of bytes and locate the logical records myself by finding
the CRLF (or other record-delimiting ) characters?  And what should my
application do if it finds a byte which is a 0x1A character?

Yes, Ye Olde Bane of 'application-specific' strikes again!


MCM
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-29T02:58:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4dts58F1a6i9fU1@individual.net>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com> <4dt42nF1brnadU1@individual.net> <127it2ff7bacs46@corp.supernews.com> <4dtjl5F1btl54U1@individual.net> <e5c8aa$8k6$00$1@news.t-online.com> <3gieg.714$VE1.70@newssvr14.news.prodigy.com>`

```
Thanks Michael,

A very concise and accurate summation of the points discussed.

Pete.

TOP POST nothing new below...

"Michael Mattias" <michael.mattias@gte.net> wrote in message 
news:3gieg.714$VE1.70@newssvr14.news.prodigy.com...
> "Roger While" <simrw@sim-basis.de> wrote in message
> news:e5c8aa$8k6$00$1@news.t-online.com...
…[72 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 8)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-28T12:58:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148846314.665773.301020@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<3gieg.714$VE1.70@newssvr14.news.prodigy.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com> <4dt42nF1brnadU1@individual.net> <127it2ff7bacs46@corp.supernews.com> <4dtjl5F1btl54U1@individual.net> <e5c8aa$8k6$00$1@news.t-online.com> <3gieg.714$VE1.70@newssvr14.news.prodigy.com>`

```
> (FWIW, the definition
> of a "text" file as a "collection of carriage-return-line-feed delimited
> logical records" is about as universal a definition as exists).

No. Macintosh software uses CR alone as a line terminator, Unix/Linux
use LF alone, CP/M used CR+LF which MS-DOS and Windows continued with.

Fortunately file transfer software, such as ftp, converts these as the
file is transferred when in ASCII mode.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 8)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-05-29T15:32:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<suEeg.2515$sK6.949@edtnps90>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com> <4dt42nF1brnadU1@individual.net> <127it2ff7bacs46@corp.supernews.com> <4dtjl5F1btl54U1@individual.net> <e5c8aa$8k6$00$1@news.t-online.com> <3gieg.714$VE1.70@newssvr14.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message 
news:3gieg.714$VE1.70@newssvr14.news.prodigy.com...
>
> Bottom line is, on the MS-DOS and WIndows operating systems all files are
> but a stream of bytes; there are no end-of-record markers, there is no
> end-of-file marker; all characaters stored in the file are equally
> considered valid 'data' characters.

    To further support this view, in Java, the function[*] which is used to 
read a byte can return any value from -1 to 255. If you get values between 0 
and 255, that means the function actually did manage to read a byte from the 
file, and it may very well be 0x1A (AKA CTRL-Z). If that function 
returns -1, that means that the end of the file has been reached.

    A byte, as we all know, can have one of 256 possible values, but this 
read function may return one of 257 possible values. So a file could, for 
example, start with a 0x1A, and then have a 0x41 (the capital letter 'A'), 
and then just end right there and then, with no line feeds, carriage 
returns, or CTRL-Zs or anything else. In Java, you'd receive the decimal 
values 27, 33 and -1 to represent this stream of bytes of length 2.

    - Oliver

[*] Actually, there's more than one way to read data from a file. The one 
I'm referring to here, for the curious, is java.io.FileInputStream.read().
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-29T02:54:36+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4dtrtiF1c1uo8U1@individual.net>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com> <4dt42nF1brnadU1@individual.net> <127it2ff7bacs46@corp.supernews.com> <4dtjl5F1btl54U1@individual.net> <e5c8aa$8k6$00$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message 
news:e5c8aa$8k6$00$1@news.t-online.com...
> Sorry PD, CR/LF has never, and will never indicate EOF.
.
Don't be sorry.  I agree. :-)

I was confusing EOR with EOF in a line sequential file.

My bad.

Pete.

> CR/LF indicates end-of-line (EOL)(in a text file); period.
> The extra end-of-file (EOF) byte comes from MSDOS which indeed
…[3 more quoted lines elided]…
>

EOF in modern windows systems is recognised from the file size
> Roger
>
…[185 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-05-28T10:43:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<127jds6j7p7f6e8@corp.supernews.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com> <4dt42nF1brnadU1@individual.net> <127it2ff7bacs46@corp.supernews.com> <4dtjl5F1btl54U1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
news:4dtjl5F1btl54U1@individual.net...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message
…[28 more quoted lines elided]…
> >> >> when the only option was a command line interface...these comments
(as
> >> > this
> >> >> is a COBOL forum) are prefixed with *>
…[10 more quoted lines elided]…
> >> >> *> Make sure that textfile.txt DOES contain the expected
characters...
> >> >>
> >> >> C:\Documents and Settings\dashwood>type testfile.txt
…[14 more quoted lines elided]…
> >> >> It would appear that there are three more characters than we
actually
> >> > input.
> >> >>
…[18 more quoted lines elided]…
> >> >> is incorrect for a text file (possibly COBOL uses a different EOF,
but
> > I
> >> >> doubt it); it is x'0D' x'0A' and both these characters ARE INCLUDED
in
> >> >> the
> >> >> size reported by the OS.
…[16 more quoted lines elided]…
> I never intended to suggest otherwise, Rick.

Well, OK; but, specifically, it was "the two characters
which indicate EOF (in the Windows environment)"
that threw me.

> I know very well that size determines the length of a file and I have
> written bit stream IO routines in both x86 assembler and COBOL that
utilise
> this fact. Nevertheless, I wasn't 100% sure what might happen when a line
> sequential file was created in this environment.  The above test seems to
> indicate that, when using COBOL files of type line sequential in this
> environment CR LF ARE used to indicate the end of the file.

I would suggest that the CR LF appeared in the last
two positions of the file because ECHO sent them to
the screen, they were redirected to the file, and they
happen to have been the last two characters before
the file was closed.

> The question was
> whether these 'tokens' are included in the file size and my answer is that
…[3 more quoted lines elided]…
> that EOF is always indicated by these characters, I siimply responded to
the
> specific case that was presented.
>
> I think your point is taken that there are cases where they are not used
as
> EOF markers or are entirely absent. I see that Richard made a clear
> statement about this too.
…[5 more quoted lines elided]…
> >> duplication of whatever is in operand 1). If there is no EOF marker
then
> > it
> >> won't be copied or created on the output.  That is why I chose to use
…[26 more quoted lines elided]…
> checked and it is interesting, nonetheless.

One feature of Micro Focus that may apply to Fijitsu,
is the ability to embed control characters in a COBOL
source file. These control characters are saved in the
file with a nul character (x"00") preceeding each control
character. With this ability, it is possible that a x"1A'
could appear almost anywhere in a COBOL source
file.

[For those who may not be aware,
Hexadecimal literals and concatenation did not become
standard COBOL until 2002. If one had a need for
conformance to COBOL 85 and to insert a control
character into an alphanumeric literal one could (for
ASCII on MS-DOS) enter Alt+026 to place the
character into the literal, directly, or one could, during
initialization, move function char (27) to identifier (3:1),
for example, to place the character there, indirectly.
Now it seems more clear to use: "AB" & x"26" & "DE".]

> >
> > Then
…[11 more quoted lines elided]…
> It might be best for HeyBub to simply use a hex editor on one of his
Include
> files and see how it is formatted.

Off-hand, I can think of no substitute for knowing what
should be there and why.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 6)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-05-28T15:25:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<127k1nrac8jks10@news.supernews.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com> <4dt42nF1brnadU1@individual.net> <127it2ff7bacs46@corp.supernews.com> <4dtjl5F1btl54U1@individual.net>`

```
Pete Dashwood wrote:
>>
>
> It might be best for HeyBub to simply use a hex editor on one of his
> Include files and see how it is formatted.

I did. Some files include the X'1A' byte as part of the recorded file 
length, some don't. That's the confusion.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-28T18:15:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148865324.690700.232810@38g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<127k1nrac8jks10@news.supernews.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com> <4dt42nF1brnadU1@individual.net> <127it2ff7bacs46@corp.supernews.com> <4dtjl5F1btl54U1@individual.net> <127k1nrac8jks10@news.supernews.com>`

```
> I did. Some files include the X'1A' byte as part of the recorded file
> length, some don't. That's the confusion.

You are only confused in thinking that x'1A' has any significance to
MS-DOS/Windows, it neither knows nor cares whether a file has one or
not.  Actually Windows/DOS does not care about CR/LF in disk files
either, the console does action various control characters though so
copying a file to the console shows the file in lines.

It may be relevant whether a particular program thinks that x'1a' does
end the file, but only where there are significant characters beyond
that.

The x'1a's found in some files are likely to be the remnants of using
old DOS editors, possibly ones originally designed for CP/M where the
x'1a' is useful.  Strip them all out and forget about it.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-29T22:20:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4e0072F1cc721U1@individual.net>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com> <4dt42nF1brnadU1@individual.net> <127it2ff7bacs46@corp.supernews.com> <4dtjl5F1btl54U1@individual.net> <127k1nrac8jks10@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:127k1nrac8jks10@news.supernews.com...
> Pete Dashwood wrote:
>>>
…[6 more quoted lines elided]…
>
Guess it depends on how and where the files were created?

Can you establish a pattern?

Pete.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 8)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-05-29T11:28:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZVAeg.100153$F_3.89652@newssvr29.news.prodigy.net>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com> <4dt42nF1brnadU1@individual.net> <127it2ff7bacs46@corp.supernews.com> <4dtjl5F1btl54U1@individual.net> <127k1nrac8jks10@news.supernews.com> <4e0072F1cc721U1@individual.net>`

```
"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message
news:4e0072F1cc721U1@individual.net...
>
> "HeyBub" <heybubNOSPAM@gmail.com> wrote in message
…[12 more quoted lines elided]…
> Can you establish a pattern?

That's the point- there is no pattern.... as Richard pointed out, some
editors do, some editors don't.. just as some applications write files with
a Ctrl-Z EOF marker and other applications don't. With some it may be an
option (e.g., Ultra-Edit allows you to 'save as PC or Unix delimited text".

Basically, it comes down to answering the question , "does <single character
eg 0x1A or character string eg 0x0D0A> have any meaning to my application?"
Maybe it does, maybe it doesn't.

I had one about six months ago... I was converting data for a client in
Florida; the input used 0x1A as a FIELD delimiter. Would have been a pretty
crummy conversion had I treated it as EOF, no?  OK, so that file was never
presented as a "text" file, but it still makes the point that any character
in a file has meaning only in an applications context.


MCM
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-05-29T12:26:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e5epaj$8lf$1@reader1.panix.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <127k1nrac8jks10@news.supernews.com> <4e0072F1cc721U1@individual.net> <ZVAeg.100153$F_3.89652@newssvr29.news.prodigy.net>`

```
In article <ZVAeg.100153$F_3.89652@newssvr29.news.prodigy.net>,
Michael Mattias <michael.mattias@gte.net> wrote:

[snip]

>OK, so that file was never
>presented as a "text" file, but it still makes the point that any character
>in a file has meaning only in an applications context.

Gosh... it seems that, once again, 'meaning is the result of 
interpretation'.

DD
```

###### ↳ ↳ ↳ Re: EOF location?

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-05-28T08:11:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QWceg.177289$eR6.83536@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<127ihcv1n0jub63@corp.supernews.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127ihcv1n0jub63@corp.supernews.com>`

```


Rick Smith wrote:

> (snip) 
> So that settles it?
…[4 more quoted lines elided]…
> On Windows 98SE, I get 8 characters in the file.

On Windows XP this doesn't work exactly the same for me.  F6 recalls 
the "copy con: textfile.txt" command and wipes out the 12345678 string.

So I have to type the eight digits, then type CTRL-Z, and then press 
enter.  But once I got past that, I get similar results.

The DIR command reports the file is exactly eight bytes long, and my 
homegrown hex viewer just shows nulls after the eight character string.

I can edit that file with Notepad, inserting characters in the middle, 
and the resulting file still ends with Nulls instead of 0D 0A 1A.

On the other hand, using the ECHO command to write (or append) to a 
text file can be used inside a .BAT file, if you don't mind the 0D 0A 
at the end of the line.

With kindest regards,
```

##### ↳ ↳ Re: EOF location?

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-05-29T09:17:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<127m0hs2180amf2@news.supernews.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net>`

```
Pete Dashwood wrote:
>> I've got copy books with both conditions and I suspect this
>> inconsistency is screwing up PowerCOBOL's "#INCLUDE" commands. (I
…[4 more quoted lines elided]…
> I used it for a while then completely scrapped it.

I was advised to use #INCLUDE in the DATA DIVISION and COPY in the PROCEDURE 
DIVISION by a factotum at Fijutsu some time back.

Be that as it may, I've diligently gone through the program at issue, 
replacing all #INCLUDE and COPY statements with their corresponding source 
modules. I *still* get the error:

   "An error was found in the debug information file. File 
name=BISNS310A.svd Please correct a program when corresponding to notes of 
#INCLUDE and COPY."

What's the circumvention? (I've tried the extremes of cursing and prayer.)
```

###### ↳ ↳ ↳ Re: EOF location?

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-05-29T11:45:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148928350.370646.185330@u72g2000cwu.googlegroups.com>`
- **In-Reply-To:** `<127m0hs2180amf2@news.supernews.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127m0hs2180amf2@news.supernews.com>`

```
Is it time to look "sideways", for example, are your paths correct,
have you got an old member somewhere in the access paths, have you made
any configuration changes lately, or, if on a company system, has
someone else made them, is it related to a compiler required service,
etc?
```

###### ↳ ↳ ↳ Re: EOF location?

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-31T00:45:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4e2t4iF1ch2hkU1@individual.net>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <127m0hs2180amf2@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:127m0hs2180amf2@news.supernews.com...
> Pete Dashwood wrote:
>>> I've got copy books with both conditions and I suspect this
…[8 more quoted lines elided]…
> PROCEDURE DIVISION by a factotum at Fijutsu some time back.

Yes, I wasted several weeks following the advice I received regarding 
undocumented dialogs appearing out of COM components written in PowerCOBOL. 
In the end I solved it myself by rewriting the whole lot in OO NetCOBOL.

Their support has been abysmal and it is one of the reasons I didn't 
upgrade.

>
> Be that as it may, I've diligently gone through the program at issue, 
…[5 more quoted lines elided]…
> #INCLUDE and COPY."

Have you tried compiling with debug options off? (Turn OFF TEST)
Have you made sure that the .SVD file is in the SAME DIRECTORY as the 
executable?
Check comments in your INCLUDE file. Make sure that asterisks or NOTE 
statements are in the right place and legal.
If you are compiling some of the app. from a Fujitsu COBOL Project and other 
parts of it from external files, this can be problematic. Best to include 
all required modules in the Project and let it generate the appropriate MAKE 
file.

>
> What's the circumvention? (I've tried the extremes of cursing and prayer.)
If none of the above Band Aids help, mail me the Project File, with the 
#INCLUDEs and COPY statements expanded as you noted. I can establish whether 
the problem is in your environment or the source code.

Pete.
```

##### ↳ ↳ Re: EOF location?

- **From:** Clever Monkey <clvrmnky.invalid@hotmail.com.invalid>
- **Date:** 2006-05-29T15:28:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **In-Reply-To:** `<4dsr45F1bi54rU1@individual.net>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net>`

```
Pete Dashwood wrote:
> "HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
> news:127hfdman9s836f@news.supernews.com...
…[58 more quoted lines elided]…
> 
It is not quite correct to say that the 0D0A pair indicates any sort of 
EOF marker.  An ASCII CRLF pair are actually "line separators" used to 
distinguish one line from the other.  A single 0x1A (control-Z in ASCII) 
is used to indicate EOF, similar to EOT in POSIX environments.

What happens if we have two lines in a text file on some sort of 
DOS/Win32 machines:

[...]
17$ cat testfile.txt
123456789
123456789
18$ od -hc testfile.txt
0000000000    31  32  33  34  35  36  37  38  39  0D  0A  31  32  33  34  35
                1   2   3   4   5   6   7   8   9  \r  \n   1   2   3 
4   5
0000000020    36  37  38  39  0D  0A
                6   7   8   9  \r  \n
0000000026
19$ wc testfile.txt
       2       2      22    testfile.txt
20$ ls -l testfile.txt
-rw-rw-rw-   1 user     group          22 May 29 15:00 testfile.txt
21$
[...]

As we can see, those "\r\n" pairs are at the end of every line, not the 
end of every file.  We have two lines of text, separated by the CRLF 
pairs.  (Win32 is pretty relaxed, in that the last CRLF pair can 
actually be omitted. In this case we have a "normalized" file).  Each 
line is 11 characters long; 9 characters and two line-end characters. 
Note also that the size in bytes is the same as the character count.

I assume it would depend on the file APIs in question, but it is typical 
for routines to return lengths that include all the characters, 
including the CRLF pair.  The EOF/EOT marker is "present", but is 
usually used up by API calls that scan for it while retrieving the 
contents of a file.

This implies that those routines that count characters will ignore the 
EOF.  Indeed, those routines will likely stop whatever they are doing 
immediately once they encounter the EOF and return with whatever they 
got so far.  Applications that use the usual APIs to get at the contents 
of text files will normally never count or show the trailing EOF.
```

###### ↳ ↳ ↳ Re: EOF location?

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-05-29T22:58:34+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e5fn9v$iof$03$1@news.t-online.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca>`

```
Can you stop talking rubbish and refer to my previous post.
There is so much wrong in this post that defies belief.

Roger

"Clever Monkey" <clvrmnky.invalid@hotmail.com.invalid> schrieb im 
Newsbeitrag news:YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca...
> Pete Dashwood wrote:
>> "HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
…[103 more quoted lines elided]…
> text files will normally never count or show the trailing EOF.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-31T00:57:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4e2tpjF1cnofiU1@individual.net>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca> <e5fn9v$iof$03$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message 
news:e5fn9v$iof$03$1@news.t-online.com...
> Can you stop talking rubbish and refer to my previous post.
> There is so much wrong in this post that defies belief.
>
Could you point some of it out, Roger?

Up until the para that starts "I assume..." it looked OK to me. He pointed 
out my error which I had already admitted to, but his examples looked 
good... I would disagree with some of what came after that, but I think it 
is probably arguable.

What am I missing here?

Pete.
TOP POST - no more from me below

> Roger
>
…[112 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 5)_

- **From:** Clever Monkey <clvrmnky.invalid@hotmail.com.invalid>
- **Date:** 2006-05-30T11:41:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZIZeg.24175$43.3185@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **In-Reply-To:** `<4e2tpjF1cnofiU1@individual.net>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca> <e5fn9v$iof$03$1@news.t-online.com> <4e2tpjF1cnofiU1@individual.net>`

```
Pete Dashwood wrote:
> "Roger While" <simrw@sim-basis.de> wrote in message 
> news:e5fn9v$iof$03$1@news.t-online.com...
…[9 more quoted lines elided]…
> 
I certainly meant no disrespect.  I re-read your reply carefully to make 
sure what I thought you were saying was a reasonable assumption.  I used 
pretty neutral language, and made it clear I was responding to one idea 
presented by yourself.

As for the other two paragraphs in question, well, my comments were half 
hand-waving and half long years of experience working on disparate 
systems with different APIs and different "file" semantics.  The details 
were certainly left as an exercise for the reader (myself included in 
that group).

Think of them as a jumping off point to discuss where and how these ways 
of looking at how "data" collected into "files" are the same or 
different across environments or platforms.  It can certainly be spun 
off into a thread on a more on-topic forum, if necessary.

If this is deemed rubbish, so be it.  How can I argue?
```

###### ↳ ↳ ↳ Re: EOF location?

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-29T13:59:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148936367.761691.120950@j73g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca>`

```
> A single 0x1A (control-Z in ASCII) is used to indicate EOF,

That is only true if the particular program tests specifically for that
character.  Any file can have Ctrl-Zs scattered through them and what
happens is entirely dependent on the program.

WordStar (yes I still have that) will stop reading (WS comes from
CP/M).  TYPE will also stop (it, too, comes from CP/M via MS-DOS 1).
Notepad and most other editors will read it and show a blob of some
kind - and will read all the data beyond it.

In CP/M the file size was only recorded to the nearest 128 byte record
so software filled the remainder of the last record with at least one
x'1a' and stripped that off when reading.  MS-DOS/Windows has never
needed that because it recorded the size in bytes, but because it is a
clone of CP/M it has followed that convention with some programs such
as command.com and type.

> similar to EOT in POSIX environments.

Except that EOT is 'End of Transmission' and has no effect of files.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 4)_

- **From:** Clever Monkey <clvrmnky.invalid@hotmail.com.invalid>
- **Date:** 2006-05-30T11:04:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vaZeg.24172$43.14911@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **In-Reply-To:** `<1148936367.761691.120950@j73g2000cwa.googlegroups.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca> <1148936367.761691.120950@j73g2000cwa.googlegroups.com>`

```
Richard wrote:
>> A single 0x1A (control-Z in ASCII) is used to indicate EOF,
> 
…[3 more quoted lines elided]…
> 
I carefully noted in the rest of my reply that this is an API 
convention.  I never suggested that the EOF char had to be unique, but 
the very tools that were used upthread would, in fact, never allow one 
to "see" the EOF.  They use APIs that look for it and consume it.

[...]

>> similar to EOT in POSIX environments.
> 
> Except that EOT is 'End of Transmission' and has no effect of files.
> 
Except for stdin and friends, which are files (or have file semantics) 
on POSIX systems.  Since there is no special character marking EOF on 
most POSIX systems they are not equivalent.  But the chars are used 
similarly in other regards.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-30T13:15:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149017159.131044.285910@r44g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<vaZeg.24172$43.14911@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca> <1148936367.761691.120950@j73g2000cwa.googlegroups.com> <vaZeg.24172$43.14911@nnrp.ca.mci.com!nnrp1.uunet.ca>`

```

Not so Clever Monkey wrote:

> >> A single 0x1A (control-Z in ASCII) is used to indicate EOF,
> >
…[5 more quoted lines elided]…
> convention.

You keep talking about 'API' but The DOS/Win32 API does not have that
convention, nor does POSIX.  Neither knows nor cares about Ctrl-Z in
disk files. Certain application programs may still recognize Ctrl-Z and
may or may not deal with them in any way they see fit.

The only 'convention' was with CP/M programs 30 years ago and that was
_not_ part of the 'API'.

>  I never suggested that the EOF char had to be unique, but
> the very tools that were used upthread would, in fact, never allow one
> to "see" the EOF.

Actually you never even tried a Ctrl-Z with those tools.  The example
file DID NOT HAVE A CTRL-Z in it or after it.  You merely assumed that
there was one and that the tools or the 'API' were hiding it.  Now go
back and hexedit in a couple of x'1a's and see what the tool does about
'hiding' it.

> They use APIs that look for it and consume it.

You still use 'API' as if you had a clue about it.  In DOS/Win32 'End
of File' is _not_ a character, it is the state of reading past the size
of the file.  You don't see a character for 'End of Fie' because there
isn't one, not because it 'hides' it.

It may be that some language systems, those derived from CP/M perhaps,
may treat a Ctrl-Z as an 'End of File', but as I indicated, even C
buffered input will happily read and process Ctrl-Zs in a file and will
count them.

> >> similar to EOT in POSIX environments.
> >
…[3 more quoted lines elided]…
> on POSIX systems.

No. stdin does not recognise EOT.  It is certainly true that the
console input handler does and a Ctrl-D (EOT) will create a situation
where the stdin stream has reached the size of the input.  That is the
console handler does not pass the EOT to stdin at all.

This is easy to demonstrate by creating a file on disk with embedded
Ctrl-D and Xtrl-Z and then redirecting it to stdin of cat or similar.
The program will read the Ctrl-D and Ctrl-Z and will continue to read
the rest of the characters.

You also failed miserably to demonstrate anything useful at all because
you were trying to show what DOS/Win32 would do by using Unix.  Not
that either would work the way you claim.

> Since there is no special character marking EOF on
> most POSIX systems they are not equivalent.  But the chars are used
> similarly in other regards.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 6)_

- **From:** Clever Monkey <clvrmnky.invalid@hotmail.com.invalid>
- **Date:** 2006-05-31T12:37:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GDjfg.24323$43.23049@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **In-Reply-To:** `<1149017159.131044.285910@r44g2000cwb.googlegroups.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca> <1148936367.761691.120950@j73g2000cwa.googlegroups.com> <vaZeg.24172$43.14911@nnrp.ca.mci.com!nnrp1.uunet.ca> <1149017159.131044.285910@r44g2000cwb.googlegroups.com>`

```
Richard wrote:
> Not so Clever Monkey wrote:
> 
…[15 more quoted lines elided]…
> 
I don't know what either of us are talking about anymore.  I'm not sure 
how we got on the subject of what is or is not part of an API.

I mention API mostly in reference of the Win32 API (which seemed 
appropriate, given the context under which I was responding -- remember, 
I only have Pete Dashwood's reply as the OP) and used the term only 
because I was generalizing the idea of file access, and what EOF might 
mean to any sort of code one might run into.

In order to generalize and abstract the idea of "data" being accessed 
via "files", I used the most general form of a collection of routines 
that would allow us to (among other things) inspect files -- an API.  I 
also used the word "routine" as well.  I did not want to specifically 
talk about a particular (for example) platform or library or even 
function, since how we handle such data is really up to us.

At any rate, you are correct: the common file and string handling 
routines do not care about the EOF char -- it is divorced from the 
notion of end-of-file).  I did not intend to suggest otherwise, and a 
quick test using fopen(), gets() and strlen() proves that.

However, some code, when it sees a cntrl-Z, will stop opening up the 
file.  I've seen it happen.  That's all I was driving at.  I usually 
don't even care if the cntrl-Z is there or not, since the 
APIs/functions/routines/languages/things I use tell me what they do when 
they encounter the "end of file" or not, and I can figure out the rest.

I certainly made no absolute statements about such characters, only 
general observations I've made over the years.  My last two paragraphs 
were off-hand remarks meant to convey "such characters may be present, 
but the programmer only needs to care about them if they need to care 
about them".

That all being said, I think I now understand what you might have been 
getting at.  For the question, "would an EOF char in a file count as 
part of the file for the purpose of file size?".  The answer is, almost 
certainly.

8$ print "\^Z" > outfile.txt
9$ od -ch outfile.txt
0000000000   032  \r  \n
               1A  0D  0A
0000000003
10$ ls -l outfile.txt
-rw-rw-rw-   1 user     group           3 May 31 12:14 outfile.txt
11$

I did not mean to suggest that this was not the case.  I certainly know 
that such characters can be part of any file.  Since I was answering 
that question only indirectly I focused instead on the idea that such a 
stream of characters can mean all sorts of things to different 
functions, routines, code, APIs, things.

For some reason, the following tickles me:

12$ file outfile.txt
outfile.txt:    ARC archive
13$
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-31T14:32:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149111127.219407.42390@i39g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<GDjfg.24323$43.23049@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca> <1148936367.761691.120950@j73g2000cwa.googlegroups.com> <vaZeg.24172$43.14911@nnrp.ca.mci.com!nnrp1.uunet.ca> <1149017159.131044.285910@r44g2000cwb.googlegroups.com> <GDjfg.24323$43.23049@nnrp.ca.mci.com!nnrp1.uunet.ca>`

```

Clever Monkey wrote:

> I don't know what either of us are talking about anymore.

No change there then. You certainly didn't know what you were talking
about, and you didn't know what I was talking about.

Sorry, like DD, I just couldn't resist.

> I'm not sure how we got on the subject of what is or is not part of an API.

Because you brought it up and claimed misinformation as to what was and
was not part of an 'API'.

[flannel and denial deleted]

> At any rate, you are correct: the common file and string handling
> routines do not care about the EOF char -- it is divorced from the
> notion of end-of-file).  I did not intend to suggest otherwise,

You _explicitly_ stated otherwise, repeatedly, and also about the EOT
character.

> and a quick test using fopen(), gets() and strlen() proves that.

Thank you for finally doing your homework.

> However, some code, when it sees a cntrl-Z, will stop opening up the
> file.  I've seen it happen.

That had already been pointed out, days ago, and that Heybub should
strip them out if that happens with his programs.

> I certainly made no absolute statements about such characters,

You made several absolute, and wrong, statements about such characters.

[more flannel and denial deleted]

> That all being said, I think I now understand what you might have been
> getting at.  For the question, "would an EOF char in a file count as
> part of the file for the purpose of file size?".  The answer is, almost
> certainly.

Which is 100% reversal from your prior claim that it was present but
not counted.

> I did not mean to suggest that this was not the case.

You explicitly stated that this was not the case.

I would suggest that in your place of work you never 'lose' an
argument. Everyone wanders off before you will ever agree you were
wrong. When they later show you were wrong you probably, as here, deny
that was what you said, as here.

Don't argue in writing, it makes it too easy to check back.
```

###### ↳ ↳ ↳ Re: EOF location?

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-29T15:47:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1148942828.967788.305650@j73g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca>`

```

Not such a Clever Monkey wrote:

> What happens if we have two lines in a text file on some sort of
> DOS/Win32 machines:
>

> 17$ cat testfile.txt
> 18$ od -hc testfile.txt
> 19$ wc testfile.txt
> 20$ ls -l testfile.txt

That is hardly "some sort of DOS/Win32", it might be cygwin.

> (Win32 is pretty relaxed, in that the last CRLF pair can
> actually be omitted. In this case we have a "normalized" file).

'Win32' neither knows nor cares about any CR/LF especially whether
there is one at the end of the file.  There is no such thing as a
'normalized file', though there is a 'normalized file path' which is
quite a different thing.

> Each
> line is 11 characters long; 9 characters and two line-end characters.
> Note also that the size in bytes is the same as the character count.

Well duhhh.

> I assume it would depend on the file APIs in question, but it is typical
> for routines to return lengths that include all the characters,
> including the CRLF pair.

There are no Operating system disk file APIs in DOS or Windows that
care about the CR/LF nor any that give a length that notices whether
there are CR/LF or not.

It is up to each language implementation or application to deal with
whatever it wishes to do with any particualr characters in the file.

> The EOF/EOT marker is "present", but is
> usually used up by API calls that scan for it while retrieving the
> contents of a file.

No. Wrong. There is no requirement for an EOF to be present, it is
indicated entirely by the file size.  EOT is not used in files as any
sort of ending of the file.

> This implies that those routines that count characters will ignore the
> EOF.  Indeed, those routines will likely stop whatever they are doing
> immediately once they encounter the EOF and return with whatever they
> got so far.

That may or may not be true depending entirely on the routine itself.
It is not something that is 'likely', some will always do so, some will
never do so.  Some may even have an option.

>  Applications that use the usual APIs to get at the contents
> of text files will normally never count or show the trailing EOF.

DOS/Win32 have no disk file APIs that will ever notice a Ctrl-Z nor
care about it. If the file is full of EOF (Ctrl-Z) characters then dir
will show how many there are.

Whether a particular language implementation does this or not depends
on the author. For example I just did a small C program that read a
text file (fopen, getc) and counted the total characters and the x'1a'
characters of a file that had several. It counted the whole file size
and 12 x'1a' characters.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-31T01:10:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4e2uirF1alg2bU1@individual.net>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca> <1148942828.967788.305650@j73g2000cwa.googlegroups.com>`

```
Thanks for that Richard.

I think I see what Roger was getting at now.

Please correct me if the following summary is wrong:

1. The file size is all that matters as far as Windows is concerned.

2. Any control characters used by applications are placed entirely at the 
risk of those applications, without any guarantee that anything OTHER than 
the application will even notice them.

I realised this when I wrote some apps using byte stream IO a while back. 
But I'd never really explored it or verbalized it.

In the COBOL environment, dealing with LINE SEQUENTIAL files in the Fujitsu 
environment (remember the start of this conversation :-)?), you come to 
expect a CR/LF at the end of each record (I understand Unix only uses one of 
these, but I don't know, as I don't use Unix environments...), and I think 
we have established that there may or may not be a Ctrl/Z.

I am probably no wiser than I was before, but between you, you and Roger 
have ensured that I am certainly better informed :-)

Poor old HeyBub on the other hand is not much further ahead...

Pete.


"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1148942828.967788.305650@j73g2000cwa.googlegroups.com...
>
> Not such a Clever Monkey wrote:
…[66 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 4)_

- **From:** Clever Monkey <clvrmnky.invalid@hotmail.com.invalid>
- **Date:** 2006-05-30T11:30:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%xZeg.24174$43.3506@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **In-Reply-To:** `<1148942828.967788.305650@j73g2000cwa.googlegroups.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca> <1148942828.967788.305650@j73g2000cwa.googlegroups.com>`

```
Richard wrote:
> Not such a Clever Monkey wrote:
> 
…[10 more quoted lines elided]…
> 
It might, but it is not.  I was making the point that I was on a Win32 
machine with POSIX utilities that allow us to inspect files.  There are 
several ways to do this.  Just trying to be clear, here.  (By the way, 
even if I was running cygwin, I would consider this simply a programming 
environment and set of libraries running on "some sort of" Win32/DOS.)

I use the exact same POSIX utils (exact, as in from the same vendor) on 
the 390, as well.  This has been a life-saver in the past!

>> (Win32 is pretty relaxed, in that the last CRLF pair can
>> actually be omitted. In this case we have a "normalized" file).
…[5 more quoted lines elided]…
> 
What I said.  This was just an aside.  I used scare quotes around the 
word for a reason.  The fact is that POSIX utilities *must* right out 
lines that end in the right EOL char(s).  The OS imposes no requirements.

>> Each
>> line is 11 characters long; 9 characters and two line-end characters.
…[3 more quoted lines elided]…
> 
I was replying in the same spirit of the OP (or the closest thing to an 
OP that my node is willing to give me) of "showing your work".

>> I assume it would depend on the file APIs in question, but it is typical
>> for routines to return lengths that include all the characters,
…[5 more quoted lines elided]…
> 
Ok.  I never implied otherwise.  Some file APIs are able to return 
lines.  They will return lines that include any line ends that are 
present, even if there are no line ends.

I was speaking to Pete's description of EOL char(s) and EOF on DOS-like 
systems.  This is the only reason I mention line ends at all.

> It is up to each language implementation or application to deal with
> whatever it wishes to do with any particualr characters in the file.
> 
Again, I did mention that my current example was anything more than an 
example, and I did make plenty of caveats.  I was speaking to Pete's 
comment regarding EOF/EOL chars only.  The other stuff was just background.

Thank you for expanding upon my comments, however.

>> The EOF/EOT marker is "present", but is
>> usually used up by API calls that scan for it while retrieving the
…[5 more quoted lines elided]…
> 
Not true.  Under some circumstances using these APIs to cycle through a 
text file until you get "EOF" will fail when confronted with a file that 
contains embedded EOF chars.  It's a rare enough but common problem.

Actually, one of the responses to my reply described such a problem.

*shrug*  I've seen it happen enough times, so I have actual experience 
with the problem.

>> This implies that those routines that count characters will ignore the
>> EOF.  Indeed, those routines will likely stop whatever they are doing
…[6 more quoted lines elided]…
> 
Agreed.  This is something I took the time to make clear.  My use of 
likely is meant to cover the cases where one routine, function or API 
works in one way, and another works quite different.  That is, I did not 
intend the meaning to be "a function, routine or API may or may not 
handling EOF chars reliably depending on how it feels".

>>  Applications that use the usual APIs to get at the contents
>> of text files will normally never count or show the trailing EOF.
…[4 more quoted lines elided]…
> 
I haven't used actual DOS in years, but I'm unclear on how "dir" would 
do this.

> Whether a particular language implementation does this or not depends
> on the author. For example I just did a small C program that read a
…[3 more quoted lines elided]…
> 
I agree this is a convention, and I am pretty POSIX oriented in this 
regard.  I understand you can make a program to actually read in such 
chars.  It is pretty common on Win32/DOS to refer to such files or file 
access as "binary" (not necessarily binary used in the sense of libc 
APIs that work with FILEs, but similar).

However, since we were talking about the notion of line ends I kept my 
discussion pretty much about so-called text files, where both EOL and 
EOF can matter quite a bit.

But your comments regarding the fact that it is the programmer or 
implementer that defines what these characters mean is well-taken and 
appreciated.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-30T13:12:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149019949.506175.271020@y43g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<%xZeg.24174$43.3506@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca> <1148942828.967788.305650@j73g2000cwa.googlegroups.com> <%xZeg.24174$43.3506@nnrp.ca.mci.com!nnrp1.uunet.ca>`

```

Clever Monkey wrote:

> It might, but it is not.  I was making the point that I was on a Win32
> machine with POSIX utilities that allow us to inspect files.

There are many utilities that 'allow us to inspect files'. Using ones
that will use Win32 semantics may show Win32 features rather than POSIX
features.  But in fact neither will show us what you claimed for EOF.

> There are
> several ways to do this.  Just trying to be clear, here.  (By the way,
> even if I was running cygwin, I would consider this simply a programming
> environment and set of libraries running on "some sort of" Win32/DOS.)

Exactly, a POSIX/Unix environment, not a Win32/DOS one.

> >> Each
> >> line is 11 characters long; 9 characters and two line-end characters.
…[5 more quoted lines elided]…
> OP that my node is willing to give me) of "showing your work".

Unfortunately your 'work' was lacking:

"""The EOF/EOT marker is "present", but is
usually used up by API calls that scan for it while retrieving the
contents of a file."""

You assumed that there was a EOF (x'1a') character but it wasn't
showing because:

"""This implies that those routines that count characters will ignore
the
EOF.  Indeed, those routines will likely stop whatever they are doing
immediately once they encounter the EOF and return with whatever they
got so far.  Applications that use the usual APIs to get at the
contents
of text files will normally never count or show the trailing EOF. """

You never tried a file with hex characters in them other than CR/LF so
you came to an invalid conclusion.

> Ok.  I never implied otherwise.  Some file APIs are able to return
> lines.  They will return lines that include any line ends that are
> present, even if there are no line ends.

You are confusing 'API's with library functions. There are _no_ Win32
disk APIs that return 'lines' with or without line terminators.

> The other stuff was just background.

It is the 'other stuff' that is complete nonsense.

> Not true.  Under some circumstances using these APIs to cycle through a
> text file until you get "EOF" will fail when confronted with a file that
> contains embedded EOF chars.

Which 'API's ?  Programs may test for characters and stop on certain
ones, but the Win32 'API' will never stop on an embedded x'1A'.  Nor
will POSIX.

> It's a rare enough but common problem.

'Rare but common'.  wonderful.

> > DOS/Win32 have no disk file APIs that will ever notice a Ctrl-Z nor
> > care about it. If the file is full of EOF (Ctrl-Z) characters then dir
…[3 more quoted lines elided]…
> do this.

DIR reports the size of the file, it does not inspect the contents.
You should not that I said 'full of Ctrl-Z's.  Try it, try learning
something rather than repeating half-learnt nonsense.

> I agree this is a convention, and I am pretty POSIX oriented in this
> regard.  I understand you can make a program to actually read in such
> chars.

You can in POSIX/Unix/Linux too.  Write a C program using fopen/fgetc
on a file of random hex characters and see that it will read to the
size of the file.

>  It is pretty common on Win32/DOS to refer to such files or file
> access as "binary" (not necessarily binary used in the sense of libc
> APIs that work with FILEs, but similar).

No 'binary', just fopen(..., "r") and fgetc() and you will see
characters in the file that are 0x1A, and the characters beyond.

Don't you ever try this stuff before you post it ? I do. Then _I_ know
what I am talking about.

> However, since we were talking about the notion of line ends I kept my
> discussion pretty much about so-called text files, where both EOL and
> EOF can matter quite a bit.
 
You just don't listen do you.
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 6)_

- **From:** Clever Monkey <clvrmnky.invalid@hotmail.com.invalid>
- **Date:** 2006-05-31T13:04:26-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u0kfg.24333$43.13863@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **In-Reply-To:** `<1149019949.506175.271020@y43g2000cwc.googlegroups.com>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca> <1148942828.967788.305650@j73g2000cwa.googlegroups.com> <%xZeg.24174$43.3506@nnrp.ca.mci.com!nnrp1.uunet.ca> <1149019949.506175.271020@y43g2000cwc.googlegroups.com>`

```
Richard wrote:
> Clever Monkey wrote:
> 
…[6 more quoted lines elided]…
> 
I'm no longer sure what I've supposed to have claimed.  [Though see my 
comments below, and my reply elsewhere, as I think this horse is well 
and truly dead.]

>> There are
>> several ways to do this.  Just trying to be clear, here.  (By the way,
…[4 more quoted lines elided]…
> 
Right, except with 100% Win32/DOS file semantics.  About the only thing 
different to me is that I can work in a Bash shell instead of a cmd.exe 
shell.  Technically this is not acceptable as a POSIX environment, as a 
fair bit more of the OS would have to change (I've been involved, 
obliquely, with work to make Win32 truly POSIX).  Win32 (well, I guess 
NT 4 and 5) cannot be called, referred to, or presented as a POSIX or 
Unix environment without a fair amount of changes to the OS.

It's just an XP box with some payware tools installed so I can have a 
real shell and convenient tools.

For the purposes of talking about EOL chars (my only intent in this 
thread, really) this seemed appropriate.  I don't want to go off in 
several directions discussing what is or is not Win32.  To me this is 
arguing the Buddha nature; fun in its own way but not germane to the 
current conversation.  Suffice it to say that I am on a plain Win32 
development system, only with a subset of POSIX tools running as an 
application that use the regular Win32 APIs to get work done (and parts 
of a custom libc supplied from the days when Windows had no real C library).

>>>> Each
>>>> line is 11 characters long; 9 characters and two line-end characters.
…[7 more quoted lines elided]…
> 
Well, surely not for the part of my reply directed to Pete.  Remember 
that the "work" we are talking about here is related to the EOL 
discussion.  It is, as far as I know, quite accurate and clear.

Honest, teacher, I did *most* of my homework!  Unfortunately, I made the 
mistake of tagging on a few sentences at the end that I did not 
fact-check to the limit required by USENET.  Mea maxima culpa.

Which leads us to...

> """The EOF/EOT marker is "present", but is
> usually used up by API calls that scan for it while retrieving the
> contents of a file."""
> 
A-ha!  I now know what you are taking so much umbrage with!  All that 
essentially unrelated stuff about POSIX and showing your work leads us 
to this.  I can't recall if you actually quoted this previously and it 
got lost in the noise.

Yes, this was an untrue statement.  I was conflating the notion of 
"end-of-file" as referenced in various APIs with the EOF character on a 
specific platform.  I assumed such characters were still necessary on 
Win32.  My misunderstanding was compounded by having to work on code 
(not ours!) that stopped because it reached an EOF char in a file, and 
decided it was time to stop.

A short test in C cleared this up.  I suppose if I had done this in my 
original reply all this back and forth could have been avoided.

[Rest snipped for "brevity".]
```

###### ↳ ↳ ↳ Re: EOF location?

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-05-31T14:16:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1149110193.016628.242460@j55g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<u0kfg.24333$43.13863@nnrp.ca.mci.com!nnrp1.uunet.ca>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca> <1148942828.967788.305650@j73g2000cwa.googlegroups.com> <%xZeg.24174$43.3506@nnrp.ca.mci.com!nnrp1.uunet.ca> <1149019949.506175.271020@y43g2000cwc.googlegroups.com> <u0kfg.24333$43.13863@nnrp.ca.mci.com!nnrp1.uunet.ca>`

```

Slightly Clever Monkey wrote:

> I'm no longer sure what I've supposed to have claimed.

The messages are on Google and elsewhere and will be forever. You could
easily go back and check what you did claim and where it was pointed
out to be misinformation.  You now seem to want to disassociate
yourself from that with flannel such as: "supposed to have".

>  It is, as far as I know, quite accurate and clear.

You got one sentence right and the rest was nonsense and
misinformation.

> > """The EOF/EOT marker is "present", but is
> > usually used up by API calls that scan for it while retrieving the
…[5 more quoted lines elided]…
> got lost in the noise.

It is easy to check that I had quoted this previously, just look back
in the thread about 4 messages.  Previously, my corrections of your
misinformed claims had gotten a denial 'Not true', and showed that you
didn't understand the correction.

> Yes, this was an untrue statement.  I was conflating the notion of
> "end-of-file" as referenced in various APIs with the EOF character on a
…[3 more quoted lines elided]…
> decided it was time to stop.

Thank you for finally agreeing, now that you have done your homework,
with what you have been disputing for days.
```

###### ↳ ↳ ↳ Re: EOF location?

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-05-31T00:48:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4e2t8nF1ct3vqU1@individual.net>`
- **References:** `<127hfdman9s836f@news.supernews.com> <4dsr45F1bi54rU1@individual.net> <YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca>`

```
Good Post.

Thanks.

Pete.

"Clever Monkey" <clvrmnky.invalid@hotmail.com.invalid> wrote in message 
news:YXHeg.24087$43.23700@nnrp.ca.mci.com!nnrp1.uunet.ca...
> Pete Dashwood wrote:
>> "HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
…[103 more quoted lines elided]…
> text files will normally never count or show the trailing EOF.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
