# GBF ノルマ自動算出ツール

## 動作環境

- OS問わず(確認済みWindows10 64bit)
- Python >= 3.8

## 導入手順

- Pythonのインストール

    - ここからダウンロード (https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe)
    - インストーラが起動したら `Add Python3.9 to PATH` にチェックを入れる
    
        ![1](https://user-images.githubusercontent.com/27270665/176100923-1800dff5-db80-49d8-9162-60b9b13b71ef.PNG)

    - インストールを実施

- モジュールのインストール

    - `install.bat` をダブルクリック
    
        ![0](https://user-images.githubusercontent.com/27270665/176104068-e5a967a0-bd6a-4029-9b86-8bee39645aed.PNG)

## 使用方法

- グラブルの貢献度ページのHTMLを保存する

    - F12を押下し、開発者ツールを起動
    
        ![2](https://user-images.githubusercontent.com/27270665/176100972-af8c57b9-76b6-4c3c-b7a4-1a79e2f92aa9.PNG)

    - 先頭の `<html lang=` の行を選択し、HTMLとして編集を押下
    
        ![3](https://user-images.githubusercontent.com/27270665/176101139-eafb322d-aba0-4045-bb9f-d479bc5b4f9a.png)

    - HTMLが開いたら `Ctrl+a` で全体を選択し `Ctrl+c` と `Ctrl+p` でファイルとして保存
    
        ![4](https://user-images.githubusercontent.com/27270665/176101346-1b5b94c2-89f3-48f5-913e-5eaa06e6c513.PNG)

    - 適当な名前で `ContributionHTMLs` に保存する
    
        ![5](https://user-images.githubusercontent.com/27270665/176101600-47df30f2-9f7c-4efd-ba14-3675a37d4589.PNG)

    - これを貢献度ページの3ページ分全て別々に保存する
    
- ツールを実行する
    - `execution.bat` をダブルクリック
    
        ![6](https://user-images.githubusercontent.com/27270665/176104245-cd29a5c0-cb3f-4f58-a22c-f0b1c746a36c.PNG)      
    
    - 実行されると同フォルダに `GBFNorma.tsv` が出力される

        ![7](https://user-images.githubusercontent.com/27270665/176104443-6017ec80-02c4-42e3-b296-4a4dbdd2d7a9.PNG)

    - 内容を確認すると貢献度一覧とノルマが確認できる
    
        ```tsv
        "GN"	"本戦開始時貢献度"	"ノルマ貢献度"
        "グラン1"	"2,015,128,927"	"2,415,128,927"
        "グラン2"	"2,000,510,418"	"2,400,510,418"
        "グラン3"	"1,905,341,758"	"2,305,341,758"
        "グラン4"	"1,864,126,148"	"2,264,126,148"
        "ジータ1"	"1,793,964,626"	"2,193,964,626"
        "ジータ1"	"1,780,829,479"	"2,180,829,479"
        "ジータ1"	"1,745,883,720"	"2,145,883,720"
        "ジータ1"	"1,719,913,540"	"2,119,913,540"
        ```
        
    - TSVのためエクセルやスプレッドシートに直接コピペが可能
        
## ノルマの変更方法

- `NormaExporter.py` を開き、下記を編集する (デフォルトでは4億)

  ```python
  # 本戦ノルマの指定
  NORMA = 400000000
  ```
