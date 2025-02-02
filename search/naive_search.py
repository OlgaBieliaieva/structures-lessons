def naive_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    # Перебір по символах головного рядка
    for i in range(N - M + 1):
        j = 0

        # Перебір по символах підрядка
        while j < M:
            if main_string[i + j] != pattern[j]:
                break
            j += 1

        # Якщо значення j дорівнює довжині підрядка, то підрядок знайдено
        if j == M:
            return i

    return -1

main_string = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
position = naive_search(main_string, pattern)

if position != -1:
    print(f"Підрядок знайдено на позиції {position}")
else:
    print("Підрядок не знайдено в головному рядку.")


# Наївний алгоритм пошуку підрядка має складність O(n×m)O(n×m), 
# де nn — довжина головного рядка, а mm — довжина підрядка. 
# Втім, якщо ми розглядаємо ситуацію, де довжина підрядка MM наближається до довжини головного рядка NN, 
# складність може бути представлена вже як O(n2)O(n2). Це робить алгоритм неефективним для довгих рядків.