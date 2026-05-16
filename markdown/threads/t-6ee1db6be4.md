[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Options when moving COBOL from UNIX to WINDOWS

_7 messages · 5 participants · 2001-08_

---

### Options when moving COBOL from UNIX to WINDOWS

- **From:** david@quantumcat.demon.co.uk (David Latimer)
- **Date:** 2001-08-24T08:35:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9026f4e.0108240735.24e9b078@posting.google.com>`

```
I work as 1 of 2 COBOL developers in a very small IT dept!

We currently use MicroFocus COBOL V4.0 on an ICL UNIX box
running UnixWare 2.1.3 (A bit behind the times?).

Within a year or two we will probably move from the UNIX
box to a WINDOWS server.

This is mainly because we won't need to pay for UNIX 
hardware/software support (limited inhouse knowledge) but
also because we would like to introduce some mouse control
to the existing screens (e.g. clicking into fields and on
buttons).

After that we could go full GUI & interact with other
WINDOWS programs like Excell/Word/Outlook.

What might be the best options in terms of compilers/products
and conversion methodologies?

I ought to mention that:
a) I'm not sure if we are 100% ANSI-85 compliant.
b) All our screen handling code (using ACCEPT AND DISPLAY 
with screens defined in the SCREEN SECTION) is in the same
programs as the business logic. (Yes, i know you're not
supposed to now!)
c) We have SYSTEM calls within some programs.

Sorry if i've rambled on a bit but thanks in advance,
David
```

#### ↳ Re: Options when moving COBOL from UNIX to WINDOWS

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2001-08-24T17:20:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b868996.17499361@news.epix.net>`
- **References:** `<a9026f4e.0108240735.24e9b078@posting.google.com>`

```
David:

Our COBOL Tools are completely COBOL compiler independent.

We have assisted a number of companies in conversion from
DISPLAY/ACCEPT to our COBOL sp2 (COBOL GUI Tool) calls.

Our software also supports the UNIX environment, so we understand the
environment from which you are coming.

We have solutions for your Windows Print Manager needs and also
provide multiple Internet enabling solutions, including both thin
client/server solutions as well as web browser client/server solutions

Please contact me at rtwolfe@flexus.com for more information.

Thanks.


david@quantumcat.demon.co.uk (David Latimer) wrote:

>I work as 1 of 2 COBOL developers in a very small IT dept!
>
…[27 more quoted lines elided]…
>David


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: Options when moving COBOL from UNIX to WINDOWS

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-08-24T18:11:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B8699A9.B8E6DA0B@home.com>`
- **References:** `<a9026f4e.0108240735.24e9b078@posting.google.com>`

```


David Latimer wrote:

> I work as 1 of 2 COBOL developers in a very small IT dept!
>
…[27 more quoted lines elided]…
> David

I can't address Unix directly because I haven't used it.

1. If you are comfortable/satisfied with Micro Focus products then it
makes sense to 'upgrade' within the family - unless your searching
reveals cheaper prices, something closer to what you are looking for
etc.

2. I'm assuming you are hell bent on going Windows. If you wanted to
stick with Screen Section does M/F have a sample program for using the
Mouse with Unix ? (in DOS it was ADMOUSE.cbl - (AD = their
Accept/Display or Adis module).

3. Windowing - several options, (I'm reasonably certain the Unix version
parallels the PC Net Express - but check with M/F for specifics). M/F
two options - Dialog System, (successor/extension to their Panels
product) or you could use Windows GUIs using OO classes - don't touch
the latter with a barge pole if you aren't already into windowing/OO.
You can communicate with  Java - but you have to learn the language.
Other alternatives are Flexus SP2 or Norton Screen I/O - you write
conventional COBOL programs and they do the Windowing for you.

4. How long for you to get into Windowing ?. Make a guesstimate, then
double or triple the time - if you haven't been anywhere near Windows
before.

5. Each of the various Windowing options will let you get into
Excel/Word/Outlook.

6. Conversion methodologies. Your Screens are integrated with business
logic. What's new, we all did it that way ! Given there is a reasonable
time slice between what you are doing now and getting into Windowing,
give this one a lot of thought and extract your 'Screens' into separate
programs called by the business logic. Will make it much easier to
convert to Windowing.

7. Given that you feel 'compelled' to get into Windowing - not
suggesting that you should - but maybe you should give OO COBOL a look
see. You could do the Windowing first, and possibly take a look at OO
later - but there's bound to be some extra work, i.e. you will view the
design of your non-OO programs in a particular way, then getting to OO
you will,..... "Oh I wish we had realized, we should have written the
programs this way. Would've made it easier to switch to OO...".

I'm not making a hard case for OO - just mentioning it, so you are
aware, and arrive at your own judgment.

Good luck

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Options when moving COBOL from UNIX to WINDOWS

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-08-25T09:11:33+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B875DB5.3045943D@Azonic.co.nz>`
- **References:** `<a9026f4e.0108240735.24e9b078@posting.google.com> <3B8699A9.B8E6DA0B@home.com>`

