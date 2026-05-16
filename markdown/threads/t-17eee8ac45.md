[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL IN WINDOWS CE

_2 messages · 2 participants · 2000-05_

---

### COBOL IN WINDOWS CE

- **From:** "Rui Rocha" <rui.rocha@esoterica.pt>
- **Date:** 2000-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<959262899.789977@osiris.esoterica.pt>`

```
I have an application in netexpress 3.0 and i want to run this application
in windows ce. How can i do this?
I don't have any knowledge about one cobol compiler for windows ce

Can anyone help me?
```

#### ↳ Re: COBOL IN WINDOWS CE

- **From:** khansen@screenio.com (Kevin Hansen)
- **Date:** 2000-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392d9f01.682690346@wingate>`
- **References:** `<959262899.789977@osiris.esoterica.pt>`

```
On Thu, 25 May 2000 14:54:54 +0100, "Rui Rocha"
<rui.rocha@esoterica.pt> wrote:

>I have an application in netexpress 3.0 and i want to run this application
>in windows ce. How can i do this?
>I don't have any knowledge about one cobol compiler for windows ce
>
>Can anyone help me?

We haven't really looked at supporting CE, but if you subscribe to the
Microsoft Developer Network, you get the information for CE as part of
the package.

A quick perusal of my MSDN reveals the first problem; CE runs on a
variety of processors (not sure if any of them are Intel x86 although
they mentioned the possibility).  So, the first thing you'd need is a
compiler that generated object code for (each) target processor.

Second, CE is Unicode-only, which means that your application would
need to use a GUI that was also all Unicode.  Unicode, per se, is not
a big issue; we use Unicode where necessary in our product, but it
would take a little work to convert ALL of the Windows API stuff to
Unicode.  I don't see this as a huge issue in that the programming
interface could remain ANSI anyway (it has to be this way because I
don't think there are any Unicode COBOL compilers).

Third, CE is limited in application size (memory) and only supports a
subset of the Windows API.  It would take a bit of work for an
existing GUI provider to determine how hard it would be to do what
needed to be done with the limitations of the CE API.  

While developing your application on an Intel platform, you can run a
CE emulator on NT, but, again, this still doesn't address the object
code issue.  THAT is the biggest hurdle.

Until you find a COBOL compiler that will generate object code for the
various CE hardware platforms, it won't happen.

It would be kind of fun, though.

Kevin
NORCOM COBOL Programming Tools
GUI ScreenIO; a cool COBOL/Windows Screen Manager
http://www.ScreenIO.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
