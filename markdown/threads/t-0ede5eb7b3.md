[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Newbie Q: validating fields / printing invalid

_24 messages · 12 participants · 1998-03_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Newbie Q: validating fields / printing invalid

- **From:** "chris zappanti" <ua-author-2615462@usenetarchives.gap>
- **Date:** 1998-03-10T12:31:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35057848.DF066000@pcsinconline.com>`

```

Hi,

I'm taking Cobol at college and have a simple question. If I have a
numeric field and I read an invalid vlaue into it, such as AB34C or
blanks from a file, how in the world do I print the erroneous value?
I've tried transferring the value into another field with the pic of
x(9) and printing from there, but it still halts on the invalid value
read into the original numeric field.

Should I read everything into a Pic XXXX type field and then
convert/transfer over to a numeric at a later point to provide a buffer
or have I missed something simple?

Thank you,
Chris Zappanti
```

#### ↳ Re: Newbie Q: validating fields / printing invalid

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-09T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35057848.DF066000@pcsinconline.com>`
- **References:** `<35057848.DF066000@pcsinconline.com>`

```


Chris Zappanti wrote in message <350··.@pcs··e.com>...
› Hi,
› 
…[13 more quoted lines elided]…
› 

Yes, you have missed something simple (but depending on what order your
class handles things, you may not have been taught it yet). Look at
REDEFINING your numeric field as PIC X and displaying that. When you move a
numeric field to a PIC X field, the numeric field has to be (well is
SUPPOSED TO BE) valid. However, when you redefine it, it doesn't have to
be.
```

##### ↳ ↳ Re: Newbie Q: validating fields / printing invalid

- **From:** "chris zappanti" <ua-author-2615462@usenetarchives.gap>
- **Date:** 1998-03-10T14:04:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p2@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap>`

```

› Yes, you have missed something simple (but depending on what order your

class handles things, you may not have been taught it yet). Look at
REDEFINING your numeric field as PIC X and displaying that. When you
move a
numeric field to a PIC X field, the numeric field has to be (well is
SUPPOSED TO BE) valid. However, when you redefine it, it doesn't have
to
be.<

Thanks for your reply. I want to be sure I have this straight on my
end...

I have a field:
05 IN-VALUE PIC 9V99
88 VALID-VALUE 0.00 THRU 4.00

The possibility exists that garbage will be read into that field, such
as blanks, alphanumeric values, etc. If I need to screen the field and
print the garbage, say in this example spaces rather than a value, I
use:

05 ERR-FIELD REDEFINES IN-VALUE PIC XXX.

So I test IN-VALUE for numeric, if it fails I use ERR-FIELD to print
from. Is it true in this case that if IN-VALUE fails the numeric test
that ERR-FIELD will in fact have the erroneous data? I guess from my
limited Cobol point of view I'm not clear about one crucial point. If
the field is numeric and alpha characters are read, are they in fact
contained in the IN-VALUE field? If they are allowed into the field
then is the statement "Cobol generates RT errors for illegal characters
AFTER they have been read into a field and WHEN you attempt to do
something with them?"

Hate to be so questioning, but coming from another language into this
leaves me with a million questions. The book & teacher address what to
do if there is an invalid range of numbers, etc., but they're kind of
silent on the issue how how to handle garbage into a field and the
errors it creates. Unless I'm misinterpreting some of this.

Thank you again,
Chris Zappanti
Zap··.@pcs··e.com
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-09T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p3@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap>`

```

Chris Zappanti wrote in message <350··.@pcs··e.com>...
›› Yes, you have missed something simple (but depending on what order your
› 
…[41 more quoted lines elided]…
› 
Chris,
I think that the approach you are suggesting should work. There is one
slight problem with "displaying" the alphanumeric field. If the "bad" data
isn't display data (such as hex or low-values), then you may still have some
problems reading the bad data.

As to your question on "invalid data". When it causes a problem partially
depends on how you get it into the numeric field. However, unless there are
"exceptional' circumstances, you should only get errors when you try and use
the numeric field AS a numeric field, not when you are populating it.

I hope this make sense and is useful.
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-03-09T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p3@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap>`

```

In article <350··.@pcs··e.com>,
Chris Zappanti wrote:
›› Yes, you have missed something simple (but depending on what order your
› 
…[23 more quoted lines elided]…
› from.

Well now, I would say that is right close... and you are showing good
effort and willingness to do things on your own so let me step forward and
put my foot in my mouth.

A field which is 'created' as the result of a REDEFINEs is not really
'created'... it is the original field considered under the rules of the
redefinition. In your example:

05 IN-VALUE PIC 9V99 VALUE 0.0. (<== always initialise)
88 VALID-IN-VALUE VALUES 0.00 THRU 4.00. (more descriptive 88)
05 ERR-FIELD REDEFINES IN-VALUE PIC X(3).

Consider what happens when Things Go Right (the rare occurrence).
IN-VALUE gets populated with 1.23; since the V is an implied decimal
IN-VALUE contains x'F1F2F3' (in EBCDIC, x'313233' in ASCII). ERR-FIELD,
since it uses the same data area (level 66, anyone) as IN-VALUE, *also and
simultaneously* contains x'F1F2F3' (or x'313233'); *any* change in either
data-name will show up in the other.

Now comes the valuable part. If you try to refer to a numeric field which
contains non-numeric data you run the risk of generating an
error-condition (technically known as 'le kerflooie grande'). If IN-VALUE
gets garbage in it... say, 1A3 (x'F1C1F3' or x'314533') then you do not
want to refer to it lest you attempt to perform calculations on
non-numeric data and the computer gets confused... what is A = 3?

So, then, logic might be coded:

IF IN-VALUE NUMERIC
IF VALID-IN-VALUE
PERFORM VALID-IN-VALUE-RITUAL THRU VIVR-EX
ELSE
PERFORM INVALID-IN-VALID-RITUAL THRU IIVR-EX
ELSE
DISPLAY ' CHECK-IN-VALUE PARAGRAPH '
DISPLAY ' IN-VALUE NOT NUMERIC '
DISPLAY ' IN-VALUE CONTAINS: ', ERR-FIELD'
PERFORM PROCESS-GARBAGE-INVAL THRU PGI-EX.


Now of course some folks will take exception with my style... but nobody
will take exception that the above code will compile ANSI-68 or better and
will be understood by a two-year programmer doing maintenance.

DD
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1998-03-10T17:27:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p3@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap>`

```

In article <350··.@pcs··e.com>,
Chris Zappanti wrote:
›› Yes, you have missed something simple (but depending on what order 
› your
…[25 more quoted lines elided]…
› 
 
› Yep.
 
› So I test IN-VALUE for numeric, if it fails I use ERR-FIELD to print

Nope. You test ERR-FIELD for numeric. If it's not numeric, trying to
test IN-VALUE will bomb the program. If ERR-FIELD is not numeric, then
you print from ERR-FIELD. If ERR-FIELD is numeric, then you test
IN-VALUE to make sure the data is within the specified range.

› from.  Is it true in this case that if IN-VALUE fails the numeric 
› test
…[4 more quoted lines elided]…
› contained in the IN-VALUE field?  If they are allowed into the field

Yes, they are. They are also contained in ERR-FIELD, because the two
labels map the *same* three bytes in memory. REDEFINES means literally
that: the new definition (PIC XXX) redefines the same field in another
way -- in this case, as alphanumeric, instead of strictly numeric.

› then is the statement "Cobol generates RT errors for illegal 
› characters
› AFTER they have been read into a field and WHEN you attempt to do
› something with them?"

If you attempt to do something with them using the IN-VALUE
definition, then you have a problem. But not if you use ERR-FIELD.
Fields defined as alphanumeric (PIC X) may contain anything.
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 4)_

- **From:** "jim k" <ua-author-718715@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p6@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap>`

```

(Doug Miller) wrote:
› 
› In article <350··.@pcs··e.com>,
…[22 more quoted lines elided]…
› 

Sorry, this is incorrect. The purpose of the numeric check is to allow
numeric fields to be checked before using the data. If you redefine the
numeric field to alpha-numeric, how does the program know that it is
display numeric versus packed numeric.
You should always check the numeric field for numeric, as the original
poster stated.


›
› If you attempt to do something with them using the IN-VALUE
› definition, then you have a problem. But not if you use ERR-FIELD.
› Fields defined as alphanumeric (PIC X) may contain anything.
But, again, if checking for numeric, how does the compiler know to check
for display or packed unless you check the numeric field itself!

Jim K
Old COBOL prgrammer, been there, done that, got the coding scars to
prove it.


* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"The important thing is to stop lying to yourself.  A man 
 who lies to himself, and believes his own lies, becomes 
 unable to recognize the truth, either in himself or in 
 anyone else, and he ends up losing respect for himself 
 as well as for others.  When he has no respect for anyone, 
 he can no longer love and, in order to divert himself, 
 having no love in him, he yields to his impulses, indulges 
 in the lowest forms of pleasure, and behaves in the end 
 like an animal, in satisfying his vices. 
 And it all comes from lying -- lying to others and to yourself."

        --Feodor Mikhailovich Dostoyevsky from his 1880 work, 
          "The Brothers Karamazov"


* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 5)_

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p7@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap>`

```

Guess again,
If you have a compiler that lets you test a packed field for "IF NUMERIC"
then you have an extension. The current Standard ONLY lets you test DISPLAY
fields for IF NUMERIC. (Many compilers do have an extension for testing
packed fields - and the next Standard should also allow this, but it isn't
something you can do today - and stay conforming. And if you think about
testing a binary field, you'll realize it can't ever fail.)

It is still reasonable to test the numeric rather than the alphanumeric
version of the field - but this only really makes a difference if the
numeric field is signed. If it is unsigned (as in this case) testing the
alphanumeric field will work exactly as requested.
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 6)_

- **From:** "jim k" <ua-author-718715@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p8@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap> <gap-0ede5eb7b3-p8@usenetarchives.gap>`

```

William M. Klein wrote:
› 
› Guess again,
…[4 more quoted lines elided]…
› something you can do today - and stay conforming.
I was not aware that this was an extension. All of my experience is on
mainframe cobol. Several versions, but COBOL nonetheless.

How did the standard expect packed fields to be verified?

› And if you think about
› testing a binary field, you'll realize it can't ever fail.)
 
