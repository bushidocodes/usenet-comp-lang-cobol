[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Performance enhancement

_3 messages · 3 participants · 1997-09_

---

### Performance enhancement

- **From:** "rkri..." <ua-author-13460296@usenetarchives.gap>
- **Date:** 1997-09-25T12:04:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<875203440.31658@dejanews.com>`

```

Hi folks

I have a ISAM file. Which is the best method to process this file and
create an output file. Should the access method be sequential or indexed
or dynamic. Please help me in the same

Regards
Rajesh

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

#### ↳ Re: Performance enhancement

- **From:** "donts..." <ua-author-8744626@usenetarchives.gap>
- **Date:** 1997-09-25T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4cab1dd92d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<875203440.31658@dejanews.com>`
- **References:** `<875203440.31658@dejanews.com>`

```

On Thu, 25 Sep 1997 11:11:32 -0600, rkr··.@ik··n.com wrote:
› I have a ISAM file. Which is the best method to process this file and
› create an output file. Should the access method be sequential or indexed
› or dynamic. Please help me in the same

If you just want to convert the file structure then use the
appropriate utility: copy, convert, etc.

If you need to process the records on the way to output then I assume
you are going to write a COBOL program to do the job.

If you're going to process all or most of the records in the file,
then sequential in primary key order is fastest. If you're going to
process sections of the file, then dynamic is the answer, and if you
need to jump around then use random.

I once read that it's faster to process an entire file sequentially if
you're going to be hitting more than 4% of the records.

George Trudeau
```

##### ↳ ↳ Re: Performance enhancement

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1997-09-27T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4cab1dd92d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-4cab1dd92d-p2@usenetarchives.gap>`
- **References:** `<875203440.31658@dejanews.com> <gap-4cab1dd92d-p2@usenetarchives.gap>`

```

------------------ snip --------------------------------------
› If you're going to process all or most of the records in the file,
› then sequential in primary key order is fastest. If you're going to
› process sections of the file, then dynamic is the answer, and if you
› need to jump around then use random.
Actually, in some COBOL implementations, using some types of filesystems,
it is possible to read the records in sequential order without using keyed
read (e.g., in physical storage order, like reading the data portion of a
VSAM KSDS cluster as an ESDS dataset). This does apply to ISAM on some
platforms. If this is an option, then it is usually faster even than a
keyed order read. Of course, it is only useful if the speed of the
physical sequential read makes up for having to read the entire file.

› I once read that it's faster to process an entire file sequentially if
› you're going to be hitting more than 4% of the records.

4% may be a little low, and it depends on how you you have to access it,
but by the time you hit 20% you are almost certain of saving time. It also
depends on physical record size, since short records buffer better, and
hence enhance sequential read efficiency.

"There's a big difference between mostly dead, and all dead.  Please, open
his mouth."
    Miracle Max, "The Princess Bride"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
