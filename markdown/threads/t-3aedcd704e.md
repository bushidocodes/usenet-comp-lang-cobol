[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Integrating WebSphere Applications with COBOL Applications

_5 messages · 5 participants · 2003-10_

---

### Integrating WebSphere Applications with COBOL Applications

- **From:** dineshmalhotra <member44613@dbforums.com>
- **Date:** 2003-10-17T09:49:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3493280.1066398554@dbforums.com>`

```

Hello Everyone -



I am currently working with a large company that has huge COBOL
investments (applications and resources) that is moving towards a
distributed mid-range solution environment using WebSphere on AIX.



We would like to use our COBOL resources and have them write the core
business functionality for one of the application in COBOL (why COBOL
programmers - they already understand the business logic verfy well)
and maintain the data access to the Oracle 9i database.  However, we
would like to use Java within WebSphere to expose the interfaces for
the COBOL programs.



Has any one ever used this architecture paradigm for a high volume,
performance sensitive solution and if yes, what would you advise us to
keep in mind when we architect this solution?



Any or all help on this subject will be truly appreciated.



**PS**

We have MicroFocus COBOL in house but they haven't been able to come up
with an option that will address our concerns from the reliability,
failover, availability and scalability perspective.
```

#### ↳ Re: Integrating WebSphere Applications with COBOL Applications

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-10-17T23:15:13-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F90A231.F4954A2C@istar.ca>`
- **References:** `<3493280.1066398554@dbforums.com>`

```
dineshmalhotra wrote:
> 
> Hello Everyone -
…[10 more quoted lines elided]…
> the COBOL programs.

Did the company investigate using Websphere on z/OS with either Oracle
for z/OS or DB2?  Java also runs on z/OS.

> 
> Has any one ever used this architecture paradigm for a high volume,
…[12 more quoted lines elided]…
> Posted via http://dbforums.com
```

#### ↳ Re: Integrating WebSphere Applications with COBOL Applications

- **From:** mossjm@wideopenwest.com (QCBLSRC)
- **Date:** 2003-10-19T10:00:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3473e5fa.0310190900.1a024ecd@posting.google.com>`
- **References:** `<3493280.1066398554@dbforums.com>`

```
dineshmalhotra 

Your best solution is the AS/400.
It runs COBOL and Java/WebSphere.

You can run your COBOL apps and have Websphere/Java apps update the
same data files in realtime.  I am doing it with great success.

QCBLSRC
```

#### ↳ Re: Integrating WebSphere Applications with COBOL Applications

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2003-10-21T10:42:51+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bn2ut7$9il$1@hyperion.microfocus.com>`
- **References:** `<3493280.1066398554@dbforums.com>`

```
Micro Focus Server Express allows you to mix COBOL and Java in the same
application and will work with WebSphere. This will get even better when
Micro Focus Enterprise Server is released on ALL major Unix platforms very
soon.

Paul
www.microfocus.com

"dineshmalhotra" <member44613@dbforums.com> wrote in message
news:3493280.1066398554@dbforums.com...
>
> Hello Everyone -
…[36 more quoted lines elided]…
> Posted via http://dbforums.com
```

#### ↳ Re: Integrating WebSphere Applications with COBOL Applications

- **From:** "Gary" <IDontThink@so.com.so>
- **Date:** 2003-10-31T01:38:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D2job.66211$e01.229622@attbi_s02>`
- **References:** `<3493280.1066398554@dbforums.com>`

```
"dineshmalhotra" wrote:

<snip>

> We would like to use our COBOL resources and have them write the core
> business functionality for one of the application in COBOL (why COBOL
…[3 more quoted lines elided]…
> the COBOL programs.

Dinesh, Micro Focus Net Express V4.0 (released May 2003) will allow you to
expose the interfaces of your COBOL programs, narrow the interface,
construct the necessary mappings and generate an EJB (for you) that you can
deploy within WebSphere. The connection mechanism is established through use
of the Java Connector Architecture (JCA).

Look at:
http://supportline.microfocus.com/supportline/documentation/books/nx40/nx40indx.htm

Select "Distributed Computing" -> "Interface Mapping Toolkit".

Gary.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
