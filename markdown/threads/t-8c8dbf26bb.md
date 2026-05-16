[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Code & JES Log

_11 messages · 6 participants · 2000-05_

---

### Code & JES Log

- **From:** "Mark Muniz" <whtwolf@flash.net>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F%RX4.1301$s64.57515@news.flash.net>`

```
Wondering if anyone has an idea of how to print the program id without
hardcoding it into the code.  Also would like to know if there is a way to
get the job id normally found in the JES log into the output without first
looking at it and then hardcoding that into the code as well.

Just a thought.

Mark Muniz
whtwolf@flash.net
```

#### ↳ Re: Code & JES Log

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gotlj$2asa$1@newssvr04-int.news.prodigy.com>`
- **References:** `<F%RX4.1301$s64.57515@news.flash.net>`

```

See www.mvshelp.com topic: other, subject: Program Lookup of
Jobname/Stepname.

Mark Muniz <whtwolf@flash.net> wrote in message
news:F%RX4.1301$s64.57515@news.flash.net...
> Wondering if anyone has an idea of how to print the program id without
> hardcoding it into the code.  Also would like to know if there is a way to
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Code & JES Log

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-05-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3930A07A.369ADE61@worldnet.att.net>`
- **References:** `<F%RX4.1301$s64.57515@news.flash.net> <8gotlj$2asa$1@newssvr04-int.news.prodigy.com>`

```
Terry Heinze wrote:
> 
> See www.mvshelp.com topic: other, subject: Program Lookup of
> Jobname/Stepname.

I couldn't find this. What's the initial selection from the home page?

Bill Lynch
```

###### ↳ ↳ ↳ Re: Code & JES Log

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-05-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gqdr5$vh6$1@newssvr03-int.news.prodigy.com>`
- **References:** `<F%RX4.1301$s64.57515@news.flash.net> <8gotlj$2asa$1@newssvr04-int.news.prodigy.com> <3930A07A.369ADE61@worldnet.att.net>`

```

Help Boards, then Other Topics.
William Lynch <wblynch@worldnet.att.net> wrote in message
news:3930A07A.369ADE61@worldnet.att.net...
> Terry Heinze wrote:
> >
…[5 more quoted lines elided]…
> Bill Lynch
```

###### ↳ ↳ ↳ Re: Code & JES Log

_(reply depth: 4)_

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-05-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3930CCEF.B984CA83@worldnet.att.net>`
- **References:** `<F%RX4.1301$s64.57515@news.flash.net> <8gotlj$2asa$1@newssvr04-int.news.prodigy.com> <3930A07A.369ADE61@worldnet.att.net> <8gqdr5$vh6$1@newssvr03-int.news.prodigy.com>`

```
Terry Heinze wrote:
> 
> Help Boards, then Other Topics.

Thanks, Terry. I'll give it a shot later.

Bill
```

###### ↳ ↳ ↳ Re: Code & JES Log

_(reply depth: 5)_

- **From:** Charles Haatvedt Jr. <clastname@nospam.com>
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.139b8b14bb88d1da9896ca@news>`
- **References:** `<F%RX4.1301$s64.57515@news.flash.net> <8gotlj$2asa$1@newssvr04-int.news.prodigy.com> <3930A07A.369ADE61@worldnet.att.net> <8gqdr5$vh6$1@newssvr03-int.news.prodigy.com> <3930CCEF.B984CA83@worldnet.att.net>`

```
In article <3930CCEF.B984CA83@worldnet.att.net>, wblynch@worldnet.att.net 
says...
> Terry Heinze wrote:
> > 
…[5 more quoted lines elided]…
> 


the source code for this is on Gilbert Saint-flour's home page as 
follows...

http://members.home.net/gsf/tools/cob2job.txt
```

###### ↳ ↳ ↳ Re: Code & JES Log

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gtu16$spj$1@nntp9.atl.mindspring.net>`
- **References:** `<F%RX4.1301$s64.57515@news.flash.net> <8gotlj$2asa$1@newssvr04-int.news.prodigy.com> <3930A07A.369ADE61@worldnet.att.net> <8gqdr5$vh6$1@newssvr03-int.news.prodigy.com> <3930CCEF.B984CA83@worldnet.att.net> <MPG.139b8b14bb88d1da9896ca@news>`

```
And Gilbert's program is pointed to by the COBOL FAQ (for the semi-frequent
requests in this NG for this information).
```

#### ↳ Re: Code & JES Log

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j_SX4.366$xD4.76185@dfiatx1-snr1.gtei.net>`
- **References:** `<F%RX4.1301$s64.57515@news.flash.net>`

```
There is code at www.mvshelp.com which gets dataset names; that same code
gets the jobname and job step.

Can't help you with the program-id. I just code it in every program as

01  CONSTANTS.
   05  THIS-PROGRAM-NAME     PIC X(08) VALUE 'FOO123'.

If you use a skelton program, it's pretty easy to..

PROGRAM-ID. SKEL.
...
   05 THIS-PROGRAM-NAME   PIC X(08) VALUE 'SKEL'.

...and do a global search and replace
```

##### ↳ ↳ Re: Code & JES Log

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gov6e$3gcs$1@newssvr04-int.news.prodigy.com>`
- **References:** `<F%RX4.1301$s64.57515@news.flash.net> <j_SX4.366$xD4.76185@dfiatx1-snr1.gtei.net>`

```

I just noticed that program-id IS one of the values that can be retrieved.
How's Cheesehead Land?! :)

Michael Mattias <michael.mattias@gte.net> wrote in message
news:j_SX4.366$xD4.76185@dfiatx1-snr1.gtei.net...
> There is code at www.mvshelp.com which gets dataset names; that same code
> gets the jobname and job step.
…[19 more quoted lines elided]…
> michael.mattias@gte.net
```

###### ↳ ↳ ↳ Re: Code & JES Log

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-05-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UPgY4.2393$xD4.428776@dfiatx1-snr1.gtei.net>`
- **References:** `<F%RX4.1301$s64.57515@news.flash.net> <j_SX4.366$xD4.76185@dfiatx1-snr1.gtei.net> <8gov6e$3gcs$1@newssvr04-int.news.prodigy.com>`

```
I just dug out my source code for that module (DPU020); I didn't see
program-id in the TIOT or TCB or JFCB. But how could the PROGRAM-ID be
unique to a task? You may load multiple COBOL modules - with multiple ENTRY
points  (and IIRC, PROGRAM-ID is 'just another entry point')  into a task,
so is that another strcuture pointer list to walk?

Might be interesting sometime to enumerate all the ENTRY names (are the
names even preserved at run time?).

I think you can get the name of all the entries in a load module with some
utility; I have the info at a client site on how to do that, and have sent
myself a reminder to look it up.
```

###### ↳ ↳ ↳ Re: Code & JES Log

_(reply depth: 4)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-05-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gsrsp$1ru6$1@newssvr03-int.news.prodigy.com>`
- **References:** `<F%RX4.1301$s64.57515@news.flash.net> <j_SX4.366$xD4.76185@dfiatx1-snr1.gtei.net> <8gov6e$3gcs$1@newssvr04-int.news.prodigy.com> <UPgY4.2393$xD4.428776@dfiatx1-snr1.gtei.net>`

```

It's there; also, see Charles' post; it directs you Gilbert's home page.
Also, as someone noted in www.mvshelp.com, this is for a program executing
in batch mode.  For CICS, use the ASSIGN CICS command.

Michael Mattias <michael.mattias@gte.net> wrote in message
news:UPgY4.2393$xD4.428776@dfiatx1-snr1.gtei.net...
> I just dug out my source code for that module (DPU020); I didn't see
> program-id in the TIOT or TCB or JFCB. But how could the PROGRAM-ID be
> unique to a task? You may load multiple COBOL modules - with multiple
ENTRY
> points  (and IIRC, PROGRAM-ID is 'just another entry point')  into a task,
> so is that another strcuture pointer list to walk?
…[13 more quoted lines elided]…
> michael.mattias@gte.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
