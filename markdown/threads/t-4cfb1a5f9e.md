[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL & memory allocation & API's

_8 messages · 4 participants · 2001-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL & memory allocation & API's

- **From:** tracey@bframe.com
- **Date:** 2001-01-18T21:08:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<947m0l$s9p$1@nnrp1.deja.com>`

```
I'm having trouble with a program that once worked and I'm trying to
find that needle in a hay stack.

I have NT and just applied SP6 when this problem immediately began.

I have a MF COBOL program that is making API calls.  All calls work
fine except one.  It worked, now fails.  Preceding the call I allocate
space using a cobol call, which works fine.  This space is then
associated with a pointer that is one of several variables in one of
several parameters in the problematic call.

The error code for the call is 'invalid parameter', but doesn't tell me
which one.

I need to know if there are any special issues to be had with allocated
space in regards to these two languages (the API's are in C).

Any ideas are most welcome.


Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: MF COBOL & memory allocation & API's

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-01-18T22:00:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-1gF571eCnmZm@tcpserver>`
- **References:** `<947m0l$s9p$1@nnrp1.deja.com>`

```
On Thu, 18 Jan 2001 21:08:44, tracey@bframe.com wrote:

> I'm having trouble with a program that once worked and I'm trying to
> find that needle in a hay stack.
…[19 more quoted lines elided]…
> http://www.deja.com/

Most likely SP6 broke the API in question. Is that SP6 or SP6a? Revert
back to your previous service level.

What API are you calling????????
```

#### ↳ Re: MF COBOL & memory allocation & API's

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2001-01-18T22:52:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HsK96.182209$59.48777791@news3.rdc1.on.home.com>`
- **References:** `<947m0l$s9p$1@nnrp1.deja.com>`

```
Perhaps you could tell us what API and possibly show us your code. I had
problems with a change Microsoft made to the common controls library after
installing Internet Explorer 5.01 (which replaced COMCTL32.DLL). It turned
out that my code, which worked, did not adhere to Microsoft's documentation.
The newer version of COMCTL32.DLL was less forgiving.

Karl

<tracey@bframe.com> wrote in message news:947m0l$s9p$1@nnrp1.deja.com...
> I'm having trouble with a program that once worked and I'm trying to
> find that needle in a hay stack.
…[19 more quoted lines elided]…
> http://www.deja.com/
```

#### ↳ Re: MF COBOL & memory allocation & API's

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 2001-01-19T01:19:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010118201934.22603.00000095@ng-cp1.aol.com>`
- **References:** `<947m0l$s9p$1@nnrp1.deja.com>`

```
Hi Tracey,

What call are you using ?

Bob Hennessey
```

#### ↳ Re: MF COBOL & memory allocation & API's

- **From:** tracey@bframe.com
- **Date:** 2001-01-19T13:55:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<949gvq$c1c$1@nnrp1.deja.com>`
- **References:** `<947m0l$s9p$1@nnrp1.deja.com>`

```
The call is MQReceiveMessage

...
       77  char                   pic s9(2)  comp-5 typedef.
       77  uns-char               pic  9(2)  comp-5 typedef.
       77  short                  pic s9(4)  comp-5 typedef.
       77  uns-short              pic  9(4)  comp-5 typedef.
       77  int                    pic s9(9)  comp-5 typedef.
       77  uns-int                pic  9(9)  comp-5 typedef.
       77  long                   pic s9(9)  comp-5 typedef.
       77  uns-long               pic  9(9)  comp-5 typedef.
       77  d-l-float                         comp-2 typedef.
       77  d-float                           comp-2 typedef.
       77  float                             comp-1 typedef.
       77  proc-pointer           procedure-pointer typedef.
       77  data-pointer                     pointer typedef.
       77  void                   pic  9(2)  comp-5 typedef.


       01  WS-QUEUE                    PIC X(60000)  VALUE SPACES.
       01  CONVERT-STRING              PIC X(60000)  VALUE SPACES.
       01  CONVERTED-STRING            PIC X(60000)  VALUE SPACES.

       01  FIRST-TIME-OPEN-FLAG            PIC X   VALUE "Y".
           88  FIRST-TIME-OPEN     VALUE "Y".
       01  FIRST-TIME-CLOSE-FLAG           PIC X   VALUE "Y".
           88  FIRST-TIME-CLOSE    VALUE "Y".

      ******************************************************************
      ***Type Defs
       01  tdPropID typedef.
           05  PropID              uns-int.

       01  tdPropVar               typedef.
           05  vartype                 pic 9(4) comp-5.
           05  word1                   pic xx comp-5.
           05  word2                   pic xx comp-5.
           05  word3                   pic xx comp-5.
           05  union                   pic xxxxxxxx.
           05  caud   redefines union.
               10  celems              pic 9(9) comp-5.
               10  pelems              uns-int.
           05  lpwstr redefines union uns-int.

       01  tdPropStatus typedef.
           05  PropStatus          pic xxxx comp-5.

       01  tdMQMSGPROPS            typedef.
           05  cProp-CTR           pic xxxx comp-5.
           05  apropid             data-pointer.
           05  apropvar            data-pointer.
           05  astatus             data-pointer.

       01  myRespMQMSGPROPS        tdMQMSGPROPS.
       01  myOrigMQMSGPROPS        tdMQMSGPROPS.


      *****Original Messages
       01  myOrigPropID     pic xxxx comp-5  OCCURS 1 TO 99
                                             DEPENDING ON SUBM.
       01  myOrigPropVar    tdPropVar        OCCURS 1 TO 99
                                             DEPENDING ON SUBM.
       01  myOrigPropStatus pic xxxx comp-5  OCCURS 1 TO 99
                                             DEPENDING ON SUBM.

      *****Response Messages
       01  myRespPropID     pic xxxx comp-5  OCCURS 1 TO 99
                                             DEPENDING ON SUBM.
       01  myRespPropVar    tdPropVar        OCCURS 1 TO 99
                                             DEPENDING ON SUBM.
       01  myRespPropStatus pic xxxx comp-5  OCCURS 1 TO 99
                                             DEPENDING ON SUBM.

      *****THE-POINTERS-ETC.
       01  FN-Formatname-p         data-pointer.
       01  FN-Pathname-p           data-pointer.
       01  hResult                 data-pointer.
       01  OP-ORIGHANDLE-p         data-pointer.
       01  OP-RESPHANDLE-p         data-pointer.
       01  CC-CURSOR-p             data-pointer.
       01  Library-p               data-pointer.
       01  pFN-Length              data-pointer.
       01  myRespMQMSGPROPS-p      data-pointer.
       01  myOrigMQMSGPROPS-p      data-pointer.

       01  lpwstr-Pointer.
           05  lpwstr-label-p      data-pointer.
           05  lpwstr-label-p-char REDEFINES lpwstr-label-p
                                   uns-int.
       01  pelems-Pointer.
           05  pelems-body-p       data-pointer.
           05  pelems-body-p-char  REDEFINES pelems-body-p
                                   uns-int.
       01  ulval-body-type-Pointer.
           05  ulval-bodyt-p       data-pointer.
           05  ulval-bodyt-p-char redefines ulval-bodyt-p
                                   uns-int.
       01  pelems-Pointer.
           05  pelems-p            data-pointer.
           05  pelems-p-char      redefines pelems-p
                                   uns-int.

       77  THE-RESULT                  pic xxxx comp-5.
       88  STG-E-INVALIDPARAMETER             value h"80030057".
       88  MQ-OK                              value           0.
       88  MQ-ERROR-ILLEGAL-QUEUE-PATHNAM     value h"c00e0014".
       88  MQ-ERROR-QUEUE-NOT-FOUND           value h"c00e0003".
       88  MQ-ERROR-SERVICE-NOT-AVAILABLE     value h"c00e000b".
       88  MQ-ERROR-FORMATNAME-BUFFER-TOO     value h"c00e001f".
       88  MQ-ERROR-NO-DS                     value h"c00e0013".
       88  MQ-ERROR-ACCESS-DENIED             value h"c00e0025".
       88  MQ-ERROR-ILLEGAL-FORMATNAME        value h"c00e001e".
       88  MQ-ERROR-INVALID-PARAMETER         value h"c00e0006".
       88  MQ-ERROR-SHARING-VIOLATION         value h"c00e0009".
       88  MQ-ERROR-UNSUPPORTED-FORMATNAM     value h"c00e0020".
       88  MQ-ERROR-UNSUPPORTED-ACCESS-MO     value h"c00e0045".
       88  MQ-ERROR-INVALID-HANDLE            value h"c00e0007".
       88  MQ-ERROR-PROPERTY                  value h"c00e0002".
       88  MQ-ERROR-INSUFFICIENT-RESOURCE     value h"c00e0027".
       88  MQ-ERROR-MESSAGE-STORAGE-FAILE     value h"c00e002a".
       88  MQ-ERROR-INVALID-CERTIFICATE       value h"c00e002c".
       88  MQ-ERROR-CORRUPTED-INTERNAL-CE     value h"c00e002d".
       88  MQ-ERROR-NO-INTERNAL-USER-CERT     value h"c00e002f".
       88  MQ-ERROR-CORRUPTED-SECURITY-DA     value h"c00e0030".
       88  MQ-ERROR-CORRUPTED-PERSONAL-CE     value h"c00e0031".
       88  MQ-ERROR-BAD-SECURITY-CONTEXT      value h"c00e0035".
       88  MQ-ERROR-COULD-NOT-GET-USER-SI     value h"c00e0036".
       88  MQ-ERROR-DTC-CONNECT               value h"c00e004c".
       88  MQ-ERROR-TRANSACTION-USAGE         value h"c00e0050".
       88  MQ-ERROR-STALE-HANDLE              value h"c00e0056".
       88  MQ-ERROR-IO-TIMEOUT                value h"c00e001b".
       88  MQ-INFORMATION-PROPERTY            value h"400e0001".
       88  MQ-INFORMATION-UNSUPPORTED-PRO     value h"400e0004".
       88  MQ-ERROR-INSUFFICIENT-PROPERTI     value h"c00e003f".
       88  MQ-INFORMATION-PROPERTY-IGNORE     value h"400e0003".

       78  PROPID-M-MSGID                     value 2.
       78  PROPID-M-CORRELATIONID             value 3.
       78  PROPID-M-BODY                      value 9.
       78  PROPID-M-BODY-TYPE                 value 42.
       78  PROPID-M-BODY-SIZE                 value 10.
       78  PROPID-M-LABEL                     value 11.
       78  PROPID-M-LABEL-LEN                 value 12.
       78  VT-LPWSTR                          value 31.
       78  VT-UI4                             value 19.
       78  VT-BSTR                            value 8.
       78  MQ-NO-TRANSACTION                  value x"00".
       78  MQ-MTS-TRANSACTION                 value x"01".
       78  MQ-XA-TRANSACTION                  value x"02".
       78  MQ-SINGLE-MESSAGE                  value x"03".
       78  MQ-RECEIVE-ACCESS                  value h"00000001".
       78  MQ-SEND-ACCESS                     value h"00000002".
       78  MQ-PEEK-ACCESS                     value h"00000020".
       78  MQ-DENY-NONE                       value h"00000000".
       78  MQ-DENY-RECEIVE-SHARE              value h"00000001".
       78  VT-VECTOR-VT-UI1                   value h"1011".
       78  MQ-ACTION-RECEIVE                  value h"00000000".
       78  MQ-ACTION-PEEK-CURRENT             value h"80000000".
       78  MQ-ACTION-PEEK-NEXT                value h"80000001".

      **** GetFormatName.
       01  FN-PathName                 PIC X(256).
       01  FN-FormatName               PIC X(256).
       01  Library-name                PIC X(256).
       01  FN-Length                   uns-int.

      **** OpenQueueProperties.
       01  HANDLE               uns-int.
       01  OP-ORIGHANDLE               uns-int.
       01  OP-RESPHANDLE               uns-int.
       01  DH-HANDLE-IN                uns-int.
       01  DH-HANDLE-OUT               uns-int.
       01  AU-HANDLE                   uns-int.
       01  UP-HANDLE                   uns-int.
       01  IQ-HANDLE                   uns-int.
       01  PT-HANDLE                   uns-int.
       01  WK-HANDLE                   uns-int.
       01  PD-HANDLE                   uns-int.
       01  EM-HANDLE                   uns-int.
       01  MG-HANDLE                   uns-int.
       01  ED-HANDLE                   uns-int.
       01  AR-HANDLE                   uns-int.
       01  DR-HANDLE                   uns-int.
       01  EX-HANDLE                   uns-int.
       01  LIB-HANDLE                  uns-int.

      **** ReceiveMessageProperties.
       01  RC-RECACTION                uns-int.
       01  pBodyBuffer                 pointer.
       01  BodyBufferSize              pic xxxx comp-5.
       01  BodyBufferFlag              pic xxxx comp-5.

      **** CreateCursorProperties.
       01  CC-CURSOR                   uns-int.

       01  pBodyBufferSize             pointer.
       01  pBodyBufferSize-char redefines pBodyBufferSize uns-int.

...
       LINKAGE SECTION.
       01  AllocatedBody               PIC X(60000).
...

...
       RECEIVE-MESSAGES.

           MOVE ZEROS              TO SUBM.

      ******************************************************************
      *    BODY SIZE MESSAGE
      *
           ADD 1                   TO SUBM.
           MOVE PROPID-M-BODY-SIZE TO myOrigPropID (SUBM).
           MOVE VT-UI4             TO vartype of myOrigPropVar (SUBM).

           MOVE SUBM               TO BODY-SUB.

      ******************************************************************
      *    BODY MESSAGE
      *
           ADD 1                   TO SUBM.
           MOVE PROPID-M-BODY      TO myOrigPropID (SUBM).
           MOVE VT-VECTOR-VT-UI1   TO vartype of myOrigPropVar (SUBM).
           MOVE 60000              TO BodyBufferSize.
           MOVE BodyBufferSize     TO celems OF myOrigPropVar (SUBM).

           MOVE 2                  TO BodyBufferFlag.
           CALL "CBL_ALLOC_MEM"
                       BY REFERENCE pBodyBufferSize
                       BY VALUE     BodyBufferSize
                       BY VALUE     BodyBufferFlag
               RETURNING            RETURN-CODE.

           IF RETURN-CODE > 0
               DISPLAY "ALLOCATE MEMEORY CALL FAILED - GET HELP".

           DISPLAY "ALLOCATED POINTER: " pBodyBufferSize.
           SET ADDRESS OF AllocatedBody TO pBodyBufferSize.
           MOVE pBodyBufferSize-char TO pelems of myOrigPropVar (SUBM).


      ******************************************************************
      *    LABEL MESSAGE LENGTH
      *
           ADD 1                   TO SUBM.
           MOVE PROPID-M-LABEL-LEN TO myOrigPropID (SUBM).
           MOVE VT-UI4             TO vartype OF myOrigPropVar (SUBM).
           MOVE 256                TO lpwstr  OF myOrigPropVar (SUBM).

           MOVE SUBM               TO LABEL-SUB.


      ******************************************************************
      *    LABEL MESSAGE

           ADD 1                   TO SUBM.
           MOVE PROPID-M-LABEL     TO myOrigPropID (SUBM).
           MOVE VT-LPWSTR          TO vartype OF myOrigPropVar (SUBM).
           SET  lpwstr-label-p     TO ADDRESS OF WS-MSG-LABEL-UNICODE.
           MOVE lpwstr-Label-p-char TO lpwstr OF myOrigPropVar (SUBM).


     ******************************************************************
      *    SET FINAL STRUCTURE MQMSGPROPS

           MOVE SUBM               TO cProp-ctr of myOrigMQMSGPROPS.
           SET aPropID of myOrigMQMSGPROPS
                                   TO ADDRESS OF myOrigPropID   (1).
           SET aPropVar of myOrigMQMSGPROPS
                                   TO ADDRESS OF myOrigPropVar  (1).
           SET aStatus OF myOrigMQMSGPROPS
                                   TO ADDRESS OF myOrigPropStatus (1).
           SET myOrigMQMSGPROPS-P  TO ADDRESS OF myOrigMQMSGPROPS.


           CALL WINAPI "MQReceiveMessage"
               USING
                   BY VALUE       OP-ORIGHANDLE
5 min              BY VALUE       300000
                   BY VALUE       RC-RECACTION
                   BY VALUE       myOrigMQMSGPROPS-p
                   BY VALUE       x"00"
                   BY VALUE       x"00"
CURSOR             BY VALUE       x"00"
                   BY VALUE       MQ-NO-TRANSACTION
               GIVING
                   THE-RESULT.

      ****FREE ALLOCATED MEMORY SPACE
           CALL "CBL_FREE_MEM"
               USING   BY VALUE     pBodyBufferSize
               RETURNING            RETURN-CODE.

           IF RETURN-CODE > 0
               DISPLAY "FREE MEMORY CALL FAILED - GET HELP".

       RECEIVE-MESSAGES-EXIT.
           EXIT.
...


Sent via Deja.com
http://www.deja.com/
```

##### ↳ ↳ Re: MF COBOL & memory allocation & API's

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2001-01-19T16:52:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oh_96.188412$59.50061996@news3.rdc1.on.home.com>`
- **References:** `<947m0l$s9p$1@nnrp1.deja.com> <949gvq$c1c$1@nnrp1.deja.com>`

```
Here's the call as documented by Microsoft:

HRESULT APIENTRY MQReceiveMessage(
  QUEUEHANDLE hSource,
  DWORD dwTimeout,
  DWORD dwAction,
  MQMSGPROPS pMessageProps,
  LPOVERLAPPED lpOverlapped,
  PMQRECEIVECALLBACK fnReceiveCallback,
  HANDLE hCursor,
  Transaction *pTransaction
);


Here's what you have:

>            CALL WINAPI "MQReceiveMessage"
>                USING
…[7 more quoted lines elided]…
>                    BY VALUE       MQ-NO-TRANSACTION   GIVING  THE-RESULT.


Here's what you should probably have:

        CALL WINAPI "MQReceiveMessage" USING
            BY VALUE
                                OP-ORIGHANDLE
                                30000 size 4
                                RC-RECACTION
            BY REFERENCE
                                myOrigMQMSGPROPS
            BY VALUE 0 size 4
                                0 size 4
                                0 size 4
            BY VALUE MQ-NO-TRANSACTION GIVING THE-RESULT.


Karl


<tracey@bframe.com> wrote in message news:949gvq$c1c$1@nnrp1.deja.com...
> The call is MQReceiveMessage
>
…[285 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: MF COBOL & memory allocation & API's

- **From:** tracey@bframe.com
- **Date:** 2001-01-19T17:40:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<949u6t$op4$1@nnrp1.deja.com>`
- **References:** `<947m0l$s9p$1@nnrp1.deja.com> <949gvq$c1c$1@nnrp1.deja.com> <oh_96.188412$59.50061996@news3.rdc1.on.home.com>`

```
Thanks for taking the time to look at this.  I just tried out your
suggestion and a number of additional combinations based on your
suggesiton, and it would not work.

Are you familiar with memory allocation and if so, am I doing all that
I need to?


Sent via Deja.com
http://www.deja.com/
```

###### ↳ ↳ ↳ Re: MF COBOL & memory allocation & API's

_(reply depth: 4)_

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2001-01-19T20:40:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WC1a6.189486$59.50259806@news3.rdc1.on.home.com>`
- **References:** `<947m0l$s9p$1@nnrp1.deja.com> <949gvq$c1c$1@nnrp1.deja.com> <oh_96.188412$59.50061996@news3.rdc1.on.home.com> <949u6t$op4$1@nnrp1.deja.com>`

```
In answer to your question, yes I am familiar with memory allocation
although I haven't used CBL_ALLOC_MEM in version 4.0 of MF COBOL on NT
because the (old) documentation claims that it is only supported for GNT and
INT, and I always compile to native code when using that compiler. As well,
since INT and GNT require the runtime, I cannot be sure how MERANT
implemented the CBL_ALLOC_MEM function, so the pointer returned may not be
usable by the Win32 API. Instead I use the Win32 API functions:
LocalAlloc(), LocalLock(), LocalUnlock() and LocalFree().

In terms of your program, I am unsure why you are bothering to allocate
memory since it would be far easier to declare 'AllocatedBody' in
WORKING-STORAGE and use a single "SET my-pointer to TO ADDRESS OF ..."
statement to get the address for setting the 'pelems' variable.

However, your original message states that you were having a problem with a
call parameter  which you assume to be related to your memory allocation
code. I haven't made that assumption.

Karl




<tracey@bframe.com> wrote in message news:949u6t$op4$1@nnrp1.deja.com...
> Thanks for taking the time to look at this.  I just tried out your
> suggestion and a number of additional combinations based on your
…[7 more quoted lines elided]…
> http://www.deja.com/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
