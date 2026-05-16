[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu PowerCOBOL and Picture Objects

_3 messages · 2 participants · 2001-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu PowerCOBOL and Picture Objects

- **From:** Jeff Campbell <jcampbell@ins-msi.com>
- **Date:** 2001-02-14T14:11:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A8A8CD5.ED3FE85B@ins-msi.com>`

```
I am trying to use a third party control, Videosoft's VSVIEW7, on a
PowerCOBOL form. I am using the VSprinter to preview some text. This
works fine.

My problem is: I want to add a company logo to the preview pages. The
VSprinter has a DrawPicture method which uses as one of it's arguments
a reference to a Visual Basic Picture Object.

My question: How can I include a Picture Object with a bit map from
the logo .BMP file? I looked at the Image Control but it doesn't have
a Picture property. 

Hopefully, someone can point me in the right direction.

TIA,

Jeff Campbell
n8wxs@arrl.net
```

#### ↳ Re: Fujitsu PowerCOBOL and Picture Objects

- **From:** "Paulo Vieira" <pvieira@emporsoft.pt>
- **Date:** 2001-02-15T10:06:04
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96g9s6$m67$1@venus.telepac.pt>`
- **References:** `<3A8A8CD5.ED3FE85B@ins-msi.com>`

```
Hi,
I've never worked with Videosoft's controls, but "Visual Basic Picture
Object" is probably a handle and not a file name.
Let's get to both scenarios:
A) You need to pass the name of a picture file to the control: simply use
the "ImageName" property of the Image control. This property references the
file name which contains your picture.
B) You need to pass the memory address of the control: (this is only a
guess) do a CALL "POWCONVTOOLE" using your image control and returning a OLE
HANDLE, and then pass that handle to the VS control. As I said, this is
guess work because I never tried it before.
By the way, this is only possible with Version 5.
regards,
Paulo Vieira, emporsoft

"Jeff Campbell" <jcampbell@ins-msi.com> wrote in message
news:3A8A8CD5.ED3FE85B@ins-msi.com...
> I am trying to use a third party control, Videosoft's VSVIEW7, on a
> PowerCOBOL form. I am using the VSprinter to preview some text. This
…[15 more quoted lines elided]…
> n8wxs@arrl.net
```

##### ↳ ↳ Re: Fujitsu PowerCOBOL and Picture Objects

- **From:** Jeff Campbell <jcampbell@ins-msi.com>
- **Date:** 2001-02-20T03:51:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A91E44B.326F2C7@ins-msi.com>`
- **References:** `<3A8A8CD5.ED3FE85B@ins-msi.com> <96g9s6$m67$1@venus.telepac.pt>`

```
Thanks for responding.

Paulo Vieira wrote:
> 
> Hi,
…[5 more quoted lines elided]…
> file name which contains your picture.

> B) You need to pass the memory address of the control: (this is only a
> guess) do a CALL "POWCONVTOOLE" using your image control and returning a OLE
> HANDLE, and then pass that handle to the VS control. As I said, this is
> guess work because I never tried it before.

Well, I don't know how to do this. As far as I can tell the image
control
in PowerCOBOL doesn't export it's image. That is I don't see an "image"
property that could be handed to another control as in:

  move "image" of image-control to "image" of another-image-control.

Even if it did export it I doubt it's memory layout is the same as a
visual basic picture object. So I wouldn't be able to:

  invoke vsprinter1 "DrawPicture" image of image-control ...

because the DrawPicture method wants a picture object reference as
it's argument.

> By the way, this is only possible with Version 5.

Opps, I forgot to include that I am using version 5.

> regards,
> Paulo Vieira, emporsoft

Thanks again for taking the time to respond.

Jeff Campbell
n8wxs@arrl.net

> 
> "Jeff Campbell" ?jcampbell@ins-msi.com? wrote in message
…[18 more quoted lines elided]…
> ? n8wxs@arrl.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
