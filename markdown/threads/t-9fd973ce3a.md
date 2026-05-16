[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Netexpress 3.0 and Crystal Report OCX

_2 messages · 2 participants · 1999-06_

---

### Netexpress 3.0 and Crystal Report OCX

- **From:** "tommy" <tommynilsen@yahoo.com>
- **Date:** 1999-06-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7j47s3$a3c$1@nntp.newmedia.no>`

```
Has anyone used the OCX-control that comes with Crystal Report 7.0 in
DialogSystem ??

Please let me know.

I can't get the "SetDataFiles" call to work.
I don't understand how to use the "object reference" data-type as input
parameter.

Tommy Nilsen
```

#### ↳ Re: Netexpress 3.0 and Crystal Report OCX

- **From:** Stephen.Biggs@merant.com (Steve Biggs)
- **Date:** 1999-06-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7j5jeh$cho$1@zutalors.mfltd.co.uk>`
- **References:** `<7j47s3$a3c$1@nntp.newmedia.no>`

```
"tommy" <tommynilsen@yahoo.com> wrote:
[Ref: Crystal Reports 7.0]
>I can't get the "SetDataFiles" call to work.
>I don't understand how to use the "object reference" data-type as input
>parameter.

Tommy,
What does Crystal Reports documentation say that the "DataFiles" 
property's type is?

It could be another type of object that Crystal Reports provides, in which 
case you need to find another method that creates or gives you back that 
type of object first (ie as an object reference).

Possibly, it could take an array or variant type. In which case, see our 
documentation on the "olesafea" (SafeArray) and "olevar" (Variant) classes 
in the Class Library Reference. If it is a variant, you might be able to 
get away with just using a basic data type, depending on how sophisticated 
the Crystal Reports component is.

(Whatever, you probably won't just be able to pass an uninitialized object 
reference: Crystal Reports is expecting *something*!)

Steve.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
