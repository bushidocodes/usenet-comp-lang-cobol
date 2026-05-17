[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 32-bit MF COBOL DLL calling from VB4

_2 messages · 2 participants · 1996-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### 32-bit MF COBOL DLL calling from VB4

- **From:** "api" <ua-author-834858@usenetarchives.gap>
- **Date:** 1996-10-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bbba02$be241fc0$3b070701@test1>`

```

Pls, help
I am trying to get VB4 to call MF cobol in 32-bit land. I cannot seem to
get the stack correct. Parameters are not getting in and on return we get
a junp to the unknown.
Does anyone knows the compile/link options to get this to work? We have
been using CALLING-CONVENTIONS 3, 67
Doug
```

#### ↳ Re: 32-bit MF COBOL DLL calling from VB4

- **From:** "paterlin..." <ua-author-17087218@usenetarchives.gap>
- **Date:** 1996-10-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-04ec0bcd59-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bbba02$be241fc0$3b070701@test1>`
- **References:** `<01bbba02$be241fc0$3b070701@test1>`

```

"api" wrote:

› Pls, help
› I am trying to get VB4 to call MF cobol in 32-bit land. I cannot seem to
…[3 more quoted lines elided]…
› been using CALLING-CONVENTIONS 3, 67

I have the same problem using calling-convention 74. Doing a dll using
MFCobol seens nearly impossibile.

I have do an attempt to create an OLEServer using VisualObject Cobol,
but even the sample in the compiler doesn't work.

I have fount another solution. I have built an exe in MFCobol that
get parameters from command line then write the result to a temporary
file. VB can run this program using CreateProcess and
WaitForSingleObject and read back the data in the temporary file.

It's ugly but it's work !!!!




################################################
# Roberto Paterlini #
# Reggio Emilia - Italy #
# email: pat··.@i··.it #
#==============================================#
# Don't worry, be happy!!!! #
#==============================================#
# PATSoft - Shareware per Windows #
# Archivio Softeca - TTBase Font Manager #
# http://www.bns.it/patsoft/ #
################################################
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
