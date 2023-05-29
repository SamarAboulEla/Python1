is_cloudy = False
is_snowy = False
is_sunny = True

if is_cloudy and is_snowy:
    print("It is cloudy & snowy.")
elif is_cloudy or is_snowy:
    print("It is cloudy or snowy.")
else:
    print("It's neither cloudy nor snowy.")
    if not is_sunny:
        print("It's not sunny too")
    else:
        print("It is sunny :)")
