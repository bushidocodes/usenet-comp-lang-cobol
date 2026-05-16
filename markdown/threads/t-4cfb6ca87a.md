[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# History of programming

_11 messages · 5 participants · 2009-05_

---

### History of programming

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-05-08T17:23:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<x_idndRflMl5LZnXnZ2dnUVZ_oydnZ2d@earthlink.com>`

```
Example:

"1959 - After losing a bet with L. Ron Hubbard, Grace Hopper and several 
other sadists invent the Capitalization Of Boilerplate Oriented Language 
(COBOL) . Years later, in a misguided and sexist retaliation against Adm. 
Hopper's COBOL work, Ruby conferences frequently feature misogynistic 
material."

http://james-iry.blogspot.com/2009/05/brief-incomplete-and-mostly-wrong.html
```

#### ↳ Re: History of programming

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-05-09T14:18:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76k7giF1cfrc3U1@mid.individual.net>`
- **References:** `<x_idndRflMl5LZnXnZ2dnUVZ_oydnZ2d@earthlink.com>`

```


"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:x_idndRflMl5LZnXnZ2dnUVZ_oydnZ2d@earthlink.com...
> Example:
>
…[7 more quoted lines elided]…
>
LOL!

BTW, if you are still grappling with Cyrillic, I came across some components 
that are free and will do what you want. Check out:

http://www.chilkatsoft.com/refdoc/xChilkatCharset2Ref.html

This is more comprehensive than a similar component I have so I downloaded 
it and tried it from C#. It is excellent. In the example strings they show 
for instantiating the object, a correction is needed for PowerCOBOL or 
Fujitsu NetCOBOL, as follows:

01   CKProgID pic x(16) value "Chilkat.Charset2".    *> examples show this 
as "Chilkat.Charset"...
01   objCKCharset  OBJECT REFERENCE COM.
01   unlock-string  pic x(20) value "This can be anything".

invoke com "CREATE-OBJECT"
           using CKProgID
           returning  objCKCharset
end-invoke
invoke objCKCharset "UnlockComponent"
           using unlock-string
end-invoke

(Remember to reference *COM in the REPOSITORY...)

There is also a string component available from the same outfit:

http://www.chilkatsoft.com/download/CkString.zip

... it also needs a correction for Fujitsu...

01   CKstrProgID pic x(16) value "Chilkat.CKString.1".    *> examples show 
this as "Chilkat.String"...
01   objCKString  OBJECT REFERENCE COM.

invoke com "CREATE-OBJECT"
           using CKstrProgID
           returning  objCKString
end-invoke

(Remember to reference *COM in the REPOSITORY...)

And a very interesting example which uses both of the components here:

http://www.example-code.com/vb/vb6-display-unicode.asp

I think that with these two components you should be able to solve all of 
your language concerns.

Pete.
```

##### ↳ ↳ Re: History of programming

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-05-11T09:01:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MJydnd6EQptdspXXnZ2dnUVZ_jSdnZ2d@earthlink.com>`
- **References:** `<x_idndRflMl5LZnXnZ2dnUVZ_oydnZ2d@earthlink.com> <76k7giF1cfrc3U1@mid.individual.net>`

```
Pete Dashwood wrote:
> "HeyBub" <heybub@NOSPAMgmail.com> wrote in message
> news:x_idndRflMl5LZnXnZ2dnUVZ_oydnZ2d@earthlink.com...
…[60 more quoted lines elided]…
>

Thanks for the pointers.

I still can't figure out how to get Cyrillic characters out of a PowerCOBOL 
text box.

Any other suggestions would be welcome...
```

###### ↳ ↳ ↳ Re: History of programming

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-05-12T11:43:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76rrfsF18inp4U1@mid.individual.net>`
- **References:** `<x_idndRflMl5LZnXnZ2dnUVZ_oydnZ2d@earthlink.com> <76k7giF1cfrc3U1@mid.individual.net> <MJydnd6EQptdspXXnZ2dnUVZ_jSdnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>> "HeyBub" <heybub@NOSPAMgmail.com> wrote in message
…[65 more quoted lines elided]…
> PowerCOBOL text box.

I thought the text box was showing question marks?

Presumably, you have set the font properties of the Text Box to be Cyrillic?

If you have solved that and it now shows correct Cyrillic characters, you 
just need to move the Text property to a Unicode string. (the CKString noted 
above would be ideal as it has methods you can use to convert the string.

It isn't clear exactly what the problem is, Jerry.

Pete.
```

###### ↳ ↳ ↳ Re: History of programming

_(reply depth: 4)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-05-12T09:35:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UuednaCkuee1FJTXnZ2dnUVZ_oOdnZ2d@earthlink.com>`
- **References:** `<x_idndRflMl5LZnXnZ2dnUVZ_oydnZ2d@earthlink.com> <76k7giF1cfrc3U1@mid.individual.net> <MJydnd6EQptdspXXnZ2dnUVZ_jSdnZ2d@earthlink.com> <76rrfsF18inp4U1@mid.individual.net>`

```
Pete Dashwood wrote:
>>
>> Thanks for the pointers.
…[11 more quoted lines elided]…
> convert the string.

The Text Box does show Cyrilic but any movement FROM the Text Box converts 
to question marks. Assuming TXT-BOX is initialized with Cyrillic 
characters...

    MOVE 'TEXT' OF TXT-BOX TO Data-name

results in Data-name containing "3F3F3F..." when I hoped for "C1C2C3..."
```

###### ↳ ↳ ↳ Re: History of programming

_(reply depth: 5)_

- **From:** "Kerry Liles" <kerry.removethisandoneperiod.liles@gmail.com>
- **Date:** 2009-05-12T21:20:04-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gud792$mjr$1@news.motzarella.org>`
- **References:** `<x_idndRflMl5LZnXnZ2dnUVZ_oydnZ2d@earthlink.com> <76k7giF1cfrc3U1@mid.individual.net> <MJydnd6EQptdspXXnZ2dnUVZ_jSdnZ2d@earthlink.com> <76rrfsF18inp4U1@mid.individual.net> <UuednaCkuee1FJTXnZ2dnUVZ_oOdnZ2d@earthlink.com>`

```
"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:UuednaCkuee1FJTXnZ2dnUVZ_oOdnZ2d@earthlink.com...
> Pete Dashwood wrote:
>>>
…[20 more quoted lines elided]…
> results in Data-name containing "3F3F3F..." when I hoped for "C1C2C3..."

Perhaps this is elsewhere in this thread, but just in case: what is the 
picture claus for Data-name and TXT-BOX?
```

###### ↳ ↳ ↳ Re: History of programming

_(reply depth: 6)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-05-13T08:47:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kPGdnYqvXt7tUpfXnZ2dnUVZ_hidnZ2d@earthlink.com>`
- **References:** `<x_idndRflMl5LZnXnZ2dnUVZ_oydnZ2d@earthlink.com> <76k7giF1cfrc3U1@mid.individual.net> <MJydnd6EQptdspXXnZ2dnUVZ_jSdnZ2d@earthlink.com> <76rrfsF18inp4U1@mid.individual.net> <UuednaCkuee1FJTXnZ2dnUVZ_oOdnZ2d@earthlink.com> <gud792$mjr$1@news.motzarella.org>`

```
Kerry Liles wrote:
> "HeyBub" <heybub@NOSPAMgmail.com> wrote in message
> news:UuednaCkuee1FJTXnZ2dnUVZ_oOdnZ2d@earthlink.com...
…[26 more quoted lines elided]…
> the picture claus for Data-name and TXT-BOX?

* 01  Data-name PIC X(20).

* "TEXT-BOX" is a Text box control on the form.
```

###### ↳ ↳ ↳ Re: History of programming

_(reply depth: 7)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2009-05-13T13:00:03-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pcrl055r2v5pokpjserob90djcl81jkhgh@4ax.com>`
- **References:** `<x_idndRflMl5LZnXnZ2dnUVZ_oydnZ2d@earthlink.com> <76k7giF1cfrc3U1@mid.individual.net> <MJydnd6EQptdspXXnZ2dnUVZ_jSdnZ2d@earthlink.com> <76rrfsF18inp4U1@mid.individual.net> <UuednaCkuee1FJTXnZ2dnUVZ_oOdnZ2d@earthlink.com> <gud792$mjr$1@news.motzarella.org> <kPGdnYqvXt7tUpfXnZ2dnUVZ_hidnZ2d@earthlink.com>`

```
On Wed, 13 May 2009 08:47:24 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>Kerry Liles wrote:
>> "HeyBub" <heybub@NOSPAMgmail.com> wrote in message
…[32 more quoted lines elided]…
>
Unless you use Unicode in your program, you may not be able to do what
you want.  I suspect that there are no code points in common for
letters (alphabetics?) in the Cyrilic and Latin code pages.  If you
can get the Cyrilic into the program, you may be able to then do a
custom translation to Latin assuming that there is a correspondence
between a Cyrilic letter and its Latin counterpart.  Play with USAGE
NATIONAL and PIC N(number).
```

###### ↳ ↳ ↳ Re: History of programming

_(reply depth: 8)_

- **From:** "Kerry Liles" <kerry.removethisandoneperiod.liles@gmail.com>
- **Date:** 2009-05-13T13:56:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<guf2vu$2kg$1@news.motzarella.org>`
- **References:** `<x_idndRflMl5LZnXnZ2dnUVZ_oydnZ2d@earthlink.com> <76k7giF1cfrc3U1@mid.individual.net> <MJydnd6EQptdspXXnZ2dnUVZ_jSdnZ2d@earthlink.com> <76rrfsF18inp4U1@mid.individual.net> <UuednaCkuee1FJTXnZ2dnUVZ_oOdnZ2d@earthlink.com> <gud792$mjr$1@news.motzarella.org> <kPGdnYqvXt7tUpfXnZ2dnUVZ_hidnZ2d@earthlink.com> <pcrl055r2v5pokpjserob90djcl81jkhgh@4ax.com>`

```
"Clark F Morris" <cfmpublic@ns.sympatico.ca> wrote in message 
news:pcrl055r2v5pokpjserob90djcl81jkhgh@4ax.com...
> On Wed, 13 May 2009 08:47:24 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
> wrote:
…[42 more quoted lines elided]…
> NATIONAL and PIC N(number).

Although I haven't played around with Unicode in COBOL, that is what I was 
looking for: where is it necessary to use PIC N  (meaning Unicode) rather 
than the usual PIC X

Hopefully someone else with real experience can chime in on this...

cheers
```

###### ↳ ↳ ↳ UTF-* and Cyrillic (was: History of programming

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-13T19:20:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RsJOl.49029$iW4.23855@en-nntp-01.dc1.easynews.com>`
- **References:** `<x_idndRflMl5LZnXnZ2dnUVZ_oydnZ2d@earthlink.com> <76k7giF1cfrc3U1@mid.individual.net> <MJydnd6EQptdspXXnZ2dnUVZ_jSdnZ2d@earthlink.com> <76rrfsF18inp4U1@mid.individual.net> <UuednaCkuee1FJTXnZ2dnUVZ_oOdnZ2d@earthlink.com> <gud792$mjr$1@news.motzarella.org> <kPGdnYqvXt7tUpfXnZ2dnUVZ_hidnZ2d@earthlink.com> <pcrl055r2v5pokpjserob90djcl81jkhgh@4ax.com> <guf2vu$2kg$1@news.motzarella.org>`

```
"Kerry Liles" <kerry.removethisandoneperiod.liles@gmail.com> wrote in message 
news:guf2vu$2kg$1@news.motzarella.org...
> "Clark F Morris" <cfmpublic@ns.sympatico.ca> wrote in message 
> news:pcrl055r2v5pokpjserob90djcl81jkhgh@4ax.com...
>> On Wed, 13 May 2009 08:47:24 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
>> wrote:
>>
<snip>
> Although I haven't played around with Unicode in COBOL, that is what I was 
> looking for: where is it necessary to use PIC N  (meaning Unicode) rather than 
…[4 more quoted lines elided]…
> cheers
Asking why you need PIC N isntead of PIC X for Unicode is sort-of like asking 
why you need PIC 9 instead of PIC X for numerics.  The WHOLE POINT of "PIC N 
Usage National" is to define "larger" character sets (i.e. it carries more 
informaiton).

As it says at,
 http://en.wikipedia.org/wiki/UTF-8

"
UTF-8 encodes each character (code point) in 1 to 4 octets (8-bit bytes), with 
the single octet encoding used only for the 128 US-ASCII characters. See the 
Description section below for details."

If you want to use UTF-8 JUST for ascii characters, then you can probably use 
PIC X.  However, if you want to use it for other alphabets, you need to tell the 
computer that more than one "octet" may be used to represent the data.

See also
 http://www.fileformat.info/info/unicode/block/cyrillic/index.htm
and
http://www.fileformat.info/info/unicode/block/cyrillic/utf8test.htm

For informaiton on the two (not one) "byte" values used for UTF-8 Cyrillic
```

###### ↳ ↳ ↳ Re: History of programming

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-05-13T23:16:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76vofnF1f5imrU1@mid.individual.net>`
- **References:** `<x_idndRflMl5LZnXnZ2dnUVZ_oydnZ2d@earthlink.com> <76k7giF1cfrc3U1@mid.individual.net> <MJydnd6EQptdspXXnZ2dnUVZ_jSdnZ2d@earthlink.com> <76rrfsF18inp4U1@mid.individual.net> <UuednaCkuee1FJTXnZ2dnUVZ_oOdnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>>>
…[21 more quoted lines elided]…
> "C1C2C3..."

Ok, I get it now :-)

I tried some experiments using the PowerCOBOL control and I can't get it to 
work properly in the time I have available for it.

Even selecting "Cyrillic" as the font still gives a string of question marks 
when I paste cyrillic into the box.

If the Text property of the box is wrong, nothing else can ever work. There 
are a couple of functions UTF8-of and UCS2-of  which probably need to be 
applied but I just don't have time at the moment to make this work.

If I were doing it for myself I'd use the CK components and make it web 
based so as to have total control over the Text Box. Failing that you could 
try Fujitsu support... yeah, I know...

Sorry.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
