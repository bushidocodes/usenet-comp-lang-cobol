[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Imaging for Windows and Powercobol

_1 message · 1 participant · 2001-11_

---

### Imaging for Windows and Powercobol

- **From:** "Gianni Spano" <softline2000@tin.it>
- **Date:** 2001-11-08T09:25:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ef306a5975d96d3439e5edcf6d90c2c9.40368@mygate.mailgate.org>`

```
I'm developing an application in Fujitsu Powercobol v6.1 using the Imgedit.ocx
supplied with Windows 2000.
When i put an annotation on the imgedit panel, i would set the
"AnnotationGroup" property using a string (field name) to recognize the
annotation on the panel.
Using Powercobol, the first time i set the string, in the POW-GROUPNAME
parameter the string with the field name appears correctly.
If i put a second annotation on the panel and after i click on the first
annotation to verify its annotation group name, i see in the POW-GROUPNAME only
the first character of the string passed (ex. "C" for "Customer_Name"), without
see the rest of string value.
A friend of mine informed me that there is a bug on Windows 2000 fr Unicode
convertion.
In fact, using the same application on a Win98 machine, there aren't problems.
Also i was trying to build a little Vb Dll to "convert" the string using the
"strConv" function, but the result is the same.
Does anyone know how i can resolve this trouble?
Suggestions and tips are appreciate.

Gianni
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
