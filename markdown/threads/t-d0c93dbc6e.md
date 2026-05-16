[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# UNISYS Screen Codes

_1 message · 1 participant · 1999-02_

---

### Re: UNISYS Screen Codes

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joIu2.3724$Xl5.5053184@news1.mia>`
- **References:** `<79cpqs$c6j4@ns2.hgo.net>`

```
Duncan Kinder wrote:
>As a school assignment, I am developing an interactive program, the menus of
>which depend upon UNISYS screen codes.  I am working with COBOL 74.
…[6 more quoted lines elided]…
>hexadecimal numbers and they are staring back at me.

I assume you are referring to the Unisys A Series.  The following hex codes
are EBCDIC.

  HEX NAME  FUNCTION
  1C   FS   Left Delimiter: protected transmittable field
  1D   GS   Left Delimiter: right justified unprotected transmittable field
  1F   RS   Left Delimiter: normal unprotected transmittable field
  1E   US   Right Delimiter: end transmittable field
  4A   [    Will be changed into RS (1F) when terminal enters forms mode
  5A   ]    Will be changed into US (1E) when terminal enters forms mode

When a screen is transmitted ot the terminal an Escape-'W' is appended,
which places the terminal in 'forms mode'.  While in forms mode, the
user can only enter data into the fields defined between appropriate
left and right delimiter characters.  When the 'Xmit' key is pressed in
forms mode, only the data in the defined fields are transmitted to the
A Series mainframe.  The FS, GS and RS characters are the left delimiter
characters, and they specify what type of field it is.  The FS character
begins a 'protected transmittable' field.  This field is to send data to
the mainframe that cannot be changed by the user, such as a trancode.
The US character is the universal right delimiter for all fields.  The
left and right square brackets can be used instead of the normal left
and right delimiters, if you want to deal only with printable characters.
When the terminal enters forms mode, these are changed into the actual
left and right delimiters.

  HEX NAME  FUNCTION
  0E   SO   Start Reverse Video (ends with US or end of line)
  18   CAN  Start Blink (ends with US or end of line)
  3F   SUB  Bright Video (ends with US or end of line)

In addition, there are several highlighting characters.  When used, they
start the highlighting feature, and the highlighting continues to the
right until the first US character or the end of the line is encountered.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
