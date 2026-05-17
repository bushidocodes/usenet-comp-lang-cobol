[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL calling C calling COBOL

_3 messages · 3 participants · 1997-03_

---

### COBOL calling C calling COBOL

- **From:** "mark erickson" <ua-author-5460620@usenetarchives.gap>
- **Date:** 1997-03-10T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3325DFF5.4E9D@asizip.com>`

```

I am trying to use a function within a C library that requires the
addresses of two functions/procedures that are within the COBOL code.
The function in the C library will "callback" the COBOL
functions/procedures with parameters. Can this be done? If so, how?

Thanks in advance for any help!!!!

Mark Erickson
ma··.@asi··p.com
```

#### ↳ Re: COBOL calling C calling COBOL

- **From:** "del archer" <ua-author-6589011@usenetarchives.gap>
- **Date:** 1997-03-13T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3c7d346eaa-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3325DFF5.4E9D@asizip.com>`
- **References:** `<3325DFF5.4E9D@asizip.com>`

```

Mark Erickson wrote:

› I am trying to use a function within a C library that requires the
› addresses of two functions/procedures that are within the COBOL code.
› The function in the C library will "callback" the COBOL
› functions/procedures with parameters.  Can this be done?  If so, how?

If you are using MicroFocus COBOL, you can use a procedure pointer. It is
described in the manual.

Del.
```

##### ↳ ↳ Re: COBOL calling C calling COBOL

- **From:** "geir knaplund" <ua-author-6588924@usenetarchives.gap>
- **Date:** 1997-03-14T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3c7d346eaa-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3c7d346eaa-p2@usenetarchives.gap>`
- **References:** `<3325DFF5.4E9D@asizip.com> <gap-3c7d346eaa-p2@usenetarchives.gap>`

```

Del Archer wrote:
› 
› Mark Erickson wrote:
…[9 more quoted lines elided]…
› Del.

To point you in the right direction...
(Please check MSDEV Help for actual parameters.. I just write this as I
remembered it..)

int main(int argc, char *argv[]..)
{
....
HINSTANCE HCobDLL;
FARPROC CobENTRY;
int parm1;
char parm2[30];
....
HCobDLL = LoadLibrary("MyCobFuncs.dll");
CobENTRY = GetProcAddress(HCobDLL, "some_entry_point_of_mine");
cobENTRY(parm1, parm2,...)
....

exit(0);
}

Something like the above (with som error-checking.. :-)) )..

I can get an actual working example if you don't get it to work...

Please note that you have to use CASE and LITLINK and MAP for your COBOL
DLL to make this work..


- Geir Knaplund
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
