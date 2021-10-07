## amod 
> 这是一个第三方的 aardio 库管理工具，管理工程里的第三方依赖库。
库路径可为本地路径、git、url(lzmp格式下载地址)三种。第三库用 [amod.toml](##配置文件) 配置。
使用方法为把本库 clone 到工具目录或者代码段目录。

## 使用方法

### 包的安装

#### 1、本地文件夹

#### 2、 url下载

​	支持 lzma gz tgz 文件后缀



## 配置文件
amod.toml 配置参考

* `[package]` — Defines a package.
  * `name` — The name of the package.
  * `version` — The version of the package.
  * `authors` — The authors of the package..
  * `description` — A description of the package.
  * `documentation` — URL of the package documentation.
  * `readme` — Path to the package's README file.
  * `homepage` — URL of the package homepage.
  * `repository` — URL of the package source repository.
  * `license` — The package license.
  * `license-file — Path to the text of the license.
  * `keywords` — Keywords for the package.
* `[dependencies]`— Package library dependencies.
* `[dev-dependencies]` — Dependencies for examples, tests, and benchmarks.

<a id="package-metadata"></a>
### The `[package]` section

package 如果不作为依赖库可以空。如果作为依赖库则要求填写。

```toml
[package]
name = "hello_world" # the name of the package
version = "0.1.0"    # the current version, obeying semver
authors = "Alice <a@example.com>" # the authors is 
```
必填字段为name version 其它为可选

#### The `name` field
包名为 `aardio` 有效的 `namespace ` 名称


#### The `version` field

版本号为语义化版本 [说明](https://semver.org/lang/zh-CN//), 一些原则:
* 如果没到1.0.0 之前可修改 api
* 如果版本为1.0.0 之后则只能在主要版本修改已存在的 api 不能在次要版本修改
* 增加功能请增加版本号


#### The `authors` field
作者名为可选字段，但是发布为远程为必选字段。

#### The `description` field

包说明为可选字段，但是发布为远程为必选字段.

```toml
[package]
# ...
description = "A short description of my package"
```

#### The `documentation` field
文档链接，如果有的话。

```toml
[package]
# ...
documentation = "https://github.com/zzerding/aardio-log4j"
```

#### The `readme` field

readme 字段应该是包根目录中文件的路径（相对于这个 amod.toml），可选

```toml
[package]
# ...
readme = "README.md"
```


#### The `homepage` field

包或者作者主页 url ，可选

```toml
[package]
# ...
homepage = "https://zzerd.com/"
```

#### The `repository` field

包仓库 url ，可选

```toml
[package]
# ...
repository = "https://github.com/zzerding/aardio-log4j"
```

#### The `license` and `license-file` fields

许可证字段包含发布包所依据的软件许可证的名称。 license-file 字段包含包含许可​​证文本的文件的路径（相对于 amod.toml）

```toml
[package]
# ...
license = "MIT OR Apache-2.0"
```

使用 OR 表示用户可以选择任一许可证。 使用 AND 表示用户必须同时遵守两个许可证。 WITH 运算符表示具有特殊例外的许可证。 一些例子：

* `MIT OR Apache-2.0`
* `LGPL-2.1-only AND MIT AND BSD-2-Clause`
* `GPL-2.0-or-later WITH Bison-exception-2.2`

如果软件包使用非标准许可证，则可以指定 license-file 字段来代替许可证字段。

```toml
[package]
# ...
license-file = "LICENSE.txt"
```


#### The `keywords` field

关键字字段是描述此包的字符串数组。搜索包时，这会有所帮助，您可以选择任何有助于找到此包的词。

```toml
[package]
# ...
keywords = ["gamedev", "graphics"]
```
### The `[dependencies]` and `[dev-dependencies]` section
dependencies 安装在工程目录`/lib`，dev-dependencies 安装在主程目录`/tools`。

您的  可以依赖url、git 存储库或本地文件系统上的子目录中的其他库

```toml
[dependencies]
ahk = "0.1.12"

指定用git安装
​```toml
[dependencies]
log4j = { git = "https://github.com/zzerding/aardio-log4j" }
```

指定lzmp gz  tgz url 安装
```toml
[dependencies]
log4j = { url = "https://github.com/zzerding/aardio-log4j/releases/latest/download/log4j.tar.lzma" }


指定本地路径安装
log4j = {path = "~/aardio/lib/log4j"}

```


## 参考
* [cargo](https://doc.rust-lang.org/cargo/reference/manifest.html)
* [spdx](https://spdx.dev/spdx-specification-21-web-version)
* [TOML]( https://toml.io/)
*/


var body = string.gfmark.render(md);
var htmlStr = /**
<!doctype html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<link href="http://cdn.staticfile.org/github-markdown-css/4.0.0/github-markdown.css" rel="stylesheet" type="text/css" />
<style>
	.markdown-body {
		box-sizing: border-box;
		min-width: 200px;
		max-width: 980px;
		margin: 0 auto;
		padding: 45px;
	}
	@media (max-width: 767px) {
		.markdown-body {
			padding: 15px;
		}
	}
</style>
</head>
<body>

<article class="markdown-body">
	${body}
</article>
</body>
</html>## amod 
> 这是一个第三方的 aardio 库管理工具，管理工程里的第三方依赖库。
库路径可为本地路径、git、url(lzmp格式下载地址)三种。第三库用 [amod.toml](##配置文件) 配置。
使用方法为把本库 clone 到工具目录或者代码段目录。

## 使用方法
## 配置文件
amod.toml 配置参考

* `[package]` — Defines a package.
  * `name` — The name of the package.
  * `version` — The version of the package.
  * `authors` — The authors of the package..
  * `description` — A description of the package.
  * `documentation` — URL of the package documentation.
  * `readme` — Path to the package's README file.
  * `homepage` — URL of the package homepage.
  * `repository` — URL of the package source repository.
  * `license` — The package license.
  * `license-file — Path to the text of the license.
  * `keywords` — Keywords for the package.
* `[dependencies]`— Package library dependencies.
* `[dev-dependencies]` — Dependencies for examples, tests, and benchmarks.

<a id="package-metadata"></a>
### The `[package]` section

package 如果不作为依赖库可以空。如果作为依赖库则要求填写。

```toml
[package]
name = "hello_world" # the name of the package
version = "0.1.0"    # the current version, obeying semver
authors = "Alice <a@example.com>" # the authors is 
```
必填字段为name version 其它为可选

#### The `name` field
包名为 `aardio` 有效的 `namespace ` 名称


#### The `version` field

版本号为语义化版本 [说明](https://semver.org/lang/zh-CN//), 一些原则:
* 如果没到1.0.0 之前可修改 api
* 如果版本为1.0.0 之后则只能在主要版本修改已存在的 api 不能在次要版本修改
* 增加功能请增加版本号


#### The `authors` field
作者名为可选字段，但是发布为远程为必选字段。

#### The `description` field

包说明为可选字段，但是发布为远程为必选字段.

```toml
[package]
# ...
description = "A short description of my package"
```

#### The `documentation` field
文档链接，如果有的话。

```toml
[package]
# ...
documentation = "https://github.com/zzerding/aardio-log4j"
```

#### The `readme` field

readme 字段应该是包根目录中文件的路径（相对于这个 amod.toml），可选

```toml
[package]
# ...
readme = "README.md"
```


#### The `homepage` field

包或者作者主页 url ，可选

```toml
[package]
# ...
homepage = "https://zzerd.com/"
```

#### The `repository` field

包仓库 url ，可选

```toml
[package]
# ...
repository = "https://github.com/zzerding/aardio-log4j"
```

#### The `license` and `license-file` fields

许可证字段包含发布包所依据的软件许可证的名称。 license-file 字段包含包含许可​​证文本的文件的路径（相对于 amod.toml）

```toml
[package]
# ...
license = "MIT OR Apache-2.0"
```

使用 OR 表示用户可以选择任一许可证。 使用 AND 表示用户必须同时遵守两个许可证。 WITH 运算符表示具有特殊例外的许可证。 一些例子：

* `MIT OR Apache-2.0`
* `LGPL-2.1-only AND MIT AND BSD-2-Clause`
* `GPL-2.0-or-later WITH Bison-exception-2.2`

如果软件包使用非标准许可证，则可以指定 license-file 字段来代替许可证字段。

```toml
[package]
# ...
license-file = "LICENSE.txt"
```


#### The `keywords` field

关键字字段是描述此包的字符串数组。搜索包时，这会有所帮助，您可以选择任何有助于找到此包的词。

```toml
[package]
# ...
keywords = ["gamedev", "graphics"]
```
### The `[dependencies]` and `[dev-dependencies]` section
dependencies 安装在工程目录`/lib`，dev-dependencies 安装在主程目录`/tools`。

您的  可以依赖url、git 存储库或本地文件系统上的子目录中的其他库

```toml
[dependencies]
ahk = "0.1.12"

指定用git安装
​```toml
[dependencies]
log4j = { git = "https://github.com/zzerding/aardio-log4j" }
```

指定lzmp(或者 aardio) url 安装
```toml
[dependencies]
log4j = { url = "https://github.com/zzerding/aardio-log4j/releases/latest/download/log4j.tar.lzma" }


指定本地路径安装
log4j = {path = "~/aardio/lib/log4j"}

```


## 参考
* [cargo](https://doc.rust-lang.org/cargo/reference/manifest.html)
* [spdx](https://spdx.dev/spdx-specification-21-web-version)
* [TOML]( https://toml.io/)

