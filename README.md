# Oauth
A Oauth2.0 verification demo

## code todos
1. 模仿 github，我的代码首先需要 user、oauth 模块，需要一个商家授权页面 oauth app 登记页面，来处理 第三方登记
2. 能够处理以下链接
https://localhost.com:3000/oauth/authorize?client_id={}&redirect_uri={}
并返回
http://localhost:8080/oauth/redirect?code={}

3. 下发 token，能够处理以下链接
http://localhost:3000/oauth/access_token?client_id={}&client_secret={}&code={}
返回以下json数据
{'access_token': 'woxoyaj2pwgklzr4qkh25yv795vh1qbgat42d1bj', 'scope': '', 'token_type': 'bearer'}

4. 能够让用户获取信息
http://localhost:3000/api/user/profile