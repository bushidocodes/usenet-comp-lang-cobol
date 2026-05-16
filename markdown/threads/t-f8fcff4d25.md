[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SCREEN SECTION MENUS and Changing Text Interactively through Menu.

_7 messages · 7 participants · 2000-04 → 2000-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### SCREEN SECTION MENUS and Changing Text Interactively through Menu.

- **From:** "Mark Hanlon" <great_cdn_guy@yahoo.com>
- **Date:** 2000-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qwSI4.35432$m5.669675@news1.rdc2.on.home.com>`

```
Hey Everyone,

Just to be upfront and frank I am a student, so bare that in mind.  I am
working on a simple interactive program using indexed files to add, chage,
query, and delete records.  I am using screen commands to display my menus
and data.  Everythign is working great for adding and quering records, but
unfortunatly I do not have an idea how to edit records using the screen
method.

What I am trying to do is display the original data and then be able to tab
or enter through each record and change it.  Currently when I cycle to ie
the Name field, the data is removed allowing me to reenter the string.  Is
ther a command to allow me to edit the existing text or hit return to keep
the current text.  The code I am using at present in my screen storage is as
follows:

       01  INPUT-SCREEN.
?
           05  LINE  7    COLUMN 30  PIC X(15)  TO WS-LAST-NAME
?
             REVERSE  NO HIGHLIGHT  REQUIRED  AUTO.
?
           05  LINE  7    COLUMN 60  PIC XX     TO WS-INITIALS
?
             REVERSE  NO HIGHLIGHT  REQUIRED  AUTO.
?
           05  LINE 10    COLUMN 40  PIC X(3)   TO WS-LOATION-CODE
?
             REVERSE  NO HIGHLIGHT  REQUIRED  AUTO.
?
           05  LINE 11    COLUMN 40  PIC 99     TO WS-COMISSION-RATE
?
             REVERSE  NO HIGHLIGHT  REQUIRED  AUTO.
?
           05  LINE 12    COLUMN 40  PIC 9(8)   TO WS-SALES-AMOUNT
?
             REVERSE  NO HIGHLIGHT  REQUIRED  AUTO.

All suggestions would be appreciated.

Thanks,

Mark Hanlon
```

#### ↳ Re: SCREEN SECTION MENUS and Changing Text Interactively through Menu.

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F3F653.A0EFCC7D@home.com>`
- **References:** `<qwSI4.35432$m5.669675@news1.rdc2.on.home.com>`

```


Mark Hanlon wrote:
> 
> Hey Everyone,
> 
> Just to be upfront and frank I am a student, so bare that in mind.  I am
> working on a simple interactive program using indexed files to add, chage.......<snip>

Mark,

To save a lot of guessing, which COBOL (plus Version) and O/S - plus
suggest you post complete source code of what you have done - and then
you will get a clearer answer from the group.

Jimmy, Calgary AB
```

#### ↳ Re: SCREEN SECTION MENUS and Changing Text Interactively through Menu.

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 2000-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d1jro$rb7$1@hyperion.mfltd.co.uk>`
- **References:** `<qwSI4.35432$m5.669675@news1.rdc2.on.home.com>`

```
Mark,

If you want your Screen Section initially to contain the values of the WS-
items you will need to change the syntax you are using.

The <blah> TO WS-item syntax just returns the values entered to your
working-storage.
Adding <blah> FROM WS-item will set the values in the screen to the item in
working-storage. Or rather than having both TO and FROM statements you can
have USING which is the combination of both.

Lastly, depending on compiler/vendor you may need to do a DISPLAY prior to
the ACCEPT to get the appropriate values into the screen fields.

I hope this helps.


Mark Hanlon <great_cdn_guy@yahoo.com> wrote in message
news:qwSI4.35432$m5.669675@news1.rdc2.on.home.com...
> Hey Everyone,
>
…[7 more quoted lines elided]…
> What I am trying to do is display the original data and then be able to
tab
> or enter through each record and change it.  Currently when I cycle to ie
> the Name field, the data is removed allowing me to reenter the string.  Is
> ther a command to allow me to edit the existing text or hit return to keep
> the current text.  The code I am using at present in my screen storage is
as
> follows:
>
…[28 more quoted lines elided]…
>
```

#### ↳ Re: SCREEN SECTION MENUS and Changing Text Interactively through Menu.

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d19b4$25ns$1@news.hitter.net>`
- **References:** `<qwSI4.35432$m5.669675@news1.rdc2.on.home.com>`

```
Instead of TO WS-LAST-NAME, use USING WS-LAST-NAME.

Screen items with FROM data-name are display-only.
Screen items with TO data-name are accept-only.
Screen items with USING data-name are both display and accept.
------------------
Rick Smith

Mark Hanlon wrote in message ...
>Hey Everyone,
>
…[11 more quoted lines elided]…
>the current text.  The code I am using at present in my screen storage is
as
>follows:
>
…[28 more quoted lines elided]…
>
```

#### ↳ Re: SCREEN SECTION MENUS and Changing Text Interactively through Menu.

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d1qls$r9g$1@news.igs.net>`
- **References:** `<qwSI4.35432$m5.669675@news1.rdc2.on.home.com>`

```
Change the screen section code to have "from"s as well as "to"s, and that
should fix your problem.  I have changed a line below as and example.

Mark Hanlon wrote in message ...

<snip>

>What I am trying to do is display the original data and then be able to tab
>or enter through each record and change it.  Currently when I cycle to ie
>the Name field, the data is removed allowing me to reenter the string.  Is
>ther a command to allow me to edit the existing text or hit return to keep
>the current text.  The code I am using at present in my screen storage is
as
>follows:
>
>       01  INPUT-SCREEN.
>?
******---> like so:
>           05  LINE  7    COLUMN 30  PIC X(15)
                                  from WS-LAST-NAME
                                 TO WS-LAST-NAME
```

##### ↳ ↳ Re: SCREEN SECTION MENUS and Changing Text Interactively through Menu.

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8enjpn$s69$1@news.inet.tele.dk>`
- **References:** `<qwSI4.35432$m5.669675@news1.rdc2.on.home.com> <8d1qls$r9g$1@news.igs.net>`

```
Or, if your compiler understand my syntax:
           05  Scr-Last-Name.
                07 LINE 7 COLUMN 10 PIC X(19) VALUE "Last Name . . . . :".
                07 LINE 7 COLUMN 30  PIC X(15) Using WS-LAST-NAME.

Begin with a Screen with the key-value (Last-name or initials or whatever).
In this example:
  Display Scr-Last-Name.
  Accept Scr-Last-Name.

Now WS-Last-Name to the FD record and read the record from the file into
your Ws-fields and then:
  Display Scr-the-rest-of-it.
  Accept Scr-the-rest-of-it.

Don't forget to experiment with Foreground-color and Background-color - It's
fun.

Regards
Ib


donald tees skrev i meddelelsen <8d1qls$r9g$1@news.igs.net>...
>Change the screen section code to have "from"s as well as "to"s, and that
>should fix your problem.  I have changed a line below as and example.
…[5 more quoted lines elided]…
>>What I am trying to do is display the original data and then be able to
tab
>>or enter through each record and change it.  Currently when I cycle to ie
>>the Name field, the data is removed allowing me to reenter the string.  Is
…[14 more quoted lines elided]…
>
```

#### ↳ R: SCREEN SECTION MENUS and Changing Text Interactively through Menu.

- **From:** "Daniele Eramo" <pittigghiu@tiscalinet.it>
- **Date:** 2000-05-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8enguh$rm$1@lacerta.tiscalinet.it>`
- **References:** `<qwSI4.35432$m5.669675@news1.rdc2.on.home.com>`

```
Dear Mark,
have you tried to use the "USING" clause in the definition of maps? If you
use that clause the field will be able to receive data from map and to send
data to the map. If you use this clause you will have a big help to edit
data record.

For example:  02  LINE n COLUMN m PIC X(....) USING field-name.

I'm a mainframe COBOL programmer, if you want some helps....I'm here

Daniele from ITALY


Mark Hanlon <great_cdn_guy@yahoo.com> wrote in message
qwSI4.35432$m5.669675@news1.rdc2.on.home.com...
> Hey Everyone,
>
…[7 more quoted lines elided]…
> What I am trying to do is display the original data and then be able to
tab
> or enter through each record and change it.  Currently when I cycle to ie
> the Name field, the data is removed allowing me to reenter the string.  Is
> ther a command to allow me to edit the existing text or hit return to keep
> the current text.  The code I am using at present in my screen storage is
as
> follows:
>
…[28 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
