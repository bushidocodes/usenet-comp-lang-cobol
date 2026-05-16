[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# event driven, execute with no return

_1 message · 1 participant · 1999-02_

---

### Re: event driven, execute with no return

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a7ta0$1ih@lotho.delphi.com>`
- **References:** `<7a4bpm$gr0$1@news1.epix.net> <36c75626.0@mercury.nildram.co.uk>`

```

Ah- the concept of OS Semaphores makes it to COBOL at last... :) 

<grin>


Simon Cordingley (simonc@casegen.co.uk) wrote:
: I have done something similar to this in a Casegen program - might be worth
: trying in PowerCobol.

: If I understand you correctly, you want to be able to cancel outstanding
: events from an event in your form.

: Create a WS-CANCEL variable with a 88 level - "CANCEL-EVENT". All
: cancellable events must now check the variable before processing:

: IF CANCEL-EVENT
:     GO TO event-EXIT
: END-IF

: normal event code....

: Make the variable EXTERNAL if you have non-modal dialogs to allow for
: changing events accross multiple forms.

: Don't forget, there will have to be code in a non-cancellable event to
: ENABLE the events again!

: Hope this may help.

: Simon Cordingley
: Casegen Systems Ltd
: www.casegen.co.uk

: don ferrario wrote in message <7a4bpm$gr0$1@news1.epix.net>...
: >I am working with Fujitsu PowerCobol, which like some others
: >is an event driven cobol system.
: >
: >When a program statement (such as changing focus to a control)
: >generates an event, an event program is begun.
: >
: >When the event program ends, flow returns to the original point,
: >as expected.
: >
: >PROBLEM:  I don't always want the program flow to return.  Depending
: >on the user's actions, these returns can stack up, and the flow is
: sometimes
: >not as desired.
: >
: >Is there a statement, within a subprogram, which can be issued which
: >will cancel all previous  waiting subprograms?  This almost sounds
: >like the old ALTER statement, but not quite.  CANCEL comes to mind,
: >but so far as I know, you can only CANCEL programs under the current
: >one, not programs executing *above* the current program.
: >
: >This is becoming quite a problem for me, because depending on how
: >the user interacts with the program, it is almost impossible to code
: >anticipating
: >all the possible program return-flows.
: >
: >don ferrario
: >http://www.ferrario.com/don
: >
: >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
