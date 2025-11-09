def has_duplicates(lst):
    # 利用集合去重后长度对比，判断是否有重复元素
    return len(lst) != len(set(lst))

# 测试示例
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],       # 无重复 → False
        [1, 2, 2, 3],       # 有重复 → True
        [],                 # 空列表 → False
        [5],                # 单个元素 → False
        ["a", "b", "a"]     # 字符串重复 → True
    ]
    for case in test_cases:
        result = has_duplicates(case)
        print(f"列表 {case} 是否有重复元素：{result}")
