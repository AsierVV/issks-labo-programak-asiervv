# XOR bidezko fluxu zifraketa


def xor_eragiketa(mezua, gakoa):
    """
    Mezuaren eta gakoaren byte bakoitzen artean
    XOR eragiketa egiten du.
    """

    # Badaezpada luzerak konprobatu
    if len(mezua) != len(gakoa):
        raise ValueError(
            "Mezuak eta gakoak luzera berekoa izan behar dute."
        )

    emaitza = bytearray()

    for i in range(len(mezua)):
        emaitza.append(mezua[i] ^ gakoa[i])

    return bytes(emaitza)


def programa():

    print("================================")
    print("XOR BIDEZKO FLUXU ZIFRAKETA")
    print("================================\n")

    # Mezua eta gakoa irakurri
    mezu_testua = input("Sartu mezua: ")
    gako_testua = input("Sartu gakoa: ")

    # Espazioak kendu XOR egiteko
    mezu_testurik_gabe = mezu_testua.replace(" ", "")

    # Testuak byte-kate bihurtu
    mezua = mezu_testurik_gabe.encode("utf-8")
    gakoa = gako_testua.encode("utf-8")

    # Luzerak egiaztatu
    if len(mezua) != len(gakoa):

        print("\nERROREA:")
        print("Mezuak eta gakoak luzera berekoa izan behar dute.")

        print(f"Mezuaren luzera: {len(mezua)} byte")
        print(f"Gakoaren luzera: {len(gakoa)} byte")

        return

    # XOR bidez zifratu
    kriptograma = xor_eragiketa(
        mezua,
        gakoa
    )

    # XOR bera erabiliz deszifratu
    mezu_deszifratua = xor_eragiketa(
        kriptograma,
        gakoa
    )

    # Deszifratutako mezua testu bihurtu
    mezu_deszifratua_testua = mezu_deszifratua.decode("utf-8")

    print("\n================================")
    print("EMAITZAK")
    print("================================")

    print(f"Jatorrizko mezua: {mezu_testua}")
    print(f"Gakoa: {gako_testua}")
    print(f"Kriptograma: {kriptograma.hex()}")
    print(f"Deszifratutako mezua: {mezu_deszifratua_testua}")

    # Hexadezimalean erakutsi
    print("\nDATUAK HEXADEZIMALEAN:")
    print("----------------------")
    print(f"Jatorrizko mezua: {mezua.hex()}")
    print(f"Gakoa: {gakoa.hex()}")
    print(f"Kriptograma: {kriptograma.hex()}")
    print(f"Deszifratutako mezua: {mezu_deszifratua.hex()}")

    # Egiaztatu
    if mezu_deszifratua == mezua:

        print("\nEgiaztapena: ZUZENA")
        print("Deszifratzeak jatorrizko mezua berreskuratu du.")

    else:

        print("\nEgiaztapena: OKERRA")


programa()
