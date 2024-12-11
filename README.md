# Discord Botを作成してみる

EC2のインスタンスを落としたかどうか、6時間ごとに通知を送るBotを作成してみる。

## Versions

- conda 24.3.0
- Python: 3.12.7

## 動作確認

```sh
$ python hello_bot.py
```

![alt text](imgs/hello.png)

## Taskfileの導入

```sh
$ brew install go-task
```

### Conda環境の保存

```sh
$ task export-conda-env
```

### 既存のConda環境の更新

```sh
$ task update-conda-env
```

### Conda環境の作成

```sh
$ task create-conda-env
```

## Ref

- https://zenn.dev/remew/articles/introduce-taskfile
