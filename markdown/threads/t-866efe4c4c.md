[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus CALL-CONVENTION 8 doesn't seem to work

_2 messages · 2 participants · 1996-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus CALL-CONVENTION 8 doesn't seem to work

- **From:** "kevin j. hansen" <ua-author-17072510@usenetarchives.gap>
- **Date:** 1996-10-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bbba24$9b2e1c60$4101a8c0@kjh>`

```

I have some assembler routines I wish to link statically (LITLINK) within a
program, but must let the COBOL routines link dynamically so that I can
animate the modules. I have coded the CALL-CONVENTION EXACTLY as shown in
the manual, but I cannot get the assembler routines to link statically
unless I preface the name with two underscore characters.

SPECIAL-NAMES.
CALL-CONVENTION 8 IS LITLINKED.
.
.
CALL LITLINKED 'ASMPROG' USING ... (Compiles as dynamic call)


CALL '__ASMPROG' USING... (Compiles as static call)

What am I doing wrong? This is MF 3.2.20 compiler...

Thanks.

Kevin Hansen
```

#### ↳ Re: Micro Focus CALL-CONVENTION 8 doesn't seem to work

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-10-16T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-866efe4c4c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bbba24$9b2e1c60$4101a8c0@kjh>`
- **References:** `<01bbba24$9b2e1c60$4101a8c0@kjh>`

```

Kevin J. Hansen wrote:
› 
› I have some assembler routines I wish to link statically (LITLINK) within a
…[13 more quoted lines elided]…
› What am I doing wrong?  This is MF 3.2.20 compiler...

Hi Kevin.

You're doing nothing wrong, but I can explain why you are seeing what you're
seeing.

1) Any CALL LITLINKED "name" call will cause the code generator to add a leading
underscore to "name", as the assumption is that any global (callable) symbol
names will begin with an underscore (C compilers will prefix any external
symbols with an underscore too - if we didn't do this, you could not call
C from COBOL (and that includes most of the CBL_ and PC_ calls!)).

2) CALL "__name" causes the code generator to drop into a compatibility mode for
the 16-bit product before CALL CONVENTIONs existed - any double-underscore
prefixed name implied litlinking and also the removal of the underscores.

I'm not sure what I would suggest as the best fix. Maybe you can either change
your ASM code to have a leading underscore or, if that is not possible or
desirable, have a simple glue layer in assembler that is just a bunch of
"_name" symbols which simply jump to "name" ?

Theoretically, it would be possible to have a call convention that specifies the
name should be taken absolutely literally, but to use that the knowledge of what
language the routine is written in would have to be placed in the COBOL source.
I think that would be undesirable.

Cheers, Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
