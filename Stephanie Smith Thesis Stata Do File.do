** Do File for Stephanie Smith Thesis Submission May 2020 **
** Used GAGE Merged Dataset **

** Set controls and Drawing Indicator list **
global covariates age female hhsize years_in_jordan
global characteristics LackofDetails FocusonSymbolsMem LackofConcern MonsterPictures AggressiveFigure PoliticalSlogans DrawninDarkColors DrawninSingleColor MultipleFiguresDrawn SymbolofDespair FigureDrawn DrawninLight SymbolofHope


** Dependent Variable: Psychological Distress **

* 10 Fold Cross Validation, Covariates not penalized
cvlasso cr_ghq12_binary $covariates $characteristics, notpen($covariates) seed(123)
cvlasso, lopt


** Dependent Variable: PTSD **

* 10 Fold Cross Validation, Covariates not penalized
cvlasso af_trauma_PTSD $covariates $characteristics, notpen($covariates) seed(123)
cvlasso, lopt


** Dependent Variable: Exposure to Violence **

* 10 Fold Cross Validation, Covariates not penalized
cvlasso high_violence $covariates $characteristics, notpen($covariates) seed(123)
cvlasso, lopt


** Create Indices for Psychological Distress and PTSD **
* PTSD
pca LackofDetails FocusonSymbolsMem LackofConcern MonsterPictures AggressiveFigure PoliticalSlogans MultipleFiguresDrawn
rotate
predict pa_PTSD

* Psychological Distress
pca DrawninDarkColors DrawninSingleColor SymbolofDespair FigureDrawn DrawninLight SymbolofHope
rotate
predict pa_distress


** Create standardized variables of questionnaire scores **
*GHQ-12
egen cr_ghq12_std= std(cr_ghq12)
*HTQ
egen af_trauma_std= std(af_trauma)

** Correlation between Drawings and Questionnaires
*Drawings & GHQ-12 - Psychological Distress
reg cr_ghq12_std pa_distress age female hhsize years_in_jordan

*Drawings & HTQ - PTSD
reg af_trauma_std pa_PTSD age female hhsize years_in_jordan
