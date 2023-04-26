def dec_to_hex(decimal):
    """
    10진수를 16진수로 변환하는 함수입니다.
    :param decimal: 10진수 값
    :return: 16진수 값
    """
    hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex_str = ''
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hex_str = str(remainder) + hex_str
        else:
            hex_str = hex_map[remainder] + hex_str
        decimal //= 16
    return hex_str