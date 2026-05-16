[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress and Form variables

_2 messages · 2 participants · 2001-02_

---

### NetExpress and Form variables

- **From:** mrtonyr@my-deja.com
- **Date:** 2001-02-01T20:22:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95cght$9ec$1@nnrp1.deja.com>`

```
I am having a little trouble with image submit buttons using NetExpress
2.0. I need to use 3 submit buttons to submit one form and be able to
tell which button was used to submit the form. All my resources say
that you can use multiple submit buttons with different value fields
and the cgi program will be passed the value of the button that is
used. It is supposed to work with both submit buttons and input images.
Everything works ok when I use regular buttons. I need to use inputs of
type image because people will be clicking on logos and whenever I do,
I do not get the form value. Here is the code:

        01 IN-FORM IS EXTERNAL-FORM.
            02 IN-SUBMIT        PIC X(3)    IDENTIFIED BY "DLSUBMIT".

        PROCEDURE DIVISION.
            INITIALIZE IN-FORM.
            ACCEPT IN-FORM..
            DISPLAY IN-SUBMIT.
            STOP RUN.

In the html file it looks like this:
     <td> &nbsp <input name=DLSUBMIT type=image value='qif'
           src=../images/download_button.jpg> </td>

The form is being submitted properly because there are other variables
that are being passed. It works fine if I change the above line to read:
     <td> &nbsp <input type=submit name=DLSUBMIT value='qif'></td>

But everything I have read says that either should work. Any
suggestions or is this a NetExpress thing? Is there any way to capture
and display the whole String that the browser sends the program, or are
we stuck with the way NetExpress puts it into the input form?
Thanks,

Tony



Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: NetExpress and Form variables

- **From:** "David Sands" <david.sands@merant.com>
- **Date:** 2001-02-09T16:14:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<961a3m$l5r$1@hyperion.mfltd.co.uk>`
- **References:** `<95cght$9ec$1@nnrp1.deja.com>`

```
Hi Tony,

I don't think that image buttons actually submit a value to the server. It
submits the x and y coords of where the user clicked in the image.

You could try something like:-

        01 IN-FORM IS EXTERNAL-FORM.
            02 IN-SUBMITX        PIC X(10)    IDENTIFIED BY "DLSUBMIT.x".
            02 IN-SUBMITY        PIC X(10)    IDENTIFIED BY "DLSUBMIT.y".

Rgds
David.



<mrtonyr@my-deja.com> wrote in message news:95cght$9ec$1@nnrp1.deja.com...
> I am having a little trouble with image submit buttons using NetExpress
> 2.0. I need to use 3 submit buttons to submit one form and be able to
…[36 more quoted lines elided]…
> http://www.deja.com/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