› Never expected this to happen.
 
› It is still reasonable to test the numeric rather than the alphanumeric
› version of the field - but this only really makes a difference if the
› numeric field is signed.  If it is unsigned (as in this case) testing the
› alphanumeric field will work exactly as requested.
While this is true, it is more *consistent* to check the numeric field
everytime. And, unfortunately, consistency is one the difficult things
to come by in programming.



› + Bill Klein -
› "C" is a nice letter to START the name of your programming language
› with but I wouldn't want to end up there.
›
›
I like your sig, I ,with your permission, will add it to my permanent
quote file.

Jim K.

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"The important thing is to stop lying to yourself.  A man 
 who lies to himself, and believes his own lies, becomes 
 unable to recognize the truth, either in himself or in 
 anyone else, and he ends up losing respect for himself 
 as well as for others.  When he has no respect for anyone, 
 he can no longer love and, in order to divert himself, 
 having no love in him, he yields to his impulses, indulges 
 in the lowest forms of pleasure, and behaves in the end 
 like an animal, in satisfying his vices. 
 And it all comes from lying -- lying to others and to yourself."

        --Feodor Mikhailovich Dostoyevsky from his 1880 work, 
          "The Brothers Karamazov"


* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 7)_

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p9@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap> <gap-0ede5eb7b3-p8@usenetarchives.gap> <gap-0ede5eb7b3-p9@usenetarchives.gap>`

```

