[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus COBOL OPEN (DOS) duration

_14 messages · 10 participants · 2006-07 → 2006-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus COBOL OPEN (DOS) duration

- **From:** "Alan" <alan.with.an.eh@gmail.com>
- **Date:** 2006-07-20T06:46:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com>`

```
Anyone have any information about the duration of a Cobol OPEN duration
on a relative indexed DOS file?

This is an odd symptom as I'm creating/running utility programs to
archive old data, I'm encountering files that error out with a 4/1..An
open has been attempted on a file already open...but the files I'm
preparing for archive so these are data files that have not been
touched in almost 10 years.

I would have thought that a system reboot would eventually clear out
these open file flags. Mind you these are relative indexed files, not
sequential or other indexed files.

Does this make sense or should I be investigating something else
opening these files? It really doesn't make sense that the files would
be touched by any other program. They definitely aren't flagged before
I run my utlity and show no signs of use. Strange...

Alan.
```

#### ↳ Re: Microfocus COBOL OPEN (DOS) duration

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-20T14:03:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3Mvg.17167$js3.16749@fe04.news.easynews.com>`
- **References:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com>`

```
Just for clarification (and I don't know the answer), do you mean these are 
RELATIVE files?  I don't know what a "relative indexed" file would be.
```

##### ↳ ↳ Re: Microfocus COBOL OPEN (DOS) duration

- **From:** "Alan" <alan.with.an.eh@gmail.com>
- **Date:** 2006-07-20T07:08:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153404495.806648.31490@h48g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<e3Mvg.17167$js3.16749@fe04.news.easynews.com>`
- **References:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com> <e3Mvg.17167$js3.16749@fe04.news.easynews.com>`

```
Sorry Bill...they're RELATIVE files.

Environmental habit.

Thanks. : )

Alan.
```

#### ↳ Re: Microfocus COBOL OPEN (DOS) duration

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-07-20T12:45:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12bvg9sdag8581a@news.supernews.com>`
- **References:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com>`

```
Alan wrote:
> Anyone have any information about the duration of a Cobol OPEN
> duration on a relative indexed DOS file?
…[14 more quoted lines elided]…
> I run my utlity and show no signs of use. Strange...

Your supposition is correct. What happens if your utility ignores the "41" 
and attempts a read?
```

#### ↳ Re: Microfocus COBOL OPEN (DOS) duration

- **From:** ozzy.kopec@gmail.com
- **Date:** 2006-07-20T11:18:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153419514.778121.99850@i3g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com>`
- **References:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com>`

```

Alan wrote:
> Anyone have any information about the duration of a Cobol OPEN duration
> on a relative indexed DOS file?
…[6 more quoted lines elided]…
>
If I have time I could try a quicky at home (DOS MFCOBOL) and
experiment on opening an open file or such for access is realtive
files.

You're not using the *extended* file status codes are you?   I think a
041 is corrupt index, where the standard 2 byte FS 41 =  "open on open"
like you said.

try closing it first?

Snip of the code??
```

#### ↳ Re: Microfocus COBOL OPEN (DOS) duration

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-07-20T12:17:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153423079.482179.87850@m79g2000cwm.googlegroups.com>`
- **In-Reply-To:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com>`
- **References:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com>`

```

Alan wrote:

> This is an odd symptom as I'm creating/running utility programs to
> archive old data, I'm encountering files that error out with a 4/1..An
> open has been attempted on a file already open...but the files I'm
> preparing for archive so these are data files that have not been
> touched in almost 10 years.

A file 'already open' is within the same run unit. You will only get
that error if the program opens the file and then executes an open for
the file without an intervening close.

It will not be beacause another program had opened the file - that
would just happen without error if sharing is on or will give a file
lock error 9A.

If will not be because the file had been opened in the past and not
closed.  MF does not detect that, or at least there is no status for
it.

Check your program logic, you may be looping back to the open instead
of the read, or the open of another file, say the 'archive' file, may
have the same name.

A 9/041, which is corrupt file index, cannot occur on a relative file,
please post the select assign. If you have specified a relative file as
an indexed file then the index will be 'missing'.
```

##### ↳ ↳ Re: Microfocus COBOL OPEN (DOS) duration

- **From:** "Alan" <alan.with.an.eh@gmail.com>
- **Date:** 2006-07-20T13:46:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153428395.084800.276730@75g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1153423079.482179.87850@m79g2000cwm.googlegroups.com>`
- **References:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com> <1153423079.482179.87850@m79g2000cwm.googlegroups.com>`

```
Ohhh...how I knew you were going to mention about the loop back to open
the file again. : )

That's why I was asking about this "long-term" open on the files...To
fix this (it makes me laugh because I read dailywtf.com diligently) I
have a check on the status to see if the error comes back a 4/1 : file
open on an open (ANSI'85). Well occasionally the file errors out on the
open so I issue a close and go back to the file open routine label
because either 2 things are gonna happen...either the file will close
or the thing won't close and go into a loop..but it has to close and
falls through quite nicely to open the file properly.

I wrote a check routine now to write a log of all the closes I have to
do. The lists are huge and inconsistent with an extract that is
required (hence 1 open/file) on every file...Sort of why I had to ask
if anyone's seen this.

Thanks for the feedback though,
Alan
```

###### ↳ ↳ ↳ Re: Microfocus COBOL OPEN (DOS) duration

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-07-20T15:41:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153435297.907410.52600@i42g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1153428395.084800.276730@75g2000cwc.googlegroups.com>`
- **References:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com> <1153423079.482179.87850@m79g2000cwm.googlegroups.com> <1153428395.084800.276730@75g2000cwc.googlegroups.com>`

```

Alan wrote:
> Ohhh...how I knew you were going to mention about the loop back to open
> the file again. : )
>
> That's why I was asking about this "long-term" open on the files...

There is no 'long term' open on a file.  If the file is opened in
shared mode then it does not care if another process has it open even
if that process is still running or died some horrible death yonks ago.
 The '4/1' error is explicitly and specifically an error in the current
run-unit.  If there was a file lock caused by a different run-unit you
would get a '9A' error in Microfocus.

A 'run-unit', however, is all the programs that call each other in one
process.  So if the program you are referring to has been called by a
program that has the file open then you will get a '41' error. Or if
the main program called one program that opened the file and did not
close it but did an exit program then your program was called it would
get a '41' on trying to open.

> To
> fix this (it makes me laugh because I read dailywtf.com diligently) I
…[5 more quoted lines elided]…
> falls through quite nicely to open the file properly.

Are you testing for 'success' by checking the file staus for '00' ?

There are success codes that not '00', you should only check the first
byte for '0' to indicate that the file opened correctly.

> I wrote a check routine now to write a log of all the closes I have to
> do. The lists are huge and inconsistent with an extract that is
> required (hence 1 open/file) on every file...Sort of why I had to ask
> if anyone's seen this.

It is most likely a programmer error causing this.
```

###### ↳ ↳ ↳ Re: Microfocus COBOL OPEN (DOS) duration

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-07-20T22:48:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2LTvg.213932$Mn5.207446@pd7tw3no>`
- **In-Reply-To:** `<1153428395.084800.276730@75g2000cwc.googlegroups.com>`
- **References:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com> <1153423079.482179.87850@m79g2000cwm.googlegroups.com> <1153428395.084800.276730@75g2000cwc.googlegroups.com>`

```
Alan wrote:
> Ohhh...how I knew you were going to mention about the loop back to open
> the file again. : )
…[17 more quoted lines elided]…
> 

All the above reads like pidgin-English. Post the source that is causing 
problems plus any copyfiles - then you should get a straight answer.

The DOS version of the Animator should help - it will show a file-status 
code (using the Animator Examine and hopefully whether the file is 
currently open(in which mode) or closed), BEFORE you step to the code to 
OPEN any file. Doesn't make sense that you are trying to build a log to 
trap errors.

It's belt and braces, but as I keep my file access in separate 
classes(programs) per file using OO, I do the following - bearing in 
mind this is for each separate file.

01 FileFlag		pic 9 value 0.
    88 FileOpened	value 1.
    88 FileClosed	value 0.

.............

Open Myfile

if file-status = "00"  *> (or whatever other "0?" values are acceptable)
    set FileOpened to true

else........ report error
end-if

and when it comes to CLOSing :-

If FileOpened
    close MyFile

	if file-status = "00"
    	set FileClosed to true

	else ..... report error
	End-if
End-if

Above is not a requirement - but leaves me peaceful...... (Weird 
perhaps, but it does ensure that I don't accidentally attempt to close a 
*closed* file twice).

Look at the recent thread,  "Re: scrittura di record su file .dat". I 
posted an OO version of M/F file-status codes. You can adapt it from a 
class to a program by PERFORMING PARAGRAPHS rather than my INVOKES. To 
display your error messages in detail under DOS use a standard message 
format in the SCREEN-SECTION.

Jimmy
```

###### ↳ ↳ ↳ Re: Microfocus COBOL OPEN (DOS) duration

_(reply depth: 4)_

- **From:** "Alan" <alan.with.an.eh@gmail.com>
- **Date:** 2006-07-21T07:02:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153490546.237746.300760@h48g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<2LTvg.213932$Mn5.207446@pd7tw3no>`
- **References:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com> <1153423079.482179.87850@m79g2000cwm.googlegroups.com> <1153428395.084800.276730@75g2000cwc.googlegroups.com> <2LTvg.213932$Mn5.207446@pd7tw3no>`

```
Thanks all...

I don't want to start posting code.I know where you're going though.
Thanks for the idea for the status test and thanks for the confirmation
that there is no (albeit absurd I know) "long term" on the file open.

When it comes to hammering the nail in the board, sometimes there's no
time to waste for the reason why there's already a nail there to start
hammering to begin with...just hammer it in.

Hope Cow Town's nice these days...lot's of good friends out there.

Alan
```

###### ↳ ↳ ↳ Re: Microfocus COBOL OPEN (DOS) duration

_(reply depth: 5)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-07-21T10:19:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1153502387.163792.156760@s13g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1153490546.237746.300760@h48g2000cwc.googlegroups.com>`
- **References:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com> <1153423079.482179.87850@m79g2000cwm.googlegroups.com> <1153428395.084800.276730@75g2000cwc.googlegroups.com> <2LTvg.213932$Mn5.207446@pd7tw3no> <1153490546.237746.300760@h48g2000cwc.googlegroups.com>`

```

Alan wrote:
> Thanks all...
>
…[4 more quoted lines elided]…
> Alan

Sounds like you would be a match for our very own Doc Dwarf.

Hang with us.
```

###### ↳ ↳ ↳ Re: Microfocus COBOL OPEN (DOS) duration

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2006-07-22T12:22:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CMowg.70989$Lm5.65267@newssvr12.news.prodigy.com>`
- **References:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com> <1153423079.482179.87850@m79g2000cwm.googlegroups.com> <1153428395.084800.276730@75g2000cwc.googlegroups.com>`

```
"Alan" <alan.with.an.eh@gmail.com> wrote in message
news:1153428395.084800.276730@75g2000cwc.googlegroups.com...
>
> I wrote a check routine now to write a log of all the closes I have to
> do. The lists are huge and inconsistent with an extract that is
> required (hence 1 open/file) on every file...Sort of why I had to ask
> if anyone's seen this.

Seen it? Heck, I have fifty-two cents says at least 90% of those here have
DONE it at one time or another.

Sorry, but as you've learned from others, "file already open" errors are
.... yes.... programmer errors. The only way it can happen is if the run
unit does unmatched OPEN/CLOSE pairs.

MCM
```

###### ↳ ↳ ↳ Re: Microfocus COBOL OPEN (DOS) duration

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-07-23T01:08:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4iema8F3f2kuU1@individual.net>`
- **References:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com> <1153423079.482179.87850@m79g2000cwm.googlegroups.com> <1153428395.084800.276730@75g2000cwc.googlegroups.com> <CMowg.70989$Lm5.65267@newssvr12.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message 
news:CMowg.70989$Lm5.65267@newssvr12.news.prodigy.com...
> "Alan" <alan.with.an.eh@gmail.com> wrote in message
> news:1153428395.084800.276730@75g2000cwc.googlegroups.com...
…[14 more quoted lines elided]…
>
Whilst I have extreme reservations about ever using the phrase ' the only 
way', I have to agree with Michael that I know of no other way in which you 
could be getting the message that you are.

Pete.
```

#### ↳ Re: Microfocus COBOL OPEN (DOS) duration

- **From:** Paul Robinson <paul@paul-robinson.us>
- **Date:** 2006-09-06T12:51:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44fefc8d$0$25777$815e3792@news.qwest.net>`
- **In-Reply-To:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com>`
- **References:** `<1153403183.166173.292900@s13g2000cwa.googlegroups.com>`

```
Alan wrote:

> Anyone have any information about the duration of a Cobol OPEN duration
> on a relative indexed DOS file?
…[3 more quoted lines elided]…
> open has been attempted on a file already open...

As other people will tell you, you can only get an "open on a file 
already open" if the *same* program is opening the same file twice 
without closing it in between opens.  Any other open by a separate 
program would get you a "sharing violation", not the error you name.

When I say "the same program" I mean the same running image; a second 
copy of the identical program running on the same machine is a separate 
  process, in effect, a different program, and would not trigger an 
"open on a file already open" error.

When a COBOL program exits - by a stop run, a program crash, a 
force-terminate because of an operating system proper shutdown, or a 
program "vaporization" because of an immediate reboot or machine turn 
off - all files are closed, automatically and by force if a running 
program failed to close the file.  If all programs that opened that file 
were only reading it, no effects will occur.  If any program that opened 
that file was writing to it, either the last write succeeded or it did 
not (if the buffers were not flushed before the program quit or was 
removed).

A reboot of a machine is equivalent to a no-warning force-terminate 
("vaporization") of all running programs.  Any files they have open are 
closed, any buffers they have in memory are lost, as well as any writes 
to those buffers that have not been committed to disk or other media.

Once a machine restarts, except for any automatically started programs 
that might use some file, all files on a system are in a closed state, 
any prior opens will not be of any significance, thus only opens that 
occur during that session will have any effect.

Now, if the system did not shut down properly the directory system may 
be in shambles if system tables were not properly committed, but the 
file itself will still be closed.  You may or may not have lost data 
from any writes in progress, but the file will no longer be open.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
