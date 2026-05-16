[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need CICS - APPC help

_3 messages · 2 participants · 1998-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Need CICS - APPC help

- **From:** Ed.Stevens@nmm.nissan-usa.com
- **Date:** 1998-11-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72ul58$1is$1@nnrp1.dejanews.com>`

```
Any heavy-duty CICS guys here?

We have started a project to develop a web-based app, connecting to apps on
the MVS host for database access.  We are using MS SNA Server with COMTI and
MS Transaction Server to make the connection.  The connection from SNA Server
appears as an LU6.2 device to the host.  The active components of the web
pages are written in VB and are expecting to talk to a Cobol pgm running
under CICS.

The basic connections are working, and the page is causing the CICS pgm to
start, but it (the Cobol pgm) is failing with a CICS abend ADPL.  I have
traced this back to a INVREQ on a RECEIVE.  The error manual says this is one
of two things:

1. The command is used on an APPC conversation that is not using the EXEC CICS
interface or that is not a mapped conversation.

2. A distributed program link server application specified the function-
shipping session (its principal facility) on the CONVID option (RESP2=200).

Investigation of the EIB block in the program dump showed RESP2=x'C8'
(d'200')  so I guess we have nailed the problem, but how to fix it?  (I used
to do a lot of CICS programming, but never any LU6.2/appc stuff -- and the
last few years I have drifted over to the 'dark side' and been working in
DBA, tech support, and a variety of PC based special assignments.)

FWIW, we also see the input data supplied by the VB pgm is in the TIOA, so we
assume that everything on the PC end is doing its job correctly.

So far, our Cobol program is just a very small 'proof of technique' example
based on sample programs included with the PC components - very small.  Here
are the relevant parts:

WORKING-STORAGE SECTION.
01  FILLER.
	05  PASSED-DATA-LEN     PIC 9(4) COMP    VALUE ZERO.
01  WS-LU-IO-AREA.
	03  CA-PART-NUM                PIC X(5).
	03  CA-PART-DESC               PIC X(30).
	03  CA-BIN                     PIC X(3).

LINKAGE SECTION.
01 DFHCOMMAREA.
	02  CA-COMMAREA 	PIC X.

PROCEDURE DIVISION.
	MOVE LENGTH OF WS-LU-IO-AREA TO PASSED-DATA-LEN
	EXEC CICS RECEIVE
		INTO (WS-LU-IO-AREA)
		LENGTH (PASSED-DATA-LEN)
		NOTRUNCATE
	END-EXEC

*--------------------------------------------------------------
*   MODIFY THE INPUT FIELDS IN A RECOGNIZABLE WAY:
*   - REVERSE STRING OF ALPHA'S
*   - COMPUTE NINES-COMPLEMENT OF NUMERICS
*--------------------------------------------------------------
	MOVE LENGTH OF WS-LU-IO-AREA TO PASSED-DATA-LEN
	EXEC CICS SEND
		FROM (WS-LU-IO-AREA)
		LENGTH (PASSED-DATA-LEN)
	END-EXEC
	EXEC CICS RETURN END-EXEC.
	GOBACK.
```

#### ↳ Re: Need CICS - APPC help

- **From:** Ed.Stevens@nmm.nissan-usa.com
- **Date:** 1998-11-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72v026$c6n$1@nnrp1.dejanews.com>`
- **References:** `<72ul58$1is$1@nnrp1.dejanews.com>`

```
Never mind.  We found the solution.  If you're curious, in poking around the
transaction dump, I found that a commarea had been allocated and the input
data placed there.  So, instead of trying to RECEIVE and SEND the data, I
simply looked in the DFHCOMMAREA, did what I needed with it, and placed the
return data back in the DFHCOMMAREA.  The only CICS command needed was EXEC
CICS RETURN END-EXEC.

In article <72ul58$1is$1@nnrp1.dejanews.com>,
  Ed.Stevens@nmm.nissan-usa.com wrote:
> Any heavy-duty CICS guys here?
>
…[70 more quoted lines elided]…
>
```

#### ↳ Re: Need CICS - APPC help

- **From:** WOB@my-dejanews.com
- **Date:** 1998-11-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72vekn$pt4$1@nnrp1.dejanews.com>`
- **References:** `<72ul58$1is$1@nnrp1.dejanews.com>`

```
In article <72ul58$1is$1@nnrp1.dejanews.com>,
  Ed.Stevens@nmm.nissan-usa.com wrote:
> Any heavy-duty CICS guys here?
>
…[70 more quoted lines elided]…
>
Ed,

Code looks fine. I'm assuming the conversation is the principal facility and
that CICS is the Back-End Transaction?

In your VTAM Definitions, are you using Dependent or Independent LU's? Does
this occur on the very first handshake-session between the Server and CICS?

Are these sessions conversational or non-conversational? In other words, once
the server executes an APPC-ALLOCATE, the Back-End Transaction (Session)
remains active (Conversational) or it dies after you issue the SEND (that's
what it looks like)? Are the Sessions executing at SYNCLEVEL ZERO?

Just for kicks, define a fullword and specify the STATE parameter on the
RECEIVE and see what CVDA you get. This may tell you much more.

You also may want to post this to bit.listserv.cics-l.

Cheers,

WOB,
Atlanta




-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
