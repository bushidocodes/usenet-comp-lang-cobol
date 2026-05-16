[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol heck - i'm makjing progress

_6 messages · 3 participants · 2004-07_

---

### cobol heck - i'm makjing progress

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-27T22:00:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wp-dnfX0oOF6uZrcRVn-vg@comcast.com>`

```
I have actally have been making progress.  I have nearly 1200 fields and one
way or another, I have narrowed it down to about 50 that I don;t quite get.
I'm sure that these are simple but could you fill in the blanks.

As you can see I have 2 completed examples, the other 5 are mystery to me.

 The thing is, rather than understand this stuff, I have been using pattern
matching to translate these stinkers.  The empty ones below, I do not quite
have the pattern right.

This rich text file might not post right, so if not I will try again.
 Thanks

      COBOL
     Field_Size
     FieldType
     input_record
     output_record

      S9(1)V
     1
     10



      S9(3)V
     2
     10



      S9(5)V
     3
     10



      S9(7)V
     4
     10
     pack_lowsign * 5
     ascii * pic --------9.99

      S9(9)V
     5
     10



      S9(11)V
     6
     10



      S9(14)V
     8
     10
     pack_lowsign * 8
     ascii * pic --------9.99
```

#### ↳ Re: cobol heck - i'm makjing progress

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-27T22:08:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5oWdncX4_LpIu5rcRVn-oQ@comcast.com>`
- **References:** `<wp-dnfX0oOF6uZrcRVn-vg@comcast.com>`

```
This might be easier to read!
"COBOL" "Field_Size" "FieldType" "input_record" "output_record"
"S9(1)V" 1 10
"S9(11)V" 6 10
"S9(14)V" 8 10 "pack_lowsign * 8" "ascii * pic --------9.99"
"S9(3)V" 2 10
"S9(5)V" 3 10
"S9(7)V" 4 10 "pack_lowsign * 5" "ascii * pic --------9.99"
"S9(9)V" 5 10




"Carol" <kgdg@helkusa.com> wrote in message
news:wp-dnfX0oOF6uZrcRVn-vg@comcast.com...
> I have actally have been making progress.  I have nearly 1200 fields and
one
> way or another, I have narrowed it down to about 50 that I don;t quite
get.
> I'm sure that these are simple but could you fill in the blanks.
>
> As you can see I have 2 completed examples, the other 5 are mystery to me.
>
>  The thing is, rather than understand this stuff, I have been using
pattern
> matching to translate these stinkers.  The empty ones below, I do not
quite
> have the pattern right.
>
…[54 more quoted lines elided]…
>
```

##### ↳ ↳ Re: cobol heck - i'm makjing progress

- **From:** Glenn Someone <dontspamme@whydoyouneedmyaddressspammers.com>
- **Date:** 2004-07-28T02:31:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l3leg09q78j5s5rluctcbrfnri1ohgqpi7@4ax.com>`
- **References:** `<wp-dnfX0oOF6uZrcRVn-vg@comcast.com> <5oWdncX4_LpIu5rcRVn-oQ@comcast.com>`

```
I don't quite understand what you are trying to convey with your notes
here, but I can help a little.

What you are encountering seems to be COMP-3 fields mainly as you
describe here based on comparing the field sizes you list with the
specifications.  Another term for this is "packed decimal" fields.  

Examples (where $ means it's a hex byte):

+3743 =  $03 $74 $3C 
-143 = $14 $3D 
32471 = $32 $47 $1F (this one shouldn't matter too much since you list
signs - the F means no sign is indicated)

The S in the definition means to store the sign, and the V is just an
implied decimal point.

I don't know the rest of your notations (field type onward) so I can't
say too much more because I don't know your expectations with those.

On Tue, 27 Jul 2004 22:08:54 -0600, "Carol" <kgdg@helkusa.com> wrote:

>This might be easier to read!
>"COBOL" "Field_Size" "FieldType" "input_record" "output_record"
…[6 more quoted lines elided]…
>"S9(9)V" 5 10
```

##### ↳ ↳ Re: cobol heck - i'm makjing progress

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-28T09:25:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41077016.64717830@news.optonline.net>`
- **References:** `<wp-dnfX0oOF6uZrcRVn-vg@comcast.com> <5oWdncX4_LpIu5rcRVn-oQ@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote:

>This might be easier to read!
>"COBOL" "Field_Size" "FieldType" "input_record" "output_record"
…[6 more quoted lines elided]…
>"S9(9)V" 5 10

Asterisk means the next word is size. In the output definition, the asterisk
seems out of place.
```

##### ↳ ↳ Re: cobol heck - i'm makjing progress

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-28T09:35:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4107728b.65347019@news.optonline.net>`
- **References:** `<wp-dnfX0oOF6uZrcRVn-vg@comcast.com> <5oWdncX4_LpIu5rcRVn-oQ@comcast.com>`

```
"Carol" <kgdg@helkusa.com> wrote:

>This might be easier to read!
>"COBOL" "Field_Size" "FieldType" "input_record" "output_record"
…[6 more quoted lines elided]…
>"S9(9)V" 5 10

On the input side, the size is ((digits + 1) / 2), rounded up if necessary.Thus,
S9(11) has a size of 6.
```

###### ↳ ↳ ↳ Re: cobol heck - i'm makjing progress

- **From:** "Carol" <kgdg@helkusa.com>
- **Date:** 2004-07-28T07:32:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uaidnetkHIBDN5rcRVn-tQ@comcast.com>`
- **References:** `<wp-dnfX0oOF6uZrcRVn-vg@comcast.com> <5oWdncX4_LpIu5rcRVn-oQ@comcast.com> <4107728b.65347019@news.optonline.net>`

```
thanks that is the formula i need.

"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:4107728b.65347019@news.optonline.net...
> "Carol" <kgdg@helkusa.com> wrote:
>
…[10 more quoted lines elided]…
> On the input side, the size is ((digits + 1) / 2), rounded up if
necessary.Thus,
> S9(11) has a size of 6.
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
