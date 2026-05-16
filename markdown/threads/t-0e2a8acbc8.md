[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetCobol - API Call

_6 messages · 4 participants · 2002-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### NetCobol - API Call

- **From:** "R. Hendriks" <R.Hendriks_1@kub.nl>
- **Date:** 2002-06-22T14:56:10+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<af1s2m$k2u$1@mailnews.kub.nl>`

```
Hi there,

I've downloaded the API-Guide (allapi.net) and am trying to figure out how
to make api calls from fujitsu's netcobol. It just can't get it to work. The
project builder always gives the error that it has an unresolved external.
I've inserted the user32.lib file in the project so it should find the
function (here the SetClipBoardDataA function). I think there's a problem
with the arguments I pass with the api call. I haven't been able to find a
good description of API calls in Fujitsu's documentation (just to examples
and that's not enough).

Does anyone have a good reference for me? Thanx.

Rik Hendriks
```

#### ↳ Re: NetCobol - API Call

- **From:** "Gianni Spano" <softline2000@tin.it>
- **Date:** 2002-06-22T14:41:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<417183aae5340ebbaf0a1fc0de8e4307.40368@mygate.mailgate.org>`
- **References:** `<af1s2m$k2u$1@mailnews.kub.nl>`

```
Hi Rik,

You probably need to put the string "ALPHAL(WORD)" on the script 
properties of project (down the form name, tipically Mainform).
I use continuously Api call using Powercobol and it is easy to do.
If you need something, let me know.
Do you need to call the "SetClipBoardDataA" function?
Send me you project and i will take a look.
I'm preparing a sort of "Api Superbible for Powercobol".
When it will finished i will post a message on the forum.

Gianni




"R. Hendriks" <R.Hendriks_1@kub.nl> wrote in message
news:af1s2m$k2u$1@mailnews.kub.nl

> Hi there,
> 
…[11 more quoted lines elided]…
> Rik Hendriks
```

##### ↳ ↳ Re: NetCobol - API Call

- **From:** "R. Hendriks" <R.Hendriks_1@kub.nl>
- **Date:** 2002-06-22T19:41:24+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<af2cqe$pfp$1@mailnews.kub.nl>`
- **References:** `<af1s2m$k2u$1@mailnews.kub.nl> <417183aae5340ebbaf0a1fc0de8e4307.40368@mygate.mailgate.org>`

```
Giannai,

I have indeed inserted the ALPHAL(WORD) option at the start of the problem.
I'm currently not using PowerCOBOL but the normal compiler to create a test
.dll file. The program works fine since the compiler reports no errors. Also
at this moment, I can built a .dll file using the WINLINK, but the COBOL97
project manager is still reluctant to build my file. When I call the .dll
file using a call from powercobol (i've added the .lib file to the project)
I get the error "the file main.exe is connected to unknow output
keybevent.dll:keybevent". This I should be able to resolve.

I'm testing out the copy-paste functionality and therefor need the
SetClipBoardData. As far a I know there's no built in copy-paste function in
PowerCOBOL. I'm a little bit inexperienced with NetCOBOL and am now in the
process of learning as much as possible.

I've looking forward to your Superbible of the api functions. Can you sent
me an email when you've finished it, or perhaps need someone to give you an
opinion on it? My mailaddress is R.Hendriks_1@kub.nl        .

Rik Hendriks

"Gianni Spano" <softline2000@tin.it> wrote in message
news:417183aae5340ebbaf0a1fc0de8e4307.40368@mygate.mailgate.org...
> Hi Rik,
>
…[19 more quoted lines elided]…
> > I've downloaded the API-Guide (allapi.net) and am trying to figure out
how
> > to make api calls from fujitsu's netcobol. It just can't get it to work.
The
> > project builder always gives the error that it has an unresolved
external.
> > I've inserted the user32.lib file in the project so it should find the
> > function (here the SetClipBoardDataA function). I think there's a
problem
> > with the arguments I pass with the api call. I haven't been able to find
a
> > good description of API calls in Fujitsu's documentation (just to
examples
> > and that's not enough).
> >
…[8 more quoted lines elided]…
> Posted via Mailgate.ORG Server - http://www.Mailgate.ORG
```

###### ↳ ↳ ↳ Re: NetCobol - API Call

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-06-22T19:12:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7_3R8.348917$Gs.27008080@bin5.nnrp.aus1.giganews.com>`
- **References:** `<af1s2m$k2u$1@mailnews.kub.nl> <417183aae5340ebbaf0a1fc0de8e4307.40368@mygate.mailgate.org> <af2cqe$pfp$1@mailnews.kub.nl>`

```

"R. Hendriks" <R.Hendriks_1@kub.nl>
>
> I'm testing out the copy-paste functionality and therefor need the
> SetClipBoardData. As far a I know there's no built in copy-paste function
in
> PowerCOBOL. I'm a little bit inexperienced with NetCOBOL and am now in the
> process of learning as much as possible.
>

But copy-paste is part of Windows. Do you need to read the clipboard under
program control?

If the user just wants to move text about, there's no need for you to do
anything in your program.
```

###### ↳ ↳ ↳ Re: NetCobol - API Call

_(reply depth: 4)_

- **From:** "R. Hendriks" <R.Hendriks_1@kub.nl>
- **Date:** 2002-06-23T12:06:11+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<af46ii$ean$1@mailnews.kub.nl>`
- **References:** `<af1s2m$k2u$1@mailnews.kub.nl> <417183aae5340ebbaf0a1fc0de8e4307.40368@mygate.mailgate.org> <af2cqe$pfp$1@mailnews.kub.nl> <7_3R8.348917$Gs.27008080@bin5.nnrp.aus1.giganews.com>`

```
Sorry about the copy-paste api call. I was under the impression that I had
to hard code this functionality. I've checked whether CTRL-C and CTRL-V
worked just like that (put two textboxes on a form and ran it). Don't know
what I did wrong then, but it works fine. No need for the SetClipBoardData
know. Perhaps in the future when moving objects.

Conclusion: basic copy-paste functionality is indeed build-it!


"JerryMouse" <nospam@bisusa.com> wrote in message
news:7_3R8.348917$Gs.27008080@bin5.nnrp.aus1.giganews.com...
>
> "R. Hendriks" <R.Hendriks_1@kub.nl>
> >
> > I'm testing out the copy-paste functionality and therefor need the
> > SetClipBoardData. As far a I know there's no built in copy-paste
function
> in
> > PowerCOBOL. I'm a little bit inexperienced with NetCOBOL and am now in
the
> > process of learning as much as possible.
> >
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: NetCobol - API Call

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-06-23T11:31:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PkiR8.3461$bt.1365@nwrddc04.gnilink.net>`
- **References:** `<af1s2m$k2u$1@mailnews.kub.nl> <417183aae5340ebbaf0a1fc0de8e4307.40368@mygate.mailgate.org> <af2cqe$pfp$1@mailnews.kub.nl> <7_3R8.348917$Gs.27008080@bin5.nnrp.aus1.giganews.com> <af46ii$ean$1@mailnews.kub.nl>`

```
R. Hendriks <R.Hendriks_1@kub.nl> wrote in message
news:af46ii$ean$1@mailnews.kub.nl...
> Sorry about the copy-paste api call. I was under the impression that I had
> to hard code this functionality. I've checked whether CTRL-C and CTRL-V
…[4 more quoted lines elided]…
> Conclusion: basic copy-paste functionality is indeed build-[in]!

Yes, it is; however, some applications may subclass the edit controls (text
boxes) and disable it. For applications you create, you must go out of your
way to do so.

That is, if you want to use ctrl-c, ctrl-v to provide data transfer between
your applications, it will work 'no muss, no fuss, no bother'; but you need
to test if you want to use one of your applications and another application.

(That said, I've only seen a handful of applications where it does not
work).

(Also, this tells you that if you want to disable "built in copy-paste" it
is doable.)

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
