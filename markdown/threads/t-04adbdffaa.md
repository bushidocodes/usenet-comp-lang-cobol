[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress and CGI

_4 messages · 2 participants · 1997-12_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### NetExpress and CGI

- **From:** "10053..." <ua-author-1071939@usenetarchives.gap>
- **Date:** 1997-12-16T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34979756.5000048@news.global-one.at>`

```

Hi everybody!

I just want to know how to use CGI variables like "HTTP_USER_AGENT"
with Micro Focus NetExpress.
I know how to write CGI programs and how to use embedded HTML and so
on, so my only problem is how to use the abovementioned system
variables (the CGI program is running under MS Internet Information
Server / Windows NT 4.0).

Another problem I have:
I have a CGI form on my web page. When the user has filled the fields
and clicks on "submit", the contents of this form should be
automatically e-mailed to me. But when I use the "mailto" command, the
user gets an email window of his mail client program. How can the mail
be sent without user interaction?

Any help will be appreciated!

Thank you all in advance,

R. Graf
```

#### ↳ Re: NetExpress and CGI

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1997-12-16T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-04adbdffaa-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34979756.5000048@news.global-one.at>`
- **References:** `<34979756.5000048@news.global-one.at>`

```

RG wrote:
› I just want to know how to use CGI variables like "HTTP_USER_AGENT"
› with Micro Focus NetExpress.
…[3 more quoted lines elided]…
› Server / Windows NT 4.0).

Hi.

Regular environment variable handling should work:

DATA DIVISION.
WORKING-STORAGE SECTION.
01 USER-AGENT PIC X(100)
PROCEDURE DIVISION.
DISPLAY "HTTP_USER_AGENT" UPON ENVIRONMENT-NAME
ACCEPT USER-AGENT FROM ENVIRONMENT-VALUE
DISPLAY USER-AGENT.

(Haven't compiled or tested this, but it's close enough to point you
in the right direction if it doesn't work as-is).

› Another problem I have:
› I have a CGI form on my web page. When the user has filled the fields
…[3 more quoted lines elided]…
› be sent without user interaction?

Not sure if you can do this automatically within the HTML with a
mailto: URL. Why not just write a simple CGI which formats and emails
the FORM contents ?

Cheers,
Kev.
```

##### ↳ ↳ Re: NetExpress and CGI

- **From:** "10053..." <ua-author-1071939@usenetarchives.gap>
- **Date:** 1997-12-16T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-04adbdffaa-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-04adbdffaa-p2@usenetarchives.gap>`
- **References:** `<34979756.5000048@news.global-one.at> <gap-04adbdffaa-p2@usenetarchives.gap>`

```

On Wed, 17 Dec 1997 11:44:13 +0000, Kevin Digweed
wrote:

›› Another problem I have:
›› I have a CGI form on my web page. When the user has filled the fields
…[10 more quoted lines elided]…
› Kev.

Yes, but how can I realize this (email) with CGI?

Thank you,
Ruediger.
```

###### ↳ ↳ ↳ Re: NetExpress and CGI

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1997-12-18T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-04adbdffaa-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-04adbdffaa-p3@usenetarchives.gap>`
- **References:** `<34979756.5000048@news.global-one.at> <gap-04adbdffaa-p2@usenetarchives.gap> <gap-04adbdffaa-p3@usenetarchives.gap>`

```

RG wrote:
› 
› On Wed, 17 Dec 1997 11:44:13 +0000, Kevin Digweed 
…[14 more quoted lines elided]…
› Yes, but how can I realize this (email) with CGI?

That depends on the Operating System your CGI is destined to run on,
and possibly, the mail clients installed on the server.
Basically, unless you want to talk directly to an OS interface (like
MAPI, on Windows), you need to talk to a mail client which will mail
the document on your behalf - Netscape, MS Exchange, etc. I expect
that talking to a mail client will be the simpler route, but you will
need to read up on the developer docs for those you wish to support
to know how to send a message.

If you intend to port your CGI to Unix, be aware that Unix machines
won't support the OS interface (not suprisingly), and will probably
not have the same clients available. However, on Unix, it may be even
easier, as the standard "mail" or "mailx" command could be used - it
mails it`s standard input stream to the recipients specified on the
command line. Something like:

SELECT mailfile ASSIGN "COBOL_MAILER"
ORGANIZATION LINE SEQUENTIAL.

FD mailfile.
01 mailrec PIC X(100).

PROCEDURE DIVISION.
DISPLAY "DD_COBOL_MAILER" UPON ENVIRONMENT-NAME
DISPLAY ">mailx root" UPON ENVIRONMENT-VALUE

OPEN OUTPUT mailfile
WRITE mailrec FROM "Testing, Testing ...."
CLOSE mailfile
STOP RUN.

This uses the DD_ mechanism to map the file to a pipe which is
connected to the stdin stream of "mailx" (the ">" leading character
indicates this)). When run on a Unix system with "mailx", the mail
message "Testing, Testing ...." should be sent to user "root".
Obviously the real application would need to build that command line
up with the true recipient addresses and subject lines etc. Type
"man mail" from the shell prompt on the Unix machine to see what
options are available (there are a LOT, but most are for mailbox
reading etc and are irrelevant when just using mailx to send a
message).

If you do want to support both Windows based and Unix OS's you should
probably think about abstracting the mail-sending part of your CGI
into a seperate module.

Cheers,
Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
