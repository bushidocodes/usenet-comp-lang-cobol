[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Read (no 'into') write (no 'from')

_9 messages · 9 participants · 1998-04_

---

### Read (no 'into') write (no 'from')

- **From:** "m..." <ua-author-468112@usenetarchives.gap>
- **Date:** 1998-04-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6grrt0$3kn$1@camel15.mindspring.com>`

```

Hi,

I wonder if anybody had problems with doing the following:

fd file-1
...
01 rec-1

fd out-file-1
....
01 out-rec-1

read file-1
make modifications to data
move rec-1 to out-rec-1
write out-rec-1

In my installation, a programmer maintains that Cobol has a problem
with it, and one should use a working-storage record as an
intermediate.
```

#### ↳ Re: Read (no 'into') write (no 'from')

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-11T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ed5ceac33d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6grrt0$3kn$1@camel15.mindspring.com>`
- **References:** `<6grrt0$3kn$1@camel15.mindspring.com>`

```


Moshe Rybak wrote in message <6grrt0$3kn$1.··.@cam··g.com>...
› Hi,
› 
…[19 more quoted lines elided]…
› 

I think that the most common problem with placing your fields under the FD
rather than using READ INTO and WRITE FROM with WS items has to do with
PERFORM UNTIL loops. Often, programs use something like

AT END Move "low-values" to full-record

However, if that "full-record" is under the FD and not in working-Storage,
you can (and with many but not all compilers WILL) get errors when trying to
access fields in the FD before the 1st read or after the last read (or
write). If you use "flag" fields in working-storage and never try to
access the fields under your FD when they are "officially" available, then
you shouldn't have any problem. My experience (and this may be more
tradition than requirement) is that MOST COBOL programs do use the READ INTO
and WRITE FROM formats.
```

#### ↳ Re: Read (no 'into') write (no 'from')

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-04-12T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ed5ceac33d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6grrt0$3kn$1@camel15.mindspring.com>`
- **References:** `<6grrt0$3kn$1@camel15.mindspring.com>`

```


Moshe Rybak wrote in message <6grrt0$3kn$1.··.@cam··g.com>...
› In my installation, a programmer maintains that Cobol has a problem
› with it, and one should use a working-storage record as an
› intermediate.


I think the problem with the programmer, not the language. My
dad use to say, fifty year ago, a poor workman always blames
his tools. Nothing changes.
```

#### ↳ Re: Read (no 'into') write (no 'from')

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1998-04-12T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ed5ceac33d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6grrt0$3kn$1@camel15.mindspring.com>`
- **References:** `<6grrt0$3kn$1@camel15.mindspring.com>`

```

In article <6grrt0$3kn$1.··.@cam··g.com>, m.··.@pip··e.com (Moshe
Rybak) writes:

› In my installation, a programmer maintains that Cobol has a problem
› with it, and one should use a working-storage record as an
› intermediate.

I would normally discourage direct manipulation of the input record. Before the
first READ or after reaching EOF, the input record area is indeterminate, that
is, moving a value to that area may corrupt memory, may cause a data protection
or operation exception, or may work. If you are using tricks like moving HIGH
VALUES or ALL '9' to a field upon EOF, this should be in a working storage
area, not a file area. Some compilers may have ways of making the record area
quite determinate (e.g., SAME AREA clause), but that could become a maintenance
nightmare.

There should be no problem directly manipulating the output record area while
the file is open.

I tend to prefer doing manipulations in working storage so that if, for some
reason, I get a formatted dump, I can see what the exact records looked like,
as well as the values of the areas I was manipulating. In many cases the exact,
unretouched, input record contents give valuable clues on what went wrong.
```

#### ↳ Re: Read (no 'into') write (no 'from')

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-04-12T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ed5ceac33d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6grrt0$3kn$1@camel15.mindspring.com>`
- **References:** `<6grrt0$3kn$1@camel15.mindspring.com>`

```

In article <6grrt0$3kn$1.··.@cam··g.com>,
Moshe Rybak wrote:
› Hi,
› 
…[17 more quoted lines elided]…
› intermediate.

Aahhhhh, yes... this programmer is the beneficiary of the Ancient Wisdom
which states:

'Thou Shalt Not Perform Arithmetic Manipulations in File Buffers'

You may ask 'why?'... the answer I was given was that at times one gets
Upredictable Results. I will admit to sloppiness on my part and I have
not run this Wisdom through rigorous testing; as this advice was given by
my first programming instructor I've been adhering thereunto ever since.
*Always* READ INTO and WRITE FROM and you will not incur Greater
Troubles... do otherwise at your own risk.

DD
```

#### ↳ Re: Read (no 'into') write (no 'from')

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1998-04-12T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ed5ceac33d-p6@usenetarchives.gap>`
- **In-Reply-To:** `<6grrt0$3kn$1@camel15.mindspring.com>`
- **References:** `<6grrt0$3kn$1@camel15.mindspring.com>`

```

Moshe Rybak wrote:
› 
› Hi,
…[18 more quoted lines elided]…
› intermediate.

In my experience (IBM mainframe COBOL) it should work fine.

20 years ago I was taught that it was good programming practice to read
into working-storage and write from working-storage because it was more
easy to locate the working-storage copy of the record in a core dump.
The buffers defined under the FD are owned by the operating system, and
may be located far away from your program.

Modern dump analysis tools will probably locate and print the buffer
areas anyway, so the old advice may not be valid anymore. There was
quite a debate here a few months ago as to what would be in the FD
buffers if you read past the end of file (would the last record still be
there?) or if you wrote a record (would the last record written still be
in the FD Buffer?). I can't remember if the controversy was resolved.

I still read INTO and write FROM (except for variable length records
where it may not be allowed), but that's primarily from habit.

I hope that helps.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
"Y2K? Because Centuries Happen!"
Time Machine reports at http://home.att.net/~arnold.trembley
```

##### ↳ ↳ Re: Read (no 'into') write (no 'from')

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-04-11T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ed5ceac33d-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ed5ceac33d-p6@usenetarchives.gap>`
- **References:** `<6grrt0$3kn$1@camel15.mindspring.com> <gap-ed5ceac33d-p6@usenetarchives.gap>`

```

Arnold Trembley wrote:
› 
› Moshe Rybak wrote:
…[8 more quoted lines elided]…
›› intermediate.
 
› Modern dump analysis tools will probably locate and print the buffer
› areas anyway, so the old advice may not be valid anymore.  There was
…[3 more quoted lines elided]…
› in the FD Buffer?).  I can't remember if the controversy was resolved.