In article <350··.@ea··r.com>, Jim K wrote:
› William M. Klein wrote:
›› 
…[10 more quoted lines elided]…
› 

Unpack it to a DISPLAY field... as I recall the IBM manual shows IF fldnam
NUMERIC working on COMP-3 fields in Big Blue Ink, meaning that it is an
IBM extension.

DD
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 8)_

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p10@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap> <gap-0ede5eb7b3-p8@usenetarchives.gap> <gap-0ede5eb7b3-p9@usenetarchives.gap> <gap-0ede5eb7b3-p10@usenetarchives.gap>`

```

doc··.@cl··k.net wrote
because
William M. Klein wrote
because
Jim K wrote
because
Doug Miller wrote.

Some thoughts from my side:

Fact: DISPLAY is a USAGE, it is not the same as PICTURE X. This seems to me one of
the misinterpretations in the discussion. In my experience it has been a
misinterpr. in many discussions.
Fact: Class conditions on non-DISPLAY are nonconforming The Standard. Ones goal
should be to prevent non-numerics by early testing, in the input-stage. Packed data
should be reliable before it is packed.
Fact: REDEFINES is just another way to *look* at the same memory, but does not
change it, so it is dangerous if not understood that way. When I put on a pair of
sun-glasses (is that correct english) the world does not change, but my perception.
another analogy: when I stick another piece of paper on a bottle of HCl, then the
contents does *not* suddenly change from acid to milk nor vice versa. So: a NUMERIC
test on the pic XXX original does not take into account the format of the
redefiner: not the sign, not the number of digits, not the editing, especially not
the USAGE.
Fact: A numeric test on a field with a picture other than X(n) or 9(n) is either
"to be sure" or a faulty design. (The error in design being for example one or more
of these: 1) accepting non-display data which is not garantueed to be numeric
[symptom:usage not display] 2) letting someone type in a sign combined with digit
[symptom: S in picture] 3) not being userfriendly in the inteface [symptom: V in
picture])

Some thoughts!

The Frog, considering programming in Cobol
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 9)_

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p11@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap> <gap-0ede5eb7b3-p8@usenetarchives.gap> <gap-0ede5eb7b3-p9@usenetarchives.gap> <gap-0ede5eb7b3-p10@usenetarchives.gap> <gap-0ede5eb7b3-p11@usenetarchives.gap>`

```

In article <350··.@I··.nl>,
Cobol Frog (Huib Klink) wrote:
› doc··.@cl··k.net wrote
› because
…[8 more quoted lines elided]…
› Fact: DISPLAY is a USAGE, it is not the same as PICTURE X.

This may be a difference in loose terminology; I was taught that DISPLAY
numerics are ones are composed of x'F0' - x'F9'... ones which will not be
distorted if one DISPLAYs them.

› This seems to me one of
› the misinterpretations in the discussion. In my experience it has been a
› misinterpr. in many discussions.
 
› First definitions, then logic... very good!
 
› Fact: Class conditions on non-DISPLAY are nonconforming The Standard. Ones goal
› should be to prevent non-numerics by early testing, in the input-stage. Packed data
› should be reliable before it is packed.

Fact: garbage can be found in data at any time; this is not a world where
'should' = 'is'. Now, as to what is 'reasonable verification' as opposed
to 'over-verification'... *that* is something best discussed over many
beers.

› Fact: REDEFINES is just another way to *look* at the same memory, but does not
› change it, so it is dangerous if not understood that way. When I put on a pair of
› sun-glasses (is that correct english)
 
› Close enough... also unhyphenated (sunglasses).
 
› the world does not change, but my perception.
 
› How do you know this?  (perception versus reality... another beer-talk)
 
› another analogy: when I stick another piece of paper on a bottle of HCl, then the
› contents does *not* suddenly change from acid to milk nor vice versa.

No, but it is no longer the original HCl as the level of free protons
diminishes.

› So: a NUMERIC
› test on the pic XXX original does not take into account the format of the
…[3 more quoted lines elided]…
› "to be sure" or a faulty design.

Or an awareness that garbage data can show up at *any* time... see my
assertion above.

› (The error in design being for example one or more
› of these: 1) accepting non-display data which is not garantueed to be numeric

Oh, come *on* now... imagine a customer-number, usually numeric...
suddenly, some bright-boy in a corner-office says 'All customers with
certain charateristics will have an 'A' as the first digit of the
customer-number.'

› [symptom:usage not display] 2) letting someone type in a sign combined
› with digit

'Letting'? I have had this as a requirement... of course, along with the
possibility that the user keys in, along with a + or a - (or neither,
defaults to +) either a decimal-number (.75), a fraction (3/4) or a
fraction with embedded spaces (3 / 4).

› [symptom: S in picture] 3) not being userfriendly in the inteface
› [symptom: V in picture])

Not all data are for users to 'interface' with, of course... and have you
ever had a data-feed from a supplier or customer which was prone to
containing 'garbage'? Test, test and then... test some more.

