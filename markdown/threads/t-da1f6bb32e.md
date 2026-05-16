[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VSAM Question

_7 messages · 6 participants · 2001-07_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### VSAM Question

- **From:** "Fergus" <fergus.obrien@ie-technology.com>
- **Date:** 2001-07-20T15:43:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AIY57.18152$Fk7.167043@news.indigo.ie>`

```
Hi
Can some IBM mainframer tell me if this can be done.

I have an indexed VSAM file with the following key structure:

03 ACC-KEY.
     05 ACC-NUM       PIC 9(05).
     05 ACC-TYPE       PIC X(01).

ACC-TYPE can be one of four values and an ACC-NUM can only have one
associated ACC-TYPE (i.e. there cannot be a 12345A and a 12345B).

I need to check the existence of the ACCount on the file but I don't know
the ACC-TYPE.

In my program (COBOL BTW) I could write 4 READ statements that check for
each ACC-TYPE in turn until one is found.

e.g
MOVE 12345 TO ACC-NUM
MOVE 'A'       TO ACC-TYPE

READ FILE
IF STATUS = 23      (i.e. not found)

MOVE 'B'       TO ACC-TYPE
READ FILE
check STATUS
etc.

However, this seems to me to be rather inelegant.

Is there any way to read the file with the ACC-TYPE set to SPACES (LOW
VALUES?) and then to query the resulting returned record.  I can always
compare the ACC-NUM's to check if I have the right account.

I know I can do something similar in DL/1 (GET NEXT) but is there any
similar code for a read greater in COBOL.

TIA

Fergus
```

#### ↳ Re: VSAM Question

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2001-07-20T18:30:00+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.ggsmi00.pminews@news.wanadoo.es>`
- **References:** `<AIY57.18152$Fk7.167043@news.indigo.ie>`

```
On Fri, 20 Jul 2001 15:43:34 +0100, Fergus wrote:

>Hi
>Can some IBM mainframer tell me if this can be done.
…[12 more quoted lines elided]…
>

The START statement with the KEY NOT LESS clause permits this.

Just issue a START and a READ NEXT on this file and check if the read record
is the one you want.

Hope this helps,
Willem Clements
BrainBench MVP for COBOL II
http://www.brainbench.com
```

#### ↳ Re: VSAM Question

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-07-20T11:41:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9j9muq$ac0$1@slb6.atl.mindspring.net>`
- **References:** `<AIY57.18152$Fk7.167043@news.indigo.ie>`

```
If you have your ACCESS as DYNAMIC, you can do a START statement with your
type set to low-values and do "greater than".  This will get you the first
record that has that acct-num (*OR* the next acct-num).

I think that is what you want.
```

#### ↳ Re: VSAM Question

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-07-21T13:34:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rxf67.1896$ar1.6231@www.newsranger.com>`
- **References:** `<AIY57.18152$Fk7.167043@news.indigo.ie>`

```
Use START, then READ.

In article <AIY57.18152$Fk7.167043@news.indigo.ie>, Fergus says...
>
>Hi
…[42 more quoted lines elided]…
>
```

#### ↳ Re: VSAM Question

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 2001-07-22T13:12:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B5B259F.C7B47EF4@sprynet.com>`
- **References:** `<AIY57.18152$Fk7.167043@news.indigo.ie>`

```
Fergus wrote:
> 
> Hi
…[36 more quoted lines elided]…
> similar code for a read greater in COBOL.

My first question is, why even have ACC-TYPE as part of the key?
```

##### ↳ ↳ Re: VSAM Question

- **From:** ar656@freenet.carleton.ca (Luis Gomez-Almeida)
- **Date:** 2001-07-22T16:27:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9jfd0f$lm4$1@freenet9.carleton.ca>`
- **References:** `<AIY57.18152$Fk7.167043@news.indigo.ie> <3B5B259F.C7B47EF4@sprynet.com>`

```

Frank Swarbrick <infocat@sprynet.com> wrote in message
news:3B5B259F.C7B47EF4@sprynet.com...
> Fergus wrote:
> >
…[12 more quoted lines elided]…
> > I need to check the existence of the ACCount on the file but I don't
know
> > the ACC-TYPE.
> >
…[25 more quoted lines elided]…
>

Very important question. However, being a contractor I have been in numerous
places where reason seems to have abandoned them eons ago, so there is no
use to ask those (very important) questions. Thus, in the case of the person
asking the question, I would use "START."

Regards,
Luis
```

###### ↳ ↳ ↳ Re: VSAM Question

- **From:** "Fergus" <fergus.obrien@ie-technology.com>
- **Date:** 2001-07-22T21:40:14+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<U6I67.18712$Fk7.174905@news.indigo.ie>`
- **References:** `<AIY57.18152$Fk7.167043@news.indigo.ie> <3B5B259F.C7B47EF4@sprynet.com> <9jfd0f$lm4$1@freenet9.carleton.ca>`

```
Yep, it's a classic case of Luis' experience.  I also would not have used
the type in the key for its been done that way for eons and no amount of
logic is going to get in changed.

Thanks to those that helped.  I'll try the START, READ NEXT suggestion
tomorrow.

Fergus

"Luis Gomez-Almeida" <ar656@freenet.carleton.ca> wrote in message
news:9jfd0f$lm4$1@freenet9.carleton.ca...
>
> Frank Swarbrick <infocat@sprynet.com> wrote in message
…[19 more quoted lines elided]…
> > > In my program (COBOL BTW) I could write 4 READ statements that check
for
> > > each ACC-TYPE in turn until one is found.
> > >
…[15 more quoted lines elided]…
> > > VALUES?) and then to query the resulting returned record.  I can
always
> > > compare the ACC-NUM's to check if I have the right account.
> > >
…[6 more quoted lines elided]…
> Very important question. However, being a contractor I have been in
numerous
> places where reason seems to have abandoned them eons ago, so there is no
> use to ask those (very important) questions. Thus, in the case of the
person
> asking the question, I would use "START."
>
…[3 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