The code presented should work fine. If you CLOSE the input file, the
record area may go away. If you do a READ and get an (invalid key or at
end) error conditionm the record area almost certainly will be lost.

The previous debate here involved the status of a record area after
WRITEing to the file. In general, assume that the data area is lost
after a WRITE.
I  |\   Randall Bart
L  |/   mailto:Bar··.@usa··m.net    Bar··.@wor··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \  Cancer victim/Medical Marijuana activist Todd McCormick jailed
e    |\ for using Marinol w/ prescription: http://www.freecannabis.org
Y    |/        http://marijuanamagazine.com/toc/articles/toddheld.html
o    |\ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00  
u    |/ Is it easy yet?:http://members.aol.com/PanicYr00/Sequence.html
```

##### ↳ ↳ Re: Read (no 'into') write (no 'from')

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-04-12T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ed5ceac33d-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ed5ceac33d-p6@usenetarchives.gap>`
- **References:** `<6grrt0$3kn$1@camel15.mindspring.com> <gap-ed5ceac33d-p6@usenetarchives.gap>`

```

Arnold Trembley wrote:

› I still read INTO and write FROM (except for variable length records
› where it may not be allowed), but that's primarily from habit.
›
› I hope that helps.

Another thing to note is that you cannot count on the data remaining in
the buffer after the WRITE. In WS it will still be available.
```

#### ↳ Re: Read (no 'into') write (no 'from')

- **From:** "david m scott" <ua-author-12766278@usenetarchives.gap>
- **Date:** 1998-04-16T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ed5ceac33d-p9@usenetarchives.gap>`
- **In-Reply-To:** `<6grrt0$3kn$1@camel15.mindspring.com>`
- **References:** `<6grrt0$3kn$1@camel15.mindspring.com>`

```



Moshe Rybak wrote in article
› In my installation, a programmer maintains that Cobol has a problem
› with it, and one should use a working-storage record as an
› intermediate.

I am rather lazy, and prefer to accomplish as much in a command as the
language permits as long as it doesn't work against readability of the
code. I always code
READ ... INTO and WRITE ... FROM, but the data which I READ is read into an
intermediate area, where I do all my work, then that data is the source in
my WRITE command. I have never seen COBOL have any problem with this
mechanism on any of three platforms that I have used.


david scott
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
