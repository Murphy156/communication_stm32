def calculate_parity_bit(data1, data2, data3):
    """
    计算奇偶校验位

    参数:
    data1 (str): 第一个输入数据
    data2 (str): 第二个输入数据
    data3 (str): 第三个输入数据

    返回:
    int: 奇偶校验位（0 或 1）
    """
    # 将三个数据合并成一个字符串
    combined_data = data1 + data2 + data3

    count_ones = sum(int(bit) for bit in combined_data)  # 计算输入数据中的 1 的个数
    parity_bit = count_ones % 2  # 求取奇偶校验位
    return parity_bit


# 示例用法
if __name__ == "__main__":
    data1 = "1010101"
    data2 = "1100110"
    data3 = "1111111"
    # 计算奇偶校验位
    parity_bit = calculate_parity_bit(data1, data2, data3)
    print(f"合并后的数据: {data1}{data2}{data3}")
    print(f"奇偶校验位: {parity_bit}")