# 家园版本发布

[![建立状态][travis-image]][travis-url] [![依赖状态][dep-image]][dep-url]

该存储库包含[ethereum.org][1]网站的家园版。

![截图](https://cloud.githubusercontent.com/assets/112898/15186824/f2c9ba56-1774-11e6-944b-8309c6b9114e.png "截图")

## 条件

* node
* npm

## 安装

确保你已经安装了node.js和npm。

克隆存储库并安装依赖项

```bash
git clone https://github.com/ethereum/ethereum-org
cd ethereum-org
npm install
npm install -g grunt-cli
```

## 建立静态资源

```bash
grunt
```

## 运行

```bash
npm start
```

### 添加pm2支持

```bash
pm2 start pm2.json
```
请参阅<http://localhost:3000>上的界面

## 发布最新的主版到GitHub页面

```bash
git checkout gh-pages
git merge develop
grunt build
git commit -am "更新版本"
git push origin gh-pages
```

[travis-image]:https://travis-ci.org/ethereum/ethereum-org.svg
[travis-url]: https://travis-ci.org/ethereum/ethereum-org
[dep-image]: https://david-dm.org/ethereum/ethereum-org.svg
[dep-url]: https://david-dm.org/ethereum/ethereum-org

[1]: https://ethereum.org/