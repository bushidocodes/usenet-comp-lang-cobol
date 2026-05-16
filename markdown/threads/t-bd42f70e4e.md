[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Q: how to execute logic during precompiling phase ?

_6 messages · 4 participants · 1999-04_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Q: how to execute logic during precompiling phase ?

- **From:** "jeroen crabbe" <jeroen.crabbe@skynet.be>
- **Date:** 1999-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7etbdo$b10$1@news1.skynet.be>`

```

Hi all,

Does anybody know how to code a macro in Cobol so that it will execute
certain logic in the precompiler phase ? I know this is possible in PL/1 but
I don't know how to do it in Cobol. For example I would like to declare a
variable in the working storage of my cobol source which has its length
dynamically filled up during precompiling.  The length variable (&LENGHT in
the example) is the problem; where and how do I declare it and fill it up ?
I would initialize it with lets say 100.

In my cobol data structure I'd code something like this :

03    WS-VAR                 PIC    X(&LENGHT).

After precompiling the thing would have to look like this :

03    WS-VAR                 PIC    X(100).

If anyone knows what more you can do during precompiling, please let it be
known.

Thanks a lot,

Jeroentje
```

#### ↳ Re: how to execute logic during precompiling phase ?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f0eem$lma@dfw-ixnews4.ix.netcom.com>`
- **References:** `<7etbdo$b10$1@news1.skynet.be>`

```
For the information of the NG -
  I have sent some APS information to Jeroen - but because it included
fairly large "attachments" - I am not posting it to the NG.  If anyone else
is interested in getting the APS "solution" information - please email me
directly.
```

##### ↳ ↳ (APS-Cobol) how to execute logic during precompiling phase ?

- **From:** "jeroen crabbe" <jeroen.crabbe@skynet.be>
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f2vbb$vsa$1@news0.skynet.be>`
- **References:** `<7etbdo$b10$1@news1.skynet.be> <7f0eem$lma@dfw-ixnews4.ix.netcom.com>`

```

William M. Klein wrote in message <7f0eem$lma@dfw-ixnews4.ix.netcom.com>...
>For the information of the NG -
>  I have sent some APS information to Jeroen - but because it included
…[6 more quoted lines elided]…
>    wmklein at ix dot netcom dot com

Sorry for my late reply, but yesterday I was on a team event in Holland and
at work we don't have access to the net.

Well, there was no problem getting it working in APS-Cobol (Cobol generating
case tool), also the solution given for the Cobol itself worked fine
(REPLACE). In short in APS the solution to my question you gave was this :

In program section before NTRY you have to write this :

  SYM1    % &LENGTH = 100
  NTRY    CUSTCC * NORETRY

In working storage section :

  03  WF-TEST         X&LENGTH

After generation WF-TEST looked like :

  03 WF-TEST          X100


Thanks a lot, vielen Dank, merci beaucoup, dank u zeer,

Jeroentje.
```

###### ↳ ↳ ↳ Re: (APS-Cobol) how to execute logic during precompiling phase ?

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990415101716.11442.00001450@ng-ch1.aol.com>`
- **References:** `<7f2vbb$vsa$1@news0.skynet.be>`

```
wouldn't 03 WF-TEST          X100 give a compile error since it should look
like

03 WF-TEST          X(100).

Since I have never tried to change a WS field at compile time I was just
curious.  And wouldn't you have to recompile everytime you changed this field
definition?  I think you are probably looking for something that will change
the definition at runtime, and I am not sure this is possible.

TW
```

###### ↳ ↳ ↳ Re: (APS-Cobol) how to execute logic during precompiling phase ?

_(reply depth: 4)_

- **From:** "jeroen crabbe" <jeroen.crabbe@skynet.be>
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fga8d$nfp$1@news1.skynet.be>`
- **References:** `<7f2vbb$vsa$1@news0.skynet.be> <19990415101716.11442.00001450@ng-ch1.aol.com>`

```

Twymer wrote in message <19990415101716.11442.00001450@ng-ch1.aol.com>...
>wouldn't 03 WF-TEST          X100 give a compile error since it should look
>like
…[4 more quoted lines elided]…
>curious.  And wouldn't you have to recompile everytime you changed this
field
>definition?  I think you are probably looking for something that will
change
>the definition at runtime, and I am not sure this is possible.
>
>TW

The lines I wrote are in APS-Cobol, a casetool which generates Cobol. I
admit it looks very like the Cobol itself. It simplies life a bit for the
programmer (especially for writing reports, doing DB calls or writing online
stuff). It 's the thing they use in the bank I'm currently working for.

I was not asking for the field definition to change at runtime. I just
wanted to know how to do this rather simple thing because a friend/colleague
of mine was writing a program in which a lot of other field and table
definitions depended on the length of a field. Only while testing his
message processing program he would discover what the ideal (most
performant) length of that particular field would be (kind of trial and
error process). By using the solution I got, he can easily change every time
his length parameter, and all the other dependant fields will change also.
But it still means recompiling every time, as you said.

As for changing the definition at runtime, I wouldn't know myself if it were
possible. Could come in handy indeed. But I have to admit I 'm still a
newbee in Cobol myself, so I cannot help you out (yet).

Greetz,

Jeroentje.
```

#### ↳ Re: how to execute logic during precompiling phase ?

- **From:** "Luc DUVAL" <Luc.Duval@wanadoo.fr>
- **Date:** 1999-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f90a0$g0e$1@wanadoo.fr>`
- **References:** `<7etbdo$b10$1@news1.skynet.be>`

```
you must use the clause :


OCCURS DEPENDING ON ntimes.

ntimes is one element which contains one decimal value or one binary value.
The PLI macros are not used in COBOL language.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
