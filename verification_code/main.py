"""
 @Author  : CAgAG
 @Version : 1.0
 @Describe: 生成验证码
"""
import random
# pip3 install pillow
from PIL import Image, ImageDraw, ImageFont

from .utils import get_random_color, get_random_number, get_random_lower_letter, get_random_upper_letter, \
    get_random_chinese, get_random_op, generate_points, generate_lines, compute, file_path


# 普通输入型验证码
def verification_code(number=True, lower_letter=True, upper_letter=True, chinese=False,
                      save_path='./test.png',
                      width=200, height=50, count=4,
                      difficult='medium') -> str:
    """
    :param number: 是否包含数字
    :param lower_letter: 是否包含小写字母
    :param upper_letter: 是否包含大写字母
    :param chinese: 是否包含中文
    :param save_path: 验证码图片保存路径
    :param width: 验证码图片宽度
    :param height: 验证码图片高度
    :param count: 验证码字数
    :param difficult: 验证码图识别难度, 包括 simple, medium, hard, 对应 简单, 普通, 困难
    :return: 生成验证码图片到指定目录, 同时返回答案
    """
    # 定义背景颜色
    background_color = get_random_color()
    # 创建画布对象
    image = Image.new('RGB', (width, height), background_color)
    # 创建画笔对象
    draw = ImageDraw.Draw(image)
    # 背景颜色干扰
    bg_section = 40
    # 绘制噪点和干扰线
    if difficult == 'medium':
        generate_points(draw, height, width)
        generate_lines(draw, height, width)
    elif difficult == 'simple':
        generate_points(draw, height, width, count=50)
        generate_lines(draw, height, width, count=5)
        bg_section *= 2
    else:
        generate_points(draw, height, width, count=200)
        generate_lines(draw, height, width, count=20)
        bg_section //= 4

    # 验证码字符
    ans = ""
    # 用draw.text书写文字
    average_width = width // count
    for i in range(count):
        text_height = random.randint(int((height - 10) * 0.6), height - 10)
        random_list = []
        if number:
            random_list.append(get_random_number())
        if lower_letter:
            random_list.append(get_random_lower_letter())
        if upper_letter:
            random_list.append(get_random_upper_letter())
        if chinese:
            random_list.append(get_random_chinese())
        assert random_list, '必须有一种模式为True, number, lower_letter, upper_letter, chinese'

        rand_chr = random.choice(random_list)
        ans += rand_chr
        color = get_random_color()
        text_color = [0, 0, 0]
        # 背景颜色是否影响字符
        for j in range(2):
            if color[j] - background_color[j] <= bg_section:
                text_color[j] = 255 - color[j]
            else:
                text_color[j] = color[j]
        # 绘制文字
        draw.text((i * average_width + 10, 0),
                  rand_chr,
                  tuple(text_color),
                  font=ImageFont.truetype(f'{file_path()}/Fronts/SourceHanSerifSC/SourceHanSerifSC-Regular.ttf', text_height),
                  align='center')
    # 释放画笔
    del draw
    # 将图片保存在本地中，文件类型为png
    image.save(save_path, 'png')
    return ans


# 计算型验证码, + - *
# 为了避免整数与小数的歧义, 不包含除法
def verification_code_compute(save_path='./test.png',
                              width=200, height=50,
                              difficult='medium') -> str:
    """
    :param save_path: 验证码图片保存路径
    :param width: 验证码图片宽度
    :param height: 验证码图片高度
    :param difficult: 验证码图识别难度, 包括 simple, medium, hard, 对应 简单, 普通, 困难
    :return: 生成验证码图片到指定目录, 同时返回答案
    """
    # 字符数
    count = 4
    # 定义背景颜色
    background_color = get_random_color()
    # 创建画布对象
    image = Image.new('RGB', (width, height), background_color)
    # 创建画笔对象
    draw = ImageDraw.Draw(image)
    # 背景颜色干扰
    bg_section = 40
    # 绘制噪点和干扰线
    if difficult == 'medium':
        generate_points(draw, height, width)
        generate_lines(draw, height, width)
    elif difficult == 'simple':
        generate_points(draw, height, width, count=50)
        generate_lines(draw, height, width, count=5)
        bg_section *= 2
    else:
        generate_points(draw, height, width, count=200)
        generate_lines(draw, height, width, count=20)
        bg_section //= 4
    # 运算字符
    a = get_random_number()
    op = get_random_op()
    b = get_random_number()

    # 运算结果
    ans = str(compute(a, b, op))
    # 用draw.text书写文字
    average_width = width // count
    random_list = [
        a,
        op,
        b,
        '='
    ]
    for i in range(count):
        text_height = random.randint(int((height - 10) * 0.6), height - 10)
        rand_chr = random_list[i]
        color = get_random_color()
        text_color = [0, 0, 0]
        # 背景颜色是否影响字符
        for j in range(2):
            if color[j] - background_color[j] <= bg_section:
                text_color[j] = 255 - color[j]
            else:
                text_color[j] = color[j]
        # 绘制文字
        draw.text((i * average_width + 10, 0),
                  rand_chr,
                  tuple(text_color),
                  font=ImageFont.truetype(f'{file_path()}/Fronts/SourceHanSerifSC/SourceHanSerifSC-Regular.ttf', text_height),
                  align='center')
    # 释放画笔
    del draw
    # 将图片保存在本地中，文件类型为png
    image.save(save_path, 'png')
    return ans


if __name__ == '__main__':
    # print(verification_code())
    print(verification_code_compute())
