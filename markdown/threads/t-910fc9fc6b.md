[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File Handlers with MicroFocus Server Express

_3 messages · 2 participants · 2003-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### File Handlers with MicroFocus Server Express

- **From:** Helmut Leininger <h.leininger@bull.at>
- **Date:** 2003-08-27T10:25:33+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bihptu$9h7ih$1@ID-54033.news.uni-berlin.de>`

```
Hi,

I want to use my own file handlers (dependent on file type) with 
ServerExpress programs. Basically, that is no big deal.

The challenge is:
The decision if my own file handler or the MF standard file handler 
should be used for a specific file must be made at run time depending on 
an environment variable.
This could be done in the Object Cobol Developer Suite with the help of 
ufhtab.o which is not existing any more. Now, if I try to call the 
standard file handler (e.g. sqfile) from my switching handler (-msqfile 
mysqfile), I enter a recursive loop.

Are there any ideas how to do?

Best regards
```

#### ↳ Re: File Handlers with MicroFocus Server Express

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2003-08-27T13:31:30+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bii90i$s69$1@hyperion.microfocus.com>`
- **References:** `<bihptu$9h7ih$1@ID-54033.news.uni-berlin.de>`

```
Hi Helmut.

I've just replied to your posting on the Micro Focus forum, but I'll include
my response here also. With Server Express, the command-line required for
linking in your own file handler has changed. The text below is taken from
the Server Express Migration Guide :

If you call your own file handler, you should relink your application. For
example, you would previously have used a command similar to:
cob -xvo rts32 $COBDIR/ufhtab.o
    user-module -muixfile=user-file-handler
    -m urlfile=rlfile -m usqfile=sqfile -m uixfilev=ixfilev
    -m urlfilev=rlfilev -m usqfilev=sqfilev -e ''whereas you would now use:

cob -mixfile=user-file-handler -x callmyprog.cbl myprog1.cbl
user-module.oSimonT.
```

##### ↳ ↳ Re: File Handlers with MicroFocus Server Express

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2003-08-27T13:33:13+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bii93o$s6i$1@hyperion.microfocus.com>`
- **References:** `<bihptu$9h7ih$1@ID-54033.news.uni-berlin.de> <bii90i$s69$1@hyperion.microfocus.com>`

```
Apologies for the formatting problem. The command line should read :


cob -mixfile=user-file-handler -x callmyprog.cbl myprog1.cbl user-module.o


SimonT.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
