
from conversor_temperatura import create_default_converter, apply_conversion

def test_conversion():
    print("Teste 1: Convertendo Celsius para Fahrenheit")
    values = [0, 20, 37, 100]
    set_default_unit, convert_temperature = create_default_converter()
    set_default_unit("Celsius")
    results = apply_conversion(convert_temperature, values)
    assert results == [32.0, 68.0, 98.6, 212.0], f"Erro: {results}"

    print("Teste 2: Convertendo Fahrenheit para Celsius")
    values = [32, 68, 98.6, 212]
    set_default_unit, convert_temperature = create_default_converter()
    set_default_unit("Fahrenheit")
    results = apply_conversion(convert_temperature, values)
    assert results == [0.0, 20.0, 37.0, 100.0], f"Erro: {results}"

    print("Todos os testes passaram!")

if __name__ == "__main__":
    test_conversion()
