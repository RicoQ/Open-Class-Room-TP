Annee = input("\nenter a Year to verify: ")
if (Annee % 4) != 0:
    print(" --->  ** ", str(Annee), " ** is not a leap year     \# (%4 Test)")
else:
    if (Annee % 100) == 0:
        if (Annee % 400) == 0:
            print(" --->  ** ", str(Annee), " ** is a leap year     \# (%400 Test)")
        else:
            print(" --->  ** ", str(Annee), " ** is not a leap year     \# (%400 Test)")
    else:
        print(" --->  ** ", str(Annee), " ** is a leap year     \# (%100 Test)")

