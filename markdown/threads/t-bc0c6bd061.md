[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Error Handling With Intrinsic Functions

_3 messages · 3 participants · 1997-10_

---

### Error Handling With Intrinsic Functions

- **From:** "john calahan" <ua-author-8533050@usenetarchives.gap>
- **Date:** 1997-10-29T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<638udd$afq$0@204.179.92.217>`

```

I was asked about a problem at work today, and not knowing the answer, I
thought I'd put it up for discussion. We're trying to use one of the
date-related intrinsic functions, in this case, INTEGER-OF-DATE, on a
certain date field. The field is in the proper format, but for example's
sake we sent a date value of 19970230 to the function.

Under COBOL/370 in the LE environment, error CEE2805S is generated,
along with a dump and the appropriate message specifying an invalid
date. However, I'd like to have the ability to handle the error myself
so the program doesn't stop at that point, but goes on instead.

Do we have to pre-validate the data passed to these functions, or is
there some return code or status value passed back to the calling
program that we can interpret after the fact? I know a date validation
routine wouldn't be so hard to come up with, but it seems to me that
error handling would mean less coding for us. Any suggestions or ideas?
Thanks for the help.
```

#### ↳ Re: Error Handling With Intrinsic Functions

- **From:** "scom..." <ua-author-2666089@usenetarchives.gap>
- **Date:** 1997-10-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bc0c6bd061-p2@usenetarchives.gap>`
- **In-Reply-To:** `<638udd$afq$0@204.179.92.217>`
- **References:** `<638udd$afq$0@204.179.92.217>`

```

John Calahan writes...

› I was asked about a problem at work today, and not knowing the answer, I
› thought I'd put it up for discussion. We're trying to use one of the
…[15 more quoted lines elided]…
› 


John,

First off, it seems strange to me that you should get an error on that date
(or, like you say, a valid date). How did you define the field you sent to the
service (picture and usage)?

If you know you are sending valid dates you shouldn't have to do any validation
or error correction. So it sounds like you have some bad data there.

As far as detecting and handling errors, this is a natural application for a
condition handler. It's a little complicated to go over in a forum like this
(and besides, teaching this stuff is how I make my living) but you might check
the LE programming guide (SC28-1939
), chapters 16-19 for information on how to code and register a condition
handler.

Regards,


Steve Comstock
Telephone: 303-393-8716
email: SCo··.@a··.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: Error Handling With Intrinsic Functions

- **From:** "colin lucas" <ua-author-7055304@usenetarchives.gap>
- **Date:** 1997-10-30T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bc0c6bd061-p3@usenetarchives.gap>`
- **In-Reply-To:** `<638udd$afq$0@204.179.92.217>`
- **References:** `<638udd$afq$0@204.179.92.217>`

```


John Calahan wrote in message <638udd$afq$0.··.@204··2.217>...
› I was asked about a problem at work today, and not knowing the answer, I
› thought I'd put it up for discussion. We're trying to use one of the
…[15 more quoted lines elided]…
› 

You might want to try the LE callable service CEECBLDY. That returns the
same value as INTEGER-OF-DATE, but has the advantage of not abending if the
date is in the wrong format - instead it returns a non-zero feedback code.

In fact, you should be using CEECBLDY for all your date validation anyway.
It can deal with virtually any format and with 2 or 4 digit years.

Yours faithfully

Colin Lucas
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
