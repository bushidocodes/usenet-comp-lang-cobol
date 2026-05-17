[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SORT and sections: for language lawyers

_5 messages · 5 participants · 1997-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`VSAM, files, sorting`](../topics.md#files)

---

### SORT and sections: for language lawyers

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1997-07-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33C58103.548F@swbell.net>`

```

When you code an input or output procedure for the SORT verb,
does the procedure have to be a section? or can it be a
paragraph? The same question applies to MERGE.

My ancient Tyler Welburn textbook from Cobol school (ca. 1984)
says the procedure has to be a section. However when I look in
the Cobol II manual, I don't see any such requirement.

I can think of several possible reasons for this discrepancy
(including my missing something in the manual). Can a kindly
language lawyer help me out?

(I am NOT asking about the desirability of sections or paragraphs,
or whether we should even use SORT at all. I am asking about the
requirements of the language.)

Thank you.

Michael C. Kasten mc··.@swb··l.net
Visit me at http://home.swbell.net/mck9/cobol/cobol.html
```

#### ↳ Re: SORT and sections: for language lawyers

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-07-10T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d09ff1e4eb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33C58103.548F@swbell.net>`
- **References:** `<33C58103.548F@swbell.net>`

```

Michael C. Kasten wrote:
› 
› When you code an input or output procedure for the SORT verb,
…[18 more quoted lines elided]…
› Visit me at http://home.swbell.net/mck9/cobol/cobol.html

IBM COBOL II Release 3 and COBOL for MVS and VM allow SORT input procedure
and output procedure to be a paragraph rather than a section.

I'm not absolutely certain, but I believe the ANSI-85 standard dropped the
requirement the SORT procedures be sections.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

##### ↳ ↳ Re: SORT and sections: for language lawyers

- **From:** "willy weisz" <ua-author-6589000@usenetarchives.gap>
- **Date:** 1997-07-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d09ff1e4eb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d09ff1e4eb-p2@usenetarchives.gap>`
- **References:** `<33C58103.548F@swbell.net> <gap-d09ff1e4eb-p2@usenetarchives.gap>`

```

Arnold Trembley wrote:
› 
› Michael C. Kasten wrote:
…[26 more quoted lines elided]…
› requirement the SORT procedures be sections.

The ISO/ANSI COBOL-85 Standard has indeed dropped the requirement for
SORT/MERGE procedures to be sections.

This requirement stemmed from the SEGMENTATION MODULE (a long outdated
facility for defining memory overlays in COBOL) which has been defined
as obsolete in COBOL-85 as the paging in and out of parts of a program
is nowadays taken care of much more efficiently by the operating
system.

› 
› Arnold Trembley
› Software Engineer I (just a job title, still a programmer)
› MasterCard International
› St. Louis, Missouri

Willy
------------------------------------------------------------------------------
Willy Weisz

Technische Universitaet Wien         Vienna University of Technology
EDV-Zentrum                          Computing Services
Hochleistungsrechnen                 High Performance Computing

                       Wiedner Hauptstrasse 8-10
                       A-1040 Wien

Tel: (+43 1) 588 01 - 5818                  Fax: (+43 1) 587 42 11
                     e-mail: we··.@edv··c.at
```

#### ↳ Re: SORT and sections: for language lawyers

- **From:** "eugene a. pallat" <ua-author-501199@usenetarchives.gap>
- **Date:** 1997-07-10T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d09ff1e4eb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<33C58103.548F@swbell.net>`
- **References:** `<33C58103.548F@swbell.net>`

```

Michael C. Kasten wrote in article
<33C··.@swb··l.net>...
› When you code an input or output procedure for the SORT verb,
› does the procedure have to be a section? or can it be a
…[12 more quoted lines elided]…
› requirements of the language.)

The procedures can be either paragraphs or sections. I've used both,
depending upon the application.

Remove the '-' from orion-data for sending email to me.

Gene eap··.@ori··a.com

Orion Data Systems

Solicitations to me must be pre-approved in writing
by me after soliciitor pays $1,000 US per incident.
Solicitations sent to me are proof you accept this
notice and will send a certified check forthwith.
```

#### ↳ Re: SORT and sections: for language lawyers

- **From:** "tom mcfarland" <ua-author-3012834@usenetarchives.gap>
- **Date:** 1997-07-18T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d09ff1e4eb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<33C58103.548F@swbell.net>`
- **References:** `<33C58103.548F@swbell.net>`

```

COBOL II release 3 and above allows use of paragraph names as input/output
procedures. If I remember correctly, COBOL 74 allowed paragraph names but
the compiler issued a W level message with the notation that the statement
was something like 'You used a paragraph when I was expecting a section.
Statement accepted as written'. More importantly, it worked. For some
reason, release 2 of COBOL II (again if I remember correctly) elevated the
diagnostic message to the next level (E?) thus giving a return code of 8
from the compiler. Of course all of the canned procedures for program
compiles allowed the link to execute after a cc 4 but not an 8, even though
the compiler said that it was basically OK. Sanity returned in release 3.
The compiler in use at my current job does not even mention it in passing.

MERGE is no different.

It seems to be almost universally accepted that sections are required for
sort input/output procedures, but my experience has been that they are not,
except for that brief time that I used COBOL II, release 2 as noted above.


Tom McFarland

Michael C. Kasten  wrote in article
<33C··.@swb··l.net>...
> When you code an input or output procedure for the SORT verb,
> does the procedure have to be a section? or can it be a
…[18 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
