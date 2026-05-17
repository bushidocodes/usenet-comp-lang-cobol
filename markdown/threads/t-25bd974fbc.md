[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM/Cobol help

_2 messages · 2 participants · 1998-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### RM/Cobol help

- **From:** "jjs..." <ua-author-894218@usenetarchives.gap>
- **Date:** 1998-06-04T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998060518560800.OAA27871@ladder03.news.aol.com>`

```

I am a retired mainframe systems analyst who is trying to help an accounting
firm analyze their RM/Cobol code for Y2K compliance. I would be interested in
knowing of any tools to help cut down investigating Y2K compliance. I am very
familiar with the Y2K aspects and tools on mainframe Cobol applications but
need some help in regards to RM/Cobol running on a 386 machine under DOS.
```

#### ↳ Re: RM/Cobol help

- **From:** "chip ling" <ua-author-6589301@usenetarchives.gap>
- **Date:** 1998-06-05T15:46:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-25bd974fbc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1998060518560800.OAA27871@ladder03.news.aol.com>`
- **References:** `<1998060518560800.OAA27871@ladder03.news.aol.com>`

```

Jjsafer wrote:
› 
› I am a retired mainframe systems analyst who is trying to help an accounting
…[3 more quoted lines elided]…
› need some help in regards to RM/Cobol running on a 386 machine under DOS.

Try my batch program search.bat.

It has the limitation that the search string cannot contains space but
it
helps me a lot on DOS machine. Of course it cannot compare with ISPF
3.14
but it works. I believe you need this to search for the string DATE.

Here is the code ***

@echo off
rem /*******************************************/
rem /* Search batch program version 2.00 */
rem /* by Chip Ling */
rem /*******************************************/
set search=

if "%2"=="" goto :usage
if "%3"=="/s" goto :screen
if "%3"=="/S" goto :screen
if "%3"=="" goto :set3
set search=%3
goto :file

:set3
set search=search.txt
goto :file

:file
echo. > %search%
for %%f in (%2) do find /n /i "%1" %%f >> %search%
echo. >> %search%
echo *** End of Search *** >> %search%
goto :end

:screen
for %%f in (%2) do find /n /i "%1" %%f
goto :end

:usage
echo.
echo Usage: search [string] [path\filename] [/s]
echo with the /s option, output goes to screen
echo without the /s option, output goes to search.txt
echo user can override the default file name by entering one.
echo.
echo Example 1: search move c:\cobol\source\*.cbl
echo It will search the string "move" from
echo c:\cobol\source\*.cbl and output the result
echo to the screen.
echo.
echo Example 2: search move c:\cobol\source\*.cbl /s
echo Output to the default output search.txt
echo.
echo Example 2: search move c:\cobol\source\*.cbl result.txt
echo Output to the file result.txt
echo.

:end
echo.

Code ends here***

Rgds,
Chip Ling
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
