[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol to Java migration

_7 messages · 7 participants · 2002-04_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Cobol to Java migration

- **From:** diogocalvario@clix.pt (Diogo Calvário)
- **Date:** 2002-04-01T02:12:50-08:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8b6dcb8b.0204010212.57b23ce6@posting.google.com>`

```
Hi

I would like to migrate a Cobol application to Java (EJB). Is there
any tool/framework/best practices out there (free or not)? Wich are
the best ones, in your experience?

Thank you

Diogo Calvï¿½rio
```

#### ↳ Re: Cobol to Java migration

- **From:** "Ira D. Baxter" <idbaxter@semdesigns.com>
- **Date:** 2002-04-01T08:05:20-06:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3ca866e5$1@giga.realtime.net>`
- **References:** `<8b6dcb8b.0204010212.57b23ce6@posting.google.com>`

```
We build highly automated translation tools for carrying out large scale
conversions.
They are almost always custom, because customers usually
have different starting points (OS, configuration, additional
applications and 3rd party packages) and always want
a fairly unique combination of the above as targets.
EJBs are probably a bit better, but even then the
question of *which* beans makes the result unique.

To see how our translation technology works,
see http://www.semdesigns.com/Products/DMS/Porting/Porting_files/frame.htm
The example shown is being done for a large
US defense contractor.
```

#### ↳ Re: Cobol to Java migration

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2002-04-01T16:17:02+01:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.000001aa.00e6402b@ieee.org>`
- **References:** `<8b6dcb8b.0204010212.57b23ce6@posting.google.com>`

```
Diogo,

> I would like to migrate a Cobol application to Java (EJB).

Is this something you want to do, or have to do? Cobol's pretty fast, and 
Java's pretty slow. I'm not sure if you'd like the result.

---

Doug

dwscott@ieee.org
```

#### ↳ Re: Cobol to Java migration

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-04-01T21:11:20+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<Y14q8.195471$2q2.16729477@bin4.nnrp.aus1.giganews.com>`
- **References:** `<8b6dcb8b.0204010212.57b23ce6@posting.google.com>`

```

"Diogo Calv�rio" <diogocalvario@clix.pt> wrote in message
news:8b6dcb8b.0204010212.57b23ce6@posting.google.com...
> Hi
>
> I would like to migrate a Cobol application to Java (EJB). Is there
> any tool/framework/best practices out there (free or not)? Wich are
> the best ones, in your experience?

COBOL  TO  Java? I've heard of many conversions going FROM Java to COBOL,
but not the reverse.

Oh well.
```

#### ↳ Re: Cobol to Java migration

- **From:** "Gianni Spano" <softline2000@tin.it>
- **Date:** 2002-04-05T06:57:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a5c3cd715ebabecc70ccf934310f9384.40368@mygate.mailgate.org>`
- **References:** `<8b6dcb8b.0204010212.57b23ce6@posting.google.com>`

```
"Diogo Calvï¿½rio" <diogocalvario@clix.pt> wrote in message
news:8b6dcb8b.0204010212.57b23ce6@posting.google.com...

> Hi
> 
…[6 more quoted lines elided]…
> Diogo Calvï¿½rio



Hi

There is a specific product named PERCOBOL from Legacyj.com.
Take a look at this web site: www.legacyj.com.
You  can download or request a demo to see how it works and
if can satisfy your needed.

Gianni 
```

##### ↳ ↳ Re: Cobol to Java migration

- **From:** Matthew Baulch <matt@greenroom.com.au>
- **Date:** 2002-04-09T14:45:02+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CB271CE.4080507@greenroom.com.au>`
- **References:** `<8b6dcb8b.0204010212.57b23ce6@posting.google.com> <a5c3cd715ebabecc70ccf934310f9384.40368@mygate.mailgate.org>`

```
Gianni Spano wrote:

> "Diogo Calvï¿½rio" <diogocalvario@clix.pt> wrote in message
> news:8b6dcb8b.0204010212.57b23ce6@posting.google.com...
…[22 more quoted lines elided]…
> Gianni 


Unfortunately, this product merely translates it to java code that can 
be executed by the JVM, which, if you are wanting to edit, is nearly 
impossible.

If you are looking for maintainable code on the other hand, i suggest 
re-writing it completely. Are you using OO cobol? if so it mightn't be 
so much work, but cobol '85 or less will be _HELL_ to try and convert. 
(In my experience anyway).

Cheers,
   -matt-
```

#### ↳ Re: Cobol to Java migration

- **From:** Sergio Sardo <sardo@migra.it>
- **Date:** 2002-04-07T10:32:29+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1d00bu4ut8tng6jadstls68pf35rsfp4c2@4ax.com>`
- **References:** `<8b6dcb8b.0204010212.57b23ce6@posting.google.com>`

```
On 1 Apr 2002 02:12:50 -0800, diogocalvario@clix.pt (Diogo Calvï¿½rio)
wrote:

>Hi
>
…[6 more quoted lines elided]…
>Diogo Calvï¿½rio

Hi, Diogo,
 there are good tools for Cobol-To-Java migration, even if in many
cases it needs quite good knowledge either of original application,
either of Java structures.

We could offer tools, but also the migration as a service done by us
with a few Customer's interventions (mainly by Q&A).
 If you're interested, please send us an e-mail!

Best Regards

Sergio

< ing. Sergio Sardo >
< Migra Software Evolution s.r.l. - Italy >
< sardo@migra.it - http://www.migra-se.it - +39+348.4127320>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
