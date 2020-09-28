from selenium.webdriver.common.by import By


"""测试权限页面"""
# 刷新pv
test_flush_pv_xpath = (By.XPATH,'/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/a')
# 清除vip
test_clear_vip_xpath = (By.XPATH,'/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[6]/td[2]/a')
# 变成第一天登录
test_flush_score_xpath = (By.XPATH,'/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[4]/td[2]/a')
# 修改注册时间为今天
test_change_c_time_xpath = (By.XPATH,'/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[17]/td[2]/a')

"""首页"""
# 登录按钮
home_login_xpath = (By.XPATH,'//*[@id="wrapper"]/div[5]/div/div[1]/div[2]/div[2]/a[1]')
# free用户头像
home_free_user_img_xpath = (By.XPATH,'//*[@id="wrapper"]/div[5]/div/div[1]/div[2]/div[5]/a[1]/div/img')
# VIP用户头像
home_vip_user_img_xpath = (By.XPATH,'//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/div[5]/a[1]/div[1]/img')
# 退出按钮
home_logout_xpath = (By.XPATH,'//*[@id="wrapper"]/div[5]/div/div[1]/div[2]/div[5]/div/div[4]/a[5]/i')

"""登录弹窗"""
# 登录框-google按钮
login_google_icon_xpath = (By.XPATH,'//*[@id="base-public-login"]/div[2]/div/div/div/div[1]/div/a[1]')
# 登录框-fb按钮
login_fb_icon_xpath = (By.XPATH,'//*[@id="base-public-login"]/div[2]/div/div/div/div[1]/div/a[2]')
# 登录框-twitter按钮
login_twitter_icon_xpath = (By.XPATH,'//*[@id="base-public-login"]/div[2]/div/div/div/div[1]/div/a[3]')

"""邮箱登录"""
# 邮箱登录-邮箱输入框
login_email_username_id = (By.ID,'base-public-login-email-text')
# 邮箱登录-密码输入框
login_email_password_id = (By.ID,'base-public-login-password-text')
# 邮箱登录-登录按钮
login_email_button_id = (By.ID,'base-sub-Login-Btn')
"""fb登录"""
# fb登录-用户名输入框
login_fb_username_xpath = (By.XPATH,'//*[@id="email"]')
# fb登录-密码输入框
login_fb_password_xpath = (By.XPATH,'//*[@id="pass"]')
# fb登录-登录按钮
login_fb_button_xpath = (By.XPATH,'//*[@id="loginbutton"]')
"""twitter登录"""
# twitter登录-用户名输入
login_twitter_username_id = (By.ID,'username_or_email')
# twitter登录-密码输入
login_twitter_password_id = (By.ID,'password')
# twitter登录-登录按钮
login_twitter_button_id = (By.ID,'allow')

"""会员页"""
# 会员页登录按钮
premium_login_xpath = (By.XPATH,'//*[@id="wrapper"]/div[3]/div/div/div/a[1]')
# 季套餐购买按钮
premium_3_months_xpath = (By.XPATH,'//*[@id="wrapper"]/div[4]/div[2]/div[3]/article/div[1]/div[2]/a')
# 半年套餐购买按钮
premium_6_months_xpath = (By.XPATH,'//*[@id="wrapper"]/div[4]/div[2]/div[3]/article/div[2]/div[2]/a')
# 年套餐购买按钮
premium_annual_xpath = (By.XPATH,'//*[@id="wrapper"]/div[4]/div[2]/div[3]/article/div[3]/div[2]/a')
# 终身套餐购买按钮
premium_lifetime_xpath = (By.XPATH,'//*[@id="wrapper"]/div[4]/div[2]/div[2]/div/div[2]/a')
# 支付成功弹窗ok按钮
premium_pay_success_ok_xpath = (By.XPATH,'//*[@id="pay-success"]/div[2]/div/a[2]')

