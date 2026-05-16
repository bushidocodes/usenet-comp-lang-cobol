[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# GetUserName in NetExpress

_5 messages · 3 participants · 1998-12_

---

### GetUserName in NetExpress

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36669F61.58E48F10@IMN.nl>`

```
Dear Readers.

We, my collegue (Martin) and I (The Frog) keep getting problems when we
try to "read" the userid in our Win'95 application that we are building
using NetExpress v2.0 from Micro Focus. It is probably a
misunderstanding of the Windows (32 bit) API, but our implementation of
the GetUserName call fails. GetLastError yields error 1245 which is
documented in the Win32 SDK as:

" The operation being requested was not performed because the user has
not logged on to the network. The specified service does not exist.".

We reduced the problem source to one little small program. Please help
us making it function!
Martin & Huib


        $SET CASE
        $SET NOFOLDCALLNAME
        Identification division.
        Program-id. GetUserInfo.
        Environment division.
        Configuration section.
        Special-names.
            Call-convention 74 is Win32API.
        Data division.
        Working-storage section.
        77  ReturnCode                  pic X(02)  comp-5.
        77  LastErrorCode               pic X(04)  comp-5.
        77  UserId                      pic X(21).
        77  NullPos                     pic X(02)  comp-5.
        Procedure division.
        Main.
       *--- Make Windows 32 bit API available
            Call "COB32API"
       *--- Ask Windows for the user-id
            Move x"00" to UserId(1:1)
            Call Win32API "GetUserNameA"
                          using  by reference UserId
                                 by value     20 size 4
                       returning              ReturnCode
       *--- Check & show result
            Display "Rc = ", ReturnCode
            If (ReturnCode = zero)
            Then
                Call Win32API "GetLastError" returning LastErrorCode
                Display "Errcode = ", LastErrorCode
            Else
                Initialize NullPos
                Inspect UserId tallying NullPos
                    for characters before initial low-value
                Display "UserId = '" UserId(1:NullPos) "'"
            End-if
       *--- Quit processing
            Goback
            .
        End program GetUserInfo.
```

#### ↳ Re: GetUserName in NetExpress

- **From:** "Karl Wagner" <kewagner@home.com>
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Hrx92.133$hV5.274750@news.rdc1.on.wave.home.com>`
- **References:** `<36669F61.58E48F10@IMN.nl>`

```
I don't know where you got the prototype for the call to GetUserName but my
SDK reference says the call is supposed to look like this:

 01  szUserName          pic x(80) value low-value.
 01  iUserNameLen        pic 9(9) comp-5 value 0.
 01  bResult             pic 9(9) comp-5 value 0.
   88  RESULT-TRUE                       value 1.
   88  RESULT-FALSE                      value 0.
 01  iError              pic 9(9) comp-5 value 0.
 01  iErrorDisp          pic 9(9)        value 0.

     Move LENGTH OF szUserName to iUserNameLen
     Call APIentry "GetUserNameA" using
         by reference szUserName
         by reference iUserNameLen
         returning    bResult
     End-Call
     If RESULT-TRUE
         Display szUserName
     Else
         Call APIentry "GetLastError"
             returning       iError
         End-Call
         Move iError to iErrorDisp
         Display iError
     End-If
     .



COBOL Frog (Huib Klink) wrote in message <36669F61.58E48F10@IMN.nl>...
>Dear Readers.
>
<<SNIP>>
>--
>Dut: Vandaag is de eerste dag van de rest van je leven! Denk eens na!
…[11 more quoted lines elided]…
>
```

##### ↳ ↳ Re: GetUserName in NetExpress

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3667A202.17ADC0C4@IMN.nl>`
- **References:** `<36669F61.58E48F10@IMN.nl> <Hrx92.133$hV5.274750@news.rdc1.on.wave.home.com>`

```
Karl Wagner wrote:

> I don't know where you got the prototype for the call to GetUserName but my
> SDK reference says the call is supposed to look like this:

8< [snipped, see org. msg.]

Success!!! Thanks Karl

In essence, two errors where made by me:
1) I passed the length by value i.s.o. by reference.
2) The returncode data item was 2 i.s.o. 4 bytes long.

The LENGTH OF special register (IBM extension lso supported in NetExpress) was
changed to FUNCTION LENGTH OF to get as standards conforming as possible. So
now the following is the resulting *working* source:

$SET CASE
$SET NOFOLDCALLNAME
Identification division.
Program-id. GetUserInfo.
Environment division.
Configuration section.
Special-names.
    Call-convention 74 is Win32API
    .
Data division.
Working-storage section.
77  UserId                      pic X(21).
77  UserIdLen                   pic X(04)  comp-5.
77  ReturnCode                  pic X(04)  comp-5.
77  LastErrorCode               pic X(04)  comp-5.
77  NullPos                     pic X(02)  comp-5.
Procedure division.
Main.
--- Make Windows 32 bit API available
    Call "COB32API"
--- Ask Windows for the user-id
    Move x"00" to UserId(1:1)
    Move function length (UserId) to UserIdLen
    Call Win32API "GetUserNameA"
                  using  by reference UserId
                         by reference UserIdLen
               returning              ReturnCode
--- Check & show result
    Display "Rc = ", ReturnCode
    If (ReturnCode = zero)
    Then
        Call Win32API "GetLastError" returning LastErrorCode
        Display "Errcode = ", LastErrorCode
    Else
        Display "UserId = '" UserId(1:UserIdLen - 1) "'"
    End-if
--- Quit processing
    Goback
    .
End program GetUserInfo.

End Frog Errors.
```

#### ↳ Re: GetUserName in NetExpress

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981203162640.03741.00001514@ng119.aol.com>`
- **References:** `<36669F61.58E48F10@IMN.nl>`

```
Hi,

I have a working example of this API if you would like me to send it to you
please e-mail me.

Thanks,
Bob
```

##### ↳ ↳ Re: GetUserName in NetExpress

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-12-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3667A280.31A96CD@IMN.nl>`
- **References:** `<36669F61.58E48F10@IMN.nl> <19981203162640.03741.00001514@ng119.aol.com>`

```
Bob7536 wrote:

> Hi,
>
…[4 more quoted lines elided]…
> Bob

I would like to see it anyway, allthough Karl Wagner solved the problem for me.
(See my answer on his post).

Thanks BH, Bob

Happy Frog
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
