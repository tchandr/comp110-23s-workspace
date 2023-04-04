def zip(str_list: list[str], int_list: list[int]) -> dict[str,int]:
    output: dict[str,int] = {}
    if len(str_list) != len(int_list):
        return output
    if len(str_list) == 0 or len(int_list) == 0:
        return output
    idx: int = 0
    while idx < len(str_list):
        output[str_list[idx]] = int_list[idx]
        idx += 1
    return output