DD
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 10)_

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p12@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap> <gap-0ede5eb7b3-p8@usenetarchives.gap> <gap-0ede5eb7b3-p9@usenetarchives.gap> <gap-0ede5eb7b3-p10@usenetarchives.gap> <gap-0ede5eb7b3-p11@usenetarchives.gap> <gap-0ede5eb7b3-p12@usenetarchives.gap>`

```

doc··.@cl··k.net wrote:

› Cobol Frog (Huib Klink)  wrote:
 
› 8< [here and on other places]
 
›› Fact: DISPLAY is a USAGE, it is not the same as PICTURE X.
› 
› This may be a difference in loose terminology; I was taught that DISPLAY
› numerics are ones are composed of x'F0' - x'F9'... ones which will not be
› distorted if one DISPLAYs them.

Because of the tiny difference, it is dangerously easy to mis-interpret. Usage display
could be applied to a data-name with a numeric picture including an embedded sign (S,
not SEPARATE). The sign and the first or last digit are then combined says The Standard.

›› Fact: Class conditions on non-DISPLAY are nonconforming The Standard. Ones goal
›› should be to prevent non-numerics by early testing, in the input-stage. Packed data
…[5 more quoted lines elided]…
› beers.

I admit: the world does 100% not behave as I like. [I can still :) ]

8< [beer-talk initiating text]

›› another analogy: when I stick another piece of paper on a bottle of HCl, then the
›› contents does *not* suddenly change from acid to milk nor vice versa.
› 
› No, but it is no longer the original HCl as the level of free protons
› diminishes.
 
› the same happens when talking to beer.
 
›› So: a NUMERIC test on the pic XXX original does not take into account the format of
› the
…[6 more quoted lines elided]…
› assertion above.

I did not sy that such a test is forbidden. It's a pity that it is needed. One should
have done something different to avoid it's need. But it is not so, so we test over and
over. But at least we can learn from our faults and try to avoid in the future. By
following some rules that I try to imply in my "facts"

›› (The error in design being for example one or more
›› of these: 1) accepting non-display data which is not garantueed to be numeric
 
› I meant (for example) that at the interface level no 100% numeric test was implemented
 
› Oh, come *on* now... imagine a customer-number, usually numeric...
› suddenly, some bright-boy in a corner-office says 'All customers with
› certain charateristics will have an 'A' as the first digit of the
› customer-number.'

Design fault: Entering letters i.s.o. digits was not used yet but allowed. And then
using that data numerically is a design error or an overlooked mistake. One could have
tested that. This data has been passed to another system, written/designed by people
that were convinced that it was numeric all the time. Who convinced them? Someone either
not knowing the letter-possibility or ignoring it. Either way I recommend a
to-be-sure-test, but are unhappy with the need of it.

›› [symptom:usage not display] 2) letting someone type in a sign combined
›› with digit
…[4 more quoted lines elided]…
› fraction with embedded spaces (3 / 4).

I remember. Were some of the nicest subroutines to code :)). Good memories. But: the
requirement to make such possible was and is horrible. Although is is historically
explainable.

›› [symptom: S in picture] 3) not being userfriendly in the inteface
›› [symptom: V in picture])
…[3 more quoted lines elided]…
› containing 'garbage'?  Test, test and then... test some more.

Was he (suppl/cust) also proud?Helaas (NL)Leider (D)
Helas (FR)
Pity (?)

› DD

The Cobol Frog (meeting DD again)
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 11)_

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p13@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap> <gap-0ede5eb7b3-p8@usenetarchives.gap> <gap-0ede5eb7b3-p9@usenetarchives.gap> <gap-0ede5eb7b3-p10@usenetarchives.gap> <gap-0ede5eb7b3-p11@usenetarchives.gap> <gap-0ede5eb7b3-p12@usenetarchives.gap> <gap-0ede5eb7b3-p13@usenetarchives.gap>`

```

In article <350··.@I··.nl>,
Cobol Frog (Huib Klink) wrote:
› doc··.@cl··k.net wrote:
› 
…[13 more quoted lines elided]…
› last digit are then combined says The Standard.

'Could be', aye... but in my limited and humble experience USAGE IS
DISPLAY is encountered rarely, I have found that PICTURE IS is run across
more frequently. Since you make the claim 'it is dangerously easy to
mis-interpret' I feel the need to ask... have you frequently found
something this 'easy' occurring?

› 
››› Fact: Class conditions on non-DISPLAY are nonconforming The Standard. Ones goal
…[8 more quoted lines elided]…
› I admit: the world does 100% not behave as I like. [I can still :) ]

How generous of you! If you keep showing this sort of progress maybe next
week the nurse will cut back on your medications!

› 
› 8< [beer-talk initiating text]
…[7 more quoted lines elided]…
› the same happens when talking to beer.

Only if the beer is of sufficient quality that one can differentiate
between the going-down and coming-out stages.

› 
››› So: a NUMERIC test on the pic XXX original does not take into account the format of
…[9 more quoted lines elided]…
› I did not sy that such a test is forbidden.

... and a Good Thing that you didn't... saying such a thing would give the
nurse second thoughts about reducing your medications.

› It's a pity that it is
› needed. One should have done something different to avoid it's need.

It is a similar pity that an unimpeded objects accellerates towards the
earth at 9.8m/s/s ... yet is *is*.

› But it is not so, so we test over and over.
 
› Precisely... test, test again, test some more.
 
› But at least we can learn from
› our faults and try to avoid in the future. By following some rules that I
› try to imply in my "facts"

Hmmmmm... Santayana said that those who do not learn from the mistakes of
the past are bound to repeat them; Nietzsche spoke of an unbreakable
'cycle of eternal recurrence'... we will leave talk of whether it is even
*possible* to 'avoid in the future' to such philosophers (beer makes many
into philosophers, of course)... test, test again, test some more.

