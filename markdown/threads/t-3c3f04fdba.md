[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# microfocus cobol accessing htmlhelp instead of winhelp.

_2 messages · 2 participants · 2003-06 → 2003-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### microfocus cobol accessing htmlhelp instead of winhelp.

- **From:** jloskill@omdcorp.com (Jim Loskill)
- **Date:** 2003-06-12T10:23:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7e867a47.0306120923.73cfcb68@posting.google.com>`

```
We are currently calling winhelp using the following code:
           MOVE 1                     TO HELP-BOOL.
           MOVE API-HELP-CONTEXT-ID   TO HELP-CONTEXT-ID.
           MOVE API-HELP-FILE-PATH    TO HELP-FILE-PATH.
           SET HELP-FILE-PATH-POINTER TO ADDRESS OF HELP-FILE-PATH.
           MOVE HELP-CONTEXT          TO HELP-UINT.        

           CALL WINAPI "WinHelp" & ANSI USING
                                   BY VALUE API-HELP-HWND
                                            HELP-FILE-PATH-POINTER
                                            HELP-UINT
                                            HELP-CONTEXT-ID
               RETURNING HELP-BOOL.
We have converted our help files to .chm files and now would
like to call htmlhelp.
Has anyone accomplished this and how was it done??
Thanks for your time!
```

#### ↳ Re: microfocus cobol accessing htmlhelp instead of winhelp.

- **From:** Jussi Jumppanen <jussij@zeusedit.com>
- **Date:** 2003-07-09T12:11:15+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F0B79C3.1349@zeusedit.com>`
- **References:** `<7e867a47.0306120923.73cfcb68@posting.google.com>`

```
Jim Loskill wrote:

> We have converted our help files to .chm files and now would
> like to call htmlhelp.
> Has anyone accomplished this and how was it done??

I can not offer a definitive answer but I hopefully offer 
a step in the right direction:

In pure Win32 terms this is what the older WinHelp API looks like:

 BOOL WINAPI WinHelp(
   HWND     hwnd,      // handle of window requesting Help 
   LPCTSTR  lpszHelp,  // address of directory-path string 
   UINT     uCommand,  // type of Help 
   DWORD    dwData     // additional data 
   );

and this is what the new HTML API looks like:

 HWND WINAPI HtmlHelp(
    HWND hwndCaller,
    LPCSTR pszFile,
    UINT uCommand,
    DWORD_PTR dwData );

and below are some links that help explain how to use the 
new HtmlHelp API:

   http://helpware.net/
   http://keyWorks.net
   http://www.helpfulsolutions.com/
   http://mvps.org/htmlhelpcenter/

Jussi Jumppanen
Author of: Zeus for Windows, Win32 (Brief, Emacs, etc) FTP Text Editor
"The C/C++, Cobol, Java, FTP, Python, PHP, Perl programmer's editor"
Home Page: http://www.zeusedit.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
