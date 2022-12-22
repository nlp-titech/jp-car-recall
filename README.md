# Japanese Car Recall Corpus

Japanese Car Recall Corpus is car recall report text data annotated with types of annotation: 1) car parts and 2) causality. This is the first corpus annotating both these two information on the car recall text. As a malfunction of a vehicle is related to corresponding parts, we annotate both information to explore how the domain knowledge of vehicle parts can help causality extraction.


## Two types of annoation

### Car part annotation
![alt text](images/part_ann_example.jpg)
For car part annoation, we annoate vehicle parts as entities and the relations between parts as relations.

### Causality annotation
![alt text](images/causal_ann_example.jpg)

For car part annoation, we annoate malfunctions and their causes.

## Data Format

We annotated data with [brat](https://brat.nlplab.org/). Every annotation document is composed of a foo.txt file and a foo.ann file. Here are the examples of a `foo.txt` and `foo.ann`.

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


## Corpus discription and citation

For more detailed description of the corpus, please refer `paper.pdf` in this repo.
If you use this corpus in your project, please cite as
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
## License [![CC BY 4.0](http://mirrors.creativecommons.org/presskit/buttons/80x15/svg/by.svg)](http://creativecommons.org/licenses/by/4.0/)

All content in this repository is licensed under the [Creative Commons - Attribution 4.0 International (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/) license.
