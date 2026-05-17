[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Animate - calling DLL's

_2 messages · 2 participants · 1996-11_

---

### MF Animate - calling DLL's

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1996-11-24T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<57bq77$rhu$1@news-feed.inet.tele.dk>`

```

Hi;

I'm trying to animate a Cobol program where I call some rutines in a DLL.
The call statement looks like this:
CALL '_CICS_EpiInitialize'
USING BY VALUE CICS-EPI-VERSION-100
RETURNING EPI-RETURN-CODE.
When I run the program in .EXE mode, I have no problem, but when i try to run in
ANIMATE Mode, i receive error 173;
Called program file not found in drive/directory (Error 173)

I'm running on OS/2, using MF Cobol 3.1.54

Any ideas how to do this ?

Regards

Niels Chr. Madsen
```

#### ↳ Re: MF Animate - calling DLL's

- **From:** "jamie burks" <ua-author-6589396@usenetarchives.gap>
- **Date:** 1996-11-24T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ead69f81bd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<57bq77$rhu$1@news-feed.inet.tele.dk>`
- **References:** `<57bq77$rhu$1@news-feed.inet.tele.dk>`

```

You probably haven't loaded the DLL to make the entry points available.
You'll have to do something like this:

...
01 MF-PROC-PTR USAGE PROCEDURE-POINTER.
...
SET MF-PROC-PTR TO ENTRY "file.DLL".

This causes the runtime to load the DLL and make it's entry points
available. I assume you weren't having a problem with the .EXE because
you linked those routines in. I don't know if this method will break a
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
