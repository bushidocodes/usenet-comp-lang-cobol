[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling C from Cobol

_2 messages · 2 participants · 1998-02_

---

### Calling C from Cobol

- **From:** "kyle.h..." <ua-author-17075556@usenetarchives.gap>
- **Date:** 1998-02-18T09:10:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ceq46$8s3$1@nnrp1.dejanews.com>`

```

I am having difficulty calling C from Cobol. We have read all of the
documentation and even tried to use the sample code which calls a WINAPI.
Even this produces the error "Can't find program XXXXXX". It is a date time
function which calls the Kernel32.dll through a WINAPI. does anyone have any
experience doing this successfully????

Kyle Hagerman

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: Calling C from Cobol

- **From:** "daniel maltes" <ua-author-1025739@usenetarchives.gap>
- **Date:** 1998-02-18T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad0e9bc02-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6ceq46$8s3$1@nnrp1.dejanews.com>`
- **References:** `<6ceq46$8s3$1@nnrp1.dejanews.com>`

```

Kyle,
There are a couple of general guidelines I can suggest, however, the
specifics depend on your COBOL compiler(make sure you have the latest
version and documentation).
1. Calling convention - There are two calling conventions involved with
Windows external function libraries. The "C" convention and the "Pascal"
convention. Using the wrong convention will definatly cause the library to
fail. FYI: The Windows API uses the Pascal calling convention. Sounds
strange since the libraries are written in C, but I guess old windows habits
are hard to break.
2. You may need to "declare" the functions by calling the library first.
ie. call "myfuncs.dll". This declares the functions in "myfuncs.dll" as
available(callable) in your COBOL program.
3. Your COBOL compiler may or may not support both the unicode and ansi
function types. For instance, the Windows API "ShellExecute" function is a
unicode type, but it also has an alias ansi type called "ShellExecuteA". I
think you'll find most COBOL compilers support the ansi types.
4. Make sure your passing the correct data types to the function. This
has alot to do with which version of Windows your using(Win16 or Win32) and
your COBOL compiler or runtime. Under Win16 most numeric data types are
passed as 'short integers'(2 bytes) while Win32 expects 'long integers'(4
bytes). However, there are COBOL compilers and runtimes that can use just
the 'integer' data type and adjust it's size to 2 or 4 bytes depending on
the host platform.
5. Passing data by reference or by value - When calling a function it is
imperative that you either pass the "value" of a variable or pass a memory
address "pointer". By reference passes the pointer and it used mostly with
passing strings. By value passes an actual value and is used with numerics.

Once again, the specific ways to accomplish the above guidelines are
dependant upon your COBOL compiler. I work with Acucobol-GT compiler and
runtime version 3.21.

Here's an example call to kernel32.dll to get the windows, system, temporary
directory paths:

IDENTIFICATION DIVISION.
PROGRAM-ID. GETPATH.
AUTHOR. Dan Maltes.
DATE-WRITTEN. 2/19/1998.
REMARKS. Call Win32 API to get windows, system, temp directories.
ENVIRONMENT DIVISION.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-BUFFER PIC X(255).
01 WS-SIZE USAGE UNSIGNED-INT.
01 RETURN-VALUE USAGE UNSIGNED-INT.

PROCEDURE DIVISION.
MAIN-LOGIC SECTION.
*Set dll-convention to pascal calling convention.
*Win32 api requires pascal calling convention.
SET ENVIRONMENT "DLL-CONVENTION" TO 1.
*Load the dll so it's functions are available.
CALL "KERNEL32.DLL".
PERFORM GET-WIN-PATH.
PERFORM GET-WIN-SYS-PATH.
PERFORM GET-WIN-TEMP-PATH.
ACCEPT OMITTED TAB.
STOP RUN.

WIN-API-FUNCTIONS SECTION.
GET-WIN-PATH.
*Call the ansi alias GetWindowsDirectoryA function.
MOVE NULL TO WS-BUFFER.
SET WS-SIZE TO SIZE OF WS-BUFFER.
*Leave room for the terminating null byte.
SUBTRACT 1 FROM WS-SIZE.
CALL "GetWindowsDirectoryA" USING
BY REFERENCE WS-BUFFER
BY VALUE WS-SIZE
RETURNING RETURN-VALUE
ON EXCEPTION
DISPLAY "Can't run GetWindowsDirectoryA function."
LINE 1 COL 1, " Return Value: " RETURN-VALUE
NOT ON EXCEPTION
DISPLAY "Windows path: " LINE 1 COL 1 WS-BUFFER.

GET-WIN-SYS-PATH.
*Call the ansi alias GetSystemDirectoryA function.
MOVE NULL TO WS-BUFFER.
SET WS-SIZE TO SIZE OF WS-BUFFER.
*Leave room for the terminating null byte.
SUBTRACT 1 FROM WS-SIZE.
CALL "GetSystemDirectoryA" USING
BY REFERENCE WS-BUFFER
BY VALUE WS-SIZE
RETURNING RETURN-VALUE
ON EXCEPTION
DISPLAY "Can't run GetSystemDirectoryA function."
LINE 2 COL 1, " Return Value: " RETURN-VALUE
NOT ON EXCEPTION
DISPLAY "Windows Sys path: " LINE 2 COL 1 WS-BUFFER.

GET-WIN-TEMP-PATH.
*Call the ansi alias GetTempPathA function.
INITIALIZE WS-BUFFER.
MOVE NULL TO WS-BUFFER.
SET WS-SIZE TO SIZE OF WS-BUFFER.
*Leave room for the terminating null byte.
SUBTRACT 1 FROM WS-SIZE.
CALL "GetTempPathA" USING
BY VALUE WS-SIZE
BY REFERENCE WS-BUFFER
RETURNING RETURN-VALUE
ON EXCEPTION
DISPLAY "Can't run GetTempPathA function."
LINE 3 COL 1, " Return Value: " RETURN-VALUE
NOT ON EXCEPTION
DISPLAY "Windows Temp path: " LINE 3 COL 1 WS-BUFFER.


Dan Maltes
Development Director
Applied Systems Technology

kyl··.@lon··e.com wrote in message
<6ceq46$8s3$1.··.@nnr··s.com>...
› I am having difficulty calling C from Cobol.  We have read all of the
› documentation and even tried to use the sample code which calls a WINAPI.
…[9 more quoted lines elided]…
› http://www.dejanews.com/   Now offering spam-free web-based newsreading
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
