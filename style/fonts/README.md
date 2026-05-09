# 字体文件

本目录存放论文模板所需的所有字体文件，确保在不同环境下（包括云环境）都能正确编译。

## ⚠️ 重要说明

**本项目直接使用本地字体，不依赖系统字体。** 编译前请确保 `fonts/otf/` 目录下包含所有必需的字体文件。

## 字体文件列表

| 文件名 | 字体名称 | 用途 |
|--------|----------|------|
| `times.ttf` | Times New Roman | 英文正文 |
| `timesbd.ttf` | Times New Roman Bold | 英文粗体 |
| `timesi.ttf` | Times New Roman Italic | 英文斜体 |
| `timesbi.ttf` | Times New Roman Bold Italic | 英文粗斜体 |
| `simsun.ttc` | 宋体 | 中文正文 |
| `simhei.ttf` | 黑体 | 中文粗体/标题 |
| `simkai.ttf` | 楷体 | 中文斜体 |
| `simfang.ttf` | 仿宋 | 中文代码/等宽 |
| `stzhongs.ttf` | 华文中宋 | 封面特殊字体 |

## 关于 .ttc 文件

`.ttc` (TrueType Collection) 是包含多个字体的集合文件。LaTeX 的 `fontspec` 包支持 .ttc 文件，通过 `FontIndex` 参数指定使用集合中的哪个字体。

- `simsun.ttc` 使用 `FontIndex = 0` 来访问宋体

## 来源

这些字体来自 Windows 系统字体目录 `C:\Windows\Fonts\`。
