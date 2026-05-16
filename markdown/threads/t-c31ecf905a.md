[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# comp3 in perl

_1 message · 1 participant · 1999-03_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### comp3 in perl

- **From:** msodos@eudoramail.com
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cbk89$nbp$1@nnrp1.dejanews.com>`

```
Here is a perl subroutine we use to read comp3 data created in MicroFocus
Cobol in a Sunos/Solaris environment. Unfortunately we do not have one yet to
write a comp3 field.


sub read_comp3
{
    local($value, $decimal) = @_;
    local($str_num, $len, $num, $sign);

    $str_num = unpack("H*", $value);
    $len = length($str_num);
    $num = substr($str_num, 0, $len - 1);
    $sign = substr($str_num, $len - 1, 1);
    $num *= -1 if ($sign eq "d");

    $num /= (10 ** $decimal);
}

It works perfectly

Mike Sodos
mike.sodos@delta-air.com

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
