"""
 @Author  : CAgAG
 @Version : 1.0
 @Describe: 随机工具函数
"""
import pathlib
import random


# 随机 RGB 颜色
def get_random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


# 随机数字
def get_random_number():
    return str(random.randint(0, 9))


# 随机小写字母
def get_random_lower_letter():
    return chr(random.randint(97, 122))


# 随机大写字母
def get_random_upper_letter():
    return chr(random.randint(65, 90))


# 随机中文字符
def get_random_chinese():
    head = random.randint(0xb0, 0xf7)
    # 在 head 区号为 55 的那一块最后 5 个汉字是乱码
    body = random.randint(0xa1, 0xf9)
    val = f'{head:x}{body:x}'
    sc = bytes.fromhex(val).decode('gb2312')
    return sc


# 绘制噪点, 创造 count 个噪点
def generate_points(draw, height, width, count=100):
    """
    :param draw: ImageDraw 对象
    :param height: 图像高度
    :param width: 图像宽度
    :param count: 噪点数量
    :return: 绘制噪点
    """
    for _ in range(count):
        xy = (random.randrange(0, width), random.randrange(0, height))
        draw.point(xy, fill=get_random_color())


# 绘制线, 创造 count 条线
def generate_lines(draw, height, width, count=10):
    """
    :param draw: ImageDraw 对象
    :param height: 图像高度
    :param width: 图像宽度
    :param count: 线数量
    :return: 绘制线
    """
    for _ in range(count):
        xy_start = (random.randrange(0, width), random.randrange(0, height))
        xy_end = (random.randrange(0, width), random.randrange(0, height))
        draw.line((xy_start, xy_end), fill=get_random_color())


# 随机数字运算符
def get_random_op():
    return str(random.choice(['+', '-', '*']))


# 计算 a, b 对应 +, -, * 的结果
def compute(a: str, b: str, op: str) -> int:
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    else:
        return int(a) * int(b)


# 当前路径
def file_path():
    return pathlib.Path(__file__).parent
