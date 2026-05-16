[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Record lengths in Unix

_7 messages · 3 participants · 2002-07_

---

### Record lengths in Unix

- **From:** "Dan" <deacondan25@NOSPAMhotmail.com>
- **Date:** 2002-07-06T22:15:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uifcj55ubiqjbf@corp.supernews.com>`

```
I am doing a migration from Vax to Tru64 Unix using ksh. We are using Compaq
Cobol. The problem I am having is this:

When using a Write After Advancing I get a CRLF which is making my records 2
bytes longer than the record is defined. I can handle this by defining the
output as pic x(100) and the input as pic x(102).

When I use a Write without an advancing, I can use the same input record
length as my output. The problem with this is that instead of 100, 100 byte
records I have 1, 10000 byte record. This is fine for passing data into
another program but it does my sorts no good. What's the point of sorting
only 1 record.

Has anyone run across this problem? How did you fix it? Is there a way
around this?

Thanks,
Dan
```

#### ↳ Re: Record lengths in Unix

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-07-07T06:10:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-s2QW1huNvgxL@thishost>`
- **References:** `<uifcj55ubiqjbf@corp.supernews.com>`

```
On Sun, 7 Jul 2002 03:15:48 UTC, "Dan" <deacondan25@NOSPAMhotmail.com>
wrote:

> I am doing a migration from Vax to Tru64 Unix using ksh. We are using Compaq
> Cobol. The problem I am having is this:
…[13 more quoted lines elided]…
> 

Try defining the file to the sort as having "fixed length 100 byte 
records".

What kind of sort are you using? Most sort programs I know of will 
handle fixed record length sequential files.
```

##### ↳ ↳ Re: Record lengths in Unix

- **From:** "Dan" <deacondan25@NOSPAMhotmail.com>
- **Date:** 2002-07-07T02:28:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uifrcs1qhgu2f4@corp.supernews.com>`
- **References:** `<uifcj55ubiqjbf@corp.supernews.com> <ZpzG4UNLyRNq-pn2-s2QW1huNvgxL@thishost>`

```

<lsunley@mb.sympatico.ca> wrote in message
news:ZpzG4UNLyRNq-pn2-s2QW1huNvgxL@thishost...
> On Sun, 7 Jul 2002 03:15:48 UTC, "Dan" <deacondan25@NOSPAMhotmail.com>
> wrote:
>
> > I am doing a migration from Vax to Tru64 Unix using ksh. We are using
Compaq
> > Cobol. The problem I am having is this:
> >
> > When using a Write After Advancing I get a CRLF which is making my
records 2
> > bytes longer than the record is defined. I can handle this by defining
the
> > output as pic x(100) and the input as pic x(102).
> >
> > When I use a Write without an advancing, I can use the same input record
> > length as my output. The problem with this is that instead of 100, 100
byte
> > records I have 1, 10000 byte record. This is fine for passing data into
> > another program but it does my sorts no good. What's the point of
sorting
> > only 1 record.
> >
…[11 more quoted lines elided]…
> Lorne Sunley

I'm using unix sort. man sort(1) does not really make make reference being
able to do this. Though I haven't tried using the -z. If this works, this
may not resolve all of the problems.
```

###### ↳ ↳ ↳ Re: Record lengths in Unix

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-07-07T14:24:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DaYV8.56781$q53.1583876@twister.austin.rr.com>`
- **References:** `<uifcj55ubiqjbf@corp.supernews.com> <ZpzG4UNLyRNq-pn2-s2QW1huNvgxL@thishost> <uifrcs1qhgu2f4@corp.supernews.com>`

```
 I'm assuming you are creating a report here or something, in which case, have you tried using a LINE SEQUENTIAL file for the
output? I think that Compaq (DEC) COBOL has that in it, and it essentially writes a variable length record terminated by a EOL
character. (Under UNIX that will be newline.)

Out of curiosity, if you are not writing a report from this, (and why you would be sorting a report I don't
know...) why are you using the "after advancing" clause? Just read the records from one file and write them to another after doing
whatever rearrangement, editing, merging, or whatever you need to do each record. If you need the records to be line delaminated for
sort, instead of truly sequential (or consecutive, whatever it is called on your platform) you should be able to use the LINE
SEQUENTIAL file type.

Sort does like to handle files with a clearly evident EOL character, so I see your issue there. the -z option pretty much just keeps
SORT from terminating if an input line is LONGER than expected, but that isn't exactly what you want.  I admit to being somewhat
curious about this, can you provide a few more details?

Thanks
Paul


"Dan" <deacondan25@NOSPAMhotmail.com> wrote in message news:uifrcs1qhgu2f4@corp.supernews.com...
>
> <lsunley@mb.sympatico.ca> wrote in message
…[40 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Record lengths in Unix

_(reply depth: 4)_

- **From:** "Dan" <deacondan25@NOSPAMhotmail.com>
- **Date:** 2002-07-07T20:48:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uihrqdjgs0bmb7@corp.supernews.com>`
- **References:** `<uifcj55ubiqjbf@corp.supernews.com> <ZpzG4UNLyRNq-pn2-s2QW1huNvgxL@thishost> <uifrcs1qhgu2f4@corp.supernews.com> <DaYV8.56781$q53.1583876@twister.austin.rr.com>`

```

"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
news:DaYV8.56781$q53.1583876@twister.austin.rr.com...
> I'm assuming you are creating a report here or something, in which case,
have you tried using a LINE SEQUENTIAL file for the
> output? I think that Compaq (DEC) COBOL has that in it, and it essentially
writes a variable length record terminated by a EOL
> character. (Under UNIX that will be newline.)
>
> Out of curiosity, if you are not writing a report from this, (and why you
would be sorting a report I don't
> know...) why are you using the "after advancing" clause? Just read the
records from one file and write them to another after doing
> whatever rearrangement, editing, merging, or whatever you need to do each
record. If you need the records to be line delaminated for
> sort, instead of truly sequential (or consecutive, whatever it is called
on your platform) you should be able to use the LINE
> SEQUENTIAL file type.
>
> Sort does like to handle files with a clearly evident EOL character, so I
see your issue there. the -z option pretty much just keeps
> SORT from terminating if an input line is LONGER than expected, but that
isn't exactly what you want.  I admit to being somewhat
> curious about this, can you provide a few more details?
>
> Thanks
> Paul

Thank you, thank you thank you. LINE SEQUENTIAL  is exactly what I was
looking for. I wish I had know about this option sooner, it would have saved
me hours of grief.
For files from the lan, using /usr/bin/mtools/dos2unix takes care of the
additional byte there.

We have tried all sorts of combos from stripping the extra byte(s)  to
expanding the incoming record size.

To answer your question about "after advancing", I guess it's years of
coding habits(bad?) on MVS and VMS systems. As long as the file is defined
as FB, the system will handle the CRs and LFs without difficulty. So I have
pretty much used "write" and "write after advancing" interchangably. This
move to unix is where we've had all of the problems. Allowing the system to
default the file to sequential is part of the problem. I haven't really used
the "organization is" except when using vsam files.

Here's how to handle the sort when using the "write" statement for the
single record:
          fold -w 142 filein.dat | sort  -o filout.dat -k 1.137,1.142r
"fold" defines the record length and pipes it to sort. Works pretty good.

Another question. Is it possible using unix sort to reformat a record? ie
take a 100 byte record, get the middle 50 bytes and apend 20 additional
characters to the end, sort it, eliminate duplicates and get a 70 byte fixed
record. What I would give for Syncsort.

Many thanks,
Dan
```

###### ↳ ↳ ↳ Re: Record lengths in Unix

_(reply depth: 5)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-07-08T03:37:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IN7W8.59673$p85.1780235@twister.austin.rr.com>`
- **References:** `<uifcj55ubiqjbf@corp.supernews.com> <ZpzG4UNLyRNq-pn2-s2QW1huNvgxL@thishost> <uifrcs1qhgu2f4@corp.supernews.com> <DaYV8.56781$q53.1583876@twister.austin.rr.com> <uihrqdjgs0bmb7@corp.supernews.com>`

```
You are welcome. I tend to cheat going from MVS to UNIX, I just FTP the blasted files down to the UNIX machine in ASCII mode. That takes plain old sequential files and turns them into line sequential files. At least it works on AIX. ;) 

