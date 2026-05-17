[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL in Java Script?

_2 messages · 2 participants · 2016-05 → 2016-07_

---

### COBOL in Java Script?

- **From:** "doctrinsograce" <ua-author-6402540@usenetarchives.gap>
- **Date:** 2016-05-23T12:37:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<755f4f65-a9be-4361-86ec-2ae63ca73e93@googlegroups.com>`

```
http://arstechnica.com/information-technology/2015/08/calling-1959-from-your-web-code-a-cobol-bridge-for-node-js/

Works with Fortran, too.

Now, once they add LISP, APL, FORTH... er um...
```

#### ↳ Re: COBOL in Java Script?

- **From:** "bwtiffin" <ua-author-14501766@usenetarchives.gap>
- **Date:** 2016-07-05T05:43:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cbdc70569a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<755f4f65-a9be-4361-86ec-2ae63ca73e93@googlegroups.com>`
- **References:** `<755f4f65-a9be-4361-86ec-2ae63ca73e93@googlegroups.com>`

```
On Monday, May 23, 2016 at 12:37:54 PM UTC-4, Doc Trins O'Grace wrote:
› http://arstechnica.com/information-technology/2015/08/calling-1959-from-your-web-code-a-cobol-bridge-for-node-js/
›
› Works with Fortran, too.
›
› Now, once they add LISP, APL, FORTH... er um...

LISP - http://open-cobol.sourceforge.net/faq/index.html#can-gnucobol-interface-with-scheme

APL - Well, J really, to avoid the magic keyboard - http://open-cobol.sourceforge.net/faq/index.html#does-gnucobol-interface-with-j

FORTH - http://open-cobol.sourceforge.net/faq/index.html#can-gnucobol-interface-with-forth

Javascript - embedded engine - http://open-cobol.sourceforge.net/faq/index.html#can-gnucobol-use-javascript

Or at a higher level with Seed - http://open-cobol.sourceforge.net/faq/index.html#seed

COBOL can pretty much do anything she puts her mind to: the document listed above has working samples for Haxe, Ada, GRETL, BASIC, Java, Perl, Python, S-Lang, Fortran, Vala/Genie, Tcl/Tk, to name but a few. Internal and/or external integrations, extend or embed. Those demos are usually written with the goal of COBOL as master of all she surveys, but sometimes (like the SWIG examples) COBOL takes on a supporting role. The SWIG entry alone exposes the potential of some 24 different languages calling into COBOL subprograms, all from a single interface definition.

Even a few integrations just for fun, Shakespeare and Piet come to mind. (Piet programs are probably the world's most beautiful programs, but rather esoteric and not much use beyond being a sight to behold). If wants be, you can run Piet images from a COBOL console. Modern computing is awesome.

No need to stop using COBOL while keeping up with the yoots. And maybe just maybe, a little old fashioned COBOL discipline will rub off on the internet generation as they try and teach old dogs new tricks (which are usually old tricks, wrapped in shiny).

Oh, and on the topic, the github repos of Ionică Bizău are well worth a visit now and again, he keeps adding new and useful features to the node-cobol Node.js layer.

Have good, make well
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
