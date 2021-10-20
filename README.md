## 提交说明

1. 文件格式为 toml 不懂的同学请参考 [https://toml.io/cn/v1.0.0](https://toml.io/cn/v1.0.0)

2. 文件名以库名命名。库名不能冲突，如果 libs 目录下没有也要检查系统库有没有重名，这个在 amod 工具里新建页输入库名可以检测重名

3. 如果是 url 文件一定要写sha1 hash 防止下载出错

   ### 示例：

   ```toml
   [package]
   #这些为必填
   name = "log4j"
   version = "v1.02"
   url = "https://cdn.jsdelivr.net/gh/zzerding/aardio-log4j@v1.0.2/dist/log4j.tar.gz"
   #git = "https://github.com/zzerding/aardio-log4j" #这样是以git clone下载的其实也很方便就是考虑到有的人连不上
   sha = "fe53235cc77e20e860f8922eb941f21a17e5dfed"
   authors = "zzerd"
   description = "基于log4j理念设计的日志管理库,console有彩色输出日志可分类"
   samples = "test/log4jTest.aardio"
   
   #下面为可选的：请参考https://github.com/zzerding/amod/blob/master/docs/%E5%BA%93%E6%8F%90%E4%BA%A4%E8%A7%84%E8%8C%83.md
   homepage = "https://zzerd.com"
   repository ="https://github.com/zzerding/aardio-log4j"
   
   
   ```
   
   

## 使用说明

所有 libs 目录下的 toml 文件会通过 gihub actions 合并成 json 并gzip压缩打包，最终发布到 release 分支。下载地址为：

- [🐙 github raw](https://github.com/zzerding/amod/raw/release/libs.json.gz)

- [🚀 CDN 加速](https://cdn.jsdelivr.net/gh/zzerding/amod@release/libs.json.gz)

  cdn 可能有缓存的问题，如果 github raw 能访问不建议使用 cdn

### 使用技巧

建议把库打包一下，放到github上，然后每个版本都打上标签，用 jsdelivr cdn 加速。当然这不是强制要求的，你也可以放 git 地址