```
> David Latimer wrote:
> >
…[7 more quoted lines elided]…
> > hardware/software support (limited inhouse knowledge) but

Moving to a Windows server means that you won't have to pay for _Unix_
hardware/software support but will need to pay someone to do Windows
hardware/software support, and will especially need to pay for licences
and upgrades - it is expected that MS licences will be expiring ones
with a life of 3 years.  

Perhaps you are paying ICL maintenance contracts.  Have you thought
about moving to Linux on bog standard PCs ?  Perhaps Caldera 'Open Unix'
which is Unixware with Linux personality.  In theory it can run all
UnixWare and Linux apps.

> > also because we would like to introduce some mouse control
> > to the existing screens (e.g. clicking into fields and on
> > buttons).

I have systems in MF Cobol that run on DOS, Windows, Unixware and Linux
from one set of source code.  I detect the OS and take some different
paths depending on which it is running on.

It is possible to use the mouse with MF ACCEPT/DISPLAY where a mouse is
available but generally with the sort of systems that are used by Cobol
a mouse gets in the way more that helping.  You can enable the mouse
using a call to adis and then it can be detected as if the user pushed a
function key (ie you fall off the accept).  The XY position can be
detected so that you can treat specific areas of the screen as if they
were buttons.

I have a mixture of older ADIS programs and newer SP2 where some
functions require to use an older program.  It is possible within a
system to switch between SP2 and ADIS so that the original system can
continue to be used while new functions are built or programs are
changed to GUI/SP2.

> > After that we could go full GUI & interact with other
> > WINDOWS programs like Excell/Word/Outlook.

Or you could use StarOffice/KOffice etc under Linux.
```

###### ↳ ↳ ↳ Re: Options when moving COBOL from UNIX to WINDOWS

- **From:** david@quantumcat.demon.co.uk (David Latimer)
- **Date:** 2001-08-28T04:16:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9026f4e.0108280316.63380861@posting.google.com>`
- **References:** `<a9026f4e.0108240735.24e9b078@posting.google.com> <3B8699A9.B8E6DA0B@home.com> <3B875DB5.3045943D@Azonic.co.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<3B875DB5.3045943D@Azonic.co.nz>...
> > David Latimer wrote:
> > >
…[13 more quoted lines elided]…
> with a life of 3 years.  

We already have 3 Windows servers (running things like MS Exchange).

> 
> Perhaps you are paying ICL maintenance contracts.  Have you thought
…[14 more quoted lines elided]…
> a mouse gets in the way more that helping.  

For some of our Enquiries navigating by mouse would be more natural to
those who use Windows most of the time.

> You can enable the mouse
> using a call to adis and then it can be detected as if the user pushed a
> function key (ie you fall off the accept).  The XY position can be
> detected so that you can treat specific areas of the screen as if they
> were buttons.

