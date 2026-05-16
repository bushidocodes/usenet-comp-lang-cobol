[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Move the mouse pointer

_12 messages · 5 participants · 1999-08_

---

### Move the mouse pointer

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990810215002.27448.00000512@ng-fe1.aol.com>`

```
Hello,

Is anyone aware of a Win32 API to move the mouse pointer ?  Or a different way
to control the position of the mouse pointer ?

Thanks,
Bob Hennessey
```

#### ↳ Re: Move the mouse pointer

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37B0EC24.7757679F@home.com>`
- **References:** `<19990810215002.27448.00000512@ng-fe1.aol.com>`

```
Bob7536 wrote:
> 
> Hello,
…[4 more quoted lines elided]…
> Thanks,

Bob,

I knew it would come in handy some day. "Windows for Dummies" lists
ClipCursor, Create...., Destroy..., GetCapture, GetCaretPos, GetCursor,
GetCursorPos, and a series of Sets... Check on the SDK for cross
reference. If you are still stuck try Ken Mullins on APIs.

Jimmy
```

##### ↳ ↳ Re: Move the mouse pointer

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990811084333.18925.00000281@ng-fs1.aol.com>`
- **References:** `<37B0EC24.7757679F@home.com>`

```
Hi Jimmy,

Thanks for the reply.  I believe I have found the proper API to handle this. 
According to the Win32 SDK this is an API called mouse_event.  I am confused
about the description of this API.  The API's that I have used in the past are
described as BOOL where this one is described as VOID.  Could someone comment
on what the difference means ?

Thanks,
Bob Hennessey
```

#### ↳ Re: Move the mouse pointer

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-08-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37BD6AD6.3F694D90@IMN.nl>`
- **References:** `<19990810215002.27448.00000512@ng-fe1.aol.com>`

```
Hi Bob,

Use the SetCursorPos:

=== Start quote from SDK help files ==============
The SetCursorPos function moves the cursor to the specified screen
coordinates. If the new coordinates are not within the screen rectangle
set by the most recent ClipCursor function, Windows automatically
adjusts the coordinates so that the cursor stays within the rectangle. 
BOOL SetCursorPos(
    int X,	// horizontal position  
    int Y 	// vertical position
   );	
 
Parameters
X
Specifies the new x-coordinate, in screen coordinates, of the cursor. 
Y
Specifies the new y-coordinate, in screen coordinates, of the cursor. 
 
Return Values
If the function succeeds, the return value is nonzero.
If the function fails, the return value is zero. To get extended error
information, call GetLastError. 
Remarks
The cursor is a shared resource. A window should move the cursor only
when the cursor is in its client area. 
The calling process must have WINSTA_WRITEATTRIBUTES access to the
window station. 
=== End   quote from SDK help files ==================

I remember myself programming in client coordinates, not screen
coordinates. So before the call to SetCursorPos, first call
ClientToScreen. (The GetCursorPos also returns in screen coordinates and
needs the ScreenToClient afterwards).

=== Start quote from SDK help files ==================
The ClientToScreen function converts the client coordinates of a
specified point to screen coordinates. 
BOOL ClientToScreen(
    HWND hWnd,	// window handle for source coordinates 
    LPPOINT lpPoint 	// pointer to structure containing screen
coordinates  
   );	
 
Parameters
hWnd
Identifies the window whose client area is used for the conversion. 
lpPoint
Points to a POINT structure that contains the client coordinates to be
converted. The new screen coordinates are copied into this structure if
the function succeeds.
 
Return Values
If the function succeeds, the return value is nonzero.
If the function fails, the return value is zero.
Remarks
The ClientToScreen function replaces the client coordinates in the POINT
structure with the screen coordinates. The screen coordinates are
relative to the upper-left corner of the screen. 
See Also MapWindowPoints, POINT, ScreenToClient 
=== End   quote from SDK help files ==================

Jump Luck,

The Frog

Bob7536 wrote:
> 
> Hello,
…[5 more quoted lines elided]…
> Bob Hennessey
```

##### ↳ ↳ Re: Move the mouse pointer

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990823204958.23592.00003575@ng-fs1.aol.com>`
- **References:** `<37BD6AD6.3F694D90@IMN.nl>`

```
Hello Mr. Frog,

Does the SetCursorPos set the cursor or the mouse pointer ?  I am looking to
move the mouse pointer not the cursor.

Thanks,
Bob Hennessey
```

###### ↳ ↳ ↳ Re: Move the mouse pointer

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-08-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7psidd$d45$1@news.hitter.net>`
- **References:** `<37BD6AD6.3F694D90@IMN.nl> <19990823204958.23592.00003575@ng-fs1.aol.com>`

```
These are the definitions used for Windows (from the
Windows Platform SDK).

"A cursor is a small picture whose location on the screen
is controlled by a pointing device, such as a mouse, pen,
or trackball. In the remainder of this overview, the term
mouse refers to any pointing device."

"A caret is a flashing line, block, or bitmap in the client
area of a window. The caret typically indicates the place
at which text or graphics will be inserted."

Use SetCursorPos to move the mouse pointer.
Use SetCaretPos to move the insertion point for text.
------------------
Rick Smith

Bob7536 wrote in message <19990823204958.23592.00003575@ng-fs1.aol.com>...
>Hello Mr. Frog,
>
>Does the SetCursorPos set the cursor or the mouse pointer ?  I am looking
to
>move the mouse pointer not the cursor.
```

###### ↳ ↳ ↳ Re: Move the mouse pointer

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C29861.82DD78DE@NOSPAMhome.com>`
- **References:** `<37BD6AD6.3F694D90@IMN.nl> <19990823204958.23592.00003575@ng-fs1.aol.com> <7psidd$d45$1@news.hitter.net>`

```
Rick Smith wrote:
> 
> These are the definitions used for Windows (from the
…[5 more quoted lines elided]…
> mouse refers to any pointing device."

Have you ever looked up "cursor" in a good dictionary?  It's original
meaning is "runner".  I looked it up when I first came across it used in
a SQL context.
```

###### ↳ ↳ ↳ Re: Move the mouse pointer

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pu3me$26h3$1@news.hitter.net>`
- **References:** `<37BD6AD6.3F694D90@IMN.nl> <19990823204958.23592.00003575@ng-fs1.aol.com> <7psidd$d45$1@news.hitter.net> <37C29861.82DD78DE@NOSPAMhome.com>`

```

Howard Brazee wrote in message <37C29861.82DD78DE@NOSPAMhome.com>...
>Rick Smith wrote:
>>
…[8 more quoted lines elided]…
>a SQL context.

No, but since you mentioned it, I have to look for it everwhere.
Interestingly, I pulled this from the Microsoft Bookshelf 98
dictionary.
----------
cursor (k�r�ser) noun
Computer Science.
A bright, usually blinking, movable indicator on a display,
marking the position at which a character can be entered,
corrected, or deleted.

[Middle English, runner, from Latin, from cursus, past participle
of currere, to run.]
----------
This is almost the same definition as given for "caret" in the
Windows Platform SDK. Furthermore, I found no reference
to SQL cursors.

The change in usage of "cursor" and the addition of "caret"
may have originated with the Apple Macintosh.

Nontheless, for text screens, the "cursor control keys" still
provide a useful means for "running" through text to place
the cursor, I mean caret, at a new position.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Move the mouse pointer

_(reply depth: 6)_

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C65A2A.D3A64B3B@IMN.nl>`
- **References:** `<37BD6AD6.3F694D90@IMN.nl> <19990823204958.23592.00003575@ng-fs1.aol.com> <7psidd$d45$1@news.hitter.net> <37C29861.82DD78DE@NOSPAMhome.com> <7pu3me$26h3$1@news.hitter.net>`

```
Rick Smith / Howard Brazee / Bob Hennessey,
they all wrote about cursors. :)

Anyway, Bob,

I hope you now know to use the set/get calls, to convert between screen
and window(client) pels. Did it work for you?

The Frog
```

###### ↳ ↳ ↳ Re: Move the mouse pointer

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C68E38.6190ADAC@NOSPAMhome.com>`
- **References:** `<37BD6AD6.3F694D90@IMN.nl> <19990823204958.23592.00003575@ng-fs1.aol.com> <7psidd$d45$1@news.hitter.net> <37C29861.82DD78DE@NOSPAMhome.com> <7pu3me$26h3$1@news.hitter.net> <37C65A2A.D3A64B3B@IMN.nl>`

```
The COBOL Frog wrote:
> 
> Rick Smith / Howard Brazee / Bob Hennessey,
> they all wrote about cursors. :)

Foiled again!
```

###### ↳ ↳ ↳ Re: Move the mouse pointer

_(reply depth: 7)_

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1999-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990828123609.06826.00001215@ng-cl1.aol.com>`
- **References:** `<37C65A2A.D3A64B3B@IMN.nl>`

```
Good Morning,

The SetCursorPos API does move the mouse pointer (cursor) and not the caret
(what i used to call the cursor). If anyone would like a sample of this call
let me know.

Thanks,
Bob Hennessey
```

###### ↳ ↳ ↳ Re: Move the mouse pointer

_(reply depth: 4)_

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990824063813.08941.00003622@ng-bg1.aol.com>`
- **References:** `<7psidd$d45$1@news.hitter.net>`

```
Hi Rick,

Thanks for the information.  The cursor to me had allways been the blinking
line or box.  Guess this comes from my DOS days. 

Thanks again for the help.

Bob Hennessey
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
