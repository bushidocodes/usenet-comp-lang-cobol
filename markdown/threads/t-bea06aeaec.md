[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL77 Escape Sequences

_3 messages · 3 participants · 1999-04_

---

### COBOL77 Escape Sequences

- **From:** steverob3621@my-dejanews.com
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ej30c$vpk$1@nnrp1.dejanews.com>`

```
I'm sure there is an easy answer to this but, I haven't found it, yet! Using
COBOL77, how can I send "Escape Sequences" to a dumb terminal or printer?

I'm trying to create data entry screens and wanted to spruce them up a bit. I
know what the sequences are for the terminals and printer. Just haven't
figured out how to send them from a DISPLAY or WRITE instruction.

If someone could provide a short example, I'd appreciate it.


TIA,

Steve Robertson <steverob@hotoffice.com>

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: COBOL77 Escape Sequences

- **From:** Bernard Liengme <bliengme@stfx.ca>
- **Date:** 1999-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370E3FAA.53AE508D@stfx.ca>`
- **References:** `<7ej30c$vpk$1@nnrp1.dejanews.com>`

```
Steve:
Here is some code to try.
01 print-8lpi.
    02  esc          pic s99 binary value 27.
    02                 pic 9    value 0.
....
write print-rec from print-8lpi            ' sets an Espsom printer to 8
lines/inch

01    print-italic.
    02                pic s99 binary value 27.
    02                pic x(4)            value "(s1S0".
write print-rec from print-itallic        ' sets an HP printer to italic mode

Other ways:
        01 print-italic-off.
            02        pic x  value x"1B".               ' code for Micro focus
            02        pic x(4)    value "(s0S".        ' turns itallic off
Equivalent code fo Ryan-McFarland (Liant)
        01 print-italic-off.
            02        pic x  value H"1B".               ' code for Micro focus
            02        pic x(4)    value "(s0S".        ' turns itallic off

And one more
configuration section.
special-names.
    symbolic characters escape-char is 28.
....
01 print-itallic.
    02 pic x        value escape-char.
    02 pic x(4)    value "(s1S".

Good luck
Bernard
author of "Cobol by Command" - details at amazon.com

steverob3621@my-dejanews.com wrote:

> I'm sure there is an easy answer to this but, I haven't found it, yet! Using
> COBOL77, how can I send "Escape Sequences" to a dumb terminal or printer?
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: COBOL77 Escape Sequences

- **From:** Steve Robertson <steverob@hotoffice.com>
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370F415C.7A25246A@hotoffice.com>`
- **References:** `<7ej30c$vpk$1@nnrp1.dejanews.com> <370E3FAA.53AE508D@stfx.ca>`

```
Bernard Liengme wrote:
> 
> Steve:
…[3 more quoted lines elided]…
>     02                 pic 9    value 0.

Thanks Bernard,

This helps.

I'm still not getting exactly what I'm looking for on the terminal. If I
replace the "27" with other values the ASCII equilivent prints on my
terminal. However, it doesn't seem to be working with "ESC". At least
it's not printing "27" anymore ;-)

I'll have to capture the data on the comm port and see if the correct
string is being sent to the terminal. It possible the computer is
stripping out those characters before sending them to the terminal or
the terminal is not intrepreting them correctly. Actually, the problem
is most likely with my coding.

I originally learned COBOL in college, more than 20 years ago. Seems
like I've killed a lot of brain cells since then...

Thanks again,

Steve Robertson <steverob3621@my-dejanews.com wrote>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
