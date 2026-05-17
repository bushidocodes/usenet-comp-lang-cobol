[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP: C function assigning setting a string

_6 messages · 6 participants · 1998-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Help requests and how-to`](../topics.md#help)

---

### HELP: C function assigning setting a string

- **From:** "paul jones" <ua-author-109502@usenetarchives.gap>
- **Date:** 1998-05-27T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<356D2DD7.3B74ABFE@hotmail.com>`

```

Hi, I am not a COBOL programmer as you will soon become aware but have a
problem with some existing COBOL code calling a C function. I would
appreciate it if anyone has the answer

The COBOL code that calls a 'C' function passing two parameters, the
second of these two parameters is intended to be modified inside the C
function and then used in the COBOL.

The error I get is :- [ I am using MicroFocus COBOL on Solaris]

Execution error : file 'ubpcalc'
error code: 114, pc=0, call=1, seg=0
114 Attempt to access item beyond bounds of memory (Signal 10)


Thanks Paul Jones
pm_··.@hot··l.com

----- the C code is something like this -------

int cis_sh_msg(char* message, char** out_message)
{
/* code to find the out message */
*out_message = /* address of some new string */
}

------ the COBOL code is --------------

CIS23i CALL 'cis_sh_msg' USING CALL-C-MSG-NO,
CIS23i CALL-C-MSG,
CIS23i RETURNING CALL-C-RETURN-STATUS.

----------------------------------------
```

#### ↳ Re: HELP: C function assigning setting a string

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-05-27T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2befaff1a2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<356D2DD7.3B74ABFE@hotmail.com>`
- **References:** `<356D2DD7.3B74ABFE@hotmail.com>`

```

Paul Jones wrote:
› 
› Hi, I am not a COBOL programmer as you will soon become aware but have a
…[30 more quoted lines elided]…
› ----------------------------------------

Paul,

Given the nature of your problem, you've given *nearly* enough
information, but not quite. The PIC clauses of the COBOL items
would be useful - but not quite as useful as a fully compilable
demo.

Having said that, I'll try to help with the information you have
given.

I assume "CALL-C-MSG" is something like a PIC X(100) (ie, some
arbitratily large string). If this is true, then it's important to
realise that this is the equivalent of a char array in C.
Therefore, when you pass it BY REFERENCE (the default), you are
passing the address of the first character in the string, *NOT* the
address of a char pointer. The rough equivalent in C is something
like:

char call_c_msg_no = 0; /* eg, 01 CALL-C-MSG-NO PIC 99 COMP VALUE 0. */
char call_c_msg[100]; /* eg, 01 CALL-C-MSG PIC X(100). */
cis_sh_msg(&call_c_msg_no, &call_c_msg);

You can probably see already that your function recieving out_message
as a (char **) is wrong.

So, a couple of things to consider:

1) You probably need to copy the text byte-for-byte to the passed
message buffer.

2) COBOL PIC X(n) items are fixed length, space padded strings, and
cannot be used interchangably with C's nul-terminated strings -
you need some sort of conversion process on one side or the
other (ie, a strcpy() will not be enough unless the COBOL side
is explicitly coded to post-process the field and handle the nul).
If you decide to make the C side "intelligent", then it will also
need to know the length of the message buffer passed.

There are a lot of similar issues, but these are the ones which I expect
are giving you the immediate problem.

Cheers,
Kev.
```

#### ↳ Re: HELP: C function assigning setting a string

- **From:** "darius cooper" <ua-author-16041747@usenetarchives.gap>
- **Date:** 1998-05-27T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2befaff1a2-p3@usenetarchives.gap>`
- **In-Reply-To:** `<356D2DD7.3B74ABFE@hotmail.com>`
- **References:** `<356D2DD7.3B74ABFE@hotmail.com>`

```

Paul,

Som questions I would ask:

Does the C-program get both strings correctly? Initialize
them to some value within the COBOL program and see
if they show up correctly in C.

How is the second parameter defined in the COBOL
program? Is it a working-storage item or a linkage
section item? Is it PIC X, or is is a POINTER data-type
within COBOL?

Does it work if the second parameter is defined as char *
rather than char ** ?

Does it abend *within* the C program? Or just as it returns
to COBOL. Some printf calls with the C program should
clarify that.

Cheers,

- Darius

Paul Jones wrote in message <356··.@hot··l.com>...
› Hi, I am not a COBOL programmer as you will soon become aware but have a
› problem with some existing COBOL code calling a C function.  I would
…[33 more quoted lines elided]…
›
```

#### ↳ Re: HELP: C function assigning setting a string

