from correios import buscar_cep


def test_buscar_cep_valido():
    cep = "01001-000"
    data = buscar_cep(cep)
    assert data is not None
    assert data["cep"] == cep


def test_buscar_cep_domingos():
    cep = "91420-270"
    data = buscar_cep(cep)
    assert data is not None
    assert data["cep"] == cep


def test_buscar_cep_formato_rubbo():
    cep = "91040-000"
    data = buscar_cep(cep)
    assert data is not None
    assert data["cep"] == cep