Is this only possible in Windows(DOS) or have you been able to do it in 
Unix/Linux?
This could be a quick and useful short term measure as we use line 23 of
our screens as a standard function key map (F1 - F12).
e.g. at the end of the line we have "| Quit | Send|" (F11 & F12).

Is the XY position character based (80 * 25) or by pixel?


> 
> I have a mixture of older ADIS programs and newer SP2 where some
…[8 more quoted lines elided]…
> Or you could use StarOffice/KOffice etc under Linux.

The company has settled on MS Office.
```

###### ↳ ↳ ↳ Re: Options when moving COBOL from UNIX to WINDOWS

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-08-28T19:04:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B8BEC14.DF4CD03A@home.com>`
- **References:** `<a9026f4e.0108240735.24e9b078@posting.google.com> <3B8699A9.B8E6DA0B@home.com> <3B875DB5.3045943D@Azonic.co.nz> <a9026f4e.0108280316.63380861@posting.google.com>`

```


David Latimer wrote:

> > You can enable the mouse
> > using a call to adis and then it can be detected as if the user pushed a
…[9 more quoted lines elided]…
>

I'll  let Richard answer the rest, but specifically the above. In Windows I use the ENTER key to
terminate data put into an entry-field (that's EXACTLY the way the user had it in DOS and he sees no
reason to switch to that bloody TAB key - ergonomically it's the pits ! He does 90% plus of his
input using the Numpad). It presents a  problem for me because dear old Windows *assumes* he's hit
the OK PushButton. So I have to detect for the ENTER key and is it terminating an entryfield or is
he truly pushing the OK Button. (In OO I check if the CurrentObject is the DefaultPushbutton or
otherwise).

Remember what you want to do with F11 or F12 is no different to pressing F1 for Help in any package
you personally use, written for Windows.

Micro Focus provides "keys.cpy" for Keystrokes :-
-------------------------------------------------------------
*>> Virtual Key Codes. Cab be used when querying the character
*>> pressed on keyboard events

*>> VK_0 thru VK_9 are the same as ASCII '0' thru '9' (0x30 - 0x39)
*>> VK_A thru VK_Z are the same as ASCII 'A' thru 'Z' (0x41 - 0x5A)

78  OVK-BACK           value h"08".
78  OVK-TAB            value h"09".
78  OVK-CLEAR          value h"0c".
78  OVK-RETURN         value h"0d".
etc.....
78  OVK-HELP           value h"2f".
78  OVK-NUMPAD0        value h"60".
etc....

and the ones you are interested in :

78  OVK-F1             value h"70".
78  OVK-F2             value h"71".
78  OVK-F3             value h"72".
78  OVK-F4             value h"73".
78  OVK-F5             value h"74".
78  OVK-F6             value h"75".
78  OVK-F7             value h"76".
78  OVK-F8             value h"77".
78  OVK-F9             value h"78".
78  OVK-F10            value h"79".
78  OVK-F11            value h"7a".
78  OVK-F12            value h"7b".
etc....
-----------------------------------------------------------------------------------

So you can get a feel for how I use it testing the ENTER key :-

*>-------------------------------------------------------------
Method-id. "begin".
*>-------------------------------------------------------------
*> Here I'm telling it to check for all keystrokes

Linkage section.
01 lnk-Caller                        object reference.
Procedure Division using lnk-Caller.
  set os-Caller to lnk-Caller
  invoke self "wantAllKeys"
End Method "begin".
*>-------------------------------------------------------------
Method-id. "checkCharacterCode".   *> PRIVATE
*>-------------------------------------------------------------
*> as the result of a 'keying event' this jumps  into action

*> checks for backspace etc.....

Local-storage section.
copy "keys.cpy".
01 ls-code                              pic x(4) comp-5.
Linkage section.
01 lnk-event                            object reference.
Procedure Division using lnk-event.

 invoke lnk-event "getCharacterCode" returning ls-code

 Evaluate true
    when  ls-code = OVK-RETURN or OVK-TAB
          invoke self "returnEntryObject"
 End-evaluate

End Method "checkCharacterCode".
*>-------------------------------------------------------------
Method-id. "returnEntryObject".
*>--------------------------------------------------------------

*>. This only 'exectues' if it is an entryfield :-

Local-storage section.
01 ls-object                     object reference.
01 ls-string                     object reference.
01 ls-MethodName                 pic x(30).

01 ls-ReturnValues.
   05 ls-field                      pic x(4) comp-5.
   05 ls-length                     pic x(4) comp-5.
   05 ls-text.
      10 occurs 1 to TextLength
         depending on ls-length     pic x(01).

Procedure Division.

perform varying ls-field from 1 by 1
                until ls-field > MaxEntryFields

    invoke os-Collection(2) "at"
           using ls-field returning ls-object

    if  os-CurrentObject = ls-object
        invoke os-CurrentObject "getText" returning ls-string
        invoke ls-string "trimblanks" returning ls-string
        invoke os-CurrentObject "Getlength" returning ls-length
        invoke ls-string "getValueWithSize"
             using ls-Length returning ls-text
        invoke ls-string "finalize" returning ls-string

        invoke os-Collection(3) "at"
             using ls-field returning ls-MethodName

        invoke os-Caller ls-MethodName
               using ls-ReturnValues
         EXIT METHOD
    End-if
End-perform

End Method "returnEntryObject".
*>--------------------------------------------------------------

> Is the XY position character based (80 * 25) or by pixel?

Not the same thing at all. ADIS used with DOS is testing for Line/Column. I suppose you could test
for a specific pixel location given x and y but generally you are talking about Windows controls,
regardless of their size. If you were to substitute a set of Pushbuttons at the foot of your screen
(Dialog) that had captions for F1, F11 or F12 etc., then the Windows  is looking for you clicking
anywhere within the controls x, y, w(idth), h(eight), positioning.

Jimmy, Calgary AB
```

