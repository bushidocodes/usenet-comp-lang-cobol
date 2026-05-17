[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Error 173 with WinApi

_8 messages · 8 participants · 1998-08_

---

### Error 173 with WinApi

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1998-08-14T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6r3ltn$3oau$1@news-inn.inet.tele.dk>`

```
MicroFocus has a sample to show how to load a bitmap. When I animate the
program I get: error 173 - called program file not found in drive/directory,
at this call:

1.1 CALL WinAPI "SetWindowPos"
1.1 USING BY VALUE WS-API-Win-Handle
1.1 BY VALUE Win-TopMost SIZE 2
1.1 BY VALUE 0 SIZE 2
1.1 BY VALUE 0 SIZE 2
1.1 BY VALUE 0 SIZE 2
1.1 BY VALUE 0 SIZE 2
1.1 BY VALUE 3 SIZE 2
1.1 END-CALL

My platform is Win95. Can it bee because the function "SetWindowPos" now has
anorther name?

f.··.@l··.dk
```

#### ↳ Re: Error 173 with WinApi

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1998-08-14T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7bcef99a07-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6r3ltn$3oau$1@news-inn.inet.tele.dk>`
- **References:** `<6r3ltn$3oau$1@news-inn.inet.tele.dk>`

```
In message <<6r3ltn$3oau$1.··.@new··e.dk>> writes:
› program I get: error 173 - called program file not found in drive/directory,
› at this call:
…[12 more quoted lines elided]…
› anorther name?

SetWindowPos is a Windows API call. Do you use any other API
calls in your program ? If not then it is probably failing
because your program needs to be linked with WIN.LIB statically
or with GDIand/or USER dynamically at run time.
```

#### ↳ Re: Error 173 with WinApi

- **From:** "leif svalgaard" <ua-author-6445756@usenetarchives.gap>
- **Date:** 1998-08-14T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7bcef99a07-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6r3ltn$3oau$1@news-inn.inet.tele.dk>`
- **References:** `<6r3ltn$3oau$1@news-inn.inet.tele.dk>`

```
no it has the name you used, but it should have been included at link time.
You cannot call the WinApi as if they were dynamic programs.

f.··.@l··.dk wrote in message <6r3ltn$3oau$1.··.@new··e.dk>...
› MicroFocus has a sample to show how to load a bitmap. When I animate the
› program I get: error 173 - called program file not found in
…[20 more quoted lines elided]…
›
```

#### ↳ Re: Error 173 with WinApi

- **From:** "gene webb" <ua-author-6589136@usenetarchives.gap>
- **Date:** 1998-08-14T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7bcef99a07-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6r3ltn$3oau$1@news-inn.inet.tele.dk>`
- **References:** `<6r3ltn$3oau$1@news-inn.inet.tele.dk>`

```
I have run into this problem a couple of time. One thing that works is to
manually load the DLL by doing something like:

01 myProcedurePointer pointer.
01 myDLL pic x(20) value 'somename.dll'.

SET myProcedurePointer TO myDLL.

Do this at the beginning of the program and you can get past the call.


f.··.@l··.dk wrote in message <6r3ltn$3oau$1.··.@new··e.dk>...
› MicroFocus has a sample to show how to load a bitmap. When I animate the
› program I get: error 173 - called program file not found in
…[20 more quoted lines elided]…
›
```

#### ↳ Re: Error 173 with WinApi

- **From:** "tommy nilsen" <ua-author-17072129@usenetarchives.gap>
- **Date:** 1998-08-19T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7bcef99a07-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6r3ltn$3oau$1@news-inn.inet.tele.dk>`
- **References:** `<6r3ltn$3oau$1@news-inn.inet.tele.dk>`

```
Try
Call "cob32api.dll"
before you make any other calls.

Let me know if your'e having more problems suing the API's.

Tommy Nilsen

f.··.@l··.dk wrote:

› MicroFocus has a sample to show how to load a bitmap. When I animate the
› program I get: error 173 - called program file not found in drive/directory,
…[15 more quoted lines elided]…
› f.··.@l··.dk
```

##### ↳ ↳ Re: Error 173 with WinApi

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1998-08-19T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7bcef99a07-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7bcef99a07-p5@usenetarchives.gap>`
- **References:** `<6r3ltn$3oau$1@news-inn.inet.tele.dk> <gap-7bcef99a07-p5@usenetarchives.gap>`

```
tommy nilsen wrote:

› Try
› Call "cob32api.dll"
…[4 more quoted lines elided]…
› Tommy Nilsen

Tommy:

I tried to sue the API's, but my case was thrown out of court.



Bob Wolfe, flexus, rtwolfe at spammers-are-meat-heads flexus dot com
To reply, look at my e-mail address, get rid of the spammer insult and fix the address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Error 173 with WinApi

- **From:** "hi..." <ua-author-6589743@usenetarchives.gap>
- **Date:** 1998-08-23T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7bcef99a07-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7bcef99a07-p6@usenetarchives.gap>`
- **References:** `<6r3ltn$3oau$1@news-inn.inet.tele.dk> <gap-7bcef99a07-p5@usenetarchives.gap> <gap-7bcef99a07-p6@usenetarchives.gap>`

```
On Thu, 20 Aug 1998 17:21:55 GMT, rtw··.@fle··s.com (Bob Wolfe)
wrote:

› tommy nilsen  wrote:
› 
…[17 more quoted lines elided]…
› 
You may want to try putting this in your code:

ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SPECIAL-NAMES.
CALL-CONVENTION 74 IS WINAPI.

I use it for calling Windows Help 4.0 API's.

Guy
```

###### ↳ ↳ ↳ Re: Error 173 with WinApi

_(reply depth: 4)_

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-08-24T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7bcef99a07-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7bcef99a07-p7@usenetarchives.gap>`
- **References:** `<6r3ltn$3oau$1@news-inn.inet.tele.dk> <gap-7bcef99a07-p5@usenetarchives.gap> <gap-7bcef99a07-p6@usenetarchives.gap> <gap-7bcef99a07-p7@usenetarchives.gap>`

```
To All who have/had error 173 problems in win32 API (that includes me),

The following program, allthough still functionally under construction, showed to work Built
using NetExpress, running under Windows '95 in connection to an NT server. It calls the
functions from Windows API *dynamically*. Hence it contains:
- Call conventional directives (See special-names)
- Setup for api-usage (cob32api dll activation)
- Dynamic load (once) and calling (many) of a module using dll technics,
- Calls to API functionality (GetUserName)
- Linking directives ($SET and special-names)
and it works.

No time to snip the irrelevants out, just giving it to play with.

Good luck

The COBOL Frog

------------------CODE FOLLOWS ------------------

$SET USE(SQL)
$SET CASE
Identification division.
Program-id. DBM.



Environment division.
Configuration section.
Special-names.
Decimal-point is comma
Call-convention 74 is Win32API.



Data division.
Working-storage section.

Exec SQL
Begin declare section
End-Exec

Exec SQL
Include SQLCA
End-exec

01 Switches.
*--- Have we ever been called before? (Initially NO)
03 pic X(1) value "F".
88 FirstTimeCall value "F".
88 SubsequentCall value "S".
*--- Did we ever ask the user-id? (Initially NO)
03 pic X(1) value "?".
88 NTUserIdIsAsked value "!".
88 NTUserIDNotAsked value "?".
*--- Did we ever load DBM2? (Initially NO)
03 pic X(1) value "N".
88 DBM2Loaded value "L".
88 DBM2NotLoaded value "N".
*--- Are we connected to the DB? (Initially NO)
03 pic X(1) value "D".
88 Connected value "C".
88 NotConnected value "D".
88 DisConnected value "D".

01 usage is procedure-pointer.
03 ppDBM2.
03 ppCOB32API.

77 ReturnCode pic X(2) comp-5.
77 LastErrorCode pic X(4) comp-5.

01 LogonData.
03 DB-LogonParameter.
Copy SVCPWD.
03 ScrambleData.
05 StringLength pic 9(3).
05 ResultString pic X(100).
03 UserPasswordString pic X(201).

Linkage section.

01 DBM-Parameter.
Copy DBM-Param.
01 SecondIncomingParameter pic X.

01 SecondOutgoingParameter pic X.

Exec SQL
End declare section
End-Exec



Procedure division using DBM-Parameter,
SecondIncomingParameter.

Main.
*--- Some initial activities ...
Perform InitialProcessing

*--- See what the caller wants from me ...
Evaluate function Upper-Case (FUNCTION-CALL-P1)
When "SVC"
Evaluate function Upper-Case (FUNCTION-CALL-P2)
When "CON"
Perform ExplicitDBLogon
When "DIS"
Perform ExplicitDBLogoff
When "UID"
Perform GetNTUserId
When other
Perform RegularDBFunction
End-evaluate
When other
Perform RegularDBFunction
End-evaluate

Goback
.


InitialProcessing.
*--- Let's start thinking positively ...
Set DBM-STATUS-OKE to true
Move zero to DBM-SQLCODE
*--- Most times we pass thru the 2nd parameter,
* see for example explicit data base logon.
Set address of SecondOutgoingParameter
to address of SecondIncomingParameter
*--- Some things to be done just once at the first call
If (FirstTimeCall)
Then
Perform OnlyOnceProcessing
End-if
.


OnlyOnceProcessing.
*--- Make Windows 32 bit API available
Call "COB32API"
*--- When no user-id is given, try to get it ourself
If (DBM-NT-USER-ID = spaces or low-values)
Then
Perform GetNTUserId
*------- This implicit functionality should not disturb the
* caller, which may even be not interested in the user-id
If (DBM-STATUS-OK
or
DBM-STATUS-NO-SERVER-CONNECTION)
Then
Continue
Else *> Ignore errors on this try
Set DBM-STATUS-OK to true
End-if
End-if
*--- Remember now that we have been in this program before
Set SubsequentCall to true
.


GetNTUserId.
*--- Ask Windows for the user-id
Call Win32API "GetUserNameA"
using by reference DBM-NT-USER-ID
by value 20 size 4
returning ReturnCode
*--- Remember we've tried it!
Set NTUserIdIsAsked to true
*--- Check result
If (ReturnCode = zero)
Then
Call Win32API "GetLastError" returning LastErrorCode
Move LastErrorCode to DBM-SQLCODE
Evaluate LastErrorCode
When 1245
Set DBM-STATUS-NO-SERVER-CONNECTION to true
When other
Set DBM-STATUS-UNKNOWN-ERROR to true
End-evaluate
End-if
.


ExplicitDBLogon.
*--- See if logon is possible
If (Connected)
Then
Set DBM-STATUS-ALREADY-CONNECTED to true
Exit paragraph
End-if
*--- If we have no user-id yet, let's try to get it now
Evaluate true
When not (DBM-NT-USER-ID = spaces or low-values)
Continue
When (NTUserIDIsAsked)
Set DBM-STATUS-NO-USER-ID-AVAILABLE to true
Exit paragraph
When other
Perform GetNTUserId
If not (DBM-STATUS-OK)
Then
Exit paragraph
End-if
End-evaluate
*--- Now we need the password for this user-id
Move "SVCPWD" to FUNCTION-CALL
Move DBM-NT-USER-ID to NT-USER-ID in LogonData
* - We pass our own 2nd parameter i.s.o. the one that came in
Set address of SecondOutgoingParameter
to address of DB-LogonParameter
* - Now we call on
Perform PassOnToDBM2
* - And switch back to the original incoming 2nd parameter
Set address of SecondOutgoingParameter
to address of SecondIncomingParameter
*--- See if all this worked out well
If not (DBM-STATUS-OK)
Then
Exit paragraph
End-if
*--- Now we have the NT user-id,
* the Database user-id
* and the Database password,
* all in the LogonData structure.
* The password however is scrambled.
* So we need to de-scramble it
Move function Length (DBM-NT-USER-ID)
to StringLength in ScrambleData
Call "DBM-Scramble" using StringLength in ScrambleData,
NT-USER-ID in LogonData,
DB-PASSWORD in LogonData,
ResultString in ScrambleData
*--- Time to connect to the data base using the login data
Initialize UserPasswordString
String DB-USER-ID in LogonData delimited by space,
"." delimited by size,
ResultString in ScrambleData delimited by space
into UserPasswordString
Exec SQL
Connect to 'Pechiney' user :UserPasswordString
End-exec
*--- Now we are almost ready, but for maximum security, we first
* blank out all the memory areas that contain login data
Initialize LogonData,
ScrambleData,
UserPasswordString
*--- At last we examine the result of the SQL connect
Move SQLCODE to DBM-SQLCODE
If (SQLCODE = zero)
Then
Set DBM-STATUS-OKE to true
Set Connected to true
Else
Set DBM-STATUS-CONNECT-FAILED to true
End-if
.


ExplicitDBLogoff.
*--- See if logoff is possible
If (DisConnected)
Then
Set DBM-STATUS-CONNECTION-LOST to true
Exit paragraph
End-if
*--- Logoff
Exec SQL
Disconnect current
End-exec
Move SQLCODE to DBM-SQLCODE
If (SQLCODE = zero)
Then
Set DBM-STATUS-OKE to true
Set DisConnected to true
Else
Set DBM-STATUS-DISCONNECT-FAILED to true
End-if
.


RegularDBFunction.
*--- Connect to the database, if not yet done
If (DisConnected)
Then
Perform ExplicitDBLogon
End-if
Perform PassOnToDBM2
.


PassOnToDBM2.
*--- Only once needed: get DBM2 dll into memory (LoadLibray)
If (DBM2NotLoaded)
Then
Set ppDBM2 to entry "DBM2"
Set DBM2Loaded to true
End-if
*--- Dynamic call to server module
Call "DBM2" using DBM-Parameter,
SecondOutgoingParameter
.

End program DBM.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
