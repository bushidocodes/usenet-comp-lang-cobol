[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# output question

_6 messages · 5 participants · 2005-05_

---

### output question

- **From:** funarcade@gmail.com
- **Date:** 2005-05-19T13:10:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1116533412.487952.42300@f14g2000cwb.googlegroups.com>`

```
Hi all,

How do you output a sequential file with a carriage return and line
feed at the end of each record.

Thank you for your help in advance
```

#### ↳ Re: output question

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-05-19T16:34:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<118pu6tcje7hf6e@corp.supernews.com>`
- **References:** `<1116533412.487952.42300@f14g2000cwb.googlegroups.com>`

```

<funarcade@gmail.com> wrote in message
news:1116533412.487952.42300@f14g2000cwb.googlegroups.com...
> Hi all,
>
> How do you output a sequential file with a carriage return and line
> feed at the end of each record.

It depends on the compiler. Some allow for
ORGANIZATION IS LINE SEQUENTIAL
to accomplish what you are requesting. Tell us
what compiler you are using and what OS then
someone may be able supply a definite answer.
```

#### ↳ Re: output question

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-05-19T20:35:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d6itam$9g5$1@peabody.colorado.edu>`
- **References:** `<1116533412.487952.42300@f14g2000cwb.googlegroups.com>`

```

On 19-May-2005, funarcade@gmail.com wrote:

> Hi all,
>
…[3 more quoted lines elided]…
> Thank you for your help in advance

What is your environment?
```

#### ↳ Re: output question

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-05-19T14:47:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1116539225.797983.153330@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1116533412.487952.42300@f14g2000cwb.googlegroups.com>`
- **References:** `<1116533412.487952.42300@f14g2000cwb.googlegroups.com>`

```
> How do you output a sequential file with a carriage return and line
> feed at the end of each record.

MOVE x"0D0A"       TO End-of-Record

(or LINE SEQUENTIAL if available as already mentioned).
```

##### ↳ ↳ Re: output question

- **From:** funarcade@gmail.com
- **Date:** 2005-05-20T12:11:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1116616269.474330.130890@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1116539225.797983.153330@o13g2000cwo.googlegroups.com>`
- **References:** `<1116533412.487952.42300@f14g2000cwb.googlegroups.com> <1116539225.797983.153330@o13g2000cwo.googlegroups.com>`

```
Thank you for all the responses.

I am not sure what compiler we are using.  The cobol software is Data
General I Cobol.  We are running cobol in dos under Windows 98.  To run
it in windows 98 we are using a software called Choice!  by Wildhare

http://www.wildharecomputers.com/company.htm
```

###### ↳ ↳ ↳ Re: output question

- **From:** "JJ" <jj@nospam.com>
- **Date:** 2005-05-22T22:57:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y6KdnaYNNK7h2wzfRVn-jQ@comcast.com>`
- **References:** `<1116533412.487952.42300@f14g2000cwb.googlegroups.com> <1116539225.797983.153330@o13g2000cwo.googlegroups.com> <1116616269.474330.130890@g47g2000cwa.googlegroups.com>`

```
ORGANIZATION IS LINE SEQUENTIAL in the SELECT should be what you need in DG 
ICOBOL.

You can also use ASSIGN TO DISPLAY "filename".


<funarcade@gmail.com> wrote in message 
news:1116616269.474330.130890@g47g2000cwa.googlegroups.com...
> Thank you for all the responses.
>
…[5 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
