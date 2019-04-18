# Pipeline

raw data -> SQL -> T transformer-> SI string indexer -> 1HE hot encoder -> VA vector assembler -> processed data

Pipeline encapsulate the process/
```
filterer

extractor

indexer

encoder

assembler

classifier

grid

evaluator: MulticlassClassificationEvaluator

validator: TrainValidationSplit(estimator=classifier, parammaps=grid, evaluator=..

stages = [filterer, extractor, indexer, encoder, assembler, validator]
pipeline = Pipline(stages)

--

RFormula = (SI, 1HE, VA)

Pipeline(SQL, SQL, RFormula)


```
