[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Find and replace a record???

_3 messages · 3 participants · 1998-03_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Find and replace a record???

- **From:** "david ruth" <ua-author-3204429@usenetarchives.gap>
- **Date:** 1998-03-27T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fi26n$cp8@bgtnsc02.worldnet.att.net>`

```

Hi again,

I'm still working on a school project and I'm looking for a method to find a
specific record in a file and write over that record. I am laso looking for
a way to make a space and enter another record. We haven't hit this in
class yet, so I'm not sure these functions are something I'll be able to use
in this project. I haven't found this in my fundamental textbook. I have
had good luck in this newgroup clarifing the portions of the textbook that
are unclear.

David Ruth
```

#### ↳ Re: Find and replace a record???

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-03-27T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d39cb31be3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6fi26n$cp8@bgtnsc02.worldnet.att.net>`
- **References:** `<6fi26n$cp8@bgtnsc02.worldnet.att.net>`

```

David Ruth wrote:
›
› Hi again,
›
› I'm still working on a school project and I'm looking for a method to find a
› specific record in a file and write over that record.

You mean the record already exists and you want to REWRITE it? What
kind of format is the file whose record you want to REWRITE? Does your
platform allow for alteration of the primary key during a REWRITE?

Look at the all-caps word... then RTFM.

DD
```

#### ↳ Re: Find and replace a record???

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1998-03-28T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d39cb31be3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6fi26n$cp8@bgtnsc02.worldnet.att.net>`
- **References:** `<6fi26n$cp8@bgtnsc02.worldnet.att.net>`

```

David Ruth wrote in article
<6fi26n$c.··.@bgt··t.net>...
› Hi again,
› 
…[14 more quoted lines elided]…
› 
Since some basics on REWRITEing records has already been offered, I'd like
to add that the technique varies considerably depending on what sort of
file (sequential, indexed, relative, byte stream...), what
platform/compiler, what file manager/organization
(QSAM/VSAM/BDAM/BTRIEVE/MF-INDEX/etc.), how your replacement relates to
your original (length, key, etc.), and a few other things you need to
discover for yourself. You really need to be a great deal more specific
about some of these obvious things if you want a better reference that
RTFM.

Gary Lee nsp··.@map··m.com (Remove the spam filters, etc.)
"There's a big difference between mostly dead, and all dead. Please, open
his mouth."
Miracle Max, "The Princess Bride"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
