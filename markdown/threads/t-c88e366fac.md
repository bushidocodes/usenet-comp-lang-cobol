[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Get postion of mouse click on Bitmap using repeat group

_10 messages · 6 participants · 2006-09 → 2006-10_

---

### Get postion of mouse click on Bitmap using repeat group

- **From:** "JJ" <jjaukema@gmail.com>
- **Date:** 2006-09-29T13:25:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1159561545.566014.157520@i42g2000cwa.googlegroups.com>`

```
We are using a Flexus SP2 panel with a Bitmap.

We need identify the exact area of the bitmap that was clicked on.  We
created a repeat group which we want to overlay on the picture with a
transparent field.

How do we make the fields in the repeat group transparent and still
have program response to a mouse click on the field.  The bitmap must
be visible but the field in the repeat group should be transparent.

Has anyone done this or something like it?

Thanks, John
```

#### ↳ Re: Get postion of mouse click on Bitmap using repeat group

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-10-02T19:54:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B7eUg.82867$1T2.16466@pd7urf2no>`
- **In-Reply-To:** `<1159561545.566014.157520@i42g2000cwa.googlegroups.com>`
- **References:** `<1159561545.566014.157520@i42g2000cwa.googlegroups.com>`

```
JJ wrote:
> We are using a Flexus SP2 panel with a Bitmap.
> 
…[11 more quoted lines elided]…
> 
I would contact Bob Wolfe at Flexus on this one, outlining exactly what 
it is you want to achieve.

I don't use SP2, but subject to what you want to do, there maybe a 
simpler way than what you have outlined. To jog your memory - have you 
seen screenshots of Borland products where they use pushbuttons with 
bitmaps ? :-

PB-OK = green tick/check-mark followed by 'OK'
PB-Cancel = red diagonal cross followed by 'Cancel' etc....

The above two examples contain both text and bitmap

Having got the w(width) and h(height) of your bitmap file image you can 
create a pushbutton, square or rectangular, that your bitmap will fit into.

invoke Pushbutton "new" using x,y,w,h returning myBitmapButtonObject;
OK in SP2 you will be doing a COBOL CALL with the parameters.

In Net Express, having created the pushbutton I can tell it the button 
is to contain a bitmap image :-

invoke myBitmapButtonObject "bitmap"

If you only want to identify the whole pushbutton area (containing just 
a bitmap), then you shouldn't be worried about the 'area' covered - a 
typical mouse click on a pushbutton will return the 'button-click' event.

If however you want the bitmap to contain labels that can be clicked on 
then it is a slightly different story - but you've indicated you want 
'transparent background' - which implies you were looking for a dummy 
area, (without text), to click on within the bitmap.

You might find the following from an old "T-Y-Delphi" of interest :-

"Bitbuttons are not the answer if you are looking for a way to place 
text cues on top of an image so that you can click one to get more 
detail. For example. if you wanted to show a picture of a piece of 
machinery with annotations identifying individual parts, and enable the 
user to click on an annotation to bring up further information, you need 
to use a regular image component, and place individual label components 
on top of it. You would set the labels' Transparent property to TRUE, 
and use the labels OnClick event, just as you would for a button".

Jimmy, Calgary AB
```

#### ↳ Re: Get postion of mouse click on Bitmap using repeat group

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-10-03T13:08:36+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4odo06Fdto50U1@individual.net>`
- **References:** `<1159561545.566014.157520@i42g2000cwa.googlegroups.com>`

```

"JJ" <jjaukema@gmail.com> wrote in message 
news:1159561545.566014.157520@i42g2000cwa.googlegroups.com...
> We are using a Flexus SP2 panel with a Bitmap.
>
…[11 more quoted lines elided]…
>
You can set 'hotspots' on an existing bitmap using JavaScript. (Many web 
sites implement this; click on a map, for example). It is a simple process 
with the hotspot being reported by the click event. Trying to overlay input 
fields on a bitmap using layers is a very difficult way to approach this.

I don't think it is an SP2 problem (SP2 is just a vehicle that allows the 
bitmap to be on a panel.)  I'm not facile with SP2 so I don't know if a 
panel can have embedded, or suport calls to, script, but Bob Wolfe should be 
able to advise.

In effect, you need a 'smart' bitmap that can report where it was clicked. 
Sounds like a case for ...Super Applet! :-)  Maybe the SP2 panel can act as 
a container for a Java Applet? If, instead of loading a simple bitmap onto 
the panel, you could load something that looked like a simple bitmap but 
was, in fact, a 'smart' bitmap, you are home and dry.

In OO terms, the 'smart' bitmap is an object embedded in the SP2 panel. The 
properties of this object indicate which hotspot was clicked. These can be 
accessed from COBOL like any other object properties.

