[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Saving CoBOL

_8 messages · 4 participants · 2008-05_

---

### Saving CoBOL

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-05-01T09:52:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<copj14ltndjh64t1rupc8tv4q9bk4hqsbb@4ax.com>`

```
	
http://blogs.computerworld.com/saving_cobol
```

#### ↳ Re: Saving CoBOL

- **From:** docdwarf@panix.com ()
- **Date:** 2008-05-01T16:21:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fvcqm1$4ta$1@reader2.panix.com>`
- **References:** `<copj14ltndjh64t1rupc8tv4q9bk4hqsbb@4ax.com>`

```
In article <copj14ltndjh64t1rupc8tv4q9bk4hqsbb@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>	
>http://blogs.computerworld.com/saving_cobol

Wow... if someone isn't getting referral-fees then someone doesn't know 
much about Doing Business.

DD
```

#### ↳ Re: Saving CoBOL

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-05-02T12:11:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<67v4hcF2qjiniU1@mid.individual.net>`
- **References:** `<copj14ltndjh64t1rupc8tv4q9bk4hqsbb@4ax.com>`

```


"Howard Brazee" <howard@brazee.net> wrote in message 
news:copj14ltndjh64t1rupc8tv4q9bk4hqsbb@4ax.com...
>
> http://blogs.computerworld.com/saving_cobol
>
I enjoyed the responses more than the article itself.

No matter how you cut it, there is a huge current investment in COBOL and it 
seems irresponsible to simply throw it away.

I think refactoring may be an answer. It has certainly worked for my own 
stuff. I'm still running COBOL components as unmanaged code in .NET and have 
had no need to replace them so far.

The lack of jobs is going to be the main nail in the coffin.

The old-timers are fading away and the new guys can do the same stuff 
smarter and quicker with modern approaches and languages.

That's still noreason to throw away stuff that isn't broken...

Pete.
```

##### ↳ ↳ Re: Saving CoBOL

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-05-01T21:45:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m4-dndWCMZ2C74fVnZ2dnUVZ_gWdnZ2d@mid-floridainternet>`
- **References:** `<copj14ltndjh64t1rupc8tv4q9bk4hqsbb@4ax.com> <67v4hcF2qjiniU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:67v4hcF2qjiniU1@mid.individual.net...
[snip]
> The old-timers are fading away and the new guys can do the same stuff
> smarter and quicker with modern approaches and languages.

LOL!

<
http://www.computerworld.com/action/article.do?command=viewArticleBasic&articleId=266128 >
-----
Cobol's Batch Advantage

October 09, 2006 (Computerworld) -- For some applications,
Cobol can't be beat, says Mark Crego, chief architect at Accenture.
During one project, he wrote a script to translate information from
a government payroll system for job cost reporting. The environment
included midrange systems, a relational database, an extract, transform
and load (ETL) tool, and a data warehouse. "We were running a
13-hour processing window. The result was just too painful," he says.
Then a Cobol programmer looked at the job. "He extracted that into
a flat file and used an old-fashioned sort and was able to process the
entire thing within a 20-minute period. I was blown away," Crego says.
-----
```

###### ↳ ↳ ↳ Re: Saving CoBOL

- **From:** docdwarf@panix.com ()
- **Date:** 2008-05-02T09:34:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fven7l$eb5$1@reader2.panix.com>`
- **References:** `<copj14ltndjh64t1rupc8tv4q9bk4hqsbb@4ax.com> <67v4hcF2qjiniU1@mid.individual.net> <m4-dndWCMZ2C74fVnZ2dnUVZ_gWdnZ2d@mid-floridainternet>`

```
In article <m4-dndWCMZ2C74fVnZ2dnUVZ_gWdnZ2d@mid-floridainternet>,
Rick Smith <ricksmith@mfi.net> wrote:

[snip]

><
>http://www.computerworld.com/action/article.do?command=viewArticleBasic&articleId=266128 >

[snip]

>Then a Cobol programmer looked at the job. "He extracted that into
>a flat file and used an old-fashioned sort and was able to process the
>entire thing within a 20-minute period. I was blown away," Crego says.

This, I would argue, is not an advantage of the language but of learning 
how to see data-flows in different ways.  On my current site I came across 
a few folks who were amused/worried by another team's difficulty in 
loading data into Oracle tables; it seemed like the daily 
transaction-load-and-update took 32 hours.

I said 'Do you want to see someone look uncomfortable? Just for laughs, in 
the next meeting ask if they have sorted the input data into their 
table-key sequence, de-duping it for later research... oh, and ask if 
they've turned journalling off and whether they're using a single-row or 
bulk-load utility.'

The response was a kind of blank-faced 'whuh?' but they did it... and 
reported back that the database team liason (an Anderoid... errrr... 
Accenturion) got all fluster-faced and took notes and said he'd look into 
that... and suddenly there weren't day-and-a-half windows needed for daily 
loads.

DD
```

###### ↳ ↳ ↳ Re: Saving CoBOL

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-05-02T21:56:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6806q2F2qihc4U1@mid.individual.net>`
- **References:** `<copj14ltndjh64t1rupc8tv4q9bk4hqsbb@4ax.com> <67v4hcF2qjiniU1@mid.individual.net> <m4-dndWCMZ2C74fVnZ2dnUVZ_gWdnZ2d@mid-floridainternet> <fven7l$eb5$1@reader2.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fven7l$eb5$1@reader2.panix.com...
> In article <m4-dndWCMZ2C74fVnZ2dnUVZ_gWdnZ2d@mid-floridainternet>,
> Rick Smith <ricksmith@mfi.net> wrote:
…[32 more quoted lines elided]…
>
Good job, Doc.

I haven't worked with Accenturions but I sure had my fill of 
Anderoids...back in their heyday.

I agree entirely with your point about seeing dataflows in different ways.

I would be quick to admit that a background in COBOL is good grounding for 
this.

Pete.
```

###### ↳ ↳ ↳ Re: Saving CoBOL

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-05-02T15:02:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fvfads$gep$1@reader2.panix.com>`
- **References:** `<copj14ltndjh64t1rupc8tv4q9bk4hqsbb@4ax.com> <m4-dndWCMZ2C74fVnZ2dnUVZ_gWdnZ2d@mid-floridainternet> <fven7l$eb5$1@reader2.panix.com> <6806q2F2qihc4U1@mid.individual.net>`

```
In article <6806q2F2qihc4U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
><docdwarf@panix.com> wrote in message news:fven7l$eb5$1@reader2.panix.com...

[snip]

>> I said 'Do you want to see someone look uncomfortable? Just for laughs, in
>> the next meeting ask if they have sorted the input data into their
…[10 more quoted lines elided]…
>Good job, Doc.

It was not what I was getting paid to do, Mr Dashwood... but every so 
often I give some lagniappe.

Now if you thought that a manager looked into this situation and said 'You 
know, maybe we can use this peculiar ability in other places'... you'd 
have thought wrong.

DD
```

###### ↳ ↳ ↳ Re: Saving CoBOL

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-05-02T21:51:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6806hoF2qjrnbU1@mid.individual.net>`
- **References:** `<copj14ltndjh64t1rupc8tv4q9bk4hqsbb@4ax.com> <67v4hcF2qjiniU1@mid.individual.net> <m4-dndWCMZ2C74fVnZ2dnUVZ_gWdnZ2d@mid-floridainternet>`

```


"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:m4-dndWCMZ2C74fVnZ2dnUVZ_gWdnZ2d@mid-floridainternet...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[6 more quoted lines elided]…
>

Fair enough, given your example below. I should have qualified it to "many" 
new guys... Certainly the ones I've worked with would be laughing at your 
"Architect".

> <
> http://www.computerworld.com/action/article.do?command=viewArticleBasic&articleId=266128 >
…[15 more quoted lines elided]…
>
Proof positive that some "Architect"s (what the Hell does that mean anyway?) 
don't know much about architecture... Much easier to say how remarkable it 
was that an old approach was better, than to admit he screwed it up in the 
first place.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
