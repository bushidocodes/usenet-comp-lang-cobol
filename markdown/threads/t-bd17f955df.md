[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu & Install Shield

_9 messages · 6 participants · 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu & Install Shield

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Sw6V3.238$zd3.23467@typhoon01.swbell.net>`

```
We're have a bit of trouble using Install Shield
with a FJ application. There are a handful of
FJ modules (about 10) that refuse to register.

If you're using the commercial version of Install
Shield (not the installation wrapper provided by
Fujitsu), we'd be very interested in your comments.

Thanks.
```

#### ↳ Re: Fujitsu & Install Shield

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38250518.162727448@news1.attglobal.net>`
- **References:** `<Sw6V3.238$zd3.23467@typhoon01.swbell.net>`

```
On Sat, 6 Nov 1999 21:40:32 -0600, "Jerry P" <bismail@bisusa.com>
wrote:

>We're have a bit of trouble using Install Shield
>with a FJ application. There are a handful of
…[5 more quoted lines elided]…
>

If I don't install using the Wrapper I get "COBOL97 Not properly
Installed".  I'd love to use something OTHER than the wrapper, but I
can't get it to work.  Is this the error you are seeing?

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Fujitsu & Install Shield

- **From:** Michael Smart <nightshade-nospam@ev1.net>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ES4nOPfonpBII13XXzQzjHAgzqd0@4ax.com>`
- **References:** `<Sw6V3.238$zd3.23467@typhoon01.swbell.net> <38250518.162727448@news1.attglobal.net>`

```
On Sun, 07 Nov 1999 04:51:56 GMT, thaneH@softwaresimple.com (Thane
Hubbell) wrote:

>If I don't install using the Wrapper I get "COBOL97 Not properly
>Installed".  I'd love to use something OTHER than the wrapper, but I
>can't get it to work.  Is this the error you are seeing?

That is the same error message that we are getting. The problem,
evidently, stems from the fact that FJ wants some specific entries in
the registry. If you look on your development machine under the key:

HKEY_LOCAL_MACHINE\Software\Fujitsu

you will see a plethora of listings that the FJ wrapper will install
on client machines. The trick, so far, seems to be to figure out how
to get those keys with the proper values in them without using the
supplied wrapper!

If you have any luck, let us know!

Michael
```

#### ↳ Re: Fujitsu & Install Shield

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<803t3u$nbb$1@neptunium.btinternet.com>`
- **References:** `<Sw6V3.238$zd3.23467@typhoon01.swbell.net>`

```

Jerry P wrote in message ...
>We're have a bit of trouble using Install Shield
>with a FJ application. There are a handful of
…[8 more quoted lines elided]…
>

Some modules will very rarely self register, firstly
make sure that no-other programs are running when you run
install shield.
If this still doesn't work you can do it manually.
I don't know if you have tried this but it should work, works every time for
me.

launch a DOS session inside windows.
change the directory to \windows\system

type: regsvr32 {moduleName} -c
without the brackets, it will reg all servers.


Simon R Hart
Eaton, Ottery St. Mary, UK.
```

##### ↳ ↳ Re: Fujitsu & Install Shield

- **From:** Michael Smart <nightshade-nospam@ev1.net>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uy8nOBpJJ0yKh5DDHUkVeaGw7GYG@4ax.com>`
- **References:** `<Sw6V3.238$zd3.23467@typhoon01.swbell.net> <803t3u$nbb$1@neptunium.btinternet.com>`

```
On Sun, 7 Nov 1999 12:58:23 -0800, "Simon R Hart"
<hart1@technologist.com> wrote:

>Some modules will very rarely self register, firstly
>make sure that no-other programs are running when you run
…[13 more quoted lines elided]…
>Eaton, Ottery St. Mary, UK.

In this case these particular files do not self-register. However, it
has become apparent that they are dependent upon other files. If you
are really interested in looking at the message these files generate,
try running RegSvr32 on the following file:

f3bibtrv.dll

File should be located in: C:\FSC\COBOL97 directory.
```

###### ↳ ↳ ↳ Re: Fujitsu & Install Shield

- **From:** "Tom" <someone@microsoft.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZENV3.53054$YB4.1390142@typ12.nn.bcandid.com>`
- **References:** `<Sw6V3.238$zd3.23467@typhoon01.swbell.net> <803t3u$nbb$1@neptunium.btinternet.com> <uy8nOBpJJ0yKh5DDHUkVeaGw7GYG@4ax.com>`

```
I've done install shield for a bit and if you know where you want to put the
values in the registry its a simple call in install shield.  Variables in
the installation are no real chore either.
However my personal opinion with install shield is to go through the
training first, it is not a tool, it is its own language (albeit very
similar to c) The idiosyncracies can drive you nuts. The training will save
more than its cost in wasted time.  OrangeBrain does some excellent training
from what I've been told.  I firmly believe that many screwed up PC's are
the result of improperly designed installations, and no installation
testing.

Tom

Michael Smart wrote in message ...
>On Sun, 7 Nov 1999 12:58:23 -0800, "Simon R Hart"
><hart1@technologist.com> wrote:
…[5 more quoted lines elided]…
>>I don't know if you have tried this but it should work, works every time
for
>>me.
>>
…[17 more quoted lines elided]…
>File should be located in: C:\FSC\COBOL97 directory.
```

###### ↳ ↳ ↳ Re: Fujitsu & Install Shield

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3827aa74.140735424@news1.attglobal.net>`
- **References:** `<Sw6V3.238$zd3.23467@typhoon01.swbell.net> <803t3u$nbb$1@neptunium.btinternet.com> <uy8nOBpJJ0yKh5DDHUkVeaGw7GYG@4ax.com> <ZENV3.53054$YB4.1390142@typ12.nn.bcandid.com>`

```
On Mon, 8 Nov 1999 22:44:13 -0600, "Tom" <someone@microsoft.com>
wrote:

>I've done install shield for a bit and if you know where you want to put the
>values in the registry its a simple call in install shield.  Variables in
…[7 more quoted lines elided]…
>testing.

Agreed.  However, these people know and use install shield (heck the
Fujitsu Wrapper is install shield) but they want to do more than the
limited wrapper allows.  Rather than have two installs, they want to
make their own.  The kicker?  Figuring out what Fujitsu wants
registered and with what values, APPARANTLY in what order.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Fujitsu & Install Shield

_(reply depth: 5)_

- **From:** "Tom" <someone@microsoft.com>
- **Date:** 1999-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gmUV3.53791$YB4.1422119@typ12.nn.bcandid.com>`
- **References:** `<Sw6V3.238$zd3.23467@typhoon01.swbell.net> <803t3u$nbb$1@neptunium.btinternet.com> <uy8nOBpJJ0yKh5DDHUkVeaGw7GYG@4ax.com> <ZENV3.53054$YB4.1390142@typ12.nn.bcandid.com> <3827aa74.140735424@news1.attglobal.net>`

```
Maybe im missing it then if its in installshield it should be in there.
It should be in the setup, not always clearly visible, but there.
Unless they are using custom dlls to do the install. Then we have a
different problem.
Thane,
   Just for my own education since I dont have that fujitsu, can you
possibly isolate the I.S, and zip it up to me. Or is there a non commercial
try before you buy ware that exhibits the same tendency?
I cant get to it til this weekend, but will definately look at it.  I have a
whole week coming of learning Foxpro in another city so have nights free, to
look over code. (keeps me out of trouble)
I set up an email for it.
You know the drop spam routine, NOSPAM@ORJUNKcobol@melee.net
When you email be sure to include a return email since I will probably have
questions.
Thanks
Thane Hubbell wrote in message <3827aa74.140735424@news1.attglobal.net>...
>On Mon, 8 Nov 1999 22:44:13 -0600, "Tom" <someone@microsoft.com>
>wrote:
>
>>I've done install shield for a bit and if you know where you want to put
the
>>values in the registry its a simple call in install shield.  Variables in
>>the installation are no real chore either.
>>However my personal opinion with install shield is to go through the
>>training first, it is not a tool, it is its own language (albeit very
>>similar to c) The idiosyncracies can drive you nuts. The training will
save
>>more than its cost in wasted time.  OrangeBrain does some excellent
training
>>from what I've been told.  I firmly believe that many screwed up PC's are
>>the result of improperly designed installations, and no installation
…[10 more quoted lines elided]…
>My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Fujitsu & Install Shield

_(reply depth: 6)_

- **From:** cbronni@aol.comcomorg.n (rumplestiltskinheadbangersandlox)
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991111013229.02577.00003029@ng-cn1.aol.com>`
- **References:** `<gmUV3.53791$YB4.1422119@typ12.nn.bcandid.com>`

```
Thane this is Tom again, my regular server is all out of sorts so im using a
nice friends isp.
 
I tried emailing and newsgrouping but no luck.  basically here's what I need.
Make a small program with the Fujitsu
1.  MessageBox "Hello World" genre. so I know program works on install.
2.  Make a file on C:\ that writes one record of anything.  I use it to check
time date stamps of installation tests.
Then I will detect before and after and see the differences on a clean install
machine.

One caveat, SOME companies (Borland and their IDE) make such a disaster of
installing things that they refuse to allow developers to modify it.  If thats
the case it will show itself out.  But it doesn't sound like it, just
complicated registry entries.

The goal of this is to get to a generic Install script that most can use.

you have my email addresss.
NO.JUNKL.net@NO.com.SPAMINALS@cobol@melee.netREMOVE@THE@GARBAGE.com

someone@microsoft.com  er.. wait is that someone@a itty bitty piece of the
microsoftmonopoly.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
