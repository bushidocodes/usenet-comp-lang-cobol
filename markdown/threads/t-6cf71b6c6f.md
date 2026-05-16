[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Looking for tool to create/generate screen-sections (screen painter?)

_22 messages · 11 participants · 2002-11 → 2002-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Looking for tool to create/generate screen-sections (screen painter?)

- **From:** "G���nther De Vogelaere" <Gunther.DeVogelaere@killspammersrug.ac.be>
- **Date:** 2002-11-28T18:02:10+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<as5ho3$99c$1@gaudi2.rug.ac.be>`

```
Hello,

I'm looking for a tool to create/generate text-based screensections.

I use Microfocus Netexpress 3.1.11 Service Pack 1 and it seems that such a
tool (DSCH.exe or MicroFocus Dialog System) is  included but it generates
copy-books and 'screens' that only can be used with a call to their 'dialog
system runner'-thingy. Maybe I'm doing something horribly wrong in the
DSCH.exe-tool.

I don't want to use their system in order to be able to generate code that
also will work in a non-microfocus environment (so only accept/display of
screens).

Maybe an old, pre-windows version of this DSCH.exe would do the trick? Can
somebody tell me where I could find/ download such a tool?

Thx,
G�nther De Vogelaere

Please eliminate kill spammers to reply.
```

#### ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-11-28T19:06:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DE66C6D.B8F6C9F7@shaw.ca>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be>`

```


"Gï¿½nther De Vogelaere" wrote:

> Hello,
>
…[18 more quoted lines elided]…
> Please eliminate kill spammers to reply.

Bearing in mind that the DOS Text Screen Section you are using is NOT yet part
of the Standard, (but an updated 'version' will be when COBOL 2002 is issued),
you are kind of stuck. Micro Focus has its own Screen Section, but other than
somebody else confirming, I doubt it currently parallels what is available,
say, in Fujitsu Screen Section.

It may well be compatible with Fujitsu if you ignore the M/F Screen Attributes
and Mouse routines. M/F Screen Section also contains the 'occurs feature' for
repetitive lines for tables. Then of course if you want to get into other
'environments', Liant(RM/COBOL), AcuCOBOL etc. - how do they currently handle
Screen Section ?

It really seems hardly worth the effort - but if you can get an old DOS screen
painter like Saywhat? or Software Bottling Company, (although probably both are
out of business) - these 'paint' pretty pictures in colours. To be 'generic'
you would have to restrict yourself to the simple ANSI  'accept field' or
'display field' - coupled with getting those accepts/displays to line up with
your painted screen. You sure you want to go to all this effort ?

Simple answer - determine which compiler you are going to use to earn your
bread and butter and use their appropriate Screen Section features.

Portability in COBOL is a big "killer" and not just the Screen Section. Don't
assume, having got something to work in compiler X it will happily compile when
you give it to compilers Y and Z - you will get REAMS of compiler errors ! You
are probably not aware, but Net Express, (and same applies to Fujitsu), already
contain many of the new features which will be in COBOL 2002  - but currently
you will get errors switching between compilers.

If you are trying to hedge your bets and Screen portability is a big issue the
best route for you to go would be Flexus SP2 or Norcom's Screen IO. Both
converse happily with a large number of COBOL compilers - you merely supply
parameters to their packages. They have the added bonus, you are programming in
straightforward COBOL syntax and they produce the results for you in Windows
format. (Both packages work with Micro Focus and Fujitsu products).

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

- **From:** "G���nther De Vogelaere" <Gunther.DeVogelaere@killspammersrug.ac.be>
- **Date:** 2002-11-29T11:52:11+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<as7ge9$t8b$1@gaudi2.rug.ac.be>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca>`

```
Thx for your reply

> It really seems hardly worth the effort - but if you can get an old DOS
screen
> painter like Saywhat? or Software Bottling Company, (although probably
both are
> out of business) - these 'paint' pretty pictures in colours. To be
'generic'
> you would have to restrict yourself to the simple ANSI  'accept field' or
> 'display field' - coupled with getting those accepts/displays to line up
with
> your painted screen. You sure you want to go to all this effort ?


I wouldn't limit myself to the simple ANSI accept, display fields but I
would only use simple things like column, line.

>
> Simple answer - determine which compiler you are going to use to earn your
> bread and butter and use their appropriate Screen Section features.
>

I agree with you, but in my case I have to port quickly a bunch of programs,
some of them written in cobol,
others in IDMS (ADS) to oracle + cobol.
I have never used the dialog system of microfocus before but I have used
screens before.
Ideally, the application I'm looking for would allow me to copy the
screenoutputs from the terminal emulator and use them as a basis for my
screen sections.
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-11-29T17:49:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DE7ABE6.3AD4E673@shaw.ca>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <as7ge9$t8b$1@gaudi2.rug.ac.be>`

```


"Gï¿½nther De Vogelaere" wrote:

> Thx for your reply
>
…[26 more quoted lines elided]…
> screen sections.

From what you've written I doubt that Dialog System could be a serious
contender.
Firstly, there's the learning curve to use DS and then the problem of getting
your screens into DS format. Additionally DS is designed to have 'self contained
code' to validate fields etc., and automatically also draws off OO GUI classes
for support where necessary, plus it also an event driven process, i.e.,
Windows.

There's nothing wrong with DS as a tool, but it just doesn't seem to fit your
criteria of a quick 'importing' tool.

Your reference to IDMS (ADS) - any chance you can read from input source and
output line sequentials as dummy screen source ?. You would  still have to do
some editing of  the output to get your final result.

I believe it was 'Gazloo' who offered some other suggestions - might be worth
asking Micro Focus support for ideas.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

_(reply depth: 4)_

- **From:** "Timothy" <tim-antie.s_pam-hillock@rogers.com>
- **Date:** 2002-12-01T21:58:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xCvG9.193705$oRV.177128@news04.bloor.is.net.cable.rogers.com>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <as7ge9$t8b$1@gaudi2.rug.ac.be> <3DE7ABE6.3AD4E673@shaw.ca>`

```

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3DE7ABE6.3AD4E673@shaw.ca...
>
>
…[4 more quoted lines elided]…
> > > It really seems hardly worth the effort - but if you can get an old
DOS
> > screen
> > > painter like Saywhat? or Software Bottling Company, (although probably
…[3 more quoted lines elided]…
> > > you would have to restrict yourself to the simple ANSI  'accept field'
or
> > > 'display field' - coupled with getting those accepts/displays to line
up
> > with
> > > your painted screen. You sure you want to go to all this effort ?
…[5 more quoted lines elided]…
> > > Simple answer - determine which compiler you are going to use to earn
your
> > > bread and butter and use their appropriate Screen Section features.
> > >
> >
> > I agree with you, but in my case I have to port quickly a bunch of
programs,
> > some of them written in cobol,
> > others in IDMS (ADS) to oracle + cobol.
…[8 more quoted lines elided]…
> Firstly, there's the learning curve to use DS and then the problem of
getting
> your screens into DS format. Additionally DS is designed to have 'self
contained
> code' to validate fields etc., and automatically also draws off OO GUI
classes
> for support where necessary, plus it also an event driven process, i.e.,
> Windows.
>
> There's nothing wrong with DS as a tool, but it just doesn't seem to fit
your
> criteria of a quick 'importing' tool.
>
> Your reference to IDMS (ADS) - any chance you can read from input source
and
> output line sequentials as dummy screen source ?. You would  still have to
do
> some editing of  the output to get your final result.
>
> I believe it was 'Gazloo' who offered some other suggestions - might be
worth
> asking Micro Focus support for ideas.
>
> Jimmy, Calgary AB
>
I found an old DOS based Cobol Screen builder program that is Shareware from
1991.  It's on a 5 � floppy that I got to try out but never used.  I was
trying to build a screen for a friends business but only got as far as the
text portion and not the in/out.

This first part is the screen design. 80 x 24.

                             ONTARIO TRUCK PARTS
                                SUPPLIER LIST

COMPANY NAME:
STREET ADDRESS:
MAILING STATION 1:
MAILING STATION 2:
CITY:
PROV/STATE:           POSTAL CODE:              COUNTRY:

CONTACT NAME:
LAST:                          FIRST:                       INIT:
           PHONE:              EXT:           FAX:

BACKUP NAME:
LAST:                          FIRST:                       INIT:
           PHONE:              EXT:           FAX:

----------------------------------------------------------------------------
---

  TYPE OF PARTS: CODE:
                 DESCRIPTION:

F1 - ADD    F2 - READ   F3 - NEXT RECORD    F4 - UPDATE    F5 - MAIN MENU




This part is the code that is generated.  Is this what you are looking for?

000001* * * * * * * * * * * * * * * * * *
000011 01  OTPSL001-SCREEN.
000021* * * * * * * * * * * * * * * * * *
000031*
000041     05  OTPSL001-LINE-1.
000051         10  FILLER PIC X(20) VALUE "OTPSL001            ".
000061         10  FILLER PIC X(9) VALUE SPACES.
000071         10  FILLER PIC X(20) VALUE "ONTARIO TRUCK PARTS ".
000081         10  FILLER PIC X(31) VALUE SPACES.
000091*
000101     05  OTPSL001-LINE-2.
000111         10  FILLER PIC X(32) VALUE SPACES.
000121         10  FILLER PIC X(20) VALUE "SUPPLIER LIST       ".
000131         10  FILLER PIC X(28) VALUE SPACES.
000141*
000151     05  OTPSL001-LINE-3.
000161         10  FILLER PIC X(80) VALUE SPACES.
000171*
000181     05  OTPSL001-LINE-4.
000191         10  FILLER PIC X(20) VALUE "COMPANY NAME:       ".
000201         10  FILLER PIC X(60) VALUE SPACES.
000211*
000221     05  OTPSL001-LINE-5.
000231         10  FILLER PIC X(20) VALUE "STREET ADDRESS:     ".
000241         10  FILLER PIC X(60) VALUE SPACES.
000251*
000261     05  OTPSL001-LINE-6.
000271         10  FILLER PIC X(20) VALUE "MAILING STATION 1:  ".
000281         10  FILLER PIC X(60) VALUE SPACES.
000291*
000301     05  OTPSL001-LINE-7.
000311         10  FILLER PIC X(20) VALUE "MAILING STATION 2:  ".
000321         10  FILLER PIC X(60) VALUE SPACES.
000331*
000341     05  OTPSL001-LINE-8.
000351         10  FILLER PIC X(20) VALUE "CITY:               ".
000361         10  FILLER PIC X(60) VALUE SPACES.
000371*
000381     05  OTPSL001-LINE-9.
000391         10  FILLER PIC X(20) VALUE "PROV/STATE:         ".
000401         10  FILLER PIC X(20) VALUE "  POSTAL CODE:      ".
000411         10  FILLER PIC X(8) VALUE SPACES.
000421         10  FILLER PIC X(20) VALUE "COUNTRY:            ".
000431         10  FILLER PIC X(12) VALUE SPACES.
000441*
000451     05  OTPSL001-LINE-10.
000461         10  FILLER PIC X(80) VALUE SPACES.
000471*
000481     05  OTPSL001-LINE-11.
000491         10  FILLER PIC X(20) VALUE "CONTACT NAME:       ".
000501         10  FILLER PIC X(60) VALUE SPACES.
000511*
000521     05  OTPSL001-LINE-12.
000531         10  FILLER PIC X(20) VALUE "LAST:               ".
000541         10  FILLER PIC X(11) VALUE SPACES.
000551         10  FILLER PIC X(20) VALUE "FIRST:              ".
000561         10  FILLER PIC X(9) VALUE SPACES.
000571         10  FILLER PIC X(20) VALUE "INIT:               ".
000581*
000591     05  OTPSL001-LINE-13.
000601         10  FILLER PIC X(11) VALUE SPACES.
000611         10  FILLER PIC X(20) VALUE "PHONE:              ".
000621         10  FILLER PIC X(20) VALUE "EXT:           FAX: ".
000631         10  FILLER PIC X(29) VALUE SPACES.
000641*
000651     05  OTPSL001-LINE-14.
000661         10  FILLER PIC X(80) VALUE SPACES.
000671*
000681     05  OTPSL001-LINE-15.
000691         10  FILLER PIC X(20) VALUE "BACKUP NAME:        ".
000701         10  FILLER PIC X(60) VALUE SPACES.
000711*
000721     05  OTPSL001-LINE-16.
000731         10  FILLER PIC X(20) VALUE "LAST:               ".
000741         10  FILLER PIC X(11) VALUE SPACES.
000751         10  FILLER PIC X(20) VALUE "FIRST:              ".
000761         10  FILLER PIC X(9) VALUE SPACES.
000771         10  FILLER PIC X(20) VALUE "INIT:               ".
000781*
000791     05  OTPSL001-LINE-17.
000801         10  FILLER PIC X(11) VALUE SPACES.
000811         10  FILLER PIC X(20) VALUE "PHONE:              ".
000821         10  FILLER PIC X(20) VALUE "EXT:           FAX: ".
000831         10  FILLER PIC X(29) VALUE SPACES.
000841*
000851     05  OTPSL001-LINE-18.
000861         10  FILLER PIC X(80) VALUE SPACES.
000871*
000881     05  OTPSL001-LINE-19.
000891         10  FILLER PIC X(20) VALUE "--------------------".
000901         10  FILLER PIC X(20) VALUE "--------------------".
000911         10  FILLER PIC X(20) VALUE "--------------------".
000921         10  FILLER PIC X(20) VALUE "------------------- ".
000931*
000941     05  OTPSL001-LINE-20.
000951         10  FILLER PIC X(80) VALUE SPACES.
000961*
000971     05  OTPSL001-LINE-21.
000981         10  FILLER PIC X(20) VALUE "  TYPE OF PARTS: COD".
000991         10  FILLER PIC X(20) VALUE "E:                  ".
001001         10  FILLER PIC X(40) VALUE SPACES.
001011*
001021     05  OTPSL001-LINE-22.
001031         10  FILLER PIC X(17) VALUE SPACES.
001041         10  FILLER PIC X(20) VALUE "DESCRIPTION:        ".
001051         10  FILLER PIC X(43) VALUE SPACES.
001061*
001071     05  OTPSL001-LINE-23.
001081         10  FILLER PIC X(80) VALUE SPACES.
001091*
001101     05  OTPSL001-LINE-24.
001111         10  FILLER PIC X(20) VALUE "F1 - ADD    F2 - REA".
001121         10  FILLER PIC X(20) VALUE "D   F3 - NEXT RECORD".
001131         10  FILLER PIC X(20) VALUE "    F4 - UPDATE    F".
001141         10  FILLER PIC X(20) VALUE "5 - MAIN MENU       ".


Tim
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

_(reply depth: 5)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2002-12-01T17:49:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DEABC1F.8020300@Sympatico.ca>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <as7ge9$t8b$1@gaudi2.rug.ac.be> <3DE7ABE6.3AD4E673@shaw.ca> <xCvG9.193705$oRV.177128@news04.bloor.is.net.cable.rogers.com>`

```
I have source for one of those I wrote myself if you want a copy.  It 
might take me a day to find it in my library.
The last time I ran it, it was generating Fujitsu Version 4.0 code, and 
compiled in that language.  I thought of changing
it to write SP2 compable GUI code, but the event driven stuff  just did 
not lend itself to the approach.

If I was going to do it today, I would have it generate screen objects. 
 The better way would be to read
the original screen sections, and create a current "screen object" that 
ran in a DOS window.  That way
you could open as many of them as you wanted, and get a very "windowy" 
look. If the old screen sections
were generated, the code should be very easy to read, and something 
along that line could be hacked together
in a couple weeks of coding.

Donald

Timothy wrote:

>"James J. Gavan" <jjgavan@shaw.ca> wrote in message
>news:3DE7ABE6.3AD4E673@shaw.ca...
…[298 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

_(reply depth: 6)_

- **From:** "Timothy" <tim-antie.s_pam-hillock@rogers.com>
- **Date:** 2002-12-06T03:00:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dpUH9.18751$Q71.13604@news01.bloor.is.net.cable.rogers.com>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <as7ge9$t8b$1@gaudi2.rug.ac.be> <3DE7ABE6.3AD4E673@shaw.ca> <xCvG9.193705$oRV.177128@news04.bloor.is.net.cable.rogers.com> <3DEABC1F.8020300@Sympatico.ca>`

```
Donald,

     When you wrote your screen designer,  was the screen designed in a text
file and then process by your program or it was design with the program
reading the screen design from the video screen?  I'm thinking about
building some screens for work with the Fujitsu complier over the winter.
I'm just wondering the best way to input the screen as I haven't use the
complier much.   I'm more of a mainframe then PC programmer.

Tim
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

_(reply depth: 7)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2002-12-06T08:09:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DF0CBD5.20903@Sympatico.ca>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <as7ge9$t8b$1@gaudi2.rug.ac.be> <3DE7ABE6.3AD4E673@shaw.ca> <xCvG9.193705$oRV.177128@news04.bloor.is.net.cable.rogers.com> <3DEABC1F.8020300@Sympatico.ca> <dpUH9.18751$Q71.13604@news01.bloor.is.net.cable.rogers.com>`

```
I am not quite sure what you mean.  The program started with a 
background screen that could be
read from a text file and allowed you to place overlays on top of it. 
 You could either edit that within
the screen development program, or dump it to a text file and edit it 
with and editor, then re-load
it to the screen file data base.  When desired you would press a key and 
it would write the screen
sections.

Donald

Timothy wrote:

>Donald,
>
…[45 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

_(reply depth: 8)_

- **From:** "Timothy" <tim-antie.s_pam-hillock@rogers.com>
- **Date:** 2002-12-10T02:35:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KpcJ9.59433$Q71.24685@news01.bloor.is.net.cable.rogers.com>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <as7ge9$t8b$1@gaudi2.rug.ac.be> <3DE7ABE6.3AD4E673@shaw.ca> <xCvG9.193705$oRV.177128@news04.bloor.is.net.cable.rogers.com> <3DEABC1F.8020300@Sympatico.ca> <dpUH9.18751$Q71.13604@news01.bloor.is.net.cable.rogers.com> <3DF0CBD5.20903@Sympatico.ca>`

```
Since I don't know too much about the the Fujitsu complier, I'll just read
in a text file of a screen layout and have my program then create the
necessary cobol code out.  It will be a good project to work on over the
winter and learn about the features of the complier.  I guess I better get
back from my nephew, Thane's book.  I remember that it talk about screens
under the Fujitsu complier v3.  I hope that  there's not too much of a
difference between V3 and 5.

Thanks Donald.
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

_(reply depth: 9)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2002-12-10T09:50:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DF6295B.8060808@Sympatico.ca>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <as7ge9$t8b$1@gaudi2.rug.ac.be> <3DE7ABE6.3AD4E673@shaw.ca> <xCvG9.193705$oRV.177128@news04.bloor.is.net.cable.rogers.com> <3DEABC1F.8020300@Sympatico.ca> <dpUH9.18751$Q71.13604@news01.bloor.is.net.cable.rogers.com> <3DF0CBD5.20903@Sympatico.ca> <KpcJ9.59433$Q71.24685@news01.bloor.is.net.cable.rogers.com>`

```
No, the screen sections have not changed as far as I know.
Donald


Timothy wrote:

>Since I don't know too much about the the Fujitsu complier, I'll just read
>in a text file of a screen layout and have my program then create the
…[113 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

_(reply depth: 5)_

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-12-03T05:48:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LAXG9.41083$hK4.3639310@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <as7ge9$t8b$1@gaudi2.rug.ac.be> <3DE7ABE6.3AD4E673@shaw.ca> <xCvG9.193705$oRV.177128@news04.bloor.is.net.cable.rogers.com>`

```

    Microfocus Workbench also can do this.  Both FORMS and SCREENS.




"Timothy" <tim-antie.s_pam-hillock@rogers.com> wrote in message
news:xCvG9.193705$oRV.177128@news04.bloor.is.net.cable.rogers.com...
>
> "James J. Gavan" <jjgavan@shaw.ca> wrote in message
…[10 more quoted lines elided]…
> > > > painter like Saywhat? or Software Bottling Company, (although
probably
> > > both are
> > > > out of business) - these 'paint' pretty pictures in colours. To be
> > > 'generic'
> > > > you would have to restrict yourself to the simple ANSI  'accept
field'
> or
> > > > 'display field' - coupled with getting those accepts/displays to
line
> up
> > > with
> > > > your painted screen. You sure you want to go to all this effort ?
> > >
> > > I wouldn't limit myself to the simple ANSI accept, display fields but
I
> > > would only use simple things like column, line.
> > >
> > > >
> > > > Simple answer - determine which compiler you are going to use to
earn
> your
> > > > bread and butter and use their appropriate Screen Section features.
…[6 more quoted lines elided]…
> > > I have never used the dialog system of microfocus before but I have
used
> > > screens before.
> > > Ideally, the application I'm looking for would allow me to copy the
> > > screenoutputs from the terminal emulator and use them as a basis for
my
> > > screen sections.
> >
…[17 more quoted lines elided]…
> > output line sequentials as dummy screen source ?. You would  still have
to
> do
> > some editing of  the output to get your final result.
…[7 more quoted lines elided]…
> I found an old DOS based Cobol Screen builder program that is Shareware
from
> 1991.  It's on a 5 � floppy that I got to try out but never used.  I was
> trying to build a screen for a friends business but only got as far as the
…[22 more quoted lines elided]…
> --------------------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-11-29T11:55:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0211291155.6502c679@posting.google.com>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <as7ge9$t8b$1@gaudi2.rug.ac.be>`

```
"G nther De Vogelaere" <Gunther.DeVogelaere@killspammersrug.ac.be>
wrote

> Ideally, the application I'm looking for would allow me to copy the
> screenoutputs from the terminal emulator and use them as a basis for my
> screen sections.

It is not frantically difficult to write a screen code generator, I
wrote the basis of one in a day or so, though it grew somewhat over
some months with a week or so of effort.  Probably less total effort
than hand writing a bunch of screens and getting them working, you
only have to get the generator 'right' once and then churn out code.

Most screen painters that I saw required using the program to draw the
screen and mark the fields with properties:  FORMS2, SCREENS, .. they
worked but not to my taste.

I used a simple text file that was just the 80x25 layout required with
[ ] delimiting input areas and %%%% marking actual fields, so eg:

*SCREEN 
 Product Code[%%%%%%%%%%%]              PRODUCT MAINTENANCE

 Group       [%%]   %%%%%%%%%%%%%%%%%%
 Description [%%%%%%%%%%%%%%%%%%%%%%%%%%]
etc
*END

In front of this I add the field definitions where there is a
sequential relationship between the definition and the block of %s:

*FIELDSIKey,0,PR-Key
IGroup,1,PR-Group,,Proc-Group,Product group code - F7 to scan
available codes.
DGroup,0
IDesc,2,PR-Description,,,Description of product for invoices.
etc

Each item is:
   screen field name
   input order (0=display only)
   WS or FD field name
   field type (default = PIC X(n))
   paragraph name to perform
   prompt text (displayed in line 25)

It gets a bit more complex for tables, but essentially the fields are
read into a table, the text screen layout is processed to generate the
fixed data and to get the position and length for the fields then
several Cobol copybooks are written that will manage the screen,
displaying, accept each field (in order given by 2nd field), and
performing the specified paragraph if appropriate.

I don't use screen section, just working storage for the layouts and a
separate accept for each field.  Colouration is done dynamically by
performing some routines which do the grubby work (calling x'A7' in
the case of MF on PC) as this allows the users to set their own
colours for several functional areas (backgroud, data display, input
field, highlight area, error message) and it allows the code to set
the one input field so the user can easily see where he is at.

If you want to mimic existing screens then capturing them gives a
start for the text layout.
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-11-29T21:27:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DE7DEF3.D1B042CD@shaw.ca>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <as7ge9$t8b$1@gaudi2.rug.ac.be> <217e491a.0211291155.6502c679@posting.google.com>`

```


Richard wrote:

> "G nther De Vogelaere" <Gunther.DeVogelaere@killspammersrug.ac.be>
> wrote
…[60 more quoted lines elided]…
> start for the text layout.

An interesting approach Richard. Talk about playing an old tune on a new
instrument <G>. Much of what I'm doing with OO GUI classes parallels what you
are doing.

"and performing the specified paragraph if appropriate".

Yep, I'm doing something similar. The list of parameters contains the
Method-name to be invoked on an event..

It's sat there in the background, but I haven't totally automated quite like
you. The M/F Dialog Editor is my drawing tool to see what it looks like
visually, which in turn gives a series of IDs (Level 78's). So manually I set
up a series of parameters with fields in sequence. Once the parameter table
is created, using just the one class, I can then generate an instance for any
individual dialog, which does creation and event handling. (It was a pig to
figure out, but for tables I dynamically create the entry fields, by
supplying x, y, w and h).

The piece missing is the upfront automation - read the M/F resource file
which contains the 'windows image' and generate the individual parameter
lines without too much human intervention.

There's a couple of Net Express users who are 'hungry' to come up with a
similar, and probably more sophisticated, idea. And where I refer to the
'returning' methods, there's no logical reason why at least the skeletal code
for a method can't be generated for each event.

Be real nice if M/F would bite on this one, (automated GUI production), but
it's got to be low on any priority list as they initially switched to
re-emphasizing Dialog System and now produce a host of Java support classes.

They do of course have their Forms module which is geared to the Web. From
snapshots of the Forms module it looks like it's somewhat similar to the
PowerForm approach, draw, identify, select properties and generate code.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2002-12-02T17:17:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<205nuu83jq1i9no7chg2jkut7mj82osbcm@4ax.com>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <as7ge9$t8b$1@gaudi2.rug.ac.be>`

```
Gunther:

1.  COBOL sp2 is 100% COBOL compiler independent.  We work with ALL
the COBOL compilers without change of screen handling source code or
screen definitions.

2.  COBOL sp2 allows you to create full GUI screens dynamically from
COBOL CALL statements so that you can create your own custom
conversion programs.

3.  COBOL sp2 also fully supports the ability to integrate COM (Active
X Objects) components into your COBOL application.

4.  COBOL sp2 is also tightly integrated with our Thin Client and Web
Client Internet/intranet deployment products, so you can run your
application in just about any environment (including LINUX and VAX
server platforms) you prefer.

The best part is that everything is accomplished using ANSI standard
COBOL CALL USING statements.  COBOL and nothing but COBOL.

Contact me if I can be of further assistance.


"Gï¿½nther De Vogelaere" <Gunther.DeVogelaere@killspammersrug.ac.be>
wrote:

>Thx for your reply
>
…[28 more quoted lines elided]…
>


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-11-29T21:47:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0211292147.1aecf6ba@posting.google.com>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca>`

```
One MAJOR correction...

"James J. Gavan" <jjgavan@shaw.ca> wrote in message news:<3DE66C6D.B8F6C9F7@shaw.ca>...
> "Gï¿½nther De Vogelaere" wrote:
> 
…[24 more quoted lines elided]…
> you are kind of stuck. 

The 2002 COBOL standard is APPROVED, and PUBLISHED, and FINAL, and is
the CURRENT international COBOL standard.  And it includes the Screen
Section.
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-11-30T21:06:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DE92B74.51933AD6@shaw.ca>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <bfdfc3e8.0211292147.1aecf6ba@posting.google.com>`

```


Thane Hubbell wrote:

> One MAJOR correction...
>
…[31 more quoted lines elided]…
> Section.

Agreed Thane, but :-

 "Bearing in mind that the DOS Text Screen Section you are using is NOT yet part  of the
Standard"

- that he can use with impunity moving from a *current* compiler to another.

J4 may have achieved closure, but it is irrelevant until those enhancements are included in
"new" compilers. That's not a snide comment, but fact. Now it will BE INTERESTING to see
what the new compilers include, and more specifically what they leave out. That's leaving
aside any introductory dates for enhanced compilers.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

_(reply depth: 4)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-11-30T19:21:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0211301921.5f08b93a@posting.google.com>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <bfdfc3e8.0211292147.1aecf6ba@posting.google.com> <3DE92B74.51933AD6@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote in message news:<3DE92B74.51933AD6@shaw.ca>...
> Thane Hubbell wrote:
> 
> > One MAJOR correction...
> >
> > "James J. Gavan" <jjgavan@shaw.ca> wrote in message 

> > > Bearing in mind that the DOS Text Screen Section you are using is NOT yet part
> > > of the Standard, (but an updated 'version' will be when COBOL 2002 is issued),
…[16 more quoted lines elided]…
> aside any introductory dates for enhanced compilers.


I was merely commenting on your note that the Screen Section was not
part of the "Current" standard, where you allude to the yet to happen
event of publication.  I was correcting that misinformation -- Nothing
more.
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-12-04T16:33:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aslvrt$85b$1@slb0.atl.mindspring.net>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <bfdfc3e8.0211292147.1aecf6ba@posting.google.com>`

```
One minor clarification (not correction) below
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

_(reply depth: 4)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2002-12-05T16:28:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7vuuu4ngk2su9h4h938gf8kvin9pabd3v@4ax.com>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <bfdfc3e8.0211292147.1aecf6ba@posting.google.com> <aslvrt$85b$1@slb0.atl.mindspring.net>`

```
Bill:

Do I use the term, "only" in the COBOL FAQ?  If so, I'll be happy to
change it.

I'm going to ask Tracey to check all of our web pages too so that any
incorrect statements can be eliminated.

I may be incorrect, but I'm not sure if we ever used the term, "only"
because Norcom also uses a CALL USING approach to GUI screen handling,
which certainly falls into the category of ANSI standard syntax.

If we have used it, then you are absolutely correct that we certainly
are NOT the only approach which uses ANSI standard syntax and we'll
make the change post haste.


"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:

>One minor clarification (not correction) below
>
…[27 more quoted lines elided]…
>


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-12-05T10:47:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<asnvvm$ngb$1@slb6.atl.mindspring.net>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be> <3DE66C6D.B8F6C9F7@shaw.ca> <bfdfc3e8.0211292147.1aecf6ba@posting.google.com> <aslvrt$85b$1@slb0.atl.mindspring.net> <e7vuuu4ngk2su9h4h938gf8kvin9pabd3v@4ax.com>`

```
Not posted,

I thought that you used the statement that ONLY the "CALL approach" was ANSI
conforming - not that you were the only vendor using a CALL approach.  Sorry
if that wasn't clear - and let me know if I need to clarify my statement in
CLC.
```

#### ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

- **From:** "Gazaloo" <gaz@a.loo>
- **Date:** 2002-11-28T19:10:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%StF9.167244$nB.13320@sccrnsc03>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be>`

```
"G�nther De Vogelaere" wrote:
> I use Microfocus Netexpress 3.1.11 Service Pack 1 and it seems that such a
> tool (DSCH.exe or MicroFocus Dialog System) is  included but it generates
> copy-books and 'screens' that only can be used with a call to their
'dialog
> system runner'-thingy. Maybe I'm doing something horribly wrong in the
> DSCH.exe-tool.

No, you're not -- this is the way it's designed to work. What DS Char is
actually doing is emulating GUI screens on a text console (it uses a
subsystem called PANELS -- which you can also code to directly if you wish).
i.e. the screensets you develop will also run as Windows applications.

> I don't want to use their system in order to be able to generate code that
> also will work in a non-microfocus environment (so only accept/display of
> screens).

> Maybe an old, pre-windows version of this DSCH.exe would do the trick? Can
> somebody tell me where I could find/ download such a tool?

There used to be a tool called FORMS-2 that did something similar to what
you're after. It still ships with Object COBOL (UNIX), but no longer with
Net Express (Windows) or Server Express (UNIX). You *may* be able to
download it from Micro Focus supportline as an "as is" utility.

Some info on FORMS-2 can be found here:

http://supportline.microfocus.com/documentation/books/ocds4140/utpubb.htm
```

#### ↳ Re: Looking for tool to create/generate screen-sections (screen painter?)

- **From:** "John Osborne" <jroyoda@zbzoom.net>
- **Date:** 2002-11-28T14:50:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3de66df0$1_1@corp.newsgroups.com>`
- **References:** `<as5ho3$99c$1@gaudi2.rug.ac.be>`

```
You could use the screens program. It used to be the way to design screens
in Microfocus. I do not know if it is included in express.
"G�nther De Vogelaere" <Gunther.DeVogelaere@killspammersrug.ac.be> wrote in
message news:as5ho3$99c$1@gaudi2.rug.ac.be...
> Hello,
>
…[4 more quoted lines elided]…
> copy-books and 'screens' that only can be used with a call to their
'dialog
> system runner'-thingy. Maybe I'm doing something horribly wrong in the
> DSCH.exe-tool.
…[13 more quoted lines elided]…
>




-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
