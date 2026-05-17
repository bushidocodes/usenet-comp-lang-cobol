[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Checking for Locked records in Animator (MF 3.1.35)

_2 messages · 2 participants · 1996-12_

---

### Checking for Locked records in Animator (MF 3.1.35)

- **From:** "douglas h. troy" <ua-author-17073163@usenetarchives.gap>
- **Date:** 1996-12-08T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bbe578$abe701a0$527679a8@MyComputer.mindspring.com>`

```

Question:

Does anyone know of a way I could check for the existence of a locked
record during a debug session in Animator. I know I can read the record
and then check the file status, but I wanted to know if the Animator
facility had some method of doing this. Thus far, I have been unable to
find a way to do this.

Thanks in advance.
D.
dt··.@drs··e.com
(no junk mail please...)

Motto: If I'm awake, I'm working.
```

#### ↳ Re: Checking for Locked records in Animator (MF 3.1.35)

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-12-08T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2e0592ccea-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bbe578$abe701a0$527679a8@MyComputer.mindspring.com>`
- **References:** `<01bbe578$abe701a0$527679a8@MyComputer.mindspring.com>`

```

Douglas H. Troy wrote:
› 
› Question:
…[5 more quoted lines elided]…
› find a way to do this.

Hi. I don't think there is a specific function for doing this, but you
might
get some success by writing a program which will do the "query" for you
and,
in Animator, use the 'D'o command to "CALL "lockquery" USING ...." and
pass
it something that identifies the record you want to check (the entire
key of
the record would be best, but it might be too long to type in every
time).
Your program could then try reading the record and display whether it
received a locked-record status or not.

Alternatively, write a completely seperate program that you run
alongside
the animator which you can type a key into at any time and it'll tell
you
whether that record is locked or not. You could include all sorts of
functions to do read next/prev, start, remember 'n' previous keys to
save
re-typing etc etc.

I guess the only things to be wary of are (a) make sure the "query"
program
isn't running with any RETRYLOCK options switched on (or you won't get
the
locked record & status back) - maybe this will dictate that the first
method can't be used - and (b) make sure your program doesn't
accidentally
change the environment of the program being debugged by holding records
locked after the query.

I don't know how useable either of these would be (I haven't actually
*tried*
them), but it was just a thought. I guess that if *you're* writing the
query code, it'll be as useable as you make it! :)

Cheers, Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
