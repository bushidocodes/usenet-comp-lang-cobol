[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL os/2 API code to change fonts in a presentation space ?

_2 messages · 2 participants · 1995-11_

---

### COBOL os/2 API code to change fonts in a presentation space ?

- **From:** "ets..." <ua-author-17072749@usenetarchives.gap>
- **Date:** 1995-11-17T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48l9re$2mh6@news-s01.ny.us.ibm.net>`

```
Does anyone out there have a piece of code that will change a font in an
OS/2 presentation space ?

I'm trying to create a graphical report to send to my color printer - most of
which is going well except for the &*@#% fonts.

I've tried 'understanding' some C code - but to no avail...

Thanks,

Ethan Schultz


PS - If you know of a GOOD (and complete) book explaining how to use the
OS/2 PM API with COBOL I'd be interested in the Title or ISBN...

Thanks again.....
```

#### ↳ Re: COBOL os/2 API code to change fonts in a presentation space ?

- **From:** "chris mason" <ua-author-1350352@usenetarchives.gap>
- **Date:** 1995-11-22T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e7aa0f9cb0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<48l9re$2mh6@news-s01.ny.us.ibm.net>`
- **References:** `<48l9re$2mh6@news-s01.ny.us.ibm.net>`

```
Hello:
May I suggest OS/2 Presentation Manager Programming for COBOL, and
there's another book with a similar title. Sorry, I don't have it
in from of me. If OS/2 is anything like Windows, you probably will
have to do something like create the Font (really specify the font
characteristics) and then Select it into the current Device Context
for the printer.

The sequence of calls would be something like this:

handleoffont = CreateFont( various parms)
GetPrinterDC
SelectObject

Have you tried coding Presentation manager apps in COBOL?

The above would be something like this in COBOL

Call winapi '__CreateFont' using by value stuff-1
by reference stuff-2
returning handleofffont by value

But the winapi would be OS2API or some such and the function name(s)
would be different...


Chris Mason                                                              
       
"The Unknown COBOL Programmer"                                           
       
The opinions expressed are mine, not my Employers.                       
       
cma··.@lms··d.com or HCM··.@ix.··m.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
