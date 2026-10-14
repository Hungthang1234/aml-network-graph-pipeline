from pathlib import Path


def touch_file(path: Path) -> None:
    path.touch(exist_ok=True)


def main() -> None:
    root = Path("aml_graph_pipeline")

    directories = [
        root / "data" / "raw",
        root / "data" / "processed",
        root / "notebooks",
        root / "src" / "etl",
        root / "src" / "graph",
        root / "src" / "config",
        root / "dags",
        root / "api",
        root / "docs",
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

    code_directories = [
        root / "src",
        root / "src" / "etl",
        root / "src" / "graph",
        root / "src" / "config",
        root / "dags",
        root / "api",
    ]
    for directory in code_directories:
        touch_file(directory / "__init__.py")

    empty_directories = [
        root / "data" / "raw",
        root / "data" / "processed",
        root / "notebooks",
        root / "docs",
    ]
    for directory in empty_directories:
        touch_file(directory / ".gitkeep")

    print(f"Đã tạo cấu trúc thư mục tại: {root.resolve()}")


if __name__ == "__main__":
    main()
