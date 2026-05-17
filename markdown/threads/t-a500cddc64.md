[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Call to Dos Batch File ??

_5 messages · 5 participants · 1998-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Call to Dos Batch File ??

- **From:** "david mowat" <ua-author-4670319@usenetarchives.gap>
- **Date:** 1998-05-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6jmh2o$lc6$1@fep5.clear.net.nz>`

```

More advice requested.
Trying to call a batch file from a cobol program under Dos.
I have tried :-
Call "MyBatch.bat", and Exec MyBatch and get error 170 "System program not
found".
A call to a cobol module (exe) works fine. [Call "module.exe"]
Any help appreciated, thankyou,
```

#### ↳ Re: Call to Dos Batch File ??

- **From:** "carlos garcia" <ua-author-2945351@usenetarchives.gap>
- **Date:** 1998-05-16T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a500cddc64-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6jmh2o$lc6$1@fep5.clear.net.nz>`
- **References:** `<6jmh2o$lc6$1@fep5.clear.net.nz>`

```

David,

What cobol are you using ? If you notice that, maybe some one can help you!
In Micro-focus Cobol you can do this:

78 dos-command value x"91".
01 resultado pic 99 comp.
01 funcao-91 pic 99 comp.
01 parametros-91.
02 filler pic 99 comp value 0.
02 filler pic x.

procedure division.
DISPLAY "COMANDO.BAT" upon command-line.
call dos-command using resultado, funcao-91, parametros-91.
```

#### ↳ Re: Call to Dos Batch File ??

- **From:** "frank swarbrick" <ua-author-4445237@usenetarchives.gap>
- **Date:** 1998-05-16T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a500cddc64-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6jmh2o$lc6$1@fep5.clear.net.nz>`
- **References:** `<6jmh2o$lc6$1@fep5.clear.net.nz>`

```

David Mowat wrote:
› 
› More advice requested.
…[5 more quoted lines elided]…
› Any help appreciated, thankyou,

That's because a batch file is not an executable. You must call it through
COMMAND.COM. I'm not sure offhand how to include anything after the executable
name, but if you were to attempt it from a DOS prompt you'd type:
"COMMAND /C BATCHNM.BAT". Perhaps something like
CALL "COMMAND.COM" USING COMMAND-LINE, where COMMAND-LINE is a PIC X(80) with
a value of "/C BATCHNM.BAT". I doubt it will work exactly like that, but try
something like that.

DOS commands like "DIR", "CD", etc. would have to be performed in the same manner.

Frank Swarbrick
home: inf··.@spr··t.com
work: fra··.@1st··k.com
```

##### ↳ ↳ Re: Call to Dos Batch File ??

- **From:** "jean-michel bain-cornu" <ua-author-6589093@usenetarchives.gap>
- **Date:** 1998-05-18T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a500cddc64-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a500cddc64-p3@usenetarchives.gap>`
- **References:** `<6jmh2o$lc6$1@fep5.clear.net.nz> <gap-a500cddc64-p3@usenetarchives.gap>`

```

I think this is no good in MF COBOL. CALL x"91" is correct (see previous message) or
CALL "SYSTEM" on unix.

Frank Swarbrick wrote:

› David Mowat wrote:
›› 
…[21 more quoted lines elided]…
› work: fra··.@1st··k.com
```

#### ↳ Re: Call to Dos Batch File ??

- **From:** "dab..." <ua-author-514576@usenetarchives.gap>
- **Date:** 1998-05-17T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a500cddc64-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6jmh2o$lc6$1@fep5.clear.net.nz>`
- **References:** `<6jmh2o$lc6$1@fep5.clear.net.nz>`

```

Just guessing, as I have never tried this before, but I would have thought that
you would have to call the command interpreter (COMMAND.COM) passing the batch
file as a parm.

Might be worth a try.

Dave
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
