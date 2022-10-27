def f5(tuple_list):
    return [{"id": id, "ime": name, "prezime": surname} for id, name, surname in sorted(tuple_list, key=lambda x: x[0])
            if name[0] == surname[0]]


print(f5([(121, "Ivan", "Ivic"), (431, "Pero", "Horvat"), (31, "Marija", "Maric")]))
# Vraća novu
# sortiranu po id-u (manji->veci) listu dictionary-a o
# studentima kojima ime
# i prezime počinje istim slovom. (One-liner u return-u)
