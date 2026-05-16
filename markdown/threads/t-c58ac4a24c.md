[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Realia Cobol

_4 messages · 3 participants · 2006-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Realia Cobol

- **From:** Ray Bletko <rb@yahoo.com>
- **Date:** 2006-09-27T01:15:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns984ACD5D7E891rb@70.168.83.30>`

```
In taking over the responsibility for a machine with a Realia Cobol 
compiler, I have noticed that the output files from cobol programs have tab 
characters in them for spaces.  Would anyone know why this is happening and 
how to stop it.  Any help would be greatly appreciated.
```

#### ↳ Re: Realia Cobol

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-09-26T20:44:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12hjls4g9ashe50@news.supernews.com>`
- **References:** `<Xns984ACD5D7E891rb@70.168.83.30>`

```
Ray Bletko wrote:
> In taking over the responsibility for a machine with a Realia Cobol
> compiler, I have noticed that the output files from cobol programs
> have tab characters in them for spaces.  Would anyone know why this
> is happening and how to stop it.  Any help would be greatly
> appreciated.

It's part of the file definition.

SELECT OUT-FILE ASSIGN TO 'MYFILE.TXT[T]'...

The "T" on the end signifies TAB separators for text files in columns 1, 9, 
17, 25, 33, etc.

Two other choices are available:

   "[N]" = text file but truncate trailing spaces.
   "[U]" = text file bit trailing spaces are retained

You can stop it by recompiling the program with either an "N" or "U" in the 
file description.

You can also remove the tabs by copying the file using the Realia utility, 
viz:

REALCOPY   INFILE.TXT[T]   OUTFILE.TXT[N]

Realia permits oodles of other file types, too.
[V]ariable
[C]ompressed
[F]ixed length
[D] - Fixed length with delete byte
[R]elative
[B]yte stream
[X] - Indexed
```

##### ↳ ↳ Re: Realia Cobol

- **From:** Ray Bletko <rb@yahoo.com>
- **Date:** 2006-09-27T11:26:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns984B40C56AC7Frb@70.168.83.30>`
- **References:** `<Xns984ACD5D7E891rb@70.168.83.30> <12hjls4g9ashe50@news.supernews.com>`

```
"HeyBub" <heybubNOSPAM@gmail.com> wrote in
news:12hjls4g9ashe50@news.supernews.com: 

> Ray Bletko wrote:
>> In taking over the responsibility for a machine with a Realia Cobol
…[35 more quoted lines elided]…
> 

Thanks for the info, your reply is greatly appreciated
```

###### ↳ ↳ ↳ Re: Realia Cobol

- **From:** "Euromercante" <nospam_eurogest@euromercante.pt>
- **Date:** 2006-09-28T18:19:28+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<newscache$03cb6j$9nn$1@newsfront4.netvisao.pt>`
- **References:** `<Xns984ACD5D7E891rb@70.168.83.30> <12hjls4g9ashe50@news.supernews.com> <Xns984B40C56AC7Frb@70.168.83.30>`

```
Validate/write registers that would be in a server, acceded by Hi-Fi for
example.

Many thanks

"Ray Bletko" <rb@yahoo.com> wrote in message
news:Xns984B40C56AC7Frb@70.168.83.30...
> "HeyBub" <heybubNOSPAM@gmail.com> wrote in
> news:12hjls4g9ashe50@news.supernews.com:
…[41 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
