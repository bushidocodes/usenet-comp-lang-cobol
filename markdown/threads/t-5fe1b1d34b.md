[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Combining data vs String

_2 messages · 2 participants · 2000-06_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Combining data vs String

- **From:** Charles Hammond <ceh1@cec.wustl.edu>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.SOL.3.96.1000605160551.29446A-100000@ritz.cec.wustl.edu>`

```
Here is another idea....	

try using 	

"INSPECT FUNCTION REVERSE(VARIABLE-1) 
TALLYING COUNTER FOR LEADING SPACES.
MOVE VARIABLE-1 (1:(VAR-LENGTH - CTR)) TO NEW-VARIABLE."	

this is more difficult but it ignores inbedded spaces using a second
counter can keep keep track of your current location.  Face it most data
does have spaces in it eventually. Especially names and locations.

suggest you look at the right justify section of the FAQ.	  

Charles Hammond, BSIM Undergraduate Program
```

#### ↳ Re: Combining data vs String

- **From:** Jeff Farkas <taxberjef@naspam.naxs.net>
- **Date:** 2000-06-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.13a794742f7501c49896a2@news.naxs.com>`
- **References:** `<Pine.SOL.3.96.1000605160551.29446A-100000@ritz.cec.wustl.edu>`

```
Charles Hammond wrote:
I am sure this is not what most folks have in mind but.. shit it is just about 
midnight and I thought what the hell!!:-)
> Here is another idea....	
> 
…[4 more quoted lines elided]…
> MOVE VARIABLE-1 (1:(VAR-LENGTH - CTR)) TO NEW-VARIABLE."	

Interesting...

> 
> this is more difficult but it ignores inbedded spaces using a second
> counter can keep keep track of your current location.  Face it most data
> does have spaces in it eventually. Especially names and locations.

Okay... lets look at an example..

pic x(20) value "first  last".

So, I have several emended spaces in between first and last. If I just start my 
counter at 20 and keep reducing it by one until I locate a non space item(IE "t") I 
stop counting down. In my example I would move data from position 1 thru 11 to any 
field. 

All I would use is a little loop and determine the end position of the string and I 
can move it to anywhere I like. I know it is not very slick but it does work. And I 
guess that is what matters? HUH???:-)

I know that my logic is a bit flawed and the way I present is is not as good as most 
but guess what?? The code I would write works very well!!:-)

> suggest you look at the right justify section of the FAQ.	  
Let's not and just say we did. Okay????
> 
> Charles Hammond, BSIM Undergraduate Program
> 
> 
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
