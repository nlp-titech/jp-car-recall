# 自動車リコールコーパス

[![en](https://img.shields.io/badge/lang-en-red)](https://github.com/nlp-titech/jp-car-recall#readme)
[![jp](https://img.shields.io/badge/lang-jp-blue)](https://github.com/nlp-titech/jp-car-recall/blob/main/README.jp.md)

自動車リコールコーパスは、自動車リコール報告書のテキストデータに、1)自動車の部品、2)因果関係のアノテーションを付与したものである。このコーパスは、自動車のリコール報告テキストにこの2つの情報をアノテーションした初めてのコーパスである。自動車の故障は部品と関連しているため、部品に関する知識が因果関係の抽出にどのように役立つかを調べるために、両方の情報をアノテーションしている。

## データと2種類のアノテーション

[国土交通省のサイト](https://www.mlit.go.jp/jidosha/carinf/rcl/index.html)からリコールテキストデータを収集した。

### 自動車部品アノテーション

![alt text](images/part_ann_example.jpg)
自動車部品のアノテーションでは、自動車部品をentity、部品間の関係をrelationとしてアノテーションしている。

### 因果関係アノテーション

![alt text](images/causal_ann_example.jpg)

因果関係のアノテーションでは、不具合とその原因をアノテーションしている。

## データフォーマット

データには[brat](https://brat.nlplab.org/)でアノテーションをつける。アノテーション文書は以下の例で示す`foo.txt`と`foo.ann`と同様のフォーマットのファイルで構成される。

`foo.txt`
```
後部反射器において、車体への取付が不適切なため、そのままの状態で使用を続けると、走行時の車体の振動により当該反射器が脱落するおそれがある。
```

`foo.ann`
```T1	Argument 0 20	後部反射器において、車体への取付が不適切
T2	Argument 40 49	走行時の車体の振動
T3	Argument 52 60	当該反射器が脱落
T4	Connective 21 23	ため
T5	Connective 49 52	により
R1	REASON Arg1:T4 Arg2:T1	
R2	RESULT Arg1:T4 Arg2:T3	
R3	REASON Arg1:T5 Arg2:T2	
R4	RESULT Arg1:T5 Arg2:T3	
T6	Argument 24 38	そのままの状態で使用を続ける
T7	Connective 38 39	と
R5	CONDITION Arg1:T7 Arg2:T6	
R6	RESULT Arg1:T7 Arg2:T3	
```


## コーパスの説明と引用

コーパスの詳細については、このレポジトリにある `paper.pdf` を参照してください。
このコーパスを研究・プロジェクトで使用する場合は、以下のように引用してください。
> Hsuan-Yu Kuo, Youmi Ma, and Naoaki Okazaki. Annotating Entity and Causal Relationships on Japanese Vehicle Recall Information. In Proceedings of the 36th Pacific Asia Conference on Language, Information and Computation (PACLIC), pages (to appear), October 2022.

Or

```
@inproceedings{Kuo:PACLIC2023,
    title = "Annotating Entity and Causal Relationships on Japanese Vehicle Recall Information",
    author = "Kuo, Hsuan-Yu and
              Ma, Youmi and 
              Okazaki, Naoaki ",
    booktitle = "Proceedings of the 36th annual Meeting of Pacific Asia Conference on Language, Information and Computation (PACLIC 36)",
    month = october,
    year = "2022",
}
```

---
## ライセンス [![CC BY 4.0](http://mirrors.creativecommons.org/presskit/buttons/80x15/svg/by.svg)](http://creativecommons.org/licenses/by/4.0/)

このレポジトリのすべてのコンテンツが [Creative Commons - Attribution 4.0 International (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/) のライセンスに準拠します。
