[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem O2/2 warp 32bit cobol calling 16bit c

_2 messages · 2 participants · 1997-02_

---

### Problem O2/2 warp 32bit cobol calling 16bit c

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1997-02-06T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ddvdc$93i@news.interlog.com>`

```

I am having problems calling 16bit dll from 32bit cobol under os/2 warp.
It seems the thunking from 32bit to 16bit is not working.
The calling convention used is 35.
.
SPECIAL-NAMES.
call-convention 35 is thunked.
.
WORKING-STORAGE SECTION.
01 connID pic 9(9) comp-5.
77 ws-error-code pic 9(9) comp-5.
.
PROCEDURE DIVISION.
.
call thunked "NWGetDefaultConnectionID" using
by reference connID
returning ws-error-code
end-call

Links compiles and links o.k.

Links with.

link386 OF98/pmtype:pm+cobintfn+panels2+MFFH+XFHNAME+CBLLDS,OF98.DLL,,mfrts32+mfcmlib+os2386+SQL17O32+OFDBG+DSRUN+nwcalls,OF98.DEF/NOD/NOE/NOI;

Stevan Moldvaj sm··.@int··g.com
```

#### ↳ Re: Problem O2/2 warp 32bit cobol calling 16bit c

- **From:** "del archer" <ua-author-6589011@usenetarchives.gap>
- **Date:** 1997-02-09T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b9bc18ce15-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5ddvdc$93i@news.interlog.com>`
- **References:** `<5ddvdc$93i@news.interlog.com>`

```

sm··d@int··g.com@interlog.com wrote:
›
› I am having problems calling 16bit dll from 32bit cobol under os/2 warp.
› It seems the thunking from 32bit to 16bit is not working.

What do you mean when you say, "not working"?

Del.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
