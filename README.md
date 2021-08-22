### 支持验证码类型

- 数字
- 字母
- 中文
- 简单运算 (+ - *)

### 环境安装

```bash
pip install pillow
```

### 使用

```python
# 需要输入的验证码
print(verification_code.verification_code(number=True, lower_letter=True, upper_letter=True, chinese=True,
                                              width=200, height=50, count=4,
                                              difficult='medium',
                                              save_path='./images/verification_code.png'))
# 简单计算的验证码
print(verification_code.verification_code_compute(save_path='./images/verification_code_compute.png'))
```

#### 生成的图片

![verification_code](./images/verification_code.png)

![verification_code](./images/verification_code_compute.png)

#### 输出

```bash
Sz兄4
5
```