Believe it or not, there are UNIX tools that do just about everything that SyncSort will do, but you have to put them together. What you essentially want to do is run a filter against the input to strip out the middle 50 bytes, add in the 20, and write out a 70 byte record which you pipe through sort with the -u option. (-u will eliminate duplicate keys, so I am assuming there that keys will not be identical unless the entire record is identical, that may be a bad assumption. If it is, there are other simple ways to do it of course.) 

For the filter, you can use a C program, an Awk or SED script, or even a COBOL program. :) 
In fact, here is a small COBOL program that might work for you on it. (C is even easier, but unless you are familiar with C, the syntax is somewhat arcane.) Several utilities besides AWK and SED also exist for this - you might look at it as a good excuse to learn PERL.  Using the example below, you would run something like 
this: 

cobf < input-line-sequential-file-ending-with-a-line-of-spaces | sort -u 

Hope this helps a bit, if you need more intensive help, e-mail me directly and I'll see what I can do to help you out. I don't have your COBOL compiler available to me here, but I can certainly help you out with the UNIX, C and so forth a bit. 
 
-Paul

      **************
       identification division.
       program-id. 'cobf'.
       data division.
       working-storage section.
       01  ws-input-line                             pic x(100).
       01  ws-output-line                            pic x(70).

       procedure division.
           accept ws-input-line
           perform until ws-input-line = SPACES
             move ws-input-line(25:50) to ws-output-line
             move "12345678901234567890" to ws-output-line(51:20)
             display ws-output-line
             accept ws-input-line
             end-perform
           goback.
 

