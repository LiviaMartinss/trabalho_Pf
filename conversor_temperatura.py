celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
fahrenheit_to_celsius = lambda f: (f - 32) * 5/9

def apply_conversion(conversion_function, values):
    return [conversion_function(v) for v in values]

def create_default_converter():
    default_unit = "Celsius" 
    
    def set_default_unit(unit):
        nonlocal default_unit
        default_unit = unit
    
    def convert_temperature(temp):
        if default_unit == "Fahrenheit":
            return fahrenheit_to_celsius(temp) 
        else:
            return celsius_to_fahrenheit(temp)
        
    return set_default_unit, convert_temperature


def get_user_input():
    unit = input("Escolha a unidade de entrada (Celsius ou Fahrenheit): ").strip().capitalize()
    if unit not in ["Celsius", "Fahrenheit"]:
        print("Unidade inválida. Usando Celsius como padrão.")
        unit = "Celsius"
    
    values = input("Digite os valores separados por vírgula (exemplo: 0,20,37,100): ").strip()
    try:
        values_list = list(map(float, values.split(',')))
    except ValueError:
        print("Valores inválidos. Usando lista padrão.")
        values_list = [0, 20, 37, 100]
    
    return unit, values_list

if __name__ == "__main__":
  
    unit, values_list = get_user_input()
    set_default_unit, convert_temperature = create_default_converter()
    set_default_unit(unit)
    converted_values = apply_conversion(convert_temperature, values_list)
    
    print(f"Valores convertidos ({unit} para {'Celsius' if unit == 'Fahrenheit' else 'Fahrenheit'}):", converted_values)