› 
››› (The error in design being for example one or more
…[10 more quoted lines elided]…
› Design fault: Entering letters i.s.o. digits was not used yet but allowed.

Fertiliser. Please explain how a change in specifications mandated by
Someone Of Sufficient Authority is a 'design fault'... I say that *no*
system can be designed with all possible future changes/enhancements in
mind.

› And then using that data numerically is a design error or an overlooked
› mistake.

Fertiliser. Someone changes the way that things are to be displayed
and/or interpreted. Last week a customer-number containing a letter of
*any* kind was invalid data, next week a customer-number for a customer of
certain characteristics which does *not* contain an 'A' as the first
character is invalid... things change, one must respond.

› One could have tested that. This data has been passed to another
› system, written/designed by people
› that were convinced that it was numeric all the time. Who convinced them?

The people who signed the paychecks convinced them that all
customer-numbers were numeric... it was very simple, if you wrote code
that allowed for an alpha in customer number then you did not get a
payckeck. (convincing enough to most people) Now someone who signs
paychecks says 'if condition-x and custno(1:1) not = 'A' perform
fire-the-programmer until situation-is-otherwise'.

› Someone either not knowing the letter-possibility or ignoring it.

Since, as previously stated, it is impossible to know all possible changes
which might be applied to a system then some things *must* be ignored in
order for anything to be accomplished; similarly, an
automobile-manufacturer *must* 'ignore the possibility' that the vehicles
it designs will ever be operated in a null-gravity environment... imagine
the time it would spend redesigning the cup-holder!

› Either way I recommend a to-be-sure-test, but are unhappy with the need
› of it.

So, in the end, then, test, test again and then test some more... perhaps
another beer will do something about that unhappiness?

› 
››› [symptom:usage not display] 2) letting someone type in a sign combined
…[8 more quoted lines elided]…
› memories.

Fascinating how such pleasant memories can result from horrible things...
and fascinating how lovely roses can grow from smelly fertiliser.

› But: the requirement to make such possible was and is horrible.

A programmer's life is a hard life, or so all the fishermen and
coal-miners tell me.

› Although is is historically explainable.

It is explicable quite easily by slight changes to the code-example I gave
above... re=use of the fire-the-programmer paragraph/section.

› 
››› [symptom: S in picture] 3) not being userfriendly in the inteface
…[8 more quoted lines elided]…
› Pity (?)

Pride has nothing to do with it... was the supplier's/customer's
pain-in-the-buttocksness sufficiently outweighed by other aspects of
maintaining the business relationship?

DD
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 12)_

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-15T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p14@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap> <gap-0ede5eb7b3-p8@usenetarchives.gap> <gap-0ede5eb7b3-p9@usenetarchives.gap> <gap-0ede5eb7b3-p10@usenetarchives.gap> <gap-0ede5eb7b3-p11@usenetarchives.gap> <gap-0ede5eb7b3-p12@usenetarchives.gap> <gap-0ede5eb7b3-p13@usenetarchives.gap> <gap-0ede5eb7b3-p14@usenetarchives.gap>`

```

doc··.@cl··k.net wrote:

› In article <350··.@I··.nl>,
› Cobol Frog (Huib Klink)  wrote:
…[19 more quoted lines elided]…
› more frequently.

That's because USAGE DISPLAY is default. And a good PICTURE is not. (defaults come in free,
a programmer has to be paid for)

›  Since you make the claim 'it is dangerously easy to
› mis-interpret' I feel the need to ask... have you frequently found
› something this 'easy' occurring?
 
› *Very* frequently. :(
 
›› I admit: the world does 100% not behave as I like. [I can still :) ]
› 
› How generous of you!  If you keep showing this sort of progress maybe next
› week the nurse will cut back on your medications!

But my med. against it was beer! I still want my beer. (No problem if the beer is given by
nurses, of course).

›› 8< [beer-talk initiating text]
 
›› 8< [again]
 
›› I did not sy that such a test is forbidden.
› 
…[7 more quoted lines elided]…
› earth at 9.8m/s/s ... yet is *is*.

Some even faster. Ask ESA. Their hardware was not controlled by Cobol.

8< [philosopy]

› Fertiliser.  Please explain how a change in specifications mandated by Someone Of
› Sufficient Authority is a 'design fault'... I say that *no*
› system can be designed with all possible future changes/enhancements in
› mind.
 
› But with more in mind than those had who made some rigid systems I know!
 
›› And then using that data numerically is a design error or an overlooked
›› mistake.
› 
› Fertiliser.  Someone changes the way that things are to be displayed
› and/or interpreted.
 
› Yep. And looked not further than his nose-tip?
 
›  Last week a customer-number containing a letter of
› *any* kind was invalid data, next week a customer-number for a customer of
› certain characteristics which does *not* contain an 'A' as the first
› character is invalid... things change, one must respond.
 
› I repeat:
 
›› One could have tested that. This data has been passed to another
›› system, written/designed by people
›› that were convinced that it was numeric all the time.
 
› [8< pay-check argument. Bosses are all the same]
 
› Since, as previously stated, it is impossible to know all possible changes
› which might be applied to a system then some things *must* be ignored in
…[3 more quoted lines elided]…
› the time it would spend redesigning the cup-holder!

So I recommend: define with pic X unless you have to do arithmetic with it. The need to
change to pic 9 then equals the need to start arithmetic. Use that argument to the check
payer/ the "someone with suff. authority".

8< the rest in which we agreed to test, test and test.

