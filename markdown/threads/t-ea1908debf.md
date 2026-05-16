[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# executable icons? Fujitsu 3

_2 messages · 2 participants · 1999-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### executable icons? Fujitsu 3

- **From:** "Barvin" <barvin@mwis.net>
- **Date:** 1999-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IYPS3.1367$UG4.14008@newsfeed.slurp.net>`

```
I've been seeing some Fujitsu users out here so if you're one I'd like to
know if you have created the executable to have your own icon (.ico) rather
than the globe icon of Fujitsu's ?
I've experimented with @iconDLL as well as @iconNAME with no success, though
I'm not clear on their purpose anyway as they are runtime variables, whereas
the program icon is created with the executable.
What am I missing?
```

#### ↳ Re: executable icons? Fujitsu 3

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381c7285.342163555@news1.attglobal.net>`
- **References:** `<IYPS3.1367$UG4.14008@newsfeed.slurp.net>`

```
On Sun, 31 Oct 1999 00:01:40 -0500, "Barvin" <barvin@mwis.net> wrote:

>I've been seeing some Fujitsu users out here so if you're one I'd like to
>know if you have created the executable to have your own icon (.ico) rather
>than the globe icon of Fujitsu's ?

Well, it's a bit of a Funky way to do it, but I do this:

Make an .rc file that contains the following:

#define ID_DEF               100

Icon ICON icon.ico


Put it in the same directory as your icon.ico file.

Run RC filename.rc

Then replace project.res with your new .res, naming it project.res.  

You will get your new icon.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
