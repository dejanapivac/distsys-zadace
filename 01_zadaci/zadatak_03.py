def f3(l):
    assert isinstance(l, list)
    assert all(isinstance(i, dict) for i in l)
    assert all([bool(i) if len(i.keys()) == 3 else False for i in l])
    cijena = sum([j["cijena"] * j["kolicina"] for j in l])
    artikli = [i["naziv"] for i in l]
    return {"ukupno": {"artikli": artikli, "cijena": cijena}}
    return {}


print(f3([{"cijena": 8, "naziv": "Kruh", "kolicina": 1}, {"cijena": 13, "naziv": "Sok", "kolicina": 2},
          {"cijena": 7, "naziv": "Upaljac", "kolicina": 1}]))
