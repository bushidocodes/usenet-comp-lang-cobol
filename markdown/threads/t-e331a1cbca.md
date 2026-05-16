[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question:VB-COBOL data

_4 messages · 3 participants · 2003-04_

---

### Question:VB-COBOL data

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2003-04-23T15:29:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030423112906.18769.00000168@mb-m25.aol.com>`

```
I am trying to assist a co-worker with mapping VB data types to 
the various COBOL formats.  We are trying to write data directly 
to a Unisys ClearpathNX Series host.
The data format is a mixed bag of character  and Packed decimal
fields.  
I remember reading a thread or browsing a ZIP file that had a very detailed
explanation of the data types on each side and the equivalents.
I vaguely recall seeing a DLL provided that handled the conversion from 
one type to another.
Are there any specific locations that I could look to find additional
reference on how to deal with packed fields in particular?

I am certain that this might be better suited in a VB forum, but I have not yet

subscribed to any at this time.
```

#### ↳ Re: Question:VB-COBOL data

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-04-23T12:55:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b86k3501hjd@enews1.newsguy.com>`
- **References:** `<20030423112906.18769.00000168@mb-m25.aol.com>`

```
You'll likely get more expert response, but I can offer some
speculations.

> I am trying to assist a co-worker with mapping VB data types
to
> the various COBOL formats.  We are trying to write data
directly
> to a Unisys ClearpathNX Series host.

> The data format is a mixed bag of character  and Packed
decimal
> fields.

This mapping will not be as direct as one from VB to another
floating-point language, such as C.  In those languages,
numerics are represented a sum of 2-powered terms.  COBOL uses
a sum of 10-powered terms, so there will be some mathematic
imprecision involved in that translation.  (Small aside: Don't
overlook VB's decimal and currency types -- they're both fixed
point numeric types.)

Here is a link (picked from this group,) that covers a lot of
COBOL data considerations:
http://www.providerpaymentpartner.com/tsihome_html/downloads/C2
IEEE.htm

> I remember reading a thread or browsing a ZIP file that had a
very detailed
> explanation of the data types on each side and the
equivalents.
> I vaguely recall seeing a DLL provided that handled the
conversion from
> one type to another.

I would definitely suggest use a toolkit for this -- writing
your own logic will be expensive, and for no gains in code
library capital.  I looked at COBjects for making a data
conversion from a COBOL app to VB, but did not use it, so
cannot make a meaningful recommendation.  Hopefully others in
this group have some infantry-level experience.

http://www.ratrix.com/COBjects.htm

> Are there any specific locations that I could look to find
additional
> reference on how to deal with packed fields in particular?

> I am certain that this might be better suited in a VB forum,
but I have not yet
> subscribed to any at this time.

I would try: news://microsoft.public.vb.general.discussion
```

##### ↳ ↳ Re: Question:VB-COBOL data

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2003-04-23T21:28:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030423172859.18821.00000180@mb-m10.aol.com>`
- **References:** `<b86k3501hjd@enews1.newsguy.com>`

```
grinder,

Thanks for the reference links.  I'll definitely take a trip around the web
to review each of the locations you have pointed out.  Much of what you
have said makes sense.  Our shop is not real big on accepting outside
objects.  A lot of NIH mentality.  

In article <b86k3501hjd@enews1.newsguy.com>, "Grinder"
<grinder@no.spam.maam.com> writes:

>
>You'll likely get more expert response, but I can offer some
…[21 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Question:VB-COBOL data

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-23T22:05:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_6Epa.2897$%_3.2279158@newssrv26.news.prodigy.com>`
- **References:** `<20030423112906.18769.00000168@mb-m25.aol.com> <b86k3501hjd@enews1.newsguy.com>`

```
"Grinder" <grinder@no.spam.maam.com> wrote in message
news:b86k3501hjd@enews1.newsguy.com...
>
> Here is a link (picked from this group,) that covers a lot of
> COBOL data considerations:
> http://www.providerpaymentpartner.com/tsihome_html/downloads/C2
> IEEE.htm

Damn, first time I remember anyone actually citing that link. Kind of a
kick.

Yes, I do have a DLL kit, but it goes FROM COBOL to IEEE, not the other way.

To go *TO* COBOL best bet is to see if someone has a COBOL-written DLL you
can call.

MCM
(site owner, author of document)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