The Cobol Groggy of Beer
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 13)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-03-15T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p15@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap> <gap-0ede5eb7b3-p8@usenetarchives.gap> <gap-0ede5eb7b3-p9@usenetarchives.gap> <gap-0ede5eb7b3-p10@usenetarchives.gap> <gap-0ede5eb7b3-p11@usenetarchives.gap> <gap-0ede5eb7b3-p12@usenetarchives.gap> <gap-0ede5eb7b3-p13@usenetarchives.gap> <gap-0ede5eb7b3-p14@usenetarchives.gap> <gap-0ede5eb7b3-p15@usenetarchives.gap>`

```

Cobol Frog (Huib Klink) wrote:
› 
› doc··.@cl··k.net wrote:
…[24 more quoted lines elided]…
› That's because USAGE DISPLAY is default. And a good PICTURE is not. (defaults come in > free, a programmer has to be paid for)

My error, I should have been more clear... my intention was to point out
the rarity of PICTURE IS versus PIC.

› 
››  Since you make the claim 'it is dangerously easy to
…[3 more quoted lines elided]…
› *Very* frequently. :(

Then you should hang out with a better class of programmer... *if*
they'll have you, of course.

› 
››› I admit: the world does 100% not behave as I like. [I can still :) ]
…[4 more quoted lines elided]…
› But my med. against it was beer! I still want my beer. (No problem if the beer is >given by nurses, of course).

Hmmmm... perhaps this thread should be ended here and taken to
alt.beer.enemas?

[snippage about beerm gravity and philosophy... in some order or other]

› 
›› Fertiliser.  Please explain how a change in specifications mandated by Someone Of
…[4 more quoted lines elided]…
› But with more in mind than those had who made some rigid systems I know!

Last time I looked *everything* was a 'matter of degree'... including
this statement.

› 
››› And then using that data numerically is a design error or an overlooked
…[5 more quoted lines elided]…
› Yep. And looked not further than his nose-tip?

There may be an inverserse relationship involving rising in the
Corporate Hierarchy and the ability to see post-proboscum... perhaps I
can get a PhD.

› 
››  Last week a customer-number containing a letter of
…[8 more quoted lines elided]…
››› that were convinced that it was numeric all the time.

Repeating does not make it so... 'could have guessed' is not often a
system-design standard.

› 
› [8< pay-check argument. Bosses are all the same]
…[8 more quoted lines elided]…
› So I recommend: define with pic X unless you have to do arithmetic with it. The need >to change to pic 9 then equals the need to start arithmetic. Use that argument to the >check payer/ the "someone with suff. authority".

This is how I was taught, I agree... on the other hand there are many
whom I've met with 'suff. authority' who have said 'I don't need that
academic crap and I'm signing the check... do it my way or hit the
highway.' (this is also called 'micromanagement')

›
› 8< the rest in which we agreed to test, test and test.

DD
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 14)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-03-15T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p16@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap> <gap-0ede5eb7b3-p8@usenetarchives.gap> <gap-0ede5eb7b3-p9@usenetarchives.gap> <gap-0ede5eb7b3-p10@usenetarchives.gap> <gap-0ede5eb7b3-p11@usenetarchives.gap> <gap-0ede5eb7b3-p12@usenetarchives.gap> <gap-0ede5eb7b3-p13@usenetarchives.gap> <gap-0ede5eb7b3-p14@usenetarchives.gap> <gap-0ede5eb7b3-p15@usenetarchives.gap> <gap-0ede5eb7b3-p16@usenetarchives.gap>`

```

The Goobers wrote:
(snip)

›››  Since you make the claim 'it is dangerously easy to
››› mis-interpret' I feel the need to ask... have you frequently found
…[5 more quoted lines elided]…
› they'll have you, of course.

Hey, I thought this was comp.lang.cobol; how'd we end up discussing C?

Bill Lynch

(rest snipped)
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 14)_

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-15T19:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p16@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap> <gap-0ede5eb7b3-p8@usenetarchives.gap> <gap-0ede5eb7b3-p9@usenetarchives.gap> <gap-0ede5eb7b3-p10@usenetarchives.gap> <gap-0ede5eb7b3-p11@usenetarchives.gap> <gap-0ede5eb7b3-p12@usenetarchives.gap> <gap-0ede5eb7b3-p13@usenetarchives.gap> <gap-0ede5eb7b3-p14@usenetarchives.gap> <gap-0ede5eb7b3-p15@usenetarchives.gap> <gap-0ede5eb7b3-p16@usenetarchives.gap>`

```

The Goobers wrote:

› Cobol Frog (Huib Klink) wrote:
›› 
…[10 more quoted lines elided]…
›››››› Fact: DISPLAY is a USAGE, it is not the same as PICTURE X.
 
›››› 8<
 
›››› Because of the tiny difference, it is dangerously easy to mis-interpret.
›››› Usage display could be applied to a data-name with a numeric picture
›››› including an embedded sign (S, not SEPARATE). The sign and the first or
›››› last digit are then combined says The Standard.
 
››› 8<
 
›››  Since you make the claim 'it is dangerously easy to
››› mis-interpret' I feel the need to ask... have you frequently found
…[5 more quoted lines elided]…
› they'll have you, of course.

I use to be a trainer of newbie's. :)

8< the rest. I'll drink a beer and talk no more for a while.
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 11)_

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-03-12T19:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p13@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap> <gap-0ede5eb7b3-p8@usenetarchives.gap> <gap-0ede5eb7b3-p9@usenetarchives.gap> <gap-0ede5eb7b3-p10@usenetarchives.gap> <gap-0ede5eb7b3-p11@usenetarchives.gap> <gap-0ede5eb7b3-p12@usenetarchives.gap> <gap-0ede5eb7b3-p13@usenetarchives.gap>`

```

