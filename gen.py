import pyotp
import time
from progress.bar import Bar

# 输入密钥
secret_key = input("请输入谷歌密钥: ")

# while True:
    # 生成验证码
totp = pyotp.TOTP(secret_key)
code = totp.now()

# 显示验证码及其有效时间
print("验证码:", code)

# # 使用进度条显示剩余有效时间
# bar = Bar('有效时间: 10 秒，倒计时', max=10)
# for i in range(10):
#     bar.next()
#     time.sleep(1)
# bar.finish()

    # # 检查验证码是否过期
    # if totp.verify(code):
    #     print("验证码有效!")
    # else:
    #     print("验证码已过期，请重新生成。")
    #     continue
