[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Visual Cobol R4

_6 messages · 4 participants · 2011-08_

---

### Visual Cobol R4

- **From:** Cláudio Miguel Müller <claudiomiguelmuller@gmail.com>
- **Date:** 2011-08-16T05:52:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<076d5cef-478d-4bfc-b69c-ffc1ec41c3bb@glegroupsg2000goo.googlegroups.com>`

```
Hi,
i am from Brazil.

Can i help to develop in Visual Cobol R4 GUI commands?

I already am Cobol programmer caracter.
```

#### ↳ Re: Visual Cobol R4

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-08-17T02:43:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ave13Frp8U1@mid.individual.net>`
- **References:** `<076d5cef-478d-4bfc-b69c-ffc1ec41c3bb@glegroupsg2000goo.googlegroups.com>`

```
Cl�udio Miguel M�ller wrote:
> Hi,
> i am from Brazil.
…[3 more quoted lines elided]…
> I already am Cobol programmer caracter.

Claudio, I realise that English is not your first language, so can we just 
clarify here?

You would like to know if anyone needs help using Micro Focus Visual COBOL 
R4  for .Net, with Windows Forms.

Is this correct? Are you looking for paid contract work or do you just want 
to talk to other people who are using the same tool and environment?

Is it Forms only, or are you using Silverlight, and/or WPF, or Ajax as well? 
Are you using Eclipse or Visual Studio as the IDE?


If the above is wrong, please state in more detail what exactly you are 
using and what exactly you want to do.

Pete.
```

##### ↳ ↳ Re: Visual Cobol R4

- **From:** Cláudio Miguel Müller <claudiomiguelmuller@hotmail.com>
- **Date:** 2011-08-16T08:34:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ec207f6-8a7b-47a1-9df6-ddd7e8f2909e@gz5g2000vbb.googlegroups.com>`
- **References:** `<076d5cef-478d-4bfc-b69c-ffc1ec41c3bb@glegroupsg2000goo.googlegroups.com> <9ave13Frp8U1@mid.individual.net>`

```
Hi Pete,
sorry my english.

I already use Visual Cobol R4 to run simples Cobol programs caracter
display.

But i dont know to use Visual Cobol with Visual Studio IDE.

I dont know to use Windows Forms in Visual Cobol R4 IDE.

I dont find examples and/or tutoriais to create Windows Forms.

Examples in Visual Cobol R4 is not completed or with more details.

Cláudio.

On Aug 16, 11:43 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Cláudio Miguel Müller wrote:
> > Hi,
…[23 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Visual Cobol R4

- **From:** Joe Coleman <colsub@gmail.com>
- **Date:** 2011-08-16T11:07:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4117e8aa-f4b8-4974-9f0e-1ede102e4b50@glegroupsg2000goo.googlegroups.com>`
- **In-Reply-To:** `<9ec207f6-8a7b-47a1-9df6-ddd7e8f2909e@gz5g2000vbb.googlegroups.com>`
- **References:** `<076d5cef-478d-4bfc-b69c-ffc1ec41c3bb@glegroupsg2000goo.googlegroups.com> <9ave13Frp8U1@mid.individual.net> <9ec207f6-8a7b-47a1-9df6-ddd7e8f2909e@gz5g2000vbb.googlegroups.com>`

```
Visual COBOL R3 had a "Samples" folder, which included Visual Studio/.NET examples. It was installed in the Public user folder (Win7). I haven't used R4, so
I don't know if it's different.
```

###### ↳ ↳ ↳ Re: Visual Cobol R4

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-08-17T12:26:08+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9b0g53FuthU1@mid.individual.net>`
- **References:** `<076d5cef-478d-4bfc-b69c-ffc1ec41c3bb@glegroupsg2000goo.googlegroups.com> <9ave13Frp8U1@mid.individual.net> <9ec207f6-8a7b-47a1-9df6-ddd7e8f2909e@gz5g2000vbb.googlegroups.com>`

```
Cl�udio Miguel M�ller wrote:
> Hi Pete,
> sorry my english.

No problem, (it is much better than my Portuguese... :-)) We just need to be 
sure that you are understood.
>
> I already use Visual Cobol R4 to run simples Cobol programs caracter
> display.

OK, these are called "Desktop" or "Console" applications. As opposed to GUI 
(Graphic User Interface) applications.
>
> But i dont know to use Visual Cobol with Visual Studio IDE.

I understand. Visual Studio is pretty huge and it is very powerful. BUT, it 
does make designing and building GUI applications very easy in whatever 
language you are using (including COBOL). You already know COBOL but you 
probably need to invest some time in learning to use Visual Studio. (It's a 
bit like learning to use a chainsaw if you are a lumberjack...)

You can use Visual Studio (VS) to design and build Windows forms by dragging 
and dropping form controls (text boxes, dropdowns, menus, tree views, 
buttons, images, etc. onto the form surface from a toolbox, in VS. VS gives 
you access to all the properties (colour, font, etc.) of each control and 
you can also access these properties from your COBOL. This is all done in a 
part of VS called the "Design Surface" or "Designer". You can see exactly 
what you are building and you can test run it even before you write any 
COBOL. Once you are satisfied with your form the next step is to write the 
event processing in COBOL. Events are "what happens". The user clicks a 
button on your form and a "Click" event is raised. The system vectors 
control to the code you wrote to handle that event. (If you didn't write 
any, the results are disappointing... nothing happens when the button is 
clicked, for example...)

This is a different paradigm from the usual COBOL one where the programmer 
controls the order in which things happen (open file, read data, process 
data, close file...) The GUI environment is event driven and your code must 
respond when events happen. Although this is a little strange at first, it 
is real fun to write and very satisfying when it is finished. VS lets you 
step through the code for each event as it occurs and it isn't too long 
before you are productive.

>
> I dont know to use Windows Forms in Visual Cobol R4 IDE.

No, you need to learn how to use Visual Studio. There are basic videos 
available that will get you started, but the ones I used are in English. You 
probably need to search for tutorial videos in Portuguese.
>
> I dont find examples and/or tutoriais to create Windows Forms.

It is really pretty easy once you master the tools. I strongly recommend 
video as the way to learn. You can pause it and back up if you hit something 
you are not sure about, and there are thousands of free short videos 
available on the Internet. You may not find examples specifically for COBOL, 
but the principles are the same for whatever language you are using.  (The 
Design Surface is language independent and it doesn't matter whether you use 
VB, C#, C++, or COBOL you still build your forms the same way.)

> Examples in Visual Cobol R4 is not completed or with more details.
>

It would be very hard for them to show the non-COBOL part of GUI development 
unless they gave a video or a detailed walkthrough. Get to know VS and what 
you want to do will fall into place.

Good Luck!

Pete.
```

###### ↳ ↳ ↳ Re: Visual Cobol R4

_(reply depth: 4)_

- **From:** Cláudio Miguel Müller <claudiomiguelmuller@hotmail.com>
- **Date:** 2011-08-17T11:43:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<17300d9d-a124-49b3-95c0-f2f90f730741@e35g2000yqc.googlegroups.com>`
- **References:** `<076d5cef-478d-4bfc-b69c-ffc1ec41c3bb@glegroupsg2000goo.googlegroups.com> <9ave13Frp8U1@mid.individual.net> <9ec207f6-8a7b-47a1-9df6-ddd7e8f2909e@gz5g2000vbb.googlegroups.com> <9b0g53FuthU1@mid.individual.net>`

```
On 16 ago, 21:26, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> Cláudio Miguel Müller wrote:
> > Hi Pete,
…[75 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

Hi Pete, thanks for the explanation.

Now so will learn the Visual Studio and then communicate with Cobol.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
