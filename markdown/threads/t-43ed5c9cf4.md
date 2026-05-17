[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CGI and COBOL

_6 messages · 3 participants · 1998-05_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### CGI and COBOL

- **From:** "scott bentley" <ua-author-15581873@usenetarchives.gap>
- **Date:** 1998-05-06T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6isg1e$j6g$1@ionews.ionet.net>`

```

My company has developed a CGI application in MF COBOL. We were running it
on a web server running Windows NT and Microsoft Internet Information Server
v3.0. We recently upgraded to to IIS V4.0. Now our CGI doesn't work. It
attempts to make a call to a .gnt file (I guess some sort of linked file).
At this point the program appears to stop or never returns anything to the
browser.

Is there ANYONE with some COBOL and CGI experience that can give me a hand.
```

#### ↳ Re: CGI and COBOL

- **From:** "t..." <ua-author-3348609@usenetarchives.gap>
- **Date:** 1998-05-06T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43ed5c9cf4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6isg1e$j6g$1@ionews.ionet.net>`
- **References:** `<6isg1e$j6g$1@ionews.ionet.net>`

```

On Thu, 7 May 1998 09:28:10 -0500, "Scott Bentley"
wrote:

› My company has developed a CGI application in MF COBOL. We were running it
› on a web server running Windows NT and Microsoft Internet Information Server
…[7 more quoted lines elided]…
› 
which MF COBOL? Originally we developed some CGI programming under
VisOc, but until we applied the service pack, we had bad results.
```

##### ↳ ↳ Re: CGI and COBOL

- **From:** "scott bentley" <ua-author-15581873@usenetarchives.gap>
- **Date:** 1998-05-06T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43ed5c9cf4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-43ed5c9cf4-p2@usenetarchives.gap>`
- **References:** `<6isg1e$j6g$1@ionews.ionet.net> <gap-43ed5c9cf4-p2@usenetarchives.gap>`

```

Animator v 8.3.30 and
Workbench v 4.0

That's about as much as I know. And we're using some C program for standard
input.


Studly wrote in message <355··.@new··g.com>...
› On Thu, 7 May 1998 09:28:10 -0500, "Scott Bentley"
› wrote:
…[15 more quoted lines elided]…
›
```

#### ↳ Re: CGI and COBOL

- **From:** "karl wagner" <ua-author-12514286@usenetarchives.gap>
- **Date:** 1998-05-07T10:57:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43ed5c9cf4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6isg1e$j6g$1@ionews.ionet.net>`
- **References:** `<6isg1e$j6g$1@ionews.ionet.net>`

```

Scott Bentley wrote:
› 
› My company has developed a CGI application in MF COBOL. We were running it
…[6 more quoted lines elided]…
› Is there ANYONE with some COBOL and CGI experience that can give me a hand.

I suspect somebody had configured IIS 3.0 to know what to do scripts
with a .GNT extenstion, and this information was lost when you upgraded.
This is just a guess but try adding an REGSZ (string) entry for .gnt to
the registry entry:

HKEY_LOCAL_MACHINE\SYSTEM\ControlSet002\Services\W3SVC\Parameters\Script
Map

Name = .gnt
Value = 'x:\cobol32\exedll\run.exe %s %s'

Take a look at the IIS help for 'Configuring Registry Entries' and the
subheading 'Associating Interpreters with Applications (Script
Mapping)'.

Of course, you could compile and link the CGI script to an EXE and avoid
the configuration issues.

Karl Wagner
```

##### ↳ ↳ Re: CGI and COBOL

- **From:** "scott bentley" <ua-author-15581873@usenetarchives.gap>
- **Date:** 1998-05-06T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43ed5c9cf4-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-43ed5c9cf4-p4@usenetarchives.gap>`
- **References:** `<6isg1e$j6g$1@ionews.ionet.net> <gap-43ed5c9cf4-p4@usenetarchives.gap>`

```

The primary cgi is an .exe file and supposedly it can make calls to the .gnt
files without further assistance (correct me if i'm wrong, I'm just relaying
info my programmer told me). So, there's no need to make script map registry
entries. Besides, I just checked on our production server (the current
problem is luckily on a test box) which is running IIS 3.0 and there were no
script map entries for it. Or anywhere else in the registry.

My worst fear is that IIS 4 is causing the problem. I really hope I'm wrong.



Karl Wagner wrote in message <355··.@sym··o.ca>...
› Scott Bentley wrote:
›› 
…[18 more quoted lines elided]…
› Karl Wagner
```

###### ↳ ↳ ↳ Re: CGI and COBOL

- **From:** "karl wagner" <ua-author-12514286@usenetarchives.gap>
- **Date:** 1998-05-07T11:41:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-43ed5c9cf4-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-43ed5c9cf4-p5@usenetarchives.gap>`
- **References:** `<6isg1e$j6g$1@ionews.ionet.net> <gap-43ed5c9cf4-p4@usenetarchives.gap> <gap-43ed5c9cf4-p5@usenetarchives.gap>`

```

Scott Bentley wrote:
› 
› The primary cgi is an .exe file and supposedly it can make calls to the .gnt
…[29 more quoted lines elided]…
›› Karl Wagner


Basic debugging tips:

1) Does the CGI script work from a command line? (You may have to set a
few environment variables such as CONTENT_LENGTH and REQUEST_METHOD to
fool the script into thinking it was invoked by the web server. Your
programmer probably already knows how to do this.

2) If the answer is 'yes' then check the environment variables like
PATH, and COBDIR to make sure they are set as system variables and
include all the relevant directories. The web server is started as a
system service so the environment variables need to be defined at the
system level in order to be available to the CGI application. Changes to
the environment variables won't take effect until the web server is
restarted, usually by rebooting the machine.

3) Are there any rogue 'DISPLAY' statements in the CGI application.
Anything written to STDOUT will be considered as the reply from the CGI
application. If it doesn't contain the correct MIME headers then the web
browser will choke on it.

Karl Wagner
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