Cobol Frog (Huib Klink) wrote: in relation to numeric testing. "IF
NUMERIC"

› I did not sy that such a test is forbidden. It's a pity that it is needed. One should
› have done something different to avoid it's need. But it is not so, so we test over and
…[5 more quoted lines elided]…
› 
There are other reasons to use the IF NUMERIC test than to determine if
invalid data has entered a field.

Consider this test:

IF ZIP-CODE (1:5) numeric
PERFORM USA-ZIP-ROUTINE
ELSE
PERFORM CANADIAN-ZIP-ROUTINE
END-IF
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 12)_

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-15T19:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p19@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap> <gap-0ede5eb7b3-p8@usenetarchives.gap> <gap-0ede5eb7b3-p9@usenetarchives.gap> <gap-0ede5eb7b3-p10@usenetarchives.gap> <gap-0ede5eb7b3-p11@usenetarchives.gap> <gap-0ede5eb7b3-p12@usenetarchives.gap> <gap-0ede5eb7b3-p13@usenetarchives.gap> <gap-0ede5eb7b3-p19@usenetarchives.gap>`

```

Thane Hubbell wrote:

› Cobol Frog (Huib Klink) wrote: in relation to numeric testing. "IF
› NUMERIC"
 
› 8< some text about numeric needs
 
› There are other reasons to use the IF NUMERIC test than to determine if
› invalid data has entered a field.
…[7 more quoted lines elided]…
› END-IF

Coleur locale. :)

But you're right. All the discussion between DD and me was about numeric validation, not
about numeric testing. Which also is a subtle difference.

The Frog
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 7)_

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1998-03-12T13:36:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p9@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap> <gap-0ede5eb7b3-p7@usenetarchives.gap> <gap-0ede5eb7b3-p8@usenetarchives.gap> <gap-0ede5eb7b3-p9@usenetarchives.gap>`

```

Jim K wrote:
› 
› William M. Klein wrote:
…[10 more quoted lines elided]…
›   How did the standard expect packed fields to be verified?

The standard did not say what they were and could not provide rules for
what would and would not make them valid. In the proposed standard it
says that the implementor says what makes them valid (it still does not
say what they are).

›› And if you think about
›› testing a binary field, you'll realize it can't ever fail.)
›
› Never expected this to happen.

I depends. If the user says it is an unsigned binary some vendors might
say that anything with the sign bit set is not valid (although most
would allow this as a valid positive binary unsigned number). Some
could even say that if it is out of the range of the PICTURE it is not
valid. The rules in the new standard would allow that assumption for
USAGE IS BINARY.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, NCITS J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
don··.@tan··m.com
No clever quotes here
```

###### ↳ ↳ ↳ Re: Newbie Q: validating fields / printing invalid

_(reply depth: 4)_

- **From:** "john l. mindock" <ua-author-6588931@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p6@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p2@usenetarchives.gap> <gap-0ede5eb7b3-p3@usenetarchives.gap> <gap-0ede5eb7b3-p6@usenetarchives.gap>`

```

(Doug Miller) wrote:
› 
› In article <350··.@pcs··e.com>,
…[19 more quoted lines elided]…
›› 
 
› 
›› So I test IN-VALUE for numeric, if it fails I use ERR-FIELD to print
› 
› Nope. You test ERR-FIELD for numeric. If it's not numeric, trying to
› test IN-VALUE will bomb the program. 

This is not quite correct. Just FYI - it used to be (older compliers)
that you couldn't ask about a PIC 9 FIELD and NUMERIC in the same
sentence. With the newer compilers you can.
John
```

#### ↳ Re: Newbie Q: validating fields / printing invalid

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-03-09T19:00:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p23@usenetarchives.gap>`
- **In-Reply-To:** `<35057848.DF066000@pcsinconline.com>`
- **References:** `<35057848.DF066000@pcsinconline.com>`

```

Chris Zappanti wrote:
› Hi,
› 
…[12 more quoted lines elided]…
› Chris Zappanti

Good question, Chris. The way I address this problem is to declare all
numeric input fields something like this:

03 MY-FIELD.
05 MY-FIELD-NUM PIC 9(04).

Then test MY-FIELD for numeric. If it is numeric, then you can safely
reference MY-FIELD-NUM. An even better way is to actually scan the input
field for a numeric value. This allows the user to input a decimal point
and only enter the number of digits needed to specify the value. Here is
a routine called GET-NUM (get number) that works in COBOL 74 or COBOL 85.

******************************************************************
* *
* N U M B E R W O R K A R E A *
* *
******************************************************************
*
01 NUMBER-WORK-AREA.
03 NW-NBR-ERROR-FLAG PIC 9(01).
03 NW-WORK-NBR.
05 NW-WORK-CHAR OCCURS 25 TIMES
INDEXED BY NW-WX
NW-WLIM.
07 NW-WORK-DIGIT PIC 9(01).
03 NW-DEC-PLACES PIC 9(02).
03 NW-BLD-SIGN PIC S9(01).
03 NW-BLD-NBR PIC 9(12)V9(06).
03 NW-BLD-NBR-SPLIT REDEFINES NW-BLD-NBR.
05 NW-BLD-INTEGER PIC 9(12).
05 NW-BLD-DECIMAL PIC V9(06).
88 NW-RESULT-INTEGER VALUE ZERO.
05 NW-BLD-DEC-DIGITS REDEFINES NW-BLD-DECIMAL.
07 NW-BLD-DEC-DIGIT OCCURS 6 TIMES
INDEXED BY NW-BDX
NW-BDLIM
PIC 9(01).
03 NW-EXTRACTED-NBR PIC S9(12)V9(06).

