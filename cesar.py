from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0


# Indar erasoa Cesar-en zifraketaren aurka

mezu_zifratua = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"


def deszifratu_cesar(mezua, desplazamendua):
    emaitza = ""

    for c in mezua:

        # Hizki bat bada
        if c.isalpha():

            # Letra larriak
            if c.isupper():
                hasiera = ord('A')
            else:
                # Letra xeheak
                hasiera = ord('a')

            # Desplazamendua aplikatzen dugu
            hizki_berria = chr(
                (ord(c) - hasiera - desplazamendua) % 26 + hasiera
            )

            emaitza += hizki_berria

        else:
            # Hizkia ez bada, ez da aldatzen
            emaitza += c

    return emaitza


def indar_eraso_cesar(mezu_zifratua):

    print("Indar-erasoa hasi da gakoa bilatzeko.\n")

    # Gako posible guztiak frogatu
    for gakoa in range(26):

        mezu = deszifratu_cesar(mezu_zifratua, gakoa)

        # Hizkuntza automatikoki detektatu
        try:
            hizkuntza = detect(mezu)

            if hizkuntza == "es":
                print(f"Gakoa aurkitu da: {gakoa}")
                print(f"Mezu deszifratua: {mezu}")
                return

        except Exception:
            # Detekzioak huts egiten badu, hurrengo gakoa probatu
            continue

    print("Ezin izan da gakoa automatikoki aurkitu.")


# Mezua
indar_eraso_cesar(mezu_zifratua)
