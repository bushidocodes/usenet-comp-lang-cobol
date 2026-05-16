[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress, CGI, and Environment Variable Question

_3 messages · 3 participants · 2001-02_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### NetExpress, CGI, and Environment Variable Question

- **From:** "Progger" <karturner@aol.com>
- **Date:** 2001-02-01T08:41:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9865AC34C35B30EC.0A509C17C1B0D555.71DD4FFD943AD6FE@lp.airnews.net>`

```
Help please.   Is it possible to set a value to a CGI environment variable?
How about a regular variable or parameter?  If so, how?  Thanks for any help
you can offer.

Karen
```

#### ↳ Re: NetExpress, CGI, and Environment Variable Question

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2001-02-01T14:24:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Skee6.35999$KP3.9856678@news3.rdc1.on.home.com>`
- **References:** `<9865AC34C35B30EC.0A509C17C1B0D555.71DD4FFD943AD6FE@lp.airnews.net>`

```
You may want to read the reference material on Internet programming that
ships with NetExpress. It's quite thorough.

Normally CGI environment variables are set by the http server and read by
the CGI application.
If you're using environment variables to pass information to subprocesses
then there are more efficient mechanisms you should be considering  However,
if you really want to set environment variables then NetExpress supports the
X/Open extensions.

To set the value of the environment variable my_env_var

DISPLAY "my_env_var" UPON ENVIRONMENT-NAME
DISPLAY my-env-val  UPON ENVIRONMENT-VALUE

To read an environment variable:

DISPLAY "my_env_var" UPON ENVIRONMENT-NAME
ACCEPT my-env-val FROM ENVIRONMENT-VALUE

I have no idea what you mean by "regular variable or parameter". COBOL
variables are set using instructions like MOVE, STRING, UNSTRING, COMPUTE,
ADD, SUBTRACT, MULTIPY, DIVIDE, ACCEPT, READ, etc. ;-)

- Karl



"Progger" <karturner@aol.com> wrote in message
news:9865AC34C35B30EC.0A509C17C1B0D555.71DD4FFD943AD6FE@lp.airnews.net...
> Help please.   Is it possible to set a value to a CGI environment
variable?
> How about a regular variable or parameter?  If so, how?  Thanks for any
help
> you can offer.
>
> Karen
>
>
```

##### ↳ ↳ Re: NetExpress, CGI, and Environment Variable Question

- **From:** "Progger" <turner_karen@mail.chattanooga.gov>
- **Date:** 2001-02-01T12:06:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3154FC593316E601.D9A537C4B04431C9.452EAF702A0C2F8C@lp.airnews.net>`
- **References:** `<9865AC34C35B30EC.0A509C17C1B0D555.71DD4FFD943AD6FE@lp.airnews.net> <Skee6.35999$KP3.9856678@news3.rdc1.on.home.com>`

```
Thanks.
This is not internet related.  This is the situation that I have (I will try
to be brief)....

In 1997, we migrated from our in house accounting and purchasing
applications from IBM to SCT BANNER application on the Windows 95 (for user
interface) and VMS (for Oracle db and reports and processes).  If not
familiar, SCT BANNER is a outside package.  The user interface is
Developer/Designer 2000 and reports and process are C and Cobol which are
ran from VMS batch files.  Since then we have written a couple hundred in
house Cobol programs.

Now we have migrated Banner to NT.  The only thing left of accounting and
purchasing that is still running on VMS are the couple hundred in house
cobol programs.  The goal it to get them off of VMS.  Management has chosed
Microfocus NetExpress for the Cobol and Perl for the job/batch file.  I
believe Perl was chosen because that is what Banner uses.

ALL of our cobol programs pass data back and forth to the batch files
running them by getting symbols and setting symbols.  Our jobs have to be
integrated with the Banner application (submitted and ran in the same way as
Banner baseline jobs).  To make them work with Banner's submission screens
with little or no modification to Banner programs our in house jobs have to
be able to get and set Perl variables that are available.  I understand that
this is the way that Banner is doing it.

We haven't actually started converting our programs.  I am just gathering
information.  I have an assignment to do the first program, but right now I
have other pressing assignments.  I am sure to have many, many questions as
time goes by.  Any insight that anyone can provide will be greatly
appreciated.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
