[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# assignment

_11 messages · 6 participants · 1999-10 → 1999-11_

---

### assignment

- **From:** "xyz" <Suze.V@online.be>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v7brc$3i$1@trex.antw.online.be>`

```
I have a project for my school, and I have a problem.

I want to build in some time related objects, like a timer on the right
upper corner, ...
can anybody help me with this?

Kareem.v@online.be
```

#### ↳ Re: assignment

- **From:** docdwarf@clark.net ()
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZuGR3.3265$pp1.68327@dfw-read.news.verio.net>`
- **References:** `<7v7brc$3i$1@trex.antw.online.be>`

```
In article <7v7brc$3i$1@trex.antw.online.be>, xyz <Suze.V@online.be> wrote:
>I have a project for my school, and I have a problem.

Please do your own homework.

DD
```

#### ↳ Re: assignment

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v7hr2$q2t$1@aklobs.kc.net.nz>`
- **References:** `<7v7brc$3i$1@trex.antw.online.be>`

```
xyz <Suze.V@online.be> wrote:
: I have a project for my school, and I have a problem.

: I want to build in some time related objects, like a timer on the right
: upper corner, ...
: can anybody help me with this?

It is easy enough to get the time using ACCEPT Time-Data FROM TIME,
and this can be displayed with DISPLAY Time-Data AT 0170 (may
vary depending on compiler).

There are two problems, the first is that if you do an ACCEPT
then it will wait for the user to enter the data (depending
on which device the accept operated on).  It _may_ be possible
to have the ACCEPT terminate automatically your compiler
supports ON TIMEOUT (or similar).

The second problem is that a program that is just displaying
the time (and possibly checking other things) may use all the
CPU time it can get hold of.  This is anti-social on a multi-user
machine and inconvenient on a multi-tasking one.

If, for example, you use Windows and it becomes exceedingly
sluggish because you are running a time-display program you
may be a little annoyed.  If it is a Unix box then others
will be annoyed too (though Unix wouldn't suffer as much).
```

##### ↳ ↳ Re: assignment

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v7k1b$n1v$1@neptunium.btinternet.com>`
- **References:** `<7v7brc$3i$1@trex.antw.online.be> <7v7hr2$q2t$1@aklobs.kc.net.nz>`

```

Richard Plinston wrote in message <7v7hr2$q2t$1@aklobs.kc.net.nz>...
>xyz <Suze.V@online.be> wrote:
>: I have a project for my school, and I have a problem.
…[28 more quoted lines elided]…
>


Why use DOS, if you use Windows using the "new" Cobol you could simply
register an area for an Idle Object which will then update that area when
the date changes.

Such as:

         invoke wsEventManager "registerIdleObject" using self


Simon R Hart
Eaton, Ottery St. Mary, UK.
```

##### ↳ ↳ Re: assignment

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3818490A.23E01047@zip.com.au>`
- **References:** `<7v7brc$3i$1@trex.antw.online.be> <7v7hr2$q2t$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:
> 
> xyz <Suze.V@online.be> wrote:
…[26 more quoted lines elided]…
> --

Look up _beginthread in your windows manual.  Get the cursor to the
position and print the time.  Restore the cursor position.  Sleep one
second and do it again.

In unix look up pthread_create.
In MVS look up pthread_create and forget about doing it, it is to
hard.


By the way I have no idea whether this will work, 
Ken
```

###### ↳ ↳ ↳ Re: assignment

- **From:** "xyz" <Suze.V@online.be>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7va0v3$15c$1@trex.antw.online.be>`
- **References:** `<7v7brc$3i$1@trex.antw.online.be> <7v7hr2$q2t$1@aklobs.kc.net.nz> <3818490A.23E01047@zip.com.au>`

```
my compiler doesn't support that

Ken Foskey heeft geschreven in bericht <3818490A.23E01047@zip.com.au>...
```

###### ↳ ↳ ↳ Re: assignment

_(reply depth: 4)_

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7velrc$oi2$1@uranium.btinternet.com>`
- **References:** `<7v7brc$3i$1@trex.antw.online.be> <7v7hr2$q2t$1@aklobs.kc.net.nz> <3818490A.23E01047@zip.com.au> <7va0v3$15c$1@trex.antw.online.be>`

```

xyz wrote in message <7va0v3$15c$1@trex.antw.online.be>...
>my compiler doesn't support that
>
>Ken Foskey heeft geschreven in bericht <3818490A.23E01047@zip.com.au>...
>


But the best method is to use the method
"CreateTimer" under class AbstractWindow
then keep on updating the textlabel with the new
time.

i.e.:


          invoke self "CreateTimer" using wsTimer        <---- pic x(04)
comp-5.

          move length of wstimer to StringLength

          invoke CharacterArray "WithLengthValue" using StringLength
                                                        wsTimer
                                              returning aString

          invoke oTimeLabelObject "SetLabel" using aString
          invoke aString "Finalize" returning aString


keep looping this or use register this as an idle object like I said before.

If your compiler doesn't support this, then I suggest you buy a new one.


Simon R Hart
Eaton, Ottery St. Mary, UK.
```

###### ↳ ↳ ↳ Re: assignment

_(reply depth: 5)_

- **From:** "xyz" <Suze.V@online.be>
- **Date:** 1999-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vf6np$lf7$1@trex.antw.online.be>`
- **References:** `<7v7brc$3i$1@trex.antw.online.be> <7v7hr2$q2t$1@aklobs.kc.net.nz> <3818490A.23E01047@zip.com.au> <7va0v3$15c$1@trex.antw.online.be> <7velrc$oi2$1@uranium.btinternet.com>`

```
tnx, I'll try it, but I'm not sure my compiler is going to support that
```

###### ↳ ↳ ↳ Re: assignment

_(reply depth: 6)_

- **From:** "Keysers Wonne" <wonne@vanroey.be>
- **Date:** 1999-11-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vk2mk$7up$1@trex.antw.online.be>`
- **References:** `<7v7brc$3i$1@trex.antw.online.be> <7v7hr2$q2t$1@aklobs.kc.net.nz> <3818490A.23E01047@zip.com.au> <7va0v3$15c$1@trex.antw.online.be> <7velrc$oi2$1@uranium.btinternet.com> <7vf6np$lf7$1@trex.antw.online.be>`

```
nope: CA-realia sux big time!!!

xyz <Suze.V@online.be> schreef in berichtnieuws
7vf6np$lf7$1@trex.antw.online.be...
> tnx, I'll try it, but I'm not sure my compiler is going to support that
>
>
```

#### ↳ Re: assignment

- **From:** "Keysers Wonne" <wonne@vanroey.be>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7va4k8$2lg$1@trex.antw.online.be>`
- **References:** `<7v7brc$3i$1@trex.antw.online.be>`

```
dunno,
YET!!!

xyz <Suze.V@online.be> schreef in berichtnieuws
7v7brc$3i$1@trex.antw.online.be...
> I have a project for my school, and I have a problem.
>
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: assignment

- **From:** "xyz" <Suze.V@online.be>
- **Date:** 1999-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vf6np$lf7$2@trex.antw.online.be>`
- **References:** `<7v7brc$3i$1@trex.antw.online.be> <7va4k8$2lg$1@trex.antw.online.be>`

```
and meanwhile? :-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
