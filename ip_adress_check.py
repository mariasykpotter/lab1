def check_ip(s):
    import re
    out = re.fullmatch("\d(0,3)\.\d(0,3)\.\d(0,3)\.\d(0,3)", s)
    return out is not None


def ip_adress(s):
    lst = s.split(".")
    if len(lst) != 4:
        return False
    for number in lst:
        number = int(number)
        if number < 0 and number > 255:
            return False
    return True


def check_mask_ip(mask, ip):
    s1 = ""
    s2 = ""
    if ip_adress(mask) and ip_adress(ip):
        lst_mask = mask.split(".")
        lst_ip = ip.split(".")
        for i in range(4):
            el3 = int(lst_mask[i]) & int(lst_ip[i])
            s1 += str(el3) + "."
            el4 = int(lst_mask[i]) & ~int(lst_ip[i])
            s2 += str(el4) + "."
    return s1, s2


r1 = input()
r2 = input()
print(check_mask_ip(r1, r2))
