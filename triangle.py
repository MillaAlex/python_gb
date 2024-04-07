"""Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого 
отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше 
суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является 
ли треугольник разносторонним, равнобедренным или равносторонним."""

side_a = int(input("Enter length of side a: "))
side_b = int(input("Enter length of side b: "))
side_c = int(input("Enter length of side c: "))

if (side_a + side_b > side_c) and (side_c + side_b > side_a) and (side_c + side_a > side_b):
    print("Such a triangle exists.")
    if side_a == side_b and side_b == side_c and side_a == side_c:
        print("The triangle is equal-sided.")
    if side_a == side_b or side_b == side_c or side_a == side_c:
        print("The triangle is isosceles.")
    else:
        print("The triangle is multifaceted.")
else:
    print("Such a triangle does not exist.")
