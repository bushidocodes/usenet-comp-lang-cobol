[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help! Data input problem!

_4 messages · 4 participants · 1998-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help! Data input problem!

- **From:** Jean-michel Hiver <hiver@emi.u-bordeaux.fr>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365AEB73.31631EEC@emi.u-bordeaux.fr>`

```
Hi!

I'm a beginner in programming cobol and I have a problem I can't solve.

I have this data structure:

01 price
  05 dollars	PIC 9(4).
  05 cents	PIC 99.

I'm trying to avoid prompting the user:
"Enter the dollars:"
then
"Enter the cents".

What i'd like to do is juste something like

"Enter stuff price:"

then the user's input could be
5312
or
234.15

or whatever. Can you help, please ?
```

#### ↳ Re: Help! Data input problem!

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uGwYo7$F#GA.328@upnetnews03>`
- **References:** `<365AEB73.31631EEC@emi.u-bordeaux.fr>`

```
Check out usage of FUNCTION NUMVAL (user-input-field).

Jean-michel Hiver wrote in message <365AEB73.31631EEC@emi.u-bordeaux.fr>...
>Hi!
>
…[26 more quoted lines elided]…
>jhiver@usa.net
```

#### ↳ Re: Help! Data input problem!

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73h1tt$ije$1@news.igs.net>`
- **References:** `<365AEB73.31631EEC@emi.u-bordeaux.fr>`

```
Jean-michel Hiver wrote in message <365AEB73.31631EEC@emi.u-bordeaux.fr>...
>I'm a beginner in programming cobol and I have a problem I can't solve.
>I have this data structure:
>01 price
>  05 dollars PIC 9(4).
>  05 cents PIC 99.


If you want to accept the data in a different format, then
define the new format, accept that, and move the data
into the fields that you want.  I would look at the screen
section for formatted data input.  The accept and display
variable (as opposed to screens) verbs are quite primitive
and really only there for debugging and console use.
```

#### ↳ Re: Help! Data input problem!

- **From:** "Warren Porter" <warrenp@netdoornospam.com>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ecd72.2392$b53.12131@axe.netdoor.com>`
- **References:** `<365AEB73.31631EEC@emi.u-bordeaux.fr>`

```
I kinda question breaking down 'price' into dollars and cents, just define
it as 9(4)V99.  But to let the user have the option of entering a decimal
point or not:

Define a separate array for entry [PIC X w/ occurs] and redefine each PIC X
with a PIC 9.  You will also have to redefine the CENTS field to reference
each byte of it as well.  After accepting user input into the array, first
zero the PRICE field and a secondary subscript field.  In a perform varying
a primary subscript for each position of your input array

IF char(x) NUMERIC
   IF SUBSCR = ZERO
     COMPUTE PRICE = PRICE * 10 + char-redef-9(x)
   ELSE
     MOVE char(x) TO cent-array(SUBSCR)
     ADD 1 TO SUBSCR
ELSE
  IF char(x) = "."
     MOVE 1 TO SUBSCR
END-PERFORM (if needed)

HTH

Jean-michel Hiver wrote in message <365AEB73.31631EEC@emi.u-bordeaux.fr>...
>I have this data structure:
>
…[18 more quoted lines elided]…
>or whatever. >jhiver@usa.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
