[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Article on COBOL in Federal Computer Week

_10 messages · 6 participants · 2009-07_

---

### Article on COBOL in Federal Computer Week

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2009-07-17T16:38:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9-adne6RU52sfP3XnZ2dnUVZ_vSdnZ2d@earthlink.com>`

```
http://fcw.com/articles/2009/07/13/tech-cobol-turns-50.aspx

Talks about some strengths and weaknesss of COBOL vis-a-vis converting to 
other languages.
```

#### ↳ Re: Article on COBOL in Federal Computer Week

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2009-07-18T13:38:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ce1ioF26cr6bU1@mid.individual.net>`
- **References:** `<9-adne6RU52sfP3XnZ2dnUVZ_vSdnZ2d@earthlink.com>`

```
In article <9-adne6RU52sfP3XnZ2dnUVZ_vSdnZ2d@earthlink.com>,
	"Charles Hottel" <chottel@earthlink.net> writes:
> http://fcw.com/articles/2009/07/13/tech-cobol-turns-50.aspx
> 
> Talks about some strengths and weaknesss of COBOL vis-a-vis converting to 
> other languages. 
> 

I usally read these articles until I hit the logical falacy that invalidates
the whole premise of the article.  In this one it was: "Cobol simply can't
compete when it comes to displaying output in graphical form."  Just what is
it that makes COBOL not able to "compete when it comes to displaying output
in graphical form"?  Just because the current crop of COBOL programmers
don't do it (or just don't know how to do it) doesn't make it a shortcoming
of the language.  There are a number of ways in which COBOL can do GUI
output.  For the most part. the exact same way other languages do it, by
calling routines to create graphical objects.

bill
```

##### ↳ ↳ Re: Article on COBOL in Federal Computer Week

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-07-18T13:17:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h3t0nq12e1h@news3.newsguy.com>`
- **In-Reply-To:** `<7ce1ioF26cr6bU1@mid.individual.net>`
- **References:** `<9-adne6RU52sfP3XnZ2dnUVZ_vSdnZ2d@earthlink.com> <7ce1ioF26cr6bU1@mid.individual.net>`

```
Bill Gunshannon wrote:
> 
> I usally read these articles until I hit the logical falacy that invalidates
…[7 more quoted lines elided]…
> calling routines to create graphical objects.

For that matter, a great many applications these days display
graphical output by including an IMG element in the HTML they write to
their standard output stream, which is then delivered to a web
browser, which fetches the referenced data and displays the image.
COBOL certainly has no problem doing that.

It's particularly ironic, then, that Robinson's comment about
graphical output, which you quoted above, comes immediately after a
sentence about "Web-centric languages". There aren't many prominent
"Web-centric languages" - PHP, ASP, and JSP on the server side;
ECMAScript and Java (when used for applets) on the client side. Pretty
much everything else commonly used for web development is a
general-purpose language. This entire paragraph is pretty much nonsense.
```

###### ↳ ↳ ↳ Re: Article on COBOL in Federal Computer Week

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-07-18T14:13:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3eadaef-b813-4904-98f6-1d244f076285@d9g2000prh.googlegroups.com>`
- **References:** `<9-adne6RU52sfP3XnZ2dnUVZ_vSdnZ2d@earthlink.com> <7ce1ioF26cr6bU1@mid.individual.net> <h3t0nq12e1h@news3.newsguy.com>`

```
On Jul 19, 5:17 am, Michael Wojcik <mwoj...@newsguy.com> wrote:
> Bill Gunshannon wrote:
>
…[17 more quoted lines elided]…
> graphical output, which you quoted above, comes immediately after a

I started developing a Cobol Windows based container loading system
with an early release MF Cobol/2 2.5 in 1991. This had graphical
layout of the vessel and each bay, graphical representation of the
tanks and curves for the torsion and bending. It also could represent
terminal layouts so that one could drag-and-drop containers into the
bays. Later it had a 'helm view' perspective over the container load,
taking into account the draft and trim so that the horizon could be
drawn to ensure adequate view. Actually the helm view could be varied
so that a programmed series of these gave a flyby of the vessel.

> sentence about "Web-centric languages". There aren't many prominent
> "Web-centric languages" - PHP, ASP, and JSP on the server side;
> ECMAScript and Java (when used for applets) on the client side. Pretty
> much everything else commonly used for web development is a
> general-purpose language. This entire paragraph is pretty much nonsense.

I have had Cobol CGI programs since OS/2 with IBMs web server using MS
Cobol 4.5. The same code runs on Windows and Linux and is still used.
```

##### ↳ ↳ Re: Article on COBOL in Federal Computer Week

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-20T07:45:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<06t865pss52h21rdiv5nj7bns1gj9ogubn@4ax.com>`
- **References:** `<9-adne6RU52sfP3XnZ2dnUVZ_vSdnZ2d@earthlink.com> <7ce1ioF26cr6bU1@mid.individual.net>`

```
On 18 Jul 2009 13:38:32 GMT, billg999@cs.uofs.edu (Bill Gunshannon)
wrote:

>I usally read these articles until I hit the logical falacy that invalidates
>the whole premise of the article.  In this one it was: "Cobol simply can't
…[6 more quoted lines elided]…
>calling routines to create graphical objects.

"Just because the current crop of COBOL programmers don't do it" is
sufficient reason.  
```

###### ↳ ↳ ↳ Re: Article on COBOL in Federal Computer Week

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-07-20T17:33:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h43cqj11p49@news3.newsguy.com>`
- **In-Reply-To:** `<06t865pss52h21rdiv5nj7bns1gj9ogubn@4ax.com>`
- **References:** `<9-adne6RU52sfP3XnZ2dnUVZ_vSdnZ2d@earthlink.com> <7ce1ioF26cr6bU1@mid.individual.net> <06t865pss52h21rdiv5nj7bns1gj9ogubn@4ax.com>`

```
Howard Brazee wrote:
> On 18 Jul 2009 13:38:32 GMT, billg999@cs.uofs.edu (Bill Gunshannon)
> wrote:
…[12 more quoted lines elided]…
> sufficient reason.  

Sufficient reason for what? It's not sufficient to support the
argument's claim, as stated. And, in any case, it's not true - there
are COBOL applications that produce graphical output. (I have one
running right now on this machine.) And yes, it was written by a COBOL
programmer who is still working today, which presumably is enough for
"current crop" status.
```

###### ↳ ↳ ↳ Re: Article on COBOL in Federal Computer Week

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-21T09:03:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ilb65lv1l3on3gsme8e5na3u70nj3ovr1@4ax.com>`
- **References:** `<9-adne6RU52sfP3XnZ2dnUVZ_vSdnZ2d@earthlink.com> <7ce1ioF26cr6bU1@mid.individual.net> <06t865pss52h21rdiv5nj7bns1gj9ogubn@4ax.com> <h43cqj11p49@news3.newsguy.com>`

```
On Mon, 20 Jul 2009 17:33:39 -0400, Michael Wojcik
<mwojcik@newsguy.com> wrote:

>> "Just because the current crop of COBOL programmers don't do it" is
>> sufficient reason.  
>
>Sufficient reason for what? It's not sufficient to support the
>argument's claim, as stated. 

If CoBOL programmers don't do it, who would do it in CoBOL?   We can't
ignore the requirement that CoBOL programs need to be programmed by
CoBOL programmers.

>And, in any case, it's not true - there
>are COBOL applications that produce graphical output. (I have one
>running right now on this machine.) And yes, it was written by a COBOL
>programmer who is still working today, which presumably is enough for
>"current crop" status.

Agreed.

While the graphic programs I have written to print a logo out of
letters on band printers doesn't meet the standards used for this
discussion, there are platforms which aren't so limited.

Trouble is - in most (in my limited experience - all), mainframe shops
have CoBOL for the mainframe, and other languages for desktops, where
the graphics are done.    Speculating on the reason for this, I come
up with:

1.   The people with experience with graphics learned with "free"
tools such as Java, on the desktop.
2.   Experimenting with desktop graphics on the cheap involved using
their skills.
3.   Once a pilot program is working, it is easier to continue it than
to buy compilers and train users to use CoBOL.  
4.   There isn't much incentive to switch from Java to CoBOL anyway.

Notice how much of this is about programming and training and how
little of it is about the actual features of the language.
```

###### ↳ ↳ ↳ Re: Article on COBOL in Federal Computer Week

_(reply depth: 5)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2009-07-21T14:26:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gwp9m.34339$qM4.15378@newsfe01.iad>`
- **In-Reply-To:** `<5ilb65lv1l3on3gsme8e5na3u70nj3ovr1@4ax.com>`
- **References:** `<9-adne6RU52sfP3XnZ2dnUVZ_vSdnZ2d@earthlink.com> <7ce1ioF26cr6bU1@mid.individual.net> <06t865pss52h21rdiv5nj7bns1gj9ogubn@4ax.com> <h43cqj11p49@news3.newsguy.com> <5ilb65lv1l3on3gsme8e5na3u70nj3ovr1@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 20 Jul 2009 17:33:39 -0400, Michael Wojcik
> <mwojcik@newsguy.com> wrote:
…[23 more quoted lines elided]…
> 
Just for info, and I think you would need the patience of Job to do it, 
Net Express does have classes for pens and drawing surface; they include 
quick methods for the common shapes, circle, rectangle/square, triangle 
etc. But of course, when it comes to graphic programming, what they 
provide is only the appetizer/hors d'oeuvre.

Jimmy
```

###### ↳ ↳ ↳ Re: Article on COBOL in Federal Computer Week

_(reply depth: 5)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-07-28T12:57:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h4nh5n15j0@news1.newsguy.com>`
- **In-Reply-To:** `<5ilb65lv1l3on3gsme8e5na3u70nj3ovr1@4ax.com>`
- **References:** `<9-adne6RU52sfP3XnZ2dnUVZ_vSdnZ2d@earthlink.com> <7ce1ioF26cr6bU1@mid.individual.net> <06t865pss52h21rdiv5nj7bns1gj9ogubn@4ax.com> <h43cqj11p49@news3.newsguy.com> <5ilb65lv1l3on3gsme8e5na3u70nj3ovr1@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 20 Jul 2009 17:33:39 -0400, Michael Wojcik
> <mwojcik@newsguy.com> wrote:
…[8 more quoted lines elided]…
> CoBOL programmers.

Agreed, but clearly there's a difference between "COBOL programmers
don't do this today" and "COBOL programmers will never do this". I
don't think the article was that subtle; my reading of it was that the
author assumed that it was simply impossible to build such
applications in COBOL, regardless of what programmers were willing to try.

> Trouble is - in most (in my limited experience - all), mainframe shops
> have CoBOL for the mainframe, and other languages for desktops, where
…[12 more quoted lines elided]…
> little of it is about the actual features of the language.

Yes. People come to programming through many routes, but since the
rise of personal computers, I suspect relatively few have started with
COBOL. Many of the youngest generation of programmers probably started
with declarative markup (HTML) and ECMAScript (Javascript / JScript /
ActionScript), then learned web-back-end scripting languages like PHP,
ASP, and JSP.
```

###### ↳ ↳ ↳ Re: Article on COBOL in Federal Computer Week

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-07-28T13:00:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mkiu65d8fqm9r57l3c86qt9cnm4sruj0q6@4ax.com>`
- **References:** `<9-adne6RU52sfP3XnZ2dnUVZ_vSdnZ2d@earthlink.com> <7ce1ioF26cr6bU1@mid.individual.net> <06t865pss52h21rdiv5nj7bns1gj9ogubn@4ax.com> <h43cqj11p49@news3.newsguy.com> <5ilb65lv1l3on3gsme8e5na3u70nj3ovr1@4ax.com> <h4nh5n15j0@news1.newsguy.com>`

```
On Tue, 28 Jul 2009 12:57:10 -0400, Michael Wojcik
<mwojcik@newsguy.com> wrote:

>Yes. People come to programming through many routes, but since the
>rise of personal computers, I suspect relatively few have started with
…[3 more quoted lines elided]…
>ASP, and JSP.

And the accountant who was given a brand new tabulating machine to
work with is no longer in the work place.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
