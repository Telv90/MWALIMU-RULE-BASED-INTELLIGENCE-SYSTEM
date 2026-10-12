# MWALIMU RULE BASED INTELLIGENCE SYSTEM
## Use case Diagram
It a visual representation that shows how the use interacts with the system.
```mermaid
flowchart LR
Learner -->Register
Learner -->ChooseSubject
Learner -->AttemptQuizes
Learner -->ViewScores
Learner -->ViewProgress

Teacher -->ViewProgress

Register -->StoreProfiles
AttemptQuizes -->EvaluateAnswer
EvaluateAnswer -->UpdatePerformance
