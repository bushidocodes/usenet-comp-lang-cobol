[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol Program in System Tray

_8 messages · 3 participants · 2007-07_

---

### Cobol Program in System Tray

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-07-03T23:14:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1183529679.754225.26270@i13g2000prf.googlegroups.com>`

```
Hi,

Browsed codes that will put a program into the System Stray (Windows
OS) when minimized... but it is in VB codes. Basically it uses Windows
API.

http://www.developerfusion.co.uk/show/98/

I'm not that familiar with VB. Maybe the link above doesn't do what I
wanted. My objective really is to put my Cobol program into the System
Tray when "minimized". Anyone?
```

#### ↳ Re: Cobol Program in System Tray

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-06T00:20:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f460cF3afkq4U1@mid.individual.net>`
- **References:** `<1183529679.754225.26270@i13g2000prf.googlegroups.com>`

```

"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:1183529679.754225.26270@i13g2000prf.googlegroups.com...
> Hi,
>
…[9 more quoted lines elided]…
>

Do you want it with or without a pop-up menu?

Not sure if you are seeing my posts; I suggested you use exception 
processing for your disconnection problem about 4 days before Jimmy posted 
the same solution (in more detail).

Don't get me wrong; I'm glad you solved it, and Jimmy's solution was fine, 
but there's no point me going into detail on this if you are not seeing my 
posts.

Pete.
```

##### ↳ ↳ Re: Cobol Program in System Tray

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-07-05T06:24:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1183641870.988356.218810@j4g2000prf.googlegroups.com>`
- **In-Reply-To:** `<5f460cF3afkq4U1@mid.individual.net>`
- **References:** `<1183529679.754225.26270@i13g2000prf.googlegroups.com> <5f460cF3afkq4U1@mid.individual.net>`

```
Yes, Pete I did respond to your comment... but the topic was suddenly
shifted to Judson that is why instead of looking at some of the posts,
I did some manipulation instead with the OLE exception coding on my
own. Thanks to the advise, actually after seeing it I did ask the same
query in Microfocus Forum and they answered me back the same... except
there was no coding, but mostly OLE exception documentations.

The query I have now is basically connected to the solved Cobol (soap)
program.

I want the program running in the background that is why I want it
running (continuously that is)... but minimized in the system tray. It
is a program in the background that is "throwing" data into the server
(using WSDL/Soap) in a continuous manner. So I think popup menu is not
needed in this case.

The objective now is at the initial boot (startup) of the PC, the
Cobol program will auto-execute... but directly minimized into the
system tray. Can we do this in Cobol?
```

###### ↳ ↳ ↳ Re: Cobol Program in System Tray

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-06T03:43:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f4hstF3bf0sbU1@mid.individual.net>`
- **References:** `<1183529679.754225.26270@i13g2000prf.googlegroups.com> <5f460cF3afkq4U1@mid.individual.net> <1183641870.988356.218810@j4g2000prf.googlegroups.com>`

```

"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:1183641870.988356.218810@j4g2000prf.googlegroups.com...
> Yes, Pete I did respond to your comment... but the topic was suddenly
> shifted to Judson that is why instead of looking at some of the posts,
…[17 more quoted lines elided]…
>
Yes, but it isn't simple.

If you code it using the Windows API it has some messy stuff in the 
structure it uses.(And there is some tedious code required)

Here is a very straightforward outline in VB. It shows everything you need 
to do if you use the Win API and is fairly easily "translatable" into OO 
COBOL. I could translate this into PowerCOBOL in about an hour, but I don't 
know how MF DIALOG currently works and you need to check events like form 
load, pass window handles and monitor WM_Messages.

http://vb-helper.com/howto_tray_icon.html

If you are running DotNET it is much simpler. In C# I can do it with around 
6 lines of code. (Most of that is ensuring that the icon disappears off the 
task bar into the system tray when minimized)

I could wrap this as a COM+ component you can invoke from COBOL and that 
would be a very simple solution for you.

Unfortunately, the wrapping I need to include in the .DLL so you can use it, 
is fairly non-trivial and I simply don't have the time at the moment. I also 
don't have time to explore how you set COM properties from MF COBOL and you 
would need to set some before invoking the method to minimise.

I suggest you try the MF forums and see if someone hasn't done this with MF 
COBOL already.

If you are really stuck and can't get it to work, let me know and I'll 
produce a COM+ component based on either COBOL or C# that does it. BUT, I 
can't do it before end of next week and you need to advise whether you are 
running DotNET or not.

Pete.
```

###### ↳ ↳ ↳ Re: Cobol Program in System Tray

_(reply depth: 4)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-07-05T16:27:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1183678061.493045.184870@i13g2000prf.googlegroups.com>`
- **In-Reply-To:** `<5f4hstF3bf0sbU1@mid.individual.net>`
- **References:** `<1183529679.754225.26270@i13g2000prf.googlegroups.com> <5f460cF3afkq4U1@mid.individual.net> <1183641870.988356.218810@j4g2000prf.googlegroups.com> <5f4hstF3bf0sbU1@mid.individual.net>`

```
Hi Pete,

Saw the link documention (and code) which is much simplier than the
one I searched. I am even thinking that I will just instead use VB
code to call my Cobol program... but again, got no Visual Studio (or
VB compiler) on my PC. MS licensing here requires a buck. I'm not
running .NET either.

In this case I do not use MF Dialog because all I wanted is simply
background processing with "DISPLAY" statement. The code below provide
how we create a "text-based" window in MF.


       special-names.
           call-convention 74 is winAPI.
               :
               :
               :
       01  wHwnd                   pic x(4) comp-5.
       01  wstatusCode             pic x(2) comp-5.
       01  wSetWindowTextReturn    pic x(4) comp-5.
               :
               :
               :
           CALL "PC_WIN_HANDLE" using wHwnd
                            returning wstatusCode

           CALL winAPI "SetWindowTextA"
            using by value wHwnd
              by reference z"SOAP: Title of the window"
                 returning wSetWindowTextReturn.
               :
               :
               :
           DISPLAY "blah-blah-blah"

           DISPLAY "process/process/process"

           DISPLAY "blah-blah-blah"

           DISPLAY "process/process/process".


It is just a simple WinAPI call that creates the window with a title
(window handle "wHwnd"). Within the window, probably I'm going to
display individual data that is being processed... or maybe an error
but nonetheless it will just only show things I needed to display. It
is purely simple ACCEPT, DISPLAY statement that it is going to be
viewed within that window.

I do not know how you could do it in Cobol but it is a good thing that
there is a way. I will wait for you... while maybe try to check
anything I could sniff on.
```

###### ↳ ↳ ↳ Re: Cobol Program in System Tray

_(reply depth: 5)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-07-05T20:17:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zoydnSa3RtG3OxDbnZ2dnUVZ_vXinZ2d@comcast.com>`
- **In-Reply-To:** `<1183678061.493045.184870@i13g2000prf.googlegroups.com>`
- **References:** `<1183529679.754225.26270@i13g2000prf.googlegroups.com> <5f460cF3afkq4U1@mid.individual.net> <1183641870.988356.218810@j4g2000prf.googlegroups.com> <5f4hstF3bf0sbU1@mid.individual.net> <1183678061.493045.184870@i13g2000prf.googlegroups.com>`

```
Rene_Surop wrote:
> I'm not running .NET either.

Not to speak for Pete, but Microsoft has free versions of C# and VB.NET 
(among others) available...

http://msdn.microsoft.com/vstudio/express/default.aspx

(The list of all the free "express" products goes down the left-hand 
side of the page, under the heading "Browse by Product".)
```

###### ↳ ↳ ↳ Re: Cobol Program in System Tray

_(reply depth: 6)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-07-10T23:05:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1184133920.962295.231660@e16g2000pri.googlegroups.com>`
- **In-Reply-To:** `<zoydnSa3RtG3OxDbnZ2dnUVZ_vXinZ2d@comcast.com>`
- **References:** `<1183529679.754225.26270@i13g2000prf.googlegroups.com> <5f460cF3afkq4U1@mid.individual.net> <1183641870.988356.218810@j4g2000prf.googlegroups.com> <5f4hstF3bf0sbU1@mid.individual.net> <1183678061.493045.184870@i13g2000prf.googlegroups.com> <zoydnSa3RtG3OxDbnZ2dnUVZ_vXinZ2d@comcast.com>`

```
Hi Pete,

Already worked it out with Microfocus Forum, they (David Sands) gave
me the sample Cobol code that I needed. They've supported my coding
since the time I used their MF NetExpress so I posted this topic to
them as well.
```

###### ↳ ↳ ↳ Re: Cobol Program in System Tray

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-12T00:04:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5fjva6F3c5u4fU1@mid.individual.net>`
- **References:** `<1183529679.754225.26270@i13g2000prf.googlegroups.com> <5f460cF3afkq4U1@mid.individual.net> <1183641870.988356.218810@j4g2000prf.googlegroups.com> <5f4hstF3bf0sbU1@mid.individual.net> <1183678061.493045.184870@i13g2000prf.googlegroups.com> <zoydnSa3RtG3OxDbnZ2dnUVZ_vXinZ2d@comcast.com> <1184133920.962295.231660@e16g2000pri.googlegroups.com>`

```

"Rene_Surop" <infodynamics_ph@yahoo.com> wrote in message 
news:1184133920.962295.231660@e16g2000pri.googlegroups.com...
> Hi Pete,
>
…[4 more quoted lines elided]…
>
Excellent! Glad you got it solved, and thanks for the note.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