- **From:** "robert moriarty" <ua-author-17074153@usenetarchives.gap>
- **Date:** 1998-05-28T09:46:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2befaff1a2-p4@usenetarchives.gap>`
- **In-Reply-To:** `<356D2DD7.3B74ABFE@hotmail.com>`
- **References:** `<356D2DD7.3B74ABFE@hotmail.com>`

```

Paul Jones wrote:
: Hi, I am not a COBOL programmer as you will soon become aware but have a
: problem with some existing COBOL code calling a C function. I would
: appreciate it if anyone has the answer

: The COBOL code that calls a 'C' function passing two parameters, the
: second of these two parameters is intended to be modified inside the C
: function and then used in the COBOL.

: The error I get is :- [ I am using MicroFocus COBOL on Solaris]

: Execution error : file 'ubpcalc'
: error code: 114, pc=0, call=1, seg=0
: 114 Attempt to access item beyond bounds of memory (Signal 10)


: Thanks Paul Jones
: pm_··.@hot··l.com

: ----- the C code is something like this -------

: int cis_sh_msg(char* message, char** out_message)
: {
: /* code to find the out message */
: *out_message = /* address of some new string */
: }

: ------ the COBOL code is --------------

: CIS23i CALL 'cis_sh_msg' USING CALL-C-MSG-NO,
: CIS23i CALL-C-MSG,
: CIS23i RETURNING CALL-C-RETURN-STATUS.

: ----------------------------------------

Hi,

By convention COBOL passes ALL arguments BY REFERENCE. There are overrides
on some compilers to allow passing BY VALUE (like C, copy of item on the
stack) and BY CONTENT, which creates a temporary copy of the parameter in
the calling program and passes a reference to the copy. One thing to check
carefully is the parameter ordering on both compilers. Pascal used to
reverse the order so if you called Fx passing (a,b,c), Fx actually received
(c,b,a). Not a problem in Pascal but it could drive you nuts working
cross-language.

Good Luck,
Bob
```

#### ↳ Re: HELP: C function assigning setting a string

- **From:** "aacin..." <ua-author-17071800@usenetarchives.gap>
- **Date:** 1998-05-30T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2befaff1a2-p5@usenetarchives.gap>`
- **In-Reply-To:** `<356D2DD7.3B74ABFE@hotmail.com>`
- **References:** `<356D2DD7.3B74ABFE@hotmail.com>`

```

Paul Jones writes : >>>
Hi, I am not a COBOL programmer as you will soon become aware but have a
problem with some existing COBOL code calling a C function. I would appreciate
it if anyone has the answer

The COBOL code that calls a 'C' function passing two parameters, the second of
these two parameters is intended to be modified inside the C function and then
used in the COBOL.

The error I get is :- [ I am using MicroFocus COBOL on Solaris]

Execution error : file 'ubpcalc'
error code: 114, pc=0, call=1, seg=0
114 Attempt to access item beyond bounds of memory (Signal 10)

Thanks Paul Jones
pm_··.@hot··l.com

----- the C code is something like this -------

int cis_sh_msg(char* message, char** out_message)
{
/* code to find the out message */
*out_message = /* address of some new string */
}

------ the COBOL code is --------------

CIS23i CALL 'cis_sh_msg' USING CALL-C-MSG-NO,
CIS23i CALL-C-MSG,
CIS23i RETURNING CALL-C-RETURN-STATUS.

----------------------------------------

Paul,
A few things come to mind. One, COBOL is field length oriented and doesn't
handle strings as they are know in C. A COBOL program doesn't require a field
to be null terminated but C does. If you pass a "string" to a C program that
isn't terminated propterly any attempt to use the string will cause either
garbage or a segmentation fault. You would have to get an x'00' at the end of
the string in the COBOL program.

Second, most C compilers expect parameters to be passed to a function in the
reverse order from how they are declared, e.g., foo(a, b) really gets the parms
in order of b, a on the stack.
You could be passing the arguments in the wrong sequence which could cause the
C program to crash.

Without seeing more of the details of the 2 programs I can only give you what I
believe at a gut level to be the possible problems.

HTH,
Jim Castro
```

##### ↳ ↳ Re: HELP: C function assigning setting a string

- **From:** "monaco" <ua-author-111933@usenetarchives.gap>
- **Date:** 1998-05-31T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2befaff1a2-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2befaff1a2-p5@usenetarchives.gap>`
- **References:** `<356D2DD7.3B74ABFE@hotmail.com> <gap-2befaff1a2-p5@usenetarchives.gap>`

```

› Paul,
› A few things come to mind.   One, COBOL is field length oriented and
…[25 more quoted lines elided]…
› Jim Castro

Not sure of the memory scheme, but on PC's I'd say given the
error- that cobol was passing a near reference to the string and
not a far one...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
