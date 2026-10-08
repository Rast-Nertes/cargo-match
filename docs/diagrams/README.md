# Диаграммы Lab#01

| Файл | Назначение |
|------|------------|
| `c4-context.mmd` | C4 Level 1 — контекст системы |
| `c4-containers.mmd` / `.puml` / `.svg` | C4 Level 2 — контейнеры |
| `erd.mmd` / `.puml` / `.svg` | ER-диаграмма (3NF) |
| `use-cases.mmd` | Use Cases по ролям |

Регенерация SVG (Mermaid CLI):

```bash
npx -y @mermaid-js/mermaid-cli -i c4-containers.mmd -o c4-containers.svg
npx -y @mermaid-js/mermaid-cli -i erd.mmd -o erd.svg
npx -y @mermaid-js/mermaid-cli -i c4-context.mmd -o c4-context.svg
npx -y @mermaid-js/mermaid-cli -i use-cases.mmd -o use-cases.svg
```
