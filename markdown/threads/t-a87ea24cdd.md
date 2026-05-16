[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus COBOL question: MOVE 'N' TO DCLININV-CSR-OPEN.

_7 messages · 4 participants · 2004-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus COBOL question: MOVE 'N' TO DCLININV-CSR-OPEN.

- **From:** "Thomas A. Li" <tli@corporola.com>
- **Date:** 2004-06-14T18:22:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<L1mzc.314$UnA1.141@news04.bloor.is.net.cable.rogers.com>`

```
What does it means in Microfocus COBOL for the following line?
           MOVE 'N' TO DCLININV-CSR-OPEN.

Where is the identifier DCLININV-CSR-OPEN defined? If in a compiler added
copybook, what's its name?

Thanks in advance.

Thomas Li
```

#### ↳ Re: Microfocus COBOL question: MOVE 'N' TO DCLININV-CSR-OPEN.

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-06-14T19:34:06+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8orrc0tv8doma5qk9naeoubm56e57t6nft@4ax.com>`
- **References:** `<L1mzc.314$UnA1.141@news04.bloor.is.net.cable.rogers.com>`

```
On Mon, 14 Jun 2004 18:22:35 GMT, "Thomas A. Li" <tli@corporola.com>
wrote:

>What does it means in Microfocus COBOL for the following line?
>           MOVE 'N' TO DCLININV-CSR-OPEN.
…[7 more quoted lines elided]…
>
Although this smells a lot like homework, I am going to give you some
hints.

Variables can be defined anywere on the Data Division.
This means any of their sections, and includes any copybook referenced
within this division.

If you don't know where it is defined either compile the program and
look at the listing.

Alternatively search your source objects for that string. How you do
this will depend on your OS.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Microfocus COBOL question: MOVE 'N' TO DCLININV-CSR-OPEN.

- **From:** "Thomas A. Li" <tli@corporola.com>
- **Date:** 2004-06-14T21:16:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LAozc.32$BrC1.7@news04.bloor.is.net.cable.rogers.com>`
- **References:** `<L1mzc.314$UnA1.141@news04.bloor.is.net.cable.rogers.com> <8orrc0tv8doma5qk9naeoubm56e57t6nft@4ax.com>`

```
I'm sure it is a kind of Microfocus or SQL specific identifier and it is not
user defined in data division. I'm translating an application in Microfocus
COBOL into Java. I have searched all the files available but I can't find
the definition of this kind of variables. There are hundreds of them used.
Maybe it is for cursor control in embedded SQL. Look at the following piece
of code:
         IF DCLININV-CSR-OPEN NOT = 'CF0'
               EXEC SQL
                   CLOSE DCLININV_CF0_CSR
               END-EXEC
               EXEC SQL
                   OPEN DCLININV_CF0_CSR
               END-EXEC
               ....
           END-IF.

But  DCLININV-CSR-OPEN has never occured in a DECLARE CURSOR command.
Bu there ia a similar one called:      05   DB-DCLININV-CSR-OPEN   PIC
X(003) VALUE 'N'. Is there any relation between these two identifiers?

Thanks a lot.

Thomas Li

"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
news:8orrc0tv8doma5qk9naeoubm56e57t6nft@4ax.com...
> On Mon, 14 Jun 2004 18:22:35 GMT, "Thomas A. Li" <tli@corporola.com>
> wrote:
…[27 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Microfocus COBOL question: MOVE 'N' TO DCLININV-CSR-OPEN.

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-06-14T22:56:35+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gh7sc0hdtimcm5sd24j228d0ij03us2k44@4ax.com>`
- **References:** `<L1mzc.314$UnA1.141@news04.bloor.is.net.cable.rogers.com> <8orrc0tv8doma5qk9naeoubm56e57t6nft@4ax.com> <LAozc.32$BrC1.7@news04.bloor.is.net.cable.rogers.com>`

```
On Mon, 14 Jun 2004 21:16:27 GMT, "Thomas A. Li" <tli@corporola.com>
wrote:

Top posting corrected.

>"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
>news:8orrc0tv8doma5qk9naeoubm56e57t6nft@4ax.com...
…[49 more quoted lines elided]…
>X(003) VALUE 'N'. Is there any relation between these two identifiers?

maybe..

In order for you to determine this you will need to precompile the
program. This will create an expanded source, where all your "exec sql
... end-exec" will be converted to another set of COBOL instructions,
and the "declare" variables will also be added/converted according to
the needs of your exec's.

By the name of the variable I agree with you. I think this is a cursor
declaration, and it may not be straightforward to convert to Java.
Can't help you here.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Microfocus COBOL question: MOVE 'N' TO DCLININV-CSR-OPEN.

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-06-14T16:56:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0fCdne90ZMeIglPdRVn-sA@giganews.com>`
- **References:** `<L1mzc.314$UnA1.141@news04.bloor.is.net.cable.rogers.com> <8orrc0tv8doma5qk9naeoubm56e57t6nft@4ax.com> <LAozc.32$BrC1.7@news04.bloor.is.net.cable.rogers.com>`

```
Thomas A. Li wrote:
>  I'm translating an application
> in Microfocus COBOL into Java.

Is nothing sacred?

Mark my words, they day will come when they attempt to translate King's "I
have a dream" speech, the Pledge of Allegiance (with or without "under
God"), and the microwave instructions for a frozen pot pie.

COBOL to Java is like Howard Hughes' project of building a wooden airplane;
it probably can be done, but why?

The only reason I can think of is the original COBOL program did something
weird, like supervised a toaster or monitored the tire-pressure in a
go-cart.

At a minimum, a project such as this violates the first rule of programming:
If it's working, leave-it-the-hell-alone!
```

###### ↳ ↳ ↳ Re: Microfocus COBOL question: MOVE 'N' TO DCLININV-CSR-OPEN.

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-06-26T22:34:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10dsg2qlop4hbfb@corp.supernews.com>`
- **In-Reply-To:** `<0fCdne90ZMeIglPdRVn-sA@giganews.com>`
- **References:** `<L1mzc.314$UnA1.141@news04.bloor.is.net.cable.rogers.com> <8orrc0tv8doma5qk9naeoubm56e57t6nft@4ax.com> <LAozc.32$BrC1.7@news04.bloor.is.net.cable.rogers.com> <0fCdne90ZMeIglPdRVn-sA@giganews.com>`

```
JerryMouse wrote:
> Thomas A. Li wrote:
> 
…[4 more quoted lines elided]…
> If it's working, leave-it-the-hell-alone!

But it supports the rule "If you market a COBOL-to-Java product, and a 
potential client has given you a program your translator can't handle, 
you need to make it work (and fast) so you don't lose them, which may 
negatively impact your paycheck."  :)
```

###### ↳ ↳ ↳ Re: Microfocus COBOL question: MOVE 'N' TO DCLININV-CSR-OPEN.

_(reply depth: 5)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-06-27T07:34:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r9WdnfoNHNdQI0Pd4p2dnA@giganews.com>`
- **References:** `<L1mzc.314$UnA1.141@news04.bloor.is.net.cable.rogers.com> <8orrc0tv8doma5qk9naeoubm56e57t6nft@4ax.com> <LAozc.32$BrC1.7@news04.bloor.is.net.cable.rogers.com> <0fCdne90ZMeIglPdRVn-sA@giganews.com> <10dsg2qlop4hbfb@corp.supernews.com>`

```
LX-i wrote:
> JerryMouse wrote:
>> Thomas A. Li wrote:
…[10 more quoted lines elided]…
> negatively impact your paycheck."  :)

Which generates another axiom: It's hard to market a solution for a problem
that....

"Negatively impact?"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
