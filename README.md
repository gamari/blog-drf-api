# 概要

ブログ用のAPI。


## コンテナ

- docker-compose.yml
    - 本番環境
- docker-compose-local.yml
    - 開発環境



## 本番での実行手順

- [ ] TODO検証中

docker-compose -f docker-compose-production.yml build
docker-compose -f docker-compose-production.yml up -d