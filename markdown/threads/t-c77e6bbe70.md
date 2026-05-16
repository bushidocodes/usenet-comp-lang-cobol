[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Passing parameters

_5 messages · 4 participants · 2005-11_

---

### Passing parameters

- **From:** Alain Reymond <arwebmail@skynet.be>
- **Date:** 2005-11-21T21:31:12+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43822e92$0$31943$ba620e4c@news.skynet.be>`

```
Hello,

I developped (under Micro Focus OCDS) a piece of program. I found a
curious situation to me.
I use a lot of parameters with numerical values. For some reasons, I
choosed to use comp-1 data.

Here is an example of the declaration of a method :

  method-id. "PS-moveto".
  *> Moves the current position (cursor) to the passed position
  *> This function starts a new path if it is called in page-scope,
  *> otherwise it will set the current point and continues with the
  *> current path.
  data division.
  working-storage section.
  1 wss-x pic ---9.99.
  1 wss-y pic ---9.99.
  1 buffer pic x(512).
  linkage section.
  1 x usage comp-1.
  1 y usage comp-1.
  procedure division using x,y.
  if (fp = 0) then
    invoke self "PS-Error" using PS-RuntimeError, z"PSDoc is null."
    exit method
  end-if
  move x to wss-x
  move y to wss-y
  string wss-x " " wss-y " moveto" x"0a" x"00" delimited by size
  into buffer
  invoke self "PS-Printf" using buffer
  move spaces to buffer
  exit method.
  end method "PS-moveto".

In the calling program, I have to declare two variables :
  1 x comp-1.
  1 y comp-1.
and make a call like that :
  move 100 to x
  move 100 to y
  invoke ps "PS-MoveTo" using x, y
to make the called program work properly.

If I try
  invoke ps "PS-MoveTo" using 100, 100
the parameters are passed incorrectly.

The compiler is not able to see that I am passing numbers. It makes the
programs very verbose and less easy to read.

Is there a way to make a call like hereabove ? Some kind of transtype
procedure...
I understand that the called method is declared elsewhere and that the
modules are compiled separetly. But 100 is a numerical value. So, why
can't the system see that the calling program passes a numerical value
to the called program and transtype it to a comp-1 format ?


Regards.

Alain
```

#### ↳ Re: Passing parameters

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-11-21T21:50:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oirgf.564385$1i.512522@pd7tw2no>`
- **In-Reply-To:** `<43822e92$0$31943$ba620e4c@news.skynet.be>`
- **References:** `<43822e92$0$31943$ba620e4c@news.skynet.be>`

```
Alain Reymond wrote:
> Hello,
> 
…[4 more quoted lines elided]…
> 

Alain,

Generally speaking it is 'safer' to use the M/F Pic x(4) comp-5, 
particularly if there is the likelihood you will be invoking an M/F 
support class where they consistently use pic x(4) comp-5. You've 
probably read it but forgotten - M/F stress this point somewhere in the 
on-line help. (Note - any likelihood you go 'off screen' then use pic 
s9(09) comp-5 for x and y co-ordinates).

Another alternative is to 'send' a copyfile parameter list to get 
specifically what you want. I use Dialog Editor and GUIs. Rather than 
follow the M/F examples to 'copy paste' like minded text for controls,
for example I design a Customer-Dialog; I then create a sub-class called 
"dlgCustomer.cbl". (For conveninence in the IDE I get 'groupings' of 
classes : dlg = Dialog, edt = Edit..., file = File etc.). I've extracted 
the control IDs, Level 78s and added my own preferences for properties, 
'readonly', 'disabled' 'entry field length' etc. So these appear in a 
Working-Storage Section as a Table, of text and plain numerics :-

*> Resource Sequence Field
*> ID       Number   Length    A D  R,C F P V    MethodName
*> IIII     SSS      LLL       9,99,9,9,9,9,9,x-------30------
*> ----     ---      ---       - -- - - - - - ----------------

01 ws-a.

*>                        ID   Seq Len X DF R C F P V
*>                        IIII,SSS,LLL,X,NN,N,N,N,N,N,
    *> Entryfields :

    05.
       10 pic x(TL) value "0214,001,004,0,00,2,0,0,0,0,".
       10 pic x(ML) value "EF-PrimeKey".
    05. ETC..

Above looks a bit gibberish-like withhout explanation. I have a method 
which goes through that table and passes each element as a separate set 
of parameters to a template to create Dialogs. Even there I recently 
came unstuck confusing myself between say pic 9(03) and pic x(4) comp-5 
in the Dialog template. I was moving the parameter-block from Linkage to 
the Global area as Dialog-Parmeters, and for numeric parameters as Usage 
display. I had some methods in the Dialog template expecting pic x(4) 
comp-5 ! So although initially I have to pass the parameters from the 
Table as usage display, one method in the template is handling the 
receipt - it makes sense to move item by item from the parameter linkage 
- and taking the 'Len' ( = Length above) :-

Linkage:-

01 Lnk-Parameters. (following is a copyfile)
  05...
  05...
  05 lnk-length pic 9(03).
  05... etc....

Dialog Template - Instance Global data - Dialog-Length pic x(4) comp-5.

so that there are no 'gotchas' :-

move lnk-length to Dialog-Length

So, consistently within my Dialog-template I refer to numerics as pic 
x(4) comp-5, (at least so far as parameters are concerned). And only one 
method, regardles of Dialog, performs this function in the Dialog 
template, for any application.

Just for info, seeing as you refer to x and y co-ordinates, I use a 
technique to set the Mouse on the Default pushbutton PB-OK -

OBJECT. (instance)
OBJECT-STORGE SECTION OR WORKING-STORAGE SECTION.

*> Co-ordinates to point (centre) the Mouse on the Default
*> Pushbutton ( PB-OK)

01 Default-XY.
    05 Default-X                pic x(4) comp-5.
    05 Default-Y                pic x(4) comp-5.

*> Following used to point the Mouse at other controls,
*> specifically a Listbox; as there could be more than one per
*> Dialog instance, the Table allows for four

01 Control-XY occurs 4.
    05 Control-X               pic x(4) comp-5.
    05 Control-Y               pic x(4) comp-5.

Methods in the Dialog Template instance :-
*>--------------------------------------------------------------
Method-id. "zCreatePushbutton".
*>------------------------------------------------------------
78 CancelButtonID                value 2.
78 DefaultButtonID               value 1.
78 ExitButtonID                  value 55.
01 ls-event                      pic x(4) comp-5.

01 n                             pic x(4) comp-5.

invoke self "getObjectFromId"
               using Dialog-ID returning Dialog-Object
move clicked to ls-event

Evaluate true

   when Dialog-ID = DefaultButtonID
        set os-DefaultButton to Dialog-Object
        invoke os-DefaultButton "default"
        invoke os-DefaultButton "setEventto" using
            ls-event, self, "defaultButton "

   when Dialog-ID = CancelButtonID
        invoke Dialog-Object "setEventto" using
            ls-event, self, "CancelDialog "
        move Dialog-MethodName to CancelMethodName

   when Dialog-ID = ExitButtonID   etc.....

End-Evaluate

invoke os-DialogCollection(1) "add" using Dialog-Object
invoke self "zAddMethodRecord"

if      Dialog-ID = DefaultButtonID
         move zeroes to n
         invoke self "zMakeMousePointer" using Dialog-field, n
End-if

End Method "zCreatePushbutton".
*>------------------------------------------------------------
Method-id. "zMakeMousePointer".
*>--------------------------------------------------------------
*> This method stores the co-ordinates for Pushbutton-OK. It can
*> also be used to position the Mouse over other controls as
*> necessary

Local-storage section.
01 x                             pic x(4) comp-5.
01 y                             pic x(4) comp-5.
01 w                             pic x(4) comp-5.
01 h                             pic x(4) comp-5.

Linkage section.
01 lnk-Field                     pic x(4) comp-5.
01 n                             pic x(4) comp-5.

Procedure Division using lnk-Field, n.

invoke os-DialogCollection(1) "at"
        using lnk-Field returning Dialog-Object
invoke Dialog-Object "getRectangle" using x, y, w, h

if    n = zeroes
       compute Default-X    = x + ( w / 2)  *> i.e.,
       compute Default-Y    = y + ( h / 2)  *> Default Pushbutton

else  compute Control-X(n) = x + ( w / 2)
       compute Control-Y(n) = y + ( h / 2)
End-if

End Method "zMakeMousePointer".
*>--------------------------------------------------------------
Method-id. "setFocuswithMouse".
*>--------------------------------------------------------------
*> As necssary, co-ordinates are set for up to four controls,
*> in addition to the Default-Pushbutton. This is ONLY invoked
*> from the Business Logic which is aware of whether or not
*> a particular Control has been created, plus whether or not to
*> 'point' the Mouse at the Control.

*> It is up to the designer to ensure the correct value of n
*> is provided. (Listbox would normally be '1').

*> See method "zmakeMousePointer" for creation

Linkage section.
01 lnk-Field                        pic x(4) comp-5.
01 n                                pic x(4) comp-5.

Procedure Division using lnk-field, n.

    invoke os-DialogCollection(1) "at"
           using lnk-Field returning Dialog-Object
    invoke Dialog-Object "setFocus"
    invoke Mouse "setXY" using self Control-X (n), Control-Y (n)
    invoke super "show"

*> *** see, I'm invoking the M/F support method "setXY", above, so 
comp-5s are an absolute MUST for success.

End Method "setFocuswithMouse".
*>--------------------------------------------------------------

Now I don't think the above is a 'direct' answer to your question, but 
hopefully it gives you some ideas. Use pic x(4) comp-5 for 
compatibility. All I have ever used is pic 9(03)comp-3 and pic x(4) 
comp-5 - haven't used comp-1 in over twenty years !!!

PS: Do you never use the M/F Forum ? Sign up it's free, (one of the few 
things that are :-) ). Your English is excellent, and even if it wasn't, 
Jean (M/F) from Quebec would jump in to assist. Post questions under Net 
Express or University Edition as appropriate.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Passing parameters

- **From:** Alain Reymond <arwebmail@skynet.be>
- **Date:** 2005-11-22T18:09:14+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<438350bb$0$29402$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<oirgf.564385$1i.512522@pd7tw2no>`
- **References:** `<43822e92$0$31943$ba620e4c@news.skynet.be> <oirgf.564385$1i.512522@pd7tw2no>`

```
James J. Gavan a ï¿½crit :
> Alain Reymond wrote:
> 
…[210 more quoted lines elided]…
> Jimmy, Calgary AB

James,

I thank you for your long answer. As William also noticed in his mail,
the pic x(4) comp-5 is valid for integers. The comp-1 is a float.
The code I gave is part of library designed to generate postscript files
(available on Sourceforge under the name pscoblib). The coordinates can
be integer values as well as floating point values. I primitively wanted
to interface it with C procedures (this explains the comp-1 and s9(9)
comp-5 I choosed. Finally, I wrote the methods in plain OO Cobol.

Maybe I can change for some pic S9(m)V9(n).

Regards.

Alain Reymond
```

#### ↳ Re: Passing parameters

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-11-21T22:53:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<odsgf.17548$V%1.4644@fe09.news.easynews.com>`
- **References:** `<43822e92$0$31943$ba620e4c@news.skynet.be>`

```
You *MIGHT* want to look at passing the numeric literals
   BY VALUE

(the default is "by reference" - and if you do that with a literal, don't 
ask me WHAT is supposed to happen).

However, as Jimmy indicates in his post, those are usually binary - not 
floating point.  You could *try* something like

   Call whatever using By Value +1.0E01

but I certainly have never seen that type of code (and your subprogram would 
need to be prepared to receive that type of data)

"Alain Reymond" <arwebmail@skynet.be> wrote in message 
news:43822e92$0$31943$ba620e4c@news.skynet.be...
> Hello,
>
…[60 more quoted lines elided]…
> Alain
```

#### ↳ Re: Passing parameters

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-11-21T18:32:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11o4pohdnmq453@news.supernews.com>`
- **References:** `<43822e92$0$31943$ba620e4c@news.skynet.be>`

```
Alain Reymond wrote:
> Hello,
>
…[55 more quoted lines elided]…
> to the called program and transtype it to a comp-1 format ?

Same reason the compiler can't type it to a COMP-0, COMP-3, COMP-5, DISPLAY, 
or anything else - the compiler doesn't know what format is expected by the 
called program.

Secondly, the compiler passes addresses (when BY REFERENCE), so to 
accommodate your scheme the compiler would have to build a literal pool of 
such parameters and hand off the appropriate address at call time.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
