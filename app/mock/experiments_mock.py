EXPERIMENTS_MOCK = [
    {
        "experiment_id": 101,
        "project_id": 1,
        "name": "Prueba 2 capas ocultas 100 épocas GPU",
        "status": "COMPLETED",
        "resources": {
            "cpus": 8,
            "memory": "16G",
            "gpu": True
        },
        "dataset": "imagenet_subset.zip",
        "code": "train_v1.py",
        "created_at": "2026-02-01",
        "job_id": 1003
    },
    {
        "experiment_id": 102,
        "project_id": 2,
        "name": "LSTM 50 épocas CPU",
        "status": "RUNNING",
        "resources": {
            "cpus": 4,
            "memory": "8G",
            "gpu": False
        },
        "dataset": "traffic_data.csv",
        "code": "lstm_model.py",
        "created_at": "2026-03-10",
        "job_id": 1001
    },
    {
        "experiment_id": 103,
        "project_id": 2,
        "name": "LSTM 100 épocas GPU",
        "status": "PENDING",
        "resources": {
            "cpus": 8,
            "memory": "16G",
            "gpu": True
        },
        "dataset": "traffic_data.csv",
        "code": "lstm_model_v2.py",
        "created_at": "2026-03-11",
        "job_id": 1002
    },
    {
        "experiment_id": 104,
        "project_id": 2,
        "name": "Transformer 50 épocas GPU",
        "status": "PENDING",
        "resources": {
            "cpus": 16,
            "memory": "32G",
            "gpu": True
        },
        "dataset": "traffic_data.csv",
        "code": "transformer_model.py",
        "created_at": "2026-03-12",
        "job_id": None
    }
]