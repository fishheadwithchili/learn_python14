结业项目：配置驱动的日志与任务编排器

目标
- 使用 tomllib 读取 TOML 配置；
- 用结构化模式匹配解析命令；
- 使用 asyncio.TaskGroup 并发执行任务；
- 应用 typing（内置泛型、Union |、Self/类型参数）确保 API 清晰；
- （可选）引入 sys.monitoring 统计函数调用次数。

结构
```
capstone/
  README.md
  src/
    main.py
    config.toml
```

验收标准
- `python src/main.py` 能读取 `config.toml`，按规则执行任务并打印结果；
- 关键函数具备类型注解并通过检查；
- 有至少 1 处 `match/case` 与 1 处 `TaskGroup` 应用。