The fun bit would be building the object, defining it's properties, methods, 
and events, and wrapping it so that SP2 can accommodate it. I would use an 
ActiveX/COM/OLE container (but I'm biased...:-)). I'd be surprised if SP2 
won't accommodate an OLE object, but if it won't, then I'd replace the SP2 
panel with something more amenable...

Good luck.

Pete.
```

##### ↳ ↳ Re: Get postion of mouse click on Bitmap using repeat group

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-10-02T17:45:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1159836311.762261.287550@m73g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<4odo06Fdto50U1@individual.net>`
- **References:** `<1159561545.566014.157520@i42g2000cwa.googlegroups.com> <4odo06Fdto50U1@individual.net>`

```

Pete Dashwood wrote:

> I would use an
> ActiveX/COM/OLE container (but I'm biased...:-)). I'd be surprised if SP2
> won't accommodate an OLE object, but if it won't, then I'd replace the SP2
> panel with something more amenable...


>From the Flexus website:

"""COBOL sp2's Support for Highly Advanced Embedded Controls

COBOL sp2's Active X Control support can also be used to invoke and
control just about any type of Active X Control available.  This gives
you the capability to add additional 3rd party controls to
significantly enhance and modernize your application.  Just a few
examples of the types of controls which you can add include: ...."""
```

###### ↳ ↳ ↳ Re: Get postion of mouse click on Bitmap using repeat group

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-10-04T14:49:26+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ogi99FedpepU1@individual.net>`
- **References:** `<1159561545.566014.157520@i42g2000cwa.googlegroups.com> <4odo06Fdto50U1@individual.net> <1159836311.762261.287550@m73g2000cwd.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1159836311.762261.287550@m73g2000cwd.googlegroups.com...
>
> Pete Dashwood wrote:
…[17 more quoted lines elided]…
>
Excellent! I always thought it was a good tool; this just reinforces that 
opinion. :-)

Pete.
```

##### ↳ ↳ Re: Get postion of mouse click on Bitmap using repeat group

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-10-04T13:50:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s_OUg.12089$N4.7510@clgrps12>`
- **References:** `<1159561545.566014.157520@i42g2000cwa.googlegroups.com> <4odo06Fdto50U1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:4odo06Fdto50U1@individual.net...
>
> "JJ" <jjaukema@gmail.com> wrote in message 
…[19 more quoted lines elided]…
> this.

    I don't know what SP2 is, but if this is going to be for a website, you 
should also consider the imagemap HTML tag. (There's a tutorial at 
http://www.ihip.com/ but you can google "imagemap" to find plenty more).

    - Oliver
```

