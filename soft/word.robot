*** Settings ***
Library           Selenium2Library
Library           DateTime

*** Keywords ***
退出驱动
    evaluate    os.system(r'taskkill /f /im IEDriverServer.exe')    os
    evaluate    os.system(r'taskkill /f /im chromedriver.exe')    os

打开浏览器
    [Arguments]    ${x}    ${y}
    open browser    ${x}    ${y}

关闭窗口
    close window

关闭浏览器
    close browser

关闭所有浏览器
    close all browsers

点击元素
    [Arguments]    ${x}
    wait until page contains element    ${x}    30    error
    click element    ${x}

点击列表
    [Arguments]    ${x}    ${y}
    wait until page contains element    ${x}    30    error
    @{z}    get webelements    ${x}
    click element    @{z}[${y}]

点击按钮
    [Arguments]    ${x}
    wait until page contains element    ${x}    30    error
    click button    ${x}

点击链接
    [Arguments]    ${x}
    wait until page contains element    ${x}    30    error
    click link    ${x}

点击radio
    [Arguments]    ${x}    ${y}
    wait until page contains element    name:${x}    30    error
    select radio button    ${x}    ${y}

下拉框
    [Arguments]    ${x}    ${y}
    wait until page contains element    ${x}    30    error
    select from list by value    ${x}    ${y}

双击
    [Arguments]    ${x}
    wait until page contains element    ${x}    30    error
    double click element    ${x}

输入文本
    [Arguments]    ${x}    ${y}
    wait until page contains element    ${x}    30    error
    clear element text    ${x}
    input text    ${x}    ${y}

jq点击
    [Arguments]    ${x}
    wait until page contains element    css:${x[1:-1]}    30    error
    execute javascript    $(${x}).click()

jq双击
    [Arguments]    ${x}
    wait until page contains element    css:${x[1:-1]}    30    error
    execute javascript    $(${x}).dblclick()

jq输入
    [Arguments]    ${x}    ${y}
    wait until page contains element    css:${x[1:-1]}    30    error
    execute javascript    $(${x}).val(${y})

js点击
    [Arguments]    ${x}
    wait until page contains element    css:${x[1:-1]}    30    error
    execute javascript    document.querySelectorAll(${x})[0].click()

js点击1
    [Arguments]    ${x}    ${y}
    wait until page contains element    css:${x[1:-1]}    30    error
    execute javascript    document.querySelectorAll(${x})[${y}].click()

js输入
    [Arguments]    ${x}    ${y}
    wait until page contains element    ${x}    30    error
    ${t1}    get current date
    assign id to element    ${x}    ${t1}
    execute javascript    window.document.getElementById('${t1}').value='${y}'

滚动条
    [Arguments]    ${x}    ${y}
    wait until page contains element    css:${x[1:-1]}    30    error
    execute javascript    document.querySelectorAll(${x})[0].scollTop=${y}

打开新页面
    [Arguments]    ${x}
    sleep    3
    execute javascript    window.open('${x}')

切换frame
    [Arguments]    ${x}
    wait until page contains element    ${x}    30    error
    select frame    ${x}

得到窗口
    sleep    2
    @{x}    get window handles
    [Return]    @{x}

切换窗口
    [Arguments]    ${x}    ${y}
    ${z}    evaluate    list(set(${x})-set(${y}))
    sleep    5
    select window    ${z[0]}

返回主页面
    select window       main

验证
    [Arguments]    ${x}    ${y}
    wait until page contains element    ${x}    30    error
    ${z}    get text    ${x}
    should contain    ${z}    ${y}

得到文本
    [Arguments]    ${x}
    wait until page contains element    ${x}    30    error
    ${y}    get text    ${x}
    [Return]    ${y}

rf输入时间
    [Arguments]    ${x}    ${y}
    ${t1}    get current date
    ${t2}    add time to date    ${t1}    ${y}days
    wait until page contains element    ${x}    30    error
    assign id to element    ${x}    ${t1}
    execute javascript    window.document.getElementById('${t1}').value='${t2[0:11]}'

py输入时间
    [Arguments]    ${x}    ${y}    ${z}    ${d}
    import library    c:/robot/py/date.py
    ${t1}    evaluate    int(${d})
    ${t2}    date    ${y}    ${z}    ${t1}
    ${t3}    get current date
    wait until page contains element    ${x}    30    error
    assign id to element    ${x}    ${t3}
    execute javascript    window.document.getElementById('${t3}').value='${t2}'

数据
    [Arguments]    ${x}    ${y}
    import library    ${x}/read.py
    @{z}    read    ${x}    ${y}
    [Return]    @{z}
