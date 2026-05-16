[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Mouse in MF 3.4

_2 messages · 2 participants · 2000-03_

---

### Mouse in MF 3.4

- **From:** "pmjones" <pmjones@netcomuk.co.uk>
- **Date:** 2000-03-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bb6qe$oq6$1@taliesin2.netcom.net.uk>`

```
One for the old MF hands ...

I've gone back in time to work on a character based "DOS box" application.
This application has no mouse control. I dug into my old examples, and
enabled the mouse via x"AF", so that (a) clicking within an ACCEPT "form"
will cause the cursor to move there (b) return LEFT mouse click as a value
when getting a keyboard char via x"AF"/27.

So far so good
- I have mouse control within a form
- I can detect a mouse when waiting for a key (cursor movement, eg PgUp, Rt
Arrow)
-- after the second I can read the word under the cursor and mimic the
desired key press

Yes, there is a question .....

Can any right mouse click be detected?

It would be a nice extra to
- have right click terminate an accept (and popup a context menu)
- be detected on getting a keyboard character

I don't want to use the CBL_ mouse routines, as this would be a huge
exercise. The application is about to get either an html or dialog front
end - this is a short term add-on, as I declared mouse control to be a
doddle given the way the application is written.

Any info appreciated !

Pete
```

#### ↳ Re: Mouse in MF 3.4

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38D92EFB.161A2A1F@home.com>`
- **References:** `<8bb6qe$oq6$1@taliesin2.netcom.net.uk>`

```


pmjones wrote:
> 
> One for the old MF hands ...
> 
Old, but comparatively 'young' when it comes to using M/F. You possibly
have the documentation I'm referring to - but I did post some M/F
on-line help text a while back - check it out on deja.com. Whether it
contains a feature to test the double-click I don't recall - still you
don't want to use the CBL_MOUSE routines - you are difficult to please
aren't you :-)

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
