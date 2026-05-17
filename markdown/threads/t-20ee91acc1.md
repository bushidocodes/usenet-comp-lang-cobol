[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dialog/NetExpress Question

_3 messages · 3 participants · 1998-01_

---

### Dialog/NetExpress Question

- **From:** "bob..." <ua-author-47816@usenetarchives.gap>
- **Date:** 1998-01-21T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980122012201.UAA09295@ladder02.news.aol.com>`

```

Hi,

Could someone help me with the following question. In Dialog 2.5/3.0 the
Object Information Line (page 2-21 Ver. 2.5 guide) says that the position and
size of the selected object are shown in generic coordinates. They are not
pixels but are related to the standard system font for the environment in use.
If (0,0) is the top left corner of the screen what is the bottom right corner
of the screen ?

Thanks,

Bob Hennessey
```

#### ↳ Re: Dialog/NetExpress Question

- **From:** "red..." <ua-author-9624@usenetarchives.gap>
- **Date:** 1998-01-21T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-20ee91acc1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19980122012201.UAA09295@ladder02.news.aol.com>`
- **References:** `<19980122012201.UAA09295@ladder02.news.aol.com>`

```

On 22 Jan 1998 01:22:10 GMT, bob··.@a··.com (Bob7536) wrote:

› Hi,
› 
…[6 more quoted lines elided]…
› 

That will depend on the font. We had one heck of a time with that,
moving from machine to machine whacked it all up. We abandoned any
attempt to utilize or make any sense of it.
```

#### ↳ Re: Dialog/NetExpress Question

- **From:** "s..." <ua-author-13061530@usenetarchives.gap>
- **Date:** 1998-01-21T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-20ee91acc1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<19980122012201.UAA09295@ladder02.news.aol.com>`
- **References:** `<19980122012201.UAA09295@ladder02.news.aol.com>`

```

bob··.@a··.com (Bob7536) wrote:
› Hi,
› 
…[5 more quoted lines elided]…
› of the screen ?

Hi Bob,
Generic coordinates are indeed a scaling system based on the size of
the font. The bottom right coordinates will vary according to screen
size (as per normal pixel coordinates).

The font was used as typically, it varies with the screen size (ie a
larger screen size will often mean a larger font, although this isn't
*always* the case), and therefore the values used in any DS screenset for
size and position will scale accordingly. (Using pixels means that you
would get a hideously small window or button, say, when moving from a
640x480 to a 1024x768 screen).

The scaling used is thus: One typical font character will scale to
32x64 generic units. So the formula from pixels to generic coordinates
is (roughly, without adding rounding):
x-coords: (32 * x) / font-width
y-coords: (64 * y) / font-height
If your font size on a 480x640 screen is 8x16, this means that
the screen size is:
(32 * 480) / 8 = 1920 generic units,
(64 * 640) / 16 = 2560 generic units,

NB: With rounding, it is the equivalent of:
x-coords: ((64 * x) + font-width) / (2 * font-width)
y-coords: ((128 * y) + font-height) / (2 * font-height)

This scaling seemed to produce reasonable results across OS/2,
Windows and Motif, which were the original operating systems
for Dialog System. DS recommends that you try the screensets out
on other screen sizes, due to the varying ratios of font/screen
size available.

Panels2 (the underlying API for much of DS) has a conversion API
to do the conversion for you, and this is documented in Workbench
4.0 (Pf-Map-Coordinate-Space).

E-mail me if you've any further queries!

Hope that helps,
Steve.
Micro Focus.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
