config = {
  "language": "en",
  "pipeline":[
    {
      "name": "WhitespaceTokenizer"
    },
    {
      "name": "RegexFeaturizer"
    },
    {
      "name": "LexicalSyntacticFeaturizer"
    },
    {
      "name": "CountVectorsFeaturizer"
    },
    {
      "name": "CountVectorsFeaturizer",
      "analyzer": "char_wb",
      "min_ngram": 1,
      "max_ngram": 4
    },
    {
      "name": "DIETClassifier",
      "epochs": 100,
      "constrain_similarities": True
    },
    {
        "name": "EntitySynonymMapper"
    },
    {
      "name": "ResponseSelector",
      "epochs": 100,
      "constrain_similarities": True
    },
    {
      "name": "FallbackClassifier",
      "threshold": 0.3,
      "ambiguity_threshold": 0.1
    }
  ],
  "policies":[
    {
      "name": "MemoizationPolicy"
    },
    {
      "name": "RulePolicy"
    },
    {
      "name": "UnexpecTEDIntentPolicy",
      "max_history": 5,
      "epochs": 100,
    },
    {
      "name": "TEDPolicy",
      "max_history": 5,
      "epochs": 100,
      "constrain_similarities": True
    }
  ]
}
