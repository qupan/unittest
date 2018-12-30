一个简单的请求拦截器的例子，它会中止所有的图像请求：

const puppeteer = require('puppeteer');

puppeteer.launch().then(async browser => {
  const page = await browser.newPage();
  await page.setRequestInterception(true);
  page.on('request', interceptedRequest => {
    if (interceptedRequest.url().endsWith('.png') || interceptedRequest.url().endsWith('.jpg'))
      interceptedRequest.abort();
    else
      interceptedRequest.continue();
  });
  await page.goto('https://example.com');
  await browser.close();
});
NOTE 启用请求拦截将禁用页面缓存。

page.setUserAgent(userAgent)
userAgent <string> 在此页面中使用的特定用户代理
returns: <Promise> Promise在用户代理被设置时解决。
