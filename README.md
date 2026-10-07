# カルマンフィルタ

線形の状態空間モデルで観測系列をフィルタリングし、予測と実測を比較します。

状態と観測のメモは [KF/readme.md](KF/readme.md) にあります。

## ディレクトリ

コードは `KF/` にあります。

| パス | 内容 |
| --- | --- |
| `KF/src/model.py` | 予測ステップと更新ステップ |
| `KF/src/predict.py` | 系列全体への適用 |
| `KF/src/evaluate.py` | 予測と実測のプロット |
| `KF/config.toml` | 初期状態、遷移行列 `A`、観測行列 `H`、ノイズ共分散 `Q` と `R` |
| `KF/data/kalman_filter_dummy_state_space.csv` | ダミーの観測系列 |

## 実行

```bash
pip install numpy pandas matplotlib
cd KF
PYTHONPATH=src python src/evaluate.py
```

図は `output/predict vs acutual.png` に保存されます。
