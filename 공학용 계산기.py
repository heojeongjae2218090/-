# 안전공학 계산기

def calculate_safety_factor(ultimate_stress, working_stress):
    safety_factor = ultimate_stress / working_stress
    return safety_factor

def calculate_allowable_stress(ultimate_stress, safety_factor):
    allowable_stress = ultimate_stress / safety_factor
    return allowable_stress

def calculate_allowable_load(allowable_stress, cross_sectional_area):
    allowable_load = allowable_stress * cross_sectional_area
    return allowable_load

ultimate_stress = float(input("최대 응력을 입력하세요: "))
working_stress = float(input("작동 응력을 입력하세요: "))
cross_sectional_area = float(input("단면적을 입력하세요: "))

safety_factor = calculate_safety_factor(ultimate_stress, working_stress)
print(f"안전률: {safety_factor}")

allowable_stress = calculate_allowable_stress(ultimate_stress, safety_factor)
print(f"허용 응력: {allowable_stress}")

allowable_load = calculate_allowable_load(allowable_stress, cross_sectional_area)
print(f"허용 하중: {allowable_load}")