"Dan" <deacondan25@NOSPAMhotmail.com> wrote in message news:uihrqdjgs0bmb7@corp.supernews.com...
> 
> "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
…[57 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Record lengths in Unix

_(reply depth: 6)_

- **From:** "Dan" <deacondan25@NOSPAMhotmail.com>
- **Date:** 2002-07-08T20:09:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uikdtfc9g34qf9@corp.supernews.com>`
- **References:** `<uifcj55ubiqjbf@corp.supernews.com> <ZpzG4UNLyRNq-pn2-s2QW1huNvgxL@thishost> <uifrcs1qhgu2f4@corp.supernews.com> <DaYV8.56781$q53.1583876@twister.austin.rr.com> <uihrqdjgs0bmb7@corp.supernews.com> <IN7W8.59673$p85.1780235@twister.austin.rr.com>`

```
I haven't had any problems with FTP'd files for testing. However, with the Vax going away...

Yes, in this case, the dups will be on the whole record. Other cases are not so simple, the example is a good start.

There's still alot to learn with Unix. It may take awhile. Like your example below, I still have some difficulty remembering how to use the pipes properly. Your Cobol example is even simpler than what I had envisioned. As for Awk and sed, I still need to learn them. C and Perl may have to wait a while. Since everyone is new to unix, I probably try to stick with Unix utilities, cobol or sas. It will make it easier to turn the system over.
Thanks --Dan
  "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message news:IN7W8.59673$p85.1780235@twister.austin.rr.com...
  You are welcome. I tend to cheat going from MVS to UNIX, I just FTP the blasted files down to the UNIX machine in ASCII mode. That takes plain old sequential files and turns them into line sequential files. At least it works on AIX. ;) 

  Believe it or not, there are UNIX tools that do just about everything that SyncSort will do, but you have to put them together. What you essentially want to do is run a filter against the input to strip out the middle 50 bytes, add in the 20, and write out a 70 byte record which you pipe through sort with the -u option. (-u will eliminate duplicate keys, so I am assuming there that keys will not be identical unless the entire record is identical, that may be a bad assumption. If it is, there are other simple ways to do it of course.) 

  For the filter, you can use a C program, an Awk or SED script, or even a COBOL program. :) 
  In fact, here is a small COBOL program that might work for you on it. (C is even easier, but unless you are familiar with C, the syntax is somewhat arcane.) Several utilities besides AWK and SED also exist for this - you might look at it as a good excuse to learn PERL.  Using the example below, you would run something like 
  this: 

  cobf < input-line-sequential-file-ending-with-a-line-of-spaces | sort -u 

  Hope this helps a bit, if you need more intensive help, e-mail me directly and I'll see what I can do to help you out. I don't have your COBOL compiler available to me here, but I can certainly help you out with the UNIX, C and so forth a bit. 

  -Paul

        **************
         identification division.
         program-id. 'cobf'.
         data division.
         working-storage section.
         01  ws-input-line                             pic x(100).
         01  ws-output-line                            pic x(70).

         procedure division.
             accept ws-input-line
             perform until ws-input-line = SPACES
               move ws-input-line(25:50) to ws-output-line
               move "12345678901234567890" to ws-output-line(51:20)
               display ws-output-line
               accept ws-input-line
               end-perform
             goback.
   

  "Dan" <deacondan25@NOSPAMhotmail.com> wrote in message news:uihrqdjgs0bmb7@corp.supernews.com...
  > 
  > "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
…[57 more quoted lines elided]…
  >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