#### ↳ Re: Options when moving COBOL from UNIX to WINDOWS

- **From:** alain.reymond-nospam@ceia.com (Alain Reymond)
- **Date:** 2001-08-27T08:05:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b89f8cd.522120@news.skynet.be>`
- **References:** `<a9026f4e.0108240735.24e9b078@posting.google.com>`

```
We had exactly the same problem on (astonishing!) the same platform.

We studied the problem. Here are some arguments that lead to our
conclusion:

1- You do not want to pay for a Unix hardware/software support. I can
understand. Moving from a Unix to a Windows box will make you pay for
a Windows support which is not cheap for a good NT server and all it's
licences.

2- Porting a program from Unix to Windows/GUI is not just transferring
it to the new system and recompile it. You have to re-think your
entire application to profit from the benefits of the GUI essentially
based on processing a flow of events generated by the user. This is a
very long and expensive work.

3- If you have been running under Unix for many years, you must
certainly have developed some expertise. Why lose that capital?

4- Adding GUI facilities in an application is legitimate. But does the
entire application require that functionality? An idea is to clearly
identify which portions require GUI interactions and find an
appropriate solution: exportation/importation of data or ODBC (Parkway
for example), etc... if your Unix server is integrated in a network.

If you look at the price of a Linux box (Dell for example), you can
find a very good system, ready to run, for a few euros (or dollars),
with Redhat installed. You can integrate it in a network with Windows
stations and access the system through a good telnet program
(TinyTerm, Anzio or many others). You can have drives mounted using
NFS or samba, share printers.

Considering all that points - and others -, we moved under Linux last
December. We bought a MF Cobol licence. It took us half a day to
migrate from our ICL/Unixware server to the Linux one: ftp and
compile. We had just a few changes for the spooling facilities.

Until now, we haven't got any problem with that solution. Every case
is particular. In our case, we are satisfied with our choices.

Hope a real life experience can be interesting.

Alain

>I work as 1 of 2 COBOL developers in a very small IT dept!
>
…[27 more quoted lines elided]…
>David
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
