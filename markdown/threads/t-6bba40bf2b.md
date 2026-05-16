[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PowerCOBOL Control Mumble-Mumble

_4 messages · 2 participants · 2004-11_

---

### PowerCOBOL Control Mumble-Mumble

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-11-15T07:46:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wvednXoehZzdLgXcRVn-iA@giganews.com>`

```
Consider a PC TextBox control with a GotFocus Event.....

When the control is accessed via a mouse-click, the text is selected 
(highlighted). When the control is accessed via [TAB] the text is not 
selected.

I have determined that fiddling with the control in the GotFocus Event turns 
off the text selection. For example, the line:

  MOVE WSDUM TO 'Text' OF TXT-1

in the GotFocus event disables the text selection via [TAB] but not via 
mouse. That is, when reaching the field by tabbing, the text is not 
selected; clicking on the field, however, does select (light-up, highlight) 
all the text.

I want the text selected no matter how the user reaches the field.

Any ideas anyone?

Thanks
------
Here's the whole GotFocus Event:

   MOVE 'TEXT' OF TXT-1 TO WSDUM.
   MOVE '------9' to 'PictureString' of 'RenderText' OF TXT-1
   COMPUTE WSDUM = WSDUM * 100
   MOVE WSDUM TO 'TEXT' OF TXT-1.

===========
I'm JerryMouse and I approved this message.
```

#### ↳ Re: PowerCOBOL Control Mumble-Mumble

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-11-16T14:08:43+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2vt290F2odv6uU1@uni-berlin.de>`
- **References:** `<wvednXoehZzdLgXcRVn-iA@giganews.com>`

```
 When you open the form (in the OPEN event)

           move POW-TRUE to "SelectText" of [control name]...

TABbing to it will show selected text, as will clicking on it.

It is not advisable to set properties on GotFocus, because the act of
setting them can raise another GotFocus event and this gets queued, with
unpredictable results, under certain (admittedly rare) circumstances. I make
it a practice to set all properties BEFORE I activate the control, and I
don't usually rely on the default properties to be intact.

I would put the line of code above as the last statement in the RETURN
event, as well as in the Form OPEN.

HTH,

Pete.

"JerryMouse" <nospam@bisusa.com> wrote in message
news:wvednXoehZzdLgXcRVn-iA@giganews.com...
> Consider a PC TextBox control with a GotFocus Event.....
>
…[4 more quoted lines elided]…
> I have determined that fiddling with the control in the GotFocus Event
turns
> off the text selection. For example, the line:
>
…[4 more quoted lines elided]…
> selected; clicking on the field, however, does select (light-up,
highlight)
> all the text.
>
…[18 more quoted lines elided]…
>
```

##### ↳ ↳ Re: PowerCOBOL Control Mumble-Mumble

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-11-15T21:13:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NNOdnZSFCZmg7QTcRVn-rg@giganews.com>`
- **References:** `<wvednXoehZzdLgXcRVn-iA@giganews.com> <2vt290F2odv6uU1@uni-berlin.de>`

```
Pete Dashwood wrote:
> When you open the form (in the OPEN event)
>
…[9 more quoted lines elided]…
> properties to be intact.

But doesn't setting the properties (under admittedly rare) circumstances 
raise the GotFocus event?

>
> I would put the line of code above as the last statement in the RETURN
…[4 more quoted lines elided]…
> Pete.

Thanks for the advice.

1. SelectText defaults to TRUE.
2. For a Text Box, SelectText can only be referenced (not set) at execution 
time.
3. Testing the SelectText property shows that it is true.

You're right about the control going a little silly. If nothing but reading 
the contents takes place in the GotFocus control, the SelectText doesn't 
wink off. Moving something to the control in the GotFocus event (or changing 
the RenderText sub-property) turns off the text selection.

I need a PreGotFocus event.
```

###### ↳ ↳ ↳ Re: PowerCOBOL Control Mumble-Mumble

- **From:** "Peter E.C Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-11-16T23:05:47+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1100599554.F9wcJuR5/aVBpqMCfa9qKQ@teranews>`
- **References:** `<wvednXoehZzdLgXcRVn-iA@giganews.com> <2vt290F2odv6uU1@uni-berlin.de> <NNOdnZSFCZmg7QTcRVn-rg@giganews.com>`

```

"JerryMouse" <nospam@bisusa.com> wrote in message
news:NNOdnZSFCZmg7QTcRVn-rg@giganews.com...
> Pete Dashwood wrote:
> > When you open the form (in the OPEN event)
…[13 more quoted lines elided]…
> raise the GotFocus event?

No. Not normally. Changing properties should not activate ANY events.  I
have seen it happen a couple of times where what was being asked of the
event processing was not starightforward (that's why I noted it is a rare
occurrence.) > >

> > I would put the line of code above as the last statement in the RETURN
> > event, as well as in the Form OPEN.

OK, I take your point that if it isn't modifiable at run time that is
pointless. Sorry.

> >
> > HTH,
…[5 more quoted lines elided]…
> 1. SelectText defaults to TRUE.

Yes, I know. I implied that above.

> 2. For a Text Box, SelectText can only be referenced (not set) at
execution
> time.

That, I did not know. Sorry. You may find there is a connection here between
multiline and single line TB behaviours.

> 3. Testing the SelectText property shows that it is true.
>
Then the text MUST be selected.

> You're right about the control going a little silly. If nothing but
reading
> the contents takes place in the GotFocus control, the SelectText doesn't
> wink off. Moving something to the control in the GotFocus event (or
changing
> the RenderText sub-property) turns off the text selection.
>

Have another look at the edit conditions. It sounds edit-related to me. If
the control thinks the return event has been generated it might well
de-select the text.

> I need a PreGotFocus event.

You can get one when tabbing  (LostFocus on the previous TAB field... I did
this once; never again), but not on clicking.

I'd need to see the control before further speculation.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
