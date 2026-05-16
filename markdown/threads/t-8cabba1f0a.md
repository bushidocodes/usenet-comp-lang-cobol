[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The InternetConnect API.

_2 messages · 2 participants · 1998-12_

---

### The InternetConnect API.

- **From:** tommy nilsen <tommy.nilsen@merkantildata.no>
- **Date:** 1998-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368A31E4.41F43BF9@merkantildata.no>`

```
Hi.

I'm trying to use the InternetConnect API in Microfocus Netexpress 2.0,
but I get a return value of 183.
The Win32SDK telles me that error-code 183 = "Cannot create a file when
that file already exists".

Heres whats the call looks like:

78 INTERNET-SERVICE-HTTP           value 3.
01 InternetOpenHandle                            pic s9(9)  comp-5.
01 dwService                                           pic s9(9)
comp-5.
01 dwFlags                                              pic s9(9)
comp-5.
01 dwContext                                          pic s9(9)  comp-5.

           move INTERNET-SERVICE-HTTP to dwService
           move 0                                              to
dwFlags
           move 1                                              to
dwContext
           call WINAPI "InternetConnectA" using
                   by value InternetOpenHandle
                   by reference "www.nor22.no"&x"00"
                   by value 80
                   by reference "test"&x"00"
                   by reference "test"&x"00"
                   by value dwService
                   by value dwFlags
                   by value dwContext
               returning InternetConnecthandle
           end-call

Can anyone of you tell me if you see any errors in the code..?
I've tried to translate it from VisualBasic to Cobol, but since I'm no
expert I'm not shure if I've done it right...

Heres the API source in VisualBasic.

Public Declare Function InternetConnect Lib "wininet.dll" Alias
"InternetConnectA" _
(ByVal hInternetSession As Long, _
ByVal sServerName As String, _
ByVal nServerPort As Integer, _
ByVal sUsername As String, _
ByVal sPassword As String, _
ByVal lService As Long, _
ByVal lFlags As Long, _
ByVal lContext As Long) As Long


Any help would be greatly appreciated...

Tommy Nilsen
tommy.nilsen@merkantildata.no
```

#### ↳ Re: The InternetConnect API.

- **From:** "Roberto Bongini" <futura.info@mclink.it>
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76fd9s$979$1@news.mclink.it>`
- **References:** `<368A31E4.41F43BF9@merkantildata.no>`

```
In this source error-code is zero.  I try and the function is OK but I do
not have the functions before this because InternetOpenHandle is zero and
hInternet return zero.
Try it and, if you can, send the complete source so I can test your code.
Greetings.
      $set case defaultbyte"00"
       special-names.
           call-convention 74 is WinApi.
       working-storage section.
       77  wininet             procedure-pointer.
       78  INTERNET-SERVICE-HTTP       value 3.
       77  InternetOpenHandle      pic x(4) comp-5.
       77  dwService               pic x(4) comp-5.
       77  dwFlags                 pic x(4) comp-5.
       77  dwContext               pic x(4) comp-5.
       77  hInternet               pic x(4) comp-5.
       77  nServerPort             pic x(4) comp-5.
       procedure division.
           set wininet to entry "wininet.dll".
           move INTERNET-SERVICE-HTTP to dwService.
           move 0 to dwFlags.
           move 1 to dwContext.
           move 80 to nServerPort.
           call WinApi "InternetConnectA" using
                                       by value InternetOpenHandle
                                       by reference z"www.globeit.it"
                                       by value nServerPort
                                       by reference z"mf1275"
                                       by reference z"nu,36k"
                                       by value dwService
                                       by value dwFlags
                                       by value dwContext
                                       returning hInternet.
           stop run.

tommy nilsen ha scritto nel messaggio
<368A31E4.41F43BF9@merkantildata.no>...
>Hi.
>
…[30 more quoted lines elided]…
>           end-call
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
