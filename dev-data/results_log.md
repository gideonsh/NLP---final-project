# SQuAD 2.0 Trials Log

This file tracks all trial runs to monitor improvements and avoid over-correction.

---

## full_data_set_202602170639
**Timestamp:** 2026-02-17 06:39:12

**Dataset:** dev-data/full_data_set-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 55.20 |
| **Overall F1** | 61.41 |
| **NoAns Accuracy** | 58.49% (286/489) |
| **HasAns F1** | 64.21 |
| **HasAns EM** | 52.05 |
| **Total Questions** | 1000 (HasAns: 511, NoAns: 489) |
| **Binary Classification** | 71.20% (712/1000) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Margin | Status |
|-------|----------|---------------|------------------|--------|--------|
| 0 | Who did Alexander I marry? | Sybilla of Normandy | Sybilla of Normandy | -0.0256 | ✅ |
| 1 | What culture's arrival in Scotland is know as the ... | Norman | Normans | -0.8032 | ❌ |
| 2 | Who did King David I of Scotland Marry? | NO ANSWER | Sybilla of Normandy | -0.4035 | ❌ |
| 3 | What did Sybilla of Normandy introduce to Scotland... | NO ANSWER | Normans | -0.2908 | ❌ |
| 4 | Where was Ralph earl of? | Hereford | Hereford | 0.0000 | ✅ |
| 5 | Who was Ralph in charge of being at war with? | the Welsh | Welsh | 0.0000 | ❌ |
| 6 | Who made Ralph earl? | Edward the Confessor | Edward the Confessor | 0.0000 | ✅ |
| 7 | Who came into contact with Wales after the conques... | NO ANSWER | NO ANSWER | 0.2437 | ✅ |
| 8 | Who made Edward the Confessor Earl? | NO ANSWER | Edward the Confessor | 0.0000 | ❌ |
| 9 | What country was under the control of Norman baron... | Wales | Wales | 0.0027 | ✅ |
| 10 | What came under Williams dominace before the conqu... | NO ANSWER | NO ANSWER | 0.0445 | ✅ |
| 11 | What Welsh lords did William conquer? | NO ANSWER | NO ANSWER | 0.2859 | ✅ |
| 12 | What year did Roger de Tosny fail to accomplish wh... | 1018 | 1018 | -1.0000 | ✅ |
| 13 | Who was in charge of the papal army in the War of ... | William of Montreuil | William of Montreuil | 0.0000 | ✅ |
| 14 | Where did the Normans carve out a principality bef... | NO ANSWER | NO ANSWER | 0.1014 | ✅ |
| 15 | What did the Normans take part in in the 10th cent... | NO ANSWER | Reconquista in Iberia | -0.4537 | ❌ |
| 16 | Who carved out a state for himself from Moorish la... | NO ANSWER | Roger de Tosny | 0.0000 | ❌ |
| 17 | What war occured in the 1oth century? | NO ANSWER | NO 1018 | -0.0912 | ❌ |
| 18 | When did the Siege of Antioch take place? | 1097 | 1097 | -0.9491 | ✅ |
| 19 | What was the name of Bohemond's nephew? | Tancred | Tancred | 0.0000 | ✅ |
| 20 | What major conquest did Tancred play a roll in? | Jerusalem | Jer Jerusalem | 0.0000 | ❌ |
| 21 | When did Tancred lay siege to Antioch? | NO ANSWER | NO ANSWER | 0.8218 | ✅ |
| 22 | What was the name of Tancred's nephew? | NO ANSWER | Boemond of Taranto | 0.0000 | ❌ |
| 23 | How long did Western Europe control Cyprus? | 380 years | 380 years | -1.0000 | ✅ |
| 24 | Who defeated Anglo-Norman forces during the third ... | NO ANSWER | NO ANSWER | 0.9600 | ✅ |
| 25 | Who dominated Western Europe for 380 years? | NO ANSWER | Western European | -0.1995 | ❌ |
| 26 | What ruined Richard's plans to reach Acre? | a storm | storm | 0.0000 | ❌ |
| 27 | Who was Richard's fiancee? | Berengaria | Berengaria | 0.0000 | ✅ |
| 28 | What year did the storm hit Richard's fleet? | 1191 | 1191 | -0.0712 | ✅ |
| 29 | Who ruled Cyprus in 1191? | Isaac Komnenos | Is Isaac Komnenos | 0.0000 | ❌ |
| 30 | Who left Messina in the 11th century? | NO ANSWER | NO ANSWER | 0.2906 | ✅ |
| 31 | What year did Richards fleet avoid a storm? | NO ANSWER | April 1191 | -0.5485 | ❌ |
| 32 | Who ruled Cyprus in the 11th century? | NO ANSWER | NO ANSWER | 0.0941 | ✅ |
| 33 | Who was Guy's Rival? | Conrad of Montferrat | Con Conrad of Montferrat | 0.0000 | ❌ |
| 34 | What were Isaac's chains made out of? | silver | NO ANSWER | 0.0113 | ❌ |
| 35 | Who led Richard's troops when Cyprus was conquered... | Guy de Lusignan | Guy de Lusignan | 0.0000 | ✅ |
| 36 | Who's chains were made out of copper? | NO ANSWER | NO ANSWER | 0.8322 | ✅ |
| 37 | Who led Issacs troops to Cyprus? | NO ANSWER | NO ANSWER | 0.1870 | ✅ |
| 38 | Who offered Issac his daughter? | NO ANSWER | Richard | 0.0000 | ❌ |
| 39 | Who became the King of the Canary Islands? | Bethencourt | Henry III of Castile | -0.1700 | ❌ |
| 40 | Who bought the rights? | Enrique Pérez de Guzmán | En Enrique Pérez de Guzmán, 2nd Count | 0.0000 | ❌ |
| 41 | Who sold the rights? | Maciot de Bethencourt | Maciot de Bethencourt | 0.0000 | ✅ |
| 42 | What title did Henry II take in the Canary Island? | NO ANSWER | NO ANSWER | 0.1454 | ✅ |
| 43 | Who sold the rights to the island in the 14th cent... | NO ANSWER | Maciot de Bethencourt | 0.0000 | ❌ |
| 44 | Where are Jersey and Guernsey | Channel Islands | Jersey and Guernsey | -0.4108 | ❌ |
| 45 | How many customaries does Norman customary law hav... | two | Two | 0.0000 | ✅ |
| 46 | What Norman law wasdeveloped between 1000 and 1300... | NO ANSWER | NO ANSWER | 0.1701 | ✅ |
| 47 | What law has 3 customeries? | NO ANSWER | NO ANSWER | 0.3295 | ✅ |
| 48 | What was authored in the 12th century? | NO ANSWER | Très ancien coutumier | -0.3229 | ❌ |
| 49 | What is the Norman architecture idiom? | Romanesque | Romanesque | 0.0000 | ✅ |
| 50 | What kind of arches does Norman architecture have? | rounded | rounded arches | 0.0000 | ❌ |
| 51 | What type of arch did the Normans invent? | NO ANSWER | NO ANSWER | 0.2659 | ✅ |
| 52 | What architecture type came after Norman in Englan... | Early Gothic | Early Gothic | 0.0000 | ✅ |
| 53 | What architecture type came before Norman in Engla... | Anglo-Saxon | Ang Anglo-Saxon | 0.0000 | ❌ |
| 54 | What place had the Norman Arab architectural style... | Sicily | Kingdom of Sicily | 0.0000 | ❌ |
| 55 | What precedes the period of Anglo-Saxon architectu... | NO ANSWER | NO ANSWER | 0.1162 | ✅ |
| 56 | What architecture type came after Early Gothic? | NO ANSWER | NO ANSWER | 0.0496 | ✅ |
| 57 | Who incorperated Islamic, LOmbard, and Byzantine b... | NO ANSWER | NO ANSWER | 0.7090 | ✅ |
| 58 | When did the church reform begin? | early 11th century | In the early 11th century | -0.3740 | ❌ |
| 59 | Who used the church to unify themselves? | dukes | dukes of Normandy | 0.0000 | ❌ |
| 60 | What kind of art did the Normans have a rich tradi... | NO ANSWER | NO ANSWER | 0.4358 | ✅ |
| 61 | Who began a program of church reform in the 1100s | NO ANSWER | dukes of Normandy | 0.0000 | ❌ |
| 62 | Who was divided by the church? | NO ANSWER | NO ANSWER | 0.0294 | ✅ |
| 63 | Who experienced aa golden age in the 1100s and 120... | NO ANSWER | Normandy | 0.0000 | ❌ |
| 64 | When were the French wars of religion? | 16th century | 16th century | -0.9252 | ✅ |
| 65 | What wars did France fight in the 1600s? | NO ANSWER | French Wars of Religion | -0.3122 | ❌ |
| 66 | What revolution was fought in the 1899's? | NO ANSWER | NO ANSWER | 0.5570 | ✅ |
| 67 | What kind of needlework was used in the creation o... | embroidery | emb embroidery | 0.0000 | ❌ |
| 68 | What is Norman art's most well known piece? | Bayeux Tapestry | Bayeux Tapestry | 0.0000 | ✅ |
| 69 | Who commissioned the Tapestry? | Odo | Odo, the Bishop of Bayeux and first Earl of | 0.0000 | ❌ |
| 70 | What is the oldest work of Norman art? | NO ANSWER | NO ANSWER | 0.4652 | ✅ |
| 71 | Who commissioned Danish vikings to create the Baye... | NO ANSWER | Odo, the Bishop of Bayeux and first Earl of | 0.0000 | ❌ |
| 72 | In what century did important classical music deve... | 11th | 11th century | -0.5570 | ❌ |
| 73 | Who were the two abbots at Fécamp Abbey? | William of Volpiano and John of Ravenna | William of Volpiano and John of Ravenna | 0.0000 | ✅ |
| 74 | What developed in Normandy during the 1100s? | NO ANSWER | mus musical production and education | -0.0073 | ❌ |
| 75 | What was Fecamp Abby the center of? | NO ANSWER | Mus musical production and education | -0.0334 | ❌ |
| 76 | Where did the monks flee to? | southern Italy | Southern Italy | 0.0000 | ✅ |
| 77 | What monastery did the Saint-Evroul monks establis... | Latin monastery at Sant'Eufemia. | Sant'Eufemia | 0.0000 | ❌ |
| 78 | Who patronized the monks in Italy?  | Robert Guiscard | Robert Guiscard | 0.0000 | ✅ |
| 79 | What tradition were the Saint-Evroul monks known f... | singing | singing | -0.0246 | ✅ |
| 80 | Who fled from southern Italy? | NO ANSWER | Mon monks of Saint-Evroul | 0.0000 | ❌ |
| 81 | What branch of theoretical computer science deals ... | Computational complexity theory | Computational complexity theory | -0.8775 | ✅ |
| 82 | By what main attribute are computational problems ... | inherent difficulty | their inherent difficulty | -0.1435 | ❌ |
| 83 | What is the term for a task that generally lends i... | computational problems | computational problem | -0.1344 | ❌ |
| 84 | What is computational complexity principle? | NO ANSWER | NO ANSWER | 0.0826 | ✅ |
| 85 | What branch of theoretical computer class deals wi... | NO ANSWER | Computational complexity theory | -0.8574 | ❌ |
| 86 | What is understood to be a task that is in princip... | NO ANSWER | NO ANSWER | 0.5055 | ✅ |
| 87 |  What cannot be solved by mechanical application o... | NO ANSWER | NO ANSWER | 0.6577 | ✅ |
| 88 | What is a manual application of mathematical steps... | NO ANSWER | Manual application of mathematical steps is an algorithm | 0.0000 | ❌ |
| 89 | What measure of a computational problem broadly de... | if its solution requires significant resources | NO ANSWER | 0.0508 | ❌ |
| 90 | What method is used to intuitively assess or quant... | mathematical models of computation | Comput computational complexity | -0.0237 | ❌ |
| 91 | What are two basic primary resources used to guage... | time and storage | NO ANSWER | 0.0191 | ❌ |
| 92 | What unit is measured to determine circuit complex... | number of gates in a circuit | number of gates in a circuit | 0.0000 | ✅ |
| 93 | What practical role does defining the complexity o... | determine the practical limits on what computers can and cannot do | NO ANSWER | 0.0622 | ❌ |
| 94 | What measure of computational problem broadly defi... | NO ANSWER | NO ANSWER | 0.3871 | ✅ |
| 95 | What method is not used to intuitively assess or q... | NO ANSWER | NO ANSWER | 0.1315 | ✅ |
| 96 | What are three basic primary resources used to gau... | NO ANSWER | NO ANSWER | 0.0181 | ✅ |
| 97 | What unit is measured to determine circuit simplic... | NO ANSWER | number of gates in a circuit | -0.0359 | ❌ |
| 98 | What number is used in perpendicular computing? | NO ANSWER | NO ANSWER | 0.2856 | ✅ |
| 99 | What two fields of theoretical computer science cl... | analysis of algorithms and computability theory | analysis of algorithms and computability theory | -0.0201 | ✅ |
| 100 | What field of computer science analyzes the resour... | analysis of algorithms | Analysis of algorithms | 0.0000 | ✅ |
| 101 | What field of computer science analyzes all possib... | computational complexity theory | NO ANSWER | 0.0231 | ❌ |
| 102 | What field of computer science is primarily concer... | computability theory | NO ANSWER | 0.0265 | ❌ |
| 103 | What are two fields of theoretical computer scienc... | NO ANSWER | NO ANSWER | 0.1503 | ✅ |
| 104 | What is not the key distinction between analysis o... | NO ANSWER | NO ANSWER | 0.1577 | ✅ |
| 105 | What is the process of analyzing the amount of res... | NO ANSWER | NO ANSWER | 0.2307 | ✅ |
| 106 | What is the process that asks a more specific ques... | NO ANSWER | analysis of algorithms | -0.0117 | ❌ |
| 107 | What process classifies problems that can and cann... | NO ANSWER | NO ANSWER | 0.0708 | ✅ |
| 108 | What is the name given to the input string of a co... | problem instance | problem instance | -0.0940 | ✅ |
| 109 | In computational complexity theory, what is the te... | the problem | problem | -0.2875 | ❌ |
| 110 | Is a problem instance typically characterized as a... | concrete | con concrete | -0.0419 | ❌ |
| 111 | What is another name for any given measure of inpu... | instances | Instance | -0.0187 | ❌ |
| 112 | What is the general term used to describe the outp... | solution | output | 0.0000 | ❌ |
| 113 | What can be viewed as a limited collection of inst... | NO ANSWER | instance | -0.5453 | ❌ |
| 114 | What is the name given to the input string of a co... | NO ANSWER | instance | -0.0536 | ❌ |
| 115 | What term refers to the concrete question to be so... | NO ANSWER | problem | -0.3447 | ❌ |
| 116 | What is the output corresponding to the given ques... | NO ANSWER | NO ANSWER | 0.1833 | ✅ |
| 117 | What is a particular measure input associated with... | NO ANSWER | NO ANSWER | 0.1016 | ✅ |
| 118 | By how many kilometers does the traveling salesman... | 2000 | 2000 | -0.8185 | ✅ |
| 119 | What is one example of an instance that the quanti... | round trip through all sites in Milan | Is there a route of at most 2000 kilometres passing through | -0.0016 | ❌ |
| 120 | What does computational complexity theory most spe... | computational problems | comput computational problems | 0.0091 | ❌ |
| 121 | How many miles does the traveling salesman problem... | NO ANSWER | NO ANSWER | 0.4925 | ✅ |
| 122 | What is the qualitative answer to this particular ... | NO ANSWER | NO ANSWER | 0.1641 | ✅ |
| 123 | What is one example of an instance that the qualit... | NO ANSWER | What is a route of at most 2000 kilometres passing through | 0.0078 | ❌ |
| 124 | What does computational simplicity theory most spe... | NO ANSWER | NO ANSWER | 0.0230 | ✅ |
| 125 | In a computational problem, what can be described ... | problem instance | string | -0.0213 | ❌ |
| 126 | What is the name of the alphabet is most commonly ... | binary alphabet | NO ANSWER | 0.0354 | ❌ |
| 127 | What is another term for the string of a problem i... | bitstrings | string | 0.0000 | ❌ |
| 128 | In the encoding of mathematical objects, what is t... | binary notation | They are represented in binary notation | 0.0000 | ❌ |
| 129 | What is one way in which graphs can be encoded?  | adjacency matrices | They can be encoded directly via their adjacency matrices | -0.0191 | ❌ |
| 130 | What is a string over a Greek number when consider... | NO ANSWER | NO ANSWER | 0.1428 | ✅ |
| 131 | What is the name of the alphabet that is rarely us... | NO ANSWER | NO ANSWER | 0.2532 | ✅ |
| 132 | What is another term for the the string of a probl... | NO ANSWER | NO ANSWER | 0.0310 | ✅ |
| 133 | What is represented by non-binary notation in the ... | NO ANSWER | NO ANSWER | 0.0348 | ✅ |
| 134 | How can graphs be encoded indirectly? | NO ANSWER | Ind directly via their adjacency lists in binary | -0.0113 | ❌ |
| 135 | What kind of problems are one of the main topics s... | Decision problems | Decision problems | -0.6945 | ✅ |
| 136 | What are the two simple word responses to a decisi... | yes or no | NO ANSWER | -0.0025 | ❌ |
| 137 | What are the two integer responses to a decision p... | 1 or 0 | 0 and 1 | -0.3573 | ❌ |
| 138 | What will the output be for a member of the langua... | yes | yes | 0.0000 | ✅ |
| 139 | What answer denotes that an algorithm has accepted... | yes | YES | 0.0000 | ✅ |
| 140 | What kind of solutions are one of the central obje... | NO ANSWER | Decision problems | -0.5969 | ❌ |
| 141 | What is a typical type of computational problem wh... | NO ANSWER | decision problem | -0.3925 | ❌ |
| 142 | What can be viewed as an informal language where t... | NO ANSWER | NO ANSWER | 0.0287 | ✅ |
| 143 | What are the three integer responses to a decision... | NO ANSWER | 1, 0, or yes | -0.1285 | ❌ |
| 144 | What answer denotes that a solution has accepted a... | NO ANSWER | yes | 0.0000 | ❌ |
| 145 | What kind of graph is an example of an input used ... | arbitrary graph | arbitrary graph | -0.5024 | ✅ |
| 146 | What is the term for the set of all connected grap... | formal language | NO ANSWER | 0.0715 | ❌ |
| 147 | What encoding decision needs to be made in order t... | how graphs are encoded as binary strings | NO ANSWER | 0.2331 | ❌ |
| 148 | What type of graph is an example of an output used... | NO ANSWER | NO ANSWER | 0.1402 | ✅ |
| 149 | What is the term for the set of all unconnected gr... | NO ANSWER | NO ANSWER | 0.2531 | ✅ |
| 150 | What encoding decision needs to be made in order t... | NO ANSWER | NO ANSWER | 0.1641 | ✅ |
| 151 | How does one obtain an indefinite definition of th... | NO ANSWER | NO ANSWER | 0.6579 | ✅ |
| 152 | A function problem is an example of what? | a computational problem | computation | -0.3884 | ❌ |
| 153 | How many outputs are expected for each input in a ... | a single output | NO ANSWER | 0.0115 | ❌ |
| 154 | The traveling salesman problem is an example of wh... | A function problem | function | -0.4062 | ❌ |
| 155 | In addition to the traveling salesman problem, wha... | the integer factorization problem | NO ANSWER | 0.0475 | ❌ |
| 156 | Is the output of a functional problem typically ch... | complex | NO ANSWER | 0.0613 | ❌ |
| 157 | What is a computational solution where a single in... | NO ANSWER | NO ANSWER | 0.1052 | ✅ |
| 158 | What is expected where a computational problems of... | NO ANSWER | NO ANSWER | 0.1420 | ✅ |
| 159 | What is a function solution an example of? | NO ANSWER | computational problem | -0.4210 | ❌ |
| 160 | What are other irrelevant examples of a function p... | NO ANSWER | NO ANSWER | 0.0263 | ✅ |
| 161 | Is the output of a functional solution typically c... | NO ANSWER | NO ANSWER | 0.0592 | ✅ |
| 162 | How can function problems typically be restated? | decision problems | set of triples (a, b, c) such that | -0.0278 | ❌ |
| 163 | If two integers are multiplied and output a value,... | set of triples | Multip set | -0.0174 | ❌ |
| 164 | What can not be restated as decision problems? | NO ANSWER | NO ANSWER | 0.1967 | ✅ |
| 165 | What is the expression set called where three inte... | NO ANSWER | NO ANSWER | 0.0152 | ✅ |
| 166 | What corresponds to solving the problem of multipl... | NO ANSWER | set of triples (a, b, c) such that | -0.0573 | ❌ |
| 167 | What is a commonly used measurement used to determ... | how much time the best algorithm requires to solve the problem | NO ANSWER | 0.0768 | ❌ |
| 168 | What is one variable on which the running time may... | the instance | size of the instance | 0.0000 | ❌ |
| 169 | How is the time needed to obtain the solution to a... | as a function of the size of the instance | NO ANSWER | 0.0299 | ❌ |
| 170 | In what unit is the size of the input measured? | bits | bits | 0.0000 | ✅ |
| 171 | Complexity theory seeks to define the relationship... | an increase in the input size | algorithm | 0.0000 | ❌ |
| 172 | How does one measure the simplicity of a computati... | NO ANSWER | NO ANSWER | 0.4277 | ✅ |
| 173 | What is one variable which the running of time be ... | NO ANSWER | NO ANSWER | 0.0674 | ✅ |
| 174 | How is the time needed to obtain the question to a... | NO ANSWER | NO ANSWER | 0.1569 | ✅ |
| 175 | What is  interested in how algorithms scale with a... | NO ANSWER | NO ANSWER | 0.2431 | ✅ |
| 176 | How is time not required to solve a problem calcul... | NO ANSWER | NO ANSWER | 0.0679 | ✅ |
| 177 | Whose thesis states that the solution to a problem... | Cobham's thesis | Cobham | 0.0000 | ❌ |
| 178 | If input size is is equal to n, what can respectiv... | the time taken | NO ANSWER | 0.1163 | ❌ |
| 179 | What term corresponds to the maximum measurement o... | worst-case time complexity | NO ANSWER | 0.0815 | ❌ |
| 180 | How is worst-case time complexity written as an ex... | T(n) | NO ANSWER | 0.0754 | ❌ |
| 181 | Assuming that T represents a polynomial in T(n), w... | polynomial time algorithm | NO ANSWER | 0.2020 | ❌ |
| 182 | How is time taken expressed as a function of x? | NO ANSWER | NO ANSWER | 0.4403 | ✅ |
| 183 | Whose hypothesis states the the solution to a prob... | NO ANSWER | NO ANSWER | 0.0571 | ✅ |
| 184 | What term corresponds to the minimum measurement o... | NO ANSWER | NO ANSWER | 0.2238 | ✅ |
| 185 | How is best-case time complexity written as an exp... | NO ANSWER | NO ANSWER | 0.2774 | ✅ |
| 186 | What is the term given to the corresponding algori... | NO ANSWER | NO ANSWER | 0.2543 | ✅ |
| 187 | What is the term for a mathematical model that the... | A Turing machine | Turing machine | -1.0000 | ❌ |
| 188 | It is generally assumed that a Turing machine can ... | an algorithm | anything | -0.1649 | ❌ |
| 189 | What is the most commonplace model utilized in com... | the Turing machine | Turing machine | -0.5707 | ❌ |
| 190 | What does a Turing machine handle on a strip of ta... | symbols | Symbols | 0.0000 | ✅ |
| 191 | What a scientific model of a general computing mac... | NO ANSWER | Turing machine | -1.0000 | ❌ |
| 192 | What is a scientific device that manipulates symbo... | NO ANSWER | Turing machine | -1.0000 | ❌ |
| 193 | What are intended as a practical computing technol... | NO ANSWER | NO ANSWER | 0.1275 | ✅ |
| 194 | What is a scientific experiment that can solve a p... | NO ANSWER | Turing machine | -0.5722 | ❌ |
| 195 | What is generally considered to be the most basic ... | A deterministic Turing machine | deterministic Turing machine | -0.4988 | ❌ |
| 196 | What fixed set of factors determine the actions of... | rules | fixed set of rules | -0.4872 | ❌ |
| 197 | What is the term used to identify a deterministic ... | A probabilistic Turing machine | Prob probabilistic | -0.0798 | ❌ |
| 198 | What type of Turing machine is capable of multiple... | A non-deterministic Turing machine | non-deterministic | -0.1577 | ❌ |
| 199 | What is the term given to algorithms that utilize ... | randomized algorithms | randomizable algorithms | 0.0000 | ❌ |
| 200 | What uses a flexible set of rules to determine its... | NO ANSWER | deterministic Turing machine | -0.4708 | ❌ |
| 201 | What is a deterministic Turing machine with an ext... | NO ANSWER | NO ANSWER | 0.8961 | ✅ |
| 202 | What does not often help algorithms solve problems... | NO ANSWER | NO ANSWER | 0.0444 | ✅ |
| 203 | Which machine allows the machine to have multiple ... | NO ANSWER | NO ANSWER | 0.2170 | ✅ |
| 204 | How is one way that one should not view non-determ... | NO ANSWER | Turing machine branches into many possible computational paths at each step | -0.0069 | ❌ |
| 205 | Turing machines are commonly employed to define wh... | complexity classes | complex classes | 0.0000 | ❌ |
| 206 | What are two factors that directly effect how powe... | time or space | Resource (such as time or space) | 0.0000 | ❌ |
| 207 | In the determination of complexity classes, what a... | probabilistic Turing machines, non-deterministic Turing machines | Deterministic Turing machines, probabilistic Turing machines | 0.0092 | ❌ |
| 208 | What are many types of Turing machines not used fo... | NO ANSWER | NO ANSWER | 0.4395 | ✅ |
| 209 | What are three factors that directly effect how po... | NO ANSWER | NO ANSWER | 0.0649 | ✅ |
| 210 | What machines are not equally powerful in principl... | NO ANSWER | NO ANSWER | 0.4284 | ✅ |
| 211 | What may not be more powerful than others when the... | NO ANSWER | NO ANSWER | 0.0719 | ✅ |
| 212 | What is an example of a machine model that deviate... | random access machines | Random access machine | 0.0000 | ❌ |
| 213 | In considering Turing machines and alternate varia... | computational power | NO ANSWER | 0.1707 | ❌ |
| 214 | What two resources commonly consumed by alternate ... | time and memory | time and memory | 0.0000 | ✅ |
| 215 | What commonality do alternate machine models, such... | the machines operate deterministically | NO ANSWER | 0.0137 | ❌ |
| 216 | What is not an example of a machine model that dev... | NO ANSWER | NO ANSWER | 0.3582 | ✅ |
| 217 | What measurement is affected by conversion between... | NO ANSWER | NO ANSWER | 0.0168 | ✅ |
| 218 | What two resources are uncommonly consumed by alte... | NO ANSWER | Time and memory consumption | 0.0000 | ❌ |
| 219 | What do all these models not have in common? | NO ANSWER | NO ANSWER | 0.4994 | ✅ |
| 220 | What type of Turing machine can be characterized b... | non-deterministic | non-deterministic | 0.0000 | ✅ |
| 221 | What often affects or facilitates ease of analysis... | unusual resources | branch out | -0.0332 | ❌ |
| 222 | A non-deterministic Turing machine has the ability... | mathematical models | Many of the mathematical models | 0.0000 | ❌ |
| 223 | What is the most critical resource in the analysis... | time | Non-deterministic time | 0.0000 | ❌ |
| 224 | What is harder to analyze in terms of more unusual... | NO ANSWER | Deterministic | 0.0067 | ❌ |
| 225 | What type of machine is a computational model that... | NO ANSWER | Deterministic | 0.0000 | ❌ |
| 226 | What has a lot to do with how we physically want t... | NO ANSWER | NO ANSWER | 0.0187 | ✅ |
| 227 | What machine's branching does not exactly capture ... | NO ANSWER | Deterministic Turing machine | 0.0000 | ❌ |
| 228 | What is the least critical resource in the analysi... | NO ANSWER | NO ANSWER | 0.0777 | ✅ |
| 229 | The time required to output an answer on a determi... | state transitions | NO ANSWER | 0.0155 | ❌ |
| 230 | Complexity theory classifies problems based on wha... | difficulty | their difficulty | -0.0095 | ❌ |
| 231 | What is the expression used to identify any given ... | DTIME(f(n)) | NO ANSWER | 0.0385 | ❌ |
| 232 | What is the most critical resource measured to in ... | time | NO ANSWER | 0.0445 | ❌ |
| 233 | What is not used for a precise definition of what ... | NO ANSWER | NO ANSWER | 0.3501 | ✅ |
| 234 | How is Turing machine M said not to operate? | NO ANSWER | NO ANSWER | 0.0758 | ✅ |
| 235 | What is the expression used to identify any given ... | NO ANSWER | NO ANSWER | 0.0506 | ✅ |
| 236 | What is the least critical resource measured in as... | NO ANSWER | NO ANSWER | 0.0498 | ✅ |
| 237 | How can decision problem B be solved in time x(f)? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 238 | Time and space are both examples of what type of r... | complexity resources | computer resources | -0.0829 | ❌ |
| 239 | A complexity resource can also be described as wha... | computational resource | Analogous | -0.0662 | ❌ |
| 240 | What is typically used to broadly define complexit... | Blum complexity axioms | Blum complexity axioms | 0.0000 | ✅ |
| 241 | Communication complexity is an example of what typ... | Complexity measures | Communication complexity | -0.0579 | ❌ |
| 242 | Decision tree is an example of what type of measur... | Complexity measures | type | -0.0110 | ❌ |
| 243 | What can not be made for space requirements? | NO ANSWER | NO ANSWER | 0.1982 | ✅ |
| 244 | What are the least well known complexity resources... | NO ANSWER | NO ANSWER | 0.1874 | ✅ |
| 245 | How are complexity measures generally not defined? | NO ANSWER | NO ANSWER | 0.3095 | ✅ |
| 246 | What are other complexity measures not used in com... | NO ANSWER | NO ANSWER | 0.5762 | ✅ |
| 247 | What type of measure is communication complexity n... | NO ANSWER | NO ANSWER | 0.0742 | ✅ |
| 248 | What are the three primary expressions used to rep... | best, worst and average | NO ANSWER | 0.0471 | ❌ |
| 249 | Case complexity likelihoods provide variable proba... | complexity measure | NO ANSWER | 0.0336 | ❌ |
| 250 | What is one common example of a critical complexit... | time | NO ANSWER | 0.1122 | ❌ |
| 251 | Case complexities provide three likelihoods of wha... | inputs | time complexity | 0.0049 | ❌ |
| 252 | What are the three secondary expressions used to r... | NO ANSWER | NO ANSWER | 0.0362 | ✅ |
| 253 | What three different ways are used to measure spac... | NO ANSWER | NO ANSWER | 0.7328 | ✅ |
| 254 | What is one not common example of a critical compl... | NO ANSWER | NO ANSWER | 0.0732 | ✅ |
| 255 | What differing variable remains the same size when... | NO ANSWER | NO ANSWER | 0.0477 | ✅ |
| 256 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | 0.0117 | ❌ |
| 257 | When extensive time is required to sort integers, ... | worst-case | NO ANSWER | 0.0453 | ❌ |
| 258 | What is the expression used to denote a worst case... | O(n2) | O(n2) | 0.0000 | ✅ |
| 259 | What does not solve the problem of sorting a list ... | NO ANSWER | NO ANSWER | 0.3010 | ✅ |
| 260 | What does the deterministic parting algorithm quic... | NO ANSWER | NO ANSWER | 0.1224 | ✅ |
| 261 | What case complexity is represented when limited t... | NO ANSWER | NO ANSWER | 0.1547 | ✅ |
| 262 | What is the expression not used to denote worst ca... | NO ANSWER | NO ANSWER | 0.0552 | ✅ |
| 263 | What case complexity is represented when each pivo... | NO ANSWER | NO ANSWER | 0.3368 | ✅ |
| 264 | Classification of resources is contingent on deter... | the most efficient algorithm | minimum amount of time required by the most efficient algorithm solving a | 0.0000 | ❌ |
| 265 | The analysis of a specific algorithm is typically ... | analysis of algorithms | analysis of a particular algorithm falls under the field of analysis of | 0.0000 | ❌ |
| 266 | Which bound of time is more difficult to establish... | lower bounds | NO ANSWER | 0.1131 | ❌ |
| 267 | A specific algorithm demonstrating T(n) represents... | upper bound | NO ANSWER | 0.0746 | ❌ |
| 268 | What is the colloquial phrase used to convey the c... | all possible algorithms | NO ANSWER | 0.0609 | ❌ |
| 269 | How does one note classify the computation time (o... | NO ANSWER | To classify the computation time (or similar resources), one is interested | -0.0423 | ❌ |
| 270 | What is usually taken as the best case complexity,... | NO ANSWER | Wor worst-case complexity | 0.0000 | ❌ |
| 271 | What does not fall under the field of analysis of ... | NO ANSWER | NO ANSWER | 0.1863 | ✅ |
| 272 | When does one not need to show only that there is ... | NO ANSWER | NO ANSWER | 0.3123 | ✅ |
| 273 | What is easy about proving lower bounds? | NO ANSWER | NO ANSWER | 0.7129 | ✅ |
| 274 | What expression is generally used to convey upper ... | big O notation | big O | -0.0831 | ❌ |
| 275 | What does a big O notation hide? | constant factors and smaller terms | constant factors and smaller terms | 0.0000 | ✅ |
| 276 | How would one write T(n) = 7n2 + 15n + 40 in big O... | T(n) = O(n2) | O(n2) | 0.0000 | ❌ |
| 277 | Big O notation provides autonomy to upper and lowe... | the computational model | autn, lower | -0.0435 | ❌ |
| 278 | What is usually not stated using the big O notatio... | NO ANSWER | NO ANSWER | 0.0884 | ✅ |
| 279 | What does not hide constant factors or smaller ter... | NO ANSWER | Big O notation | 0.0057 | ❌ |
| 280 | What makes the bounds dependent of the specific de... | NO ANSWER | Constant factors | 0.0000 | ❌ |
| 281 | How would one abbreviate T(n)=8n2 + 16n = 40 in bi... | NO ANSWER | NO ANSWER | 0.2052 | ✅ |
| 282 | What has complicated definitions that prevent clas... | complexity classes | NO ANSWER | 0.7944 | ❌ |
| 283 | Complexity classes are generally classified into w... | framework | NO ANSWER | 0.0604 | ❌ |
| 284 | Difficulty in establishing a framework for complex... | complicated definitions | Variable: complexity | -0.0083 | ❌ |
| 285 | What fits the framework of complexity classes? | NO ANSWER | NO ANSWER | 0.5306 | ✅ |
| 286 | What has uncomplicated definitions that prevent cl... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 287 | What are complexity classes generally not classifi... | NO ANSWER | NO ANSWER | 0.8150 | ✅ |
| 288 | What variable is easy to establish in a framework ... | NO ANSWER | NO ANSWER | 0.4462 | ✅ |
| 289 | Concrete bounding of computation time frequently p... | chosen machine model | computer model | -0.2672 | ❌ |
| 290 | A multi-tape Turing machine requires what type of ... | linear time | NO ANSWER | 0.0232 | ❌ |
| 291 | A language solved in quadratic time implies the us... | single-tape Turing machines | single-tape Turing machine | 0.0000 | ❌ |
| 292 | What thesis specifies that a polynomial relationsh... | Cobham-Edmonds thesis | Cobham-Edmonds thesis | 0.0000 | ✅ |
| 293 | Decision problems capable of being solved by a det... | complexity class P | P | 0.0000 | ❌ |
| 294 | What does not often yield complexity classes that ... | NO ANSWER | NO ANSWER | 0.0260 | ✅ |
| 295 | What does not frequently produce complexity classe... | NO ANSWER | NO ANSWER | 0.4081 | ✅ |
| 296 | What can not be solved in linear time on multi-tap... | NO ANSWER | Can be solved in linear time on multi-tape Turing machine | -0.0826 | ❌ |
| 297 | What is not a binary string? | NO ANSWER | NO ANSWER | 0.3451 | ✅ |
| 298 | What thesis specifies that a trinomial relationshi... | NO ANSWER | Cobham-Edmonds thesis | 0.0000 | ❌ |
| 299 | What are two examples of measurements are bound wi... | time or space | NO ANSWER | 0.0259 | ❌ |
| 300 | What function is used by algorithms to define meas... | bounding | NO ANSWER | 0.0944 | ❌ |
| 301 | Bounding of time and space or similar measurements... | complexity classes | algorithm | -0.0066 | ❌ |
| 302 | What cannot be defined by bounding the time or spa... | NO ANSWER | NO ANSWER | 0.7327 | ✅ |
| 303 | What are three examples of measurement that are bo... | NO ANSWER | NO ANSWER | 0.0246 | ✅ |
| 304 | What function is used by algorithms to define meas... | NO ANSWER | NO ANSWER | 0.3477 | ✅ |
| 305 | What is often used by algorithms to measure boundi... | NO ANSWER | NO ANSWER | 0.1410 | ✅ |
| 306 | What are three examples of complexity classes asso... | BPP, ZPP and RP | BPP, ZPP, RP | 0.0000 | ❌ |
| 307 | AC and NC are complexity classes typically associa... | Boolean | Boolean | 0.0000 | ✅ |
| 308 | BQP and QMA are examples of complexity classes mos... | quantum | Quantistic | 0.0000 | ❌ |
| 309 | What is the expression used to represent a complex... | #P | #P | 0.0000 | ✅ |
| 310 | IP and AM are most commonly defined by what type o... | Interactive | Interactive proof systems | 0.0000 | ❌ |
| 311 | What are the other four important complexity class... | NO ANSWER | P, IP, BPP, and RP | -0.2346 | ❌ |
| 312 | What machine does not define BPP, ZPP, and RP? | NO ANSWER | Quant Turing machines | -0.0108 | ❌ |
| 313 | What machine does not define BQP or QMA? | NO ANSWER | Decision problems | -0.0001 | ❌ |
| 314 | What is least important complexity class of counti... | NO ANSWER | NO ANSWER | 0.2822 | ✅ |
| 315 | What system not often define classes like IP and A... | NO ANSWER | probabilistic Turing machines | -0.0358 | ❌ |
| 316 | What is an example of a measurement within a compl... | computation time | NO ANSWER | 0.2228 | ❌ |
| 317 | In what expression can one expect to find DTIME(n) | DTIME(n2) | NO ANSWER | 0.4747 | ❌ |
| 318 | What theorems are responsible for determining ques... | time and space hierarchy theorems | time and space hierarchy theorems | -0.0364 | ✅ |
| 319 | Resources are constrained by hierarchy theorems to... | a proper hierarchy on the classes defined | resources | 0.0000 | ❌ |
| 320 | What kind of statement is made in the effort of es... | quantitative statements | NO ANSWER | 0.0258 | ❌ |
| 321 | What is not an example of a measurement within a c... | NO ANSWER | NO ANSWER | 0.5175 | ✅ |
| 322 | What does not define a bigger set of problems? | NO ANSWER | NO ANSWER | 0.7851 | ✅ |
| 323 | What expression does not usually contain DTIME(n)? | NO ANSWER | NO ANSWER | 0.5283 | ✅ |
| 324 | What does not induce a proper hierarchy on the cla... | NO ANSWER | NO ANSWER | 0.6810 | ✅ |
| 325 | What kind of statement is not made in an effort of... | NO ANSWER | NO ANSWER | 0.5366 | ✅ |
| 326 | What is the foundation for separation results with... | time and space hierarchy theorems | time hierarchy theorem and the space hierarchy theorem | -0.4389 | ❌ |
| 327 | What is responsible for constraining P according t... | EXPTIME | P | -0.0288 | ❌ |
| 328 | Within what variable is L constrained according to... | PSPACE | PSPACE | -0.0628 | ✅ |
| 329 | What does not form the basis for most separation r... | NO ANSWER | NO ANSWER | 0.3207 | ✅ |
| 330 | What does the past time and space hierarchy theore... | NO ANSWER | Separ separation results of complexity classes | -0.0105 | ❌ |
| 331 | What is not strictly contained in EXPTIME? | NO ANSWER | NO ANSWER | 0.2349 | ✅ |
| 332 | What is not strictly contained in PSPACE? | NO ANSWER | NO ANSWER | 0.2282 | ✅ |
| 333 | What concept is frequently used to define complexi... | reduction | re reduction | 0.0000 | ❌ |
| 334 | Reduction essentially takes one problem and conver... | another problem | one | 0.0000 | ❌ |
| 335 | According to reduction, if X and Y can be solved b... | reduces | NO ANSWER | 0.1523 | ❌ |
| 336 | What are two examples of different types of reduct... | Karp reductions and Levin reductions | Cook reductions and Karp reductions | 0.0000 | ❌ |
| 337 | Polynomial time reductions are an example of what? | the bound on the complexity of reductions | pol polynomial-time reductions | -0.0514 | ❌ |
| 338 | What are many complexity classes not defined by? | NO ANSWER | NO ANSWER | 0.0731 | ✅ |
| 339 | What is defined by using the theorem of reduction? | NO ANSWER | NO ANSWER | 0.0648 | ✅ |
| 340 | What is a transformation of two problems into on t... | NO ANSWER | NO ANSWER | 0.0489 | ✅ |
| 341 | What captures the formal notion of a problem being... | NO ANSWER | transformation of one problem into another problem | 0.0000 | ❌ |
| 342 | What are the six types of reductions? | NO ANSWER | NO ANSWER | 0.3587 | ✅ |
| 343 | What is the most frequently employed type of reduc... | polynomial-time reduction | Pol polynomial-time reduction | -0.0417 | ❌ |
| 344 | What equates to a squared integer according to pol... | multiplying two integers | squaring | -0.0847 | ❌ |
| 345 | What measurement of time is used in polynomial tim... | polynomial time | NO ANSWER | 0.0176 | ❌ |
| 346 | What would need to remain constant in a multiplica... | input | inputs | -0.0208 | ❌ |
| 347 | According to polynomial time reduction squaring ca... | multiplication | multip multiplication | -0.0316 | ❌ |
| 348 | What is the least used type of reduction? | NO ANSWER | NO ANSWER | 0.3213 | ✅ |
| 349 | What is the meaning of polynomial-space reduction? | NO ANSWER | pol polynomial-time reduction | -0.0149 | ❌ |
| 350 | What can the problem of dividing an integer be red... | NO ANSWER | Multip multiplying two integers | -0.1188 | ❌ |
| 351 | What does one not need to remain constant in a mul... | NO ANSWER | NO | -0.0113 | ❌ |
| 352 | What is more difficult that multiplication? | NO ANSWER | NO ANSWER | 0.1202 | ✅ |
| 353 | The complexity of problems often depends on what? | the type of reduction being used | type of reduction | 0.0000 | ❌ |
| 354 | What would create a conflict between a problem X a... | if every problem in C can be reduced to X | NO ANSWER | 0.1464 | ❌ |
| 355 | An algorithm for X which reduces to C would us to ... | solve any problem in C | Allow us to solve any problem in C | 0.0000 | ❌ |
| 356 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | 0.0817 | ❌ |
| 357 | What does the complexity of problems not often dep... | NO ANSWER | re reduction | 0.0091 | ❌ |
| 358 | What would not create a conflict between a problem... | NO ANSWER | NO ANSWER | 0.3882 | ✅ |
| 359 | What problem in C is harder than X? | NO ANSWER | NO ANSWER | 0.4778 | ✅ |
| 360 | How is a problem set that is hard for expression Q... | NO ANSWER | NO ANSWER | 0.3111 | ✅ |
| 361 | The hardest problems in NP can be analogously writ... | NP-complete | NO ANSWER | 0.0110 | ❌ |
| 362 | NP complete problems contain the lowest likelihood... | NP | P | 0.0091 | ❌ |
| 363 | If P = NP is unsolved, and reduction is applied to... | there is no known polynomial-time solution | It would mean that there is no known polynomial-time solution for Π | -0.1764 | ❌ |
| 364 | If polynomial time can be utilized within an NP-co... | NP | NO ANSWER | 0.2435 | ❌ |
| 365 | What happens if a problem X is in C, and soft for ... | NO ANSWER | NO ANSWER | 0.4364 | ✅ |
| 366 | What is the softest problem in C? | NO ANSWER | NO ANSWER | 0.8840 | ✅ |
| 367 | What is class contains the the least difficult pro... | NO ANSWER | NO ANSWER | 0.5931 | ✅ |
| 368 | What would indicate that there is a known polynomi... | NO ANSWER | NO ANSWER | 0.2211 | ✅ |
| 369 | What complexity class is characterized by a comput... | P | P | 0.0000 | ✅ |
| 370 | What hypothesis is associated with the complexity ... | Cobham–Edmonds thesis | Cobham–Edmonds thesis | -0.4327 | ✅ |
| 371 | What complexity class is commonly characterized by... | NP | NO ANSWER | 0.0669 | ❌ |
| 372 | What is an example of a problem that rests within ... | Boolean satisfiability problem | Boolean satisfiability problem, the Hamiltonian path problem, and | -0.3840 | ❌ |
| 373 | In what theoretical machine is it confirmed that a... | Turing machines | NO ANSWER | 0.0521 | ❌ |
| 374 | What is often seen as a scientific abstraction mod... | NO ANSWER | complexity class P | -0.5340 | ❌ |
| 375 | What theory is the Cobham-Edward thesis? | NO ANSWER | Cobham–Edmonds thesis | -0.4683 | ❌ |
| 376 | What complexity class is not commonly characterize... | NO ANSWER | NO ANSWER | 0.1554 | ✅ |
| 377 | What is an example of a problem that rests within ... | NO ANSWER | 3. The Hamiltonian path problem | -0.2787 | ❌ |
| 378 | What ,theoretical machine did not confirm that a p... | NO ANSWER | NO ANSWER | 0.0835 | ✅ |
| 379 | If P is ultimately proven to be equal tot NP, what... | more efficient solutions | This problem can be shown to have more efficient solutions | -0.0268 | ❌ |
| 380 | What is a particular problem in biology that would... | protein structure prediction | Pro protein structure prediction in biology | 0.0000 | ❌ |
| 381 | What is the prize offered for finding a solution t... | $1,000,000 | $1,000,000 | -0.7020 | ✅ |
| 382 | What is one of the least important open questions ... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 383 | What effect would happen if P is ultimately proven... | NO ANSWER | NO ANSWER | 0.4807 | ✅ |
| 384 | What is a particular problem in chemistry that wou... | NO ANSWER | Pro protein structure prediction in biology | 0.0075 | ❌ |
| 385 | What problem was proposed by Clay Mathematics Inst... | NO ANSWER | NO ANSWER | 0.5763 | ✅ |
| 386 | What was the prize for finding a solution to P=NP ... | NO ANSWER | NO ANSWER | 0.8297 | ✅ |
| 387 | Who demonstrated that P= NP implies problems not p... | Ladner | Ladner | 0.0000 | ✅ |
| 388 | What is the name for a problem that meets Ladner's... | NP-intermediate problems | NP-intermediate problems | 0.0000 | ✅ |
| 389 | What is an example of an NP-intermediate problem n... | graph isomorphism problem | They are some of the very few NP problems not known to be | 0.0000 | ❌ |
| 390 | Who showed that if P=NQ then there exists problems... | NO ANSWER | NO ANSWER | 0.7327 | ✅ |
| 391 | What is the name a a problem that meets Ladder's a... | NO ANSWER | NP-intermediate problems | 0.0000 | ❌ |
| 392 | What is not example of an NP-intermediate problem ... | NO ANSWER | NO ANSWER | 0.0841 | ✅ |
| 393 | What are four examples of problems believed to be ... | NO ANSWER | graph isomorphism problem, the discrete logarithm problem, | 0.0000 | ❌ |
| 394 | What is the problem attributed to defining if two ... | The graph isomorphism problem | graph isomorphism | -0.5627 | ❌ |
| 395 | What class is most commonly not ascribed to the gr... | NP-complete | NO ANSWER | 0.3534 | ❌ |
| 396 | What finite hierarchy implies that the graph isomo... | polynomial time hierarchy | NO ANSWER | 0.0670 | ❌ |
| 397 | To what level would the polynomial time hierarchy ... | second level | If graph isomorphism is NP-complete, the polynomial time hierarchy | -0.4706 | ❌ |
| 398 | Who are commonly associated with the algorithm typ... | Laszlo Babai and Eugene Luks | Laszlo Babai and Eugene Luks | -0.0182 | ✅ |
| 399 | What is the graph isolation problem?  | NO ANSWER | NO ANSWER | 0.4948 | ✅ |
| 400 | What is the problem attributed to defining if thre... | NO ANSWER | NO ANSWER | 0.0933 | ✅ |
| 401 | What is an important solved problem in complexity ... | NO ANSWER | NO ANSWER | 0.1588 | ✅ |
| 402 | What infinite hierarchy implies that the graph iso... | NO ANSWER | NO ANSWER | 0.5513 | ✅ |
| 403 | What would the polynomial hierarchy collapse if gr... | NO ANSWER | NO ANSWER | 0.3476 | ✅ |
| 404 | What computational problem is commonly associated ... | The integer factorization problem | integer factorization | -0.2640 | ❌ |
| 405 | The integer factorization problem essentially seek... | k | k | -0.0268 | ✅ |
| 406 | That there currently exists no known integer facto... | modern cryptographic systems | Modern cryptographic systems | -0.5055 | ✅ |
| 407 | What is the most well-known algorithm associated w... | the general number field sieve | general number field sieve | -0.8048 | ❌ |
| 408 | What is the integer practice problem? | NO ANSWER | NO ANSWER | 0.6561 | ✅ |
| 409 | What computational problem is not commonly associa... | NO ANSWER | Brum-2 | -0.0044 | ❌ |
| 410 | What problem is phrased on deciding whether the in... | NO ANSWER | NO such problem is given | -0.0950 | ❌ |
| 411 | What problem would have polynomial time hierarchy ... | NO ANSWER | integer factorization problem | -0.3601 | ❌ |
| 412 | What is the least well known algorithm associated ... | NO ANSWER | NO ANSWER | 0.2875 | ✅ |
| 413 | What is the unproven assumption generally ascribed... | suspected to be unequal | = PSPACE | -0.0469 | ❌ |
| 414 | What is an expression that can be used to illustra... | P ⊆ NP ⊆ PP ⊆ PSPACE | ⊆ NP ⊆ PP ⊆ PSPACE | 0.0021 | ❌ |
| 415 | Where can the complexity classes RP, BPP, PP, BQP,... | between P and PSPACE | NO ANSWER | 0.0250 | ❌ |
| 416 | What evidence between and among complexity classes... | Proving that any of these classes are unequal | NO ANSWER | 0.1960 | ❌ |
| 417 | What is the proven assumption generally ascribed t... | NO ANSWER | NO ANSWER | 0.1973 | ✅ |
| 418 | What is an expression that caan be used to illustr... | NO ANSWER | NO ANSWER | 0.0505 | ✅ |
| 419 | Where can complexity classes RPP, BPP, PPP, BQP, M... | NO ANSWER | NO ANSWER | 0.0195 | ✅ |
| 420 | What is impossible for the complexity classes RP, ... | NO ANSWER | NO ANSWER | 0.3680 | ✅ |
| 421 | What would not be a major breakthrough in complexi... | NO ANSWER | NO ANSWER | 0.4175 | ✅ |
| 422 | In what complexity class do complement problems of... | co-NP | co-NP | 0.0000 | ✅ |
| 423 | How do the yes/no answers of a complement problem ... | reversed | NO ANSWER | 0.1144 | ❌ |
| 424 | What is commonly believed to be the value relation... | not equal | is not equal to NP | -0.4673 | ❌ |
| 425 | What implication can be derived for P and NP if P ... | P is not equal to NP | is not equal to NP | -0.4785 | ❌ |
| 426 | What complexity class do incompatible problems of ... | NO ANSWER | co-NP | 0.0000 | ❌ |
| 427 | How do the yes/no answers of an incompatible probl... | NO ANSWER | NO ANSWER | 0.6587 | ✅ |
| 428 | What is not commonly believed to be the value rela... | NO ANSWER | NO, it is believed that NP is not equal to co-N | -0.1403 | ❌ |
| 429 | What implication can not be derived for P and NP i... | NO ANSWER | If P is not equal to NP, then P is not equal | -0.0999 | ❌ |
| 430 | What variable is associated with all problems solv... | L | L | 0.0000 | ✅ |
| 431 | Though unkown, what are the most commonly ascribed... | strictly contained in P or equal to P | NO ANSWER | 0.0854 | ❌ |
| 432 | What lies between L and P that prevents a definiti... | complexity classes | NO ANSWER | 0.0673 | ❌ |
| 433 | What are two complexity classes between L and P? | NL and NC | NL and NC | 0.0000 | ✅ |
| 434 | What is unknown about the complexity classes betwe... | if they are distinct or equal classes | NO ANSWER | 0.1176 | ❌ |
| 435 | What variable is not associated with all problems ... | NO ANSWER | NO ANSWER | 0.1048 | ✅ |
| 436 | What are the least commonly ascribed attributes of... | NO ANSWER | NO ANSWER | 0.2982 | ✅ |
| 437 | What does not lie between L and P that allows a de... | NO ANSWER | NO ANSWER | 0.4243 | ✅ |
| 438 | What are three complexity classes between L and P? | NO ANSWER | NO ANSWER | 0.0259 | ✅ |
| 439 | What is known about the complexity between L and P... | NO ANSWER | NO ANSWER | 0.4144 | ✅ |
| 440 | Problems capable of theoretical solutions but cons... | intractable problems | intractable | 0.0000 | ❌ |
| 441 | Intractable problems lacking polynomial time solut... | exponential-time algorithms | Pol polynomial time algorithm | -0.0280 | ❌ |
| 442 | If NP is not equal to P, viewed through this lens,... | NP-complete problems | NP-complete problems | 0.0000 | ✅ |
| 443 | What are problems that cannot be solved in theory,... | NO ANSWER | NO ANSWER | 0.0173 | ✅ |
| 444 | When are problems that have polynomial-tome soluti... | NO ANSWER | NO ANSWER | 0.0529 | ✅ |
| 445 | What states that only problems that cannot be solv... | NO ANSWER | Cobham–Edmonds thesis | 0.0000 | ❌ |
| 446 | When would a program not be useful for very small ... | NO ANSWER | If its running time is, say, n15 | -0.1148 | ❌ |
| 447 | What algorithm is always practical? | NO ANSWER | NO ANSWER | 0.4326 | ✅ |
| 448 | What eponymous variation of arithmetic presents a ... | Presburger arithmetic | Presburger arithmetic | 0.0000 | ✅ |
| 449 | Despite the Presburger problem, and in view of int... | algorithms have been written | Al algorithms can solve the problem in reasonable times in most cases | -0.0372 | ❌ |
| 450 | What is an example of a problem to which effective... | NP-complete knapsack problem | decision problem in Presburger arithmetic | 0.0000 | ❌ |
| 451 | How quickly can an algorithm solve an NP-complete ... | in less than quadratic time | Less than quadratic time | 0.0000 | ❌ |
| 452 | What is the example of another problem characteriz... | NP-complete Boolean satisfiability problem | Boolean satisfiability problem | -0.0053 | ❌ |
| 453 | What unknown variation of arithmetic presents a de... | NO ANSWER | NO ANSWER | 0.0466 | ✅ |
| 454 | What has not been done to establish solutions in r... | NO ANSWER | NO ANSWER | 0.0491 | ✅ |
| 455 | What can not solve the NP-complete knapsack proble... | NO ANSWER | NO ANSWER | 0.4340 | ✅ |
| 456 | What do SAT solvers not usually handle when testin... | NO ANSWER | NO ANSWER | 0.2351 | ✅ |
| 457 | What tactic did researchers employ to offset the f... | foundations were laid out | They laid out foundations | 0.0057 | ❌ |
| 458 | Who was the most influential researcher among thos... | Alan Turing | NO ANSWER | 0.0751 | ❌ |
| 459 | What theoretical device is attributed to Alan Turi... | Turing machines | Turing machines | 0.0000 | ✅ |
| 460 | In what year was the Alan Turing's definitional mo... | 1936 | 1936 | -1.0000 | ✅ |
| 461 | In the most basic sense what did a Turing machine ... | a computer | NO ANSWER | 0.0708 | ❌ |
| 462 | What were laid out by various companies? | NO ANSWER | found the foundations | 0.0020 | ❌ |
| 463 | What tactic did companies employ to offset the for... | NO ANSWER | NO ANSWER | 0.2390 | ✅ |
| 464 | Who was the least influential researcher working o... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 465 | What device did Alan Turning invent in 1974? | NO ANSWER | NO ANSWER | 0.8685 | ✅ |
| 466 | What was the Turning calculator a robust and flexi... | NO ANSWER | computer | 0.0000 | ❌ |
| 467 | What paper is commonly considered the bellwether u... | On the Computational Complexity of Algorithms | "On the Computational Complexity of Algorithms" by Juris Hartmanis | -0.1668 | ❌ |
| 468 | What individuals were responsible for authoring "O... | Juris Hartmanis and Richard Stearns | Juris Hartmanis and Richard Stearns | 0.0000 | ✅ |
| 469 | In what year was Hatmanis and Stearn's seminal wor... | 1965 | 1965 | -1.0000 | ✅ |
| 470 | What complex measurements were defined by "On the ... | time and space | Time and space complexity | 0.0000 | ❌ |
| 471 | In what year did Edmond's characterize a "good" al... | 1965 | 1965 | -0.8568 | ✅ |
| 472 | What seminal paper is commonly considered the begi... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 473 | Who wrote "On the Computational Complexity of Scie... | NO ANSWER | NO ANSWER | 0.7349 | ✅ |
| 474 | What seminal paper was written by Juris Hartmanis ... | NO ANSWER | NO ANSWER | 0.6085 | ✅ |
| 475 | What simple measurements were defined by "On the C... | NO ANSWER | time and space complexity | 0.0000 | ❌ |
| 476 | Who provided a definition of linear bounded automa... | John Myhill | John Myhill | 0.0000 | ✅ |
| 477 | In what year did Raymond Sullivan publish a study ... | 1961 | NO ANSWER | 0.5087 | ❌ |
| 478 | In 1962, who was responsible for the authorship of... | Hisao Yamada | Hisao Yamada | 0.0000 | ✅ |
| 479 | Who wrote later papers studying problems solvable ... | NO ANSWER | Myhill (1960), Smullyan (1961), | -0.2091 | ❌ |
| 480 | Who provided a definition of linear bounded automa... | NO ANSWER | NO ANSWER | 0.5288 | ✅ |
| 481 | What year did Dick Sullivan publish a study on rud... | NO ANSWER | NO ANSWER | 0.6320 | ✅ |
| 482 | Who wrote a paper on real time computations in 197... | NO ANSWER | NO ANSWER | 0.6586 | ✅ |
| 483 | Who was pioneer and studied specific complexity me... | NO ANSWER | NO ANSWER | 0.3941 | ✅ |
| 484 | What is the concrete choice typically assumed by m... | input encoding | NO ANSWER | 0.0608 | ❌ |
| 485 | In the effort of maintaining a level of abstractio... | encoding | encoding | -0.0070 | ✅ |
| 486 | What can not be achieved by ensuring different rep... | NO ANSWER | NO ANSWER | 0.2993 | ✅ |
| 487 | What is the abstract choice typically assumed by m... | NO ANSWER | NO ANSWER | 0.0667 | ✅ |
| 488 | What does not regularly use input coding as its co... | NO ANSWER | Proof of theorems | -0.0296 | ❌ |
| 489 | What choice is typically left dependent in an effo... | NO ANSWER | encoding | 0.0015 | ❌ |
| 490 | Who is responsible for axiomatic complexity theory... | Manuel Blum | Man Manuel Blum | 0.0000 | ❌ |
| 491 | What theorem was implicated by Manuel Blum's axiom... | speed-up theorem | speed-up theorem | 0.0000 | ✅ |
| 492 | What is the paper written by Richard Karp in 1972 ... | "Reducibility Among Combinatorial Problems" | "Reducibility Among Combinatorial Problems | -0.0656 | ❌ |
| 493 | How many combinatory and graph theoretical problem... | 21 | 21 | -1.0000 | ✅ |
| 494 | Who developed an axiomatic complexity theory based... | NO ANSWER | NO ANSWER | 0.8211 | ✅ |
| 495 | Who is responsible for the so-called, speed-up the... | NO ANSWER | NO ANSWER | 0.7795 | ✅ |
| 496 | Who proved that these exist practical relevant pro... | NO ANSWER | NO ANSWER | 0.5969 | ✅ |
| 497 | Who wrote the paper "Reductibility Among Combinato... | NO ANSWER | NO ANSWER | 0.3643 | ✅ |
| 498 | What book featured 25 diverse comninatorial and gr... | NO ANSWER | NO ANSWER | 0.0425 | ✅ |
| 499 | What is Southern California often abbreviated as? | SoCal | SoCal | 0.0000 | ✅ |
| 500 | Despite being traditionall described as "eight cou... | 10 counties | 11 | -0.3358 | ❌ |
| 501 | What is a major importance of Southern California ... | economic center | Southern California is a major economic center for the state of California and | -0.0456 | ❌ |
| 502 | What are the ties that best described what the "ei... | demographics and economic ties | Dem demographics | 0.0000 | ❌ |
| 503 | The reasons for the las two counties to be added a... | historical political divisions | histor political divisions | -0.0114 | ❌ |
| 504 | What counties does the more extensive eight county... | NO ANSWER | Im Imperial, Los Angeles, Orange, Riverside, San Bernardino, | 0.0000 | ❌ |
| 505 | What additional two counties make ten counties int... | NO ANSWER | Kern and San Luis Obispo | 0.0000 | ❌ |
| 506 | Where is the center of economic activity for the U... | NO ANSWER | NO ANSWER | 0.7094 | ✅ |
| 507 | What is the name of the region that is not defined... | Southern California Megaregion | Southern California Megaregion | -0.5262 | ✅ |
| 508 | How many megaregions are there in the United State... | 11 | NO | -0.8810 | ❌ |
| 509 | What is the name of the state that the megaregion ... | Nevada | Nevada | 0.0000 | ✅ |
| 510 | Which border does the megaregion extend over? | Mexican | South | -0.0458 | ❌ |
| 511 | What is the name of the area past the border that ... | Tijuana | Las Vegas, Nevada | -0.0280 | ❌ |
| 512 | What is one of the 10 megaregions in the United St... | NO ANSWER | Greater Southern California Megaregion | -0.3579 | ❌ |
| 513 | Where does the 8 county megaregion extend from? | NO ANSWER | NO ANSWER | 0.0446 | ✅ |
| 514 | What is Las Vegas one of in the United States? | NO ANSWER | One of the 11 megaregions of the United States | 0.0000 | ❌ |
| 515 | Which coastline does Southern California touch? | Pacific | Pacific coast | 0.0000 | ❌ |
| 516 | How many metropolitan areas does Southern Californ... | seven | Seven | 0.0000 | ✅ |
| 517 | How many inhabitants does the Los Angeles area con... | 12 million | Over 12 million | -0.4311 | ❌ |
| 518 | Which of the three heavily populated areas has the... | San Diego | San Diego area with over 3 million inhabitants | -0.1676 | ❌ |
| 519 | How many people does the Greater Los Angeles Area ... | 17.5 million | 17.5 million | -0.8295 | ✅ |
| 520 | What percent of California's 22 million people liv... | NO ANSWER | 60 | -1.0000 | ❌ |
| 521 | What does MAS stand for? | NO ANSWER | MAS | -0.0132 | ❌ |
| 522 | How many people live in Riverside?  | NO ANSWER | 4 million | -0.0255 | ❌ |
| 523 | What does CSA stand for? | NO ANSWER | Central Southern Area | 0.0014 | ❌ |
| 524 | What is the name of the water body that is found t... | Colorado River | Colorado River | 0.0000 | ✅ |
| 525 | What is the name of the desert on the border of Ar... | Colorado Desert | Colorado Desert | 0.0000 | ✅ |
| 526 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | 0.0000 | ✅ |
| 527 | What is the name of the border to the south? | Mexico–United States border | Mexico–United States border | 0.0000 | ✅ |
| 528 | What desert is to the south near Arizona? | NO ANSWER | NO ANSWER | 0.0333 | ✅ |
| 529 | What desert is to the south near Nevada? | NO ANSWER | NO ANSWER | 0.0268 | ✅ |
| 530 | What direction is the Colorado-Mexico border? | NO ANSWER | South | -0.1244 | ❌ |
| 531 | The cities of Los Angeles and San Diego are a part... | California | California | 0.0000 | ✅ |
| 532 | What is the population of Los Angeles? | 3,792,621 | 3,792,621 | -1.0000 | ✅ |
| 533 | Which city is the most populous in California? | Los Angeles | Los Angeles | 0.0000 | ✅ |
| 534 | What is the eighth most populous city in the natio... | San Diego | NO ANSWER | 0.0200 | ❌ |
| 535 | In which cardinal direction from Los Angeles is Sa... | south | South | 0.0000 | ✅ |
| 536 | What are two of the three major cities located in ... | NO ANSWER | Los Angeles and San Diego | -0.1067 | ❌ |
| 537 | What city has a population of 3,792,261? | NO ANSWER | NO ANSWER | 0.0790 | ✅ |
| 538 | What city has a population of 1,307,204? | NO ANSWER | NO ANSWER | 0.1037 | ✅ |
| 539 | What second most populous city is north of Los Ang... | NO ANSWER | NO ANSWER | 0.2473 | ✅ |
| 540 | Orange, San Diego, Riverside and San Bernardino ma... | Los Angeles | Los Angeles | 0.0000 | ✅ |
| 541 | What country are all the counties in? | United States | United States | 0.0000 | ✅ |
| 542 | What are Los Angeles, Orange, San Diego, San Berna... | counties | five most populous counties in the state of the United States | 0.0000 | ❌ |
| 543 | What is the lowest ranking one of the counties cou... | 15 | Rank 15 | -0.2182 | ❌ |
| 544 | What is the smallest geographical region discussed... | counties | state | -0.0134 | ❌ |
| 545 | What are the five most populous counties in the Un... | NO ANSWER | NO ANSWER | 0.4793 | ✅ |
| 546 | How many populous counties are in the United State... | NO ANSWER | NO | -0.2846 | ❌ |
| 547 | What county are Los Angeles, Orange, San Diego, Sa... | NO ANSWER | NO ANSWER | 0.0524 | ✅ |
| 548 | What is the name given to the district that is ass... | Hollywood | Hollywood | 0.0000 | ✅ |
| 549 | Which city does the Hollywood district belong to? | Los Angeles | Los Angeles | 0.0000 | ✅ |
| 550 | Which company owns ABC? | The Walt Disney Company | Walt Disney Company | -1.0000 | ❌ |
| 551 | Other than the motion picture and television indus... | music | NO ANSWER | 0.3242 | ❌ |
| 552 | Other than Universal and Warner Brothers, what oth... | Sony | Walt Disney Company | -0.5594 | ❌ |
| 553 | What company owns ACB? | NO ANSWER | Walt Disney Company | -0.9766 | ❌ |
| 554 | What three industries are centered in Hollywood? | NO ANSWER | Motion picture, television, and music | -0.2528 | ❌ |
| 555 | Where is Los Angeles a district of? | NO ANSWER | California | -0.0451 | ❌ |
| 556 | What major companies are headquartered in Los Ange... | NO ANSWER | Sony Pictures, Universal, MGM, Paramount Pictures, 20th | -0.4899 | ❌ |
| 557 | Other than surf, what other culture is southern Ca... | skateboard | Board sports, including snowboard and extreme sports | -0.0313 | ❌ |
| 558 | What is the name of the professional skateboarder ... | Tony Hawk | Tony Hawk | 0.0000 | ✅ |
| 559 | What famous snowbaorder lives in southern Californ... | Shaun White | Sha Shaun White | -0.0351 | ❌ |
| 560 | Southern California is second to which island in t... | Oahu | Oahu | 0.0000 | ✅ |
| 561 | What is the shortened name of the annual yacht rac... | Transpac | Transpac | 0.0000 | ✅ |
| 562 | Where are No Fear and RCVA headquartered? | NO ANSWER | No Fear and RVCA | -0.2360 | ❌ |
| 563 | Who are Rob Curran and Tim Machado? | NO ANSWER | Rob Machado and Tim Curran are professional surfers | 0.0000 | ❌ |
| 564 | Where does professional surfer Tony Hawk live? | NO ANSWER | Southern California | -0.7242 | ❌ |
| 565 | What famous surfing spots is Oahu second to? | NO ANSWER | Trestles, Rincon, The Wedge, Huntington Beach | -0.1942 | ❌ |
| 566 | What was held at the San Diego Yacht Club from 198... | NO ANSWER | NO ANSWER | 0.2233 | ✅ |
| 567 | What is the name of the desert city? | Palm Springs | Palm Springs | 0.0000 | ✅ |
| 568 | Other than the desert city why do many locals and ... | beaches | popular for its resort feel and nearby open spaces | -0.0278 | ❌ |
| 569 | Which region of California is Palm Springs located... | southern | Southern California | 0.0000 | ❌ |
| 570 | Other than for its resort feel, what is Palm Sprin... | open spaces | open spaces | 0.0079 | ✅ |
| 571 | Who visits Palm Springs for the beaches? | NO ANSWER | Tour tourists | -0.0301 | ❌ |
| 572 | What is the desert of southern California popular ... | NO ANSWER | res resort feel | 0.0000 | ❌ |
| 573 | Which coast is the desert on? | NO ANSWER | NO ANSWER | 0.0548 | ✅ |
| 574 | Geographically speaking, where is California's nor... | 37° 9' 58.23" | 37° 9' 58.23" | -1.0000 | ✅ |
| 575 | How many miles south of San Jose is the north - so... | 11 | 11 | -1.0000 | ✅ |
| 576 | The term "southern" California usually refers to h... | ten | ten | 0.0000 | ✅ |
| 577 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | Tehachapi Mountains | 0.0000 | ✅ |
| 578 | Point Conception is an example of a landmark among... | northern | Point Conception | 0.0000 | ❌ |
| 579 | What lies at 37° 8' 59.23" latitude? | NO ANSWER | NO ANSWER | 0.0659 | ✅ |
| 580 | What is around 18 miles south of San Jose? | NO ANSWER | San Jose | -0.1763 | ❌ |
| 581 | What lies at 35° 48′ 27″ north latitude? | NO ANSWER | NO ANSWER | 0.1575 | ✅ |
| 582 | What uses Point Tehachapi and the Conception Mount... | NO ANSWER | definition | 0.0001 | ❌ |
| 583 | Which country used to rule California? | Mexico | Mexico | 0.0000 | ✅ |
| 584 | Los Angeles is in the lower part of what? | Alta California | Al Alta California | -0.0131 | ❌ |
| 585 | Which Californio is located in the upper part? | Monterey | Californios of Monterey | 0.0000 | ❌ |
| 586 | What was the name of the legislation passed in 185... | the Missouri Compromise | Compromise of 1850 | 0.0000 | ❌ |
| 587 | The legislation allowed California to be admitted ... | free | Free state | 0.0000 | ❌ |
| 588 | What country did California once rule? | NO ANSWER | Mexico | 0.0000 | ❌ |
| 589 | Who were there disputes between when California ru... | NO ANSWER | Cal Californios | 0.0000 | ❌ |
| 590 | What line is at 30 degrees, 36 minutes? | NO ANSWER | line of the Missouri Compromise | -0.2726 | ❌ |
| 591 | What was passed in 1805? | NO ANSWER | NO ANSWER | 0.6965 | ✅ |
| 592 | Other than land laws, what else were the Californi... | inequitable taxes | taxes | 0.0000 | ❌ |
| 593 | What was the name given to the regions in which th... | Cow Counties | "Cow Counties" | -0.6696 | ❌ |
| 594 | How many times did southern California attempt to ... | three | Three | 0.0000 | ✅ |
| 595 | What was the percentage of people that voted in fa... | 75 | 75% | -0.8630 | ❌ |
| 596 | Which Senator was a strong advocate for the Pico A... | Milton Latham | Milton Latham | 0.0000 | ✅ |
| 597 | Who attempted to achieve a separate statehood in 1... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 598 | What was passed in 1895? | NO ANSWER | NO ANSWER | 0.9318 | ✅ |
| 599 | Who was the governor of California in 1895? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 600 | Who was elected in 1859? | NO ANSWER | Ab Abraham Lincoln | 0.0000 | ❌ |
| 601 | What title did Latham Milton hold? | NO ANSWER | Senator | 0.0000 | ❌ |
| 602 | Which newspaper defined southern California? | Los Angeles Times | Los Angeles Times | 0.0000 | ✅ |
| 603 | In which year did the newspaper define southern Ca... | 1900 | 1900 | -0.9754 | ✅ |
| 604 | In which year did the newspaper change its previou... | 1999 | 1900 | -0.9437 | ❌ |
| 605 | What was the newer county added to the list? | Imperial | Imperial | -1.0000 | ✅ |
| 606 | How many counties initially made up the definition... | seven | 7 | 0.0000 | ❌ |
| 607 | How did the Los Angeles Times define southern Cali... | NO ANSWER | NO ANSWER | 0.8589 | ✅ |
| 608 | What did the Los Angeles Times add to the definiti... | NO ANSWER | NO ANSWER | 0.9439 | ✅ |
| 609 | What did the California Times define twice? | NO ANSWER | seven counties of Los Angeles, San Bernardino, Orange, Riverside | -0.1129 | ❌ |
| 610 | Which organizations most commonly divide and promo... | regional tourism groups | California State Automobile Association and the Automobile Club of Southern California | -0.7252 | ❌ |
| 611 | Other than the Automobile Club of Southern Califor... | California State Automobile Association | California State Automobile Association | -0.4558 | ✅ |
| 612 | The two AAA clubs divided the state into a norther... | three-region | three-region | -0.0427 | ✅ |
| 613 | Which mountain range influenced the split of the r... | Tehachapis | Tehachapis | -0.5800 | ✅ |
| 614 | In the definition based off the mountain range, wh... | southern | east | -0.1684 | ❌ |
| 615 | What type of club is the California Automobile Sta... | NO ANSWER | AAA | -0.2525 | ❌ |
| 616 | What type of club is the Southern California Autom... | NO ANSWER | Automobile Club of Southern California | -0.3418 | ❌ |
| 617 | What type of phrase is North of the Tehachapis? | NO ANSWER | des geographical | 0.0000 | ❌ |
| 618 | What type of groups divides California into only n... | NO ANSWER | two AAA Auto Clubs of the state | -0.1764 | ❌ |
| 619 | Where does southern California's megalopolis stand... | third | NO ANSWER | 0.0216 | ❌ |
| 620 | Although southern california consts of a heavily d... | vast areas | NO ANSWER | 0.0581 | ❌ |
| 621 | Southern Californian communities are well known to... | suburban | NO ANSWER | 0.0110 | ❌ |
| 622 | Outside of its use of automobiles, what else is so... | highways | NO ANSWER | 0.1268 | ❌ |
| 623 | What kind of region can be found inside the urban ... | international metropolitan | larg, spread-out, suburban communities | -0.0146 | ❌ |
| 624 | What are the second and third most populated megal... | NO ANSWER | Great Lakes Megalopolis and the Northeastern megal | 0.0094 | ❌ |
| 625 | What are the dominant areas of Los Angeles? | NO ANSWER | Los Angeles, Orange County, San Diego, and Riverside-San | 0.0000 | ❌ |
| 626 | What international metropolitan region is in the N... | NO ANSWER | NO ANSWER | 0.2702 | ✅ |
| 627 | What is the main gap to continued urbanization? | Camp Pendleton | Camp Pendleton | 0.0000 | ✅ |
| 628 | Other than the San Diego metropolitan area, what o... | Inland Empire | Temecula and Murrieta | -0.1051 | ❌ |
| 629 | Who considers Los Angeles County to be a separate ... | United States Census Bureau | United States Census Bureau | 0.0000 | ✅ |
| 630 | Other than L.A. which other county do many people ... | Orange | L.A | 0.0000 | ❌ |
| 631 | Other than the 1980s, in which decade did most of ... | 1990s | 1990s | -0.5041 | ✅ |
| 632 | What was developed in 1980? | NO ANSWER | 1980s and 1990s | -0.2327 | ❌ |
| 633 | What counties to most people commute to? | NO ANSWER | NO ANSWER | 0.0116 | ✅ |
| 634 | What formed in the Coachella Valley north of Orang... | NO ANSWER | New cities | -0.0779 | ❌ |
| 635 | What counties near Kern-Bakersfield County was pop... | NO ANSWER | Bakersfield-Kern County, Santa Maria and San Luis Ob | 0.0000 | ❌ |
| 636 | What kind of climate does southern California main... | Mediterranean | Mediterranean climate | 0.0000 | ❌ |
| 637 | Other than many sunny days, what characteristic is... | infrequent rain | NO ANSWER | 0.0223 | ❌ |
| 638 | What is the low end of the temperature range in su... | 60's | 60 | -1.0000 | ❌ |
| 639 | How frequent is snow in the Southwest of the state... | very rare | NO ANSWER | 0.1001 | ❌ |
| 640 | What is the high end of the temperature range in w... | 70 | 80's | -0.5624 | ❌ |
| 641 | What type of climate does California have? | NO ANSWER | NO ANSWER | 0.0332 | ✅ |
| 642 | Where are summer temperature ranges 70-50s? | NO ANSWER | Sou Southeast of the state | -0.0841 | ❌ |
| 643 | Where are winter temperature ranges 90-60s? | NO ANSWER | In the summers | 0.0061 | ❌ |
| 644 | What is rare on the Southeast of the state? | NO ANSWER | Snow | 0.0000 | ❌ |
| 645 | What term best describes southern California's col... | varied | NO ANSWER | 0.0373 | ❌ |
| 646 | The region spans starting at islands found in whic... | Pacific Ocean | Pacific Ocean | 0.0000 | ✅ |
| 647 | What type of landscapes other than geologic and na... | topographic | Val valleys | 0.0089 | ❌ |
| 648 | The region spans which mountains other than the Tr... | Peninsular | Other Peninsular Ranges | 0.0000 | ❌ |
| 649 | The mountain ranges tail off into what kind of geo... | valleys | mounting | -0.0091 | ❌ |
| 650 | What types of collections does desert California h... | NO ANSWER | Geologic, topographic, and natural ecosystem landscapes | 0.0000 | ❌ |
| 651 | What ocean has the Transverse and Peninsular Range... | NO ANSWER | Pacific | 0.0000 | ❌ |
| 652 | What ocean has large and small interior valleys? | NO ANSWER | NO ANSWER | 0.0731 | ✅ |
| 653 | What area has the most diversity of anywhere in th... | NO ANSWER | NO ANSWER | 0.0533 | ✅ |
| 654 | How many earthquakes does southern California expe... | 10,000 | 10,000 | -0.8671 | ✅ |
| 655 | Generally speaking, what size are the earthquakes ... | small | NO ANSWER | 0.0113 | ❌ |
| 656 | What magnitude was the 1994 Northridge earthquake? | 6.7 | 6.7 | -0.9719 | ✅ |
| 657 | What kind of destruction did the 1994 earthquake c... | property damage | Property damage | 0.0000 | ✅ |
| 658 | How much was the 1994 earthquake estimated to have... | $20 billion | $20 billion | 0.0000 | ✅ |
| 659 | What year was the Northridge earthquake that cause... | NO ANSWER | NO ANSWER | 0.8057 | ✅ |
| 660 | What earthquake caused $20 million in damage? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 661 | How many earthquakes does the state of California ... | NO ANSWER | 10,000 | -0.8498 | ❌ |
| 662 | How many earthquakes are greater than a 4.7 magnit... | NO ANSWER | NO ANSWER | 0.7976 | ✅ |
| 663 | Which fault can produce a magnitude earthquake of ... | San Andreas | San Andreas Fault | 0.0000 | ❌ |
| 664 | What magnitude of earthquake can many faults produ... | 6.7 | 6.7+ | -0.5918 | ❌ |
| 665 | Other than the San Jacinto Fault, and the Elsinore... | Puente Hills | Puente Hills Fault | 0.0000 | ❌ |
| 666 | Which organization released a California Earthquak... | USGS | USGS | 0.0000 | ✅ |
| 667 | The earthquake forecast models what features of ea... | occurrence | earthquake occurrence | -0.0505 | ❌ |
| 668 | What fault can produce a magnitude 8.7 event? | NO ANSWER | NO ANSWER | 0.8034 | ✅ |
| 669 | What faults other than the San Andreas can produce... | NO ANSWER | San Jacinto Fault, the Puente Hills Fault, and the | 0.0000 | ❌ |
| 670 | What did the UGSS release? | NO ANSWER | California Earthquake forecast | 0.0000 | ❌ |
| 671 | What does the UGSS California Earthquake forecast ... | NO ANSWER | NO ANSWER | 0.0950 | ✅ |
| 672 | Southern California's distinctive regions are divi... | economically | economically | -0.0499 | ✅ |
| 673 | Outside of national recognition, what other kind o... | global | often | 0.0067 | ❌ |
| 674 | Cities that anchor the regions are often the hub f... | economic | economic | 0.0000 | ✅ |
| 675 | What are regions anchored by that are recognized g... | NO ANSWER | cities | 0.0000 | ❌ |
| 676 | What are the globally recognized anchor cities kno... | NO ANSWER | anchor of economic activity and home to many tourist destinations | 0.0000 | ❌ |
| 677 | How is California divided? | NO ANSWER | So, culturally, politically, and economically | -0.1218 | ❌ |
| 678 | Southern California had a population of 22,680,010... | 2010 | 2010 | -1.0000 | ✅ |
| 679 | What does southern California have a reputation fo... | high growth rates | high growth rates | 0.0000 | ✅ |
| 680 | What is the state average growth rate? | 10.0% | 10.0% | -1.0000 | ✅ |
| 681 | What kind of economy did northern California start... | tech-oriented | tech-oriented | 0.0000 | ✅ |
| 682 | Which region began to grow and assert itself in th... | Greater Sacramento | Greater Sacramento region | 0.0000 | ❌ |
| 683 | What census showed southern California as having a... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 684 | How much did southern California grow in the year ... | NO ANSWER | NO ANSWER | 0.6218 | ✅ |
| 685 | What economy started growing in the Greater Bay Re... | NO ANSWER | tech | 0.0000 | ❌ |
| 686 | What city is in the Greater Bay Region? | NO ANSWER | NO ANSWER | 0.2010 | ✅ |
| 687 | What is the name associated with the eight areas t... | Metropolitan Statistical Areas | Eight | -0.0318 | ❌ |
| 688 | How many extended metropolitan areas are there? | two | 4 | -0.1107 | ❌ |
| 689 | Each of the extended metropolitan areas has a popu... | five million | Five million | -0.4531 | ✅ |
| 690 | What does the El Centro metropolitan area and San ... | Southern Border Region | Southern Border Region | -0.0608 | ✅ |
| 691 | What is the population of the Greater Los Angeles ... | 17,786,419 | 17,786,419 | -1.0000 | ✅ |
| 692 | What consists of one Metropolitan Statistical Area... | NO ANSWER | Southern California | -0.4470 | ❌ |
| 693 | What consists of eight Combined Statistical Areas? | NO ANSWER | Southern California | -0.7998 | ❌ |
| 694 | What area has a population of 17,786,914? | NO ANSWER | NO ANSWER | 0.0207 | ✅ |
| 695 | What area has a population of 5,105,786? | NO ANSWER | San Diego–Tijuana | 0.0000 | ❌ |
| 696 | What areas are north of Greater Santa Barbara? | NO ANSWER | Santa Barbara, San Luis Obispo, and Bakersfield | 0.0000 | ❌ |
| 697 | What is the largest city in all of California? | Los Angeles | Los Angeles | -1.0000 | ✅ |
| 698 | What is the population of the second largest city ... | 1.3 million | 1.3 million | -0.7267 | ✅ |
| 699 | How many cities in southern California have over 2... | twelve | Tw twelve | 0.0000 | ❌ |
| 700 | There are 34 cities in southern California that ha... | 100,000 | 100,000 | -0.9549 | ✅ |
| 701 | Other than San Bernardino, which other developed s... | Riverside | Riverside | 0.0000 | ✅ |
| 702 | What are the two largest cities in the United Stat... | NO ANSWER | NO ANSWER | 0.4132 | ✅ |
| 703 | Where are there 34 cities over 200,000 in populati... | NO ANSWER | Southern California | -0.0135 | ❌ |
| 704 | Where are there 12 cities over 100,000 in populati... | NO ANSWER | South California | 0.0000 | ❌ |
| 705 | What city has a population of 3.3 million people? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 706 | What city has a population of 1.7 million people? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 707 | What resource is the economy of southern Californi... | petroleum | Pet petroleum | 0.0000 | ❌ |
| 708 | Southern California is most famous for tourism and... | Hollywood | Film | -0.1049 | ❌ |
| 709 | The region was a leader in what event between 2001... | the housing bubble | region was a leader in the housing bubble | 0.0000 | ❌ |
| 710 | Southern California's economy can be described as ... | diverse | one of the largest | 0.0000 | ❌ |
| 711 | What was the effect of the housing crash on the re... | heavily impacted | region was heavily impacted by the housing crash | 0.0000 | ❌ |
| 712 | Who does the largest economy in the United States ... | NO ANSWER | NO ANSWER | 0.4132 | ✅ |
| 713 | What took place during 2000-2017? | NO ANSWER | housing bubble | -0.0650 | ❌ |
| 714 | What is southern California's economy completely d... | NO ANSWER | pet petroleum | -0.0306 | ❌ |
| 715 | Where is southern Hollywood located? | NO ANSWER | NO ANSWER | 0.3856 | ✅ |
| 716 | Motion pictures, petroleum and aircraft manufactur... | 1920s | 1920s | -0.6176 | ✅ |
| 717 | What characteristic best describes the agricultura... | richest | NO ANSWER | 0.0350 | ❌ |
| 718 | Which type of livestock was the argricultural regi... | cattle | cattle | 0.0000 | ✅ |
| 719 | Outside of livestock, what else was considered a m... | citrus | Cit citrus | 0.0000 | ❌ |
| 720 | What industry has managed to survive major militar... | aerospace | aerospace | 0.0000 | ✅ |
| 721 | What have been major industries since 1902? | NO ANSWER | NO ANSWER | 0.1327 | ✅ |
| 722 | What were major industries until suburbs were turn... | NO ANSWER | cattle and citrus | 0.0000 | ❌ |
| 723 | What is a major factor even with aerospace cutback... | NO ANSWER | major factor | 0.0000 | ❌ |
| 724 | What year were farmlands turned into suburbs? | NO ANSWER | NO ANSWER | 0.6425 | ✅ |
| 725 | What type of district is southern California home ... | business | business districts | -0.0229 | ❌ |
| 726 | What does CBD stand for? | Central business districts | Central business districts | -0.1498 | ✅ |
| 727 | What is the only district in the CBD to not have "... | South Coast Metro | NO ANSWER | 0.0312 | ❌ |
| 728 | What does CDB stand for? | NO ANSWER | CBD | -0.4985 | ❌ |
| 729 | What does CDB include? | NO ANSWER | Business districts | -0.1808 | ❌ |
| 730 | What does DCB stand for? | NO ANSWER | DB | -0.1539 | ❌ |
| 731 | Downtown Burbank is an example of what kind of dis... | business | Local business district | 0.0000 | ❌ |
| 732 | Downtown Santa Monica and Downtown Glendale are a ... | Los Angeles Area | Los Angeles | -0.0307 | ❌ |
| 733 | Warner Center is located in which area? | San Fernando Valley | San Fernando Valley | 0.0000 | ✅ |
| 734 | Century City is an example of a district that belo... | Los Angeles | Century City | -0.0273 | ❌ |
| 735 | What business districts are within the downtown Lo... | NO ANSWER | NO ANSWER | 0.0232 | ✅ |
| 736 | What main business district is in downtown Los Ang... | NO ANSWER | Downtown Los Angeles | 0.0000 | ❌ |
| 737 | What additional business districts are in downtown... | NO ANSWER | Downtown Los Angeles central business district as well as those lining the | 0.0000 | ❌ |
| 738 | The Sand Bernardino - Riverside area maintains wha... | business | Business districts | -0.0231 | ❌ |
| 739 | Other than San Bernardino, what is the name of the... | Riverside | Riverside | 0.0000 | ✅ |
| 740 | Other than Downtown San Bernardino, and University... | Hospitality Business/Financial Centre | Hospital Hospitality Business/Financial Centre | -0.0368 | ❌ |
| 741 | What business districts does the San Bernardino ar... | NO ANSWER | Downtown San Bernardino, Hospitality Business/Financial Centre, University Town | -0.0215 | ❌ |
| 742 | What business districts does the Riverside area ma... | NO ANSWER | Hospital, Business/Financial Centre, University Town | -0.0385 | ❌ |
| 743 | Which county is developing its business center? | Orange | Orange | -1.0000 | ✅ |
| 744 | Where are international corporations headquartered... | University of California, Irvine | University of California, Irvine | 0.0000 | ✅ |
| 745 | Jamboree Business Parks belongs to which business ... | West Irvine | West Irvine | 0.0000 | ✅ |
| 746 | What other business district does Orange County en... | South Coast Metro | South Coast Metro | 0.0000 | ✅ |
| 747 | At what rate is Orange County developing its busin... | rapidly | NO ANSWER | 0.2135 | ❌ |
| 748 | What county does the rapidly developing downtown S... | NO ANSWER | Orange | -1.0000 | ❌ |
| 749 | What districts does downtown Santa Ana include? | NO ANSWER | South Coast Metro and Newport Center | 0.0000 | ❌ |
| 750 | What locations are headquartered at the California... | NO ANSWER | University of California, Irvine | 0.0098 | ❌ |
| 751 | What includes Irvine Center Tech and Business Jamb... | NO ANSWER | West Irvine | 0.0000 | ❌ |
| 752 | What is the central business district of San Diego... | Downtown San Diego | Downtown San Diego | -1.0000 | ✅ |
| 753 | Other than its main central  business district, wh... | Northern San Diego | Northern San Diego and some within North County regions | 0.0000 | ❌ |
| 754 | Outside of Northern San Diego, which other region ... | North County | NO ANSWER | 0.0182 | ❌ |
| 755 | University City is an example of a business distri... | San Diego | NO ANSWER | 0.0255 | ❌ |
| 756 | What is the central business district of downtown ... | NO ANSWER | Downtown San Diego | -0.8068 | ❌ |
| 757 | What are located in Northern downtown San Diego? | NO ANSWER | NO ANSWER | 0.0804 | ✅ |
| 758 | What business districts are located in Northern do... | NO ANSWER | NO ANSWER | 0.1466 | ✅ |
| 759 | What is the second busiest airport in the United S... | Los Angeles International Airport | Los Angeles International Airport | 0.0000 | ✅ |
| 760 | What is the metric they use to determine how busy ... | passenger volume | NO ANSWER | 0.0568 | ❌ |
| 761 | What ranking in terms of busiest airports from int... | third | third | 0.0000 | ✅ |
| 762 | Which airport is home to the busiest single runway... | San Diego International Airport | San Diego International Airport | 0.0000 | ✅ |
| 763 | What is the world's busiest general aviation airpo... | Van Nuys Airport | Van Nuys Airport | 0.0000 | ✅ |
| 764 | What is the busiest airport by passenger volume in... | NO ANSWER | NO ANSWER | 0.2529 | ✅ |
| 765 | What is the second-busiest single runway airport i... | NO ANSWER | NO ANSWER | 0.4874 | ✅ |
| 766 | What is the second-busiest general aviation airpor... | NO ANSWER | NO ANSWER | 0.0855 | ✅ |
| 767 | What major commercial airports are located in Los ... | NO ANSWER | Los Angeles, Burbank, and Long Beach | 0.0000 | ❌ |
| 768 | What is the name of the commuter rail system? | Metrolink | Metrolink | 0.0000 | ✅ |
| 769 | How many lines does the commuter rail system have? | seven | 7 | -0.0274 | ❌ |
| 770 | How many lines run out of Downtown Los Angeles? | Six | 6 | -0.6551 | ❌ |
| 771 | A single line connects San Bernardino, Riverside a... | Orange | Orange | 0.0000 | ✅ |
| 772 | Where do seven lines of Metrolink run out of? | NO ANSWER | Downtown Los Angeles | 0.0000 | ❌ |
| 773 | What is the name of the Los Angeles rail system? | NO ANSWER | Metrolink | 0.0000 | ❌ |
| 774 | What counties are connected to Los Angeles, Ventur... | NO ANSWER | Vent, San Bernardino | -0.0017 | ❌ |
| 775 | What is the United States busiest commercial port? | Port of Los Angeles | NO ANSWER | 0.0530 | ❌ |
| 776 | What is the second busiest container port in the U... | Port of San Diego | Port of Long Beach | 0.0000 | ❌ |
| 777 | The Port of Long Beach belongs to which region of ... | Southern | Southern California | -0.6355 | ❌ |
| 778 | What is home to Southern California? | NO ANSWER | Ports | -0.0293 | ❌ |
| 779 | What is the busiest container port in the United S... | NO ANSWER | NO ANSWER | 0.2115 | ✅ |
| 780 | What is the Port of San Diego adjacent to? | NO ANSWER | United States | -0.0407 | ❌ |
| 781 | What is the United State's second-busiest commerci... | NO ANSWER | United States' second busiest container port | 0.0000 | ❌ |
| 782 | What is the moniker that is being used to describe... | The Tech Coast | Tech Coast | -0.8982 | ❌ |
| 783 | What kind of universities is the region famous for... | research | Public and private institutions | -0.0303 | ❌ |
| 784 | What kind of university is the California Institut... | private | Private | 0.0000 | ✅ |
| 785 | How many campuses does the University of Californi... | 5 | 5 | -0.6984 | ✅ |
| 786 | How many campuses does the California State Univer... | 12 | 12 | -0.8951 | ✅ |
| 787 | What are the 5 California University campuses? | NO ANSWER | Irvine, Los Angeles, Riverside, Santa Barbara, and San | -0.4196 | ❌ |
| 788 | How many California University campuses are there? | NO ANSWER | 21 | 0.0000 | ❌ |
| 789 | How many State of California University campuses a... | NO ANSWER | 12 | -0.0354 | ❌ |
| 790 | Where is Redland University located? | NO ANSWER | NO ANSWER | 0.1590 | ✅ |
| 791 | Where is Pomona University located? | NO ANSWER | NO ANSWER | 0.0839 | ✅ |
| 792 | The Los Angeles Rams are an example of what kind o... | NFL | National | -0.1083 | ❌ |
| 793 | The Los Angeles Clippers are a team belonging to w... | NBA | NBA | 0.0000 | ✅ |
| 794 | The Los Angeles Angels of Anaheim are from which s... | MLB | ML | 0.0000 | ❌ |
| 795 | What is the other NHL team aside from the Anaheim ... | Los Angeles Kings | Los Angeles Kings | -0.9417 | ✅ |
| 796 | What is the lone MLS team that belongs to southern... | LA Galaxy | LA Galaxy | -0.7947 | ✅ |
| 797 | What NLF teams are from Southern California? | NO ANSWER | Los Angeles Rams, Los Angeles Chargers | -0.6869 | ❌ |
| 798 | What NAB teams are from Southern California? | NO ANSWER | NFL, NBA, MLB, NHL, and MLS | -0.4063 | ❌ |
| 799 | What MBL teams are from Southern California? | NO ANSWER | Los Angeles Dodgers, Los Angeles Angels of Anaheim | -0.6603 | ❌ |
| 800 | What NLH teams are from Southern California? | NO ANSWER | Los Angeles Kings, Anaheim Ducks | -0.4452 | ❌ |
| 801 | What MSL team is from Southern California? | NO ANSWER | LA Galaxy | -0.8422 | ❌ |
| 802 | Which team was suspended from the MLS? | Chivas USA | Chivas USA | 0.0000 | ✅ |
| 803 | How many teams did Los Angeles used to have? | two | Two | 0.0000 | ✅ |
| 804 | Which year resulted in the suspension of one of th... | 2014 | 2014 | -1.0000 | ✅ |
| 805 | What was the name of the stadium that the teams pl... | StubHub Center | StubHub Center | 0.0000 | ✅ |
| 806 | When is the suspended team scheduled to return? | 2018 | 2018 | -0.7035 | ✅ |
| 807 | How many Major Soccer League teams were in Los Ang... | NO ANSWER | Two | 0.0000 | ❌ |
| 808 | What Major Soccer League teams played in Los Angel... | NO ANSWER | LA Galaxy and Chivas USA | 0.0000 | ❌ |
| 809 | When were the LA Galaxy suspended? | NO ANSWER | NO ANSWER | 0.6834 | ✅ |
| 810 | When is a second MSL team scheduled to return? | NO ANSWER | 2018 | -0.6805 | ❌ |
| 811 | What other kind of sport is popular in southern Ca... | College | College sports | -0.3863 | ❌ |
| 812 | The Bruins belong to which college? | UCLA | UCLA | 0.0000 | ✅ |
| 813 | What is the name of the team from USC? | Trojans | Trojans | 0.0000 | ✅ |
| 814 | Which conference do the teams in southern Californ... | Pac-12 | Pac-12 Conference | 0.0000 | ❌ |
| 815 | The two listed teams play for which NCAA group? | Division I | NO ANSWER | 0.0213 | ❌ |
| 816 | What is the ULCA mascot? | NO ANSWER | NO ANSWER | 0.0308 | ✅ |
| 817 | What is the UCS mascot? | NO ANSWER | Brujans | 0.0000 | ❌ |
| 818 | What conference are both ULCA and UCS part of? | NO ANSWER | NO ANSWER | 0.0510 | ✅ |
| 819 | What is a growing sport in southern California? | Rugby | Rugby | -0.9116 | ✅ |
| 820 | At which level of education is this sport becoming... | high school | high school | 0.0000 | ✅ |
| 821 | What is rugby rapidly becoming with high schools? | an official school sport | official school sport | -0.0212 | ❌ |
| 822 | What sport is growing in all California schools? | NO ANSWER | Rugby | -0.2956 | ❌ |
| 823 | What company was formed by the merger of Sky Telev... | BSkyB | BSkyB | 0.0000 | ✅ |
| 824 | Who is the UK's largest digital subscription telev... | BSkyB | NO ANSWER | 0.0449 | ❌ |
| 825 | What year did BSkyB acquire Sky Italia? | 2014 | 2014 | -1.0000 | ✅ |
| 826 | What is the name of the holding company for BSkyB? | Sky plc | British Sky Broadcasting Group plc | 0.0000 | ❌ |
| 827 | What is the name of the United Kingdom operation f... | Sky UK Limited | Sky UK Limited | 0.0000 | ✅ |
| 828 | What company was angry about the merger of Sky Tel... | NO ANSWER | NO ANSWER | 0.7638 | ✅ |
| 829 | Who is the UK's smallest digital subscription tele... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 830 | What year did BSkyB remove Sky Italia? | NO ANSWER | NO ANSWER | 0.8977 | ✅ |
| 831 | When did BSkyB become the largest US television co... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 832 | What company no longer trades as Sky? | NO ANSWER | NO ANSWER | 0.0258 | ✅ |
| 833 | What year was Setanta Sports awarded Primeier Leag... | 2006 | 2006 | -0.8658 | ✅ |
| 834 | How many of the six total packages available to br... | two | two | -0.1673 | ✅ |
| 835 | Who purhcased the remaining 4 pacakages available ... | Sky | Sky | 0.0000 | ✅ |
| 836 | How much did Sky bid to win the 4 broadcast pacakg... | £1.3bn | £4.2bn | 0.0000 | ❌ |
| 837 | Which company had a short legal battle with the Eu... | NO ANSWER | BSkyB | 0.0000 | ❌ |
| 838 | How many of the six total packages available to br... | NO ANSWER | Two | -0.1613 | ❌ |
| 839 | Sky lost how many packages? | NO ANSWER | 2 | -0.3183 | ❌ |
| 840 | How much did Sky bid to lose the 4 broadcast packa... | NO ANSWER | NO ANSWER | 0.1216 | ✅ |
| 841 | What channel was never dropped from Sky? | NO ANSWER | NO ANSWER | 0.6240 | ✅ |
| 842 | What consortium was BSkyB excluded from? | ONdigital | ONdigital | 0.0000 | ✅ |
| 843 | Who did BSkyB team up with because it was not part... | Freeview | NO ANSWER | 0.0424 | ❌ |
| 844 | How many BSkyB channels were available to customer... | three | 3 | 0.0000 | ❌ |
| 845 | What channel replaced Sky Travel? | Sky Three | Sky Three | 0.0000 | ✅ |
| 846 | What was Sky Travel later rebranded as? | Pick TV | Pick TV | -1.0000 | ✅ |
| 847 | What consortium was BSkyB included with? | NO ANSWER | ONdigital | -0.0157 | ❌ |
| 848 | What was Pick TV later rebranded as? | NO ANSWER | Pick | -0.9774 | ❌ |
| 849 | What channel came before Sky Travel? | NO ANSWER | Sky News | 0.0000 | ❌ |
| 850 | Who did BSkyB team up with because it was part of ... | NO ANSWER | It was ITV Digital | 0.0000 | ❌ |
| 851 | What channel was never rebranded? | NO ANSWER | NO ANSWER | 0.3588 | ✅ |
| 852 | What service did BSkyB chare additional subscripti... | Sky+ PVR | Sky+ PVR | -0.0301 | ✅ |
| 853 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | 0.0000 | ✅ |
| 854 | WHat allows customers to get Sky+ functions if the... | monthly fee | NO ANSWER | 0.0573 | ❌ |
| 855 | When did BSkyB discontinue the Sky+ Box? | January 2010 | January 2010 | -0.2913 | ✅ |
| 856 | What replaced the Sky+Box? | Sky+HD Box | Sky+HD Box | 0.0000 | ✅ |
| 857 | What service did BSkyB give away for free uncondit... | NO ANSWER | Sky+ | -0.0111 | ❌ |
| 858 | When did Sky launch a TV advertising campaign targ... | NO ANSWER | NO ANSWER | 0.8646 | ✅ |
| 859 | What isn't required by customers to get Sky+ funct... | NO ANSWER | NO ANSWER | 0.0226 | ✅ |
| 860 | When did BSkyB upgrade the Sky+ Box? | NO ANSWER | January 2010 | -0.4244 | ❌ |
| 861 | What replaced the Sky+HD Box? | NO ANSWER | smaller version of the SkyHD box without Sky+ functionality | 0.0000 | ❌ |
| 862 | What is the name of the TV scrambling system BSkyB... | VideoGuard | VideoGuard | 0.0000 | ✅ |
| 863 | Who is VideoGuard owned by? | NDS | Cisco Systems | 0.0000 | ❌ |
| 864 | Who is the parent company of NDS? | Cisco Systems | Cisco Systems | 0.0000 | ✅ |
| 865 | Who has design authority over all of the digital s... | BSkyB | BSkyB | -1.0000 | ✅ |
| 866 | What is the name brand of the personal video recor... | Sky+ | Sky+ | 0.0000 | ✅ |
| 867 | What is the name of the TV scrambling system BSkyB... | NO ANSWER | NO ANSWER | 0.3433 | ✅ |
| 868 | Whose digital receivers are only built by one manu... | NO ANSWER | They | -0.1400 | ❌ |
| 869 | What is available as stand-alone DVB CAMs? | NO ANSWER | NO ANSWER | 0.4812 | ✅ |
| 870 | What company was never involved with NDS? | NO ANSWER | NO ANSWER | 0.1805 | ✅ |
| 871 | What is the name brand of the video recorder that ... | NO ANSWER | NO ANSWER | 0.3484 | ✅ |
| 872 | What year did BSkyB and Virgin Media have a disput... | 2007 | 2007 | -1.0000 | ✅ |
| 873 | What channels were removed from the network in Mar... | basic channels | NO ANSWER | 0.1476 | ❌ |
| 874 | What did Virgin Media claim BSkyB did that resulte... | substantially increased the asking price | Virginia Media claimed that BSkyB substantially increased the asking price for | -0.2017 | ❌ |
| 875 | What additional srevice did BSkyB offer besides HD... | Video On Demand | Video On Demand content | 0.0000 | ❌ |
| 876 | What additional srevice did BSkyB offer besides Vi... | HD channels | HD channels | 0.0000 | ✅ |
| 877 | What year did BSkyB and Virgin Media have an agree... | NO ANSWER | NO, the dispute was in 2007 | -0.5175 | ❌ |
| 878 | What channels were always available on the network... | NO ANSWER | NO ANSWER | 0.4571 | ✅ |
| 879 | What additional service did BSkyB offer besides HD... | NO ANSWER | NO ANSWER | 0.0252 | ✅ |
| 880 | What claim did BSkyB agree with? | NO ANSWER | NO ANSWER | 0.1751 | ✅ |
| 881 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 882 | when did the English High court find Microsoft's u... | July 2013 | July 2013 | -0.1067 | ✅ |
| 883 | What year did BSkyB and Microsoft announce their s... | 2013 | 2013 | -1.0000 | ✅ |
| 884 | What did Microsoft announce that it would rename S... | OneDrive | "OneDrive" | -0.9401 | ❌ |
| 885 | What did Microsoft announce that it would rename S... | OneDrive for Business | OneDrive for Business | -0.9305 | ✅ |
| 886 | What kind of service is the SkyDrive Service? | cloud storage | Cloud storage service | 0.0000 | ❌ |
| 887 | When did the English High Court of Justice find th... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 888 | When did Microsoft decide to appeal the ruling? | NO ANSWER | NO ANSWER | 0.9474 | ✅ |
| 889 | What did Microsoft announce that it would rename O... | NO ANSWER | After an unspecified "reasonable period of time to allow for an orderly | -0.4345 | ❌ |
| 890 | What did Microsoft announce that it would rename O... | NO ANSWER | None, the new brand for OneDrive for Business and OneDrive | -0.7995 | ❌ |
| 891 | When did Microsoft announce OneDrive will soon bec... | NO ANSWER | 2014 | -0.7790 | ❌ |
| 892 | Who was the chief executive officer when the servi... | Sam Chisholm | Sam Chisholm | 0.0000 | ✅ |
| 893 | Who's satellites would the new free-to-air channel... | Astra | Astra's | 0.0000 | ❌ |
| 894 | When did BSkyB end their analogue service? | 27 September 2001 | 27 September 2001 | -1.0000 | ✅ |
| 895 | What platform caused BSkyB to end their analogue s... | Sky Digital | launch and expansion of the Sky Digital platform | -0.8872 | ❌ |
| 896 | How many households had BSkyB service in 1994? | 3.5 million | 3.5 million | -1.0000 | ✅ |
| 897 | What platform helped BSkyB to avoid ending their a... | NO ANSWER | launch and expansion of the Sky Digital platform | -0.6596 | ❌ |
| 898 | Whose satellites were never broadcast as free-to-a... | NO ANSWER | NO ANSWER | 0.0478 | ✅ |
| 899 | How many subscribers were lost within two months o... | NO ANSWER | NO ANSWER | 0.7435 | ✅ |
| 900 | Who commended the operations in front of the Selec... | NO ANSWER | Michael Grade | 0.0000 | ❌ |
| 901 | Which company never expanded their platform? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 902 | Sky UK Limited is formerly known by what name? | BSkyB | British Sky Broadcasting or BSkyB | 0.0000 | ❌ |
| 903 | What kind of company is Sky UK Limited? | telecommunications | telecommunications company | -0.0219 | ❌ |
| 904 | How many customers does Sky UK Limited have as a p... | 11 million | 11 million | -1.0000 | ✅ |
| 905 | what other digital TV service took Sky UK Limited'... | Freeview | Freeview | 0.0000 | ✅ |
| 906 | Sky UK Limited is now known by what name? | NO ANSWER | Sky UK Limited (formerly British Sky Broadcasting or BSkyB) | -0.5937 | ❌ |
| 907 | What has Sky UK Limited never been involved with? | NO ANSWER | NO ANSWER | 0.4392 | ✅ |
| 908 | How many customers did Sky UK Limited lose as a pa... | NO ANSWER | Its corporate headquarters are based in Isleworth | -0.1674 | ❌ |
| 909 | What was the UK's least popular TV service in 2015... | NO ANSWER | NO ANSWER | 0.7904 | ✅ |
| 910 | Where did the headquarters relocate from? | NO ANSWER | NO ANSWER | 0.1782 | ✅ |
| 911 | What is the name of Sky Q's broadband router? | Sky Q Hub | Sky Q Hub | -0.8882 | ✅ |
| 912 | What are the Sky Q mini set top boxes able to conn... | Sky Q Silver set top boxes | Other Sky Q set top boxes with a Wi-Fi or Power-line | -0.2701 | ❌ |
| 913 | What does connecting different Sky Q boxes enable ... | share recordings | share recordings and other media | 0.0000 | ❌ |
| 914 | When is Sky going to introduce UHD broadcasts? | 2016 | later in 2016 | -0.0445 | ❌ |
| 915 | When are the new Sky Q products going to be availa... | 2016 | 2016 | -0.4548 | ✅ |
| 916 | What is the name of Sky Q's dial-up router? | NO ANSWER | NO ANSWER | 0.3406 | ✅ |
| 917 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | Nothing | -0.0990 | ❌ |
| 918 | What does disconnecting different Sky Q boxes enab... | NO ANSWER | Sky Q Mini set top boxes connect to the Sky Q Silver | 0.0000 | ❌ |
| 919 | What set top box can no longer display UHD broadca... | NO ANSWER | Sky Q Mini | -0.3363 | ❌ |
| 920 | What are BSkyB's standard definition broadcasts co... | DVB-compliant MPEG-2 | DVB | 0.0000 | ❌ |
| 921 | Sky Movies and Sky Box office also include what op... | Dolby Digital | DVB-compliant MPEG-2, with the Sky Movies and | 0.0000 | ❌ |
| 922 | What is Sky+ HD material broadcast using? | MPEG-4 | MPG-4 | 0.0000 | ❌ |
| 923 | What is the proprietary system that Sky+HD uses? | OpenTV | OpenTV | 0.0000 | ✅ |
| 924 | What does most of the HD material use as a standar... | DVB-S2 | DVB-S2 | 0.0000 | ✅ |
| 925 | What box is required to view MPEG-3? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 926 | What is the proprietary system that Sky+HD can't u... | NO ANSWER | NO ANSWER | 0.0561 | ✅ |
| 927 | What channel never used looping video streams? | NO ANSWER | NO ANSWER | 0.8078 | ✅ |
| 928 | What kind of soundtracks are mandatory with the Sk... | NO ANSWER | NO ANSWER | 0.1992 | ✅ |
| 929 | When was Sky Digital launched? | 1998 | 1998 | -1.0000 | ✅ |
| 930 | What satellite was used when Sky digital was launc... | Astra 2A | Astra 2A | -1.0000 | ✅ |
| 931 | What satellite enabled Sky Digital to launch an al... | Eutelsat's Eurobird 1 | Astra 2A | -0.5470 | ❌ |
| 932 | How many television and radio channels could the n... | hundreds | hundreds | 0.0000 | ✅ |
| 933 | What is the position of the satellite that allowed... | 28.5°E | 28.5°E | -1.0000 | ✅ |
| 934 | What service used Astra 2A in 1995? | NO ANSWER | NO ANSWER | 0.6216 | ✅ |
| 935 | What satellite made it impossible for Sky Digital ... | NO ANSWER | NO ANSWER | 0.3470 | ✅ |
| 936 | How many television and radio channels did the dig... | NO ANSWER | NO ANSWER | 0.0173 | ✅ |
| 937 | When was the only satellite launched? | NO ANSWER | NO ANSWER | 0.6365 | ✅ |
| 938 | When did BSkyB launch it's HDTV service? | 22 May 2006 | 22 May 2006 | -0.9559 | ✅ |
| 939 | How many people were registered to receive the HD ... | 40,000 | 40,000 | -1.0000 | ✅ |
| 940 | What was the name of the set top box manufacturer ... | Thomson | Th Thomson | 0.0000 | ❌ |
| 941 | What was the number of customers that the BBC  rep... | 17,000 | 17,000 | -1.0000 | ✅ |
| 942 | What was the total number of homes Sky announced t... | 4,222,000 | 4,222,000 | -1.0000 | ✅ |
| 943 | When did BSkyB fail launching it's HDTV service? | NO ANSWER | NO ANSWER | 0.4118 | ✅ |
| 944 | Which manufacturer never had supply issues when de... | NO ANSWER | NO ANSWER | 0.9064 | ✅ |
| 945 | How many people never registered to receive the HD... | NO ANSWER | 40,000 | -0.3531 | ❌ |
| 946 | Who reported that 17,000 customers received the se... | NO ANSWER | BBC | 0.0000 | ❌ |
| 947 | When did Sky announce the total number of homes wi... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 948 | When did BSkyB announce it's intention to replace ... | 8 February 2007 | 8 February 2007 | -1.0000 | ✅ |
| 949 | When did Setanta Sports say it would launch as a s... | March | March | 0.0000 | ✅ |
| 950 | What platform was Sentanta Sports planning on laun... | digital terrestrial | freeview | -0.0151 | ❌ |
| 951 | What were NTL's services rebranded as? | Virgin Media | Virgin Media | 0.0000 | ✅ |
| 952 | What does BSkyB's sport portfolio include? | English Premier League Football | English Premier League Football | 0.0000 | ✅ |
| 953 | When did BSkyB announce it's intention to improve ... | NO ANSWER | On 8 February 2007 | -1.0000 | ❌ |
| 954 | When did Setanta Sports say it would launch as a f... | NO ANSWER | NO ANSWER | 0.1893 | ✅ |
| 955 | What platform was Sentanta Sports planning to avoi... | NO ANSWER | NO ANSWER | 0.0504 | ✅ |
| 956 | What was Virgin Media rebranded as? | NO ANSWER | NTB | 0.0000 | ❌ |
| 957 | What channel lost advertising revenue due to their... | NO ANSWER | NO ANSWER | 0.2650 | ✅ |
| 958 | What are free-to-air encrypted broadcasts known as... | free-to-view | Free-to-view | 0.0000 | ✅ |
| 959 | What do some encrypted broadcasts require to view? | monthly subscription | monthly subscription | 0.0000 | ✅ |
| 960 | What does a receiver have to be equipped with to v... | VideoGuard UK | VideoGuard UK | 0.0000 | ✅ |
| 961 | What is the universal band that digital recievers ... | Ku band | 9.75/10.600 GHz | -0.4298 | ❌ |
| 962 | What service is a VideoGuard UK equipped receiver ... | Sky | Sky service | 0.0000 | ❌ |
| 963 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | 0.0338 | ✅ |
| 964 | What does a receiver have to be equipped with to v... | NO ANSWER | NO ANSWER | 0.2735 | ✅ |
| 965 | What is the localized band that digital receivers ... | NO ANSWER | band | -0.3293 | ❌ |
| 966 | What service is a VideoGuard UK equipped receiver ... | NO ANSWER | Sky service | 0.0000 | ❌ |
| 967 | What band is fitted in the middle of the satellite... | NO ANSWER | 10.600 GHz | -0.2833 | ❌ |
| 968 | When were the talks held for braodcast right to th... | 1991 | autm of 1991 | -0.4041 | ❌ |
| 969 | Who were the current rights holders for the Primer... | ITV | IT ITV | 0.0000 | ❌ |
| 970 | What did ITV increase their yearly offer for contr... | £34m | £34m | 0.0000 | ✅ |
| 971 | Who was given the highlights of most of the matche... | BBC | BBC | 0.0000 | ✅ |
| 972 | How much was BSkyB going to pay for the Primier Le... | £304m | £304m | -0.0492 | ✅ |
| 973 | What company was not concerned about retaining new... | NO ANSWER | NO ANSWER | 0.6612 | ✅ |
| 974 | How much did BSkyB pay to give up their rights for... | NO ANSWER | £304m | 0.0033 | ❌ |
| 975 |  Who never saw highlights of most of the matches? | NO ANSWER | It was ITV | -0.0123 | ❌ |
| 976 | Who were never rights holders for the Premier Leag... | NO ANSWER | NO ANSWER | 0.2481 | ✅ |
| 977 | Who does BSkyB have an operating license from? | Ofcom | Ofcom | 0.0000 | ✅ |
| 978 | what is the fee range for accessing BSkyB's EPG? | £15–100,000 | £15–100,000 | 0.0000 | ✅ |
| 979 | Can BSkyB veto the presence of channels on their E... | no | NO ANSWER | 1.0000 | ❌ |
| 980 | Does BSkyB carry any control over a channels conte... | not | NO ANSWER | 0.8893 | ❌ |
| 981 | Does BSkyB carry any control over the picture qual... | not | NO ANSWER | 0.8383 | ❌ |
| 982 | Who took away the operating license from BSkyB? | NO ANSWER | Ofcom | 0.0000 | ❌ |
| 983 | What company has veto over the presence of channel... | NO ANSWER | NO ANSWER | 0.3066 | ✅ |
| 984 | What can BSkyB veto the presence of channels on? | NO ANSWER | NO ANSWER | 0.3573 | ✅ |
| 985 | What service doesn't require a fee to use? | NO ANSWER | NO ANSWER | 0.0333 | ✅ |
| 986 | When was BSkyB's digital service launched? | 1 October 1998 | 1 October 1998 | -1.0000 | ✅ |
| 987 | What was the name of BSkyB's digital service launc... | Sky Digital | Sky Digital | 0.0000 | ✅ |
| 988 | What did BSkyB name their interactive service? | Sky Active | Sky Active | 0.0000 | ✅ |
| 989 | Who did BSkyB compete with initially? | ONdigital | IT and ITV Digital | -0.2201 | ❌ |
| 990 | Within the 30 days how many digiboxes had been sol... | 100,000 | 100,000 | -0.6479 | ✅ |
| 991 | When was BSkyB's digital service unofficially laun... | NO ANSWER | NO ANSWER | 0.2291 | ✅ |
| 992 | What company supported BSkyB the most? | NO ANSWER | NO ANSWER | 0.4384 | ✅ |
| 993 | Within 30 days how many digiboxes had been discard... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 994 | When did BSkyB decide to stop giving away free dig... | NO ANSWER | NO ANSWER | 0.8621 | ✅ |
| 995 | When was virgin media rebranded from NTL Telewest? | 2007 | 2007 | -1.0000 | ✅ |
| 996 | what was NTL Telewest re-branded to in 2007? | Virgin Media | Virgin Media | -1.0000 | ✅ |
| 997 | What did Virgin Media concentrate on instead of of... | Video On Demand | Video On Demand service | -0.0271 | ❌ |
| 998 | What was the one linear HD channel Virgin Media ca... | BBC HD | BBC HD | 0.0000 | ✅ |
| 999 | what was the name of the other HD channel Virgin m... | Channel 4 HD | Channel 4 HD | 0.0000 | ✅ |

**correct binary classification:** 71.20% (712/1000)

============================================================
Trial: full_data_set_202602170639
============================================================
Overall EM:        55.20
Overall F1:        61.41
NoAns Accuracy:    58.49% (286/489)
HasAns F1:         64.21
HasAns EM:         52.05
Total Questions:   1000 (HasAns: 511, NoAns: 489)
correct binary classification: 71.20% (712/1000)
============================================================

Detailed Metrics:
('exact', 55.2)
('f1', 61.41)
('total', 1000)
('HasAns_exact', 52.055)
('HasAns_f1', 64.208)
('HasAns_total', 511)
('NoAns_exact', 58.487)
('NoAns_f1', 58.487)
('NoAns_total', 489)
('best_exact', 55.2)
('best_exact_thresh', 0.0)
('best_f1', 61.41)
('best_f1_thresh', 0.0)
============================================================

---

## full_data_set_202602171357
**Timestamp:** 2026-02-17 13:57:09

**Dataset:** dev-data/full_data_set-results.csv

### Metrics

| Metric | Value |
|--------|-------|
| **Overall EM** | 55.40 |
| **Overall F1** | 62.15 |
| **NoAns Accuracy** | 58.69% (287/489) |
| **HasAns F1** | 65.47 |
| **HasAns EM** | 52.25 |
| **Total Questions** | 1000 (HasAns: 511, NoAns: 489) |
| **Binary Classification** | 71.30% (713/1000) |

### Detailed Results

| Index | Question | Actual Answer | Model Prediction | Margin | Status |
|-------|----------|---------------|------------------|--------|--------|
| 0 | Who did Alexander I marry? | Sybilla of Normandy | Sybilla of Normandy | -0.0256 | ✅ |
| 1 | What culture's arrival in Scotland is know as the ... | Norman | Normans | -0.8032 | ❌ |
| 2 | Who did King David I of Scotland Marry? | NO ANSWER | David's sister Maud of Scotland | -0.4035 | ❌ |
| 3 | What did Sybilla of Normandy introduce to Scotland... | NO ANSWER | King David I of Scotland | -0.2908 | ❌ |
| 4 | Where was Ralph earl of? | Hereford | Hereford | 0.0000 | ✅ |
| 5 | Who was Ralph in charge of being at war with? | the Welsh | the Welsh | 0.0000 | ✅ |
| 6 | Who made Ralph earl? | Edward the Confessor | Edward the Confessor | 0.0000 | ✅ |
| 7 | Who came into contact with Wales after the conques... | NO ANSWER | NO ANSWER | 0.2437 | ✅ |
| 8 | Who made Edward the Confessor Earl? | NO ANSWER | King Edward | 0.0000 | ❌ |
| 9 | What country was under the control of Norman baron... | Wales | Wales | 0.0027 | ✅ |
| 10 | What came under Williams dominace before the conqu... | NO ANSWER | NO ANSWER | 0.0445 | ✅ |
| 11 | What Welsh lords did William conquer? | NO ANSWER | NO ANSWER | 0.2859 | ✅ |
| 12 | What year did Roger de Tosny fail to accomplish wh... | 1018 | 1018 | -1.0000 | ✅ |
| 13 | Who was in charge of the papal army in the War of ... | William of Montreuil | William of Montreuil | 0.0000 | ✅ |
| 14 | Where did the Normans carve out a principality bef... | NO ANSWER | NO ANSWER | 0.1014 | ✅ |
| 15 | What did the Normans take part in in the 10th cent... | NO ANSWER | Requista | -0.4537 | ❌ |
| 16 | Who carved out a state for himself from Moorish la... | NO ANSWER | Roger de Tosny | 0.0000 | ❌ |
| 17 | What war occured in the 1oth century? | NO ANSWER | War of Barbastro | -0.0912 | ❌ |
| 18 | When did the Siege of Antioch take place? | 1097 | 1097 | -0.9491 | ✅ |
| 19 | What was the name of Bohemond's nephew? | Tancred | Tancred | 0.0000 | ✅ |
| 20 | What major conquest did Tancred play a roll in? | Jerusalem | Conj conquest of Jerusalem | 0.0000 | ❌ |
| 21 | When did Tancred lay siege to Antioch? | NO ANSWER | NO ANSWER | 0.8218 | ✅ |
| 22 | What was the name of Tancred's nephew? | NO ANSWER | Tancred | 0.0000 | ❌ |
| 23 | How long did Western Europe control Cyprus? | 380 years | 380 years | -1.0000 | ✅ |
| 24 | Who defeated Anglo-Norman forces during the third ... | NO ANSWER | NO ANSWER | 0.9600 | ✅ |
| 25 | Who dominated Western Europe for 380 years? | NO ANSWER | Ang Anglo-Norman forces | -0.1995 | ❌ |
| 26 | What ruined Richard's plans to reach Acre? | a storm | storm | 0.0000 | ❌ |
| 27 | Who was Richard's fiancee? | Berengaria | Berengaria | 0.0000 | ✅ |
| 28 | What year did the storm hit Richard's fleet? | 1191 | April 1191 | -0.0712 | ❌ |
| 29 | Who ruled Cyprus in 1191? | Isaac Komnenos | Is Isaac Komnenos | 0.0000 | ❌ |
| 30 | Who left Messina in the 11th century? | NO ANSWER | NO ANSWER | 0.2906 | ✅ |
| 31 | What year did Richards fleet avoid a storm? | NO ANSWER | 1191 | -0.5485 | ❌ |
| 32 | Who ruled Cyprus in the 11th century? | NO ANSWER | NO ANSWER | 0.0941 | ✅ |
| 33 | Who was Guy's Rival? | Conrad of Montferrat | Con Conrad of Montferrat | 0.0000 | ❌ |
| 34 | What were Isaac's chains made out of? | silver | NO ANSWER | 0.0113 | ❌ |
| 35 | Who led Richard's troops when Cyprus was conquered... | Guy de Lusignan | Guy de Lusignan | 0.0000 | ✅ |
| 36 | Who's chains were made out of copper? | NO ANSWER | NO ANSWER | 0.8322 | ✅ |
| 37 | Who led Issacs troops to Cyprus? | NO ANSWER | NO ANSWER | 0.1870 | ✅ |
| 38 | Who offered Issac his daughter? | NO ANSWER | The person named by Richard | 0.0000 | ❌ |
| 39 | Who became the King of the Canary Islands? | Bethencourt | Henry III of Castile | -0.1700 | ❌ |
| 40 | Who bought the rights? | Enrique Pérez de Guzmán | En Enrique Pérez de Guzmán, 2nd Count | 0.0000 | ❌ |
| 41 | Who sold the rights? | Maciot de Bethencourt | Jean's nephew Maciot de Bethencourt | 0.0000 | ❌ |
| 42 | What title did Henry II take in the Canary Island? | NO ANSWER | NO ANSWER | 0.1454 | ✅ |
| 43 | Who sold the rights to the island in the 14th cent... | NO ANSWER | Maciot de Bethencourt | 0.0000 | ❌ |
| 44 | Where are Jersey and Guernsey | Channel Islands | The Channel Islands | -0.4108 | ❌ |
| 45 | How many customaries does Norman customary law hav... | two | 2 | 0.0000 | ❌ |
| 46 | What Norman law wasdeveloped between 1000 and 1300... | NO ANSWER | NO ANSWER | 0.1701 | ✅ |
| 47 | What law has 3 customeries? | NO ANSWER | NO ANSWER | 0.3295 | ✅ |
| 48 | What was authored in the 12th century? | NO ANSWER | Two customaries in Latin | -0.3229 | ❌ |
| 49 | What is the Norman architecture idiom? | Romanesque | Romanesque | 0.0000 | ✅ |
| 50 | What kind of arches does Norman architecture have? | rounded | rounded arches | 0.0000 | ❌ |
| 51 | What type of arch did the Normans invent? | NO ANSWER | NO ANSWER | 0.2659 | ✅ |
| 52 | What architecture type came after Norman in Englan... | Early Gothic | Early Gothic | 0.0000 | ✅ |
| 53 | What architecture type came before Norman in Engla... | Anglo-Saxon | Ang Anglo-Saxon | 0.0000 | ❌ |
| 54 | What place had the Norman Arab architectural style... | Sicily | The Kingdom of Sicily | 0.0000 | ❌ |
| 55 | What precedes the period of Anglo-Saxon architectu... | NO ANSWER | NO ANSWER | 0.1162 | ✅ |
| 56 | What architecture type came after Early Gothic? | NO ANSWER | NO ANSWER | 0.0496 | ✅ |
| 57 | Who incorperated Islamic, LOmbard, and Byzantine b... | NO ANSWER | NO ANSWER | 0.7090 | ✅ |
| 58 | When did the church reform begin? | early 11th century | in the early 11th century | -0.3740 | ❌ |
| 59 | Who used the church to unify themselves? | dukes | The dukes of Normandy | 0.0000 | ❌ |
| 60 | What kind of art did the Normans have a rich tradi... | NO ANSWER | NO ANSWER | 0.4358 | ✅ |
| 61 | Who began a program of church reform in the 1100s | NO ANSWER | The dukes of Normandy | 0.0000 | ❌ |
| 62 | Who was divided by the church? | NO ANSWER | NO ANSWER | 0.0294 | ✅ |
| 63 | Who experienced aa golden age in the 1100s and 120... | NO ANSWER | Normandy | 0.0000 | ❌ |
| 64 | When were the French wars of religion? | 16th century | 16th century | -0.9252 | ✅ |
| 65 | What wars did France fight in the 1600s? | NO ANSWER | NO, the 16th century | -0.3122 | ❌ |
| 66 | What revolution was fought in the 1899's? | NO ANSWER | NO ANSWER | 0.5570 | ✅ |
| 67 | What kind of needlework was used in the creation o... | embroidery | Emb embroidery | 0.0000 | ❌ |
| 68 | What is Norman art's most well known piece? | Bayeux Tapestry | Bayeux Tapestry | 0.0000 | ✅ |
| 69 | Who commissioned the Tapestry? | Odo | Odo, the Bishop of Bayeux and first Earl of | 0.0000 | ❌ |
| 70 | What is the oldest work of Norman art? | NO ANSWER | NO ANSWER | 0.4652 | ✅ |
| 71 | Who commissioned Danish vikings to create the Baye... | NO ANSWER | Odo, the Bishop of Bayeux and first Earl of | 0.0000 | ❌ |
| 72 | In what century did important classical music deve... | 11th | The 11th century | -0.5570 | ❌ |
| 73 | Who were the two abbots at Fécamp Abbey? | William of Volpiano and John of Ravenna | William of Volpiano and John of Ravenna | 0.0000 | ✅ |
| 74 | What developed in Normandy during the 1100s? | NO ANSWER | neumes | -0.0073 | ❌ |
| 75 | What was Fecamp Abby the center of? | NO ANSWER | cent centres of musical production and education | -0.0334 | ❌ |
| 76 | Where did the monks flee to? | southern Italy | Southern Italy | 0.0000 | ✅ |
| 77 | What monastery did the Saint-Evroul monks establis... | Latin monastery at Sant'Eufemia. | Sant'Eufemia | 0.0000 | ❌ |
| 78 | Who patronized the monks in Italy?  | Robert Guiscard | Robert Guiscard | 0.0000 | ✅ |
| 79 | What tradition were the Saint-Evroul monks known f... | singing | singing | -0.0246 | ✅ |
| 80 | Who fled from southern Italy? | NO ANSWER | Mon monks of Saint-Evroul | 0.0000 | ❌ |
| 81 | What branch of theoretical computer science deals ... | Computational complexity theory | computational complexity theory | -0.8775 | ✅ |
| 82 | By what main attribute are computational problems ... | inherent difficulty | Algorithm | -0.1435 | ❌ |
| 83 | What is the term for a task that generally lends i... | computational problems | task | -0.1344 | ❌ |
| 84 | What is computational complexity principle? | NO ANSWER | NO ANSWER | 0.0826 | ✅ |
| 85 | What branch of theoretical computer class deals wi... | NO ANSWER | Computational complexity theory | -0.8574 | ❌ |
| 86 | What is understood to be a task that is in princip... | NO ANSWER | NO ANSWER | 0.5055 | ✅ |
| 87 |  What cannot be solved by mechanical application o... | NO ANSWER | NO ANSWER | 0.6577 | ✅ |
| 88 | What is a manual application of mathematical steps... | NO ANSWER | Manual application of mathematical steps is an algorithm | 0.0000 | ❌ |
| 89 | What measure of a computational problem broadly de... | if its solution requires significant resources | NO ANSWER | 0.0508 | ❌ |
| 90 | What method is used to intuitively assess or quant... | mathematical models of computation | Comput computational complexity | -0.0237 | ❌ |
| 91 | What are two basic primary resources used to guage... | time and storage | NO ANSWER | 0.0191 | ❌ |
| 92 | What unit is measured to determine circuit complex... | number of gates in a circuit | The number of gates in a circuit | 0.0000 | ❌ |
| 93 | What practical role does defining the complexity o... | determine the practical limits on what computers can and cannot do | NO ANSWER | 0.0622 | ❌ |
| 94 | What measure of computational problem broadly defi... | NO ANSWER | NO ANSWER | 0.3871 | ✅ |
| 95 | What method is not used to intuitively assess or q... | NO ANSWER | NO ANSWER | 0.1315 | ✅ |
| 96 | What are three basic primary resources used to gau... | NO ANSWER | NO ANSWER | 0.0181 | ✅ |
| 97 | What unit is measured to determine circuit simplic... | NO ANSWER | The number of gates in a circuit | -0.0359 | ❌ |
| 98 | What number is used in perpendicular computing? | NO ANSWER | NO ANSWER | 0.2856 | ✅ |
| 99 | What two fields of theoretical computer science cl... | analysis of algorithms and computability theory | Analysis of algorithms and computability theory | -0.0201 | ✅ |
| 100 | What field of computer science analyzes the resour... | analysis of algorithms | Analysis of algorithms | 0.0000 | ✅ |
| 101 | What field of computer science analyzes all possib... | computational complexity theory | NO ANSWER | 0.0231 | ❌ |
| 102 | What field of computer science is primarily concer... | computability theory | NO ANSWER | 0.0265 | ❌ |
| 103 | What are two fields of theoretical computer scienc... | NO ANSWER | NO ANSWER | 0.1503 | ✅ |
| 104 | What is not the key distinction between analysis o... | NO ANSWER | NO ANSWER | 0.1577 | ✅ |
| 105 | What is the process of analyzing the amount of res... | NO ANSWER | NO ANSWER | 0.2307 | ✅ |
| 106 | What is the process that asks a more specific ques... | NO ANSWER | Classically | -0.0117 | ❌ |
| 107 | What process classifies problems that can and cann... | NO ANSWER | NO ANSWER | 0.0708 | ✅ |
| 108 | What is the name given to the input string of a co... | problem instance | An instance | -0.0940 | ❌ |
| 109 | In computational complexity theory, what is the te... | the problem | The problem | -0.2875 | ✅ |
| 110 | Is a problem instance typically characterized as a... | concrete | con concrete | -0.0419 | ❌ |
| 111 | What is another name for any given measure of inpu... | instances | Problem instance | -0.0187 | ❌ |
| 112 | What is the general term used to describe the outp... | solution | Output | 0.0000 | ❌ |
| 113 | What can be viewed as a limited collection of inst... | NO ANSWER | computational problem | -0.5453 | ❌ |
| 114 | What is the name given to the input string of a co... | NO ANSWER | An instance | -0.0536 | ❌ |
| 115 | What term refers to the concrete question to be so... | NO ANSWER | problem | -0.3447 | ❌ |
| 116 | What is the output corresponding to the given ques... | NO ANSWER | NO ANSWER | 0.1833 | ✅ |
| 117 | What is a particular measure input associated with... | NO ANSWER | NO ANSWER | 0.1016 | ✅ |
| 118 | By how many kilometers does the traveling salesman... | 2000 | 2000 | -0.8185 | ✅ |
| 119 | What is one example of an instance that the quanti... | round trip through all sites in Milan | Is there a route of at most 2000 kilometres passing through | -0.0016 | ❌ |
| 120 | What does computational complexity theory most spe... | computational problems | comput computational problems | 0.0091 | ❌ |
| 121 | How many miles does the traveling salesman problem... | NO ANSWER | NO ANSWER | 0.4925 | ✅ |
| 122 | What is the qualitative answer to this particular ... | NO ANSWER | NO ANSWER | 0.1641 | ✅ |
| 123 | What is one example of an instance that the qualit... | NO ANSWER | round trip through all sites in Milan whose total length is at | 0.0078 | ❌ |
| 124 | What does computational simplicity theory most spe... | NO ANSWER | NO ANSWER | 0.0230 | ✅ |
| 125 | In a computational problem, what can be described ... | problem instance | string over an alphabet | -0.0213 | ❌ |
| 126 | What is the name of the alphabet is most commonly ... | binary alphabet | NO ANSWER | 0.0354 | ❌ |
| 127 | What is another term for the string of a problem i... | bitstrings | bitstrings | 0.0000 | ✅ |
| 128 | In the encoding of mathematical objects, what is t... | binary notation | binary | 0.0000 | ❌ |
| 129 | What is one way in which graphs can be encoded?  | adjacency matrices | They can be encoded directly via their adjacency matrices | -0.0191 | ❌ |
| 130 | What is a string over a Greek number when consider... | NO ANSWER | NO ANSWER | 0.1428 | ✅ |
| 131 | What is the name of the alphabet that is rarely us... | NO ANSWER | NO ANSWER | 0.2532 | ✅ |
| 132 | What is another term for the the string of a probl... | NO ANSWER | NO ANSWER | 0.0310 | ✅ |
| 133 | What is represented by non-binary notation in the ... | NO ANSWER | NO ANSWER | 0.0348 | ✅ |
| 134 | How can graphs be encoded indirectly? | NO ANSWER | by encoding their adjacency lists in binary | -0.0113 | ❌ |
| 135 | What kind of problems are one of the main topics s... | Decision problems | decision problems | -0.6945 | ✅ |
| 136 | What are the two simple word responses to a decisi... | yes or no | YES, the answer is either yes or no | -0.0025 | ❌ |
| 137 | What are the two integer responses to a decision p... | 1 or 0 | NO ANSWER | -0.3573 | ❌ |
| 138 | What will the output be for a member of the langua... | yes | YES | 0.0000 | ✅ |
| 139 | What answer denotes that an algorithm has accepted... | yes | "Yes | 0.0000 | ❌ |
| 140 | What kind of solutions are one of the central obje... | NO ANSWER | Decision problems | -0.5969 | ❌ |
| 141 | What is a typical type of computational problem wh... | NO ANSWER | Decision problem | -0.3925 | ❌ |
| 142 | What can be viewed as an informal language where t... | NO ANSWER | NO ANSWER | 0.0287 | ✅ |
| 143 | What are the three integer responses to a decision... | NO ANSWER | YES, 0, 1 | -0.1285 | ❌ |
| 144 | What answer denotes that a solution has accepted a... | NO ANSWER | yes | 0.0000 | ❌ |
| 145 | What kind of graph is an example of an input used ... | arbitrary graph | An arbitrary graph | -0.5024 | ❌ |
| 146 | What is the term for the set of all connected grap... | formal language | NO ANSWER | 0.0715 | ❌ |
| 147 | What encoding decision needs to be made in order t... | how graphs are encoded as binary strings | NO ANSWER | 0.2331 | ❌ |
| 148 | What type of graph is an example of an output used... | NO ANSWER | NO ANSWER | 0.1402 | ✅ |
| 149 | What is the term for the set of all unconnected gr... | NO ANSWER | NO ANSWER | 0.2531 | ✅ |
| 150 | What encoding decision needs to be made in order t... | NO ANSWER | NO ANSWER | 0.1641 | ✅ |
| 151 | How does one obtain an indefinite definition of th... | NO ANSWER | NO ANSWER | 0.6579 | ✅ |
| 152 | A function problem is an example of what? | a computational problem | decision problem | -0.3884 | ❌ |
| 153 | How many outputs are expected for each input in a ... | a single output | NO ANSWER | 0.0115 | ❌ |
| 154 | The traveling salesman problem is an example of wh... | A function problem | problem | -0.4062 | ❌ |
| 155 | In addition to the traveling salesman problem, wha... | the integer factorization problem | NO ANSWER | 0.0475 | ❌ |
| 156 | Is the output of a functional problem typically ch... | complex | NO ANSWER | 0.0613 | ❌ |
| 157 | What is a computational solution where a single in... | NO ANSWER | NO ANSWER | 0.1052 | ✅ |
| 158 | What is expected where a computational problems of... | NO ANSWER | NO ANSWER | 0.1420 | ✅ |
| 159 | What is a function solution an example of? | NO ANSWER | computational problem | -0.4210 | ❌ |
| 160 | What are other irrelevant examples of a function p... | NO ANSWER | NO ANSWER | 0.0263 | ✅ |
| 161 | Is the output of a functional solution typically c... | NO ANSWER | NO ANSWER | 0.0592 | ✅ |
| 162 | How can function problems typically be restated? | decision problems | Can be recast as decision problems | -0.0278 | ❌ |
| 163 | If two integers are multiplied and output a value,... | set of triples | THE set of triples (a, b, c) such that | -0.0174 | ❌ |
| 164 | What can not be restated as decision problems? | NO ANSWER | NO ANSWER | 0.1967 | ✅ |
| 165 | What is the expression set called where three inte... | NO ANSWER | NO ANSWER | 0.0152 | ✅ |
| 166 | What corresponds to solving the problem of multipl... | NO ANSWER | The set of triples (a, b, c) such that | -0.0573 | ❌ |
| 167 | What is a commonly used measurement used to determ... | how much time the best algorithm requires to solve the problem | NO ANSWER | 0.0768 | ❌ |
| 168 | What is one variable on which the running time may... | the instance | Input size | 0.0000 | ❌ |
| 169 | How is the time needed to obtain the solution to a... | as a function of the size of the instance | NO ANSWER | 0.0299 | ❌ |
| 170 | In what unit is the size of the input measured? | bits | bits | 0.0000 | ✅ |
| 171 | Complexity theory seeks to define the relationship... | an increase in the input size | the size of the input in bits | 0.0000 | ❌ |
| 172 | How does one measure the simplicity of a computati... | NO ANSWER | NO ANSWER | 0.4277 | ✅ |
| 173 | What is one variable which the running of time be ... | NO ANSWER | NO ANSWER | 0.0674 | ✅ |
| 174 | How is the time needed to obtain the question to a... | NO ANSWER | NO ANSWER | 0.1569 | ✅ |
| 175 | What is  interested in how algorithms scale with a... | NO ANSWER | NO ANSWER | 0.2431 | ✅ |
| 176 | How is time not required to solve a problem calcul... | NO ANSWER | NO ANSWER | 0.0679 | ✅ |
| 177 | Whose thesis states that the solution to a problem... | Cobham's thesis | Cobham | 0.0000 | ❌ |
| 178 | If input size is is equal to n, what can respectiv... | the time taken | NO ANSWER | 0.1163 | ❌ |
| 179 | What term corresponds to the maximum measurement o... | worst-case time complexity | NO ANSWER | 0.0815 | ❌ |
| 180 | How is worst-case time complexity written as an ex... | T(n) | NO ANSWER | 0.0754 | ❌ |
| 181 | Assuming that T represents a polynomial in T(n), w... | polynomial time algorithm | NO ANSWER | 0.2020 | ❌ |
| 182 | How is time taken expressed as a function of x? | NO ANSWER | NO ANSWER | 0.4403 | ✅ |
| 183 | Whose hypothesis states the the solution to a prob... | NO ANSWER | NO ANSWER | 0.0571 | ✅ |
| 184 | What term corresponds to the minimum measurement o... | NO ANSWER | NO ANSWER | 0.2238 | ✅ |
| 185 | How is best-case time complexity written as an exp... | NO ANSWER | NO ANSWER | 0.2774 | ✅ |
| 186 | What is the term given to the corresponding algori... | NO ANSWER | NO ANSWER | 0.2543 | ✅ |
| 187 | What is the term for a mathematical model that the... | A Turing machine | Turing machine | -1.0000 | ❌ |
| 188 | It is generally assumed that a Turing machine can ... | an algorithm | anything | -0.1649 | ❌ |
| 189 | What is the most commonplace model utilized in com... | the Turing machine | The Turing machine | -0.5707 | ✅ |
| 190 | What does a Turing machine handle on a strip of ta... | symbols | symbols | 0.0000 | ✅ |
| 191 | What a scientific model of a general computing mac... | NO ANSWER | Turing machine | -1.0000 | ❌ |
| 192 | What is a scientific device that manipulates symbo... | NO ANSWER | Turing machine | -1.0000 | ❌ |
| 193 | What are intended as a practical computing technol... | NO ANSWER | NO ANSWER | 0.1275 | ✅ |
| 194 | What is a scientific experiment that can solve a p... | NO ANSWER | Church–Turing thesis | -0.5722 | ❌ |
| 195 | What is generally considered to be the most basic ... | A deterministic Turing machine | deterministic Turing machine | -0.4988 | ❌ |
| 196 | What fixed set of factors determine the actions of... | rules | fixed set of rules | -0.4872 | ❌ |
| 197 | What is the term used to identify a deterministic ... | A probabilistic Turing machine | Prob probabilistic | -0.0798 | ❌ |
| 198 | What type of Turing machine is capable of multiple... | A non-deterministic Turing machine | Non-deterministic Turing machine | -0.1577 | ❌ |
| 199 | What is the term given to algorithms that utilize ... | randomized algorithms | randomizable algorithms | 0.0000 | ❌ |
| 200 | What uses a flexible set of rules to determine its... | NO ANSWER | deterministic Turing machine | -0.4708 | ❌ |
| 201 | What is a deterministic Turing machine with an ext... | NO ANSWER | NO ANSWER | 0.8961 | ✅ |
| 202 | What does not often help algorithms solve problems... | NO ANSWER | NO ANSWER | 0.0444 | ✅ |
| 203 | Which machine allows the machine to have multiple ... | NO ANSWER | NO ANSWER | 0.2170 | ✅ |
| 204 | How is one way that one should not view non-determ... | NO ANSWER | is not a physically realizable model | -0.0069 | ❌ |
| 205 | Turing machines are commonly employed to define wh... | complexity classes | complex classes | 0.0000 | ❌ |
| 206 | What are two factors that directly effect how powe... | time or space | time and space | 0.0000 | ❌ |
| 207 | In the determination of complexity classes, what a... | probabilistic Turing machines, non-deterministic Turing machines | 1. deterministic Turing machines, probabilistic Turing machines | 0.0092 | ❌ |
| 208 | What are many types of Turing machines not used fo... | NO ANSWER | NO ANSWER | 0.4395 | ✅ |
| 209 | What are three factors that directly effect how po... | NO ANSWER | NO ANSWER | 0.0649 | ✅ |
| 210 | What machines are not equally powerful in principl... | NO ANSWER | NO ANSWER | 0.4284 | ✅ |
| 211 | What may not be more powerful than others when the... | NO ANSWER | NO ANSWER | 0.0719 | ✅ |
| 212 | What is an example of a machine model that deviate... | random access machines | random access machines | 0.0000 | ✅ |
| 213 | In considering Turing machines and alternate varia... | computational power | NO ANSWER | 0.1707 | ❌ |
| 214 | What two resources commonly consumed by alternate ... | time and memory | time and memory | 0.0000 | ✅ |
| 215 | What commonality do alternate machine models, such... | the machines operate deterministically | NO ANSWER | 0.0137 | ❌ |
| 216 | What is not an example of a machine model that dev... | NO ANSWER | NO ANSWER | 0.3582 | ✅ |
| 217 | What measurement is affected by conversion between... | NO ANSWER | NO ANSWER | 0.0168 | ✅ |
| 218 | What two resources are uncommonly consumed by alte... | NO ANSWER | time and memory | 0.0000 | ❌ |
| 219 | What do all these models not have in common? | NO ANSWER | NO ANSWER | 0.4994 | ✅ |
| 220 | What type of Turing machine can be characterized b... | non-deterministic | Non-deterministic Turing machine | 0.0000 | ❌ |
| 221 | What often affects or facilitates ease of analysis... | unusual resources | resource | -0.0332 | ❌ |
| 222 | A non-deterministic Turing machine has the ability... | mathematical models | non-deterministic time | 0.0000 | ❌ |
| 223 | What is the most critical resource in the analysis... | time | Non-deterministic time | 0.0000 | ❌ |
| 224 | What is harder to analyze in terms of more unusual... | NO ANSWER | non-deterministic time | 0.0067 | ❌ |
| 225 | What type of machine is a computational model that... | NO ANSWER | Deterministic | 0.0000 | ❌ |
| 226 | What has a lot to do with how we physically want t... | NO ANSWER | NO ANSWER | 0.0187 | ✅ |
| 227 | What machine's branching does not exactly capture ... | NO ANSWER | Deterministic Turing machine | 0.0000 | ❌ |
| 228 | What is the least critical resource in the analysi... | NO ANSWER | NO ANSWER | 0.0777 | ✅ |
| 229 | The time required to output an answer on a determi... | state transitions | NO ANSWER | 0.0155 | ❌ |
| 230 | Complexity theory classifies problems based on wha... | difficulty | Their difficulty | -0.0095 | ❌ |
| 231 | What is the expression used to identify any given ... | DTIME(f(n)) | NO ANSWER | 0.0385 | ❌ |
| 232 | What is the most critical resource measured to in ... | time | NO ANSWER | 0.0445 | ❌ |
| 233 | What is not used for a precise definition of what ... | NO ANSWER | NO ANSWER | 0.3501 | ✅ |
| 234 | How is Turing machine M said not to operate? | NO ANSWER | NO ANSWER | 0.0758 | ✅ |
| 235 | What is the expression used to identify any given ... | NO ANSWER | NO ANSWER | 0.0506 | ✅ |
| 236 | What is the least critical resource measured in as... | NO ANSWER | NO ANSWER | 0.0498 | ✅ |
| 237 | How can decision problem B be solved in time x(f)? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 238 | Time and space are both examples of what type of r... | complexity resources | Comput complexity | -0.0829 | ❌ |
| 239 | A complexity resource can also be described as wha... | computational resource | computum | -0.0662 | ❌ |
| 240 | What is typically used to broadly define complexit... | Blum complexity axioms | Blum complexity axioms | 0.0000 | ✅ |
| 241 | Communication complexity is an example of what typ... | Complexity measures | Complex computational resource | -0.0579 | ❌ |
| 242 | Decision tree is an example of what type of measur... | Complexity measures | Communication complexity | -0.0110 | ❌ |
| 243 | What can not be made for space requirements? | NO ANSWER | NO ANSWER | 0.1982 | ✅ |
| 244 | What are the least well known complexity resources... | NO ANSWER | NO ANSWER | 0.1874 | ✅ |
| 245 | How are complexity measures generally not defined? | NO ANSWER | NO ANSWER | 0.3095 | ✅ |
| 246 | What are other complexity measures not used in com... | NO ANSWER | NO ANSWER | 0.5762 | ✅ |
| 247 | What type of measure is communication complexity n... | NO ANSWER | NO ANSWER | 0.0742 | ✅ |
| 248 | What are the three primary expressions used to rep... | best, worst and average | NO ANSWER | 0.0471 | ❌ |
| 249 | Case complexity likelihoods provide variable proba... | complexity measure | NO ANSWER | 0.0336 | ❌ |
| 250 | What is one common example of a critical complexit... | time | NO ANSWER | 0.1122 | ❌ |
| 251 | Case complexities provide three likelihoods of wha... | inputs | Case complexities measure the time complexity of inputs of the same size | 0.0049 | ❌ |
| 252 | What are the three secondary expressions used to r... | NO ANSWER | NO ANSWER | 0.0362 | ✅ |
| 253 | What three different ways are used to measure spac... | NO ANSWER | NO ANSWER | 0.7328 | ✅ |
| 254 | What is one not common example of a critical compl... | NO ANSWER | NO ANSWER | 0.0732 | ✅ |
| 255 | What differing variable remains the same size when... | NO ANSWER | NO ANSWER | 0.0477 | ✅ |
| 256 | What provides a solution to a list of integers pro... | deterministic sorting algorithm quicksort | NO ANSWER | 0.0117 | ❌ |
| 257 | When extensive time is required to sort integers, ... | worst-case | NO ANSWER | 0.0453 | ❌ |
| 258 | What is the expression used to denote a worst case... | O(n2) | O(n2) | 0.0000 | ✅ |
| 259 | What does not solve the problem of sorting a list ... | NO ANSWER | NO ANSWER | 0.3010 | ✅ |
| 260 | What does the deterministic parting algorithm quic... | NO ANSWER | NO ANSWER | 0.1224 | ✅ |
| 261 | What case complexity is represented when limited t... | NO ANSWER | NO ANSWER | 0.1547 | ✅ |
| 262 | What is the expression not used to denote worst ca... | NO ANSWER | NO ANSWER | 0.0552 | ✅ |
| 263 | What case complexity is represented when each pivo... | NO ANSWER | NO ANSWER | 0.3368 | ✅ |
| 264 | Classification of resources is contingent on deter... | the most efficient algorithm | resources | 0.0000 | ❌ |
| 265 | The analysis of a specific algorithm is typically ... | analysis of algorithms | Analysis of algorithms | 0.0000 | ✅ |
| 266 | Which bound of time is more difficult to establish... | lower bounds | NO ANSWER | 0.1131 | ❌ |
| 267 | A specific algorithm demonstrating T(n) represents... | upper bound | NO ANSWER | 0.0746 | ❌ |
| 268 | What is the colloquial phrase used to convey the c... | all possible algorithms | NO ANSWER | 0.0609 | ❌ |
| 269 | How does one note classify the computation time (o... | NO ANSWER | upper | -0.0423 | ❌ |
| 270 | What is usually taken as the best case complexity,... | NO ANSWER | The worst-case complexity | 0.0000 | ❌ |
| 271 | What does not fall under the field of analysis of ... | NO ANSWER | NO ANSWER | 0.1863 | ✅ |
| 272 | When does one not need to show only that there is ... | NO ANSWER | NO ANSWER | 0.3123 | ✅ |
| 273 | What is easy about proving lower bounds? | NO ANSWER | NO ANSWER | 0.7129 | ✅ |
| 274 | What expression is generally used to convey upper ... | big O notation | big O | -0.0831 | ❌ |
| 275 | What does a big O notation hide? | constant factors and smaller terms | Constant factors and smaller terms | 0.0000 | ✅ |
| 276 | How would one write T(n) = 7n2 + 15n + 40 in big O... | T(n) = O(n2) | T(n) = O(n2) | 0.0000 | ✅ |
| 277 | Big O notation provides autonomy to upper and lowe... | the computational model | comput computational model | -0.0435 | ❌ |
| 278 | What is usually not stated using the big O notatio... | NO ANSWER | NO ANSWER | 0.0884 | ✅ |
| 279 | What does not hide constant factors or smaller ter... | NO ANSWER | Answer | 0.0057 | ❌ |
| 280 | What makes the bounds dependent of the specific de... | NO ANSWER | constant factors | 0.0000 | ❌ |
| 281 | How would one abbreviate T(n)=8n2 + 16n = 40 in bi... | NO ANSWER | NO ANSWER | 0.2052 | ✅ |
| 282 | What has complicated definitions that prevent clas... | complexity classes | NO ANSWER | 0.7944 | ❌ |
| 283 | Complexity classes are generally classified into w... | framework | NO ANSWER | 0.0604 | ❌ |
| 284 | Difficulty in establishing a framework for complex... | complicated definitions | a | -0.0083 | ❌ |
| 285 | What fits the framework of complexity classes? | NO ANSWER | NO ANSWER | 0.5306 | ✅ |
| 286 | What has uncomplicated definitions that prevent cl... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 287 | What are complexity classes generally not classifi... | NO ANSWER | NO ANSWER | 0.8150 | ✅ |
| 288 | What variable is easy to establish in a framework ... | NO ANSWER | NO ANSWER | 0.4462 | ✅ |
| 289 | Concrete bounding of computation time frequently p... | chosen machine model | machine model | -0.2672 | ❌ |
| 290 | A multi-tape Turing machine requires what type of ... | linear time | NO ANSWER | 0.0232 | ❌ |
| 291 | A language solved in quadratic time implies the us... | single-tape Turing machines | single-tape Turing machine | 0.0000 | ❌ |
| 292 | What thesis specifies that a polynomial relationsh... | Cobham-Edmonds thesis | Cobham-Edmonds thesis | 0.0000 | ✅ |
| 293 | Decision problems capable of being solved by a det... | complexity class P | P | 0.0000 | ❌ |
| 294 | What does not often yield complexity classes that ... | NO ANSWER | NO ANSWER | 0.0260 | ✅ |
| 295 | What does not frequently produce complexity classe... | NO ANSWER | NO ANSWER | 0.4081 | ✅ |
| 296 | What can not be solved in linear time on multi-tap... | NO ANSWER | {xx \| x is any binary string} | -0.0826 | ❌ |
| 297 | What is not a binary string? | NO ANSWER | NO ANSWER | 0.3451 | ✅ |
| 298 | What thesis specifies that a trinomial relationshi... | NO ANSWER | Cobham-Edmonds thesis | 0.0000 | ❌ |
| 299 | What are two examples of measurements are bound wi... | time or space | NO ANSWER | 0.0259 | ❌ |
| 300 | What function is used by algorithms to define meas... | bounding | NO ANSWER | 0.0944 | ❌ |
| 301 | Bounding of time and space or similar measurements... | complexity classes | complex problems | -0.0066 | ❌ |
| 302 | What cannot be defined by bounding the time or spa... | NO ANSWER | NO ANSWER | 0.7327 | ✅ |
| 303 | What are three examples of measurement that are bo... | NO ANSWER | NO ANSWER | 0.0246 | ✅ |
| 304 | What function is used by algorithms to define meas... | NO ANSWER | NO ANSWER | 0.3477 | ✅ |
| 305 | What is often used by algorithms to measure boundi... | NO ANSWER | NO ANSWER | 0.1410 | ✅ |
| 306 | What are three examples of complexity classes asso... | BPP, ZPP and RP | BPP, ZPP, RP | 0.0000 | ❌ |
| 307 | AC and NC are complexity classes typically associa... | Boolean | Boolean | 0.0000 | ✅ |
| 308 | BQP and QMA are examples of complexity classes mos... | quantum | quantistic | 0.0000 | ❌ |
| 309 | What is the expression used to represent a complex... | #P | #P | 0.0000 | ✅ |
| 310 | IP and AM are most commonly defined by what type o... | Interactive | Interactive proof systems | 0.0000 | ❌ |
| 311 | What are the other four important complexity class... | NO ANSWER | 1. BPP ( probabilistic Turing machines, decision problems, | -0.2346 | ❌ |
| 312 | What machine does not define BPP, ZPP, and RP? | NO ANSWER | Boolean circuits | -0.0108 | ❌ |
| 313 | What machine does not define BQP or QMA? | NO ANSWER | Non probabilistic Turing machines | -0.0001 | ❌ |
| 314 | What is least important complexity class of counti... | NO ANSWER | NO ANSWER | 0.2822 | ✅ |
| 315 | What system not often define classes like IP and A... | NO ANSWER | Interactive proof systems | -0.0358 | ❌ |
| 316 | What is an example of a measurement within a compl... | computation time | NO ANSWER | 0.2228 | ❌ |
| 317 | In what expression can one expect to find DTIME(n) | DTIME(n2) | NO ANSWER | 0.4747 | ❌ |
| 318 | What theorems are responsible for determining ques... | time and space hierarchy theorems | time and space hierarchy theorems | -0.0364 | ✅ |
| 319 | Resources are constrained by hierarchy theorems to... | a proper hierarchy on the classes defined | classes | 0.0000 | ❌ |
| 320 | What kind of statement is made in the effort of es... | quantitative statements | NO ANSWER | 0.0258 | ❌ |
| 321 | What is not an example of a measurement within a c... | NO ANSWER | NO ANSWER | 0.5175 | ✅ |
| 322 | What does not define a bigger set of problems? | NO ANSWER | NO ANSWER | 0.7851 | ✅ |
| 323 | What expression does not usually contain DTIME(n)? | NO ANSWER | NO ANSWER | 0.5283 | ✅ |
| 324 | What does not induce a proper hierarchy on the cla... | NO ANSWER | NO ANSWER | 0.6810 | ✅ |
| 325 | What kind of statement is not made in an effort of... | NO ANSWER | NO ANSWER | 0.5366 | ✅ |
| 326 | What is the foundation for separation results with... | time and space hierarchy theorems | The time hierarchy theorem and the space hierarchy theorem | -0.4389 | ❌ |
| 327 | What is responsible for constraining P according t... | EXPTIME | The time hierarchy theorem | -0.0288 | ❌ |
| 328 | Within what variable is L constrained according to... | PSPACE | PSPACE | -0.0628 | ✅ |
| 329 | What does not form the basis for most separation r... | NO ANSWER | NO ANSWER | 0.3207 | ✅ |
| 330 | What does the past time and space hierarchy theore... | NO ANSWER | Most separation results of complexity classes | -0.0105 | ❌ |
| 331 | What is not strictly contained in EXPTIME? | NO ANSWER | NO ANSWER | 0.2349 | ✅ |
| 332 | What is not strictly contained in PSPACE? | NO ANSWER | NO ANSWER | 0.2282 | ✅ |
| 333 | What concept is frequently used to define complexi... | reduction | reduction | 0.0000 | ✅ |
| 334 | Reduction essentially takes one problem and conver... | another problem | another problem | 0.0000 | ✅ |
| 335 | According to reduction, if X and Y can be solved b... | reduces | NO ANSWER | 0.1523 | ❌ |
| 336 | What are two examples of different types of reduct... | Karp reductions and Levin reductions | 1. Cook reductions, Karp reductions, and Levin reductions | 0.0000 | ❌ |
| 337 | Polynomial time reductions are an example of what? | the bound on the complexity of reductions | Pol polynomial-time reductions | -0.0514 | ❌ |
| 338 | What are many complexity classes not defined by? | NO ANSWER | NO ANSWER | 0.0731 | ✅ |
| 339 | What is defined by using the theorem of reduction? | NO ANSWER | NO ANSWER | 0.0648 | ✅ |
| 340 | What is a transformation of two problems into on t... | NO ANSWER | NO ANSWER | 0.0489 | ✅ |
| 341 | What captures the formal notion of a problem being... | NO ANSWER | transformation of one problem into another problem | 0.0000 | ❌ |
| 342 | What are the six types of reductions? | NO ANSWER | NO ANSWER | 0.3587 | ✅ |
| 343 | What is the most frequently employed type of reduc... | polynomial-time reduction | Pol polynomial-time reduction | -0.0417 | ❌ |
| 344 | What equates to a squared integer according to pol... | multiplying two integers | squaring | -0.0847 | ❌ |
| 345 | What measurement of time is used in polynomial tim... | polynomial time | NO ANSWER | 0.0176 | ❌ |
| 346 | What would need to remain constant in a multiplica... | input | NO | -0.0208 | ❌ |
| 347 | According to polynomial time reduction squaring ca... | multiplication | multip multiplication | -0.0316 | ❌ |
| 348 | What is the least used type of reduction? | NO ANSWER | NO ANSWER | 0.3213 | ✅ |
| 349 | What is the meaning of polynomial-space reduction? | NO ANSWER | polynomial-time reduction is not the same, polynomial-time reduction is | -0.0149 | ❌ |
| 350 | What can the problem of dividing an integer be red... | NO ANSWER | Div multiplication | -0.1188 | ❌ |
| 351 | What does one not need to remain constant in a mul... | NO ANSWER | A. The inputs | -0.0113 | ❌ |
| 352 | What is more difficult that multiplication? | NO ANSWER | NO ANSWER | 0.1202 | ✅ |
| 353 | The complexity of problems often depends on what? | the type of reduction being used | what | 0.0000 | ❌ |
| 354 | What would create a conflict between a problem X a... | if every problem in C can be reduced to X | NO ANSWER | 0.1464 | ❌ |
| 355 | An algorithm for X which reduces to C would us to ... | solve any problem in C | allow us to solve any problem in C | 0.0000 | ❌ |
| 356 | A problem set that that is hard for the expression... | NP-hard | NO ANSWER | 0.0817 | ❌ |
| 357 | What does the complexity of problems not often dep... | NO ANSWER | pol polynomial-time | 0.0091 | ❌ |
| 358 | What would not create a conflict between a problem... | NO ANSWER | NO ANSWER | 0.3882 | ✅ |
| 359 | What problem in C is harder than X? | NO ANSWER | NO ANSWER | 0.4778 | ✅ |
| 360 | How is a problem set that is hard for expression Q... | NO ANSWER | NO ANSWER | 0.3111 | ✅ |
| 361 | The hardest problems in NP can be analogously writ... | NP-complete | NO ANSWER | 0.0110 | ❌ |
| 362 | NP complete problems contain the lowest likelihood... | NP | P | 0.0091 | ❌ |
| 363 | If P = NP is unsolved, and reduction is applied to... | there is no known polynomial-time solution | If P = NP is not solved, and a known NP-complete | -0.1764 | ❌ |
| 364 | If polynomial time can be utilized within an NP-co... | NP | NO ANSWER | 0.2435 | ❌ |
| 365 | What happens if a problem X is in C, and soft for ... | NO ANSWER | NO ANSWER | 0.4364 | ✅ |
| 366 | What is the softest problem in C? | NO ANSWER | NO ANSWER | 0.8840 | ✅ |
| 367 | What is class contains the the least difficult pro... | NO ANSWER | NO ANSWER | 0.5931 | ✅ |
| 368 | What would indicate that there is a known polynomi... | NO ANSWER | NO ANSWER | 0.2211 | ✅ |
| 369 | What complexity class is characterized by a comput... | P | P | 0.0000 | ✅ |
| 370 | What hypothesis is associated with the complexity ... | Cobham–Edmonds thesis | Cobham–Edmonds thesis | -0.4327 | ✅ |
| 371 | What complexity class is commonly characterized by... | NP | NO ANSWER | 0.0669 | ❌ |
| 372 | What is an example of a problem that rests within ... | Boolean satisfiability problem | Bo Boolean satisfiability problem | -0.3840 | ❌ |
| 373 | In what theoretical machine is it confirmed that a... | Turing machines | NO ANSWER | 0.0521 | ❌ |
| 374 | What is often seen as a scientific abstraction mod... | NO ANSWER | Cobham–Edmonds thesis | -0.5340 | ❌ |
| 375 | What theory is the Cobham-Edward thesis? | NO ANSWER | The Cobham–Edmonds thesis | -0.4683 | ❌ |
| 376 | What complexity class is not commonly characterize... | NO ANSWER | NO ANSWER | 0.1554 | ✅ |
| 377 | What is an example of a problem that rests within ... | NO ANSWER | NOT NP | -0.2787 | ❌ |
| 378 | What ,theoretical machine did not confirm that a p... | NO ANSWER | NO ANSWER | 0.0835 | ✅ |
| 379 | If P is ultimately proven to be equal tot NP, what... | more efficient solutions | An efficient solution to many important problems in various research and science | -0.0268 | ❌ |
| 380 | What is a particular problem in biology that would... | protein structure prediction | Pro protein structure prediction in biology | 0.0000 | ❌ |
| 381 | What is the prize offered for finding a solution t... | $1,000,000 | $1,000,000 | -0.7020 | ✅ |
| 382 | What is one of the least important open questions ... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 383 | What effect would happen if P is ultimately proven... | NO ANSWER | NO ANSWER | 0.4807 | ✅ |
| 384 | What is a particular problem in chemistry that wou... | NO ANSWER | PRO protein structure prediction in biology | 0.0075 | ❌ |
| 385 | What problem was proposed by Clay Mathematics Inst... | NO ANSWER | NO ANSWER | 0.5763 | ✅ |
| 386 | What was the prize for finding a solution to P=NP ... | NO ANSWER | NO ANSWER | 0.8297 | ✅ |
| 387 | Who demonstrated that P= NP implies problems not p... | Ladner | Ladner | 0.0000 | ✅ |
| 388 | What is the name for a problem that meets Ladner's... | NP-intermediate problems | NP-intermediate problems | 0.0000 | ✅ |
| 389 | What is an example of an NP-intermediate problem n... | graph isomorphism problem | The graph isomorphism problem, the discrete logarithm problem and | 0.0000 | ❌ |
| 390 | Who showed that if P=NQ then there exists problems... | NO ANSWER | NO ANSWER | 0.7327 | ✅ |
| 391 | What is the name a a problem that meets Ladder's a... | NO ANSWER | NP-intermediate problems | 0.0000 | ❌ |
| 392 | What is not example of an NP-intermediate problem ... | NO ANSWER | NO ANSWER | 0.0841 | ✅ |
| 393 | What are four examples of problems believed to be ... | NO ANSWER | Graph isomorphism problem, discrete logarithm problem, integer factor | 0.0000 | ❌ |
| 394 | What is the problem attributed to defining if two ... | The graph isomorphism problem | Graph isomorphism problem | -0.5627 | ❌ |
| 395 | What class is most commonly not ascribed to the gr... | NP-complete | NO ANSWER | 0.3534 | ❌ |
| 396 | What finite hierarchy implies that the graph isomo... | polynomial time hierarchy | NO ANSWER | 0.0670 | ❌ |
| 397 | To what level would the polynomial time hierarchy ... | second level | NP | -0.4706 | ❌ |
| 398 | Who are commonly associated with the algorithm typ... | Laszlo Babai and Eugene Luks | Babai and Eugene Luks | -0.0182 | ❌ |
| 399 | What is the graph isolation problem?  | NO ANSWER | NO ANSWER | 0.4948 | ✅ |
| 400 | What is the problem attributed to defining if thre... | NO ANSWER | NO ANSWER | 0.0933 | ✅ |
| 401 | What is an important solved problem in complexity ... | NO ANSWER | NO ANSWER | 0.1588 | ✅ |
| 402 | What infinite hierarchy implies that the graph iso... | NO ANSWER | NO ANSWER | 0.5513 | ✅ |
| 403 | What would the polynomial hierarchy collapse if gr... | NO ANSWER | NO ANSWER | 0.3476 | ✅ |
| 404 | What computational problem is commonly associated ... | The integer factorization problem | Integer factorization | -0.2640 | ❌ |
| 405 | The integer factorization problem essentially seek... | k | k | -0.0268 | ✅ |
| 406 | That there currently exists no known integer facto... | modern cryptographic systems | The RSA algorithm | -0.5055 | ❌ |
| 407 | What is the most well-known algorithm associated w... | the general number field sieve | The general number field sieve | -0.8048 | ✅ |
| 408 | What is the integer practice problem? | NO ANSWER | NO ANSWER | 0.6561 | ✅ |
| 409 | What computational problem is not commonly associa... | NO ANSWER | Decision | -0.0044 | ❌ |
| 410 | What problem is phrased on deciding whether the in... | NO ANSWER | nan | -0.0950 | ❌ |
| 411 | What problem would have polynomial time hierarchy ... | NO ANSWER | no problem | -0.3601 | ❌ |
| 412 | What is the least well known algorithm associated ... | NO ANSWER | NO ANSWER | 0.2875 | ✅ |
| 413 | What is the unproven assumption generally ascribed... | suspected to be unequal | it is possible that all these complexity classes collapse to one class | -0.0469 | ❌ |
| 414 | What is an expression that can be used to illustra... | P ⊆ NP ⊆ PP ⊆ PSPACE | ⊆ NP ⊆ PP ⊆ PSPACE | 0.0021 | ❌ |
| 415 | Where can the complexity classes RP, BPP, PP, BQP,... | between P and PSPACE | NO ANSWER | 0.0250 | ❌ |
| 416 | What evidence between and among complexity classes... | Proving that any of these classes are unequal | NO ANSWER | 0.1960 | ❌ |
| 417 | What is the proven assumption generally ascribed t... | NO ANSWER | NO ANSWER | 0.1973 | ✅ |
| 418 | What is an expression that caan be used to illustr... | NO ANSWER | NO ANSWER | 0.0505 | ✅ |
| 419 | Where can complexity classes RPP, BPP, PPP, BQP, M... | NO ANSWER | NO ANSWER | 0.0195 | ✅ |
| 420 | What is impossible for the complexity classes RP, ... | NO ANSWER | NO ANSWER | 0.3680 | ✅ |
| 421 | What would not be a major breakthrough in complexi... | NO ANSWER | NO ANSWER | 0.4175 | ✅ |
| 422 | In what complexity class do complement problems of... | co-NP | co-NP | 0.0000 | ✅ |
| 423 | How do the yes/no answers of a complement problem ... | reversed | NO ANSWER | 0.1144 | ❌ |
| 424 | What is commonly believed to be the value relation... | not equal | ne not equal | -0.4673 | ❌ |
| 425 | What implication can be derived for P and NP if P ... | P is not equal to NP | NP is not equal to P | -0.4785 | ❌ |
| 426 | What complexity class do incompatible problems of ... | NO ANSWER | co-NP | 0.0000 | ❌ |
| 427 | How do the yes/no answers of an incompatible probl... | NO ANSWER | NO ANSWER | 0.6587 | ✅ |
| 428 | What is not commonly believed to be the value rela... | NO ANSWER | co-NP is not equal to NP | -0.1403 | ❌ |
| 429 | What implication can not be derived for P and NP i... | NO ANSWER | NO ANSWER | -0.0999 | ✅ |
| 430 | What variable is associated with all problems solv... | L | L | 0.0000 | ✅ |
| 431 | Though unkown, what are the most commonly ascribed... | strictly contained in P or equal to P | NO ANSWER | 0.0854 | ❌ |
| 432 | What lies between L and P that prevents a definiti... | complexity classes | NO ANSWER | 0.0673 | ❌ |
| 433 | What are two complexity classes between L and P? | NL and NC | NL and NC | 0.0000 | ✅ |
| 434 | What is unknown about the complexity classes betwe... | if they are distinct or equal classes | NO ANSWER | 0.1176 | ❌ |
| 435 | What variable is not associated with all problems ... | NO ANSWER | NO ANSWER | 0.1048 | ✅ |
| 436 | What are the least commonly ascribed attributes of... | NO ANSWER | NO ANSWER | 0.2982 | ✅ |
| 437 | What does not lie between L and P that allows a de... | NO ANSWER | NO ANSWER | 0.4243 | ✅ |
| 438 | What are three complexity classes between L and P? | NO ANSWER | NO ANSWER | 0.0259 | ✅ |
| 439 | What is known about the complexity between L and P... | NO ANSWER | NO ANSWER | 0.4144 | ✅ |
| 440 | Problems capable of theoretical solutions but cons... | intractable problems | intractable | 0.0000 | ❌ |
| 441 | Intractable problems lacking polynomial time solut... | exponential-time algorithms | Pr polynomial time algorithms | -0.0280 | ❌ |
| 442 | If NP is not equal to P, viewed through this lens,... | NP-complete problems | NP-complete problems | 0.0000 | ✅ |
| 443 | What are problems that cannot be solved in theory,... | NO ANSWER | NO ANSWER | 0.0173 | ✅ |
| 444 | When are problems that have polynomial-tome soluti... | NO ANSWER | NO ANSWER | 0.0529 | ✅ |
| 445 | What states that only problems that cannot be solv... | NO ANSWER | The Cobham–Edmonds thesis | 0.0000 | ❌ |
| 446 | When would a program not be useful for very small ... | NO ANSWER | For a program that makes 2n operations before halting | -0.1148 | ❌ |
| 447 | What algorithm is always practical? | NO ANSWER | NO ANSWER | 0.4326 | ✅ |
| 448 | What eponymous variation of arithmetic presents a ... | Presburger arithmetic | Presburger arithmetic | 0.0000 | ✅ |
| 449 | Despite the Presburger problem, and in view of int... | algorithms have been written | wide range of algorithms have been written to solve the problem in | -0.0372 | ❌ |
| 450 | What is an example of a problem to which effective... | NP-complete knapsack problem | Presburger arithmetic | 0.0000 | ❌ |
| 451 | How quickly can an algorithm solve an NP-complete ... | in less than quadratic time | Qu quadratic time | 0.0000 | ❌ |
| 452 | What is the example of another problem characteriz... | NP-complete Boolean satisfiability problem | The Boolean satisfiability problem | -0.0053 | ❌ |
| 453 | What unknown variation of arithmetic presents a de... | NO ANSWER | NO ANSWER | 0.0466 | ✅ |
| 454 | What has not been done to establish solutions in r... | NO ANSWER | NO ANSWER | 0.0491 | ✅ |
| 455 | What can not solve the NP-complete knapsack proble... | NO ANSWER | NO ANSWER | 0.4340 | ✅ |
| 456 | What do SAT solvers not usually handle when testin... | NO ANSWER | NO ANSWER | 0.2351 | ✅ |
| 457 | What tactic did researchers employ to offset the f... | foundations were laid out | Definition of Turing machines by Alan Turing in 1936 | 0.0057 | ❌ |
| 458 | Who was the most influential researcher among thos... | Alan Turing | NO ANSWER | 0.0751 | ❌ |
| 459 | What theoretical device is attributed to Alan Turi... | Turing machines | Turing machines | 0.0000 | ✅ |
| 460 | In what year was the Alan Turing's definitional mo... | 1936 | 1936 | -1.0000 | ✅ |
| 461 | In the most basic sense what did a Turing machine ... | a computer | NO ANSWER | 0.0708 | ❌ |
| 462 | What were laid out by various companies? | NO ANSWER | found the foundations | 0.0020 | ❌ |
| 463 | What tactic did companies employ to offset the for... | NO ANSWER | NO ANSWER | 0.2390 | ✅ |
| 464 | Who was the least influential researcher working o... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 465 | What device did Alan Turning invent in 1974? | NO ANSWER | NO ANSWER | 0.8685 | ✅ |
| 466 | What was the Turning calculator a robust and flexi... | NO ANSWER | computer | 0.0000 | ❌ |
| 467 | What paper is commonly considered the bellwether u... | On the Computational Complexity of Algorithms | "On the Computational Complexity of Algorithms" by Juris Hartman | -0.1668 | ❌ |
| 468 | What individuals were responsible for authoring "O... | Juris Hartmanis and Richard Stearns | Juris Hartmanis and Richard Stearns | 0.0000 | ✅ |
| 469 | In what year was Hatmanis and Stearn's seminal wor... | 1965 | 1965 | -1.0000 | ✅ |
| 470 | What complex measurements were defined by "On the ... | time and space | time and space complexity | 0.0000 | ❌ |
| 471 | In what year did Edmond's characterize a "good" al... | 1965 | 1965 | -0.8568 | ✅ |
| 472 | What seminal paper is commonly considered the begi... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 473 | Who wrote "On the Computational Complexity of Scie... | NO ANSWER | NO ANSWER | 0.7349 | ✅ |
| 474 | What seminal paper was written by Juris Hartmanis ... | NO ANSWER | NO ANSWER | 0.6085 | ✅ |
| 475 | What simple measurements were defined by "On the C... | NO ANSWER | time and space complexity | 0.0000 | ❌ |
| 476 | Who provided a definition of linear bounded automa... | John Myhill | John Myhill | 0.0000 | ✅ |
| 477 | In what year did Raymond Sullivan publish a study ... | 1961 | NO ANSWER | 0.5087 | ❌ |
| 478 | In 1962, who was responsible for the authorship of... | Hisao Yamada | Hisao Yamada | 0.0000 | ✅ |
| 479 | Who wrote later papers studying problems solvable ... | NO ANSWER | Hisao Yamada | -0.2091 | ❌ |
| 480 | Who provided a definition of linear bounded automa... | NO ANSWER | NO ANSWER | 0.5288 | ✅ |
| 481 | What year did Dick Sullivan publish a study on rud... | NO ANSWER | NO ANSWER | 0.6320 | ✅ |
| 482 | Who wrote a paper on real time computations in 197... | NO ANSWER | NO ANSWER | 0.6586 | ✅ |
| 483 | Who was pioneer and studied specific complexity me... | NO ANSWER | NO ANSWER | 0.3941 | ✅ |
| 484 | What is the concrete choice typically assumed by m... | input encoding | NO ANSWER | 0.0608 | ❌ |
| 485 | In the effort of maintaining a level of abstractio... | encoding | encoding | -0.0070 | ✅ |
| 486 | What can not be achieved by ensuring different rep... | NO ANSWER | NO ANSWER | 0.2993 | ✅ |
| 487 | What is the abstract choice typically assumed by m... | NO ANSWER | NO ANSWER | 0.0667 | ✅ |
| 488 | What does not regularly use input coding as its co... | NO ANSWER | Proof of theorems | -0.0296 | ❌ |
| 489 | What choice is typically left dependent in an effo... | NO ANSWER | choice of encoding | 0.0015 | ❌ |
| 490 | Who is responsible for axiomatic complexity theory... | Manuel Blum | Man Manuel Blum | 0.0000 | ❌ |
| 491 | What theorem was implicated by Manuel Blum's axiom... | speed-up theorem | The speed-up theorem | 0.0000 | ❌ |
| 492 | What is the paper written by Richard Karp in 1972 ... | "Reducibility Among Combinatorial Problems" | "Reducibility Among Combinatorial Problems | -0.0656 | ❌ |
| 493 | How many combinatory and graph theoretical problem... | 21 | 21 | -1.0000 | ✅ |
| 494 | Who developed an axiomatic complexity theory based... | NO ANSWER | NO ANSWER | 0.8211 | ✅ |
| 495 | Who is responsible for the so-called, speed-up the... | NO ANSWER | NO ANSWER | 0.7795 | ✅ |
| 496 | Who proved that these exist practical relevant pro... | NO ANSWER | NO ANSWER | 0.5969 | ✅ |
| 497 | Who wrote the paper "Reductibility Among Combinato... | NO ANSWER | NO ANSWER | 0.3643 | ✅ |
| 498 | What book featured 25 diverse comninatorial and gr... | NO ANSWER | NO ANSWER | 0.0425 | ✅ |
| 499 | What is Southern California often abbreviated as? | SoCal | SoCal | 0.0000 | ✅ |
| 500 | Despite being traditionall described as "eight cou... | 10 counties | 10 | -0.3358 | ❌ |
| 501 | What is a major importance of Southern California ... | economic center | major economic center | -0.0456 | ❌ |
| 502 | What are the ties that best described what the "ei... | demographics and economic ties | Dem demographics | 0.0000 | ❌ |
| 503 | The reasons for the las two counties to be added a... | historical political divisions | political divisions | -0.0114 | ❌ |
| 504 | What counties does the more extensive eight county... | NO ANSWER | Im Imperial, Los Angeles, Orange, Riverside, San Bernardino, | 0.0000 | ❌ |
| 505 | What additional two counties make ten counties int... | NO ANSWER | Kern and San Luis Obispo | 0.0000 | ❌ |
| 506 | Where is the center of economic activity for the U... | NO ANSWER | NO ANSWER | 0.7094 | ✅ |
| 507 | What is the name of the region that is not defined... | Southern California Megaregion | The Southern California Megaregion | -0.5262 | ❌ |
| 508 | How many megaregions are there in the United State... | 11 | 11 | -0.8810 | ✅ |
| 509 | What is the name of the state that the megaregion ... | Nevada | Nevada | 0.0000 | ✅ |
| 510 | Which border does the megaregion extend over? | Mexican | One | -0.0458 | ❌ |
| 511 | What is the name of the area past the border that ... | Tijuana | Tijuana | -0.0280 | ✅ |
| 512 | What is one of the 10 megaregions in the United St... | NO ANSWER | The Southern California Megaregion | -0.3579 | ❌ |
| 513 | Where does the 8 county megaregion extend from? | NO ANSWER | NO ANSWER | 0.0446 | ✅ |
| 514 | What is Las Vegas one of in the United States? | NO ANSWER | megaregion | 0.0000 | ❌ |
| 515 | Which coastline does Southern California touch? | Pacific | Pacific | 0.0000 | ✅ |
| 516 | How many metropolitan areas does Southern Californ... | seven | seven | 0.0000 | ✅ |
| 517 | How many inhabitants does the Los Angeles area con... | 12 million | Over 12 million | -0.4311 | ❌ |
| 518 | Which of the three heavily populated areas has the... | San Diego | The San Diego area with over 3 million inhabitants | -0.1676 | ❌ |
| 519 | How many people does the Greater Los Angeles Area ... | 17.5 million | 17.5 million | -0.8295 | ✅ |
| 520 | What percent of California's 22 million people liv... | NO ANSWER | 60 | -1.0000 | ❌ |
| 521 | What does MAS stand for? | NO ANSWER | MSAs | -0.0132 | ❌ |
| 522 | How many people live in Riverside?  | NO ANSWER | 4 million | -0.0255 | ❌ |
| 523 | What does CSA stand for? | NO ANSWER | California | 0.0014 | ❌ |
| 524 | What is the name of the water body that is found t... | Colorado River | Colorado River | 0.0000 | ✅ |
| 525 | What is the name of the desert on the border of Ar... | Colorado Desert | Colorado Desert | 0.0000 | ✅ |
| 526 | What is the name of the desert near the border of ... | Mojave Desert | Mojave Desert | 0.0000 | ✅ |
| 527 | What is the name of the border to the south? | Mexico–United States border | Mexico–United States border | 0.0000 | ✅ |
| 528 | What desert is to the south near Arizona? | NO ANSWER | NO ANSWER | 0.0333 | ✅ |
| 529 | What desert is to the south near Nevada? | NO ANSWER | NO ANSWER | 0.0268 | ✅ |
| 530 | What direction is the Colorado-Mexico border? | NO ANSWER | South | -0.1244 | ❌ |
| 531 | The cities of Los Angeles and San Diego are a part... | California | California | 0.0000 | ✅ |
| 532 | What is the population of Los Angeles? | 3,792,621 | 3,792,621 | -1.0000 | ✅ |
| 533 | Which city is the most populous in California? | Los Angeles | Los Angeles | 0.0000 | ✅ |
| 534 | What is the eighth most populous city in the natio... | San Diego | NO ANSWER | 0.0200 | ❌ |
| 535 | In which cardinal direction from Los Angeles is Sa... | south | South | 0.0000 | ✅ |
| 536 | What are two of the three major cities located in ... | NO ANSWER | Los Angeles and San Diego | -0.1067 | ❌ |
| 537 | What city has a population of 3,792,261? | NO ANSWER | NO ANSWER | 0.0790 | ✅ |
| 538 | What city has a population of 1,307,204? | NO ANSWER | NO ANSWER | 0.1037 | ✅ |
| 539 | What second most populous city is north of Los Ang... | NO ANSWER | NO ANSWER | 0.2473 | ✅ |
| 540 | Orange, San Diego, Riverside and San Bernardino ma... | Los Angeles | Los Angeles | 0.0000 | ✅ |
| 541 | What country are all the counties in? | United States | United States | 0.0000 | ✅ |
| 542 | What are Los Angeles, Orange, San Diego, San Berna... | counties | The five most populous counties in the state of the United States | 0.0000 | ❌ |
| 543 | What is the lowest ranking one of the counties cou... | 15 | 16 | -0.2182 | ❌ |
| 544 | What is the smallest geographical region discussed... | counties | California | -0.0134 | ❌ |
| 545 | What are the five most populous counties in the Un... | NO ANSWER | NO ANSWER | 0.4793 | ✅ |
| 546 | How many populous counties are in the United State... | NO ANSWER | Top 15 | -0.2846 | ❌ |
| 547 | What county are Los Angeles, Orange, San Diego, Sa... | NO ANSWER | NO ANSWER | 0.0524 | ✅ |
| 548 | What is the name given to the district that is ass... | Hollywood | Hollywood | 0.0000 | ✅ |
| 549 | Which city does the Hollywood district belong to? | Los Angeles | Los Angeles | 0.0000 | ✅ |
| 550 | Which company owns ABC? | The Walt Disney Company | The Walt Disney Company | -1.0000 | ✅ |
| 551 | Other than the motion picture and television indus... | music | NO ANSWER | 0.3242 | ❌ |
| 552 | Other than Universal and Warner Brothers, what oth... | Sony | The Walt Disney Company | -0.5594 | ❌ |
| 553 | What company owns ACB? | NO ANSWER | The Walt Disney Company | -0.9766 | ❌ |
| 554 | What three industries are centered in Hollywood? | NO ANSWER | film, television, music | -0.2528 | ❌ |
| 555 | Where is Los Angeles a district of? | NO ANSWER | Los Angeles | -0.0451 | ❌ |
| 556 | What major companies are headquartered in Los Ange... | NO ANSWER | The Walt Disney Company, Sony Pictures, Universal, MGM, Paramount | -0.4899 | ❌ |
| 557 | Other than surf, what other culture is southern Ca... | skateboard | Extreme sports | -0.0313 | ❌ |
| 558 | What is the name of the professional skateboarder ... | Tony Hawk | Tony Hawk | 0.0000 | ✅ |
| 559 | What famous snowbaorder lives in southern Californ... | Shaun White | Sha Shaun White | -0.0351 | ❌ |
| 560 | Southern California is second to which island in t... | Oahu | The island of Oahu | 0.0000 | ❌ |
| 561 | What is the shortened name of the annual yacht rac... | Transpac | Transpac | 0.0000 | ✅ |
| 562 | Where are No Fear and RCVA headquartered? | NO ANSWER | California | -0.2360 | ❌ |
| 563 | Who are Rob Curran and Tim Machado? | NO ANSWER | Professional surfers | 0.0000 | ❌ |
| 564 | Where does professional surfer Tony Hawk live? | NO ANSWER | Southern California | -0.7242 | ❌ |
| 565 | What famous surfing spots is Oahu second to? | NO ANSWER | Southern California | -0.1942 | ❌ |
| 566 | What was held at the San Diego Yacht Club from 198... | NO ANSWER | NO ANSWER | 0.2233 | ✅ |
| 567 | What is the name of the desert city? | Palm Springs | Palm Springs | 0.0000 | ✅ |
| 568 | Other than the desert city why do many locals and ... | beaches | pop for its popular beaches | -0.0278 | ❌ |
| 569 | Which region of California is Palm Springs located... | southern | Southern California | 0.0000 | ❌ |
| 570 | Other than for its resort feel, what is Palm Sprin... | open spaces | open spaces | 0.0079 | ✅ |
| 571 | Who visits Palm Springs for the beaches? | NO ANSWER | LOCAL | -0.0301 | ❌ |
| 572 | What is the desert of southern California popular ... | NO ANSWER | open spaces | 0.0000 | ❌ |
| 573 | Which coast is the desert on? | NO ANSWER | NO ANSWER | 0.0548 | ✅ |
| 574 | Geographically speaking, where is California's nor... | 37° 9' 58.23" | 37° 9' 58.23" | -1.0000 | ✅ |
| 575 | How many miles south of San Jose is the north - so... | 11 | 11 | -1.0000 | ✅ |
| 576 | The term "southern" California usually refers to h... | ten | ten | 0.0000 | ✅ |
| 577 | Other than Point Conception, what landmark is used... | Tehachapi Mountains | The Tehachapi Mountains | 0.0000 | ❌ |
| 578 | Point Conception is an example of a landmark among... | northern | Point Conception | 0.0000 | ❌ |
| 579 | What lies at 37° 8' 59.23" latitude? | NO ANSWER | NO ANSWER | 0.0659 | ✅ |
| 580 | What is around 18 miles south of San Jose? | NO ANSWER | 11 miles | -0.1763 | ❌ |
| 581 | What lies at 35° 48′ 27″ north latitude? | NO ANSWER | NO ANSWER | 0.1575 | ✅ |
| 582 | What uses Point Tehachapi and the Conception Mount... | NO ANSWER | An definition for southern California | 0.0001 | ❌ |
| 583 | Which country used to rule California? | Mexico | Mexico | 0.0000 | ✅ |
| 584 | Los Angeles is in the lower part of what? | Alta California | lower part of Alta California | -0.0131 | ❌ |
| 585 | Which Californio is located in the upper part? | Monterey | Mon Monterey | 0.0000 | ❌ |
| 586 | What was the name of the legislation passed in 185... | the Missouri Compromise | Compromise of 1850 | 0.0000 | ❌ |
| 587 | The legislation allowed California to be admitted ... | free | free state | 0.0000 | ❌ |
| 588 | What country did California once rule? | NO ANSWER | Mexico | 0.0000 | ❌ |
| 589 | Who were there disputes between when California ru... | NO ANSWER | The Californios of Monterey in the upper part and Los Angeles in | 0.0000 | ❌ |
| 590 | What line is at 30 degrees, 36 minutes? | NO ANSWER | The line of the Missouri Compromise | -0.2726 | ❌ |
| 591 | What was passed in 1805? | NO ANSWER | NO ANSWER | 0.6965 | ✅ |
| 592 | Other than land laws, what else were the Californi... | inequitable taxes | taxes | 0.0000 | ❌ |
| 593 | What was the name given to the regions in which th... | Cow Counties | Cow Counties | -0.6696 | ✅ |
| 594 | How many times did southern California attempt to ... | three | Three | 0.0000 | ✅ |
| 595 | What was the percentage of people that voted in fa... | 75 | 75% | -0.8630 | ❌ |
| 596 | Which Senator was a strong advocate for the Pico A... | Milton Latham | Senator Milton Latham | 0.0000 | ❌ |
| 597 | Who attempted to achieve a separate statehood in 1... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 598 | What was passed in 1895? | NO ANSWER | NO ANSWER | 0.9318 | ✅ |
| 599 | Who was the governor of California in 1895? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 600 | Who was elected in 1859? | NO ANSWER | Ab Abraham Lincoln | 0.0000 | ❌ |
| 601 | What title did Latham Milton hold? | NO ANSWER | Senator | 0.0000 | ❌ |
| 602 | Which newspaper defined southern California? | Los Angeles Times | The Los Angeles Times | 0.0000 | ❌ |
| 603 | In which year did the newspaper define southern Ca... | 1900 | 1900 | -0.9754 | ✅ |
| 604 | In which year did the newspaper change its previou... | 1999 | 1999 | -0.9437 | ✅ |
| 605 | What was the newer county added to the list? | Imperial | Imperial | -1.0000 | ✅ |
| 606 | How many counties initially made up the definition... | seven | 7 | 0.0000 | ❌ |
| 607 | How did the Los Angeles Times define southern Cali... | NO ANSWER | NO ANSWER | 0.8589 | ✅ |
| 608 | What did the Los Angeles Times add to the definiti... | NO ANSWER | NO ANSWER | 0.9439 | ✅ |
| 609 | What did the California Times define twice? | NO ANSWER | seven counties | -0.1129 | ❌ |
| 610 | Which organizations most commonly divide and promo... | regional tourism groups | Two | -0.7252 | ❌ |
| 611 | Other than the Automobile Club of Southern Califor... | California State Automobile Association | California State Automobile Association | -0.4558 | ✅ |
| 612 | The two AAA clubs divided the state into a norther... | three-region | Three-region | -0.0427 | ✅ |
| 613 | Which mountain range influenced the split of the r... | Tehachapis | The Tehachapis | -0.5800 | ❌ |
| 614 | In the definition based off the mountain range, wh... | southern | the southern | -0.1684 | ❌ |
| 615 | What type of club is the California Automobile Sta... | NO ANSWER | The California State Automobile Association | -0.2525 | ❌ |
| 616 | What type of club is the Southern California Autom... | NO ANSWER | AAA | -0.3418 | ❌ |
| 617 | What type of phrase is North of the Tehachapis? | NO ANSWER | Ge geographical | 0.0000 | ❌ |
| 618 | What type of groups divides California into only n... | NO ANSWER | auto | -0.1764 | ❌ |
| 619 | Where does southern California's megalopolis stand... | third | NO ANSWER | 0.0216 | ❌ |
| 620 | Although southern california consts of a heavily d... | vast areas | NO ANSWER | 0.0581 | ❌ |
| 621 | Southern Californian communities are well known to... | suburban | NO ANSWER | 0.0110 | ❌ |
| 622 | Outside of its use of automobiles, what else is so... | highways | NO ANSWER | 0.1268 | ❌ |
| 623 | What kind of region can be found inside the urban ... | international metropolitan | megalopolis | -0.0146 | ❌ |
| 624 | What are the second and third most populated megal... | NO ANSWER | 1. The Great Lakes Megalopolis, and the Northeast | 0.0094 | ❌ |
| 625 | What are the dominant areas of Los Angeles? | NO ANSWER | Los Angeles, Orange County, San Diego, and Riverside-San | 0.0000 | ❌ |
| 626 | What international metropolitan region is in the N... | NO ANSWER | NO ANSWER | 0.2702 | ✅ |
| 627 | What is the main gap to continued urbanization? | Camp Pendleton | Camp Pendleton | 0.0000 | ✅ |
| 628 | Other than the San Diego metropolitan area, what o... | Inland Empire | The Inland Empire | -0.1051 | ❌ |
| 629 | Who considers Los Angeles County to be a separate ... | United States Census Bureau | The United States Census Bureau | 0.0000 | ❌ |
| 630 | Other than L.A. which other county do many people ... | Orange | Orange | 0.0000 | ✅ |
| 631 | Other than the 1980s, in which decade did most of ... | 1990s | The 1990s | -0.5041 | ❌ |
| 632 | What was developed in 1980? | NO ANSWER | 1990s | -0.2327 | ❌ |
| 633 | What counties to most people commute to? | NO ANSWER | NO ANSWER | 0.0116 | ✅ |
| 634 | What formed in the Coachella Valley north of Orang... | NO ANSWER | New cities | -0.0779 | ❌ |
| 635 | What counties near Kern-Bakersfield County was pop... | NO ANSWER | Bakersfield-Kern County, Santa Maria and San Luis Ob | 0.0000 | ❌ |
| 636 | What kind of climate does southern California main... | Mediterranean | Mediterranean | 0.0000 | ✅ |
| 637 | Other than many sunny days, what characteristic is... | infrequent rain | NO ANSWER | 0.0223 | ❌ |
| 638 | What is the low end of the temperature range in su... | 60's | 60 | -1.0000 | ❌ |
| 639 | How frequent is snow in the Southwest of the state... | very rare | NO ANSWER | 0.1001 | ❌ |
| 640 | What is the high end of the temperature range in w... | 70 | 80's | -0.5624 | ❌ |
| 641 | What type of climate does California have? | NO ANSWER | NO ANSWER | 0.0332 | ✅ |
| 642 | Where are summer temperature ranges 70-50s? | NO ANSWER | winters | -0.0841 | ❌ |
| 643 | Where are winter temperature ranges 90-60s? | NO ANSWER | NO, | 0.0061 | ❌ |
| 644 | What is rare on the Southeast of the state? | NO ANSWER | Snow | 0.0000 | ❌ |
| 645 | What term best describes southern California's col... | varied | NO ANSWER | 0.0373 | ❌ |
| 646 | The region spans starting at islands found in whic... | Pacific Ocean | Pacific Ocean | 0.0000 | ✅ |
| 647 | What type of landscapes other than geologic and na... | topographic | transverse | 0.0089 | ❌ |
| 648 | The region spans which mountains other than the Tr... | Peninsular | Peninsular Ranges | 0.0000 | ❌ |
| 649 | The mountain ranges tail off into what kind of geo... | valleys | large and small interior valleys | -0.0091 | ❌ |
| 650 | What types of collections does desert California h... | NO ANSWER | Geologic, topographic, and natural ecosystem landscapes | 0.0000 | ❌ |
| 651 | What ocean has the Transverse and Peninsular Range... | NO ANSWER | Pacific | 0.0000 | ❌ |
| 652 | What ocean has large and small interior valleys? | NO ANSWER | NO ANSWER | 0.0731 | ✅ |
| 653 | What area has the most diversity of anywhere in th... | NO ANSWER | NO ANSWER | 0.0533 | ✅ |
| 654 | How many earthquakes does southern California expe... | 10,000 | 10,000 | -0.8671 | ✅ |
| 655 | Generally speaking, what size are the earthquakes ... | small | NO ANSWER | 0.0113 | ❌ |
| 656 | What magnitude was the 1994 Northridge earthquake? | 6.7 | 6.7 | -0.9719 | ✅ |
| 657 | What kind of destruction did the 1994 earthquake c... | property damage | Property damage | 0.0000 | ✅ |
| 658 | How much was the 1994 earthquake estimated to have... | $20 billion | $20 billion | 0.0000 | ✅ |
| 659 | What year was the Northridge earthquake that cause... | NO ANSWER | NO ANSWER | 0.8057 | ✅ |
| 660 | What earthquake caused $20 million in damage? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 661 | How many earthquakes does the state of California ... | NO ANSWER | 10,000 | -0.8498 | ❌ |
| 662 | How many earthquakes are greater than a 4.7 magnit... | NO ANSWER | NO ANSWER | 0.7976 | ✅ |
| 663 | Which fault can produce a magnitude earthquake of ... | San Andreas | The San Andreas Fault | 0.0000 | ❌ |
| 664 | What magnitude of earthquake can many faults produ... | 6.7 | 6.7+ | -0.5918 | ❌ |
| 665 | Other than the San Jacinto Fault, and the Elsinore... | Puente Hills | Puente Hills Fault | 0.0000 | ❌ |
| 666 | Which organization released a California Earthquak... | USGS | The USGS | 0.0000 | ❌ |
| 667 | The earthquake forecast models what features of ea... | occurrence | USGS earthquake forecast models Earthquake occurrence in California | -0.0505 | ❌ |
| 668 | What fault can produce a magnitude 8.7 event? | NO ANSWER | NO ANSWER | 0.8034 | ✅ |
| 669 | What faults other than the San Andreas can produce... | NO ANSWER | The San Jacinto Fault, the Puente Hills Fault, and | 0.0000 | ❌ |
| 670 | What did the UGSS release? | NO ANSWER | California Earthquake forecast | 0.0000 | ❌ |
| 671 | What does the UGSS California Earthquake forecast ... | NO ANSWER | NO ANSWER | 0.0950 | ✅ |
| 672 | Southern California's distinctive regions are divi... | economically | economically | -0.0499 | ✅ |
| 673 | Outside of national recognition, what other kind o... | global | Some of the national and sometimes global recognition | 0.0067 | ❌ |
| 674 | Cities that anchor the regions are often the hub f... | economic | economic | 0.0000 | ✅ |
| 675 | What are regions anchored by that are recognized g... | NO ANSWER | Cities | 0.0000 | ❌ |
| 676 | What are the globally recognized anchor cities kno... | NO ANSWER | Their economic activity and tourist destinations | 0.0000 | ❌ |
| 677 | How is California divided? | NO ANSWER | Southern California is divided culturally, politically, and economically into distinctive regions | -0.1218 | ❌ |
| 678 | Southern California had a population of 22,680,010... | 2010 | 2010 | -1.0000 | ✅ |
| 679 | What does southern California have a reputation fo... | high growth rates | high growth rates | 0.0000 | ✅ |
| 680 | What is the state average growth rate? | 10.0% | 10.0% | -1.0000 | ✅ |
| 681 | What kind of economy did northern California start... | tech-oriented | tech-oriented economy | 0.0000 | ❌ |
| 682 | Which region began to grow and assert itself in th... | Greater Sacramento | the northern part of the state | 0.0000 | ❌ |
| 683 | What census showed southern California as having a... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 684 | How much did southern California grow in the year ... | NO ANSWER | NO ANSWER | 0.6218 | ✅ |
| 685 | What economy started growing in the Greater Bay Re... | NO ANSWER | Tech | 0.0000 | ❌ |
| 686 | What city is in the Greater Bay Region? | NO ANSWER | NO ANSWER | 0.2010 | ✅ |
| 687 | What is the name associated with the eight areas t... | Metropolitan Statistical Areas | Two | -0.0318 | ❌ |
| 688 | How many extended metropolitan areas are there? | two | 2 | -0.1107 | ❌ |
| 689 | Each of the extended metropolitan areas has a popu... | five million | 5 million | -0.4531 | ❌ |
| 690 | What does the El Centro metropolitan area and San ... | Southern Border Region | The Southern Border Region | -0.0608 | ❌ |
| 691 | What is the population of the Greater Los Angeles ... | 17,786,419 | 17,786,419 | -1.0000 | ✅ |
| 692 | What consists of one Metropolitan Statistical Area... | NO ANSWER | Southern California | -0.4470 | ❌ |
| 693 | What consists of eight Combined Statistical Areas? | NO ANSWER | Southern California | -0.7998 | ❌ |
| 694 | What area has a population of 17,786,914? | NO ANSWER | NO ANSWER | 0.0207 | ✅ |
| 695 | What area has a population of 5,105,786? | NO ANSWER | San Diego–Tijuana | 0.0000 | ❌ |
| 696 | What areas are north of Greater Santa Barbara? | NO ANSWER | Santa Barbara, San Luis Obispo, and Bakersfield | 0.0000 | ❌ |
| 697 | What is the largest city in all of California? | Los Angeles | Los Angeles | -1.0000 | ✅ |
| 698 | What is the population of the second largest city ... | 1.3 million | 1.3 million | -0.7267 | ✅ |
| 699 | How many cities in southern California have over 2... | twelve | 12 | 0.0000 | ❌ |
| 700 | There are 34 cities in southern California that ha... | 100,000 | 100,000 | -0.9549 | ✅ |
| 701 | Other than San Bernardino, which other developed s... | Riverside | Riverside | 0.0000 | ✅ |
| 702 | What are the two largest cities in the United Stat... | NO ANSWER | NO ANSWER | 0.4132 | ✅ |
| 703 | Where are there 34 cities over 200,000 in populati... | NO ANSWER | sou southern California | -0.0135 | ❌ |
| 704 | Where are there 12 cities over 100,000 in populati... | NO ANSWER | Southern California | 0.0000 | ❌ |
| 705 | What city has a population of 3.3 million people? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 706 | What city has a population of 1.7 million people? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 707 | What resource is the economy of southern Californi... | petroleum | Pet petroleum | 0.0000 | ❌ |
| 708 | Southern California is most famous for tourism and... | Hollywood | film | -0.1049 | ❌ |
| 709 | The region was a leader in what event between 2001... | the housing bubble | The region was a leader in the housing bubble | 0.0000 | ❌ |
| 710 | Southern California's economy can be described as ... | diverse | dom dominated | 0.0000 | ❌ |
| 711 | What was the effect of the housing crash on the re... | heavily impacted | was heavily impacted | 0.0000 | ❌ |
| 712 | Who does the largest economy in the United States ... | NO ANSWER | NO ANSWER | 0.4132 | ✅ |
| 713 | What took place during 2000-2017? | NO ANSWER | The housing bubble 2001–2007 | -0.0650 | ❌ |
| 714 | What is southern California's economy completely d... | NO ANSWER | Pet petroleum | -0.0306 | ❌ |
| 715 | Where is southern Hollywood located? | NO ANSWER | NO ANSWER | 0.3856 | ✅ |
| 716 | Motion pictures, petroleum and aircraft manufactur... | 1920s | 1920s | -0.6176 | ✅ |
| 717 | What characteristic best describes the agricultura... | richest | NO ANSWER | 0.0350 | ❌ |
| 718 | Which type of livestock was the argricultural regi... | cattle | cattle | 0.0000 | ✅ |
| 719 | Outside of livestock, what else was considered a m... | citrus | Cit citrus | 0.0000 | ❌ |
| 720 | What industry has managed to survive major militar... | aerospace | aerospace | 0.0000 | ✅ |
| 721 | What have been major industries since 1902? | NO ANSWER | NO ANSWER | 0.1327 | ✅ |
| 722 | What were major industries until suburbs were turn... | NO ANSWER | cattle and citrus | 0.0000 | ❌ |
| 723 | What is a major factor even with aerospace cutback... | NO ANSWER | major factor | 0.0000 | ❌ |
| 724 | What year were farmlands turned into suburbs? | NO ANSWER | NO ANSWER | 0.6425 | ✅ |
| 725 | What type of district is southern California home ... | business | business districts | -0.0229 | ❌ |
| 726 | What does CBD stand for? | Central business districts | Central business districts | -0.1498 | ✅ |
| 727 | What is the only district in the CBD to not have "... | South Coast Metro | NO ANSWER | 0.0312 | ❌ |
| 728 | What does CDB stand for? | NO ANSWER | CBD | -0.4985 | ❌ |
| 729 | What does CDB include? | NO ANSWER | Commercial and business districts | -0.1808 | ❌ |
| 730 | What does DCB stand for? | NO ANSWER | DC | -0.1539 | ❌ |
| 731 | Downtown Burbank is an example of what kind of dis... | business | Business district | 0.0000 | ❌ |
| 732 | Downtown Santa Monica and Downtown Glendale are a ... | Los Angeles Area | The Los Angeles Area | -0.0307 | ❌ |
| 733 | Warner Center is located in which area? | San Fernando Valley | The San Fernando Valley | 0.0000 | ❌ |
| 734 | Century City is an example of a district that belo... | Los Angeles | Century City | -0.0273 | ❌ |
| 735 | What business districts are within the downtown Lo... | NO ANSWER | NO ANSWER | 0.0232 | ✅ |
| 736 | What main business district is in downtown Los Ang... | NO ANSWER | The Downtown Los Angeles central business district | 0.0000 | ❌ |
| 737 | What additional business districts are in downtown... | NO ANSWER | Downtown Los Angeles central business district, Wilshire Boulevard Miracle Mile | 0.0000 | ❌ |
| 738 | The Sand Bernardino - Riverside area maintains wha... | business | Business districts | -0.0231 | ❌ |
| 739 | Other than San Bernardino, what is the name of the... | Riverside | Riverside | 0.0000 | ✅ |
| 740 | Other than Downtown San Bernardino, and University... | Hospitality Business/Financial Centre | Hospital Hospitality Business/Financial Centre | -0.0368 | ❌ |
| 741 | What business districts does the San Bernardino ar... | NO ANSWER | Hospital, Downtown San Bernardino, Hospitality Business/Financial Centre, University | -0.0215 | ❌ |
| 742 | What business districts does the Riverside area ma... | NO ANSWER | Hospital, Business/Financial Centre, University Town | -0.0385 | ❌ |
| 743 | Which county is developing its business center? | Orange | Orange | -1.0000 | ✅ |
| 744 | Where are international corporations headquartered... | University of California, Irvine | University of California, Irvine | 0.0000 | ✅ |
| 745 | Jamboree Business Parks belongs to which business ... | West Irvine | West Irvine | 0.0000 | ✅ |
| 746 | What other business district does Orange County en... | South Coast Metro | The South Coast Metro | 0.0000 | ❌ |
| 747 | At what rate is Orange County developing its busin... | rapidly | NO ANSWER | 0.2135 | ❌ |
| 748 | What county does the rapidly developing downtown S... | NO ANSWER | Orange | -1.0000 | ❌ |
| 749 | What districts does downtown Santa Ana include? | NO ANSWER | South Coast Metro and Newport Center | 0.0000 | ❌ |
| 750 | What locations are headquartered at the California... | NO ANSWER | International corporations | 0.0098 | ❌ |
| 751 | What includes Irvine Center Tech and Business Jamb... | NO ANSWER | West Irvine | 0.0000 | ❌ |
| 752 | What is the central business district of San Diego... | Downtown San Diego | Downtown San Diego | -1.0000 | ✅ |
| 753 | Other than its main central  business district, wh... | Northern San Diego | Most of these districts are located in Northern San Diego and some within | 0.0000 | ❌ |
| 754 | Outside of Northern San Diego, which other region ... | North County | NO ANSWER | 0.0182 | ❌ |
| 755 | University City is an example of a business distri... | San Diego | NO ANSWER | 0.0255 | ❌ |
| 756 | What is the central business district of downtown ... | NO ANSWER | Downtown San Diego | -0.8068 | ❌ |
| 757 | What are located in Northern downtown San Diego? | NO ANSWER | NO ANSWER | 0.0804 | ✅ |
| 758 | What business districts are located in Northern do... | NO ANSWER | NO ANSWER | 0.1466 | ✅ |
| 759 | What is the second busiest airport in the United S... | Los Angeles International Airport | Los Angeles International Airport | 0.0000 | ✅ |
| 760 | What is the metric they use to determine how busy ... | passenger volume | NO ANSWER | 0.0568 | ❌ |
| 761 | What ranking in terms of busiest airports from int... | third | Third | 0.0000 | ✅ |
| 762 | Which airport is home to the busiest single runway... | San Diego International Airport | San Diego International Airport | 0.0000 | ✅ |
| 763 | What is the world's busiest general aviation airpo... | Van Nuys Airport | Van Nuys Airport | 0.0000 | ✅ |
| 764 | What is the busiest airport by passenger volume in... | NO ANSWER | NO ANSWER | 0.2529 | ✅ |
| 765 | What is the second-busiest single runway airport i... | NO ANSWER | NO ANSWER | 0.4874 | ✅ |
| 766 | What is the second-busiest general aviation airpor... | NO ANSWER | NO ANSWER | 0.0855 | ✅ |
| 767 | What major commercial airports are located in Los ... | NO ANSWER | Orange County, Bakersfield, Ontario, Burbank, and | 0.0000 | ❌ |
| 768 | What is the name of the commuter rail system? | Metrolink | Metrolink | 0.0000 | ✅ |
| 769 | How many lines does the commuter rail system have? | seven | Seven | -0.0274 | ✅ |
| 770 | How many lines run out of Downtown Los Angeles? | Six | Six | -0.6551 | ✅ |
| 771 | A single line connects San Bernardino, Riverside a... | Orange | Orange | 0.0000 | ✅ |
| 772 | Where do seven lines of Metrolink run out of? | NO ANSWER | Downtown Los Angeles | 0.0000 | ❌ |
| 773 | What is the name of the Los Angeles rail system? | NO ANSWER | Metrolink | 0.0000 | ❌ |
| 774 | What counties are connected to Los Angeles, Ventur... | NO ANSWER | Los Angeles, Ventura, and San Bernardino | -0.0017 | ❌ |
| 775 | What is the United States busiest commercial port? | Port of Los Angeles | NO ANSWER | 0.0530 | ❌ |
| 776 | What is the second busiest container port in the U... | Port of San Diego | Port of Long Beach | 0.0000 | ❌ |
| 777 | The Port of Long Beach belongs to which region of ... | Southern | Southern California | -0.6355 | ❌ |
| 778 | What is home to Southern California? | NO ANSWER | Three | -0.0293 | ❌ |
| 779 | What is the busiest container port in the United S... | NO ANSWER | NO ANSWER | 0.2115 | ✅ |
| 780 | What is the Port of San Diego adjacent to? | NO ANSWER | Los Angeles | -0.0407 | ❌ |
| 781 | What is the United State's second-busiest commerci... | NO ANSWER | Port of Long Beach | 0.0000 | ❌ |
| 782 | What is the moniker that is being used to describe... | The Tech Coast | The Tech Coast | -0.8982 | ✅ |
| 783 | What kind of universities is the region famous for... | research | world-renowned research universities | -0.0303 | ❌ |
| 784 | What kind of university is the California Institut... | private | Private | 0.0000 | ✅ |
| 785 | How many campuses does the University of Californi... | 5 | 6 | -0.6984 | ❌ |
| 786 | How many campuses does the California State Univer... | 12 | 15 | -0.8951 | ❌ |
| 787 | What are the 5 California University campuses? | NO ANSWER | Irvine, Los Angeles, Riverside, Santa Barbara, and San | -0.4196 | ❌ |
| 788 | How many California University campuses are there? | NO ANSWER | 28 | 0.0000 | ❌ |
| 789 | How many State of California University campuses a... | NO ANSWER | There is a 12 California State University campuses | -0.0354 | ❌ |
| 790 | Where is Redland University located? | NO ANSWER | NO ANSWER | 0.1590 | ✅ |
| 791 | Where is Pomona University located? | NO ANSWER | NO ANSWER | 0.0839 | ✅ |
| 792 | The Los Angeles Rams are an example of what kind o... | NFL | Professional | -0.1083 | ❌ |
| 793 | The Los Angeles Clippers are a team belonging to w... | NBA | NBA | 0.0000 | ✅ |
| 794 | The Los Angeles Angels of Anaheim are from which s... | MLB | ML | 0.0000 | ❌ |
| 795 | What is the other NHL team aside from the Anaheim ... | Los Angeles Kings | Los Angeles Kings | -0.9417 | ✅ |
| 796 | What is the lone MLS team that belongs to southern... | LA Galaxy | LA Galaxy | -0.7947 | ✅ |
| 797 | What NLF teams are from Southern California? | NO ANSWER | Los Angeles Rams, Los Angeles Chargers | -0.6869 | ❌ |
| 798 | What NAB teams are from Southern California? | NO ANSWER | Los Angeles Lakers, Los Angeles Clippers, Los Angeles Dodgers, Los | -0.4063 | ❌ |
| 799 | What MBL teams are from Southern California? | NO ANSWER | Los Angeles Dodgers, Los Angeles Angels of Anaheim | -0.6603 | ❌ |
| 800 | What NLH teams are from Southern California? | NO ANSWER | Los Angeles Kings, Anaheim Ducks | -0.4452 | ❌ |
| 801 | What MSL team is from Southern California? | NO ANSWER | LA Galaxy | -0.8422 | ❌ |
| 802 | Which team was suspended from the MLS? | Chivas USA | Chivas USA | 0.0000 | ✅ |
| 803 | How many teams did Los Angeles used to have? | two | 2 | 0.0000 | ❌ |
| 804 | Which year resulted in the suspension of one of th... | 2014 | 2014 | -1.0000 | ✅ |
| 805 | What was the name of the stadium that the teams pl... | StubHub Center | The StubHub Center | 0.0000 | ❌ |
| 806 | When is the suspended team scheduled to return? | 2018 | 2018 | -0.7035 | ✅ |
| 807 | How many Major Soccer League teams were in Los Ang... | NO ANSWER | 2 | 0.0000 | ❌ |
| 808 | What Major Soccer League teams played in Los Angel... | NO ANSWER | There were two Major League Soccer teams in Los Angeles in 201 | 0.0000 | ❌ |
| 809 | When were the LA Galaxy suspended? | NO ANSWER | NO ANSWER | 0.6834 | ✅ |
| 810 | When is a second MSL team scheduled to return? | NO ANSWER | In 2018 | -0.6805 | ❌ |
| 811 | What other kind of sport is popular in southern Ca... | College | College sports | -0.3863 | ❌ |
| 812 | The Bruins belong to which college? | UCLA | UCLA | 0.0000 | ✅ |
| 813 | What is the name of the team from USC? | Trojans | Trojans | 0.0000 | ✅ |
| 814 | Which conference do the teams in southern Californ... | Pac-12 | P12 | 0.0000 | ❌ |
| 815 | The two listed teams play for which NCAA group? | Division I | NO ANSWER | 0.0213 | ❌ |
| 816 | What is the ULCA mascot? | NO ANSWER | NO ANSWER | 0.0308 | ✅ |
| 817 | What is the UCS mascot? | NO ANSWER | Brujans | 0.0000 | ❌ |
| 818 | What conference are both ULCA and UCS part of? | NO ANSWER | NO ANSWER | 0.0510 | ✅ |
| 819 | What is a growing sport in southern California? | Rugby | rugby | -0.9116 | ✅ |
| 820 | At which level of education is this sport becoming... | high school | The high school level | 0.0000 | ❌ |
| 821 | What is rugby rapidly becoming with high schools? | an official school sport | an official school sport | -0.0212 | ✅ |
| 822 | What sport is growing in all California schools? | NO ANSWER | Rugby | -0.2956 | ❌ |
| 823 | What company was formed by the merger of Sky Telev... | BSkyB | BSkyB | 0.0000 | ✅ |
| 824 | Who is the UK's largest digital subscription telev... | BSkyB | NO ANSWER | 0.0449 | ❌ |
| 825 | What year did BSkyB acquire Sky Italia? | 2014 | 2014 | -1.0000 | ✅ |
| 826 | What is the name of the holding company for BSkyB? | Sky plc | Sky plc | 0.0000 | ✅ |
| 827 | What is the name of the United Kingdom operation f... | Sky UK Limited | Sky UK Limited | 0.0000 | ✅ |
| 828 | What company was angry about the merger of Sky Tel... | NO ANSWER | NO ANSWER | 0.7638 | ✅ |
| 829 | Who is the UK's smallest digital subscription tele... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 830 | What year did BSkyB remove Sky Italia? | NO ANSWER | NO ANSWER | 0.8977 | ✅ |
| 831 | When did BSkyB become the largest US television co... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 832 | What company no longer trades as Sky? | NO ANSWER | NO ANSWER | 0.0258 | ✅ |
| 833 | What year was Setanta Sports awarded Primeier Leag... | 2006 | 2006 | -0.8658 | ✅ |
| 834 | How many of the six total packages available to br... | two | Two | -0.1673 | ✅ |
| 835 | Who purhcased the remaining 4 pacakages available ... | Sky | Sky | 0.0000 | ✅ |
| 836 | How much did Sky bid to win the 4 broadcast pacakg... | £1.3bn | £4.2bn | 0.0000 | ❌ |
| 837 | Which company had a short legal battle with the Eu... | NO ANSWER | BSkyB | 0.0000 | ❌ |
| 838 | How many of the six total packages available to br... | NO ANSWER | Two | -0.1613 | ❌ |
| 839 | Sky lost how many packages? | NO ANSWER | 4 | -0.3183 | ❌ |
| 840 | How much did Sky bid to lose the 4 broadcast packa... | NO ANSWER | NO ANSWER | 0.1216 | ✅ |
| 841 | What channel was never dropped from Sky? | NO ANSWER | NO ANSWER | 0.6240 | ✅ |
| 842 | What consortium was BSkyB excluded from? | ONdigital | ONdigital | 0.0000 | ✅ |
| 843 | Who did BSkyB team up with because it was not part... | Freeview | NO ANSWER | 0.0424 | ❌ |
| 844 | How many BSkyB channels were available to customer... | three | Three | 0.0000 | ✅ |
| 845 | What channel replaced Sky Travel? | Sky Three | Sky Three | 0.0000 | ✅ |
| 846 | What was Sky Travel later rebranded as? | Pick TV | Pick TV | -1.0000 | ✅ |
| 847 | What consortium was BSkyB included with? | NO ANSWER | BSkyB was part of ITV Digital's free-to-air replacement | -0.0157 | ❌ |
| 848 | What was Pick TV later rebranded as? | NO ANSWER | Pick | -0.9774 | ❌ |
| 849 | What channel came before Sky Travel? | NO ANSWER | Sky News | 0.0000 | ❌ |
| 850 | Who did BSkyB team up with because it was part of ... | NO ANSWER | ITB, BBC, ITV, Channel 4 and National Grid | 0.0000 | ❌ |
| 851 | What channel was never rebranded? | NO ANSWER | NO ANSWER | 0.3588 | ✅ |
| 852 | What service did BSkyB chare additional subscripti... | Sky+ PVR | Initially, BSkyB charged additional subscription fees for using a Sky | -0.0301 | ❌ |
| 853 | When did Sky launch a TV advertising campaign targ... | September 2007 | September 2007 | 0.0000 | ✅ |
| 854 | WHat allows customers to get Sky+ functions if the... | monthly fee | NO ANSWER | 0.0573 | ❌ |
| 855 | When did BSkyB discontinue the Sky+ Box? | January 2010 | January 2010 | -0.2913 | ✅ |
| 856 | What replaced the Sky+Box? | Sky+HD Box | The Sky+HD Box | 0.0000 | ❌ |
| 857 | What service did BSkyB give away for free uncondit... | NO ANSWER | BSkyB included Sky+ at no extra charge for customers with | -0.0111 | ❌ |
| 858 | When did Sky launch a TV advertising campaign targ... | NO ANSWER | NO ANSWER | 0.8646 | ✅ |
| 859 | What isn't required by customers to get Sky+ funct... | NO ANSWER | NO ANSWER | 0.0226 | ✅ |
| 860 | When did BSkyB upgrade the Sky+ Box? | NO ANSWER | In January 2010 | -0.4244 | ❌ |
| 861 | What replaced the Sky+HD Box? | NO ANSWER | smaller version of the SkyHD box without Sky+ functionality | 0.0000 | ❌ |
| 862 | What is the name of the TV scrambling system BSkyB... | VideoGuard | VideoGuard | 0.0000 | ✅ |
| 863 | Who is VideoGuard owned by? | NDS | NDS, a Cisco Systems company | 0.0000 | ❌ |
| 864 | Who is the parent company of NDS? | Cisco Systems | Cisco Systems | 0.0000 | ✅ |
| 865 | Who has design authority over all of the digital s... | BSkyB | BSkyB | -1.0000 | ✅ |
| 866 | What is the name brand of the personal video recor... | Sky+ | Sky+ | 0.0000 | ✅ |
| 867 | What is the name of the TV scrambling system BSkyB... | NO ANSWER | NO ANSWER | 0.3433 | ✅ |
| 868 | Whose digital receivers are only built by one manu... | NO ANSWER | They | -0.1400 | ❌ |
| 869 | What is available as stand-alone DVB CAMs? | NO ANSWER | NO ANSWER | 0.4812 | ✅ |
| 870 | What company was never involved with NDS? | NO ANSWER | NO ANSWER | 0.1805 | ✅ |
| 871 | What is the name brand of the video recorder that ... | NO ANSWER | NO ANSWER | 0.3484 | ✅ |
| 872 | What year did BSkyB and Virgin Media have a disput... | 2007 | 2007 | -1.0000 | ✅ |
| 873 | What channels were removed from the network in Mar... | basic channels | NO ANSWER | 0.1476 | ❌ |
| 874 | What did Virgin Media claim BSkyB did that resulte... | substantially increased the asking price | Substantially increased the asking price for the channels | -0.2017 | ❌ |
| 875 | What additional srevice did BSkyB offer besides HD... | Video On Demand | Video On Demand content | 0.0000 | ❌ |
| 876 | What additional srevice did BSkyB offer besides Vi... | HD channels | HD channels | 0.0000 | ✅ |
| 877 | What year did BSkyB and Virgin Media have an agree... | NO ANSWER | 2007 | -0.5175 | ❌ |
| 878 | What channels were always available on the network... | NO ANSWER | NO ANSWER | 0.4571 | ✅ |
| 879 | What additional service did BSkyB offer besides HD... | NO ANSWER | NO ANSWER | 0.0252 | ✅ |
| 880 | What claim did BSkyB agree with? | NO ANSWER | NO ANSWER | 0.1751 | ✅ |
| 881 | When were basic channels first introduced by BSkyB... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 882 | when did the English High court find Microsoft's u... | July 2013 | July 2013 | -0.1067 | ✅ |
| 883 | What year did BSkyB and Microsoft announce their s... | 2013 | 2013 | -1.0000 | ✅ |
| 884 | What did Microsoft announce that it would rename S... | OneDrive | OneDrive | -0.9401 | ✅ |
| 885 | What did Microsoft announce that it would rename S... | OneDrive for Business | OneDrive for Business | -0.9305 | ✅ |
| 886 | What kind of service is the SkyDrive Service? | cloud storage | Cloud storage service | 0.0000 | ❌ |
| 887 | When did the English High Court of Justice find th... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 888 | When did Microsoft decide to appeal the ruling? | NO ANSWER | NO ANSWER | 0.9474 | ✅ |
| 889 | What did Microsoft announce that it would rename O... | NO ANSWER | "SkyDrive" | -0.4345 | ❌ |
| 890 | What did Microsoft announce that it would rename O... | NO ANSWER | OneDrive for Business | -0.7995 | ❌ |
| 891 | When did Microsoft announce OneDrive will soon bec... | NO ANSWER | 27 January 2014 | -0.7790 | ❌ |
| 892 | Who was the chief executive officer when the servi... | Sam Chisholm | Sam Chisholm | 0.0000 | ✅ |
| 893 | Who's satellites would the new free-to-air channel... | Astra | Astra's | 0.0000 | ❌ |
| 894 | When did BSkyB end their analogue service? | 27 September 2001 | 27 September 2001 | -1.0000 | ✅ |
| 895 | What platform caused BSkyB to end their analogue s... | Sky Digital | the launch and expansion of the Sky Digital platform | -0.8872 | ❌ |
| 896 | How many households had BSkyB service in 1994? | 3.5 million | 3.5 million | -1.0000 | ✅ |
| 897 | What platform helped BSkyB to avoid ending their a... | NO ANSWER | The launch and expansion of the Sky Digital platform | -0.6596 | ❌ |
| 898 | Whose satellites were never broadcast as free-to-a... | NO ANSWER | NO ANSWER | 0.0478 | ✅ |
| 899 | How many subscribers were lost within two months o... | NO ANSWER | NO ANSWER | 0.7435 | ✅ |
| 900 | Who commended the operations in front of the Selec... | NO ANSWER | Michael Grade | 0.0000 | ❌ |
| 901 | Which company never expanded their platform? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 902 | Sky UK Limited is formerly known by what name? | BSkyB | British Sky Broadcasting or BSkyB | 0.0000 | ❌ |
| 903 | What kind of company is Sky UK Limited? | telecommunications | Tele telecommunications company | -0.0219 | ❌ |
| 904 | How many customers does Sky UK Limited have as a p... | 11 million | 11 million | -1.0000 | ✅ |
| 905 | what other digital TV service took Sky UK Limited'... | Freeview | Freeview | 0.0000 | ✅ |
| 906 | Sky UK Limited is now known by what name? | NO ANSWER | Sky UK Limited (formerly British Sky Broadcasting or BSkyB) | -0.5937 | ❌ |
| 907 | What has Sky UK Limited never been involved with? | NO ANSWER | NO ANSWER | 0.4392 | ✅ |
| 908 | How many customers did Sky UK Limited lose as a pa... | NO ANSWER | 11 million | -0.1674 | ❌ |
| 909 | What was the UK's least popular TV service in 2015... | NO ANSWER | NO ANSWER | 0.7904 | ✅ |
| 910 | Where did the headquarters relocate from? | NO ANSWER | NO ANSWER | 0.1782 | ✅ |
| 911 | What is the name of Sky Q's broadband router? | Sky Q Hub | Sky Q Hub | -0.8882 | ✅ |
| 912 | What are the Sky Q mini set top boxes able to conn... | Sky Q Silver set top boxes | Sky Q Silver set top boxes | -0.2701 | ✅ |
| 913 | What does connecting different Sky Q boxes enable ... | share recordings | allow all set top boxes in a household to share recordings and other | 0.0000 | ❌ |
| 914 | When is Sky going to introduce UHD broadcasts? | 2016 | Sky will introduce UHD broadcasts later in 2016 | -0.0445 | ❌ |
| 915 | When are the new Sky Q products going to be availa... | 2016 | In 2016 | -0.4548 | ❌ |
| 916 | What is the name of Sky Q's dial-up router? | NO ANSWER | NO ANSWER | 0.3406 | ✅ |
| 917 | What are the Sky Q mini set top boxes never able t... | NO ANSWER | the Sky Q Silver set top boxes | -0.0990 | ❌ |
| 918 | What does disconnecting different Sky Q boxes enab... | NO ANSWER | allows all set top boxes in a household to share recordings and other | 0.0000 | ❌ |
| 919 | What set top box can no longer display UHD broadca... | NO ANSWER | Sky Q Mini | -0.3363 | ❌ |
| 920 | What are BSkyB's standard definition broadcasts co... | DVB-compliant MPEG-2 | DVB | 0.0000 | ❌ |
| 921 | Sky Movies and Sky Box office also include what op... | Dolby Digital | DVB-compliant MPEG-2, with the Sky Movies and | 0.0000 | ❌ |
| 922 | What is Sky+ HD material broadcast using? | MPEG-4 | MPG-4 | 0.0000 | ❌ |
| 923 | What is the proprietary system that Sky+HD uses? | OpenTV | The proprietary system is OpenTV | 0.0000 | ❌ |
| 924 | What does most of the HD material use as a standar... | DVB-S2 | DVB-S2 | 0.0000 | ✅ |
| 925 | What box is required to view MPEG-3? | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 926 | What is the proprietary system that Sky+HD can't u... | NO ANSWER | NO ANSWER | 0.0561 | ✅ |
| 927 | What channel never used looping video streams? | NO ANSWER | NO ANSWER | 0.8078 | ✅ |
| 928 | What kind of soundtracks are mandatory with the Sk... | NO ANSWER | NO ANSWER | 0.1992 | ✅ |
| 929 | When was Sky Digital launched? | 1998 | 1998 | -1.0000 | ✅ |
| 930 | What satellite was used when Sky digital was launc... | Astra 2A | Astra 2A | -1.0000 | ✅ |
| 931 | What satellite enabled Sky Digital to launch an al... | Eutelsat's Eurobird 1 | Astra 2A | -0.5470 | ❌ |
| 932 | How many television and radio channels could the n... | hundreds | hundreds | 0.0000 | ✅ |
| 933 | What is the position of the satellite that allowed... | 28.5°E | 28.5°E | -1.0000 | ✅ |
| 934 | What service used Astra 2A in 1995? | NO ANSWER | NO ANSWER | 0.6216 | ✅ |
| 935 | What satellite made it impossible for Sky Digital ... | NO ANSWER | NO ANSWER | 0.3470 | ✅ |
| 936 | How many television and radio channels did the dig... | NO ANSWER | NO ANSWER | 0.0173 | ✅ |
| 937 | When was the only satellite launched? | NO ANSWER | NO ANSWER | 0.6365 | ✅ |
| 938 | When did BSkyB launch it's HDTV service? | 22 May 2006 | 22 May 2006 | -0.9559 | ✅ |
| 939 | How many people were registered to receive the HD ... | 40,000 | 40,000 | -1.0000 | ✅ |
| 940 | What was the name of the set top box manufacturer ... | Thomson | Th Thomson | 0.0000 | ❌ |
| 941 | What was the number of customers that the BBC  rep... | 17,000 | 17,000 | -1.0000 | ✅ |
| 942 | What was the total number of homes Sky announced t... | 4,222,000 | 4,222,000 | -1.0000 | ✅ |
| 943 | When did BSkyB fail launching it's HDTV service? | NO ANSWER | NO ANSWER | 0.4118 | ✅ |
| 944 | Which manufacturer never had supply issues when de... | NO ANSWER | NO ANSWER | 0.9064 | ✅ |
| 945 | How many people never registered to receive the HD... | NO ANSWER | 10,000 | -0.3531 | ❌ |
| 946 | Who reported that 17,000 customers received the se... | NO ANSWER | The BBC | 0.0000 | ❌ |
| 947 | When did Sky announce the total number of homes wi... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 948 | When did BSkyB announce it's intention to replace ... | 8 February 2007 | On 8 February 2007 | -1.0000 | ❌ |
| 949 | When did Setanta Sports say it would launch as a s... | March | March | 0.0000 | ✅ |
| 950 | What platform was Sentanta Sports planning on laun... | digital terrestrial | Digital terrestrial platform | -0.0151 | ❌ |
| 951 | What were NTL's services rebranded as? | Virgin Media | Virgin Media | 0.0000 | ✅ |
| 952 | What does BSkyB's sport portfolio include? | English Premier League Football | English Premier League Football | 0.0000 | ✅ |
| 953 | When did BSkyB announce it's intention to improve ... | NO ANSWER | On 8 February 2007 | -1.0000 | ❌ |
| 954 | When did Setanta Sports say it would launch as a f... | NO ANSWER | NO ANSWER | 0.1893 | ✅ |
| 955 | What platform was Sentanta Sports planning to avoi... | NO ANSWER | NO ANSWER | 0.0504 | ✅ |
| 956 | What was Virgin Media rebranded as? | NO ANSWER | NTB | 0.0000 | ❌ |
| 957 | What channel lost advertising revenue due to their... | NO ANSWER | NO ANSWER | 0.2650 | ✅ |
| 958 | What are free-to-air encrypted broadcasts known as... | free-to-view | free-to-view | 0.0000 | ✅ |
| 959 | What do some encrypted broadcasts require to view? | monthly subscription | monthly subscription | 0.0000 | ✅ |
| 960 | What does a receiver have to be equipped with to v... | VideoGuard UK | VideoGuard UK | 0.0000 | ✅ |
| 961 | What is the universal band that digital recievers ... | Ku band | 9.75/10.600 GHz | -0.4298 | ❌ |
| 962 | What service is a VideoGuard UK equipped receiver ... | Sky | The Sky service | 0.0000 | ❌ |
| 963 | What do encrypted broadcasts never require? | NO ANSWER | NO ANSWER | 0.0338 | ✅ |
| 964 | What does a receiver have to be equipped with to v... | NO ANSWER | NO ANSWER | 0.2735 | ✅ |
| 965 | What is the localized band that digital receivers ... | NO ANSWER | 9.75/10.600 GHz | -0.3293 | ❌ |
| 966 | What service is a VideoGuard UK equipped receiver ... | NO ANSWER | It cannot be used to decrypt other services | 0.0000 | ❌ |
| 967 | What band is fitted in the middle of the satellite... | NO ANSWER | 10.600 GHz | -0.2833 | ❌ |
| 968 | When were the talks held for braodcast right to th... | 1991 | In the autumn of 1991 | -0.4041 | ❌ |
| 969 | Who were the current rights holders for the Primer... | ITV | IT ITV | 0.0000 | ❌ |
| 970 | What did ITV increase their yearly offer for contr... | £34m | £34m | 0.0000 | ✅ |
| 971 | Who was given the highlights of most of the matche... | BBC | The BBC | 0.0000 | ❌ |
| 972 | How much was BSkyB going to pay for the Primier Le... | £304m | £304m | -0.0492 | ✅ |
| 973 | What company was not concerned about retaining new... | NO ANSWER | NO ANSWER | 0.6612 | ✅ |
| 974 | How much did BSkyB pay to give up their rights for... | NO ANSWER | 304m | 0.0033 | ❌ |
| 975 |  Who never saw highlights of most of the matches? | NO ANSWER | IT was ITV | -0.0123 | ❌ |
| 976 | Who were never rights holders for the Premier Leag... | NO ANSWER | NO ANSWER | 0.2481 | ✅ |
| 977 | Who does BSkyB have an operating license from? | Ofcom | Ofcom | 0.0000 | ✅ |
| 978 | what is the fee range for accessing BSkyB's EPG? | £15–100,000 | £15–100,000 | 0.0000 | ✅ |
| 979 | Can BSkyB veto the presence of channels on their E... | no | NO ANSWER | 1.0000 | ❌ |
| 980 | Does BSkyB carry any control over a channels conte... | not | NO ANSWER | 0.8893 | ❌ |
| 981 | Does BSkyB carry any control over the picture qual... | not | NO ANSWER | 0.8383 | ❌ |
| 982 | Who took away the operating license from BSkyB? | NO ANSWER | Ofcom | 0.0000 | ❌ |
| 983 | What company has veto over the presence of channel... | NO ANSWER | NO ANSWER | 0.3066 | ✅ |
| 984 | What can BSkyB veto the presence of channels on? | NO ANSWER | NO ANSWER | 0.3573 | ✅ |
| 985 | What service doesn't require a fee to use? | NO ANSWER | NO ANSWER | 0.0333 | ✅ |
| 986 | When was BSkyB's digital service launched? | 1 October 1998 | 1 October 1998 | -1.0000 | ✅ |
| 987 | What was the name of BSkyB's digital service launc... | Sky Digital | Sky Digital | 0.0000 | ✅ |
| 988 | What did BSkyB name their interactive service? | Sky Active | Open | 0.0000 | ❌ |
| 989 | Who did BSkyB compete with initially? | ONdigital | BSkyB competed with ONdigital (later ITV Digital) terrestrial | -0.2201 | ❌ |
| 990 | Within the 30 days how many digiboxes had been sol... | 100,000 | 100,000 | -0.6479 | ✅ |
| 991 | When was BSkyB's digital service unofficially laun... | NO ANSWER | NO ANSWER | 0.2291 | ✅ |
| 992 | What company supported BSkyB the most? | NO ANSWER | NO ANSWER | 0.4384 | ✅ |
| 993 | Within 30 days how many digiboxes had been discard... | NO ANSWER | NO ANSWER | 1.0000 | ✅ |
| 994 | When did BSkyB decide to stop giving away free dig... | NO ANSWER | NO ANSWER | 0.8621 | ✅ |
| 995 | When was virgin media rebranded from NTL Telewest? | 2007 | 2007 | -1.0000 | ✅ |
| 996 | what was NTL Telewest re-branded to in 2007? | Virgin Media | Virgin Media | -1.0000 | ✅ |
| 997 | What did Virgin Media concentrate on instead of of... | Video On Demand | Video On Demand service | -0.0271 | ❌ |
| 998 | What was the one linear HD channel Virgin Media ca... | BBC HD | BBC HD | 0.0000 | ✅ |
| 999 | what was the name of the other HD channel Virgin m... | Channel 4 HD | Channel 4 HD | 0.0000 | ✅ |

**correct binary classification:** 71.30% (713/1000)

============================================================
Trial: full_data_set_202602171357
============================================================
Overall EM:        55.40
Overall F1:        62.15
NoAns Accuracy:    58.69% (287/489)
HasAns F1:         65.47
HasAns EM:         52.25
Total Questions:   1000 (HasAns: 511, NoAns: 489)
correct binary classification: 71.30% (713/1000)
============================================================

Detailed Metrics:
('exact', 55.4)
('f1', 62.153)
('total', 1000)
('HasAns_exact', 52.25)
('HasAns_f1', 65.466)
('HasAns_total', 511)
('NoAns_exact', 58.691)
('NoAns_f1', 58.691)
('NoAns_total', 489)
('best_exact', 55.4)
('best_exact_thresh', 0.0)
('best_f1', 62.153)
('best_f1_thresh', 0.0)

---