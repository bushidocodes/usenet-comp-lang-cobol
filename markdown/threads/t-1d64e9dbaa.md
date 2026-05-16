[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# WIN API from COBOL help needed.

_7 messages · 3 participants · 2000-05_

---

### WIN API from COBOL help needed.

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3931b4d0.30839459@news.cox-internet.com>`

```
The COBOL compiler is Fujitsu v5, but it really doesn't matter - if
you have an example so I can decode the WinAPI for this, it will be
helpful.

I can't use CBL_OPEN_FILE because I need to "seek" within this file
and there are no "SEEK" routines in Fujitsu.  The main goal is to
duplicate the Ca-Realia DOS routines with WinAPI calls.

I am trying to call "CreateFileA".  My call parms seem to match the
desired setup as I get a link of CreateFileA@28 into my executeable.
However, when I call, I always get a "13" when I call GetLastError to
see why my handle was not created. (13 is "The Data is Invalid")

I am using CreateFile to open an existing file.  The documentation I
went from for calling this API is located here:

http://msdn.microsoft.com/library/psdk/winbase/filesio_4lf7.htm

Then click on CreateFile.

I had to go to the header files to get what I needed for the different
parms, but here is what I am passing:

Null terminated file name.

I want read access, so for DesiredAccess I am passing X"800000"
(Exactly as shown in WINnt.h) - Is this the right translation?  I
think so.

Share mode - X"00000003".  Adding 1 and 2 for read and write access.

Security Attributes - passing a null pointer.

Creation and Disposition - I have as a COMP-5 field with a value of 3.
I'm concerned about this one as it's defined in Winbase.h as follows:

#define CREATE_NEW          1
#define CREATE_ALWAYS       2
#define OPEN_EXISTING       3
#define OPEN_ALWAYS         4
#define TRUNCATE_EXISTING   5

Since it is passed as a DWORD I tried it as a COMP-5 which yields 

X"0300" -- but I also tried X"0003" and got the same results.

Template File is set to X"0000".

So, anyone know what I'm doing wrong to yield a 13?  I'm sure it's a
fundamental assumption about the API.

Thanks!
```

#### ↳ Re: WIN API from COBOL help needed.

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I3lY4.113798$55.2518222@news2.rdc1.on.home.com>`
- **References:** `<3931b4d0.30839459@news.cox-internet.com>`

```
Here's some of my code for Micro Focus COBOL. It should adapt.

 78  INVALID-HANDLE-VALUE            value h"FFFFFFFF".
 78  GENERIC-READ                    value h"80000000".
 78  OPEN-EXISTING                   value 3.
 78  FILE-ATTRIBUTE-NORMAL           value h"00000080".
 78  PAGE-READONLY                   value h"02".
 78  FILE-MAP-READ                   value h"0004".               .
     Call APIentry "CreateFileA" using
         by reference     cScanFileName
         by value         GENERIC-READ size 4
         by value         0 size 4
         by value         0 size 4
         by value         OPEN-EXISTING size 4
         by value         FILE-ATTRIBUTE-NORMAL size 4
         by value         0 size 4
         returning        hScanFile
     End-Call

I didn't look at your MSDN reference so this may be redundant information
but you'll have to also use CreateFileMappingA() and MapViewOfFile() to
acquire a physical address for the file handle.

- Karl


"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:3931b4d0.30839459@news.cox-internet.com...
> The COBOL compiler is Fujitsu v5, but it really doesn't matter - if
> you have an example so I can decode the WinAPI for this, it will be
…[50 more quoted lines elided]…
>
```

##### ↳ ↳ Re: WIN API from COBOL help needed.

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393268fb.76969203@news.cox-internet.com>`
- **References:** `<3931b4d0.30839459@news.cox-internet.com> <I3lY4.113798$55.2518222@news2.rdc1.on.home.com>`

```
I made some progress (I think) but I still have not gotten there.
Now, I an gettig an error code back of 87 - which is "invalid parm".
So I tried one of the file names mentioned, which is \\.A:

And I get a 2 for a return code - file not found.  

For filename I have been putting in "C:\TEST\TEST.TXT" and
terminateing it with a low value.  This gives the the 87.  I'm
assuming I have something malconstructed with the path.  In your code
do you open any disk files this way?  If so, what are you using for a
filename?

Thanks!


On Mon, 29 May 2000 03:00:56 GMT, "Oscar T. Grouch" <dustbin@home.com>
wrote:

>Here's some of my code for Micro Focus COBOL. It should adapt.
>
…[80 more quoted lines elided]…
>
```

##### ↳ ↳ Re: WIN API from COBOL help needed.

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3932752c.80090753@news.cox-internet.com>`
- **References:** `<3931b4d0.30839459@news.cox-internet.com> <I3lY4.113798$55.2518222@news2.rdc1.on.home.com>`

```
I'm back to thinking I have the file name correct, but something else
is wrong.  When I was getting the "13" on return it was because I
wasn't really passing any values - I forgot to put "by value" on the
call.

I've looked at some other Fujitsu examples of API calls, and the
socket stuff I did, and I can't see anything obviously worng with the
following code, but it always returns an 87 - invalid parm.  I tried
to duplicate your example as best I could.  Fujitsu only allows
passing by value when the data item is a COMP-5 item of 4 bytes or
less.  It seems to work for other API calls.

Here's my code.  Show me the stupid mistake.  Thanks.

 @OPTIONS ALPHAL(WORD),MAIN,TEST
 IDENTIFICATION DIVISION.
 PROGRAM-ID     TESTCALL.
*-----------------------------------------------------------------
 DATA DIVISION.
 WORKING-STORAGE SECTION.
 01  FILENAME                    PIC X(79).
 01  DESIREDACCESS               PIC S9(9) COMP-5.
 01  DESIREDACCESS-X REDEFINES DESIREDACCESS PIC X(4).
     88  F-READ-ONLY             VALUE X"80000000".
     88  F-WRITE-ONLY            VALUE X"40000000".
     88  F-READ-WRITE            VALUE X"C0000000".
 01  NULL-VALUE                  PIC S9(9) COMP-5.
 01  CREATIONDISPOSITION         PIC S9(9) COMP-5.
     88  OPEN-EXISTING                VALUE 3.
 01  FLAGSANDATTRIBUTES          PIC S9(9) COMP-5.
 01  FLAGSANDATTRIBUTES-X REDEFINES FLAGSANDATTRIBUTES     PIC X(4).
     88  FILE-ATTRIBUTE-NORMAL        VALUE X"00000080".
 01  ERROR-CODE                  PIC S9(9)                 COMP-5.
 01  F-NAME.
     03  FILLER PIC X(15) VALUE "C:\AUTOEXEC.BAT".
     03  FILLER PIC X     VALUE LOW-VALUE.
 01  L-HANDLE   PIC S9(9) COMP-5.
 PROCEDURE DIVISION. 
     SET F-READ-ONLY TO TRUE 
     SET OPEN-EXISTING TO TRUE
     SET FILE-ATTRIBUTE-NORMAL TO TRUE
     CALL "CreateFileA" WITH STDCALL USING 
                             BY REFERENCE  F-NAME
                             BY VALUE      DESIREDACCESS
                                           NULL-VALUE
                                           NULL-VALUE
                                           CREATIONDISPOSITION
                                           FLAGSANDATTRIBUTES
                                           NULL-VALUE
                                     RETURNING L-HANDLE.
     IF L-HANDLE = -1
        CALL "GetLastError" WITH STDCALL
                                 RETURNING ERROR-CODE.
     GOBACK.



On Mon, 29 May 2000 03:00:56 GMT, "Oscar T. Grouch" <dustbin@home.com>
wrote:

>Here's some of my code for Micro Focus COBOL. It should adapt.
>
…[80 more quoted lines elided]…
>
```

##### ↳ ↳ Re: WIN API from COBOL help needed.

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3932cb6e.102176218@news.cox-internet.com>`
- **References:** `<3931b4d0.30839459@news.cox-internet.com> <I3lY4.113798$55.2518222@news2.rdc1.on.home.com>`

```
On Mon, 29 May 2000 03:00:56 GMT, "Oscar T. Grouch" <dustbin@home.com>
wrote:

>Here's some of my code for Micro Focus COBOL. It should adapt.


All the help I was able to get just confirmed I was doing it right.
(Thanks Karl, just reading your questions about what I was doing
helped me figure this out -- or at least attempt the illogical).  
The one "wierdness" is that Fujitsu wants you to pass things "by 
value" which I knew.  I had it setup to pass by value, but was 
getting a return code (After I found the initial problem) of 87 -
which 
is a "bad parm".  

Basically it boiled down to that I was surrounded by endians.  <G>

When the Windows API says something has a hex value of 

x"80000000" what it REALLY means is that when you look at the 
bytes, its X"00000080".  Once I figured that out, I was OK.

Fujitsu is picky about putting numbers in numeric fields however, 
and I don't want to take a chance with accidently scalping my 
endians, so I am going to do the following:

01  DESIREDACCESS Pic s9(9) comp-5.
01  DESIREDACCESS-C4 Pic S9(9) COMP-4.
01  DESIREDACCESS-X REDEFINES DESIREDACCESS-C4 PIC 
X(4).
    88  F-READ-ONLY PIC X"80000000".
    88  F-WRITE-ONLY PIC X"40000000".
    88  F-READ-WRITE PIC X"C0000000".

Then in the code ---

Set F-READ-ONLY to TRUE
COMPUTE DESIRED-ACCESS = DESIRED-ACCESS-C4

That's me you see there jumping through flaming windows hoops.

BTW - it's obvious that MicroFocus hides a lot of this complexity from
you.  A good thing, I think.

--PS - Don't jump me for redefining 01 levels Judson - I'll clear it
up in the actual code so that isn't there.
```

###### ↳ ↳ ↳ Re: WIN API from COBOL help needed.

- **From:** khansen@screenio.com (Kevin Hansen)
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3932d077.4413095@wingate>`
- **References:** `<3931b4d0.30839459@news.cox-internet.com> <I3lY4.113798$55.2518222@news2.rdc1.on.home.com> <3932cb6e.102176218@news.cox-internet.com>`

```
On Mon, 29 May 2000 19:59:59 GMT, thaneH@softwaresimple.com (Thane
Hubbell) wrote:

>Basically it boiled down to that I was surrounded by endians.  <G>
>
…[3 more quoted lines elided]…
>bytes, its X"00000080".  Once I figured that out, I was OK.

Thane,

A tip for the future:

You might convert the values in the C headers as hex (e.g., H'00FF'
which translates directly from the C numeric values) instead of as
straight literals (X'FF00") - which, as you discovered, need to be
reversed from the C numeric definitions.  This can be quite confusing.


 You need to define the values as numeric if you do this, of course:  

01  MY-C-VALUE PIC S9(9) COMP-5 VALUE H'00FF'.

Of course, then you eventually run into bit definitions, which REALLY
take some head-scratching!

Have fun,

Kevin
NORCOM COBOL Programming Tools
GUI ScreenIO; a cool COBOL/Windows Screen Manager
http://www.ScreenIO.com
```

###### ↳ ↳ ↳ Re: WIN API from COBOL help needed.

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39330ec1.119413641@news.cox-internet.com>`
- **References:** `<3931b4d0.30839459@news.cox-internet.com> <I3lY4.113798$55.2518222@news2.rdc1.on.home.com> <3932cb6e.102176218@news.cox-internet.com> <3932d077.4413095@wingate>`

```
On Mon, 29 May 2000 20:24:40 GMT, khansen@screenio.com (Kevin Hansen)
wrote:

> You need to define the values as numeric if you do this, of course:  
>
>01  MY-C-VALUE PIC S9(9) COMP-5 VALUE H'00FF'.
>

Ah, but this is where Fujitsu played tight with the standard.  The
above is invalid!  One must put a NUMBER in there, in order for it to
be valid.  

>Of course, then you eventually run into bit definitions, which REALLY
>take some head-scratching!
>

When I do, I'll know who to call!  <G>

>Have fun,
>
>Kevin

Oh, I've had my fun now -- now I'm going to work!  Thanks Kevin.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
