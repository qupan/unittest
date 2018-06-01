*** Settings ***
Test Teardown
Library           RequestsLibrary

*** TestCases ***
场景1
    ${x}    新增接口测试入参    {"jjj":"kll","kdjfk":"315545655"}    {"jjj":"kll","kdjfk":"kdf"}
    log    ${x}

*** Keywords ***
新增接口测试入参
    [Arguments]    ${table_value}    ${json_format}
    [Documentation]    新增接口入参以及json格式
    import library    d:/robot/py/trans_type.py    #引入trans_type.py文件
    ${table_value_dict}    trans_dict    ${table_value}    #调用函数trans_dict,传入值 得到一个字典，用$变量来接收
    ${json_list}    create list    ${table_value_dict}    #把字典放到列表中，用$变量 形式接收
    &{json_format_dict}    trans_dict    ${json_format}    #再次调用函数，返回另外一个 字典,用&字典来接收
    ${json_value}    Create Dictionary    &{json_format_dict}    date=${json_list}    #把上面的两个变量放入字典中 以$变量的形式来接收
    log     ${json_value}    #打印值，作为调试
    ${last}    evaluate    demjson.encode(${json_value})    demjson    #调用python中的demjson库把值 转换为json格式
    log     ${last}    #打印出值，调试
    [Return]    ${last}

检查json返回状态
    [Arguments]    ${pathparam}    ${postdata}
    [Documentation]    得到返回体中的状态结果
    ${dict}    Create Dictionary    Content-Type=application/json    #请求头创建为字典，使用变量 $来接收
    ${result}    post request    session    ${pathparam}    data=${data}    #发送post请求，传入网址和data 参数
    log    ${result.status_code}    #打印响应码
