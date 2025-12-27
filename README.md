Problem Statement;

Automatically classify support tickets into departments (Account, Technical,Billing,Shipping,Other)

Why this matters;
Efficient ticket routing improves response times and customer satisfaction.

DataSet Documentation:

Dataset Source: 'https://www.kaggle.com/datasets/parthpatil256/it-support-ticket-data'
Total samples: 66330
Number of classes : 5 (Account, Technical, Billing, Shipping, Other)
Target columns : 'Department'
Text columns : Body,
label mapping logic:

technical support = technical 
billing and payments = billing 
product support = Account 
It support = technical  
customer service = other 
human resources = other 
general inquiry = other 
Service Outages and Maintenance = technical 
sales and pre-sales = other 
returns and exchanges = Account
Import to Note:
Return and exchange were mapped to Account because they involve user account-level actions rather than payment processing

Known issues;
Class imbalance: Technical and Other categories dominate the dataset, while Billing and Shipping have fewer samples.
"Other" is catch-all category,
Multi-intent tickets exists

Baseline Model Description:
Baseline model: TF-iDF + Linear SVC
Why chosen: Strong baseline for text classification tasks
Performance: Achieved 68 accuracy on validation set

ngram Range: (1,2)
min df: 5
max df: 0.8

Evaluation Metrics 

Train/Test split: 80/20 (stratified)
Metric used: Macro F1
Baseline result:
Macro F1 ≈ 0.68
Observations:
High confusion between Account ↔ Technical
“Other” absorbs ambiguous tickets

Error Analysis:
Error analysis revealed that most misclassifications occur between semantically overlapping classes such as Account and Technical Support, indicating limitations of bag-of-words representations in capturing context.

Why this Baseline Exists:
This baseline serves as a reference point for evaluting whether more complex models (e.g, Neural Networks, transformers) can significantly outperform traditional Ml techniques on this task.