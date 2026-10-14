# AML Network Graph Pipeline

Pipeline dữ liệu phục vụ phân tích mạng lưới giao dịch tài chính và hỗ trợ phát hiện các dấu hiệu **rửa tiền (Anti-Money Laundering - AML)**. Dự án chuyển đổi dữ liệu giao dịch từ bộ dữ liệu **Kaggle PaySim** thành cấu trúc đồ thị, từ đó giúp trực quan hóa mối quan hệ giữa các tài khoản và nhận diện những mẫu giao dịch bất thường.

## 1. Giới thiệu dự án

### Mục tiêu

- Thu thập và tiền xử lý dữ liệu giao dịch tài chính từ bộ dữ liệu PaySim.
- Mô hình hóa các giao dịch dưới dạng **đồ thị giao dịch**:
  - **Node**: tài khoản hoặc thực thể tham gia giao dịch.
  - **Edge**: giao dịch chuyển tiền giữa hai thực thể.
  - **Attributes**: số tiền, loại giao dịch, thời gian và các đặc trưng liên quan.
- Phân tích cấu trúc mạng lưới để phát hiện các hành vi đáng ngờ, chẳng hạn như:
  - Chuyển tiền qua nhiều tài khoản trung gian.
  - Mạng lưới tài khoản có quan hệ giao dịch dày đặc bất thường.
  - Giao dịch vòng tròn hoặc luân chuyển tiền giữa nhiều tài khoản.
  - Tài khoản trung tâm có vai trò bất thường trong mạng lưới.
- Cung cấp dữ liệu và trực quan hóa phục vụ phân tích, báo cáo và điều tra AML.

### Luồng xử lý tổng quát

```text
PaySim Dataset
      ↓
Tiền xử lý và chuẩn hóa dữ liệu
      ↓
Xây dựng đồ thị giao dịch
      ↓
Phân tích đặc trưng mạng lưới
      ↓
Lưu trữ và cung cấp dữ liệu qua API
      ↓
Trực quan hóa và báo cáo AML
```

## 2. Tech Stack

| Nhóm | Công nghệ | Mục đích sử dụng |
|---|---|---|
| Ngôn ngữ | **Python** | Xây dựng pipeline, phân tích dữ liệu và phát triển API |
| Xử lý dữ liệu | **Pandas** | Đọc, làm sạch, biến đổi và tổng hợp dữ liệu giao dịch |
| Phân tích đồ thị | **NetworkX** | Xây dựng và phân tích mạng lưới giao dịch |
| Cơ sở dữ liệu | **MySQL** | Lưu trữ dữ liệu giao dịch và các đặc trưng đồ thị |
| Điều phối pipeline | **Apache Airflow** | Lập lịch, điều phối và giám sát các tác vụ ETL |
| API | **Flask** | Cung cấp các endpoint truy vấn dữ liệu và kết quả phân tích |
| Hạ tầng đám mây | **AWS S3** | Lưu trữ dữ liệu thô và dữ liệu đã xử lý |
| Hạ tầng đám mây | **AWS EC2** | Triển khai pipeline, API hoặc các dịch vụ xử lý |
| Hạ tầng đám mây | **AWS RDS** | Vận hành cơ sở dữ liệu MySQL trên AWS |
| Trực quan hóa | **Power BI / PyVis** | Xây dựng dashboard và trực quan hóa mạng lưới giao dịch |

## 3. Kiến trúc thư mục

Cấu trúc thư mục cơ bản của dự án:

```text
aml-network-graph-pipeline/
├── data/
│   ├── raw/                    # Dữ liệu PaySim ban đầu
│   ├── processed/              # Dữ liệu sau khi tiền xử lý
│   └── graph/                  # Dữ liệu node, edge hoặc graph đã xây dựng
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   └── 03_graph_analysis.ipynb
├── src/
│   ├── data_ingestion/         # Đọc và tiếp nhận dữ liệu
│   ├── preprocessing/           # Làm sạch và biến đổi dữ liệu
│   ├── graph/                   # Xây dựng và phân tích đồ thị
│   ├── database/                # Kết nối và thao tác với MySQL
│   └── utils/                   # Các hàm tiện ích dùng chung
├── dags/
│   └── aml_pipeline_dag.py      # DAG điều phối pipeline bằng Airflow
├── api/
│   ├── app.py                   # Flask application
│   ├── routes/                  # Các API route
│   └── services/                # Logic phục vụ API
├── requirements.txt              # Danh sách thư viện Python
├── .env.example                  # Mẫu biến môi trường
└── README.md                     # Tài liệu dự án
```

> Cấu trúc có thể được mở rộng tùy theo cách triển khai pipeline, môi trường AWS và nhu cầu phân tích thực tế.

## 4. Hướng dẫn cài đặt

### Yêu cầu hệ thống

- Python **3.9 trở lên**
- Git
- MySQL nếu chạy pipeline với cơ sở dữ liệu cục bộ
- Apache Airflow nếu muốn chạy pipeline theo lịch

### Bước 1: Clone repository

```bash
git clone https://github.com/Hungthang1234/aml-network-graph-pipeline.git
cd aml-network-graph-pipeline
```

### Bước 2: Tạo virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Bước 3: Cài đặt dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Bước 4: Cấu hình biến môi trường

Sao chép file cấu hình mẫu và cập nhật các thông tin kết nối tương ứng:

```bash
cp .env.example .env
```

Trên Windows PowerShell, có thể sử dụng:

```powershell
Copy-Item .env.example .env
```

Các biến môi trường thường bao gồm thông tin kết nối MySQL, AWS S3/RDS và cấu hình Flask. Không commit các thông tin nhạy cảm như mật khẩu, access key hoặc secret key lên repository.

### Bước 5: Chuẩn bị dữ liệu

Tải bộ dữ liệu PaySim từ Kaggle và đặt dữ liệu thô vào thư mục:

```text
data/raw/
```

Sau đó, chạy các bước tiền xử lý và xây dựng đồ thị theo notebook hoặc module tương ứng trong thư mục `src/`.

## 5. Chạy ứng dụng

### Chạy Flask API

```bash
flask --app api.app run --debug
```

API mặc định thường được chạy tại `http://127.0.0.1:5000`.

### Chạy Apache Airflow

Sau khi đã cài đặt và cấu hình Airflow, đặt DAG vào thư mục DAGs của Airflow, sau đó bật DAG `aml_pipeline_dag` từ Airflow UI hoặc CLI.

```bash
airflow dags list
airflow dags trigger aml_pipeline_dag
```

## 6. Định hướng phát triển

- Bổ sung các thuật toán phát hiện bất thường và chấm điểm rủi ro tài khoản.
- Tích hợp các chỉ số đồ thị như degree centrality, betweenness centrality và community detection.
- Xây dựng dashboard Power BI theo dõi các chỉ số AML.
- Triển khai pipeline và API trên AWS với cơ chế logging, monitoring và phân quyền phù hợp.
- Bổ sung kiểm thử tự động cho các module xử lý dữ liệu, đồ thị và API.

## 7. Lưu ý

Dữ liệu và kết quả phân tích trong dự án phục vụ mục đích nghiên cứu, học tập và xây dựng nguyên mẫu. Khi triển khai trong môi trường thực tế, cần bổ sung các yêu cầu về bảo mật dữ liệu, quyền riêng tư, kiểm soát truy cập và tuân thủ quy định pháp lý liên quan đến phòng chống rửa tiền.