"""充值"""
"""钱海支付"""
pay_card_xpath = (By.XPATH,'//*[@id="wrapper"]/div[3]/div/div[2]/div/div[2]/ul/li[1]')  # 钱海支付
card_first_name_id = (By.ID,'strat-cardHolderFirstName') # 姓
card_last_name_id = (By.ID,'strat-cardHolderLastName') # 名
card_phone_number_id = (By.ID,'start-billPhoneNumber') # 电话
card_city_id = (By.ID,'start-billCity') # 城市
card_email_id = (By.ID,'strat-cardHolderEmail') # 邮箱
card_postal_code_id = (By.ID,'billZip') # 邮编
card_billing_address_id = (By.ID,'start-billAddress') # 账单邮寄地址
card_confirm_subscription_button_id = (By.ID,'start-show-pay-box') # 订单提交按钮
card_card_number_id = (By.ID,'card_number_temp') # 卡号输入框
card_expiration_date_id = (By.ID,'checkout_expiration_date') # 失效日期输入框
card_secure_code_id = (By.ID,'cvv2') # 安全验证码
card_pay_now_xpath = (By.XPATH,'//*[@id="wrap_height"]/div/div[3]/div/div[4]/button[1]') # 立即支付按钮

"""paypal支付"""
pay_paypal_xpath = (By.XPATH,'//*[@id="wrapper"]/div[3]/div/div[2]/div/div[2]/ul/li[2]/a/span') # paypal支付类型
paypal_icon_xpath = (By.XPATH,'//*[@id="paypal-animation-content"]/div[1]/div[1]/div/img[2]') # paypal图标按钮
paypal_email_xpath = (By.XPATH,'//*[@id="email"]') # paypal用户名
paypal_password_xpath = (By.XPATH,'//*[@id="password"]') # paypal密码
# 若出现paypal登录按钮
paypal_go_login_xpath = (By.XPATH,'//*[@id="loginSection"]/div/div[2]/a') # 点击登录入口
paypal_next_xpath = (By.XPATH,'//*[@id="btnNext"]') # 输入用户名后的下一步按钮
# 输入用户名和密码之后的登录按钮
paypal_login_xpath = (By.XPATH,'//*[@id="btnLogin"]') # 点击登录按钮
paypal_continue_xpath = (By.XPATH,'//*[@id="button"]/button') # 继续按钮
paypal_buy_now_id = (By.ID,'confirmButtonTop') # 立即购买

"""本地支付"""
pay_paymentwall_xpath = (By.XPATH,'//*[@id="wrapper"]/div[3]/div/div[2]/div/div[2]/ul/li[3]/a/span')
pw_input_email_id = (By.ID,'pw-email')
pw_input_password_id = (By.ID,'pw-fullname')
pw_confirm_subscription_xpath = (By.XPATH,'//*[@id="go-Paymentwall-div"]/div[2]/a')
pw_buy_now_button_id = (By.ID,'ps_psb')
pw_pay_success_xpath = (By.XPATH,'//*[@id="ps_content"]/h3')

"""paypal信用卡支付"""
paypal_card_icon_xpath = (By.XPATH,'//*[@id="paypal-animation-content"]/div[1]/div[2]/div[1]/img')  # paypal信用卡图标
# paypal信用卡支付弹窗中的信息
paypal_card_country_select_id = (By.ID,'countrySelector') # 选择国家下拉框1
paypal_card_card_number_id  = (By.ID,'cc') # 卡号
paypal_card_expory_id = (By.ID,'expiry_value') # 有效期
paypal_card_cvv_id = (By.ID,'cvv') # 三位有效数字
paypal_card_first_name_id = (By.ID,'firstName') # first name
paypal_card_last_name_id = (By.ID,'lastName') # last name
paypal_card_address1__id = (By.ID,'billingLine1') # 地址1
paypal_card_address2__id = (By.ID,'billingLine2') # 地址2
paypal_card_poster_code__id = (By.ID,'billingPostalCode') # 邮编
paypal_card_city_id = (By.ID,'billingCity') # 城市
paypal_card_state_id = (By.ID,'billingState') # 选择洲下拉框2

paypal_card_telephone_id = (By.ID,'telephone') # 电话
paypal_card_email_xpath = (By.XPATH,'//*[@id="email"]') # 邮箱
paypal_card_buy_now_id = (By.ID,'pomaSubmit') # 立即支付
