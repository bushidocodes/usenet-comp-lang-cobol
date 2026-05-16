[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Learning OO COBOL - What's the right construction?

_4 messages · 4 participants · 2000-03_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo) · [`Tutorials, books, learning`](../topics.md#learning)

---

### Learning OO COBOL - What's the right construction?

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38caa5c8.234139948@news.cox-internet.com>`

```
How's that for a loaded question?

I've not written a line of OO COBOL yet.  I'm still reading and
learning. I can see how OO pundits can get into religious wars over
the "right" way to do things.  It's not my intent to start such a
discussion -- I simply want to get a jump start based on others'
experience.

Let me take a very small example and illustrate what I mean and ask
some questions.

Even though I want to STRESS that OO is not about the user interface,
this example is a UI example.

The message box (Direct API or sp2 call does not matter).

With a message box you need a title, a message, and a button or
buttons, one of which is the "default" choice button.

Now lets say I want to use OO to implement a message box.  

I can see at least 2 approaches.

The first approach is to basically code the message box presentation
in the NEW method of a factory object, passing as parameters the
title, message text, buttons and default button.  Seems simple - and
maybe the right way to do it.  

I see another approach, which I personally like better.  What I want
to know is what the OO pundits here think about it.

Create a Message Box Class.

In the Factory New method, simply initialize the values used in the
API (or Sp2) call to create a message box.  When New is invoked a
handle to this initialized object is returned.

Next either using implicit Set's or explicit set methods, set the
properties of the object that was just created.  Set the message box
title, the text, the buttons and the default button.

Next, using the handle of this object, invoke the "present" method,
which returns the button clicked by the user.  

Then destroy the object.

The advantages I see to the second approach are interesting.  There's
nothing to prevent me from creating ALL of my message box objects
FIRST, and invoking them when necessary and NOT destroying them until
the application is ended.  I can have multiple instances of the
object, with object references stored in a table, or maybe even in a
Collection object (Jimmy, is that what these things are for?).

Or I can create them one at a time.

Let's say that now I want to split the message text to multiple lines
instead of one long line.  I can add some code, or use another method
to override the default Set method, that parses the line and splits it
up based on some maximum length I pass as a property with the SET
method.  

Opinions?
```

#### ↳ Re: Learning OO COBOL - What's the right construction?

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CB6EA2.2070CBCF@zip.com.au>`
- **References:** `<38caa5c8.234139948@news.cox-internet.com>`

```
Thane Hubbell wrote:
> 
> How's that for a loaded question?
…[5 more quoted lines elided]…
> experience.

> The message box (Direct API or sp2 call does not matter).
> 
> With a message box you need a title, a message, and a button or
> buttons, one of which is the "default" choice button.

The message box is a utility function, it typically is something that
is built on the fly and destroyed.  I would therefore recommend that
you create the object with the required data and get rid of it. 
Message boxes typically have a small subset of buttons, equivalent to
OK, cancel, no, help.  The selected button can be simply returned.

When you talk about a window however, you are talking about a long
term object, it can be created and modified.  Each button in the
window is also an object contained within the window.  I would design
this the second way. The only modification I would say is that objects
are always in a consistent state.  For example the title bar is not
'unset' it is a blank string.  The distinction is small but important.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: Learning OO COBOL - What's the right construction?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CAFBD6.E2D28979@home.com>`
- **References:** `<38caa5c8.234139948@news.cox-internet.com>`

```


Thane Hubbell wrote:
> 

Very, very briefly and I'll look at this in more detail later. The
messagebox bit is Windows - so keep our business logic separate from
Windows/Linux/Unix whatever. Business logic determines it should send a
message (messagebox). As you know from my code I'm currently doing this
in business logic - because it's one of the easiest things to do and
it's low priority - design wise.

But it makes sense to create a class MyMessageBox, (which Simon in UK
has done), pass it the title, message and get a return-button if
necessary. I would suggest messagebox is an exception, so only create,
show and destroy for a particular 'incident'.

Proviso, if you are 'heavy' into informative messages for the user, then
it would make sense to invoke it "new" returning os-MessageBox to
Business Program then for each message you can pass the parameters to
os-Messagebox.

Just quickly off the top of my head - the actual message - somebody may
wish to clarify this, but I haven't seen anything that lets me know 'how
wide' Windows allows for a line, (i.e. when does Windows hiccup and put
your unbroken text on the next line). Ok be a sport Bob - I'm not using
SP2 - bet you know the answer to this one. One way or another you could
pass a fairly large message, inserting say 'tilde' as a
'breakline-character, get into the message box, unstring into separate
lines etc., or use the 'tilde' doing a string delimited by 'tilde' etc.
I'm afraid all rather vague and off the cuff.

*** Read below - for that 'tilde' above substitute x"0d0a"

Query - why large message ? Because I do generate the following type of
message :-

		-------------------------------------------------
		The following files could not be located :-
			
		\Chevron-Resources-Canada-Ltd\Jumping-Pound-Creek

			CHV-22-Items.dta
			CHV-22-Readings.dta
			CHV-22-Technicians.dta
			CHV-22-Vessels.dta

		Do you want to open empty files ?

			<OK>	<Cancel>

		--------------------------------------------------

For the above I send the list of file-names (that's it ! Not the 'tilde'
- with CR LF x"odoa").  And there are obviously many permutations to
doing this. But it really makes sense to treat it as
Non-COBOl/non-business - a message feature required for the O/S. I'll
get around to MyMessageBox when I have the time.

> How's that for a loaded question?

Not loaded to me - just asking for info :-)

PS: Cheesle - Presumably you do this stuff with 'dual' Screen Section
???

Jimmy
```

##### ↳ ↳ Re: Learning OO COBOL - What's the right construction?

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38cd4ea1.25298798@news.epix.net>`
- **References:** `<38caa5c8.234139948@news.cox-internet.com> <38CAFBD6.E2D28979@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote:

>Thane Hubbell wrote:
>> 
…[26 more quoted lines elided]…
>I'm afraid all rather vague and off the cuff.

Jimmy...

since you asked...the answer is that it is completely automatic.  The
message box facility will adjust the display of the message box to
display on as many lines as are needed with automatic word wrap.  In
addition, the size of the message box will automatically increase to
accomodate more text, if need be.

no tildes necessary.

...but it does sound much more fun to use tildes, braces, ampersands,
parentheses and other squiggly lines to accomplish the same thing. <g>


>*** Read below - for that 'tilde' above substitute x"0d0a"
>
…[32 more quoted lines elided]…
>Jimmy

Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
