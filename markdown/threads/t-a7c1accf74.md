[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# sound

_4 messages · 4 participants · 1998-09 → 1998-10_

---

### sound

- **From:** "Patrick Lykins" <lynkins@access.mountain.net>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361211f9.0@news.mountain.net>`

```
Can anyone tell me if their is a way to put sound into a CoBOL program?

I really don't care how crude it is, if it's just a series of signal tone
beeps, it is better than nothing.

                                                                Thank you,

Patrick L. Lykins
```

#### ↳ Re: sound

- **From:** "Fujitsu Software" <cobol@adtools.com>
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6utmra$ord$1@nntp2.ba.best.com>`
- **References:** `<361211f9.0@news.mountain.net>`

```
Fujitsu COBOL V4 includes two routines for adding sound:

  CBL_ALARM_SOUND
  CBL_BELL_SOUND

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX:    (408) 428-0600
Email:  cobol@adtools.com
Web:   http://www.adtools.com


Patrick Lykins wrote in message <361211f9.0@news.mountain.net>...
>Can anyone tell me if their is a way to put sound into a CoBOL program?
>
…[7 more quoted lines elided]…
>
```

#### ↳ Re: sound

- **From:** cadams@cadams-ntw.acucorp.com (Chris Adams)
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn714oia.66o.cadams@cadams-ntw.acucorp.com>`
- **References:** `<361211f9.0@news.mountain.net>`

```
On Wed, 30 Sep 1998 07:08:41 -0400, Patrick Lykins
<lynkins@access.mountain.net> wrote:
>Can anyone tell me if their is a way to put sound into a CoBOL program?
>
>I really don't care how crude it is, if it's just a series of signal tone
>beeps, it is better than nothing.

What compiler are you using and what platform is it running on? 

If it's any flavor of text-mode, you're looking at a console bell (check your
manual to see if DISPLAY/ACCEPT have a bell or beep option). On the other hand
if you're running on Windows, your vendor may have provided a library routine
to play wave files (WIN$PLAYSOUND on Acucobol-GT, see I-144) and you can always
call the Windows API.

----
The opinions above are my own and may or may not match those of my employer.
```

#### ↳ Re: sound

- **From:** Martyn Woerner <mw@unspam.mfltd.unspam.co.uk>
- **Date:** 1998-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36133B73.DEB@unspam.mfltd.unspam.co.uk>`
- **References:** `<361211f9.0@news.mountain.net>`

```
Patrick Lykins wrote:
> 
> Can anyone tell me if their is a way to put sound into a CoBOL program?
> 
> I really don't care how crude it is, if it's just a series of signal tone
> beeps, it is better than nothing.

With MF COBOL running under Windows, try the windows API.  Check if
sound is available and if so, just play away.  This sort of thing - mind
you need to use the copyfile derived from the windows.h file using the
h2cpy utility to pick up the right datatypes and constant values.  If
you need more info, let me know.

      *>   Next, check if sound is available
           move SND-ASYNC to sound-mode
           if sound-enabled                    *> Do we want to try?
               set sound-enabled to false
               call ms-winapi sndPlaySound using
                       by reference init-run-sound
                       by value     sound-mode
                       returning win-return-bool
               on exception
      *>           This is not a basic Windows routine but one from
      *>           the MMSystem, so it may not have been linked in.
                   add MB-OK MB-ICONINFORMATION giving tmp-int
      $if env not = "16bit"
                   add MB-SETFOREGROUND to tmp-int
      $end
                   call ms-winapi MessageBox using
                       by value screen-hand
                       by reference "The sound routine doesn't seem " &
                                 "to be here, but no matter."   & x"00"
                       by reference "TicTac - Running Silently" & x"00"
                       by value tmp-int
                   end-call
               not on exception
                   if win-return-bool = val-true
                       set sound-enabled to true
                   end-if
               end-call
           end-if
and then ...

           move SND-ASYNC to sound-mode
           add SND-NOSTOP to sound-mode
           if sound-enabled
               perform with test after until win-return-bool = val-true
                   call ms-winapi sndPlaySound using
                           by reference init-game-sound
                           by value     sound-mode
                           returning win-return-bool
                   if win-return-bool not = val-true
                       perform zb000-yield
                   end-if
               end-perform
           end-if
           move SND-ASYNC to sound-mode

and working storage has stuff like ..

       77  sound-mode                  usage UINT    value SND-ASYNC.
       77  win-return-bool             usage BOOL.
       78  init-run-sound  value sound-path & "initrun.wav"  & x"00".
       78  init-game-sound value sound-path & "initgame.wav" & x"00".
       01  screen-data value low-values.
        03 screen-hand                 usage HWND.





Martyn.

To reply, remove the two "unspam." from the address.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
