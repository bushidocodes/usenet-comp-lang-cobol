[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need help with GetOpenFileName API Call

_3 messages · 2 participants · 1999-06_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Need help with GetOpenFileName API Call

- **From:** dblaze@merchants-fla.com (Doug Blaze)
- **Date:** 1999-06-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375e8003.4056112@news.icix.net>`

```
Hello all,

I'm at it again - trying to use the API!  You think I'd learn by now!

However, I need to allow the user to select a program (*.exe) to use
as a text viewer (ie: notepad or wordpad).  I have a button on my
screen called 'BROWSE'.  When they click it, I invoke the
GetOpenFileName API call to allow them to select a program.  I can get
the actual file name they selected in OFN-Title (ie:  notepad.exe) but
I need the complete path including drive letter.  This is supposed to
be returned in a variable pointed to by 'lpstrFile'.  However, this
field is blank after the call.  What's interesting is 'hFileOffset'
contains a value that looks correct (this represents the number of
characters from the beginning of the path to the start of the filename
pointed to by lpstrFile).  Below is the WORKING-STORAGE define of the
structure and the actual call.  I have to think I'm missing something
very obvious but after two days of trying, I can't figure it out.

I'm running NT4.0 with MF 4.0.32.  The dialog is presented fine and
the call returns TRUE.  In the displays after the call, the following
values are returned if I select the following file:  

d:\winnt\notepad.exe

          Display "Call GetOpenFileNameA Successful"
          Display "File Title Selected = " OFN-Title    (NOTEPAD.EXE)
          display "complete file name  = " OFN-FileName (spaces)
          DISPLAY "nMaxfile            = " nMaxFile     (+000000000)
          display "nFileOffset         = " nFileOffset  (+00009)
          DISPLAY "lpstrFile           = " lpstrfile    (0005275936)


Any help would be appreciated!

Doug

 01  OFN-Struct.
     05  lStructSize                 pic s9(9)  comp-5 value 0.
     05  hwndOwner                   pic s9(9)  comp-5 value 0.
     05  hInstance                   pic s9(9)  comp-5 value 0.
     05  lpstrFilter                 POINTER.
     05  lpstrCustomFilter           pic s9(9)  comp-5 value 0.
     05  nMaxCustFilter              pic s9(9)  comp-5 value 0.
     05  nFilterIndex                pic s9(9)  comp-5 value 1.
     05  lpstrFile                   POINTER.
     05  nMaxFile                    pic s9(9)  comp-5 value 0.
     05  lpstrFileTitle              POINTER.
     05  nMaxFileTitle               pic s9(9)  comp-5 value 260.
     05  lpstrInitialDir             POINTER.
     05  lpstrTitle                  pic s9(9)  comp-5 value 0.
     05  OFNFlags                    pic s9(9)  comp-5 value
                                     h"00081800".
     05  nFileOffset                 pic s9(4)  comp-5 value 0.
     05  nFileExtension              pic s9(4)  comp-5 value 0.
     05  lpstrDefExt                 pic s9(9)  comp-5 value 0.
     05  lCustData                   pic s9(9)  comp-5 value 0.
     05  lpfnHook                    pic s9(9)  comp-5 value 0.
     05  lpTemplateName              pic s9(9)  comp-5 value 0.

 01  OFN-Filters.
     05  Filler                      pic x(8)   value "Programs".
     05  Filler                      pic x      value x"00".
     05  Filler                      pic x(5)   value "*.exe".
     05  Filler                      pic x      value x"00".
 01  OFN-Title                       pic x(260) value SPACES.
 01  OFN-Init-Dir                    pic x(9)  value spaces.
*                                     "D:\WINNT".
 01  OFN-FileName                    pic x(260) value SPACES.

 Browse-For-File.
      move length of OFN-Struct    to lStructSize
      SET lpstrFilter              to address of OFN-Filters
      SET lpstrFileTitle           to address of OFN-Title
      SET lpstrInitialDir          to address of OFN-Init-Dir
      move low-values              to OFN-FileName.
      move length of OFN-Struct    to lStructSize
      CALL WinApi32 "GetOpenFileNameA" using
            BY REFERENCE OFN-Struct
            RETURNING    WReturnCode
      end-call
      SET lpstrFile to address of OFN-FileName.
      If WReturnCode not = 1
          Perform CommDlgExtendedError-Dialog
      else
          Display "Call GetOpenFileNameA Successful"
          Display "File Title Selected = " OFN-Title
          display "complete file name  = " OFN-FileName
          DISPLAY "nMaxfile            = " nMaxFile
          display "nFileOffset         = " nFileOffset
          DISPLAY "lpstrFile           = " lpstrfile
       end-if.
```

#### ↳ Re: Need help with GetOpenFileName API Call

- **From:** Steve Biggs <steve_biggs@my-deja.com>
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7jo7cd$fd5$1@nnrp1.deja.com>`
- **References:** `<375e8003.4056112@news.icix.net>`

```
dblaze@merchants-fla.com wrote:
>  Browse-For-File.
>       move length of OFN-Struct    to lStructSize
…[9 more quoted lines elided]…
>       SET lpstrFile to address of OFN-FileName.

Doug,
I think the last line should come before the API call (ie set up
lpstrFile before making the call). Also, you should set nMaxFile to the
size of the buffer (ie 260).

Steve.


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

##### ↳ ↳ Re: Need help with GetOpenFileName API Call

- **From:** dblaze@merchants-fla.com (Doug Blaze)
- **Date:** 1999-06-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<375fbae8.84669368@news.icix.net>`
- **References:** `<375e8003.4056112@news.icix.net> <7jo7cd$fd5$1@nnrp1.deja.com>`

```
Hi Steve,

You are the man!  Upon reading the nMaxFile verbage again, you are
absolutely right - and it works too!  I found that if I did the 'SET
lpstrFile to address of OFN-FileName' BEFORE the call I got a
CDERR_INITIALIZATION error.  If I set it AFTER the call, I got the
dialog box but not the correct results.  nMaxFile does say it returns
FALSE if the size of OFN-Filename is too small to contain the name -
it would be since it's size was zero!  The error indicated not enough
memory but it didn't make much sense since I have 64K!  Now I know
it's referring to the size of the receiving item for the name of the
item!  Duh!

Thanks again.
Doug





>Doug,
>I think the last line should come before the API call (ie set up
…[7 more quoted lines elided]…
>Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
