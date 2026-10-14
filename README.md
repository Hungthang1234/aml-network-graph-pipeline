# aml-network-graph-pipeline

Script khởi tạo cấu trúc dự án Data Engineering theo yêu cầu.

## Cách sử dụng

```bash
python create_project_structure.py
```

Sau khi chạy, script sẽ tạo cây thư mục `aml_graph_pipeline/` gồm:

- `data/raw/`, `data/processed/`
- `notebooks/`
- `src/etl/`, `src/graph/`, `src/config/`
- `dags/`
- `api/`
- `docs/`

Quy tắc file mặc định:

- Thư mục code: tạo `__init__.py`
- Thư mục rỗng: tạo `.gitkeep`