[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Do Not Install Visual Studio 6.0 with Net Express 2.0

_4 messages · 3 participants · 1998-09_

---

### Do Not Install Visual Studio 6.0 with Net Express 2.0

- **From:** "Gene Webb" <gene.webb@newsguy.com>
- **Date:** 1998-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6shg2s$g2@enews1.newsguy.com>`

```
I installed Visual Studio 6.0 and all of my OO class libraries stopped
working with a run time error 114.    Uninstalling Visual Studio 6.0
corrects this problem.  I will post a resolution when I get it from
Microfocus.
```

#### ↳ Re: Do Not Install Visual Studio 6.0 with Net Express 2.0

- **From:** Ibis redibis numquam peribis <rrg10300@dasb.fhda.edu>
- **Date:** 1998-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.OSF.3.95q.980901193456.31804v-100000@octane.dasb.fhda.edu>`
- **References:** `<6shg2s$g2@enews1.newsguy.com>`

```


On Tue, 1 Sep 1998, Gene Webb wrote:

=> 
=> Listen to the experts they will tell you what can't be done, and why.
=  Then do it.
=> 
=> 
If I recall correctly, 
**********************
Herman Goldstine told the story of spending an
afternoon with John von Neuman and Alan Turing. Turing spent the time
arguing that a certain design Goldstine and von Neuman were testing would
fail because of signal to noise considerations. Goldstine and von Neuman
were convinced and when Julian Bigelow, the chief engineer on the project,
came into the room, they told him that the design would have to be
changed. Bigelow wished that they had told him sooner since he just got it
working.


rrg
================================================
To do the impossible you must see the invisible. 
================================================
```

#### ↳ Re: Do Not Install Visual Studio 6.0 with Net Express 2.0

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-glsZJx5d53Rr@Dwight_Miller.iix.com>`
- **References:** `<6shg2s$g2@enews1.newsguy.com>`

```
On Tue, 1 Sep 1998 18:56:12, "Gene Webb" <gene.webb@newsguy.com> 
wrote:

> I installed Visual Studio 6.0 and all of my OO class libraries stopped
> working with a run time error 114.    Uninstalling Visual Studio 6.0
> corrects this problem.  I will post a resolution when I get it from
> Microfocus.

This is the "Shared DLL" problem.  I bet  your MFC dll's (MicroSOFT 
foundation classes) got boogered up.
```

##### ↳ ↳ Re: Do Not Install Visual Studio 6.0 with Net Express 2.0

- **From:** "Gene Webb" <gene.webb@newsguy.com>
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6smj41$6kv@enews2.newsguy.com>`
- **References:** `<6shg2s$g2@enews1.newsguy.com> <Jl0PnHJ5PvPd-pn2-glsZJx5d53Rr@Dwight_Miller.iix.com>`

```
Not sure what the problem is, but I got a response from the AnswerLab from
Steve saying they had figured out what the problem was and would be placing
a fix on WebSync which will include a new runtime.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
