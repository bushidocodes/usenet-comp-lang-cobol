[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# variable length records

_1 message · 1 participant · 2000-12_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Re: variable length records

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-12-08T00:27:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iWVX5.132$U4.8728@newsread1.prod.itd.earthlink.net>`
- **References:** `<HG9X5.2295$jo.16777708@tomcat.sk.sympatico.ca> <9SaX5.1953$aO1.117854@cletus.bright.net> <uebX5.2309$jo.29622333@tomcat.sk.sympatico.ca> <jvyyrzubevmbagrfvasbezngvpnpbz.g54hsb0.pminews@news.wanadoo.es> <7xbX5.2311$jo.29557061@tomcat.sk.sympatico.ca>`

```

"mike" <mikman@home.com> wrote in message
news:7xbX5.2311$jo.29557061@tomcat.sk.sympatico.ca...
> No not on a mainframe, just running a dos application to
> convert some data. I'm just trying to read a sequential file
…[5 more quoted lines elided]…
> process it that way, thats for sure.

You'll never find it. The CRLF is not transferred to memory during an
ordinary sequential read. Further, the read is terminated at the CRLF
and any unfilled portions of the requested record are blank-filled by
the read operation.

Here's what do:

FD  MYFILE.
01  MYREC.
   02  MYHEAD        PIC X(222).
   02  MYBIG.
      05  MYMEDIUM
         10  MYSMALL  PIC X(37).
         10  FILLER        PIC X(29).
      05  FILLER           PIC X(45).

READ MYFILE.
(Use MYHEAD to deduce whether you have only the header, MYBIG,
MYMEDIUM, or MYSMALL record)
(process whichever)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
