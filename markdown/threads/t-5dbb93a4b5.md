[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using the "RegSetValueEx" API...

_3 messages · 3 participants · 1999-01_

---

### Using the "RegSetValueEx" API...

- **From:** tommy nilsen <tommy.nilsen@merkantildata.no>
- **Date:** 1999-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369623AE.6AD8666D@merkantildata.no>`

```

Hi.

I need to set a hex value in the registry using the "RegSetValueExA"
win32-api..
Couild someone please give a hint of how to do this...

I have no problem using the same api to set a string or int value...

Any help would be greatly appreciated.

Tommy
tommy.nilsen@merkantildata.no
```

#### ↳ Re: Using the "RegSetValueEx" API...

- **From:** "Gael Wilson" <gw@mfltd.co.uk>
- **Date:** 1999-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<775fin$oar@hyperion.mfltd.co.uk>`
- **References:** `<369623AE.6AD8666D@merkantildata.no>`

```
Tommy,

The data items used in the API calls are straightforward numerics, so you
should be able to pass in decimal values. However, various compilers will
allow you to define hex values so either of the following would do exactly
the same

move 16 to val
move h"10" to val

I hope this helps.


tommy nilsen wrote in message <369623AE.6AD8666D@merkantildata.no>...
>
>Hi.
…[13 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Using the "RegSetValueEx" API...

- **From:** "tommy" <tommynilsen@yahoo.com>
- **Date:** 1999-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<776hv7$tk1$2@nntp.newmedia.no>`
- **References:** `<369623AE.6AD8666D@merkantildata.no> <775fin$oar@hyperion.mfltd.co.uk>`

```
Hi.
Thanks for answering.

In the program below you can see what I'm trying to do.
The value that is actually set in the registry is incorrect...

If you decide to try this program, be shure to take a backup of the
specified registry-key..


Tommy

----------------------------------------------------------------------------
---------------------------------------------------------------
      $set ans85 comp
       identification division.
       program-id. login.

       environment division.
       configuration section.
       special-names.
       call-convention 74 is WINAPI.
       input-output section.

      *-------------------------
       working-storage section.
      *-------------------------
       01 link-api32.
          03 link-api32-TextBuffer          pic x(200).
          03 link-api32-TextBufferLn        pic 9(9)  comp-5.
          03 link-api32-ApiStatus           pic 9(9)  comp-5.
          03 link-api32-TextBuffer2         pic x(200).
          03 link-api32-TextBuffer2Ln       pic 9(9)  comp-5.
          03 link-api32-NumBuffer           pic 9(9)  comp-5.
       78 HKEY-LOCAL-MACHINE               value 2147483650.
       78 KEY-ALL-ACCESS                   value 983103.
       01 register-status                  pic 9(1) value 0.
       01 win32-ApiStatus                  pic s9(9)  comp-5.
       01 win32-TextBuffer                 pic x(200).
       01 win32-NumBuffer                  pic 9(9)  comp-5.
       01 wskeyHandle                      pic s9(9)  comp-5.

       procedure division.

       call "cob32api.dll"
           initialize wsKeyHandle
           move HKEY-LOCAL-MACHINE to win32-NumBuffer
           move z"Software\Microsoft\Internet Explorer" to
                                                        win32-TextBuffer
           call WINAPI "RegOpenKeyExA" using
                   by value     win32-NumBuffer
                   by reference win32-TextBuffer
                   by value 0 *> Ikke i bruk
                   by value     KEY-ALL-ACCESS
                   by reference wsKeyHandle
               returning        win32-ApiStatus
           end-call
           move z"IntegratedBrowser" to link-API32-TextBuffer
           move 0 to link-API32-NumBuffer *> Type of KEY,not shure this is
the right value
           move h"01"      to link-API32-TextBuffer2*>The value I want  to
set in the registry
           move 2          to link-API32-TextBuffer2Ln
           call WINAPI "RegSetValueExA" using
                   by value wsKeyHandle
                   by reference link-API32-TextBuffer
                   by value 0
                   by value link-API32-NumBuffer
                   by reference link-API32-TextBuffer2
                   by value link-API32-TextBuffer2Ln
               returning link-API32-ApiStatus
           end-call

           stop run
           .
----------------------------------------------------------------------------
---------------------------------------------------------------







-----Opprinnelig melding-----
Fra: Gael Wilson <gw@mfltd.co.uk>
Nyhetsgrupper: comp.lang.cobol
Dato: 8. januar 1999 18:27
Emne: Re: Using the "RegSetValueEx" API...


>Tommy,
>
…[29 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