###### ↳ ↳ ↳ Re: Get postion of mouse click on Bitmap using repeat group

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-10-04T16:16:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k7RUg.93906$R63.61921@pd7urf1no>`
- **In-Reply-To:** `<s_OUg.12089$N4.7510@clgrps12>`
- **References:** `<1159561545.566014.157520@i42g2000cwa.googlegroups.com> <4odo06Fdto50U1@individual.net> <s_OUg.12089$N4.7510@clgrps12>`

```
Oliver Wong wrote:
> 
>     I don't know what SP2 is, but if this is going to be for a website, you 
> should also consider the imagemap HTML tag. (There's a tutorial at 
> http://www.ihip.com/ but you can google "imagemap" to find plenty more).

Briefly, the underlying code of SP2 is written in C, (same as Norcomm's 
Screen I-O). The objective was to relieve COBOL programmers of the 
necessity of becoming whiz-kids on GUI-ing and allow them to code in 
standard Procedural code. I'm not at all familiar with the tool, and no 
doubt it has a 'visual' dialog designer. It is compatible with (most ?) 
COBOL compilers, using traditional procedural coding.

Using COBOL Working-storage for different controls you pass (CALL) SP2 
with a series of parameters - it doesn't return object references to the 
COBOL program - so I guess it returns an ID per object. The implications 
of webbing - you would have to check the product out.

It can be used in both DOS (text) mode and Windows GUI-ing. There's more 
to it than I've indicated - go to flexus.com if you want an overview.

Jimmy
```

###### ↳ ↳ ↳ Re: Get postion of mouse click on Bitmap using repeat group

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2006-10-05T12:59:32+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4oj077FeqclbU1@individual.net>`
- **References:** `<1159561545.566014.157520@i42g2000cwa.googlegroups.com> <4odo06Fdto50U1@individual.net> <s_OUg.12089$N4.7510@clgrps12>`

```

"Oliver Wong" <owong@castortech.com> wrote in message 
news:s_OUg.12089$N4.7510@clgrps12...
>
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
…[29 more quoted lines elided]…
>
As it is on an SP2 panel this is probably a desktop (rather than web based) 
application, Oliver.

This means the presence of a Browser cannot be assumed...

There is no reason why it couldn't be implemented through a Java applet or 
Javascript wrapper around the HTML facility (this would need to run as a 
Windows Script, given you cannot rely on the Browser being there), provided 
this is then wrapped in a way that it can be embedded in the SP2 panel. I 
would do it as either a Java Bean/applet or as an ActiveX/OLE/COM component. 
But that's just me... :-)

What you DON'T want to do is start trying to get click events from an 
overlaid map in a layer of a bitmap, just because this can be stored in a 
COBOL array (if you can ever get it to work...).

I guess it would be feasible to simply use the Windows API and detect the 
mouse co-ordinates, then calculate these relative to the containing window 
frame, and check that against an array of pre-determined co-ordinate ranges, 
but you'd still need to get the click event, and you'd certainly want to 
encapsulate this rather inelegant functionality. It's a pretty inflexible 
solution, when a flexible one is readily available.

Pete.
```

###### ↳ ↳ ↳ Re: Get postion of mouse click on Bitmap using repeat group

_(reply depth: 4)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2006-10-11T13:59:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j1spi2tkk7rq3m28lr3q3v136rjjeirtfi@4ax.com>`
- **References:** `<1159561545.566014.157520@i42g2000cwa.googlegroups.com> <4odo06Fdto50U1@individual.net> <s_OUg.12089$N4.7510@clgrps12> <4oj077FeqclbU1@individual.net>`

```
Hi, Pete et. al.!

Sorry for my top-post and my late-as-usual reply.

We've been working with John and showed him how to identify the
specific area of the bitmap which was clicked upon.  There are
actually several ways to do this in sp2.

Richard's suggestion of using embedded Active X control in sp2 was
also an excellent alternative as well.

Regarding a web interface using sp2, we have supported this for many
years now with our Web Client product.  The beauty of the Flexus Web
Client is that it allows you to continue using the same COBOL sp2 CALL
USING programming interface.  Your existing COBOL sp2 panels are also
used as well.  We generate HTML/Javascript files from the sp2 panel
definitions (screens).  When the COBOL application on the server CALLs
sp2 to display a screen, the Web Client merges the data into the web
page form fields and sends it to the web server for transmission to
the connected client.

Web Client returns any user response back to the COBOL program in the
same fashion allowing an sp2 programmer to implement a web browser
user interface without changing their code or screen defintions.
There are some advanced controls supported by sp2 which are not
supported in an HTML/Javascript user interface, but they are few in
number.  We even support menu bar processing, repeat groups and other
advanced sp2 controls by generating the Javascript to manage them.

The best part is that Web Client provides a persistent connection
between the web browser and application.

Our philosophy is and always has been to provide tools which a COBOL
programmer can use regardless of COBOL compiler or environment.....and
without having to re-write their application for the new environment.

One comment on DOS......we really don't suppot MS-DOS anymore as our
customers have pretty much abandoned its usage.  We do continue to
support UNIX and Linux character mode screens as well as Linux and
UNIX servers with our GUI Thin Client and Web Client procducts.

Again, sorry for the late reply.  I've been lax in accessing the
newsgroup lately (been busy watching LOTR to see Pete's beautiful
county!!  ;-)  )

I do appreciate all of you referring John back to me.  Thanks!



"Pete Dashwood" <dashwood@enternet.co.nz> wrote:

>
>"Oliver Wong" <owong@castortech.com> wrote in message 
…[57 more quoted lines elided]…
>


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Get postion of mouse click on Bitmap using repeat group

_(reply depth: 5)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2006-10-11T18:19:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l2dqi2pcc4scvbi4he9b903nkbdso0b4jl@4ax.com>`
- **References:** `<1159561545.566014.157520@i42g2000cwa.googlegroups.com> <4odo06Fdto50U1@individual.net> <s_OUg.12089$N4.7510@clgrps12> <4oj077FeqclbU1@individual.net> <j1spi2tkk7rq3m28lr3q3v136rjjeirtfi@4ax.com>`

```
Uh Oh...I realized that I gave Richard credit for the Active X
suggestion, but it was Pete who suggested it.  My apologies!!

Richard did indeed confirm that we do offer embedded Active X control
support and, yes, that also includes OLE objects as well as OLE
Automation so that a COBOL application can launch, populate and
control a Microsoft Office application such as Microsoft Word or
Microsoft Excel.

Again....apologies for my mistake.




Bob Wolfe <rtwolfe@flexus.com> wrote:

>Hi, Pete et. al.!
>
…[114 more quoted lines elided]…
>Check out The Flexus COBOL Page at http://www.flexus.com


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
