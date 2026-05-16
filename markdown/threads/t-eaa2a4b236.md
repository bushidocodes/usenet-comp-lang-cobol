[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File Class In OO COBOL

_5 messages · 5 participants · 2000-04_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### File Class In OO COBOL

- **From:** "Westley Lodge Pty Ltd" <wlodge@hotkey.net.au>
- **Date:** 2000-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38f056b3@news.iprimus.com.au>`

```
Hi there all.

Just wondering if it is possible to create a class (FUJITSU COBOL in
particular), with all of the methods and properties to handle file
processing. The idea is rather than having a module for each file I use, I'd
rather have the one class, which I use to initialize an instance for each
file I would use, and use the methods and properties to process the file.

I had a go at it, and I have a property to set the file name. However, I am
not quite sure on how to have the one/single class to handle each filess
DIFFERENT record layout (FD).

Any comments / examples will be greatly appreciated.

Regards

Theo
```

#### ↳ Re: File Class In OO COBOL

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F064A3.109F78E3@zip.com.au>`
- **References:** `<38f056b3@news.iprimus.com.au>`

```
Westley Lodge Pty Ltd wrote:
> 
> Hi there all.
…[16 more quoted lines elided]…
> Theo

Jimmy has a set of routines for this.

If you need to process a series of files you develop a base class and
through inheritance on that base class you specialize the objects to
do what you need.

The other option depending upon your needs is that the file instance
is contained in another object (you have a reference to the file
object inside you class).  This is because the file is not the primary
focus of the object just an incidental method of holding the data.

Could you explain a little of what you are trying to do. This will
give us a clearer picture on how to structure the application.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: File Class In OO COBOL

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F0AABB.C4C7EBE2@home.com>`
- **References:** `<38f056b3@news.iprimus.com.au>`

```


Westley Lodge Pty Ltd wrote:
> 
> Hi there all.
…[15 more quoted lines elided]…
> Theo

Theo,

#1 - Get yourself a copy of Wilson (Will) Price "Elements of OO COBOL".
I don't know if the book has been updated but he issued an addendum for
the file handling you are after. The book is published by
cobolreport.com/objectz.com. The text is NetExpress based - but you can
most certainly adapt if for F/J. Should you have any problems converting
to F/J - consult with Thane Hubbell who is experimenting with F/J OO.

(Just as background, Thane and I have found we can 'swap' F/J and N/E OO
COBOL - I can get a clean compile if I set ISO 2000 directives in N/E -
but it wont work in N/E until I substitute Class is ..... instead of F/J
Repository, plus I need to add a Factory). 

#2 - Check out the recent message I wrote which has a zipfile on OO file
handling - Re: 3-Tier, March 30. Note my code is one class per file -
with research it is probable that you can create one class for ALL files
and use instances. However, this is where I suggest caution. If you get
too clever then the bloody thing can become too complicated - causing
you no small amount of headaches in understandibility and
maintainability.

Good luck !

Jimmy, Calgary AB
```

#### ↳ Re: File Class In OO COBOL

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38fb7d65.29253361@news.cox-internet.com>`
- **References:** `<38f056b3@news.iprimus.com.au>`

```
The "Best" solution I have "Concieved" of is to have one generic file
handling class, and code override methods for each FD in a new
override class.  Still more work than I want to do as well.


On Sun, 09 Apr 2000 10:08:51 GMT, "Westley Lodge Pty Ltd"
<wlodge@hotkey.net.au> wrote:

>Hi there all.
>
…[16 more quoted lines elided]…
>
```

##### ↳ ↳ Re: File Class In OO COBOL

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dg36u$aji$1@news.igs.net>`
- **References:** `<38f056b3@news.iprimus.com.au> <38fb7d65.29253361@news.cox-internet.com>`

```
My tendency would be to have a class for each file, then a superclass that
inherited all files for a system.  Much easier to work with.

As for the problem of multiple record sizes, it should be fairly trivial.
The record buffer is always set to the size of the largest record, and so
should the method argument. The other records are redefinition's of that
record anyway.

I also have a "sub-class" inherited by all file classes.  That particular
class has a method for handling and storing file-id variables, plus the
standard get a file id method that it inherits from the base.  It stores the
file id in a fixed, system wide Isam file, indexed by the filename.

Thane Hubbell wrote in message <38fb7d65.29253361@news.cox-internet.com>...
>The "Best" solution I have "Concieved" of is to have one generic file
>handling class, and code override methods for each FD in a new
…[10 more quoted lines elided]…
>>processing. The idea is rather than having a module for each file I use,
I'd
>>rather have the one class, which I use to initialize an instance for each
>>file I would use, and use the methods and properties to process the file.
>>
>>I had a go at it, and I have a property to set the file name. However, I
am
>>not quite sure on how to have the one/single class to handle each filess
>>DIFFERENT record layout (FD).
…[8 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
