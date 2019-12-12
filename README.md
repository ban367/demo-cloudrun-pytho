# demo-cloudrun-python

Cloud Run(GCP)のPython用クイックスタート

## Command

### Deploy

コンテナのデプロイ

```sh
gcloud builds submit --tag gcr.io/[PROJECT-ID]/[PROJECT-NAME]
```

Cloud Runのデプロイ

```sh
gcloud run deploy --image gcr.io/[PROJECT-ID]/[PROJECT-NAME] --platform managed
```

### Delete

コンテナを削除

```sh
gcloud container images delete gcr.io/[PROJECT-ID]/[PROJECT-NAME]
```

Cloud Runを削除

```sh
gcloud run services delete gcr.io/[PROJECT-ID]/[PROJECT-NAME]
```
