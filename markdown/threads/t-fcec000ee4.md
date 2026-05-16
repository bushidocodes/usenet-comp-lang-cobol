[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# realia cobol winapi

_2 messages · 2 participants · 2000-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### realia cobol winapi

- **From:** "Dennis Komeshak" <compusolve@charter.net>
- **Date:** 2000-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<st9h0h28d1ls82@corp.supernews.com>`

```
I am looking for an example of how to call the winapi from Realia COBOL
32bit compiler for renaming and deleting files. I think they are MoveFile
and DeleteFile. I need the format and parameters for the calls. Thanks,
```

#### ↳ Re: realia cobol winapi

- **From:** John Chafin <jchafin@cgwinc.com>
- **Date:** 2000-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8r30d5$ht7$1@nnrp1.deja.com>`
- **References:** `<st9h0h28d1ls82@corp.supernews.com>`

```
Maybe this will help. Make sure you have the Win platform SDK and that
you include the appropriate libraries in your link step.

 01  BOOL                                  pic s9(09) binary.
 01  KeyName                               PIC  X(79).
 01  Filename                              PIC  X(79).

     MOVE LOW-VALUES TO KEYNAME, FILENAME.
     STRING TPS-FILE-PATH-SERVER DELIMITED BY LOW-VALUE
            '\'
            CCLINK-USER-NAME DELIMITED BY SPACE
            '.txt'
            LOW-VALUE
         DELIMITED BY SIZE
         INTO KEYNAME.
     STRING TPS-FILE-PATH-SERVER DELIMITED BY LOW-VALUE
            '\'
            CCLINK-USER-NAME DELIMITED BY SPACE
            '.inp'
            LOW-VALUE
            DELIMITED BY SIZE
            INTO FILENAME.

     CALL 'S_MoveFileA'
         USING BY REFERENCE KEYNAME
                            FILENAME
         GIVING BOOL.

In article <st9h0h28d1ls82@corp.supernews.com>,
  "Dennis Komeshak" <compusolve@charter.net> wrote:
> I am looking for an example of how to call the winapi from Realia
COBOL
> 32bit compiler for renaming and deleting files. I think they are
MoveFile
> and DeleteFile. I need the format and parameters for the calls.
Thanks,
>
> --
…[4 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
