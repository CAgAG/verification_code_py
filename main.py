"""
 @Author  : CAgAG
 @Version : 1.0
 @Describe: 测试
"""
import verification_code

if __name__ == '__main__':
    # 需要输入的验证码
    print(verification_code.verification_code(number=True, lower_letter=True, upper_letter=True, chinese=True,
                                              width=200, height=50, count=4,
                                              difficult='medium',
                                              save_path='./images/verification_code.png'))
    # 简单计算的验证码
    print(verification_code.verification_code_compute(save_path='./images/verification_code_compute.png'))
