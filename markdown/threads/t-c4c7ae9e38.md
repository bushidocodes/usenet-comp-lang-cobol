[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MDI ?

_6 messages · 5 participants · 1999-11_

---

### MDI ?

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991102084431.11231.00001186@ng-fd1.aol.com>`

```
Good Morning,

I am responding to an a RFP and one of the requirements is that the software
must be a MDI style application.  I am not aware of what MDI stands for.  Could
someone help me out ?

Thanks,
Bob Hennessey
```

#### ↳ Re: MDI ?

- **From:** phil@sircs.co.uk (Philip Pike)
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381eec93.1233319@news.easynet.co.uk>`
- **References:** `<19991102084431.11231.00001186@ng-fd1.aol.com>`

```
On 02 Nov 1999 13:44:31 GMT, bob7536@aol.com (Bob7536) wrote:

>Good Morning,
>
…[6 more quoted lines elided]…
>


Bob,

This is some snippets abou MDI forms from the MSDN Library provided
with Visual Studio 6.0, hope this what you mean by MDI


An MDI (multiple-document interface) form is a window that acts as the
background of an application and is the container for forms that have
their MDIChild property set to True.


An application can have only one MDIForm object but manyMDI child
forms. If an MDI child form has menus, the child form's menu bar
automatically replaces the MDIForm object's menu bar when the MDI
child form is active. A minimized MDI child form is displayed as an
icon within the MDIForm.

An MDIForm object can contain only Menu and PictureBox controls and
custom controls that have an Align property. To place other controls
on an MDIForm, you can draw a picture box on the form, and then draw
other controls inside the picture box. You can use the Print method to
display text in a picture box on an MDIForm, but you can't use this
method to display text on the MDIForm itself.

Philip Pike
```

#### ↳ Re: MDI ?

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qrCT3.14954$it.416923@news2.rdc1.on.home.com>`
- **References:** `<19991102084431.11231.00001186@ng-fd1.aol.com>`

```

Bob7536 <bob7536@aol.com> wrote in message
news:19991102084431.11231.00001186@ng-fd1.aol.com...
> Good Morning,
>
> I am responding to an a RFP and one of the requirements is that the
software
> must be a MDI style application.  I am not aware of what MDI stands for.
Could
> someone help me out ?
>
> Thanks,
> Bob Hennessey
>
(M)ultiple (D)ocument (I)nterface

It refers to applications where multiple forms are maintained within the
same container form. If you take a look at MS Word, or Outlook, or just
about anything that Micro$oft publishes then you're looking at an MDI.
```

##### ↳ ↳ Re: MDI ?

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 1999-11-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991102101535.14574.00000182@ng-fd1.aol.com>`
- **References:** `<qrCT3.14954$it.416923@news2.rdc1.on.home.com>`

```
Thanks for the information.

Bob Hennessey
```

###### ↳ ↳ ↳ Re: MDI ?

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3822D707.68B2D60B@IMN.nl>`
- **References:** `<qrCT3.14954$it.416923@news2.rdc1.on.home.com> <19991102101535.14574.00000182@ng-fd1.aol.com>`

```
Bob7536 wrote:
> 
> Thanks for the information.
> 
> Bob Hennessey

Ms Word 2000 is no longer MDI but SDI (single doc. interface).

MS Word '95, '97:
-----------------
When opening a second word doc, a new child window was opened *within* the main
window. You could cascade or tile these child windows of maximize then *within*
the borders of the main window. (The main win could be non-maximized, but I
rarely saw a Word-user which did not maximize the window.)
In the task bar you see only ONE entry.

MS Word 2000:
-------------
When opening a second word doc, a new main window is opened.
In the task bar you see one entry PER open word document.

Got it? :)

Frog
```

###### ↳ ↳ ↳ Re: MDI ?

_(reply depth: 4)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vv2sg$3aq$1@news.cerf.net>`
- **References:** `<qrCT3.14954$it.416923@news2.rdc1.on.home.com> <19991102101535.14574.00000182@ng-fd1.aol.com> <3822D707.68B2D60B@IMN.nl>`

```
The COBOL Frog wrote in message <3822D707.68B2D60B@IMN.nl>...
>Ms Word 2000 is no longer MDI but SDI (single doc. interface).

Interesting point really, Microsoft has stated that they are not encouraging
MDI anymore. The focus is changed from application centric to document
centric.

MDI means that any child window is bound to the originating window of the
application, thus, such an application would for instance only have one
instance on the Windows taskbar, while with and SDI application each
individual window will appear on the windows taskbar. Equally, a minimized
mdi child will rest in peace in its master window, while a minimized SDi
child will rest in windows workspace. Just as you say.

(Sorry if I have repeated something already said, I have partly missed this
thread)

Cheesle
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