******************************************************************
* *
* G E T N U M B E R *
* *
* Judson D. McClendon *
* Sun Valley Systems *
* 329 37th Court NE *
* Birmingham, AL 35215 *
* 205/853-8440 *
* *
* CONVERTS A NUMBER IN FREE FORMAT DISPLAY FORM: *
* FOR EXAMPLE: *
* *
* "999,999,999,999.999999 " *
* "-999,999,999,999.999999" *
* " -23.61 " *
* " 4" *
* "0 " *
* " .000001 " *
* "0000000000123456789.10-" *
* " " BLANK IS VALID = 0 *
* *
* INTO FIXED NUMERIC FORM: PIC S9(12)V9(06) *
* *
* USAGE: MOVE TO NW-WORK-NBR. *
* PERFORM 003000-GET-NBR. *
* *
* RESULT: NW-NBR-ERROR-FLAG = 0 INPUT IS A VALID NUMBER *
* 1 INPUT NOT A VALID NUMBER *
* *
* IF NW-NBR-ERROR-FLAG = 0 THEN: *
* NW-EXTRACTED-NBR = NUMBER AS: PIC S9(12)V9(06) *
* NW-DEC-PLACES = NUMBER OF DIGITS TO THE RIGHT *
* OF THE DECIMAL POINT (0=NONE) *
* NW-BLD-SIGN = +1 OR -1 AS: PIC S9(01) *
* NW-BLD-INTEGER = INTEGER DIGITS AS: PIC 9(12) *
* NW-BLD-DECIMAL = DECIMAL DIGITS AS: PIC V9(06) *
* *
******************************************************************
*
003000-GET-NBR.
MOVE 0 TO NW-NBR-ERROR-FLAG.
MOVE ZERO TO NW-EXTRACTED-NBR.
MOVE 0 TO NW-DEC-PLACES.
MOVE ZERO TO NW-BLD-NBR.
MOVE +1 TO NW-BLD-SIGN.
SET NW-BDX TO 1.
SET NW-WLIM TO 25.
*
* ** LOCATE LEFTMOST DIGIT OF NUMBER **
*
SET NW-WX TO 1.
SEARCH NW-WORK-CHAR
WHEN NW-WORK-CHAR(NW-WX) NOT = SPACE
PERFORM 003010-DECODE-NBR.
IF (NW-WORK-NBR NOT = SPACES)
MOVE 1 TO NW-NBR-ERROR-FLAG
ELSE
COMPUTE NW-EXTRACTED-NBR = NW-BLD-NBR * NW-BLD-SIGN.
*
* DECODE NUMBER
*
003010-DECODE-NBR.
IF (NW-WORK-CHAR(NW-WX) = "-")
MOVE -1 TO NW-BLD-SIGN
MOVE SPACE TO NW-WORK-CHAR(NW-WX)
SET NW-WX UP BY 1.
PERFORM 003020-GET-INT-PART
UNTIL (NW-WX > NW-WLIM).
SET NW-DEC-PLACES TO NW-BDX.
SUBTRACT 1 FROM NW-DEC-PLACES.
*
* GET INTEGER PART OF NUMBER
*
003020-GET-INT-PART.
IF (NW-WORK-CHAR(NW-WX) NUMERIC)
IF (NW-BLD-INTEGER > 99999999999)
SET NW-WX TO NW-WLIM
ELSE
COMPUTE NW-BLD-INTEGER =
NW-BLD-INTEGER * 10 + NW-WORK-DIGIT(NW-WX)
MOVE SPACE TO NW-WORK-CHAR(NW-WX)
ELSE
IF (NW-WORK-CHAR(NW-WX) = ".")
MOVE SPACES TO NW-WORK-CHAR(NW-WX)
SET NW-WX UP BY 1
PERFORM 003030-GET-DEC-PART
UNTIL (NW-WX > NW-WLIM)
ELSE
IF (NW-WORK-CHAR(NW-WX) = ",")
MOVE SPACE TO NW-WORK-CHAR(NW-WX)
ELSE
SET NW-WX TO NW-WLIM.
SET NW-WX UP BY 1.
*
* GET DECIMAL PART OF NUMBER
*
003030-GET-DEC-PART.
IF (NW-WORK-CHAR(NW-WX) NUMERIC)
IF (NW-BDX > 6)
SET NW-WX TO NW-WLIM
ELSE
MOVE NW-WORK-DIGIT(NW-WX) TO NW-BLD-DEC-DIGIT(NW-BDX)
MOVE SPACES TO NW-WORK-CHAR(NW-WX)
SET NW-BDX UP BY 1
ELSE
IF (NW-WORK-CHAR(NW-WX) = "-")
MOVE -1 TO NW-BLD-SIGN
MOVE SPACE TO NW-WORK-CHAR(NW-WX)
SET NW-WX TO NW-WLIM
ELSE
SET NW-WX TO NW-WLIM.
SET NW-WX UP BY 1.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

##### ↳ ↳ Re: Newbie Q: validating fields / printing invalid

- **From:** "chris zappanti" <ua-author-2615462@usenetarchives.gap>
- **Date:** 1998-03-10T13:24:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ede5eb7b3-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ede5eb7b3-p23@usenetarchives.gap>`
- **References:** `<35057848.DF066000@pcsinconline.com> <gap-0ede5eb7b3-p23@usenetarchives.gap>`

```

Thank you for the fast response! I'm get right into this and see what I
can do.

Will let you know of my success.

Chris Zappanti
zap··.@pcs··e.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
