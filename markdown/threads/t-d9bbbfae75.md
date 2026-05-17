[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Supported (IBM MVS) Pointer and USING - "Mea Culpa"

_2 messages · 2 participants · 1998-03_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Supported (IBM MVS) Pointer and USING - "Mea Culpa"

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-18T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6erpq4$cjl@sjx-ixn7.ix.netcom.com>`

```

Well, it's time to "fess up".

Having searched the documentation, all APARs (obscure and old), and even
using the IBM "AskQ" functionality, I stand (or rather type) here in
contrition and admit that I was thoroughly and completely wrong.

According to IBM (for their current MVS COBOLs - and assuming you have a
fixed number of parameters passed to your subprogram), you should ONLY put
the true "passed parameters" in your Procedure Division USING header. You
should *not* put any structures for which you will eventually use a SET
ADDRESS OF statement to gain addressability. (Although doing so will
PROBABLY not cause you too many problems.)

(Actually, I prefer this rule to what I thought was the rule, because it now
remains true that the number of parameters in the PROCEDURE DIVISION USING
statement is always supposed to be the same as - or if you never will use
the last one(s), less than - the number of parameters passed from the
CALLing program.)

Now I am still *positive* that there was a problem with this and that there
were times that this caused S0C4's. However, I am also now convinced that
one of the following is true: A) I just imagined that there was ever a
problem; B) there was a problem, but it was a IBM code bug that has been
fixed; C) It was an application code bug - such as a misplaced SET ADDRESS
OF; or D) it was in an alternate universe and Rod Serling will be coming up
to me any moment now.

Again, sorry for the misinformation that I was so insistent upon.

P.S. For the other "train of the original thread" about WHY would you want
to use supported COBOL-specific syntax to do this and not "just" use the
documented Operating System R1 facility, I will leave that fight for another
day and thread.
```

#### ↳ Re: Supported (IBM MVS) Pointer and USING - "Mea Culpa"

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d9bbbfae75-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6erpq4$cjl@sjx-ixn7.ix.netcom.com>`
- **References:** `<6erpq4$cjl@sjx-ixn7.ix.netcom.com>`

```

As far as I am concerned: discussion closed. Next thread&topic.

William: how about a html cobol coding form in/attached to the faq?

Huib Cobol Frog

William M. Klein wrote:

8< An apology, not needed for me.

› P.S. For the other "train of the original thread" about WHY would you want
› to use supported COBOL-specific syntax to do this and not "just" use the
› documented Operating System R1 facility, I will leave that fight for another
› day and thread.

Joe Zitzelberger and I love to "fight", it seems ...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
