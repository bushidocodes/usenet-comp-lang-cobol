[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Printing BMP using PCL

_1 message · 1 participant · 1998-06_

---

### Re: Printing BMP using PCL

- **From:** MJHOPKI@ertltoys.com
- **Date:** 1998-06-24T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<6ms07a$rsh$1@nnrp1.dejanews.com>`
- **References:** `<898183583.11041.0.nnrp-01.9e98ccda@news.demon.co.uk>`

```

I have done something similar by doing the following:

1. Print the logo from a windows application and send the output to a file.
2. Open this file in your cobol program, reading each record and writing it to
the printer.

You will have to be careful to treat the file as binary sequential.  Using
the proper esc sequences you should then be able to write other data around,
under, and over the logo.  The drawback to this technique is that you need to
know the printer type and thus have a generated "logo print file" for each
printer required.

In article <898183583.11041.0.nnrp-01.9e98ccda@news.demon.co.uk>,
  "Domenyk Newman" <Domenyk.Newman@spammy.MCL-Group.com> wrote:
>
> Does anyone know of a way of printing BMP's (ie a logo) by converting to PCL
…[4 more quoted lines elided]…
>


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/   Now offering spam-free web-based newsreading
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
