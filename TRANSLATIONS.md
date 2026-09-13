# 双语维护 / Maintaining the Chinese and English Editions

[中文目录](README.md) · [English contents](en/README.md)

## 中文说明

原作者为王洪磊，中文原书来自 [Gitee](https://gitee.com/honglei_wang/Notes-on-AI-Infrastructure)。本版以提交 `f78f73a7ebb4b8c513f49788f8ce6b8ba762b002` 为初始翻译基线，新增 AI 辅助英文翻译与编辑、24 幅英文图表，以及双语导航。中文正文与原图保留；中文页面新增的导航用 HTML 注释明确标记。

英文覆盖 11 章、3 篇辑前言、序言与后记。部分重复措辞作了精简；技术示例、章节结构、参考资料及作者观点标签保留。图表以 Mermaid 或 Markdown 表格重绘。译文中的第一人称指原作者；译本不代表原作者审定，也不是针对最新软硬件重新核实的技术版本。参考资料中的 `docs/...`、`yidian/...` 等路径沿用原书名称，相关外部材料并未收录于上游仓库。

维护步骤：

1. 编辑中文文件时，同步更新 `translations.json` 中对应的英文页面；原图发生变化时，也更新英文图表。
2. 核对译文后，明确刷新该页的源文件及图片摘要。例如：
   ```sh
   python3 scripts/check_translations.py --refresh-source '第一辑：造场子/第01章-IDC与智算中心建设.md'
   ```
3. 运行完整检查：
   ```sh
   python3 scripts/check_translations.py
   ```
4. 在同一次提交中包含中文、英文、涉及的图片以及清单更新。GitHub Actions 在推送及 PR 时运行检查。

若只是改善英文措辞，直接修改英文并运行检查，无需刷新中文摘要。不要仅为消除检查错误而刷新摘要：摘要记录的是已经同步审阅过的中文版本。

## English instructions

The Chinese source stays in its original directories. Its English counterpart is recorded in [translations.json](translations.json). The manifest is ordered for reading and stores a SHA-256 digest of each Chinese page's body and each referenced source image.

When you change a Chinese page:

1. Update its paired English page, including any affected code, tables, figures, and reference lists.
2. Review both versions, then record the source and image digests for that page:
   ```sh
   python3 scripts/check_translations.py --refresh-source '第一辑：造场子/第01章-IDC与智算中心建设.md'
   ```
3. Run the checks and commit both editions with the updated manifest:
   ```sh
   python3 scripts/check_translations.py
   ```

The refresh option can be repeated for several pages. It records reviewed source state; it does **not** translate content or establish that a translation is accurate. English-only wording corrections need no source refresh.

For a new page, add the Chinese and English files, then add a pair to the manifest in reading order with `source`, `translation`, an empty `source_sha256`, and empty `assets`. Update both contents pages, regenerate navigation, and refresh that page:

```sh
python3 scripts/check_translations.py --write-navigation --refresh-source 'path/to/new-chinese-page.md'
```

New book chapters belong in the existing part directories, where coverage checks discover them. If the book gains another top-level section, extend source discovery in the checker as part of that change. Renames require updating the manifest, both contents pages, and any affected links before regenerating navigation.

## What the checks cover / 检查范围

The dependency-free checker requires Python 3.10 or later. It verifies:

- Every Chinese book page has exactly one English counterpart, with no unlisted English pages.
- Numbered sections appear in the same order.
- Every original image has one marked English figure or table.
- Chinese text and source-image hashes match the last recorded translation review.
- Language, contents, and previous/next links match the manifest.
- Local Markdown link targets exist, code fences close, and translation placeholders are resolved.

Checks do not judge translation quality, validate technical claims or commands, test external reference availability, or render Mermaid. Review diagrams on GitHub or in a Mermaid-capable Markdown viewer before merging figure changes.

检查用于发现结构遗漏及未同步修改，不能代替语言审校、技术核验或图表渲染检查。

## Navigation and figures / 导航与图表

Navigation is the only addition to the original Chinese book pages. It is enclosed by `<!-- bilingual-navigation:start -->` and `<!-- bilingual-navigation:end -->`. The checker excludes this generated block when hashing the source body.

English figures are associated with source images using a marker such as:

```html
<!-- translated-figure: images/ch01/fig01-cpu-gpu-cabinet-power.png -->
```

Keep that marker with the English Mermaid diagram or table so image changes can be traced to the correct translation. Preserve original Chinese images in `images/`.

## Attribution / 署名

Preserve the original author's attribution and upstream license notices. The source [LICENSE](LICENSE) and the original README license statement are retained; the [English contents page](en/README.md) describes the translation's scope. Changes in this edition comprise English translations, English figure adaptations, landing-page edits, navigation blocks, and maintenance tooling.
