[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# READ INTO (was: Re: Data conversion on READ (why not?))

_4 messages · 2 participants · 1999-11_

---

### Re: READ INTO (was: Re: Data conversion on READ (why not?))

- **From:** roadraat@aol.com (RoadRaat)
- **Date:** 1999-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991120154104.08843.00000543@ng-xa1.aol.com>`
- **References:** `<8144ee$n3u$1@news.hitter.net>`

```
>The larger question is whether I would intentionally hide
>a conversion of the data by using a READ INTO or show
>the conversion by using separate READ and MOVE. My
>preference would be to show the conversion.

That was the point of my original post.  I thought it would be cool to break up
my MOVEs to working storage so my W.S image of my input record would already be
converted to the data-type I needed, instead of reading into a W.S. image and
then MOVEing to ANOTHER W.S. (converted) image.

I guess you are indicating your preference for the latter approach?

RoadRaat
```

#### ↳ Re: READ INTO (was: Re: Data conversion on READ (why not?))

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<816ngp$2faq$1@news.hitter.net>`
- **References:** `<8144ee$n3u$1@news.hitter.net> <19991120154104.08843.00000543@ng-xa1.aol.com>`

```

RoadRaat wrote in message <19991120154104.08843.00000543@ng-xa1.aol.com>...
>>The larger question is whether I would intentionally hide
>>a conversion of the data by using a READ INTO or show
…[3 more quoted lines elided]…
>That was the point of my original post.  I thought it would be cool to
break up
>my MOVEs to working storage so my W.S image of my input record would
already be
>converted to the data-type I needed, instead of reading into a W.S. image
and
>then MOVEing to ANOTHER W.S. (converted) image.
>
>I guess you are indicating your preference for the latter approach?

Strictly speaking, my comment, above, does not pertain
to records with multiple fields.

However, on Nov 9, 1999, I posted comments in the thread
"Read versus Read Into and Write versus Write From"
where I expressed my preference for separate READ and
MOVE statements under certain cases, including conversion
of data.

Though you might not have seen, read, or remembered the
post, I felt that posting the same comments 8 days later was
too soon.
------------------
Rick Smith
```

##### ↳ ↳ Re: READ INTO (was: Re: Data conversion on READ (why not?))

- **From:** roadraat@aol.com (RoadRaat)
- **Date:** 1999-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991121004606.02132.00000660@ng-ff1.aol.com>`
- **References:** `<816ngp$2faq$1@news.hitter.net>`

```
>on Nov 9, 1999, I posted comments in the thread
>"Read versus Read Into and Write versus Write From"
>where I expressed my preference for separate READ and
>MOVE statements under certain cases, including conversion
>of data.

Oh, shucks, I missed those entirely.  This is exactly the subject I've been
interested in.  I think I marked the whole newsgroup as read in my newsreader
because I was tired of sifting through a couple of thou' posts.  I'm going to
see if I can get those back.

RoadRaat
```

##### ↳ ↳ Re: READ INTO (was: Re: Data conversion on READ (why not?))

- **From:** roadraat@aol.com (RoadRaat)
- **Date:** 1999-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991121131259.08838.00000739@ng-xa1.aol.com>`
- **References:** `<816ngp$2faq$1@news.hitter.net>`

```
>However, on Nov 9, 1999, I posted comments in the thread
>"Read versus Read Into and Write versus Write From"

Thanks for the tip, Rick.  For some reason my newsreader never gave me anything
at all from those posts, even when I go back and "list all".  I found the
thread using DejaNews.

I confess that that thread is largely way beyond my present understanding, but
it was fun to look at and it stretched me.  It gave me some ideas for
"breaking" my project.  It's fun to break things and to see what happens!  It
will clarify for me a lot of what you guys were talking about.

RoadRaat
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
