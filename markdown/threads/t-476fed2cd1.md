[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress Dialog System and Setting Tab order

_5 messages · 4 participants · 2000-03_

---

### NetExpress Dialog System and Setting Tab order

- **From:** Aaron Cardon <aaron@amnutrition.com>
- **Date:** 2000-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38D6BA96.A9AF7F43@amnutrition.com>`

```
Does anyone know how to set the tab order in the NetExpress 3.0 Dialog
System?  I need to set a sequential tab order for all of my entry fields
and cannot find where to set the tab order.

Any help is greatly appreciated!

Thank You,
Aaron Cardon
American Nutrition Inc.
```

#### ↳ Re: NetExpress Dialog System and Setting Tab order

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38d6c45f_4@news1.prserv.net>`
- **References:** `<38D6BA96.A9AF7F43@amnutrition.com>`

```
Aaron,

It's kind of cheesey the way they did this, but this is how it works.

1) select the Form / Screenset that you want to re-order controls on.
2) select "Edit" menu-item, then "Controls" sub-item.  This will show
the "Controls List" dialog.
3) click on the item in the list that you want to re-order, then press
the "Select" button.  This selects the item and then enables the
"Insert" button.
4) click on the item in the list that you want to insert the previously
selected item before, then click "Insert".
5) repeat steps 1-4 for every control that you want to re-order.

This is how you re-order controls in Dialog System.  I am using Dialog
System v3.1.00 in the above steps.  Good luck...
```

##### ↳ ↳ Re: NetExpress Dialog System and Setting Tab order

- **From:** Aaron Cardon <aaron@amnutrition.com>
- **Date:** 2000-03-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38D7A07E.EBEDC8A6@amnutrition.com>`
- **References:** `<38D6BA96.A9AF7F43@amnutrition.com> <38d6c45f_4@news1.prserv.net>`

```
You're right, that is a cheesey way of doing it.  However, I am greatful for
the instructions.  I just tried it and it worked fine.  Too bad you can't
prevent some of the read only fields from being tabbed to.

Thanks again for the solution!

Aaron Cardon
American Nutrition Inc.

"Lucas, Todd" wrote:

> Aaron,
>
…[38 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: NetExpress Dialog System and Setting Tab order

- **From:** "Randy Zimmerman" <rzmerant@execpc.com>
- **Date:** 2000-03-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38d7d8cd$0$40645@news.execpc.com>`
- **References:** `<38D6BA96.A9AF7F43@amnutrition.com> <38d6c45f_4@news1.prserv.net> <38D7A07E.EBEDC8A6@amnutrition.com>`

```
You should be able to automatically skip fields by going into the Entry
Field Options and also checking the "autoskip" checkbox.


"Aaron Cardon" <aaron@amnutrition.com> wrote in message
news:38D7A07E.EBEDC8A6@amnutrition.com...
> You're right, that is a cheesey way of doing it.  However, I am greatful
for
> the instructions.  I just tried it and it worked fine.  Too bad you can't
> prevent some of the read only fields from being tabbed to.
…[49 more quoted lines elided]…
>
```

#### ↳ Re: NetExpress Dialog System and Setting Tab order

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38D70001.F3B8E195@home.com>`
- **References:** `<38D6BA96.A9AF7F43@amnutrition.com>`

```


Aaron Cardon wrote:
> 
> Does anyone know how to set the tab order in the NetExpress 3.0 Dialog
…[3 more quoted lines elided]…
> Any help is greatly appreciated!

I don't use Dialog System but when designing in Dialog Editor I can
re-arrange the sequence of tabbing through fields, (I pick up on the
fields in a 'viewer' and move them with the mouse to a different
position(sequence)). Somewhere in the editing part of the D/S menu there
must be a parallel feature. 

Similarly when dynamically creating entryfields, say a 3 x 6 table,
I can generate on line first or column first to give me the tab sequence
I need to move through the table.

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
